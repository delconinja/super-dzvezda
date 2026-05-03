'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { getSubjectsForGrade } from '@/lib/subjects'
import { getActiveStudent, getSubscription, getProgress, clearActiveStudent, trialDaysLeft, isTrialExpired, StudentProfile, Subscription } from '@/lib/auth'
import { getGradeContent } from '@/lib/content'
import { Subject } from '@/types'
import SubjectIcon from '@/components/SubjectIcon'

export default function DashboardPage() {
  const router = useRouter()
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [sub, setSub] = useState<Subscription | null>(null)
  const [daysLeft, setDaysLeft] = useState(14)
  const [loading, setLoading] = useState(true)
  const [starsBySubject, setStarsBySubject] = useState<Record<string, number>>({})
  const [maxStarsBySubject, setMaxStarsBySubject] = useState<Record<string, number>>({})
  const [subjects, setSubjects] = useState<Subject[]>([])

  useEffect(() => {
    const active = getActiveStudent()
    if (!active) { router.push('/'); return }
    setStudent(active)

    const gradeSubjects = getSubjectsForGrade(active.grade)
    setSubjects(gradeSubjects)

    // Build lessonId → subjectId lookup + max stars per subject
    const gradeContent = getGradeContent(active.grade)
    const lessonSubjectMap: Record<string, string> = {}
    const maxMap: Record<string, number> = {}
    Object.entries(gradeContent).forEach(([subjectId, units]) => {
      units.forEach(u => u.lessons.forEach(l => {
        lessonSubjectMap[l.id] = subjectId
        maxMap[subjectId] = (maxMap[subjectId] || 0) + 3
      }))
    })
    setMaxStarsBySubject(maxMap)

    Promise.all([getSubscription(), getProgress(active.id)]).then(([s, progress]) => {
      if (!s) { setLoading(false); return }
      if (isTrialExpired(s)) { router.push('/trial-expired'); return }
      setSub(s)
      setDaysLeft(trialDaysLeft(s))

      const map: Record<string, number> = {}
      progress.forEach((p) => {
        const subId = lessonSubjectMap[p.lesson_id]
        if (subId) map[subId] = (map[subId] || 0) + p.stars_earned
      })
      setStarsBySubject(map)
      setLoading(false)
    })
  }, [router])

  const handleLogout = () => { clearActiveStudent(); router.push('/') }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <div className="text-5xl animate-float">⭐</div>
    </div>
  )

  if (!student) return null

  const trialColor = daysLeft <= 3 ? '#FF6B6B' : daysLeft <= 7 ? '#FFD93D' : '#6BCB77'

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center justify-between"
        style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)' }}>
        <div className="flex items-center gap-3">
          <span className="text-3xl">⭐</span>
          <span className="text-white font-black text-xl">Супер Ѕвезда</span>
        </div>
        <div className="flex items-center gap-3">
          {sub && (
            <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full"
              style={{ background: `${trialColor}22`, border: `1.5px solid ${trialColor}` }}>
              <span className="text-sm">⏳</span>
              <span className="text-xs font-black" style={{ color: trialColor }}>
                {daysLeft} {daysLeft === 1 ? 'ден' : 'дена'} пробен
              </span>
            </div>
          )}
          <button onClick={() => router.push('/parent')}
            className="text-white/60 hover:text-white/90 text-sm font-bold transition-colors">
            👪
          </button>
          <button onClick={handleLogout}
            className="text-white/50 hover:text-white/90 text-sm font-bold transition-colors">
            Излез
          </button>
        </div>
      </header>

      {daysLeft <= 3 && (
        <div className="px-6 py-3 text-center text-sm font-bold"
          style={{ background: '#FF6B6B', color: 'white' }}>
          ⚠️ Пробниот период истекува за {daysLeft} {daysLeft === 1 ? 'ден' : 'дена'}!
        </div>
      )}

      <div className="max-w-2xl mx-auto px-6 py-8">
        <div className="mb-8">
          <p className="text-sm font-bold mb-1" style={{ color: '#6B6B8A' }}>
            {student.grade}-то одделение
          </p>
          <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>
            Здраво, {student.name.split(' ')[0]}! 👋
          </h1>
          <p className="text-base mt-1 mb-4" style={{ color: '#6B6B8A' }}>
            Одбери предмет и почни да учиш!
          </p>
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 px-4 py-2 rounded-2xl font-black text-sm"
              style={{ background: student.streak > 0 ? '#FFF3E0' : '#F3F4F6', color: student.streak > 0 ? '#E65100' : '#9CA3AF', border: `2px solid ${student.streak > 0 ? '#FF9800' : '#E5E7EB'}` }}>
              🔥 {student.streak} {student.streak === 1 ? 'ден' : 'дена'} по ред
            </div>
            <div className="flex items-center gap-2 px-4 py-2 rounded-2xl font-black text-sm"
              style={{ background: '#FFFDE7', color: '#F57F17', border: '2px solid #FFD600' }}>
              ⭐ {student.stars_total} ѕвезди вкупно
            </div>
          </div>
        </div>

        <div className="grid gap-4">
          {subjects.map((subject) => (
            <button key={subject.id} type="button"
              onClick={() => router.push(`/subject/${subject.id}`)}
              className="w-full rounded-3xl p-6 text-left transition-all duration-200 active:scale-[0.98]"
              style={{ background: subject.bgColor, border: `2px solid ${subject.color}25` }}
              onMouseEnter={(e) => { e.currentTarget.style.boxShadow = `0 8px 30px ${subject.color}30`; e.currentTarget.style.transform = 'scale(1.02)' }}
              onMouseLeave={(e) => { e.currentTarget.style.boxShadow = 'none'; e.currentTarget.style.transform = 'scale(1)' }}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  <SubjectIcon subject={subject} size="lg" />
                  <div>
                    <div className="text-xl font-black" style={{ color: subject.color }}>{subject.nameMk}</div>
                    <div className="text-sm font-semibold mt-0.5" style={{ color: '#9B9BAA' }}>{subject.world}</div>
                    <div className="flex items-center gap-1 mt-2">
                      <span className="text-xs font-bold" style={{ color: '#FFD93D' }}>
                        ⭐ {starsBySubject[subject.id] || 0}
                      </span>
                      <span className="text-xs" style={{ color: '#9B9BAA' }}>
                        / {maxStarsBySubject[subject.id] || subject.unitsCount * 3} ѕвезди
                      </span>
                    </div>
                  </div>
                </div>
                <span className="text-2xl font-black" style={{ color: subject.color }}>→</span>
              </div>
            </button>
          ))}
        </div>

        <div className="mt-8 rounded-3xl p-5"
          style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
          <div className="flex items-start gap-3">
            <span className="text-2xl">💡</span>
            <div>
              <div className="text-white font-black text-sm mb-1">СОВЕТ НА ДЕНОТ</div>
              <div className="text-purple-100 text-sm leading-relaxed">
                Редовното вежбање по 15 минути е подобро од еднаш неделно по еден час. Учи секој ден!
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
