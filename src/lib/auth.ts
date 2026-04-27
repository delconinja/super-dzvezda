import { supabase } from './supabase'

export interface StudentProfile {
  id: string
  parent_id: string
  name: string
  grade: number
  pin: string
  stars_total: number
  streak: number
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
  individual:        { label: 'Поединец',       price: 8,   annual: 70,  maxStudents: 1, desc: '1 дете, сите предмети' },
  family:            { label: 'Семеен',          price: 13,  annual: 110, maxStudents: 3, desc: 'До 3 деца' },
  school:            { label: 'Училиште/Клас',   price: 80,  annual: 800, maxStudents: 35, desc: 'До 35 ученици' },
} as const

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

    // Create trial subscription
    const trialEnd = new Date(Date.now() + 14 * 24 * 60 * 60 * 1000).toISOString()
    const { error: subError } = await supabase.from('subscriptions').insert({
      parent_id: userId, trial_ends_at: trialEnd, status: 'trial',
    })
    if (subError) return { ok: false, error: 'Грешка при активирање пробен период: ' + subError.message }

    // Create student profile
    const { data: student, error: stuError } = await supabase
      .from('students')
      .insert({ parent_id: userId, name: data.studentName, grade: data.grade, pin: data.pin })
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

// ── PROGRESS ─────────────────────────────────────────────────────
export async function saveProgress(studentId: string, lessonId: string, starsEarned: number) {
  try {
    await supabase.from('progress').upsert({
      student_id: studentId, lesson_id: lessonId,
      stars_earned: starsEarned, completed: true,
      completed_at: new Date().toISOString(),
    }, { onConflict: 'student_id,lesson_id' })
    const { data: all } = await supabase
      .from('progress').select('stars_earned').eq('student_id', studentId)
    const total = (all || []).reduce((sum, r) => sum + r.stars_earned, 0)
    await supabase.from('students').update({ stars_total: total }).eq('id', studentId)
  } catch (e) { console.error('saveProgress error:', e) }
}

export async function getProgress(studentId: string) {
  try {
    const { data } = await supabase
      .from('progress').select('*').eq('student_id', studentId)
    return data || []
  } catch { return [] }
}
