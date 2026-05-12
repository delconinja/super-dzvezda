'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { supabase } from '@/lib/supabase'
import { getProgress, StudentProfile } from '@/lib/auth'
import { getSubjectsForGrade } from '@/lib/subjects'
import { getGradeContent } from '@/lib/content'
import { Subject, SubjectCategory } from '@/types'

function gradeLabel(g: number) {
  const suffix = g === 1 ? 'во' : g === 2 ? 'ро' : g === 7 || g === 8 ? 'мо' : 'то'
  return `${g}-${suffix} одделение`
}

function StarRow({ earned, max }: { earned: number; max: number }) {
  return (
    <span className="flex items-center gap-0.5">
      {Array.from({ length: max }).map((_, i) => (
        <span key={i} style={{ color: i < earned ? '#FFD93D' : '#E5E7EB', fontSize: 14 }}>★</span>
      ))}
    </span>
  )
}

export default function ParentProgressPage() {
  const router = useRouter()
  const params = useParams()
  const studentId = params?.studentId as string

  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [subjects, setSubjects] = useState<Subject[]>([])
  const [starsByLesson, setStarsByLesson] = useState<Record<string, number>>({})
  const [starsBySubject, setStarsBySubject] = useState<Record<string, number>>({})
  const [maxBySubject, setMaxBySubject] = useState<Record<string, number>>({})
  const [contentMap, setContentMap] = useState<Record<string, { id: string; title: string; unitTitle: string }[]>>({})
  const [loading, setLoading] = useState(true)
  const [expanded, setExpanded] = useState<Record<string, boolean>>({})

  useEffect(() => {
    const init = async () => {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) { router.push('/'); return }

      // Verify the student belongs to this parent
      const { data: studentRow } = await supabase
        .from('students')
        .select('*')
        .eq('id', studentId)
        .eq('parent_id', user.id)
        .single()

      if (!studentRow) { router.push('/parent'); return }
      setStudent(studentRow)

      const grade = studentRow.grade
      const gradeSubjects = getSubjectsForGrade(grade)
      setSubjects(gradeSubjects)

      // Build lesson→subject map, max stars map, and content map for display
      const gradeContent = getGradeContent(grade)
      const lessonSubjectMap: Record<string, string> = {}
      const maxMap: Record<string, number> = {}
      const cMap: Record<string, { id: string; title: string; unitTitle: string }[]> = {}

      Object.entries(gradeContent).forEach(([subjectId, units]) => {
        cMap[subjectId] = []
        units.forEach(unit => {
          unit.lessons.forEach(lesson => {
            lessonSubjectMap[lesson.id] = subjectId
            maxMap[subjectId] = (maxMap[subjectId] || 0) + 3
            cMap[subjectId].push({ id: lesson.id, title: lesson.title, unitTitle: unit.title })
          })
        })
      })
      setMaxBySubject(maxMap)
      setContentMap(cMap)

      // Fetch progress
      const progress = await getProgress(studentId)
      const byLesson: Record<string, number> = {}
      const bySubject: Record<string, number> = {}
      progress.forEach((p: { lesson_id: string; stars_earned: number }) => {
        byLesson[p.lesson_id] = p.stars_earned
        const subId = lessonSubjectMap[p.lesson_id]
        if (subId) bySubject[subId] = (bySubject[subId] || 0) + p.stars_earned
      })
      setStarsByLesson(byLesson)
      setStarsBySubject(bySubject)

      setLoading(false)
    }
    init()
  }, [router, studentId])

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <div className="text-5xl animate-float">⭐</div>
    </div>
  )

  if (!student) return null

  const categories: { key: SubjectCategory; label: string; emoji: string }[] = [
    { key: 'core', label: 'Основни', emoji: '📚' },
    { key: 'science', label: 'Наука', emoji: '🔬' },
    { key: 'social', label: 'Општество', emoji: '🌍' },
    { key: 'languages', label: 'Јазици', emoji: '💬' },
  ]

  const totalStars = Object.values(starsBySubject).reduce((a, b) => a + b, 0)
  const totalMax = Object.values(maxBySubject).reduce((a, b) => a + b, 0)

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center gap-4"
        style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)' }}>
        <button onClick={() => router.push('/parent')}
          className="text-white/70 hover:text-white text-xl font-black transition-colors outline-none select-none cursor-pointer flex items-center justify-center w-8 h-8">{'←'}</button>
        <div className="flex items-center gap-3 flex-1">
          <span className="text-2xl">⭐</span>
          <span className="text-white font-black text-lg">Напредок</span>
        </div>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8 space-y-6">
        {/* Student card */}
        <div className="bg-white rounded-3xl p-5 flex items-center gap-4"
          style={{ boxShadow: '0 2px 12px rgba(92,53,212,0.08)' }}>
          <div className="w-14 h-14 rounded-2xl flex items-center justify-center text-2xl font-black text-white flex-shrink-0"
            style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
            {student.name[0].toUpperCase()}
          </div>
          <div className="flex-1 min-w-0">
            <p className="font-black text-xl leading-tight" style={{ color: '#1A1A2E' }}>{student.name}</p>
            <p className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>{gradeLabel(student.grade)}</p>
            <div className="flex items-center gap-3 mt-1">
              <span className="text-sm font-bold" style={{ color: '#FFD93D' }}>⭐ {totalStars} / {totalMax} ѕвезди</span>
              {student.streak > 0 && (
                <span className="text-sm font-bold" style={{ color: '#FF6B6B' }}>🔥 {student.streak} дена по ред</span>
              )}
            </div>
          </div>
        </div>

        {/* Subjects by category */}
        {categories.map(({ key, label, emoji }) => {
          const group = subjects.filter(s => s.category === key)
          if (group.length === 0) return null
          return (
            <div key={key}>
              <div className="flex items-center gap-2 mb-3 px-1">
                <span className="text-base">{emoji}</span>
                <span className="text-xs font-black tracking-widest uppercase" style={{ color: '#9B9BAA' }}>{label}</span>
                <div className="flex-1 h-px" style={{ background: '#E8E8F0' }} />
              </div>
              <div className="space-y-3">
                {group.map(subject => {
                  const earned = starsBySubject[subject.id] || 0
                  const max = maxBySubject[subject.id] || 0
                  const pct = max > 0 ? Math.round((earned / max) * 100) : 0
                  const isOpen = expanded[subject.id] ?? false
                  const lessons = contentMap[subject.id] || []

                  return (
                    <div key={subject.id} className="rounded-3xl overflow-hidden"
                      style={{ background: subject.bgColor, border: `2px solid ${subject.color}25` }}>
                      <button
                        type="button"
                        className="w-full p-5 text-left"
                        onClick={() => setExpanded(prev => ({ ...prev, [subject.id]: !isOpen }))}>
                        <div className="flex items-center justify-between">
                          <div className="flex items-center gap-3">
                            <span className="text-2xl">{subject.emoji}</span>
                            <div>
                              <div className="text-base font-black" style={{ color: subject.color }}>{subject.nameMk}</div>
                              <div className="text-xs font-semibold mt-0.5" style={{ color: '#9B9BAA' }}>
                                {earned} / {max} ѕвезди · {pct}%
                              </div>
                            </div>
                          </div>
                          <div className="flex items-center gap-3">
                            {max > 0 && (
                              <div className="w-20 h-2 rounded-full overflow-hidden" style={{ background: '#00000015' }}>
                                <div className="h-full rounded-full transition-all"
                                  style={{ width: `${pct}%`, background: subject.color }} />
                              </div>
                            )}
                            <span className="text-sm font-black" style={{ color: subject.color }}>
                              {isOpen ? '▲' : '▼'}
                            </span>
                          </div>
                        </div>
                      </button>

                      {isOpen && lessons.length > 0 && (
                        <div className="px-5 pb-5 space-y-1">
                          <div className="h-px mb-3" style={{ background: `${subject.color}20` }} />
                          {lessons.map((lesson, idx) => {
                            const lessonStars = starsByLesson[lesson.id] || 0
                            return (
                              <div key={lesson.id}
                                className="flex items-center justify-between py-2 px-3 rounded-2xl"
                                style={{ background: lessonStars > 0 ? `${subject.color}10` : '#FFFFFF60' }}>
                                <div className="flex items-center gap-2 min-w-0">
                                  <span className="text-xs font-black flex-shrink-0" style={{ color: `${subject.color}80` }}>
                                    {idx + 1}.
                                  </span>
                                  <span className="text-sm font-semibold truncate" style={{ color: '#1A1A2E' }}>
                                    {lesson.title}
                                  </span>
                                </div>
                                <div className="flex-shrink-0 ml-2">
                                  <StarRow earned={lessonStars} max={3} />
                                </div>
                              </div>
                            )
                          })}
                        </div>
                      )}

                      {isOpen && lessons.length === 0 && (
                        <div className="px-5 pb-5">
                          <p className="text-xs font-semibold text-center py-3" style={{ color: '#9B9BAA' }}>
                            Нема лекции за овој предмет.
                          </p>
                        </div>
                      )}
                    </div>
                  )
                })}
              </div>
            </div>
          )
        })}
      </div>
    </main>
  )
}
