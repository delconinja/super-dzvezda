'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useRef, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { getGradeContent, ExerciseData, VideoQuiz } from '@/lib/content'
import { convertToV2, v2GetPracticeCount, v2GetQuizBlock } from '@/lib/content-v2'
import { getSubject } from '@/lib/subjects'
import SubjectIcon from '@/components/SubjectIcon'
import StarMascot from '@/components/StarMascot'
import { getActiveStudent, saveProgress, refreshStudentSession, getSelectedGrade, StudentProfile } from '@/lib/auth'
import MathVisual from '@/components/math/MathVisual'
import DragDropExercise from '@/components/DragDropExercise'

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
  const [dragDropDone, setDragDropDone] = useState(false)

  const videoRef = useRef<HTMLVideoElement>(null)
  const audioRef = useRef<HTMLAudioElement | null>(null)
  const narrationCache = useRef<Map<string, string>>(new Map())
  const firedTimestamps = useRef<Set<number>>(new Set())
  const dismissTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const talkTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const currentNarrationRef = useRef<string | null>(null)
  const lastNarrationTs = useRef<number>(-1)
  const [videoPlaying, setVideoPlaying] = useState(false)
  const [currentNarration, setCurrentNarration] = useState<string | null>(null)
  const [isSpeaking, setIsSpeaking] = useState(false)
  const [videoQuizActive, setVideoQuizActive] = useState(false)
  const [videoQuizQuestion, setVideoQuizQuestion] = useState<VideoQuiz | null>(null)
  const [videoQuizTimeLeft, setVideoQuizTimeLeft] = useState(10)
  const [videoQuizSelected, setVideoQuizSelected] = useState<string | null>(null)
  const [videoQuizAnswered, setVideoQuizAnswered] = useState(false)

  const activeStudent = getActiveStudent()
  const selectedGrade = getSelectedGrade()
  const gradeContent = getGradeContent(selectedGrade)

  const lesson = Object.values(gradeContent)
    .flatMap((units) => units.flatMap((u) => u.lessons))
    .find((l) => l.id === lessonId)

  const subjectId = Object.entries(gradeContent).find(([, units]) =>
    units.some((u) => u.lessons.some((l) => l.id === lessonId))
  )?.[0]

  const subject = getSubject(subjectId ?? '')

  const v2Lesson = (selectedGrade === 5 && lesson) ? convertToV2(lesson) : null
  const practiceCount = v2Lesson ? v2GetPracticeCount(v2Lesson) : (lesson?.exercises.length ?? 0)

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

  const handleDragDropComplete = () => {
    setCorrect((c) => c + 1)
    setRevealed(true)
    setShowStar(true)
    setTimeout(() => setShowStar(false), 900)
    setDragDropDone(true)
  }

  const handleRetry = () => {
    setSelected(null)
    setAnswered(false)
    setHintShown(false)
  }

  const stopNarration = () => {
    if (audioRef.current) { audioRef.current.pause(); audioRef.current.onended = null }
    if (talkTimerRef.current) { clearTimeout(talkTimerRef.current); talkTimerRef.current = null }
    setIsSpeaking(false)
  }

  const playAudioUrl = (url: string) => {
    stopNarration()
    const audio = new Audio(url)
    audioRef.current = audio
    audio.onplay = () => setIsSpeaking(true)
    audio.onended = () => setIsSpeaking(false)
    audio.onerror = () => setIsSpeaking(false)
    audio.play().catch(() => setIsSpeaking(false))
  }

  const speakText = async (text: string) => {
    if (narrationCache.current.has(text)) {
      playAudioUrl(narrationCache.current.get(text)!)
      return
    }
    try {
      const res = await fetch('/api/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      })
      if (!res.ok) throw new Error('tts failed')
      const blob = await res.blob()
      const url = URL.createObjectURL(blob)
      narrationCache.current.set(text, url)
      playAudioUrl(url)
    } catch {
      // Fallback: silent talking animation
      setIsSpeaking(true)
      talkTimerRef.current = setTimeout(() => setIsSpeaking(false), Math.max(2500, text.length * 65))
    }
  }

  const handleVideoPlay = () => {
    setVideoPlaying(true)
    if (currentNarrationRef.current) speakText(currentNarrationRef.current)
  }

  const handleVideoPause = () => {
    setVideoPlaying(false)
    stopNarration()
  }

  useEffect(() => {
    return () => {
      if (audioRef.current) audioRef.current.pause()
      if (talkTimerRef.current) clearTimeout(talkTimerRef.current)
    }
  }, [])

  // Pre-fetch all narration audio so there's no delay when cues trigger
  useEffect(() => {
    if (!lesson?.videoNarration?.length) return
    lesson.videoNarration.forEach(async (cue) => {
      if (narrationCache.current.has(cue.text)) return
      try {
        const res = await fetch('/api/tts', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: cue.text }),
        })
        if (!res.ok) return
        const blob = await res.blob()
        narrationCache.current.set(cue.text, URL.createObjectURL(blob))
      } catch { /* silently fail — speakText will retry on demand */ }
    })
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lesson?.id])

  const handleTimeUpdate = () => {
    if (!videoRef.current) return
    const currentTime = videoRef.current.currentTime

    // Video quizzes
    if (lesson?.videoQuizzes?.length) {
      for (const quiz of lesson.videoQuizzes) {
        if (!firedTimestamps.current.has(quiz.timestamp) && currentTime >= quiz.timestamp) {
          firedTimestamps.current.add(quiz.timestamp)
          videoRef.current.pause()
          stopNarration()
          setVideoQuizQuestion(quiz)
          setVideoQuizTimeLeft(10)
          setVideoQuizSelected(null)
          setVideoQuizAnswered(false)
          setVideoQuizActive(true)
          break
        }
      }
    }

    // Narration cues
    if (lesson?.videoNarration?.length) {
      const sorted = [...lesson.videoNarration].sort((a, b) => b.timestamp - a.timestamp)
      const activeCue = sorted.find((c) => currentTime >= c.timestamp)
      if (activeCue && activeCue.timestamp !== lastNarrationTs.current) {
        lastNarrationTs.current = activeCue.timestamp
        currentNarrationRef.current = activeCue.text
        setCurrentNarration(activeCue.text)
        speakText(activeCue.text)
      }
    }
  }

  const dismissVideoQuiz = () => {
    dismissTimerRef.current = null
    setVideoQuizActive(false)
    setVideoQuizQuestion(null)
    setVideoQuizTimeLeft(10)
    setVideoQuizSelected(null)
    setVideoQuizAnswered(false)
    videoRef.current?.play()
  }

  const handleVideoQuizAnswer = (option: string) => {
    if (videoQuizAnswered) return
    setVideoQuizSelected(option)
    setVideoQuizAnswered(true)
    if (dismissTimerRef.current) clearTimeout(dismissTimerRef.current)
    dismissTimerRef.current = setTimeout(dismissVideoQuiz, 5000)
  }

  useEffect(() => {
    if (!videoQuizActive || videoQuizAnswered) return
    if (videoQuizTimeLeft <= 0) {
      setVideoQuizAnswered(true)
      // Store in ref so React cleanup cannot cancel it
      dismissTimerRef.current = setTimeout(dismissVideoQuiz, 5000)
      return
    }
    const t = setTimeout(() => setVideoQuizTimeLeft((n) => n - 1), 1000)
    return () => clearTimeout(t)
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [videoQuizActive, videoQuizTimeLeft, videoQuizAnswered])

  const handleNext = () => {
    if (currentEx < exercises.length - 1) {
      setCurrentEx((i) => i + 1)
      setSelected(null)
      setAnswered(false)
      setHintShown(false)
      setRevealed(false)
      setWrongAttempts([])
      setDragDropDone(false)
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
        <SubjectIcon subject={subject} size="sm" />
        <span className="text-white font-black text-base leading-tight flex-1">{lesson.title}</span>
      </header>

      <div className="max-w-xl mx-auto px-4 py-6 pb-28">

        {/* Lesson content card */}
        <div className="rounded-3xl overflow-hidden shadow-sm" style={{ background: 'white' }}>

          {/* Subject colour band */}
          <div className="px-6 pt-5 pb-3 flex items-center gap-3"
            style={{ background: `${subject.color}12`, borderBottom: `3px solid ${subject.color}` }}>
            <SubjectIcon subject={subject} size="md" />
            <div>
              <p className="text-xs font-bold tracking-widest uppercase" style={{ color: subject.color }}>
                {subject.nameMk}
              </p>
              <p className="font-black text-lg leading-tight" style={{ color: '#1A1A2E' }}>
                {lesson.title}
              </p>
            </div>
          </div>

          {/* Learning objectives — V2 Grade 5 only */}
          {v2Lesson && v2Lesson.learningObjectives.length > 0 && (
            <div className="px-6 pt-4 pb-1">
              <p className="text-xs font-black tracking-widest uppercase mb-2" style={{ color: '#9B9BAA' }}>
                Цели на лекцијата
              </p>
              <ul className="flex flex-col gap-1.5">
                {v2Lesson.learningObjectives.map((obj, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm font-semibold" style={{ color: '#2D2D44' }}>
                    <span style={{ color: subject.color, fontWeight: 900 }}>✓</span>
                    {obj}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Video explainer */}
          {lesson.videoUrl && (
            <div className="px-4 pt-4 pb-2">
              <video
                ref={videoRef}
                src={lesson.videoUrl}
                controls
                playsInline
                onTimeUpdate={handleTimeUpdate}
                onPlay={handleVideoPlay}
                onPause={handleVideoPause}
                className="w-full rounded-2xl overflow-hidden"
                style={{ background: '#0D1B2A', maxHeight: 240 }}
              />
            </div>
          )}

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

      {/* Star mascot */}
      {lesson.videoUrl && lesson.videoNarration?.length && (
        <div className="fixed bottom-28 right-3 z-40 flex items-end gap-2 pointer-events-none">
          {currentNarration && (
            <div style={{ position: 'relative' }}>
              <div
                className="bg-white rounded-2xl px-3 py-2.5 shadow-xl text-xs font-semibold leading-relaxed"
                style={{ color: '#1A1A2E', border: '2px solid #FFD93D', maxWidth: 160 }}>
                {currentNarration}
              </div>
              {/* Tail pointing right toward mascot */}
              <div style={{ position: 'absolute', right: -9, bottom: 14, width: 0, height: 0,
                borderTop: '7px solid transparent', borderBottom: '7px solid transparent',
                borderLeft: '9px solid #FFD93D' }} />
              <div style={{ position: 'absolute', right: -6, bottom: 15, width: 0, height: 0,
                borderTop: '6px solid transparent', borderBottom: '6px solid transparent',
                borderLeft: '8px solid white' }} />
            </div>
          )}
          <StarMascot talking={isSpeaking} size={64} />
        </div>
      )}

      {/* Video quiz overlay */}
      {videoQuizActive && videoQuizQuestion && (
        <div className="fixed inset-0 z-50 flex items-end justify-center pb-6 px-4"
          style={{ background: 'rgba(0,0,0,0.78)' }}>
          <div className="w-full max-w-xl rounded-3xl overflow-hidden shadow-2xl animate-fade-up">

            {/* Header + countdown number */}
            <div className="px-5 py-3 flex items-center justify-between"
              style={{ background: subject.color }}>
              <span className="text-white font-black text-sm">💡 Прашање</span>
              <div className="flex items-center gap-1.5">
                <span className="text-white/70 text-sm">⏱</span>
                <span className="text-white font-black text-xl w-6 text-right">
                  {videoQuizTimeLeft}
                </span>
              </div>
            </div>

            {/* Countdown bar */}
            <div className="h-2" style={{ background: '#E8EAF0' }}>
              <div className="h-2 transition-all duration-1000"
                style={{
                  width: `${(videoQuizTimeLeft / 10) * 100}%`,
                  background: videoQuizTimeLeft <= 3 ? '#EF5350' : subject.color,
                }} />
            </div>

            {/* Question */}
            <div className="px-5 pt-4 pb-3" style={{ background: 'white' }}>
              <p className="font-black text-lg leading-snug" style={{ color: '#1A1A2E' }}>
                {videoQuizQuestion.question}
              </p>
            </div>

            {/* Options */}
            <div className="px-5 pb-5 flex flex-col gap-2.5" style={{ background: 'white' }}>
              {videoQuizQuestion.options.map((opt, idx) => {
                const isCorrect = opt === videoQuizQuestion.correctAnswer
                const isSelected = videoQuizSelected === opt
                let bg = 'white', border = '#E8EAF0', textColor = '#1A1A2E'
                let labelBg = '#F0F0F8', labelColor = '#9B9BAA'
                if (videoQuizAnswered) {
                  if (isCorrect) { bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20'; labelBg = '#4CAF50'; labelColor = 'white' }
                  else if (isSelected) { bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C'; labelBg = '#EF5350'; labelColor = 'white' }
                } else if (isSelected) {
                  bg = subject.bgColor; border = subject.color; labelBg = subject.color; labelColor = 'white'
                }
                return (
                  <button key={opt}
                    onClick={() => handleVideoQuizAnswer(opt)}
                    disabled={videoQuizAnswered}
                    className="w-full flex items-center gap-3 rounded-2xl text-left transition-all duration-200 active:scale-[0.98]"
                    style={{ background: bg, border: `2px solid ${border}`, padding: '12px 14px',
                      cursor: videoQuizAnswered ? 'default' : 'pointer' }}>
                    <div className="w-7 h-7 rounded-lg flex items-center justify-center font-black text-xs flex-shrink-0"
                      style={{ background: labelBg, color: labelColor }}>
                      {LABELS[idx]}
                    </div>
                    <span className="font-semibold text-sm flex-1" style={{ color: textColor }}>{opt}</span>
                    {videoQuizAnswered && isCorrect && <span style={{ color: '#4CAF50' }}>✓</span>}
                    {videoQuizAnswered && isSelected && !isCorrect && <span style={{ color: '#EF5350' }}>✗</span>}
                  </button>
                )
              })}

              {/* Time ran out message */}
              {videoQuizAnswered && !videoQuizSelected && (
                <p className="text-center text-sm font-bold pt-1" style={{ color: '#9B9BAA' }}>
                  Времето истече! Точен одговор: <span style={{ color: '#4CAF50' }}>{videoQuizQuestion.correctAnswer}</span>
                </p>
              )}
            </div>
          </div>
        </div>
      )}

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
          <div className="text-8xl leading-none overflow-hidden animate-star-pop">⭐</div>
        </div>
      )}

      {/* Header */}
      <header className="px-5 py-3 flex items-center justify-between"
        style={{ background: subject.color }}>
        <div className="flex items-center gap-2">
          <SubjectIcon subject={subject} size="sm" />
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

      <div className="flex-1 flex flex-col max-w-xl w-full mx-auto px-4 py-4 gap-3">

        {/* Mastery check banner — V2 Grade 5 only */}
        {v2Lesson && currentEx === practiceCount && (
          <div className="rounded-2xl overflow-hidden animate-fade-up"
            style={{ border: '2px solid #7C3AED' }}>
            <div className="px-4 py-2.5 flex items-center gap-2" style={{ background: '#7C3AED' }}>
              <span className="text-white font-black text-sm">🎯 Мастерски тест</span>
              <span className="text-white/70 text-xs ml-auto">80% за поминување</span>
            </div>
            <div className="px-4 py-2.5" style={{ background: '#F5F0FF' }}>
              <p className="text-xs font-semibold" style={{ color: '#4C1D95' }}>
                Последните {v2GetQuizBlock(v2Lesson)?.questions.length} прашања проверуваат дали ја совладавте темата.
              </p>
            </div>
          </div>
        )}

        {/* Question card — visual + text */}
        <div className="rounded-3xl overflow-hidden shadow-sm" style={{ background: 'white' }}>

          {/* Visual diagram */}
          {ex.visual && (
            <div className="flex items-center justify-center px-5 pt-5 pb-2">
              <MathVisual {...ex.visual} color={subject.color} />
            </div>
          )}

          {/* Question type tag */}
          <div className="px-5 pt-4 pb-1">
            <span className="text-xs font-black tracking-widest uppercase"
              style={{ color: subject.color, opacity: 0.7 }}>
              {ex.type === 'true-false' ? 'Точно или Неточно?' : 'Одбери точен одговор'}
            </span>
          </div>

          {/* Question text */}
          <div className="px-5 pb-5">
            <p className="font-black leading-snug" style={{ color: '#1A1A2E', fontSize: '1.1rem' }}>
              {ex.question}
            </p>
          </div>
        </div>

        {/* Drag-drop exercise */}
        {ex.type === 'drag-drop' && ex.dragItems && ex.dragTargets && (
          <DragDropExercise
            items={ex.dragItems}
            targets={ex.dragTargets}
            color={subject.color}
            explanation={ex.explanation}
            onComplete={handleDragDropComplete}
          />
        )}

        {/* Options — chip-style for T/F, full-width for multiple choice */}
        {ex.type !== 'drag-drop' && (
          ex.type === 'true-false' ? (
            // True/False — two large equal chips
            <div className={`grid grid-cols-2 gap-3 ${shake ? 'animate-shake' : ''}`}>
              {(['Точно', 'Неточно'] as const).map((opt) => {
                const isCorrect = opt === ex.correct
                const isWrong = wrongAttempts.includes(opt)
                const isSelected = selected === opt
                let bg = 'white', border = '#E8EAF0', textColor = '#1A1A2E', icon = ''
                if (revealed) {
                  if (isCorrect) { bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20'; icon = ' ✓' }
                  else if (isWrong) { bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C'; icon = ' ✗' }
                } else if (hintShown && isSelected) {
                  bg = '#FFFBEA'; border = '#FFD93D'; textColor = '#7A5800'
                } else if (isSelected) {
                  bg = subject.bgColor; border = subject.color
                }
                return (
                  <button key={opt} onClick={() => handleAnswer(opt)}
                    disabled={revealed || hintShown}
                    className="py-4 rounded-2xl font-black text-base transition-all duration-200 active:scale-[0.97]"
                    style={{ background: bg, border: `2px solid ${border}`, color: textColor,
                      opacity: (!revealed && !hintShown && wrongAttempts.includes(opt)) ? 0.35 : 1 }}>
                    {opt}{icon}
                  </button>
                )
              })}
            </div>
          ) : (
            // Multiple choice — full-width with letter badge
            <div className={`flex flex-col gap-2.5 ${shake ? 'animate-shake' : ''}`}>
              {(ex.options || []).map((opt, idx) => {
                const isCorrect = opt === ex.correct
                const isWrong = wrongAttempts.includes(opt)
                const isSelected = selected === opt
                const isFaded = !revealed && !hintShown && wrongAttempts.includes(opt)
                let bg = 'white', border = '#E8EAF0', textColor = '#1A1A2E'
                let labelBg = '#F0F0F8', labelColor = '#9B9BAA'
                let icon = null
                if (revealed) {
                  if (isCorrect) {
                    bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20'
                    labelBg = '#4CAF50'; labelColor = 'white'
                    icon = <span style={{ color: '#4CAF50' }}>✓</span>
                  } else if (isWrong) {
                    bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C'
                    labelBg = '#EF5350'; labelColor = 'white'
                    icon = <span style={{ color: '#EF5350' }}>✗</span>
                  }
                } else if (hintShown && isSelected) {
                  bg = '#FFFBEA'; border = '#FFD93D'; textColor = '#7A5800'
                  labelBg = '#FFD93D'; labelColor = '#7A5800'
                } else if (isSelected) {
                  bg = subject.bgColor; border = subject.color
                  labelBg = subject.color; labelColor = 'white'
                }
                return (
                  <button key={opt} onClick={() => handleAnswer(opt)}
                    disabled={revealed || hintShown}
                    className="w-full flex items-center gap-3 rounded-2xl text-left transition-all duration-200 active:scale-[0.98]"
                    style={{ background: bg, border: `2px solid ${border}`,
                      padding: '12px 14px', opacity: isFaded ? 0.35 : 1,
                      cursor: (revealed || hintShown) ? 'default' : 'pointer' }}>
                    <div className="w-7 h-7 rounded-lg flex items-center justify-center font-black text-xs flex-shrink-0"
                      style={{ background: labelBg, color: labelColor }}>
                      {LABELS[idx]}
                    </div>
                    <span className="font-semibold text-sm flex-1" style={{ color: textColor }}>{opt}</span>
                    {icon && <span className="flex-shrink-0 text-sm">{icon}</span>}
                  </button>
                )
              })}
            </div>
          )
        )}

        {/* Hint box — not shown for drag-drop */}
        {ex.type !== 'drag-drop' && hintShown && ex.hint && (
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

        {/* Explanation after reveal — not shown for drag-drop (component shows its own) */}
        {ex.type !== 'drag-drop' && revealed && (
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
        {(revealed || dragDropDone) && (
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
          <SubjectIcon subject={subject} size="sm" />
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
              <span className="text-5xl leading-none overflow-hidden transition-all duration-500"
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

        {/* XP reward — V2 Grade 5 only */}
        {v2Lesson && (
          <div className="flex items-center gap-3 px-5 py-3 rounded-2xl w-full max-w-xs"
            style={{ background: '#FFF9E6', border: '2px solid #FFD93D' }}>
            <span className="text-2xl">⚡</span>
            <div className="text-left">
              <p className="font-black text-base" style={{ color: '#7A5800' }}>+{v2Lesson.xpReward} XP</p>
              <p className="text-xs font-semibold" style={{ color: '#9B7B00' }}>Освоени поени</p>
            </div>
          </div>
        )}

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
