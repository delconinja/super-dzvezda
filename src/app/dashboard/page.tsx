'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { getSubjectsForGrade, gradeOrdinal } from '@/lib/subjects'
import { getActiveStudent, getSubscription, getProgress, clearActiveStudent, trialDaysLeft, isTrialExpired, StudentProfile, Subscription } from '@/lib/auth'
import { getGradeContent } from '@/lib/content'
import { Subject } from '@/types'
import SubjectIcon from '@/components/SubjectIcon'
import StarMascot from '@/components/StarMascot'

// Grades with V2 structure active — add a grade here to enable XP bar for it
const V2_GRADES = [5]

export default function DashboardPage() {
  const router = useRouter()
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [sub, setSub] = useState<Subscription | null>(null)
  const [daysLeft, setDaysLeft] = useState(14)
  const [loading, setLoading] = useState(true)
  const [starsBySubject, setStarsBySubject] = useState<Record<string, number>>({})
  const [maxStarsBySubject, setMaxStarsBySubject] = useState<Record<string, number>>({})
  const [subjects, setSubjects] = useState<Subject[]>([])
  const [totalXP, setTotalXP] = useState(0)
  const [maxXP, setMaxXP] = useState(0)
  const [gradeStats, setGradeStats] = useState({ lessons: 0, subjects: 0 })
  const [liveStarsTotal, setLiveStarsTotal] = useState<number | null>(null)

  useEffect(() => {
    const init = async () => {
      const active = getActiveStudent()
      if (!active) { router.push('/'); return }
      setStudent(active)

      const grade = active.grade
      const gradeSubjects = getSubjectsForGrade(grade)
      setSubjects(gradeSubjects)

      // Build lessonId → subjectId lookup + max stars per subject
      const gradeContent = getGradeContent(grade)
      const lessonSubjectMap: Record<string, string> = {}
      const maxMap: Record<string, number> = {}
      Object.entries(gradeContent).forEach(([subjectId, units]) => {
        units.forEach(u => u.lessons.forEach(l => {
          lessonSubjectMap[l.id] = subjectId
          maxMap[subjectId] = (maxMap[subjectId] || 0) + 3
        }))
      })
      setMaxStarsBySubject(maxMap)

      // XP stats — computed directly from gradeContent so new lessons/subjects are counted automatically
      if (V2_GRADES.includes(grade)) {
        const gradeLessonIds = new Set(Object.keys(lessonSubjectMap))
        const totalLessons = gradeLessonIds.size
        const activeSubjects = Object.values(gradeContent).filter(units =>
          units.some(u => u.lessons.length > 0)
        ).length
        setMaxXP(totalLessons * 50)
        setGradeStats({ lessons: totalLessons, subjects: activeSubjects })
      }

      Promise.all([getSubscription(), getProgress(active.id)]).then(([s, progress]) => {
        // Subscription check — trial redirect only, never block progress loading
        if (s && isTrialExpired(s)) { router.push('/trial-expired'); return }
        if (s) { setSub(s); setDaysLeft(trialDaysLeft(s)) }

        // Progress always loads regardless of subscription state
        const map: Record<string, number> = {}
        progress.forEach((p) => {
          const subId = lessonSubjectMap[p.lesson_id]
          if (subId) map[subId] = (map[subId] || 0) + p.stars_earned
        })
        setStarsBySubject(map)

        const liveTotalStars = progress.reduce((sum: number, p: { stars_earned: number }) => sum + p.stars_earned, 0)
        setLiveStarsTotal(liveTotalStars)

        if (V2_GRADES.includes(grade)) {
          const gradeLessonIds = new Set(Object.keys(lessonSubjectMap))
          const completedLessons = progress.filter(
            p => p.stars_earned > 0 && gradeLessonIds.has(p.lesson_id)
          ).length
          setTotalXP(completedLessons * 50)
        }

        setLoading(false)
      })
    }
    init()
  }, [router])

  const handleLogout = () => { clearActiveStudent(); router.push('/') }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <div className="text-5xl animate-float">⭐</div>
    </div>
  )

  if (!student) return null

  const grade = student.grade
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
          <div className="flex items-center gap-4 mb-3">
            <StarMascot talking={false} size={80} />
            <div>
              <p className="text-sm font-bold mb-1" style={{ color: '#6B6B8A' }}>
                {grade === 0 ? 'Сите одделенија' : `${grade}-${gradeOrdinal(grade)} одделение`}
              </p>
              <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>
                Здраво, {student.name.split(' ')[0]}! 👋
              </h1>
              <p className="text-base mt-1" style={{ color: '#6B6B8A' }}>
                Одбери предмет и почни да учиш!
              </p>
            </div>
          </div>
          <div className="flex items-center gap-3 mb-4">
            <div className="flex items-center gap-2 px-4 py-2 rounded-2xl font-black text-sm"
              style={{ background: student.streak > 0 ? '#FFF3E0' : '#F3F4F6', color: student.streak > 0 ? '#E65100' : '#9CA3AF', border: `2px solid ${student.streak > 0 ? '#FF9800' : '#E5E7EB'}` }}>
              🔥 {student.streak} {student.streak === 1 ? 'ден' : 'дена'} по ред
            </div>
            <div className="flex items-center gap-2 px-4 py-2 rounded-2xl font-black text-sm"
              style={{ background: '#FFFDE7', color: '#F57F17', border: '2px solid #FFD600' }}>
              ⭐ {liveStarsTotal !== null ? liveStarsTotal : student.stars_total} ѕвезди вкупно
            </div>
          </div>

          {/* XP bar — V2 grades only */}
          {V2_GRADES.includes(grade) && maxXP > 0 && (() => {
            const XP_PER_LEVEL = 200
            const level = Math.floor(totalXP / XP_PER_LEVEL) + 1
            const xpInLevel = totalXP % XP_PER_LEVEL
            const pct = Math.round((xpInLevel / XP_PER_LEVEL) * 100)
            return (
              <div className="rounded-2xl p-4 mb-1"
                style={{ background: 'linear-gradient(135deg, #F5F0FF, #EDE9FE)', border: '2px solid #DDD6FE' }}>
                <div className="flex items-center justify-between mb-1">
                  <div className="flex items-center gap-2">
                    <span className="text-lg">⚡</span>
                    <span className="font-black text-sm" style={{ color: '#5B21B6' }}>Ниво {level}</span>
                  </div>
                  <span className="text-xs font-bold" style={{ color: '#7C3AED' }}>
                    {totalXP} / {maxXP} XP
                  </span>
                </div>
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-xs font-semibold" style={{ color: '#8B5CF6' }}>
                    📚 {gradeStats.lessons} лекции
                  </span>
                  <span style={{ color: '#C4B5FD' }}>·</span>
                  <span className="text-xs font-semibold" style={{ color: '#8B5CF6' }}>
                    🎯 {gradeStats.subjects} предмети
                  </span>
                </div>
                <div className="h-3 rounded-full overflow-hidden" style={{ background: '#DDD6FE' }}>
                  <div className="h-full rounded-full transition-all duration-700"
                    style={{
                      width: `${pct}%`,
                      background: 'linear-gradient(90deg, #7C3AED, #A855F7)',
                    }} />
                </div>
                <div className="flex justify-between mt-1">
                  <span className="text-xs font-semibold" style={{ color: '#8B5CF6' }}>
                    {xpInLevel} / {XP_PER_LEVEL} XP до Ниво {level + 1}
                  </span>
                  <span className="text-xs font-semibold" style={{ color: '#A78BFA' }}>{pct}%</span>
                </div>
              </div>
            )
          })()}
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
