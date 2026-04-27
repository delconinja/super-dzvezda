'use client'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { getSubject } from '@/lib/subjects'
import { GRADE7_CONTENT } from '@/lib/content'
import { getActiveStudent, StudentProfile } from '@/lib/auth'

export default function SubjectPage() {
  const router = useRouter()
  const params = useParams()
  const subjectId = params.subjectId as string
  const subject = getSubject(subjectId)
  const [student, setStudent] = useState<StudentProfile | null>(null)

  useEffect(() => {
    const active = getActiveStudent()
    if (!active) { router.push('/'); return }
    setStudent(active)
  }, [router])

  if (!subject || !student) return null

  const units = GRADE7_CONTENT[subjectId as keyof typeof GRADE7_CONTENT] || []

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      {/* Header */}
      <header className="px-6 py-4 flex items-center gap-3"
        style={{ background: subject.color }}>
        <button onClick={() => router.push('/dashboard')}
          className="text-white/80 hover:text-white text-2xl font-bold transition-colors">←</button>
        <span className="text-3xl">{subject.emoji}</span>
        <div>
          <div className="text-white font-black text-xl">{subject.nameMk}</div>
          <div className="text-white/70 text-sm">{subject.world}</div>
        </div>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8">
        <h2 className="text-2xl font-black mb-6" style={{ color: '#1A1A2E' }}>
          Единици за {student.grade}-то одделение
        </h2>

        <div className="grid gap-4">
          {units.map((unit, unitIdx) => (
            <div key={unit.id} className="bg-white rounded-3xl p-5 shadow-sm">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 rounded-full flex items-center justify-center font-black text-white text-lg"
                  style={{ background: subject.color }}>
                  {unitIdx + 1}
                </div>
                <h3 className="text-lg font-black" style={{ color: '#1A1A2E' }}>{unit.title}</h3>
              </div>

              <div className="grid gap-2">
                {unit.lessons.map((lesson, lessonIdx) => (
                  <button key={lesson.id}
                    onClick={() => router.push(`/lesson/${lesson.id}`)}
                    className="w-full flex items-center justify-between p-3 rounded-2xl transition-all duration-200 hover:scale-[1.01]"
                    style={{ background: subject.bgColor }}>
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold text-white"
                        style={{ background: lessonIdx === 0 ? subject.color : '#D1D5DB' }}>
                        {lessonIdx === 0 ? '▶' : `${lessonIdx + 1}`}
                      </div>
                      <span className="font-bold text-sm" style={{ color: '#1A1A2E' }}>
                        {lesson.title}
                      </span>
                    </div>
                    <div className="flex gap-0.5">
                      {[...Array(3)].map((_, i) => (
                        <span key={i} className="text-gray-300 text-sm">★</span>
                      ))}
                    </div>
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  )
}
