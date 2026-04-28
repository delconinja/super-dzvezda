'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { getSubject } from '@/lib/subjects'
import { GRADE7_CONTENT } from '@/lib/content'
import { getActiveStudent, getProgress, StudentProfile } from '@/lib/auth'

export default function SubjectPage() {
  const router = useRouter()
  const params = useParams()
  const subjectId = params.subjectId as string
  const subject = getSubject(subjectId)
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [lessonStars, setLessonStars] = useState<Record<string, number>>({})

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

  if (!subject || !student) return null

  const units = GRADE7_CONTENT[subjectId as keyof typeof GRADE7_CONTENT] || []
  const totalStars = units.flatMap(u => u.lessons).reduce((s, l) => s + (lessonStars[l.id] || 0), 0)
  const maxStars = units.flatMap(u => u.lessons).length * 3

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center gap-3" style={{ background: subject.color }}>
        <button onClick={() => router.push('/dashboard')}
          className="text-white/80 hover:text-white text-2xl font-bold transition-colors">←</button>
        <span className="text-3xl">{subject.emoji}</span>
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
          Единици за {student.grade}-то одделение
        </h2>

        <div className="grid gap-4">
          {units.map((unit, unitIdx) => {
            const unitStars = unit.lessons.reduce((s, l) => s + (lessonStars[l.id] || 0), 0)
            const unitMax = unit.lessons.length * 3
            const unitDone = unit.lessons.filter(l => (lessonStars[l.id] || 0) > 0).length

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
                      {unitDone}/{unit.lessons.length} лекции · ⭐ {unitStars}/{unitMax}
                    </p>
                  </div>
                  {unitDone === unit.lessons.length && (
                    <span className="text-xl">✅</span>
                  )}
                </div>

                <div className="grid gap-2">
                  {unit.lessons.map((lesson, lessonIdx) => {
                    const stars = lessonStars[lesson.id] || 0
                    const done = stars > 0

                    return (
                      <button key={lesson.id}
                        onClick={() => router.push(`/lesson/${lesson.id}`)}
                        className="w-full flex items-center justify-between p-3 rounded-2xl transition-all duration-200 hover:scale-[1.01] active:scale-[0.99]"
                        style={{ background: done ? `${subject.color}15` : subject.bgColor, border: done ? `1.5px solid ${subject.color}40` : '1.5px solid transparent' }}>
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-black text-white flex-shrink-0"
                            style={{ background: done ? subject.color : lessonIdx === 0 ? subject.color : '#D1D5DB' }}>
                            {done ? '✓' : lessonIdx === 0 ? '▶' : `${lessonIdx + 1}`}
                          </div>
                          <span className="font-bold text-sm text-left" style={{ color: '#1A1A2E' }}>
                            {lesson.title}
                          </span>
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
              </div>
            )
          })}
        </div>
      </div>
    </main>
  )
}
