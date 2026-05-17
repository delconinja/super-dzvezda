import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase-server'
import { evaluateNewBadges, BadgeStats } from '@/lib/badges'

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null)
  if (!body) return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 })

  const { studentId, lessonId, starsEarned } = body

  if (!studentId || typeof studentId !== 'string')
    return NextResponse.json({ error: 'Invalid studentId' }, { status: 400 })
  if (!lessonId || typeof lessonId !== 'string')
    return NextResponse.json({ error: 'Invalid lessonId' }, { status: 400 })
  if (typeof starsEarned !== 'number' || starsEarned < 0 || starsEarned > 3)
    return NextResponse.json({ error: 'Invalid starsEarned' }, { status: 400 })

  const sb = createServiceClient()

  try {
    const { data: existing } = await sb
      .from('progress').select('stars_earned')
      .eq('student_id', studentId).eq('lesson_id', lessonId).single()

    if (!existing || starsEarned >= existing.stars_earned) {
      const { error } = await sb.from('progress').upsert({
        student_id: studentId, lesson_id: lessonId,
        stars_earned: starsEarned, completed: starsEarned > 0,
        completed_at: new Date().toISOString(),
      }, { onConflict: 'student_id,lesson_id' })
      if (error) return NextResponse.json({ error: error.message }, { status: 500 })
    }

    const { data: all } = await sb
      .from('progress').select('stars_earned').eq('student_id', studentId)
    const total = (all || []).reduce((sum: number, r: { stars_earned: number }) => sum + r.stars_earned, 0)

    await sb.from('students').update({ stars_total: total }).eq('id', studentId)

    if (starsEarned > 0) await updateStreak(sb, studentId)

    const { data: student } = await sb.from('students').select('*').eq('id', studentId).single()

    const newBadgeIds = starsEarned > 0
      ? await checkLessonBadges(sb, studentId, student)
      : []

    return NextResponse.json({ starsTotal: total, student, newBadgeIds })
  } catch (e) {
    return NextResponse.json({ error: String(e) }, { status: 500 })
  }
}

type ServiceClient = ReturnType<typeof createServiceClient>

async function checkLessonBadges(sb: ServiceClient, studentId: string, student: { grade: number; streak: number } | null): Promise<string[]> {
  try {
    const { data: progressRows } = await sb
      .from('progress').select('lesson_id, stars_earned').eq('student_id', studentId)
    const totalLessons = (progressRows || []).filter(p => p.stars_earned > 0).length

    // Subject/unit mapping skipped here to avoid importing the large content module
    // in a serverless function. Badge types that need it receive empty arrays.
    const studiedSubjectSet = new Set<string>()

    const { data: starRows } = await sb
      .from('challenge_stars').select('unit_id, yellow, green, blue').eq('student_id', studentId)
    const completedUnitIds = (starRows || []).filter(s => s.yellow).map(s => s.unit_id)

    const { data: earnedRows } = await sb
      .from('user_badges').select('badge_id').eq('student_id', studentId)
    const earnedBadgeIds = (earnedRows || []).map(r => r.badge_id)

    const stats: BadgeStats = {
      event: 'lesson_complete',
      totalLessons,
      totalBlueStars:   (starRows || []).filter(s => s.blue).length,
      totalGreenStars:  (starRows || []).filter(s => s.green).length,
      totalYellowStars: (starRows || []).filter(s => s.yellow).length,
      streakDays: student?.streak ?? 0,
      subjectsStudied: [...studiedSubjectSet],
      completedUnitIds,
      allUnitsBySubject: [],
    }

    const newBadgeIds = evaluateNewBadges(stats, earnedBadgeIds)
    if (newBadgeIds.length > 0) {
      await sb.from('user_badges').insert(
        newBadgeIds.map(badge_id => ({
          student_id: studentId,
          badge_id,
          earned_at: new Date().toISOString(),
        }))
      )
    }
    return newBadgeIds
  } catch { return [] }
}

async function updateStreak(sb: ServiceClient, studentId: string) {
  try {
    const { data: records } = await sb
      .from('progress').select('completed_at')
      .eq('student_id', studentId).eq('completed', true)
    if (!records?.length) {
      await sb.from('students').update({ streak: 1 }).eq('id', studentId)
      return
    }
    const dates = new Set(records.map((r: { completed_at: string }) => r.completed_at.slice(0, 10)))
    let streak = 0
    const today = new Date()
    for (let i = 0; i < 365; i++) {
      const d = new Date(today)
      d.setDate(d.getDate() - i)
      if (dates.has(d.toISOString().slice(0, 10))) streak++
      else break
    }
    await sb.from('students').update({ streak: Math.max(1, streak) }).eq('id', studentId)
  } catch { /* silent */ }
}
