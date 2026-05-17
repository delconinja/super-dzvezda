'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { getFamilySession } from '@/lib/auth'
import { supabase } from '@/lib/supabase'
import { saveAffiliateRef } from '@/lib/affiliate'
import StarMascot from '@/components/StarMascot'

const GRADES = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const
const GRADE_COLORS = ['#E8D5FF', '#FFE0C8', '#FFD0D0', '#C8F0D8', '#D8CCFF', '#FFD0E8', '#C8F0EC', '#C8E8FF', '#D0EED8']

// ── FREE TRIAL EXERCISES ────────────────────────────────────────────
type SubjectKey = 'math' | 'bio' | 'chem'

const TRIAL_EXERCISES: Record<SubjectKey, { id: string; question: string; subjectLabel: string; options: string[]; correct: number }[]> = {
  math: [
    { id: 'math-1', question: '5 + 3 = ?', subjectLabel: 'Математика · 1-во одд.', options: ['6', '7', '8', '9'], correct: 2 },
    { id: 'math-2', question: 'Топката е ПОД масата. Каде е топката?', subjectLabel: 'Математика · 1-во одд.', options: ['Под масата', 'Над масата', 'До масата', 'Пред масата'], correct: 0 },
  ],
  bio: [
    { id: 'bio-1', question: 'Кои се основните делови на растението?', subjectLabel: 'Биологија · 1-во одд.', options: ['Корен, стебло, лист', 'Глава, тело, нозе', 'Јадро, мембрана, цитоплазма', 'Цвет, плод, семе'], correct: 0 },
    { id: 'bio-2', question: 'Дрвото е жив организам. Точно или неточно?', subjectLabel: 'Биологија · 1-во одд.', options: ['Точно', 'Неточно'], correct: 0 },
  ],
  chem: [
    { id: 'chem-1', question: 'Водата е составена од...?', subjectLabel: 'Хемија · 7-мо одд.', options: ['Водород и кислород', 'Јаглерод и азот', 'Натриум и хлор', 'Калциум и фосфор'], correct: 0 },
    { id: 'chem-2', question: 'Каков е хемискиот симбол за злато?', subjectLabel: 'Хемија · 7-мо одд.', options: ['Go', 'Gl', 'Au', 'Ag'], correct: 2 },
  ],
}

const SUBJECT_META: Record<SubjectKey, { name: string; emoji: string; color: string; bg: string }> = {
  math: { name: 'Математика', emoji: '🔮', color: '#5C35D4', bg: '#F0EBFF' },
  bio:  { name: 'Биологија',  emoji: '🌿', color: '#2D7A35', bg: '#E8FAF2' },
  chem: { name: 'Хемија',     emoji: '⚗️', color: '#C0392B', bg: '#FFF0F0' },
}

function TrialSection({ onRegister, activeSubject }: { onRegister: () => void; activeSubject: SubjectKey }) {
  const exercises = TRIAL_EXERCISES[activeSubject]
  const meta = SUBJECT_META[activeSubject]
  const [answers, setAnswers] = useState<Record<string, number | null>>({})
  const [submitted, setSubmitted] = useState<Record<string, boolean>>({})
  const [allDone, setAllDone] = useState(false)

  useEffect(() => {
    setAnswers({})
    setSubmitted({})
    setAllDone(false)
  }, [activeSubject])

  const handleAnswer = (exId: string, idx: number, correct: number) => {
    if (submitted[exId]) return
    const newAnswers = { ...answers, [exId]: idx }
    const newSubmitted = { ...submitted, [exId]: true }
    setAnswers(newAnswers)
    setSubmitted(newSubmitted)
    if (exercises.every(e => newSubmitted[e.id])) setAllDone(true)
  }

  const correctCount = exercises.filter(e => submitted[e.id] && answers[e.id] === e.correct).length

  return (
    <section className="px-5 py-14" style={{ background: '#FAFAFE' }}>
      <div className="max-w-lg mx-auto">
        <div className="text-center mb-8">
          <div className="inline-block px-3 py-1 rounded-full text-xs font-black mb-3"
            style={{ background: '#FFF8C4', border: '1.5px solid #FFD93D', color: '#7A5800' }}>
            🎮 ПРОБАЈ БЕСПЛАТНО — без регистрација
          </div>
          <h2 className="text-2xl font-black mb-2" style={{ color: '#1A1A2E' }}>2 вежби, веднаш сега</h2>
          <p className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>
            Реши ги и види колку е забавно учењето со Супер Ѕвезда
          </p>
        </div>

        {/* Subject badge */}
        <div className="flex items-center gap-2 mb-4 px-1">
          <span className="text-xl">{meta.emoji}</span>
          <span className="font-black text-sm" style={{ color: meta.color }}>{meta.name}</span>
          <span className="text-xs font-semibold px-2 py-0.5 rounded-full" style={{ background: meta.bg, color: meta.color }}>
            2 вежби · бесплатно
          </span>
        </div>

        <div className="space-y-4">
          {exercises.map((ex, qi) => {
            const isSubmitted = !!submitted[ex.id]
            const chosen = answers[ex.id] ?? null
            const isCorrect = chosen === ex.correct

            return (
              <div key={ex.id} className="bg-white rounded-3xl p-5 transition-all"
                style={{ border: isSubmitted ? `2px solid ${isCorrect ? '#6BCB77' : '#FF6B6B'}` : `2px solid ${meta.color}20`, boxShadow: '0 2px 12px rgba(92,53,212,0.07)' }}>
                <div className="flex items-start gap-3 mb-4">
                  <div className="w-8 h-8 rounded-xl flex items-center justify-center font-black text-sm flex-shrink-0"
                    style={{ background: meta.bg, color: meta.color }}>
                    {qi + 1}
                  </div>
                  <div>
                    <p className="text-xs font-black tracking-widest mb-1" style={{ color: '#9B9BAA' }}>{ex.subjectLabel}</p>
                    <p className="font-black text-base" style={{ color: '#1A1A2E' }}>{ex.question}</p>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-2">
                  {ex.options.map((opt, idx) => {
                    let bg = '#F7F5FF'; let color = '#1A1A2E'; let border = 'transparent'
                    if (isSubmitted) {
                      if (idx === ex.correct) { bg = '#E8F8EA'; color = '#2D7A35'; border = '#6BCB77' }
                      else if (idx === chosen) { bg = '#FFE8E8'; color = '#C0392B'; border = '#FF6B6B' }
                    } else if (chosen === idx) {
                      bg = meta.bg; color = meta.color; border = meta.color
                    }
                    return (
                      <button key={idx} type="button"
                        onClick={() => handleAnswer(ex.id, idx, ex.correct)}
                        disabled={isSubmitted}
                        className="py-3 px-4 rounded-2xl text-sm font-black transition-all active:scale-95 disabled:cursor-default text-left"
                        style={{ background: bg, color, border: `2px solid ${border}` }}>
                        {opt}
                        {isSubmitted && idx === ex.correct && ' ✓'}
                        {isSubmitted && idx === chosen && idx !== ex.correct && ' ✗'}
                      </button>
                    )
                  })}
                </div>

                {isSubmitted && (
                  <p className="mt-3 text-sm font-bold" style={{ color: isCorrect ? '#2D7A35' : '#C0392B' }}>
                    {isCorrect ? '⭐ Точно! Одлично!' : `Точниот одговор е: ${ex.options[ex.correct]}`}
                  </p>
                )}
              </div>
            )
          })}
        </div>

        {allDone && (
          <div className="mt-6 rounded-3xl p-6 text-center"
            style={{ background: `linear-gradient(135deg, ${meta.bg}, #D4F5EC)`, border: `2px solid ${meta.color}30` }}>
            <div className="text-4xl mb-2">{correctCount === exercises.length ? '🏆' : '⭐'}</div>
            <p className="font-black text-xl mb-1" style={{ color: '#1A1A2E' }}>
              {correctCount}/{exercises.length} точни!
            </p>
            <p className="text-sm font-semibold mb-4" style={{ color: '#6B6B8A' }}>
              {correctCount === exercises.length
                ? 'Совршено! Регистрирај се за уште стотици вежби.'
                : 'Продолжи да вежбаш — секој ден малку подобро!'}
            </p>
            <button onClick={onRegister}
              className="w-full py-4 rounded-2xl text-base font-black text-white transition-all active:scale-95"
              style={{ background: '#5C35D4', boxShadow: '0 6px 20px rgba(92,53,212,0.3)' }}>
              Пробај 14 дена бесплатно →
            </button>
          </div>
        )}
      </div>
    </section>
  )
}

export default function HomePage() {
  const router = useRouter()
  const [loading, setLoading] = useState(true)
  const [activeSubject, setActiveSubject] = useState<SubjectKey>('math')

  useEffect(() => {
    const ref = new URLSearchParams(window.location.search).get('ref')
    if (ref) saveAffiliateRef(ref)
    const init = async () => {
      const family = getFamilySession()
      if (family && family.students.length > 0) {
        const { data: { user } } = await supabase.auth.getUser()
        // Parent authenticated → parent dashboard
        // Family exists but parent not logged in → kid PIN selector
        router.replace(user ? '/parent' : '/login')
        return
      }
      setLoading(false)
    }
    init()
  }, [router])

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F8F5FF' }}>
      <div className="text-7xl animate-float">⭐</div>
    </div>
  )

  return (
    <div style={{ minHeight: '100vh', background: '#FDFCFF' }}>

      {/* ── NAVBAR ── */}
      <nav className="sticky top-0 z-50 px-6 py-4 flex items-center justify-between"
        style={{ background: 'white', borderBottom: '2px solid #EDE9FF' }}>
        <div className="flex items-center gap-2">
          <span className="text-2xl">⭐</span>
          <span className="font-black text-xl" style={{ color: '#5C35D4' }}>Супер Ѕвезда</span>
        </div>
        <div className="flex items-center gap-3">
          <button onClick={() => router.push('/login')}
            className="px-4 py-2 rounded-2xl font-black text-sm transition-all active:scale-95"
            style={{ color: '#5C35D4', background: '#EDE9FF' }}>
            Влези
          </button>
          <button onClick={() => router.push('/register')}
            className="px-4 py-2 rounded-2xl font-black text-sm text-white transition-all active:scale-95"
            style={{ background: '#5C35D4', boxShadow: '0 4px 12px rgba(92,53,212,0.25)' }}>
            Регистрирај се
          </button>
        </div>
      </nav>

      {/* ── HERO ── */}
      <section className="px-5 pt-14 pb-16 text-center"
        style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>
        <div className="max-w-sm mx-auto animate-fade-up">
          <div className="mb-4 inline-block">
            <StarMascot talking={false} size={100} />
          </div>
          <h1 className="text-4xl font-black mb-3" style={{ color: '#1A1A2E', letterSpacing: '-1px' }}>
            Учи. Вежбај. Сјај!
          </h1>
          <p className="font-semibold text-base mb-8 leading-relaxed" style={{ color: '#6B6B8A' }}>
            Интерактивни лекции по математика, биологија и хемија за деца од 1-во до 9-то одделение.
          </p>

          {/* Grade badges */}
          <div className="flex justify-center gap-1.5 mb-8 flex-wrap">
            {GRADES.map((g, i) => (
              <div key={g}
                className="w-9 h-9 rounded-xl flex items-center justify-center font-black text-sm"
                style={{ background: GRADE_COLORS[i], color: '#1A1A2E' }}>
                {g}
              </div>
            ))}
          </div>

          {/* Free trial badge */}
          <div className="inline-block rounded-2xl px-4 py-2 mb-6"
            style={{ background: '#FFF8C4', border: '1.5px solid #FFD93D' }}>
            <p className="font-black text-sm" style={{ color: '#7A5800' }}>🎉 14 дена БЕСПЛАТНО · Без кредитна картичка</p>
          </div>

          {/* CTAs */}
          <button onClick={() => router.push('/register')}
            className="w-full py-4 rounded-2xl text-lg font-black text-white mb-3 transition-all active:scale-95"
            style={{ background: '#5C35D4', boxShadow: '0 8px 24px rgba(92,53,212,0.3)' }}>
            Почни бесплатно →
          </button>
          <button onClick={() => router.push('/login')}
            className="w-full py-3 rounded-2xl text-sm font-bold transition-all active:scale-95"
            style={{ color: '#7B5CE5', background: 'rgba(92,53,212,0.08)' }}>
            Веќе имаш профил? Влези →
          </button>
        </div>
      </section>

      {/* ── SUBJECTS ── */}
      <section className="px-5 py-14" style={{ background: 'white' }}>
        <h2 className="text-2xl font-black text-center mb-2" style={{ color: '#1A1A2E' }}>3 предмети, безброј авантури</h2>
        <p className="text-center text-sm font-semibold mb-8" style={{ color: '#9B9BAA' }}>Кликни на предмет за да пробаш бесплатна вежба</p>
        <div className="max-w-lg mx-auto space-y-3">
          {([
            { key: 'math' as SubjectKey, emoji: '🔮', name: 'Математика', desc: 'Броеви, геометрија, равенки', bg: '#F0EBFF', color: '#5C35D4' },
            { key: 'bio'  as SubjectKey, emoji: '🌿', name: 'Биологија',  desc: 'Клетки, екосистеми, живи суштества', bg: '#E8FAF2', color: '#2D7A35' },
            { key: 'chem' as SubjectKey, emoji: '⚗️', name: 'Хемија',     desc: 'Елементи, реакции, периоден систем', bg: '#FFF0F0', color: '#C0392B' },
          ]).map((s) => (
            <button key={s.name} type="button"
              onClick={() => {
                setActiveSubject(s.key)
                document.getElementById('trial-section')?.scrollIntoView({ behavior: 'smooth' })
              }}
              className="w-full rounded-3xl p-5 flex items-center gap-4 transition-all hover:scale-[1.01] active:scale-[0.99] text-left"
              style={{ background: activeSubject === s.key ? s.color : s.bg, border: `2px solid ${s.color}40` }}>
              <div className="text-4xl flex-shrink-0">{s.emoji}</div>
              <div className="flex-1">
                <div className="font-black text-lg" style={{ color: activeSubject === s.key ? 'white' : s.color }}>{s.name}</div>
                <div className="text-sm font-semibold" style={{ color: activeSubject === s.key ? 'rgba(255,255,255,0.75)' : '#9B9BAA' }}>{s.desc}</div>
              </div>
              <div className="text-sm font-black px-3 py-1.5 rounded-xl"
                style={{ background: activeSubject === s.key ? 'rgba(255,255,255,0.2)' : s.color + '15', color: activeSubject === s.key ? 'white' : s.color }}>
                Пробај →
              </div>
            </button>
          ))}
        </div>
      </section>

      {/* ── FEATURES ── */}
      <section className="px-5 py-14" style={{ background: '#F0FFF8' }}>
        <h2 className="text-2xl font-black text-center mb-8" style={{ color: '#1A1A2E' }}>Зошто Супер Ѕвезда?</h2>
        <div className="max-w-lg mx-auto space-y-6">
          {[
            { icon: '📋', bg: '#EDE9FF', title: 'МОН учебна програма', desc: 'Секоја лекција е усогласена со македонскиот учебник — точно она што се учи во школо.' },
            { icon: '⭐', bg: '#FFF8C4', title: 'Учење преку игри', desc: 'Ѕвезди, серии и прогрес — детето ќе бара само да учи. Без принуда.' },
            { icon: '👪', bg: '#D4F5EC', title: 'До 3 деца, еден профил', desc: 'Секое дете свој PIN и напредок. Родителот ги следи сите од едно место.' },
            { icon: '💰', bg: '#FFE0C8', title: 'Поевтино од еден час кај учител', desc: 'Само €10/месец наспроти €15 за еден час приватна настава.' },
          ].map((f) => (
            <div key={f.title} className="flex gap-4 items-start">
              <div className="w-12 h-12 rounded-2xl flex items-center justify-center text-2xl flex-shrink-0"
                style={{ background: f.bg }}>
                {f.icon}
              </div>
              <div>
                <p className="font-black" style={{ color: '#1A1A2E' }}>{f.title}</p>
                <p className="text-sm font-semibold mt-0.5 leading-relaxed" style={{ color: '#6B6B8A' }}>{f.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ── TRIAL EXERCISES ── */}
      <div id="trial-section">
        <TrialSection onRegister={() => router.push('/register')} activeSubject={activeSubject} />
      </div>

      {/* ── PRICING ── */}
      <section className="px-5 py-14" style={{ background: '#EDE9FF' }}>
        <div className="max-w-sm mx-auto text-center">
          <h2 className="text-2xl font-black mb-1" style={{ color: '#1A1A2E' }}>Едноставни цени</h2>
          <p className="text-sm font-semibold mb-8" style={{ color: '#7B5CE5' }}>Без скриени трошоци. Откажи кога сакаш.</p>

          <div className="bg-white rounded-3xl p-6 mb-4 shadow-sm">
            <div className="flex justify-center items-end gap-2 mb-1">
              <span className="text-6xl font-black" style={{ color: '#5C35D4', letterSpacing: '-2px' }}>€10</span>
              <span className="font-bold pb-2" style={{ color: '#9B9BAA' }}>/месец</span>
            </div>
            <p className="text-sm font-semibold mb-5" style={{ color: '#9B9BAA' }}>за 1 дете · сите предмети</p>

            <div className="space-y-2.5 text-left mb-6">
              {[
                '1-во дете: €10 / 600 ден',
                '2-ро дете: +€5 / +300 ден',
                '3-то дете: БЕСПЛАТНО 🎁',
                'Годишно: плати 10, добиј 12 месеци',
              ].map((f) => (
                <div key={f} className="flex items-start gap-2.5">
                  <span className="flex-shrink-0 mt-0.5" style={{ color: '#6BCB77' }}>✓</span>
                  <span className="text-sm font-semibold" style={{ color: '#1A1A2E' }}>{f}</span>
                </div>
              ))}
            </div>

            <button onClick={() => router.push('/register')}
              className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-95"
              style={{ background: '#5C35D4', boxShadow: '0 6px 20px rgba(92,53,212,0.3)' }}>
              Пробај 14 дена бесплатно →
            </button>
          </div>

          <div className="rounded-2xl p-4"
            style={{ background: '#FFF8C4', border: '1.5px solid #FFD93D' }}>
            <p className="font-black text-sm" style={{ color: '#7A5800' }}>🚀 Рана претплата — само 500 места!</p>
            <p className="text-xs font-semibold mt-0.5" style={{ color: '#9B7B00' }}>1 дете €5/мес · 2–3 деца €9/мес — заклучена цена засекогаш</p>
          </div>
        </div>
      </section>

      {/* ── FOOTER ── */}
      <footer className="px-6 py-8 text-center" style={{ background: 'white', borderTop: '2px solid #EDE9FF' }}>
        <div className="flex items-center justify-center gap-2 mb-2">
          <span className="text-xl">⭐</span>
          <span className="font-black" style={{ color: '#5C35D4' }}>Супер Ѕвезда</span>
        </div>
        <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>© 2025 Супер Ѕвезда · За деца од 1-во до 9-то одделение</p>
      </footer>

    </div>
  )
}
