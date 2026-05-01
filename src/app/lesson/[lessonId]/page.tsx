'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { getGradeContent, ExerciseData } from '@/lib/content'
import { getSubject } from '@/lib/subjects'
import { getActiveStudent, saveProgress, refreshStudentSession, StudentProfile } from '@/lib/auth'

type Phase = 'lesson' | 'exercises' | 'results'

// ── Option labels ────────────────────────────────────────────────
const LABELS = ['А', 'Б', 'В', 'Г', 'Д']

export default function LessonPage() {
  const router = useRouter()
  const params = useParams()
  const lessonId = params.lessonId as string

  const [phase, setPhase] = useState<Phase>('lesson')
  const [currentEx, setCurrentEx] = useState(0)
  const [selected, setSelected] = useState<string | null>(null)
  const [answered, setAnswered] = useState(false)
  const [hintShown, setHintShown] = useState(false)
  const [revealed, setRevealed] = useState(false)
  const [wrongAttempts, setWrongAttempts] = useState<string[]>([])
  const [correct, setCorrect] = useState(0)
  const [showStar, setShowStar] = useState(false)
  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [shake, setShake] = useState(false)

  const activeStudent = getActiveStudent()
  const gradeContent = getGradeContent(activeStudent?.grade ?? 7)

  const lesson = Object.values(gradeContent)
    .flatMap((units) => units.flatMap((u) => u.lessons))
    .find((l) => l.id === lessonId)

  const subjectId = Object.entries(gradeContent).find(([, units]) =>
    units.some((u) => u.lessons.some((l) => l.id === lessonId))
  )?.[0]

  const subject = getSubject(subjectId ?? '')

  useEffect(() => {
    const active = getActiveStudent()
    if (!active) { router.push('/'); return }
    setStudent(active)
  }, [router])

  if (!lesson || !subject) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <p style={{ color: '#6B6B8A' }}>Лекцијата не е пронајдена.</p>
    </div>
  )

  const exercises = lesson.exercises
  const ex: ExerciseData = exercises[currentEx]
  const starsEarned = correct >= exercises.length ? 3
    : correct >= Math.ceil(exercises.length * 0.6) ? 2
    : correct > 0 ? 1 : 0

  const handleAnswer = (option: string) => {
    if (revealed || hintShown) return
    setSelected(option)
    setAnswered(true)

    if (option === ex.correct) {
      setCorrect((c) => c + 1)
      setRevealed(true)
      setShowStar(true)
      setTimeout(() => setShowStar(false), 900)
    } else {
      const isFirstWrong = wrongAttempts.length === 0
      setWrongAttempts((prev) => [...prev, option])
      setShake(true)
      setTimeout(() => setShake(false), 400)
      if (ex.hint && isFirstWrong) {
        setHintShown(true)
      } else {
        setRevealed(true)
      }
    }
  }

  const handleRetry = () => {
    setSelected(null)
    setAnswered(false)
    setHintShown(false)
  }

  const handleNext = () => {
    if (currentEx < exercises.length - 1) {
      setCurrentEx((i) => i + 1)
      setSelected(null)
      setAnswered(false)
      setHintShown(false)
      setRevealed(false)
      setWrongAttempts([])
    } else {
      const stars = correct >= exercises.length ? 3
        : correct >= Math.ceil(exercises.length * 0.6) ? 2
        : correct > 0 ? 1 : 0
      if (student) {
        saveProgress(student.id, lessonId, stars)
          .then(() => refreshStudentSession(student.id))
      }
      setPhase('results')
    }
  }

  // ── LESSON PHASE ─────────────────────────────────────────────
  if (phase === 'lesson') return (
    <main className="min-h-screen" style={{ background: '#F4F6FB' }}>
      {/* Header */}
      <header className="px-5 py-4 flex items-center gap-3 sticky top-0 z-10"
        style={{ background: subject.color }}>
        <button onClick={() => router.push(`/subject/${subject.id}`)}
          className="w-9 h-9 rounded-xl flex items-center justify-center transition-all active:scale-90"
          style={{ background: 'rgba(255,255,255,0.18)' }}>
          <span className="text-white font-bold text-lg">←</span>
        </button>
        <span className="text-2xl">{subject.emoji}</span>
        <span className="text-white font-black text-base leading-tight flex-1">{lesson.title}</span>
      </header>

      <div className="max-w-xl mx-auto px-4 py-6 pb-28">

        {/* Lesson content card */}
        <div className="rounded-3xl overflow-hidden shadow-sm" style={{ background: 'white' }}>

          {/* Subject colour band */}
          <div className="px-6 pt-5 pb-3 flex items-center gap-3"
            style={{ background: `${subject.color}12`, borderBottom: `3px solid ${subject.color}` }}>
            <span className="text-3xl">{subject.emoji}</span>
            <div>
              <p className="text-xs font-bold tracking-widest uppercase" style={{ color: subject.color }}>
                {subject.nameMk}
              </p>
              <p className="font-black text-lg leading-tight" style={{ color: '#1A1A2E' }}>
                {lesson.title}
              </p>
            </div>
          </div>

          {/* Markdown content */}
          <div className="px-6 py-5 lesson-content">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                h2: ({ children }) => (
                  <h2 style={{
                    fontFamily: 'inherit',
                    fontSize: '1.2rem',
                    fontWeight: 900,
                    color: subject.color,
                    margin: '1.4rem 0 0.6rem',
                    paddingLeft: '12px',
                    borderLeft: `4px solid ${subject.color}`,
                    lineHeight: 1.3,
                  }}>{children}</h2>
                ),
                h3: ({ children }) => (
                  <h3 style={{
                    fontSize: '1rem',
                    fontWeight: 800,
                    color: '#1A1A2E',
                    margin: '1rem 0 0.4rem',
                  }}>{children}</h3>
                ),
                p: ({ children }) => (
                  <p style={{
                    fontSize: '0.9rem',
                    lineHeight: 1.75,
                    color: '#2D2D44',
                    margin: '0.5rem 0',
                  }}>{children}</p>
                ),
                strong: ({ children }) => (
                  <strong style={{ color: '#1A1A2E', fontWeight: 800 }}>{children}</strong>
                ),
                em: ({ children }) => (
                  <em style={{ color: subject.color, fontStyle: 'normal', fontWeight: 700 }}>{children}</em>
                ),
                ul: ({ children }) => (
                  <ul style={{ margin: '0.5rem 0', paddingLeft: 0, listStyle: 'none' }}>{children}</ul>
                ),
                ol: ({ children }) => (
                  <ol style={{ margin: '0.5rem 0', paddingLeft: '1.2rem' }}>{children}</ol>
                ),
                li: ({ children }) => (
                  <li style={{
                    fontSize: '0.88rem',
                    lineHeight: 1.65,
                    color: '#2D2D44',
                    padding: '3px 0 3px 20px',
                    position: 'relative',
                  }}>
                    <span style={{
                      position: 'absolute', left: 0,
                      color: subject.color, fontWeight: 900, fontSize: '1rem',
                    }}>·</span>
                    {children}
                  </li>
                ),
                blockquote: ({ children }) => (
                  <div style={{
                    background: `${subject.color}10`,
                    borderLeft: `4px solid ${subject.color}`,
                    borderRadius: '0 12px 12px 0',
                    padding: '10px 14px',
                    margin: '1rem 0',
                    fontSize: '0.88rem',
                    color: '#2D2D44',
                    lineHeight: 1.65,
                  }}>{children}</div>
                ),
                table: ({ children }) => (
                  <div style={{ overflowX: 'auto', margin: '1rem 0' }}>
                    <table style={{
                      width: '100%',
                      borderCollapse: 'collapse',
                      fontSize: '0.82rem',
                      borderRadius: '12px',
                      overflow: 'hidden',
                    }}>{children}</table>
                  </div>
                ),
                thead: ({ children }) => (
                  <thead style={{ background: subject.color }}>{children}</thead>
                ),
                th: ({ children }) => (
                  <th style={{
                    padding: '8px 12px',
                    color: 'white',
                    fontWeight: 700,
                    textAlign: 'left',
                    fontSize: '0.78rem',
                    letterSpacing: '0.04em',
                  }}>{children}</th>
                ),
                td: ({ children }) => (
                  <td style={{
                    padding: '7px 12px',
                    borderBottom: '1px solid #F0F0F5',
                    color: '#2D2D44',
                    lineHeight: 1.5,
                  }}>{children}</td>
                ),
                tr: ({ children }) => (
                  <tr style={{ background: 'white' }}>{children}</tr>
                ),
                code: ({ children }) => (
                  <code style={{
                    background: `${subject.color}15`,
                    color: subject.color,
                    padding: '2px 7px',
                    borderRadius: '6px',
                    fontFamily: 'monospace',
                    fontSize: '0.88rem',
                    fontWeight: 700,
                  }}>{children}</code>
                ),
              }}
            >
              {lesson.content}
            </ReactMarkdown>
          </div>
        </div>

        {/* Exercises count badge */}
        <div className="flex items-center gap-2 mt-5 mb-4 px-2">
          <div className="flex gap-1">
            {exercises.map((_, i) => (
              <div key={i} className="w-2 h-2 rounded-full" style={{ background: subject.color, opacity: 0.35 }} />
            ))}
          </div>
          <span className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>
            {exercises.length} вежби
          </span>
        </div>
      </div>

      {/* Start button — sticky bottom */}
      <div className="fixed bottom-0 left-0 right-0 px-4 pb-6 pt-3"
        style={{ background: 'linear-gradient(to top, #F4F6FB 70%, transparent)' }}>
        <button onClick={() => setPhase('exercises')}
          className="w-full max-w-xl mx-auto block py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-[0.98] shadow-lg"
          style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
          Почни со вежби →
        </button>
      </div>

      <style>{`
        .lesson-content > *:first-child { margin-top: 0 !important; }
        .lesson-content > *:last-child { margin-bottom: 0 !important; }
      `}</style>
    </main>
  )

  // ── EXERCISES PHASE ─────────────────────────────────────────────
  if (phase === 'exercises') return (
    <main className="min-h-screen flex flex-col" style={{ background: '#F4F6FB' }}>

      {/* Star pop animation */}
      {showStar && (
        <div className="fixed inset-0 z-50 flex items-center justify-center pointer-events-none">
          <div className="text-8xl animate-star-pop">⭐</div>
        </div>
      )}

      {/* Header */}
      <header className="px-5 py-3 flex items-center justify-between"
        style={{ background: subject.color }}>
        <div className="flex items-center gap-2">
          <span className="text-xl">{subject.emoji}</span>
          <span className="text-white font-black text-sm">{lesson.title}</span>
        </div>
        <div className="flex items-center gap-1">
          {exercises.map((_, i) => (
            <div key={i} className="w-2 h-2 rounded-full transition-all duration-300"
              style={{
                background: i < currentEx ? 'rgba(255,255,255,0.9)'
                  : i === currentEx ? 'white'
                  : 'rgba(255,255,255,0.3)',
                transform: i === currentEx ? 'scale(1.4)' : 'scale(1)',
              }} />
          ))}
        </div>
      </header>

      {/* Progress bar */}
      <div className="h-1.5 w-full" style={{ background: 'rgba(0,0,0,0.06)' }}>
        <div className="h-1.5 transition-all duration-500 rounded-r-full"
          style={{
            width: `${(currentEx / exercises.length) * 100}%`,
            background: subject.color,
          }} />
      </div>

      <div className="flex-1 flex flex-col max-w-xl w-full mx-auto px-4 py-5 gap-4">

        {/* Question card */}
        <div className="rounded-3xl overflow-hidden shadow-sm"
          style={{ background: 'white' }}>
          <div className="px-5 py-2 flex items-center gap-2"
            style={{ background: `${subject.color}15` }}>
            <span className="text-xs font-black tracking-widest uppercase" style={{ color: subject.color }}>
              {ex.type === 'true-false' ? 'Точно или Неточно?' : 'Одбери точен одговор'}
            </span>
          </div>
          <div className="px-5 py-5">
            <p className="font-black text-xl leading-snug" style={{ color: '#1A1A2E', fontSize: '1.15rem' }}>
              {ex.question}
            </p>
          </div>
        </div>

        {/* Options */}
        <div className={`flex flex-col gap-3 ${shake ? 'animate-shake' : ''}`}>
          {(ex.options || ['Точно', 'Неточно']).map((opt, idx) => {
            const isCorrect = opt === ex.correct
            const isWrong = wrongAttempts.includes(opt)
            const isSelected = selected === opt
            const isFaded = !revealed && !hintShown && wrongAttempts.includes(opt)

            let bg = 'white'
            let border = '#E8EAF0'
            let textColor = '#1A1A2E'
            let labelBg = '#F0F0F8'
            let labelColor = '#9B9BAA'
            let icon = null

            if (revealed) {
              if (isCorrect) {
                bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20'
                labelBg = '#4CAF50'; labelColor = 'white'
                icon = <span style={{ color: '#4CAF50', fontSize: '1.1rem' }}>✓</span>
              } else if (isWrong) {
                bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C'
                labelBg = '#EF5350'; labelColor = 'white'
                icon = <span style={{ color: '#EF5350', fontSize: '1rem' }}>✗</span>
              }
            } else if (hintShown && isSelected) {
              bg = '#FFFBEA'; border = '#FFD93D'; textColor = '#7A5800'
              labelBg = '#FFD93D'; labelColor = '#7A5800'
            } else if (!revealed && !hintShown && isSelected) {
              bg = subject.bgColor; border = subject.color; textColor = '#1A1A2E'
              labelBg = subject.color; labelColor = 'white'
            }

            return (
              <button key={opt}
                onClick={() => handleAnswer(opt)}
                disabled={revealed || hintShown}
                className="w-full flex items-center gap-4 rounded-2xl text-left transition-all duration-200 active:scale-[0.98]"
                style={{
                  background: bg,
                  border: `2px solid ${border}`,
                  padding: '14px 16px',
                  opacity: isFaded ? 0.38 : 1,
                  cursor: (revealed || hintShown) ? 'default' : 'pointer',
                  boxShadow: (!revealed && !hintShown) ? '0 2px 8px rgba(0,0,0,0.05)' : 'none',
                }}>
                {/* Letter label */}
                <div className="w-8 h-8 rounded-xl flex items-center justify-center font-black text-sm flex-shrink-0 transition-all"
                  style={{ background: labelBg, color: labelColor }}>
                  {LABELS[idx]}
                </div>
                <span className="font-bold text-base flex-1" style={{ color: textColor }}>
                  {opt}
                </span>
                {icon && <span className="flex-shrink-0">{icon}</span>}
              </button>
            )
          })}
        </div>

        {/* Hint box */}
        {hintShown && ex.hint && (
          <div className="rounded-2xl overflow-hidden animate-fade-up"
            style={{ border: '2px solid #FFD93D' }}>
            <div className="px-4 py-2 flex items-center gap-2"
              style={{ background: '#FFD93D' }}>
              <span className="text-lg">💡</span>
              <span className="font-black text-sm" style={{ color: '#7A5800' }}>Намек</span>
            </div>
            <div className="px-4 py-3" style={{ background: '#FFFBEA' }}>
              <p className="text-sm font-semibold leading-relaxed" style={{ color: '#5C3D00' }}>
                {ex.hint}
              </p>
              <button onClick={handleRetry}
                className="mt-3 w-full py-3 rounded-xl font-black text-sm transition-all active:scale-95"
                style={{ background: '#FFD93D', color: '#1A1A2E' }}>
                Обиди се пак →
              </button>
            </div>
          </div>
        )}

        {/* Explanation after reveal */}
        {revealed && (
          <div className="rounded-2xl overflow-hidden animate-fade-up"
            style={{ border: `2px solid ${selected === ex.correct ? '#4CAF50' : '#EF5350'}` }}>
            <div className="px-4 py-2"
              style={{ background: selected === ex.correct ? '#4CAF50' : '#EF5350' }}>
              <span className="font-black text-sm text-white">
                {selected === ex.correct ? '✓ Точно!' : '✗ Неточен одговор'}
              </span>
            </div>
            <div className="px-4 py-3"
              style={{ background: selected === ex.correct ? '#EDFFF2' : '#FFF0F0' }}>
              <p className="text-sm font-semibold leading-relaxed" style={{ color: '#1A1A2E' }}>
                {ex.explanation}
              </p>
            </div>
          </div>
        )}

        {/* Next button */}
        {revealed && (
          <button onClick={handleNext}
            className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-[0.98] shadow-md animate-fade-up"
            style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
            {currentEx < exercises.length - 1 ? 'Следно прашање →' : 'Заврши! 🎉'}
          </button>
        )}
      </div>

      <style>{`
        @keyframes shake {
          0%, 100% { transform: translateX(0); }
          20% { transform: translateX(-6px); }
          40% { transform: translateX(6px); }
          60% { transform: translateX(-4px); }
          80% { transform: translateX(4px); }
        }
        .animate-shake { animation: shake 0.35s ease-in-out; }
      `}</style>
    </main>
  )

  // ── RESULTS PHASE ────────────────────────────────────────────────
  return (
    <main className="min-h-screen flex flex-col" style={{ background: '#F4F6FB' }}>

      <header className="px-5 py-4" style={{ background: subject.color }}>
        <div className="flex items-center gap-2">
          <span className="text-xl">{subject.emoji}</span>
          <span className="text-white font-black text-sm">{lesson.title}</span>
        </div>
      </header>

      <div className="flex-1 flex flex-col items-center justify-center px-6 text-center gap-6">

        {/* Trophy */}
        <div className="text-8xl animate-float">
          {starsEarned === 3 ? '🏆' : starsEarned === 2 ? '🥈' : starsEarned === 1 ? '🌟' : '💪'}
        </div>

        {/* Title */}
        <div>
          <h1 className="text-4xl font-black mb-2" style={{ color: '#1A1A2E' }}>
            {starsEarned === 3 ? 'Совршено!' : starsEarned >= 2 ? 'Одлично!' : starsEarned === 1 ? 'Добар почеток!' : 'Обиди се пак!'}
          </h1>
          <p className="font-semibold" style={{ color: '#6B6B8A' }}>
            {correct} од {exercises.length} точни одговори
          </p>
        </div>

        {/* Stars */}
        <div className="flex justify-center gap-3">
          {[1, 2, 3].map((s) => (
            <div key={s} className="flex flex-col items-center gap-1">
              <span className="text-5xl transition-all duration-500"
                style={{
                  filter: s <= starsEarned ? 'none' : 'grayscale(1) opacity(0.25)',
                  transform: s <= starsEarned ? 'scale(1.05)' : 'scale(0.9)',
                }}>⭐</span>
            </div>
          ))}
        </div>

        {/* Score bar */}
        <div className="w-full max-w-xs">
          <div className="h-3 rounded-full overflow-hidden" style={{ background: '#E8EAF0' }}>
            <div className="h-full rounded-full transition-all duration-700"
              style={{
                width: `${(correct / exercises.length) * 100}%`,
                background: starsEarned >= 2 ? '#4CAF50' : starsEarned === 1 ? '#FFD93D' : '#EF5350',
              }} />
          </div>
          <p className="text-xs font-semibold mt-1 text-center" style={{ color: '#9B9BAA' }}>
            {Math.round((correct / exercises.length) * 100)}% точност
          </p>
        </div>

        {/* Buttons */}
        <div className="flex flex-col gap-3 w-full max-w-xs">
          <button
            onClick={() => {
              setPhase('exercises')
              setCurrentEx(0); setSelected(null); setAnswered(false)
              setHintShown(false); setRevealed(false)
              setWrongAttempts([]); setCorrect(0)
            }}
            className="w-full py-4 rounded-2xl font-black text-base transition-all active:scale-[0.98]"
            style={{ background: 'white', color: subject.color, border: `2px solid ${subject.color}` }}>
            Повтори уште еднаш
          </button>
          <button onClick={() => router.push(`/subject/${subject.id}`)}
            className="w-full py-4 rounded-2xl font-black text-base text-white transition-all active:scale-[0.98] shadow-md"
            style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
            ← Назад кон {subject.nameMk}
          </button>
        </div>

      </div>
    </main>
  )
}
