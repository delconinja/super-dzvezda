import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase-server'
import { evaluateNewBadges, BadgeStats } from '@/lib/badges'
import { getGradeContent } from '@/lib/content'

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null)
  if (!body) return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 })

  const { studentId, unitId, yellow, green, blue } = body
  if (!studentId || !unitId) return NextResponse.json({ error: 'Missing fields' }, { status: 400 })

  const sb = createServiceClient()

  try {
    // Load student to get grade + streak
    const { data: student } = await sb.from('students').select('*').eq('id', studentId).single()
    if (!student) return NextResponse.json({ error: 'Student not found' }, { status: 404 })

    // Get previous stars for this unit (to detect retry + new star)
    const { data: prev } = await sb
      .from('challenge_stars')
      .select('yellow, green, blue, attempts')
      .eq('student_id', studentId).eq('unit_id', unitId).maybeSingle()

    const isRetry = !!prev
    const gainedNewStar =
      (yellow && !prev?.yellow) ||
      (green  && !prev?.green)  ||
      (blue   && !prev?.blue)

    // Upsert — never downgrade stars, always increment attempts
    const newAttempts = (prev?.attempts ?? 0) + 1
    await sb.from('challenge_stars').upsert({
      student_id: studentId,
      unit_id:    unitId,
      yellow: prev?.yellow || yellow,
      green:  prev?.green  || green,
      blue:   prev?.blue   || blue,
      attempts:   newAttempts,
      updated_at: new Date().toISOString(),
    }, { onConflict: 'student_id,unit_id' })

    // Aggregate all challenge stars for badge engine
    const { data: allStars } = await sb
      .from('challenge_stars')
      .select('unit_id, yellow, green, blue')
      .eq('student_id', studentId)

    const stars = allStars || []
    const totalYellowStars = stars.filter(s => s.yellow).length
    const totalGreenStars  = stars.filter(s => s.green).length
    const totalBlueStars   = stars.filter(s => s.blue).length
    const completedUnitIds = stars.filter(s => s.yellow).map(s => s.unit_id)

    // Lesson count
    const { data: progressRows } = await sb
      .from('progress').select('lesson_id, stars_earned')
      .eq('student_id', studentId)
    const totalLessons = (progressRows || []).filter(p => p.stars_earned > 0).length

    // Subjects studied (from progress lesson IDs → subject lookup via grade content)
    const gradeContent = getGradeContent(student.grade)
    const lessonSubjectMap: Record<string, string> = {}
    const unitsBySubject: Record<string, string[]> = {}
    Object.entries(gradeContent).forEach(([subjectId, units]) => {
      unitsBySubject[subjectId] = units
        .filter(u => u.lessons.some(l => l.isChallenge !== true))
        .map(u => u.id)
      units.forEach(u => u.lessons.forEach(l => {
        lessonSubjectMap[l.id] = subjectId
      }))
    })
    const studiedSubjectSet = new Set<string>()
    ;(progressRows || []).forEach(p => {
      const sid = lessonSubjectMap[p.lesson_id]
      if (sid) studiedSubjectSet.add(sid)
    })

    // Already earned badges
    const { data: earnedRows } = await sb
      .from('user_badges').select('badge_id').eq('student_id', studentId)
    const earnedBadgeIds = (earnedRows || []).map(r => r.badge_id)

    const stats: BadgeStats = {
      event: 'challenge_complete',
      unitId,
      earnedYellow: prev?.yellow || yellow,
      earnedGreen:  prev?.green  || green,
      earnedBlue:   prev?.blue   || blue,
      isRetry,
      gainedNewStar,
      attempts: newAttempts,
      totalLessons,
      totalBlueStars,
      totalGreenStars,
      totalYellowStars,
      streakDays: student.streak ?? 0,
      subjectsStudied: [...studiedSubjectSet],
      completedUnitIds,
      allUnitsBySubject: Object.values(unitsBySubject),
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

    return NextResponse.json({
      yellow: prev?.yellow || yellow,
      green:  prev?.green  || green,
      blue:   prev?.blue   || blue,
      newBadgeIds,
    })
  } catch (e) {
    return NextResponse.json({ error: String(e) }, { status: 500 })
  }
}

export async function GET(req: NextRequest) {
  const studentId = req.nextUrl.searchParams.get('studentId')
  const unitId    = req.nextUrl.searchParams.get('unitId')
  if (!studentId) return NextResponse.json({ error: 'Missing studentId' }, { status: 400 })

  const sb = createServiceClient()

  if (unitId) {
    const { data } = await sb
      .from('challenge_stars')
      .select('yellow, green, blue, attempts')
      .eq('student_id', studentId).eq('unit_id', unitId).maybeSingle()
    return NextResponse.json(data || { yellow: false, green: false, blue: false, attempts: 0 })
  }

  const { data } = await sb
    .from('challenge_stars').select('unit_id, yellow, green, blue')
    .eq('student_id', studentId)
  return NextResponse.json(data || [])
}
