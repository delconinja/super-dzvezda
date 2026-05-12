'use client'

export const dynamic = 'force-dynamic'

import { useEffect, useRef, useState } from 'react'
import { useRouter, useParams } from 'next/navigation'
import { getGradeContent, ExerciseData } from '@/lib/content'
import { getActiveStudent, getSelectedGrade, StudentProfile } from '@/lib/auth'
import { getSubject } from '@/lib/subjects'
import { getBadgeDef, TIER_COLORS } from '@/lib/badges'
import SubjectIcon from '@/components/SubjectIcon'
import MathVisual from '@/components/math/MathVisual'

const LABELS = ['А', 'Б', 'В', 'Г', 'Д']

const DIFFICULTY_META = {
  easy:   { label: 'Лесно',  color: '#FFD93D', bg: '#FFFBEA', textColor: '#7A5800' },
  medium: { label: 'Средно', color: '#4CAF50', bg: '#EDFFF2', textColor: '#1B5E20' },
  hard:   { label: 'Тешко',  color: '#2196F3', bg: '#E3F2FD', textColor: '#0D47A1' },
}

const STAR_COLORS = { yellow: '#FFD93D', green: '#4CAF50', blue: '#2196F3' }

function Star({ color, size = '1.5rem' }: { color: string; size?: string }) {
  return <span style={{ color, fontSize: size, lineHeight: 1, display: 'inline-block' }}>★</span>
}

type ChallengeStars = { yellow: boolean; green: boolean; blue: boolean; attempts?: number }

async function fetchChallengeStars(studentId: string, unitId: string): Promise<ChallengeStars> {
  try {
    const res = await fetch(`/api/save-challenge-stars?studentId=${studentId}&unitId=${unitId}`)
    if (!res.ok) return { yellow: false, green: false, blue: false }
    return await res.json()
  } catch { return { yellow: false, green: false, blue: false } }
}

type Phase = 'intro' | 'quiz' | 'results'

export default function ChallengePage() {
  const router = useRouter()
  const params = useParams()
  const unitId = params.unitId as string

  const [student, setStudent] = useState<StudentProfile | null>(null)
  const [phase, setPhase] = useState<Phase>('intro')
  const [currentIdx, setCurrentIdx] = useState(0)
  const [selected, setSelected] = useState<string | null>(null)
  const [revealed, setRevealed] = useState(false)
  const [shake, setShake] = useState(false)
  const [alreadyAnswered, setAlreadyAnswered] = useState(false)
  const [earnedStars, setEarnedStars] = useState<ChallengeStars>({ yellow: false, green: false, blue: false })
  const [savedStars, setSavedStars] = useState<ChallengeStars>({ yellow: false, green: false, blue: false })
  const [newlyEarned, setNewlyEarned] = useState({ yellow: false, green: false, blue: false })
  const [newBadgeIds, setNewBadgeIds] = useState<string[]>([])
  const [saving, setSaving] = useState(false)

  const firstTryCorrect = useRef<boolean[]>([])

  const gradeContent = getGradeContent(getSelectedGrade())

  let unitData = null
  let subjectId = ''
  for (const [sid, units] of Object.entries(gradeContent)) {
    const found = units.find(u => u.id === unitId)
    if (found) { unitData = found; subjectId = sid; break }
  }

  const subject = getSubject(subjectId)
  const challengeLesson = unitData?.lessons.find(l => l.isChallenge)
  const exercises: ExerciseData[] = challengeLesson?.exercises || []

  useEffect(() => {
    const init = async () => {
      const active = getActiveStudent()
      if (!active) { router.push('/'); return }
      setStudent(active)
      const stars = await fetchChallengeStars(active.id, unitId)
      setSavedStars(stars)
    }
    init()
  }, [router, unitId])

  if (!unitData || !subject || !challengeLesson || exercises.length === 0) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <p style={{ color: '#6B6B8A' }}>Предизвикот не е пронајден.</p>
    </div>
  )

  const ex = exercises[currentIdx]
  const diff = ex?.difficulty ? DIFFICULTY_META[ex.difficulty] : DIFFICULTY_META.easy

  const easyCount   = exercises.filter(e => e.difficulty === 'easy').length
  const mediumCount = exercises.filter(e => e.difficulty === 'medium').length
  const hardCount   = exercises.filter(e => e.difficulty === 'hard').length

  const handleStart = () => {
    firstTryCorrect.current = []
    setCurrentIdx(0)
    setSelected(null)
    setRevealed(false)
    setAlreadyAnswered(false)
    setNewBadgeIds([])
    setPhase('quiz')
  }

  const handleAnswer = (option: string) => {
    if (revealed || alreadyAnswered) return
    setSelected(option)
    setAlreadyAnswered(true)
    firstTryCorrect.current[currentIdx] = option === ex.correct
    if (option !== ex.correct) {
      setShake(true)
      setTimeout(() => setShake(false), 400)
    }
    setRevealed(true)
  }

  const handleNext = async () => {
    if (currentIdx < exercises.length - 1) {
      setCurrentIdx(i => i + 1)
      setSelected(null)
      setRevealed(false)
      setAlreadyAnswered(false)
    } else {
      const ftc = firstTryCorrect.current
      const easyExs   = exercises.map((e, i) => ({ e, ok: ftc[i] })).filter(x => x.e.difficulty === 'easy')
      const mediumExs = exercises.map((e, i) => ({ e, ok: ftc[i] })).filter(x => x.e.difficulty === 'medium')
      const hardExs   = exercises.map((e, i) => ({ e, ok: ftc[i] })).filter(x => x.e.difficulty === 'hard')

      const yellow = easyExs.length   > 0 && easyExs.every(x => x.ok)
      const green  = mediumExs.length > 0 && mediumExs.every(x => x.ok)
      const blue   = hardExs.length   > 0 && hardExs.every(x => x.ok)

      setEarnedStars({ yellow, green, blue })

      if (student) {
        setSaving(true)
        try {
          const res = await fetch('/api/save-challenge-stars', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ studentId: student.id, unitId, yellow, green, blue }),
          })
          const data = await res.json()
          const merged = { yellow: data.yellow, green: data.green, blue: data.blue }
          setNewlyEarned({
            yellow: yellow && !savedStars.yellow,
            green:  green  && !savedStars.green,
            blue:   blue   && !savedStars.blue,
          })
          setSavedStars(merged)
          setNewBadgeIds(data.newBadgeIds || [])
        } catch { /* silent */ } finally {
          setSaving(false)
        }
      }

      setPhase('results')
    }
  }

  // ── INTRO ─────────────────────────────────────────────────────────
  if (phase === 'intro') return (
    <main className="min-h-screen flex flex-col" style={{ background: '#F7F5FF' }}>
      <header className="px-5 py-4 flex items-center gap-3" style={{ background: subject.color }}>
        <button onClick={() => router.push(`/subject/${subjectId}`)}
          className="w-9 h-9 rounded-xl flex items-center justify-center transition-all active:scale-90"
          style={{ background: 'rgba(255,255,255,0.18)' }}>
          <span className="text-white font-bold text-lg">{'←'}</span>
        </button>
        <SubjectIcon subject={subject} size="sm" />
        <span className="text-white font-black text-base flex-1">Предизвик</span>
      </header>

      <div className="flex-1 flex flex-col items-center justify-center px-6 gap-6 max-w-md mx-auto w-full">
        <div className="text-7xl animate-bounce">🏆</div>

        <div className="text-center">
          <h1 className="text-3xl font-black mb-2" style={{ color: '#1A1A2E' }}>Предизвик!</h1>
          <p className="font-semibold text-base" style={{ color: '#6B6B8A' }}>{unitData.title}</p>
        </div>

        <div className="w-full bg-white rounded-3xl p-5 space-y-3" style={{ boxShadow: '0 4px 16px rgba(0,0,0,0.07)' }}>
          {([
            { key: 'easy',   color: STAR_COLORS.yellow, label: 'Жолта ѕвезда', desc: `${easyCount} лесни прашања — сите точни на прв обид`, saved: savedStars.yellow },
            { key: 'medium', color: STAR_COLORS.green,  label: 'Зелена ѕвезда', desc: `${mediumCount} средни прашања — сите точни на прв обид`, saved: savedStars.green },
            { key: 'hard',   color: STAR_COLORS.blue,   label: 'Сина ѕвезда',   desc: `${hardCount} тешки прашања — сите точни на прв обид`,  saved: savedStars.blue },
          ] as const).map(item => (
            <div key={item.key} className="flex items-center gap-3">
              <Star color={item.color} size="1.8rem" />
              <div className="flex-1">
                <p className="font-black text-sm" style={{ color: '#1A1A2E' }}>{item.label}</p>
                <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>{item.desc}</p>
              </div>
              {item.saved && <span className="font-black text-sm" style={{ color: '#4CAF50' }}>Освоена ✓</span>}
            </div>
          ))}
        </div>

        <div className="w-full bg-amber-50 rounded-2xl px-4 py-3 border-2 border-amber-200">
          <p className="text-sm font-bold text-center" style={{ color: '#7A5800' }}>
            {'💡 Нема намеци! Одговори точно на прв обид за да освоиш ѕвезда.'}
          </p>
        </div>

        <button onClick={handleStart}
          className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-[0.98] shadow-lg"
          style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
          {'Започни предизвик →'}
        </button>
      </div>
    </main>
  )

  // ── QUIZ ──────────────────────────────────────────────────────────
  if (phase === 'quiz') return (
    <main className="min-h-screen flex flex-col" style={{ background: '#F4F6FB' }}>
      <header className="px-5 py-3 flex items-center justify-between" style={{ background: subject.color }}>
        <div className="flex items-center gap-2">
          <SubjectIcon subject={subject} size="sm" />
          <span className="text-white font-black text-sm">Предизвик</span>
        </div>
        <span className="text-white/80 text-sm font-bold">{currentIdx + 1} / {exercises.length}</span>
      </header>

      <div className="h-1.5 w-full" style={{ background: 'rgba(0,0,0,0.06)' }}>
        <div className="h-1.5 transition-all duration-500 rounded-r-full"
          style={{ width: `${(currentIdx / exercises.length) * 100}%`, background: diff.color }} />
      </div>

      <div className="flex-1 flex flex-col max-w-xl w-full mx-auto px-4 py-4 gap-3">
        <div className="flex justify-center">
          <span className="px-4 py-1.5 rounded-full text-sm font-black flex items-center gap-1"
            style={{ background: diff.bg, color: diff.textColor, border: `2px solid ${diff.color}` }}>
            <Star color={diff.color} size="1rem" /> {diff.label}
          </span>
        </div>

        <div className="rounded-3xl overflow-hidden shadow-sm" style={{ background: 'white' }}>
          {ex.visual && (
            <div className="flex items-center justify-center px-5 pt-5 pb-2">
              <MathVisual {...ex.visual} color={subject.color} />
            </div>
          )}
          <div className="px-5 pt-4 pb-1">
            <span className="text-xs font-black tracking-widest uppercase"
              style={{ color: subject.color, opacity: 0.7 }}>
              {ex.type === 'true-false' ? 'Точно или Неточно?' : 'Одбери точен одговор'}
            </span>
          </div>
          <div className="px-5 pb-5">
            <p className="font-black leading-snug" style={{ color: '#1A1A2E', fontSize: '1.1rem' }}>
              {ex.question}
            </p>
          </div>
        </div>

        {ex.type === 'true-false' ? (
          <div className={`grid grid-cols-2 gap-3 ${shake ? 'animate-shake' : ''}`}>
            {(['Точно', 'Неточно'] as const).map((opt) => {
              const isCorrect = opt === ex.correct
              const isSelected = selected === opt
              let bg = 'white', border = '#E8EAF0', textColor = '#1A1A2E'
              if (revealed) {
                if (isCorrect) { bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20' }
                else if (isSelected && !isCorrect) { bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C' }
              } else if (isSelected) { bg = subject.bgColor; border = subject.color }
              return (
                <button key={opt} onClick={() => handleAnswer(opt)} disabled={revealed}
                  className="py-4 rounded-2xl font-black text-base transition-all duration-200 active:scale-[0.97]"
                  style={{ background: bg, border: `2px solid ${border}`, color: textColor }}>
                  {opt}{revealed && isCorrect ? ' ✓' : revealed && isSelected && !isCorrect ? ' ✗' : ''}
                </button>
              )
            })}
          </div>
        ) : (
          <div className={`flex flex-col gap-2.5 ${shake ? 'animate-shake' : ''}`}>
            {(ex.options || []).map((opt, idx) => {
              const isCorrect = opt === ex.correct
              const isSelected = selected === opt
              let bg = 'white', border = '#E8EAF0', textColor = '#1A1A2E'
              let labelBg = '#F0F0F8', labelColor = '#9B9BAA'
              let icon = null
              if (revealed) {
                if (isCorrect) { bg = '#EDFFF2'; border = '#4CAF50'; textColor = '#1B5E20'; labelBg = '#4CAF50'; labelColor = 'white'; icon = <span style={{ color: '#4CAF50' }}>✓</span> }
                else if (isSelected) { bg = '#FFF0F0'; border = '#EF5350'; textColor = '#B71C1C'; labelBg = '#EF5350'; labelColor = 'white'; icon = <span style={{ color: '#EF5350' }}>✗</span> }
              } else if (isSelected) { bg = subject.bgColor; border = subject.color; labelBg = subject.color; labelColor = 'white' }
              return (
                <button key={opt} onClick={() => handleAnswer(opt)} disabled={revealed}
                  className="w-full flex items-center gap-3 rounded-2xl text-left transition-all duration-200 active:scale-[0.98]"
                  style={{ background: bg, border: `2px solid ${border}`, padding: '12px 14px', cursor: revealed ? 'default' : 'pointer' }}>
                  <div className="w-7 h-7 rounded-lg flex items-center justify-center font-black text-xs flex-shrink-0"
                    style={{ background: labelBg, color: labelColor }}>{LABELS[idx]}</div>
                  <span className="font-semibold text-sm flex-1" style={{ color: textColor }}>{opt}</span>
                  {icon && <span className="flex-shrink-0 text-sm">{icon}</span>}
                </button>
              )
            })}
          </div>
        )}

        {revealed && (
          <div className="rounded-2xl overflow-hidden animate-fade-up"
            style={{ border: `2px solid ${selected === ex.correct ? '#4CAF50' : '#EF5350'}` }}>
            <div className="px-4 py-2" style={{ background: selected === ex.correct ? '#4CAF50' : '#EF5350' }}>
              <span className="font-black text-sm text-white">
                {selected === ex.correct ? '✓ Точно!' : '✗ Неточен одговор'}
              </span>
            </div>
            <div className="px-4 py-3" style={{ background: selected === ex.correct ? '#EDFFF2' : '#FFF0F0' }}>
              <p className="text-sm font-semibold leading-relaxed" style={{ color: '#1A1A2E' }}>{ex.explanation}</p>
            </div>
          </div>
        )}

        {revealed && (
          <button onClick={handleNext}
            className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-[0.98] shadow-md animate-fade-up"
            style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
            {currentIdx < exercises.length - 1 ? 'Следно прашање →' : 'Погледни резултат 🎉'}
          </button>
        )}
      </div>

      <style>{`
        @keyframes shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-6px)} 40%{transform:translateX(6px)} 60%{transform:translateX(-4px)} 80%{transform:translateX(4px)} }
        .animate-shake{animation:shake 0.35s ease-in-out}
      `}</style>
    </main>
  )

  // ── RESULTS ──────────────────────────────────────────────────────
  const anyEarned = earnedStars.yellow || earnedStars.green || earnedStars.blue
  const allThree  = earnedStars.yellow && earnedStars.green && earnedStars.blue

  return (
    <main className="min-h-screen flex flex-col" style={{ background: '#F4F6FB' }}>

      {anyEarned && (
        <div className="fixed inset-0 pointer-events-none z-50 overflow-hidden">
          {Array.from({ length: 48 }).map((_, i) => (
            <div key={i} className="confetti-piece"
              style={{
                left: `${Math.random() * 100}%`,
                animationDelay: `${Math.random() * 2}s`,
                animationDuration: `${2 + Math.random() * 2}s`,
                background: ['#FFD93D', '#4CAF50', '#2196F3', '#FF6B6B', '#9C27B0', '#FF9800'][i % 6],
                width: `${6 + Math.random() * 6}px`, height: `${6 + Math.random() * 6}px`,
                borderRadius: Math.random() > 0.5 ? '50%' : '2px',
              }} />
          ))}
        </div>
      )}

      <header className="px-5 py-4" style={{ background: subject.color }}>
        <div className="flex items-center gap-2">
          <SubjectIcon subject={subject} size="sm" />
          <span className="text-white font-black text-sm">Резултати од предизвикот</span>
        </div>
      </header>

      <div className="flex-1 flex flex-col items-center justify-center px-6 text-center gap-5 max-w-md mx-auto w-full py-8">

        <div className="text-8xl animate-float">
          {allThree ? '🏆' : anyEarned ? '🌟' : '💪'}
        </div>

        <div>
          <h1 className="text-3xl font-black mb-2" style={{ color: '#1A1A2E' }}>
            {allThree ? 'Совршено!' : anyEarned ? 'Одлично!' : 'Обиди се пак!'}
          </h1>
          <p className="font-semibold" style={{ color: '#6B6B8A' }}>
            {allThree ? 'Ги освои сите три ѕвезди!' : anyEarned ? 'Освои нови ѕвезди!' : 'Не секогаш успеваме на прв обид. Пробај пак!'}
          </p>
        </div>

        {/* Stars earned */}
        <div className="w-full bg-white rounded-3xl p-5 space-y-3" style={{ boxShadow: '0 4px 16px rgba(0,0,0,0.07)' }}>
          <p className="text-xs font-black tracking-widest uppercase" style={{ color: '#9B9BAA' }}>Овој обид</p>
          {([
            { color: STAR_COLORS.yellow, label: 'Жолта ѕвезда — Лесно',  earned: earnedStars.yellow, isNew: newlyEarned.yellow },
            { color: STAR_COLORS.green,  label: 'Зелена ѕвезда — Средно', earned: earnedStars.green,  isNew: newlyEarned.green  },
            { color: STAR_COLORS.blue,   label: 'Сина ѕвезда — Тешко',    earned: earnedStars.blue,   isNew: newlyEarned.blue   },
          ]).map(item => (
            <div key={item.label} className="flex items-center gap-3 p-3 rounded-2xl"
              style={{ background: item.earned ? '#EDFFF2' : '#F7F7FA', border: `1.5px solid ${item.earned ? '#4CAF50' : '#E8EAF0'}`, opacity: item.earned ? 1 : 0.6 }}>
              <Star color={item.color} size="1.6rem" />
              <span className="font-bold text-sm flex-1 text-left" style={{ color: '#1A1A2E' }}>{item.label}</span>
              {item.earned
                ? <span className="text-xs font-black px-2 py-0.5 rounded-full"
                    style={{ background: item.isNew ? '#4CAF50' : '#D1FAE5', color: item.isNew ? 'white' : '#065F46' }}>
                    {item.isNew ? 'НОВО! ✓' : 'Освоена ✓'}
                  </span>
                : <span className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>Не освоена</span>
              }
            </div>
          ))}
        </div>

        {/* Newly earned badges */}
        {!saving && newBadgeIds.length > 0 && (
          <div className="w-full bg-white rounded-3xl p-5 space-y-3 animate-fade-up" style={{ boxShadow: '0 4px 16px rgba(0,0,0,0.07)' }}>
            <p className="text-xs font-black tracking-widest uppercase" style={{ color: '#9B9BAA' }}>Нови значки 🎖️</p>
            {newBadgeIds.map(id => {
              const def = getBadgeDef(id)
              if (!def) return null
              const tier = TIER_COLORS[def.tier]
              return (
                <div key={id} className="flex items-center gap-3 p-3 rounded-2xl"
                  style={{ background: tier.bg, border: `2px solid ${tier.border}` }}>
                  <span className="text-2xl">{def.emoji}</span>
                  <div className="flex-1 text-left">
                    <p className="font-black text-sm" style={{ color: tier.label }}>{def.nameMk}</p>
                    <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>{def.descMk}</p>
                  </div>
                  <span className="text-xs font-black px-2 py-0.5 rounded-full text-white"
                    style={{ background: tier.label }}>НОВО!</span>
                </div>
              )
            })}
          </div>
        )}

        {/* Total saved stars */}
        <div className="w-full bg-white rounded-3xl p-4" style={{ boxShadow: '0 4px 16px rgba(0,0,0,0.07)' }}>
          <p className="text-xs font-black tracking-widest uppercase mb-3" style={{ color: '#9B9BAA' }}>Вкупно освоени</p>
          <div className="flex justify-center gap-4">
            {[
              { color: STAR_COLORS.yellow, saved: savedStars.yellow },
              { color: STAR_COLORS.green,  saved: savedStars.green  },
              { color: STAR_COLORS.blue,   saved: savedStars.blue   },
            ].map(({ color, saved }) => (
              <div key={color} className="flex flex-col items-center gap-1">
                <span style={{ opacity: saved ? 1 : 0.25 }}><Star color={color} size="2.4rem" /></span>
                <span className="text-xs font-bold" style={{ color: saved ? '#4CAF50' : '#D1D5DB' }}>
                  {saved ? '✓' : '○'}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="flex flex-col gap-3 w-full">
          <button onClick={handleStart}
            className="w-full py-4 rounded-2xl font-black text-base transition-all active:scale-[0.98]"
            style={{ background: 'white', color: subject.color, border: `2px solid ${subject.color}` }}>
            Обиди се пак
          </button>
          <button onClick={() => router.push(`/subject/${subjectId}`)}
            className="w-full py-4 rounded-2xl font-black text-base text-white transition-all active:scale-[0.98] shadow-md"
            style={{ background: `linear-gradient(135deg, ${subject.color}, ${subject.color}cc)` }}>
            {'← Назад кон '}{subject.nameMk}
          </button>
        </div>
      </div>

      <style>{`
        @keyframes confetti-fall { 0%{transform:translateY(-20px) rotate(0deg);opacity:1} 100%{transform:translateY(100vh) rotate(720deg);opacity:0} }
        .confetti-piece{position:absolute;top:-20px;animation:confetti-fall linear forwards}
      `}</style>
    </main>
  )
}
