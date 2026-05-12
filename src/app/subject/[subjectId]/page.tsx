'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { getSubject, gradeOrdinal } from '@/lib/subjects'
import SubjectIcon from '@/components/SubjectIcon'
import { getGradeContent } from '@/lib/content'
import { getActiveStudent, getProgress, getSelectedGrade, StudentProfile } from '@/lib/auth'

type ChallengeStars = { yellow: boolean; green: boolean; blue: boolean }

function getChallengeStars(studentId: string, unitId: string): ChallengeStars {
  try {
    const raw = localStorage.getItem(`challenge_${studentId}_${unitId}`)
    return raw ? JSON.parse(raw) : { yellow: false, green: false, blue: false }
  } catch { return { yellow: false, green: false, blue: false } }
}

export default function SubjectPage() {
  const router = useRouter()
  const params = useParams()
  const subjectId = params.subjectId as string
  const subject = getSubject(subjectId)
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [lessonStars, setLessonStars] = useState<Record<string, number>>({})
  const [challengeStars, setChallengeStars] = useState<Record<string, ChallengeStars>>({})

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
    const gradeContent = getGradeContent(getSelectedGrade())
    const units = gradeContent[subjectId] || []
    const map: Record<string, ChallengeStars> = {}
    units.forEach(u => {
      if (u.lessons.some(l => l.isChallenge)) {
        map[u.id] = getChallengeStars(student.id, u.id)
      }
    })
    setChallengeStars(map)
  }, [student, subjectId])

  if (!subject || !student) return null

  const gradeContent = getGradeContent(getSelectedGrade())
  const units = gradeContent[subjectId] || []
  const regularLessons = units.flatMap(u => u.lessons.filter(l => !l.isChallenge))
  const totalStars = regularLessons.reduce((s, l) => s + (lessonStars[l.id] || 0), 0)
  const maxStars = regularLessons.length * 3

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center gap-3" style={{ background: subject.color }}>
        <button onClick={() => { window.location.href = '/dashboard' }}
          className="text-white/80 hover:text-white text-2xl font-bold transition-colors">←</button>
        <SubjectIcon subject={subject} size="md" />
        <div className="flex-1">
          <div className="text-white font-black text-xl">{subject.nameMk}</div>
          <div className="text-white/70 text-sm">{subject.world}</div>
        </div>
        <div className="text-right">
          <div className="text-white font-black">⭐ {totalStars}</div>
          <div className="text-white/60 text-xs">/ {maxStars} ѕвезди</div>
        </div>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8">
        <h2 className="text-2xl font-black mb-6" style={{ color: '#1A1A2E' }}>
          Единици за {student.grade}-{gradeOrdinal(student.grade)} одделение
        </h2>

        <div className="grid gap-4">
          {units.map((unit, unitIdx) => {
            const regularLessons = unit.lessons.filter(l => !l.isChallenge)
            const challengeLesson = unit.lessons.find(l => l.isChallenge)
            const unitStars = regularLessons.reduce((s, l) => s + (lessonStars[l.id] || 0), 0)
            const unitMax = regularLessons.length * 3
            const unitDone = regularLessons.filter(l => (lessonStars[l.id] || 0) > 0).length
            const allLessonsDone = unitDone === regularLessons.length
            const cStars = challengeStars[unit.id] || { yellow: false, green: false, blue: false }

            return (
              <div key={unit.id} className="bg-white rounded-3xl p-5 shadow-sm">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-10 h-10 rounded-full flex items-center justify-center font-black text-white text-lg"
                    style={{ background: subject.color }}>
                    {unitIdx + 1}
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-black" style={{ color: '#1A1A2E' }}>{unit.title}</h3>
                    <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>
                      {unitDone}/{regularLessons.length} лекции · ⭐ {unitStars}/{unitMax}
                    </p>
                  </div>
                  {allLessonsDone && !challengeLesson && (
                    <span className="text-xl">✅</span>
                  )}
                </div>

                <div className="grid gap-2">
                  {regularLessons.map((lesson) => {
                    const stars = lessonStars[lesson.id] || 0
                    const done = stars > 0

                    return (
                      <button key={lesson.id}
                        onClick={() => router.push(`/lesson/${lesson.id}`)}
                        className="w-full flex items-center justify-between p-3 rounded-2xl transition-all duration-200 hover:scale-[1.01] active:scale-[0.99]"
                        style={{
                          background: lesson.isTest
                            ? done ? '#FFF8E8' : '#FFFDF5'
                            : done ? `${subject.color}15` : subject.bgColor,
                          border: lesson.isTest
                            ? `1.5px solid ${done ? '#F0A500' : '#FFE082'}`
                            : done ? `1.5px solid ${subject.color}40` : '1.5px solid transparent',
                          cursor: 'pointer',
                        }}>
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-black flex-shrink-0"
                            style={{
                              background: lesson.isTest ? (done ? '#F0A500' : '#FFE082') : subject.color,
                              color: lesson.isTest ? (done ? 'white' : '#7A5800') : 'white',
                            }}>
                            {lesson.isTest ? (done ? '✓' : '📝') : done ? '✓' : '▶'}
                          </div>
                          <span className="font-bold text-sm text-left" style={{ color: '#1A1A2E' }}>
                            {lesson.title}
                          </span>
                          {lesson.isTest && (
                            <span className="text-xs font-black px-2 py-0.5 rounded-full"
                              style={{ background: '#FFE082', color: '#7A5800' }}>ТЕСТ</span>
                          )}
                        </div>
                        <div className="flex gap-0.5 flex-shrink-0">
                          {[1, 2, 3].map((s) => (
                            <span key={s} className="text-sm transition-colors"
                              style={{ color: s <= stars ? '#FFD93D' : '#D1D5DB' }}>★</span>
                          ))}
                        </div>
                      </button>
                    )
                  })}
                </div>

                {/* Challenge block */}
                {challengeLesson && (
                  <div className="mt-3">
                    <div className="h-px mb-3" style={{ background: '#F0F0F5' }} />
                    <button
                      onClick={() => router.push(`/challenge/${unit.id}`)}
                      className="w-full flex items-center justify-between p-4 rounded-2xl transition-all duration-200 hover:scale-[1.01] active:scale-[0.99]"
                      style={{
                        background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)',
                        border: '2px solid #5C35D4',
                      }}>
                      <div className="flex items-center gap-3">
                        <div className="w-9 h-9 rounded-full flex items-center justify-center text-lg flex-shrink-0"
                          style={{ background: '#5C35D4' }}>
                          🏆
                        </div>
                        <div className="text-left">
                          <span className="font-black text-sm block" style={{ color: 'white' }}>
                            Предизвик
                          </span>
                          <span className="text-xs font-semibold" style={{ color: 'rgba(255,255,255,0.6)' }}>
                            Освои ѕвезди по тежина
                          </span>
                        </div>
                      </div>
                      <div className="flex gap-1.5 flex-shrink-0">
                        {[
                          { color: '#FFD93D', earned: cStars.yellow },
                          { color: '#4CAF50', earned: cStars.green  },
                          { color: '#2196F3', earned: cStars.blue   },
                        ].map(({ color, earned }) => (
                          <span key={color} className="text-xl transition-all"
                            style={{ color, opacity: earned ? 1 : 0.25 }}>
                            ★
                          </span>
                        ))}
                      </div>
                    </button>
                  </div>
                )}
              </div>
            )
          })}
        </div>
      </div>
    </main>
  )
}
