import { supabase } from './supabase'
import { getAffiliateRef, clearAffiliateRef } from './affiliate'

export interface StudentProfile {
  id: string
  parent_id: string
  name: string
  grade: number
  pin: string
  stars_total: number
  streak: number
  town: string | null
  school: string | null
}

export type SubscriptionPlan =
  | 'trial'
  | 'individual'
  | 'individual_annual'
  | 'family'
  | 'family_annual'
  | 'school'

export interface Subscription {
  status: 'trial' | 'active' | 'expired' | 'cancelled'
  plan: SubscriptionPlan
  price_paid: number
  max_students: number
  billing: 'monthly' | 'annual'
  trial_ends_at: string
  subscribed_until: string | null
}

export const PLANS = {
  school: { label: 'Училиште/Клас', price: 80, annual: 800, maxStudents: 35 },
} as const

export function familyMonthlyEur(kids: number) {
  return kids <= 1 ? 10 : 15
}

export function familyMonthlyMkd(kids: number) {
  return kids <= 1 ? 600 : 900
}

export function familyAnnualEur(kids: number) {
  return familyMonthlyEur(kids) * 10
}

export function familyAnnualMkd(kids: number) {
  return familyMonthlyMkd(kids) * 10
}

export interface FamilySession {
  parentId: string
  students: StudentProfile[]
}

// ── FAMILY SESSION (localStorage) ────────────────────────────────
export function getFamilySession(): FamilySession | null {
  if (typeof window === 'undefined') return null
  try { return JSON.parse(localStorage.getItem('family_session') || 'null') } catch { return null }
}

function saveFamilySession(parentId: string, students: StudentProfile[]) {
  localStorage.setItem('family_session', JSON.stringify({ parentId, students }))
}

export function clearFamilySession() {
  localStorage.removeItem('family_session')
  localStorage.removeItem('active_student')
}

// ── ACTIVE STUDENT ────────────────────────────────────────────────
export function getActiveStudent(): StudentProfile | null {
  if (typeof window === 'undefined') return null
  try { return JSON.parse(localStorage.getItem('active_student') || 'null') } catch { return null }
}

export function setActiveStudent(student: StudentProfile) {
  localStorage.setItem('active_student', JSON.stringify(student))
}

export function clearActiveStudent() {
  localStorage.removeItem('active_student')
}

// ── PIN LOGIN (local — fast, no API call) ─────────────────────────
export function loginWithPin(
  student: StudentProfile,
  pin: string
): { ok: boolean; error?: string } {
  if (student.pin !== pin) return { ok: false, error: 'Погрешен PIN. Обиди се пак! 🔑' }
  setActiveStudent(student)
  return { ok: true }
}

// ── PARENT REGISTER ──────────────────────────────────────────────
export async function register(data: {
  email: string
  password: string
  parentName: string
  studentName: string
  grade: number
  pin: string
  town?: string
  school?: string
}): Promise<{ ok: boolean; error?: string }> {
  try {
    const { data: authData, error: authError } = await supabase.auth.signUp({
      email: data.email,
      password: data.password,
      options: { data: { full_name: data.parentName } },
    })
    if (authError) return { ok: false, error: authError.message }
    if (!authData.user) return { ok: false, error: 'Регистрацијата не успеа. Обиди се пак.' }

    // Ensure session exists
    if (!authData.session) {
      const { error: signInError } = await supabase.auth.signInWithPassword({
        email: data.email, password: data.password,
      })
      if (signInError) return { ok: false, error: 'Потврди ја е-поштата и обиди се да се логираш.' }
    }

    const userId = authData.user.id

    // Resolve affiliate ref if present
    let affiliateId: string | null = null
    const refCode = getAffiliateRef()
    if (refCode) {
      const { data: aff } = await supabase
        .from('affiliates').select('id').eq('code', refCode).eq('status', 'active').maybeSingle()
      if (aff) { affiliateId = aff.id; clearAffiliateRef() }
    }

    // Create trial subscription
    const trialEnd = new Date(Date.now() + 14 * 24 * 60 * 60 * 1000).toISOString()
    const { error: subError } = await supabase.from('subscriptions').insert({
      parent_id: userId, trial_ends_at: trialEnd, status: 'trial',
      ...(affiliateId ? { affiliate_id: affiliateId } : {}),
    })
    if (subError) return { ok: false, error: 'Грешка при активирање пробен период: ' + subError.message }

    // Create student profile
    const { data: student, error: stuError } = await supabase
      .from('students')
      .insert({
        parent_id: userId, name: data.studentName, grade: data.grade, pin: data.pin,
        town: data.town || null, school: data.school || null,
      })
      .select().single()
    if (stuError) return { ok: false, error: 'Грешка при креирање профил: ' + stuError.message }

    // Save family session so device remembers this family
    saveFamilySession(userId, [student])
    setActiveStudent(student)
    return { ok: true }
  } catch (e: unknown) {
    return { ok: false, error: 'Неочекувана грешка: ' + String(e) }
  }
}

// ── PARENT LOGIN ─────────────────────────────────────────────────
export async function parentLogin(
  email: string,
  password: string
): Promise<{ ok: boolean; error?: string }> {
  try {
    const { error } = await supabase.auth.signInWithPassword({ email, password })
    if (error) return { ok: false, error: 'Погрешна е-пошта или лозинка.' }

    // Fetch students and save family session
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return { ok: false, error: 'Не може да се најде корисник.' }

    const { data: students } = await supabase
      .from('students').select('*').eq('parent_id', user.id)
    saveFamilySession(user.id, students || [])
    return { ok: true }
  } catch (e: unknown) {
    return { ok: false, error: 'Грешка при логирање: ' + String(e) }
  }
}

// ── PARENT LOGOUT ─────────────────────────────────────────────────
export async function parentLogout() {
  clearFamilySession()
  await supabase.auth.signOut()
}

// ── GET STUDENTS FROM DB ──────────────────────────────────────────
export async function getStudents(): Promise<StudentProfile[]> {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return []
    const { data } = await supabase
      .from('students').select('*').eq('parent_id', user.id)
    return data || []
  } catch { return [] }
}

// ── SUBSCRIPTION ─────────────────────────────────────────────────
export async function getSubscription(): Promise<Subscription | null> {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return null
    const { data } = await supabase
      .from('subscriptions').select('*').eq('parent_id', user.id).single()
    return data || null
  } catch { return null }
}

export function trialDaysLeft(sub: Subscription): number {
  if (sub.status === 'active') return 999
  const left = new Date(sub.trial_ends_at).getTime() - Date.now()
  return Math.max(0, Math.ceil(left / (24 * 60 * 60 * 1000)))
}

export function isTrialExpired(sub: Subscription): boolean {
  if (sub.status === 'active') return false
  return trialDaysLeft(sub) <= 0
}

// ── ADD STUDENT ───────────────────────────────────────────────────
export async function addStudent(data: {
  studentName: string
  grade: number
  pin: string
  town?: string
  school?: string
}): Promise<{ ok: boolean; error?: string; student?: StudentProfile }> {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return { ok: false, error: 'Не си најавен.' }

    const { data: existing } = await supabase
      .from('students').select('id').eq('parent_id', user.id)
    if ((existing?.length || 0) >= 3) {
      return { ok: false, error: 'Достигнат е максимумот од 3 деца.' }
    }

    const { data: student, error } = await supabase
      .from('students')
      .insert({
        parent_id: user.id, name: data.studentName, grade: data.grade, pin: data.pin,
        town: data.town || null, school: data.school || null,
      })
      .select().single()
    if (error) return { ok: false, error: 'Грешка при додавање: ' + error.message }

    const session = getFamilySession()
    saveFamilySession(user.id, [...(session?.students || []), student])
    return { ok: true, student }
  } catch (e: unknown) {
    return { ok: false, error: 'Неочекувана грешка: ' + String(e) }
  }
}

// ── PROGRESS ─────────────────────────────────────────────────────
export async function saveProgress(
  studentId: string,
  lessonId: string,
  starsEarned: number,
): Promise<number> {
  try {
    // Only save if score is better than existing (protect high scores on retry)
    const { data: existing } = await supabase
      .from('progress').select('stars_earned')
      .eq('student_id', studentId).eq('lesson_id', lessonId).single()

    if (!existing || starsEarned >= existing.stars_earned) {
      await supabase.from('progress').upsert({
        student_id: studentId, lesson_id: lessonId,
        stars_earned: starsEarned, completed: starsEarned > 0,
        completed_at: new Date().toISOString(),
      }, { onConflict: 'student_id,lesson_id' })
    }

    const { data: all } = await supabase
      .from('progress').select('stars_earned').eq('student_id', studentId)
    const total = (all || []).reduce((sum, r) => sum + r.stars_earned, 0)
    await supabase.from('students').update({ stars_total: total }).eq('id', studentId)
    if (starsEarned > 0) await updateStreak(studentId)
    return total
  } catch (e) {
    console.error('saveProgress error:', e)
    return 0
  }
}

async function updateStreak(studentId: string): Promise<void> {
  try {
    const { data: records } = await supabase
      .from('progress').select('completed_at')
      .eq('student_id', studentId).eq('completed', true)
    if (!records?.length) {
      await supabase.from('students').update({ streak: 1 }).eq('id', studentId)
      return
    }
    const dates = new Set(records.map(r => r.completed_at.slice(0, 10)))
    let streak = 0
    const today = new Date()
    for (let i = 0; i < 365; i++) {
      const d = new Date(today)
      d.setDate(d.getDate() - i)
      if (dates.has(d.toISOString().slice(0, 10))) streak++
      else break
    }
    await supabase.from('students').update({ streak: Math.max(1, streak) }).eq('id', studentId)
  } catch (e) { console.error('updateStreak error:', e) }
}

export async function refreshStudentSession(studentId: string): Promise<void> {
  try {
    const { data: student } = await supabase
      .from('students').select('*').eq('id', studentId).single()
    if (!student) return
    setActiveStudent(student)
    const session = getFamilySession()
    if (session) {
      saveFamilySession(session.parentId, session.students.map(s => s.id === studentId ? student : s))
    }
  } catch { /* silent */ }
}

export async function getProgress(studentId: string) {
  try {
    const { data } = await supabase
      .from('progress').select('*').eq('student_id', studentId)
    return data || []
  } catch { return [] }
}
