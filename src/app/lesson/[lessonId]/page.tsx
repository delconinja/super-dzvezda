'use client'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { GRADE7_CONTENT, ExerciseData } from '@/lib/content'
import { SUBJECTS } from '@/lib/subjects'
import { getActiveStudent, saveProgress, refreshStudentSession, StudentProfile } from '@/lib/auth'

type Phase = 'lesson' | 'exercises' | 'results'

export default function LessonPage() {
  const router = useRouter()
  const params = useParams()
  const lessonId = params.lessonId as string

  const [phase, setPhase] = useState<Phase>('lesson')
  const [currentEx, setCurrentEx] = useState(0)
  const [selected, setSelected] = useState<string | null>(null)
  const [answered, setAnswered] = useState(false)
  const [correct, setCorrect] = useState(0)
  const [showStar, setShowStar] = useState(false)
  const [student, setStudent] = useState<StudentProfile | null>(null)

  // Find lesson across all subjects
  const lesson = Object.values(GRADE7_CONTENT)
    .flatMap((units) => units.flatMap((u) => u.lessons))
    .find((l) => l.id === lessonId)

  const subjectId = Object.entries(GRADE7_CONTENT).find(([, units]) =>
    units.some((u) => u.lessons.some((l) => l.id === lessonId))
  )?.[0]

  const subject = SUBJECTS.find((s) => s.id === subjectId)

  useEffect(() => {
    const active = getActiveStudent()
    if (!active) { router.push('/'); return }
    setStudent(active)
  }, [router])

  if (!lesson || !subject) return (
    <div className="min-h-screen flex items-center justify-center">
      <p style={{ color: '#6B6B8A' }}>Лекцијата не е пронајдена.</p>
    </div>
  )

  const exercises = lesson.exercises
  const ex: ExerciseData = exercises[currentEx]
  const starsEarned = correct >= exercises.length ? 3 : correct >= Math.ceil(exercises.length * 0.6) ? 2 : correct > 0 ? 1 : 0

  const handleAnswer = (option: string) => {
    if (answered) return
    setSelected(option)
    setAnswered(true)
    if (option === ex.correct) {
      setCorrect((c) => c + 1)
      setShowStar(true)
      setTimeout(() => setShowStar(false), 800)
    }
  }

  const handleNext = () => {
    if (currentEx < exercises.length - 1) {
      setCurrentEx((i) => i + 1)
      setSelected(null)
      setAnswered(false)
    } else {
      const stars = correct >= exercises.length ? 3 : correct >= Math.ceil(exercises.length * 0.6) ? 2 : correct > 0 ? 1 : 0
      if (student) {
        saveProgress(student.id, lessonId, stars)
          .then(() => refreshStudentSession(student.id))
      }
      setPhase('results')
    }
  }

  // ── LESSON PHASE ──
  if (phase === 'lesson') return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center gap-3" style={{ background: subject.color }}>
        <button onClick={() => router.push(`/subject/${subject.id}`)}
          className="text-white/80 hover:text-white text-2xl font-bold">←</button>
        <span className="text-2xl">{subject.emoji}</span>
        <span className="text-white font-black text-lg">{lesson.title}</span>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8">
        <div className="bg-white rounded-3xl p-6 shadow-sm mb-6">
          <div className="prose max-w-none" style={{ color: '#1A1A2E' }}>
            {lesson.content.split('\n').map((line, i) => {
              if (line.startsWith('## ')) return <h2 key={i} className="text-2xl font-black mb-3" style={{ color: subject.color }}>{line.slice(3)}</h2>
              if (line.startsWith('**') && line.endsWith('**')) return <p key={i} className="font-bold my-1">{line.slice(2, -2)}</p>
              if (line.startsWith('- ')) return <li key={i} className="ml-4 my-1 font-semibold">{line.slice(2)}</li>
              if (line.startsWith('💡')) return <div key={i} className="mt-4 p-3 rounded-2xl font-semibold text-sm" style={{ background: subject.bgColor, color: subject.color }}>{line}</div>
              if (line.trim() === '') return <br key={i} />
              return <p key={i} className="my-1 leading-relaxed">{line}</p>
            })}
          </div>
        </div>

        <button onClick={() => setPhase('exercises')}
          className="w-full py-4 rounded-2xl text-xl font-black text-white transition-all duration-200 hover:scale-[1.02]"
          style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
          Почни со вежби! ⭐
        </button>
      </div>
    </main>
  )

  // ── EXERCISES PHASE ──
  if (phase === 'exercises') return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      {showStar && (
        <div className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 text-8xl animate-star-pop pointer-events-none">⭐</div>
      )}

      <header className="px-6 py-4 flex items-center justify-between" style={{ background: subject.color }}>
        <div className="flex items-center gap-3">
          <span className="text-2xl">{subject.emoji}</span>
          <span className="text-white font-black">Вежби</span>
        </div>
        <span className="text-white/80 font-bold">{currentEx + 1} / {exercises.length}</span>
      </header>

      {/* Progress bar */}
      <div className="h-2 w-full" style={{ background: '#E5E7EB' }}>
        <div className="h-2 transition-all duration-500"
          style={{ width: `${((currentEx + (answered ? 1 : 0)) / exercises.length) * 100}%`, background: subject.color }} />
      </div>

      <div className="max-w-2xl mx-auto px-6 py-8">
        {/* Question */}
        <div className="bg-white rounded-3xl p-6 shadow-sm mb-6">
          <div className="text-xs font-bold mb-3 uppercase tracking-widest" style={{ color: subject.color }}>
            {ex.type === 'multiple-choice' ? 'Одбери точен одговор' : ex.type === 'true-false' ? 'Точно или Неточно?' : 'Пополни'}
          </div>
          <p className="text-xl font-black" style={{ color: '#1A1A2E' }}>{ex.question}</p>
        </div>

        {/* Options */}
        <div className="grid gap-3 mb-6">
          {(ex.options || ['Точно', 'Неточно']).map((opt) => {
            let bg = 'white'
            let border = '#E5E7EB'
            let textColor = '#1A1A2E'
            if (answered) {
              if (opt === ex.correct) { bg = '#E8F8EA'; border = '#6BCB77'; textColor = '#2D7A35' }
              else if (opt === selected) { bg = '#FFE8E8'; border = '#FF6B6B'; textColor = '#C0392B' }
            } else if (selected === opt) {
              bg = subject.bgColor; border = subject.color
            }
            return (
              <button key={opt} onClick={() => handleAnswer(opt)}
                className="w-full p-4 rounded-2xl text-left font-bold text-lg transition-all duration-200"
                style={{ background: bg, border: `2px solid ${border}`, color: textColor,
                  transform: !answered ? 'scale(1)' : undefined,
                  cursor: answered ? 'default' : 'pointer' }}>
                {opt}
                {answered && opt === ex.correct && <span className="ml-2">✅</span>}
                {answered && opt === selected && opt !== ex.correct && <span className="ml-2">❌</span>}
              </button>
            )
          })}
        </div>

        {/* Explanation */}
        {answered && (
          <div className="rounded-3xl p-4 mb-6"
            style={{ background: selected === ex.correct ? '#E8F8EA' : '#FFE8E8' }}>
            <p className="font-bold text-sm" style={{ color: selected === ex.correct ? '#2D7A35' : '#C0392B' }}>
              {selected === ex.correct ? '✅ Точно!' : '❌ Неточно'} — {ex.explanation}
            </p>
          </div>
        )}

        {answered && (
          <button onClick={handleNext}
            className="w-full py-4 rounded-2xl text-xl font-black text-white transition-all duration-200 hover:scale-[1.02]"
            style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
            {currentEx < exercises.length - 1 ? 'Следно прашање →' : 'Заврши! 🎉'}
          </button>
        )}
      </div>
    </main>
  )

  // ── RESULTS PHASE ──
  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-6"
      style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69, #5C35D4)' }}>
      <div className="text-center">
        <div className="text-8xl mb-4 animate-float">
          {starsEarned === 3 ? '🏆' : starsEarned === 2 ? '⭐' : starsEarned === 1 ? '🌟' : '💪'}
        </div>
        <h1 className="text-4xl font-black text-white mb-2">
          {starsEarned === 3 ? 'Совршено!' : starsEarned >= 2 ? 'Одлично!' : starsEarned === 1 ? 'Добар почеток!' : 'Обиди се пак!'}
        </h1>
        <p className="text-purple-200 text-lg mb-6">
          {correct} / {exercises.length} точни одговори
        </p>

        {/* Stars */}
        <div className="flex justify-center gap-4 mb-8">
          {[1, 2, 3].map((s) => (
            <span key={s} className="text-5xl transition-all duration-300"
              style={{ filter: s <= starsEarned ? 'none' : 'grayscale(1) opacity(0.3)',
                animationDelay: `${s * 0.2}s` }}>
              ⭐
            </span>
          ))}
        </div>

        <div className="flex flex-col gap-3 w-full max-w-xs mx-auto">
          <button onClick={() => { setPhase('exercises'); setCurrentEx(0); setSelected(null); setAnswered(false); setCorrect(0) }}
            className="w-full py-3 rounded-2xl font-black text-white border-2 border-white/30 hover:border-white/60 transition-all">
            🔄 Повтори
          </button>
          <button onClick={() => router.push(`/subject/${subject.id}`)}
            className="w-full py-3 rounded-2xl font-black text-white transition-all hover:scale-[1.02]"
            style={{ background: subject.color }}>
            ← Назад кон {subject.nameMk}
          </button>
        </div>
      </div>
    </main>
  )
}
