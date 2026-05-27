'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { getSubject } from '@/lib/subjects'
import SubjectIcon from '@/components/SubjectIcon'
import { getGradeContent } from '@/lib/content'
import { getActiveStudent, getProgress, getSelectedGrade, StudentProfile } from '@/lib/auth'
import LevelMap, { MapNode } from '@/components/LevelMap'
import { UnitData } from '@/lib/content'

type ChallengeStars = { yellow: boolean; green: boolean; blue: boolean }

function getChallengeStars(studentId: string, unitId: string): ChallengeStars {
  try {
    const raw = localStorage.getItem(`challenge_${studentId}_${unitId}`)
    return raw ? JSON.parse(raw) : { yellow: false, green: false, blue: false }
  } catch { return { yellow: false, green: false, blue: false } }
}

function buildMapNodes(
  units: UnitData[],
  lessonStars: Record<string, number>,
  challengeStarsMap: Record<string, ChallengeStars>,
  grade: number
): MapNode[] {
  const playMode = false
  const nodes: MapNode[] = []
  let lessonCount = 0
  let prevBlockerDone = true  // tracks if the last lesson/boss was completed

  for (let ui = 0; ui < units.length; ui++) {
    const unit = units[ui]
    const regularLessons = unit.lessons.filter(l => !l.isChallenge)
    const challengeLesson = unit.lessons.find(l => l.isChallenge)
    const unitFirstIdx = nodes.length  // index where this unit's first node will be

    for (let li = 0; li < regularLessons.length; li++) {
      const lesson = regularLessons[li]
      const stars = lessonStars[lesson.id] || 0
      const locked = !playMode && !prevBlockerDone

      nodes.push({
        id: lesson.id,
        title: lesson.title,
        type: 'lesson',
        lessonId: lesson.id,
        unitTitle: li === 0 ? unit.title : undefined,  // show unit title above first node only
        stars,
        locked,
      })

      prevBlockerDone = playMode || stars > 0
      lessonCount++

      // Small gift after every 3 completed lessons
      if (lessonCount % 3 === 0) {
        nodes.push({
          id: `gift-${lessonCount}`,
          title: 'Награда!',
          type: 'gift',
          stars: 0,
          locked: !playMode && !prevBlockerDone,
        })
      }
    }

    // Boss / challenge level at end of each unit
    if (challengeLesson) {
      const cStars = challengeStarsMap[unit.id] || { yellow: false, green: false, blue: false }
      const bossStars = [cStars.yellow, cStars.green, cStars.blue].filter(Boolean).length
      const allUnitDone = regularLessons.every(l => (lessonStars[l.id] || 0) > 0)
      const locked = !playMode && !allUnitDone

      nodes.push({
        id: `boss-${unit.id}`,
        title: 'Предизвик',
        type: 'boss',
        unitId: unit.id,
        stars: bossStars,
        locked,
      })

      prevBlockerDone = playMode || bossStars > 0
    }
  }

  return nodes
}

export default function SubjectPage() {
  const router = useRouter()
  const params = useParams()
  const subjectId = params.subjectId as string
  const subject = getSubject(subjectId)
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [lessonStars, setLessonStars] = useState<Record<string, number>>({})
  const [challengeStarsMap, setChallengeStarsMap] = useState<Record<string, ChallengeStars>>({})
  const [nodes, setNodes] = useState<MapNode[]>([])

  useEffect(() => {
    const active = getActiveStudent()
    if (!active) { router.push('/'); return }
    setStudent(active)
    getProgress(active.id).then((records) => {
      const map: Record<string, number> = {}
      records.forEach((r) => { map[r.lesson_id] = r.stars_earned })
      setLessonStars(map)
    })
  }, [router])

  useEffect(() => {
    if (!student) return
    const grade = getSelectedGrade()
    const gradeContent = getGradeContent(grade)
    const units: UnitData[] = gradeContent[subjectId] || []

    const cMap: Record<string, ChallengeStars> = {}
    units.forEach(u => {
      if (u.lessons.some(l => l.isChallenge)) {
        cMap[u.id] = getChallengeStars(student.id, u.id)
      }
    })
    setChallengeStarsMap(cMap)

    const built = buildMapNodes(units, lessonStars, cMap, grade)
    setNodes(built)
  }, [student, subjectId, lessonStars])

  if (!subject || !student) return null

  const grade = getSelectedGrade()
  const gradeContent = getGradeContent(grade)
  const units: UnitData[] = gradeContent[subjectId] || []
  const regularLessons = units.flatMap(u => u.lessons.filter(l => !l.isChallenge))
  const totalStars = regularLessons.reduce((s, l) => s + (lessonStars[l.id] || 0), 0)
  const maxStars = regularLessons.length * 3

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header
        className="px-6 py-4 flex items-center gap-3"
        style={{ background: subject.color }}
      >
        <button
          onClick={() => { window.location.href = '/dashboard' }}
          className="text-white/80 hover:text-white text-2xl font-bold transition-colors"
        >
          ←
        </button>
        <SubjectIcon subject={subject} size="md" />
        <div className="flex-1">
          <div className="text-white font-black text-xl">{subject.nameMk}</div>
          <div className="text-white/70 text-sm">{subject.world}</div>
        </div>
        <div className="text-right">
          <div className="text-white font-black">⭐ {totalStars}</div>
          <div className="text-white/60 text-xs">/ {maxStars}</div>
        </div>
      </header>

      {/* Grade band badge */}
      <div className="px-6 py-3 flex items-center gap-2"
        style={{ background: `${subject.color}15`, borderBottom: `1px solid ${subject.color}20` }}>
        <span className="text-xs font-black px-3 py-1 rounded-full"
          style={{ background: subject.color, color: 'white' }}>
          {grade <= 4 ? '🎮 Режим на игра' : '⚔️ Режим на предизвик'}
        </span>
        <span className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>
          Заврши лекција за да ја отклучиш следната
        </span>
      </div>

      <div className="max-w-lg mx-auto px-4 py-6">
        {nodes.length === 0 ? (
          <div className="text-center py-20" style={{ color: '#9B9BAA' }}>
            <div className="text-5xl mb-4">📚</div>
            <p className="font-bold">Нема содржина за овој предмет сè уште.</p>
          </div>
        ) : (
          <LevelMap nodes={nodes} subject={subject} />
        )}
      </div>
    </main>
  )
}
