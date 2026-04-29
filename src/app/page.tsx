'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { getFamilySession, loginWithPin, register, parentLogin, StudentProfile } from '@/lib/auth'
import { saveAffiliateRef } from '@/lib/affiliate'
import TownSchoolPicker from '@/components/TownSchoolPicker'

const GRADES = [5, 6, 7, 8, 9] as const

// ── HELPERS ───────────────────────────────────────────────────────
function capitalizeWords(val: string) {
  return val.replace(/(^|\s)(\S)/g, (_, sp, ch) => sp + ch.toUpperCase())
}
function isCyrillicName(val: string) {
  return /^[Ѐ-ӿ\s\-]+$/.test(val.trim())
}

// ── STAR FIELD ────────────────────────────────────────────────────
function StarField({ count = 40 }: { count?: number }) {
  const stars = Array.from({ length: count }, (_, i) => ({
    x: (i * 73 + 17) % 100,
    y: (i * 47 + 11) % 100,
    size: i % 5 === 0 ? 1.4 : i % 3 === 0 ? 1 : 0.6,
    delay: (i * 0.3) % 4,
    twinkle: i % 4 === 0,
  }))
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {stars.map((s, i) => (
        <span key={i}
          className={`absolute select-none ${s.twinkle ? 'animate-twinkle' : 'opacity-20'}`}
          style={{
            left: `${s.x}%`, top: `${s.y}%`,
            fontSize: `${s.size}rem`, color: '#FFD93D',
            animationDelay: `${s.delay}s`,
          }}>★</span>
      ))}
    </div>
  )
}

// ── LANDING PAGE ──────────────────────────────────────────────────
const GRADE_COLORS = ['#FFD93D', '#FF9A3C', '#FF6B6B', '#6BCB77', '#7B5CE5']

const FLOATERS = [
  { e: '📚', x: 12, y: 28, delay: 0,   size: '2.2rem', op: 0.3 },
  { e: '🔮', x: 78, y: 18, delay: 1.2, size: '2rem',   op: 0.35 },
  { e: '🌿', x: 88, y: 58, delay: 2.5, size: '1.8rem', op: 0.3 },
  { e: '⚗️', x: 6,  y: 65, delay: 1.8, size: '1.8rem', op: 0.3 },
  { e: '🏆', x: 55, y: 80, delay: 0.7, size: '1.5rem', op: 0.25 },
  { e: '📖', x: 38, y: 12, delay: 3.1, size: '1.6rem', op: 0.25 },
  { e: '👧', x: 92, y: 35, delay: 2,   size: '2rem',   op: 0.3 },
  { e: '👦', x: 22, y: 78, delay: 1.5, size: '2rem',   op: 0.3 },
]

function LandingPage({ onRegister, onLogin }: { onRegister: () => void; onLogin: () => void }) {
  return (
    <div>

      {/* ── HERO ── */}
      <section className="relative min-h-screen flex flex-col items-center justify-center px-5 overflow-hidden"
        style={{ background: 'linear-gradient(160deg, #07040F 0%, #130726 25%, #2D1B69 60%, #5C35D4 100%)' }}>

        <StarField count={50} />

        {/* Ghost grade numbers */}
        {GRADES.map((g, i) => (
          <span key={g} className="absolute font-black select-none pointer-events-none animate-drift"
            style={{
              left: `${[7, 78, 55, 12, 82][i]}%`,
              top: `${[14, 8, 58, 68, 42][i]}%`,
              fontSize: '9rem', lineHeight: 1,
              color: GRADE_COLORS[i], opacity: 0.055,
              animationDelay: `${i * 1.1}s`,
            }}>
            {g}
          </span>
        ))}

        {/* Floating emojis */}
        {FLOATERS.map((f) => (
          <span key={f.e} className="absolute select-none pointer-events-none animate-drift"
            style={{ left: `${f.x}%`, top: `${f.y}%`, fontSize: f.size, opacity: f.op, animationDelay: `${f.delay}s` }}>
            {f.e}
          </span>
        ))}

        {/* Center content */}
        <div className="relative z-10 text-center w-full max-w-sm animate-fade-up">

          {/* Mascot */}
          <div className="text-8xl mb-2 animate-float inline-block" style={{ filter: 'drop-shadow(0 0 30px rgba(255,217,61,0.6))' }}>⭐</div>

          <h1 className="text-5xl font-black text-white mb-1" style={{ letterSpacing: '-1.5px', textShadow: '0 2px 20px rgba(92,53,212,0.8)' }}>
            Супер Ѕвезда
          </h1>
          <p className="font-black text-lg mb-6" style={{ color: '#B39DDB' }}>Учи · Вежбај · Сјај!</p>

          {/* Grade badges */}
          <div className="flex justify-center gap-2 mb-4">
            {GRADES.map((g, i) => (
              <div key={g}
                className="w-11 h-11 rounded-2xl flex items-center justify-center font-black text-lg transition-transform hover:scale-110"
                style={{
                  background: `${GRADE_COLORS[i]}18`,
                  border: `2px solid ${GRADE_COLORS[i]}55`,
                  color: GRADE_COLORS[i],
                  boxShadow: `0 0 12px ${GRADE_COLORS[i]}25`,
                }}>
                {g}
              </div>
            ))}
          </div>

          {/* Subjects */}
          <div className="flex justify-center gap-4 mb-7 text-2xl">
            {[['🔮', 'Математика'], ['🌿', 'Биологија'], ['⚗️', 'Хемија']].map(([e, n]) => (
              <div key={n} className="flex flex-col items-center gap-1">
                <span>{e}</span>
                <span className="text-xs font-bold" style={{ color: 'rgba(255,255,255,0.4)' }}>{n}</span>
              </div>
            ))}
          </div>

          {/* Trial pill */}
          <div className="inline-block rounded-2xl px-4 py-2 mb-5"
            style={{ background: 'rgba(255,217,61,0.12)', border: '1.5px solid rgba(255,217,61,0.45)' }}>
            <p className="font-black text-sm" style={{ color: '#FFD93D' }}>🎉 14 дена БЕСПЛАТНО · Без кредитна картичка</p>
          </div>

          {/* CTA */}
          <button onClick={onRegister}
            className="w-full py-5 rounded-2xl text-xl font-black text-gray-900 block mb-4 transition-all active:scale-95 hover:scale-[1.02] animate-shimmer"
            style={{
              background: 'linear-gradient(90deg, #FFD93D, #FF9A3C, #FFD93D)',
              backgroundSize: '200% auto',
              boxShadow: '0 8px 32px rgba(255,155,61,0.45)',
            }}>
            Почни бесплатно →
          </button>

          <button onClick={onLogin}
            className="text-sm font-bold py-2 w-full block transition-colors"
            style={{ color: 'rgba(179,157,219,0.7)' }}
            onMouseEnter={e => (e.currentTarget.style.color = 'white')}
            onMouseLeave={e => (e.currentTarget.style.color = 'rgba(179,157,219,0.7)')}>
            Веќе имаш профил? Влези →
          </button>
        </div>

        <div className="absolute bottom-7 left-1/2 -translate-x-1/2 animate-bounce text-xl" style={{ color: 'rgba(255,255,255,0.25)' }}>↓</div>
      </section>

      {/* ── SUBJECT WORLDS ── */}
      <section className="px-5 py-14" style={{ background: '#0D0B1E' }}>
        <h2 className="text-2xl font-black text-white text-center mb-1">3 светски доживувања</h2>
        <p className="text-center text-sm font-semibold mb-8" style={{ color: 'rgba(179,157,219,0.6)' }}>
          Секој предмет е своја авантура
        </p>
        <div className="max-w-lg mx-auto space-y-4">
          {[
            { emoji: '🔮', name: 'Математика', world: 'Кристални пештери', color: '#7B5CE5', glow: 'rgba(123,92,229,0.25)' },
            { emoji: '🌿', name: 'Биологија',  world: 'Џунгла свет',       color: '#6BCB77', glow: 'rgba(107,203,119,0.25)' },
            { emoji: '⚗️', name: 'Хемија',     world: 'Вулкан лаб',       color: '#FF6B6B', glow: 'rgba(255,107,107,0.25)' },
          ].map((s) => (
            <div key={s.name} className="rounded-3xl p-5 flex items-center gap-4 transition-transform hover:scale-[1.01]"
              style={{
                background: `linear-gradient(135deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02))`,
                border: `1.5px solid ${s.color}40`,
                boxShadow: `0 4px 24px ${s.glow}`,
              }}>
              <div className="text-5xl flex-shrink-0">{s.emoji}</div>
              <div className="flex-1">
                <div className="font-black text-xl" style={{ color: s.color }}>{s.name}</div>
                <div className="text-sm font-semibold mb-2" style={{ color: 'rgba(255,255,255,0.35)' }}>{s.world}</div>
                <div className="flex gap-1 items-center">
                  {['⭐','⭐','⭐'].map((st, i) => <span key={i} style={{ color: '#FFD93D', fontSize: '0.85rem' }}>{st}</span>)}
                  <span className="text-xs font-semibold ml-1" style={{ color: 'rgba(255,255,255,0.3)' }}>до 36 ѕвезди</span>
                </div>
              </div>
              <div className="text-2xl" style={{ color: s.color }}>→</div>
            </div>
          ))}
        </div>
      </section>

      {/* ── APP PREVIEW (mock UI) ── */}
      <section className="px-5 py-14" style={{ background: '#F7F5FF' }}>
        <h2 className="text-2xl font-black text-center mb-1" style={{ color: '#1A1A2E' }}>Вака изгледа секоја лекција</h2>
        <p className="text-center text-sm font-semibold mb-8" style={{ color: '#9B9BAA' }}>
          Прочитај → Вежбај → Заработи ѕвезди
        </p>

        <div className="max-w-sm mx-auto">
          {/* Phone frame */}
          <div className="rounded-[2.5rem] overflow-hidden shadow-2xl"
            style={{ border: '3px solid #1A1A2E', background: '#1A1A2E' }}>
            {/* Status bar */}
            <div className="h-8 flex items-center justify-center" style={{ background: '#1A1A2E' }}>
              <div className="w-20 h-4 rounded-full" style={{ background: '#2D2D2D' }} />
            </div>
            {/* Screen */}
            <div style={{ background: '#F7F5FF', padding: '0' }}>
              {/* Subject header */}
              <div className="px-5 py-4 flex items-center gap-3" style={{ background: '#5C35D4' }}>
                <span className="text-2xl">🔮</span>
                <span className="text-white font-black">Цели броеви — вовед</span>
              </div>

              {/* Theory snippet */}
              <div className="mx-4 mt-4 bg-white rounded-2xl p-4 shadow-sm">
                <p className="text-xs font-black mb-2" style={{ color: '#5C35D4' }}>ЛЕКЦИЈА</p>
                <p className="text-sm font-semibold leading-relaxed" style={{ color: '#1A1A2E' }}>
                  Целите броеви ги вклучуваат{' '}
                  <span className="font-black" style={{ color: '#5C35D4' }}>позитивните</span>,{' '}
                  <span className="font-black" style={{ color: '#FF6B6B' }}>негативните</span> броеви и нулата.
                </p>
                {/* Number line */}
                <div className="flex items-center justify-center gap-1.5 mt-3">
                  {['−3','−2','−1','0','1','2','3'].map((n) => (
                    <span key={n} className="text-xs font-black px-1.5 py-1 rounded-lg"
                      style={{
                        background: n === '0' ? '#5C35D4' : n.startsWith('−') ? '#FFE8E8' : '#E8F8EA',
                        color: n === '0' ? 'white' : n.startsWith('−') ? '#C0392B' : '#2D7A35',
                      }}>
                      {n}
                    </span>
                  ))}
                </div>
              </div>

              {/* Exercise */}
              <div className="mx-4 mt-3 bg-white rounded-2xl p-4 shadow-sm">
                <div className="text-xs font-black mb-2 flex justify-between">
                  <span style={{ color: '#5C35D4' }}>ПРАШАЊЕ</span>
                  <span style={{ color: '#9B9BAA' }}>2 / 5</span>
                </div>
                <p className="font-black text-sm mb-3" style={{ color: '#1A1A2E' }}>Кој број е најмал?</p>
                <div className="grid grid-cols-2 gap-2">
                  {[['−5','✅',true],['−2','',false],['0','',false],['3','',false]].map(([opt, icon, correct]) => (
                    <div key={String(opt)} className="py-2.5 rounded-xl text-center font-black text-sm border-2"
                      style={{
                        background: correct ? '#E8F8EA' : 'white',
                        borderColor: correct ? '#6BCB77' : '#E5E7EB',
                        color: correct ? '#2D7A35' : '#1A1A2E',
                      }}>
                      {opt} {icon}
                    </div>
                  ))}
                </div>
              </div>

              {/* Star result */}
              <div className="mx-4 mt-3 mb-4 rounded-2xl py-4 text-center"
                style={{ background: 'linear-gradient(135deg, #1A1A2E, #5C35D4)' }}>
                <p className="text-white font-black text-sm mb-2">🏆 Совршено!</p>
                <div className="flex justify-center gap-2">
                  {[0,1,2].map((i) => (
                    <span key={i} className="text-2xl" style={{ filter: 'drop-shadow(0 0 6px #FFD93D)' }}>⭐</span>
                  ))}
                </div>
                <p className="text-purple-200 text-xs mt-1 font-semibold">5/5 точни одговори</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── KIDS ROW ── */}
      <section className="px-5 py-12 bg-white">
        <h2 className="text-2xl font-black text-center mb-2" style={{ color: '#1A1A2E' }}>За деца од 5-то до 9-то одделение</h2>
        <p className="text-center text-sm font-semibold mb-8" style={{ color: '#9B9BAA' }}>Секое одделение, свои лекции и вежби</p>

        {/* Kid cards */}
        <div className="flex justify-center gap-3 mb-10 overflow-x-auto pb-2">
          {[
            { emoji: '👧', name: 'Ана', grade: 5, stars: 47, color: '#FFD93D' },
            { emoji: '👦', name: 'Марко', grade: 7, stars: 83, color: '#FF6B6B' },
            { emoji: '🧒', name: 'Ема', grade: 9, stars: 112, color: '#6BCB77' },
          ].map((k) => (
            <div key={k.name} className="flex-shrink-0 rounded-3xl p-5 text-center w-28"
              style={{
                background: `${k.color}12`,
                border: `2px solid ${k.color}40`,
              }}>
              <div className="text-4xl mb-2">{k.emoji}</div>
              <p className="font-black text-base" style={{ color: '#1A1A2E' }}>{k.name}</p>
              <p className="text-xs font-bold mb-2" style={{ color: '#9B9BAA' }}>{k.grade}-то одд.</p>
              <div className="rounded-xl py-1 font-black text-sm" style={{ background: k.color, color: '#1A1A2E' }}>
                ⭐ {k.stars}
              </div>
            </div>
          ))}
        </div>

        {/* Why bullets */}
        <div className="max-w-lg mx-auto space-y-5">
          {[
            { icon: '📋', title: 'МОН учебна програма', desc: 'Секоја лекција е усогласена со македонскиот учебник — точно она што се учи во школо, 5-то до 9-то одд.' },
            { icon: '⭐', title: 'Учење преку игри', desc: 'Ѕвезди, серии, прогрес — детето ќе бара само да учи. Без принуда, само мотивација.' },
            { icon: '👪', title: 'До 3 деца, еден профил', desc: 'Секое дете свој PIN и напредок. Родителот ги следи сите од едно место.' },
            { icon: '💰', title: 'Поевтино од еден час кај учител', desc: '1 час кај учител ≈ €15. Супер Ѕвезда = €10/месец, 24/7, сите предмети, на телефон.' },
          ].map((w) => (
            <div key={w.title} className="flex gap-4 items-start">
              <div className="w-12 h-12 rounded-2xl flex items-center justify-center text-2xl flex-shrink-0"
                style={{ background: '#F7F5FF' }}>
                {w.icon}
              </div>
              <div>
                <p className="font-black" style={{ color: '#1A1A2E' }}>{w.title}</p>
                <p className="text-sm font-semibold mt-0.5 leading-relaxed" style={{ color: '#6B6B8A' }}>{w.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ── PRICING ── */}
      <section className="px-5 py-14 relative overflow-hidden"
        style={{ background: 'linear-gradient(160deg, #0D0B1E 0%, #2D1B69 60%, #5C35D4 100%)' }}>
        <StarField count={25} />
        <div className="relative z-10 max-w-sm mx-auto text-center">
          <h2 className="text-2xl font-black text-white mb-1">Едноставни цени</h2>
          <p className="text-sm font-semibold mb-8" style={{ color: 'rgba(179,157,219,0.7)' }}>Без скриени трошоци. Откажи кога сакаш.</p>

          {/* Price card */}
          <div className="rounded-3xl p-6 mb-5"
            style={{ background: 'rgba(255,255,255,0.08)', border: '1.5px solid rgba(255,255,255,0.15)', backdropFilter: 'blur(10px)' }}>
            <div className="flex justify-center items-end gap-2 mb-1">
              <span className="text-7xl font-black text-white" style={{ letterSpacing: '-3px' }}>€10</span>
              <span className="font-bold pb-2" style={{ color: 'rgba(179,157,219,0.7)' }}>/месец</span>
            </div>
            <p className="text-sm font-semibold mb-5" style={{ color: 'rgba(179,157,219,0.6)' }}>за 1 дете · сите предмети</p>

            <div className="space-y-2.5 text-left">
              {[
                { text: '1-во дете: €10 / 600 ден', sub: '' },
                { text: '2-ро дете: +€5 / +300 ден', sub: '' },
                { text: '3-то дете: БЕСПЛАТНО 🎁', sub: '' },
                { text: 'Годишно: плати 10, добиј 12 месеци', sub: '' },
              ].map((f) => (
                <div key={f.text} className="flex items-start gap-2.5">
                  <span className="mt-0.5 flex-shrink-0" style={{ color: '#6BCB77' }}>✓</span>
                  <span className="text-sm font-semibold text-white/80">{f.text}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Early adopter */}
          <div className="rounded-2xl p-4 mb-6"
            style={{ background: 'rgba(255,217,61,0.12)', border: '1.5px solid rgba(255,217,61,0.4)' }}>
            <p className="font-black text-sm" style={{ color: '#FFD93D' }}>🚀 Рана претплата — само 500 места!</p>
            <p className="text-xs font-semibold mt-0.5" style={{ color: '#FFE08A' }}>1 дете €5/мес · 2–3 деца €9/мес — заклучена цена засекогаш</p>
          </div>

          <button onClick={onRegister}
            className="w-full py-5 rounded-2xl text-xl font-black text-gray-900 block transition-all active:scale-95 hover:scale-[1.02] mb-3 animate-shimmer"
            style={{
              background: 'linear-gradient(90deg, #FFD93D, #FF9A3C, #FFD93D)',
              backgroundSize: '200% auto',
              boxShadow: '0 8px 32px rgba(255,155,61,0.4)',
            }}>
            Пробај 14 дена бесплатно →
          </button>
          <p className="text-xs font-semibold" style={{ color: 'rgba(179,157,219,0.5)' }}>Без кредитна картичка · Откажи кога сакаш</p>
        </div>
      </section>

    </div>
  )
}

// ── REGISTER FORM ─────────────────────────────────────────────────
function RegisterForm({ onDone, onBack }: { onDone: () => void; onBack: () => void }) {
  const [parentName, setParentName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [studentName, setStudentName] = useState('')
  const [grade, setGrade] = useState<number | null>(null)
  const [pin, setPin] = useState('')
  const [town, setTown] = useState('')
  const [school, setSchool] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleRegister = async () => {
    setError('')
    if (!parentName.trim()) return setError('Внеси го твоето ime.')
    if (!isCyrillicName(parentName)) return setError('Името мора да биде на кирилица (пр. Ана Петровска).')
    if (!email.includes('@')) return setError('Внеси валидна е-пошта.')
    if (password.length < 6) return setError('Лозинката мора да има барем 6 знаци.')
    if (!studentName.trim()) return setError('Внеси го името на детето.')
    if (!isCyrillicName(studentName)) return setError('Името на детето мора да биде на кирилица.')
    if (!grade) return setError('Одбери одделение.')
    if (pin.length !== 4) return setError('PIN мора да има точно 4 цифри.')
    setLoading(true)
    const result = await register({ email: email.trim().toLowerCase(), password, parentName: parentName.trim(), studentName: studentName.trim(), grade, pin, town: town || undefined, school: school || undefined })
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    onDone()
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10 relative overflow-hidden"
      style={{ background: 'linear-gradient(160deg, #07040F 0%, #130726 30%, #2D1B69 70%, #5C35D4 100%)' }}>
      <StarField count={30} />
      <div className="relative z-10 w-full max-w-md">
        <button onClick={onBack} className="flex items-center gap-2 mb-6 font-bold text-sm transition-colors"
          style={{ color: 'rgba(179,157,219,0.7)' }}>
          ← Назад
        </button>

        <div className="text-center mb-6">
          <div className="text-5xl mb-2 animate-float">⭐</div>
          <h1 className="text-3xl font-black text-white">Супер Ѕвезда</h1>
        </div>

        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden">
          <div className="p-3 text-center font-black text-sm text-white"
            style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
            🎉 14 дена бесплатно — без кредитна картичка!
          </div>
          <div className="p-6 space-y-4">
            <h2 className="text-xl font-black text-center" style={{ color: '#1A1A2E' }}>Креирај семеен профил</h2>

            <div className="space-y-3">
              <p className="text-xs font-black tracking-widest" style={{ color: '#9B9BAA' }}>РОДИТЕЛ</p>
              {[
                { label: 'ИМЕ', val: parentName, set: setParentName, type: 'text', ph: 'Ана Петровска', transform: capitalizeWords },
                { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'ana@example.com' },
                { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: 'Минимум 6 знаци' },
              ].map(({ label, val, set, type, ph, transform }: { label: string; val: string; set: (v: string) => void; type: string; ph: string; transform?: (v: string) => string }) => (
                <div key={label}>
                  <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>{label}</label>
                  <input type={type} value={val} onChange={(e) => { set(transform ? transform(e.target.value) : e.target.value); setError('') }}
                    placeholder={ph}
                    className="w-full px-4 py-3 rounded-2xl border-2 font-semibold text-base outline-none"
                    style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
                </div>
              ))}
            </div>

            <div className="border-t pt-3 space-y-3">
              <p className="text-xs font-black tracking-widest" style={{ color: '#9B9BAA' }}>ДЕТЕ</p>
              <div>
                <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>ИМЕ НА ДЕТЕТО</label>
                <input type="text" value={studentName}
                  onChange={(e) => { setStudentName(capitalizeWords(e.target.value)); setError('') }}
                  placeholder="Марија"
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold text-base outline-none"
                  style={{ borderColor: studentName ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
              <div>
                <label className="block text-xs font-black mb-2" style={{ color: '#6B6B8A' }}>ОДДЕЛЕНИЕ</label>
                <div className="grid grid-cols-5 gap-2">
                  {GRADES.map((g) => (
                    <button key={g} type="button" onClick={() => { setGrade(g); setError('') }}
                      className="py-3 rounded-2xl text-lg font-black border-2 transition-all duration-150"
                      style={{ background: grade === g ? '#5C35D4' : 'white', color: grade === g ? '#FFD93D' : '#5C35D4', borderColor: grade === g ? '#5C35D4' : '#E5E7EB' }}>
                      {g}
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>PIN ЗА ДЕТЕТО (4 цифри)</label>
                <input type="password" inputMode="numeric" maxLength={4}
                  value={pin} onChange={(e) => { setPin(e.target.value.replace(/\D/g, '')); setError('') }}
                  placeholder="1234"
                  className="w-full px-4 py-4 rounded-2xl border-2 font-black text-2xl text-center outline-none tracking-widest"
                  style={{ borderColor: pin.length === 4 ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
                <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>Детето го користи овој PIN секој ден</p>
              </div>

              <TownSchoolPicker
                town={town} school={school}
                onTownChange={setTown} onSchoolChange={setSchool}
              />
            </div>

            {error && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {error}</p>
              </div>
            )}

            <button type="button" onClick={handleRegister} disabled={loading}
              className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-95 disabled:opacity-60"
              style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              {loading ? 'Се регистрира...' : 'Почни со учење! ⭐'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

// ── KID SELECTOR ──────────────────────────────────────────────────
function KidSelector({ students, onBack }: { students: StudentProfile[]; onBack: () => void }) {
  const router = useRouter()
  const [selected, setSelected] = useState<StudentProfile | null>(students.length === 1 ? students[0] : null)
  const [pin, setPin] = useState('')
  const [error, setError] = useState('')

  const handlePin = (digit: string) => {
    if (pin.length >= 4) return
    const next = pin + digit
    setPin(next)
    setError('')
    if (next.length === 4) {
      if (!selected) return
      const result = loginWithPin(selected, next)
      if (!result.ok) { setTimeout(() => { setPin(''); setError(result.error!) }, 300) }
      else { router.push('/dashboard') }
    }
  }
  const KEYS = ['1','2','3','4','5','6','7','8','9','⌫','0','✓']

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-5 relative overflow-hidden"
      style={{ background: 'linear-gradient(160deg, #07040F 0%, #130726 25%, #2D1B69 60%, #5C35D4 100%)' }}>
      <StarField count={35} />
      <div className="relative z-10 w-full max-w-sm">
        <div className="text-center mb-8">
          <div className="text-6xl animate-float inline-block mb-2" style={{ filter: 'drop-shadow(0 0 20px rgba(255,217,61,0.5))' }}>⭐</div>
          <h1 className="text-3xl font-black text-white">Супер Ѕвезда</h1>
        </div>

        {(!selected || students.length > 1) && (
          <div>
            <h2 className="text-2xl font-black text-white text-center mb-5">Кој учи денес? 👋</h2>
            <div className="grid gap-3 mb-4">
              {students.map((s) => (
                <button key={s.id} type="button"
                  onClick={() => { setSelected(s); setPin(''); setError('') }}
                  className="bg-white rounded-3xl p-5 flex items-center gap-4 transition-all active:scale-95"
                  style={{ border: selected?.id === s.id ? '2px solid #5C35D4' : '2px solid transparent' }}>
                  <div className="w-14 h-14 rounded-2xl flex items-center justify-center text-3xl font-black text-white"
                    style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                    {s.name[0].toUpperCase()}
                  </div>
                  <div className="text-left">
                    <div className="text-lg font-black" style={{ color: '#1A1A2E' }}>{s.name}</div>
                    <div className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>
                      {s.grade}-то одделение · ⭐ {s.stars_total}
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {selected && (
          <div className="bg-white rounded-3xl p-6">
            {students.length > 1 && (
              <button type="button" onClick={() => { setSelected(null); setPin('') }}
                className="text-sm font-bold mb-3 block" style={{ color: '#9B9BAA' }}>← Назад</button>
            )}
            <div className="text-center mb-4">
              <div className="w-14 h-14 rounded-2xl flex items-center justify-center text-2xl font-black text-white mx-auto mb-2"
                style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                {selected.name[0].toUpperCase()}
              </div>
              <p className="font-black text-lg" style={{ color: '#1A1A2E' }}>Здраво, {selected.name}!</p>
              <p className="text-sm" style={{ color: '#9B9BAA' }}>Внеси го твојот PIN</p>
            </div>
            <div className="flex justify-center gap-4 mb-4">
              {[0,1,2,3].map((i) => (
                <div key={i} className="w-4 h-4 rounded-full transition-all duration-150"
                  style={{ background: i < pin.length ? '#5C35D4' : '#E5E7EB', transform: i < pin.length ? 'scale(1.2)' : 'scale(1)' }} />
              ))}
            </div>
            {error && <p className="text-center text-sm font-bold mb-3" style={{ color: '#FF6B6B' }}>⚠️ {error}</p>}
            <div className="grid grid-cols-3 gap-2">
              {KEYS.map((k) => (
                <button key={k} type="button"
                  onClick={() => k === '⌫' ? setPin(p => p.slice(0,-1)) : k !== '✓' ? handlePin(k) : undefined}
                  className="py-4 rounded-2xl text-xl font-black transition-all active:scale-90"
                  style={{ background: k === '⌫' ? '#FFE8E8' : k === '✓' ? '#5C35D4' : '#F7F5FF', color: k === '⌫' ? '#FF6B6B' : k === '✓' ? 'white' : '#1A1A2E' }}>
                  {k}
                </button>
              ))}
            </div>
          </div>
        )}

        <button type="button" onClick={onBack}
          className="w-full mt-5 text-center text-sm font-bold py-2 transition-colors"
          style={{ color: 'rgba(179,157,219,0.5)' }}>
          🔑 Родителски пристап
        </button>
      </div>
    </div>
  )
}

// ── PARENT LOGIN FORM ─────────────────────────────────────────────
function ParentLoginForm({ onDone, onRegister }: { onDone: () => void; onRegister: () => void }) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleLogin = async () => {
    setError('')
    if (!email.trim() || !password.trim()) return setError('Внеси е-пошта и лозинка.')
    setLoading(true)
    const result = await parentLogin(email.trim().toLowerCase(), password)
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    onDone()
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-5 relative overflow-hidden"
      style={{ background: 'linear-gradient(160deg, #07040F 0%, #130726 30%, #2D1B69 70%, #5C35D4 100%)' }}>
      <StarField count={30} />
      <div className="relative z-10 w-full max-w-sm">
        <div className="text-center mb-8">
          <div className="text-5xl mb-2 animate-float">⭐</div>
          <h1 className="text-3xl font-black text-white">Супер Ѕвезда</h1>
        </div>
        <div className="bg-white rounded-3xl shadow-2xl p-7">
          <h2 className="text-xl font-black text-center mb-5" style={{ color: '#1A1A2E' }}>🔑 Родителски пристап</h2>
          <div className="space-y-4">
            {[
              { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'ana@example.com' },
              { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: 'Твојата лозинка' },
            ].map(({ label, val, set, type, ph }) => (
              <div key={label}>
                <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                <input type={type} value={val} onChange={(e) => { set(e.target.value); setError('') }}
                  placeholder={ph} onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                  style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
            ))}
            {error && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {error}</p>
              </div>
            )}
            <button type="button" onClick={handleLogin} disabled={loading}
              className="w-full py-4 rounded-2xl text-lg font-black text-white transition-all active:scale-95 disabled:opacity-60"
              style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              {loading ? 'Се логира...' : 'Влези'}
            </button>
            <div className="flex items-center justify-between text-sm">
              <button type="button" onClick={onRegister} className="font-semibold" style={{ color: '#9B9BAA' }}>
                Нема профил? <span className="font-black" style={{ color: '#5C35D4' }}>Регистрирај се</span>
              </button>
              <a href="/reset-password" className="font-semibold" style={{ color: '#9B9BAA' }}>
                Заборавена лозинка?
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

// ── MAIN PAGE ─────────────────────────────────────────────────────
type View = 'loading' | 'landing' | 'kids' | 'parent-login' | 'register'

export default function HomePage() {
  const router = useRouter()
  const [view, setView] = useState<View>('loading')
  const [students, setStudents] = useState<StudentProfile[]>([])

  useEffect(() => {
    const ref = new URLSearchParams(window.location.search).get('ref')
    if (ref) saveAffiliateRef(ref)

    const family = getFamilySession()
    if (family && family.students.length > 0) {
      setStudents(family.students)
      setView('kids')
    } else {
      setView('landing')
    }
  }, [])

  const handleRegistered = () => {
    const family = getFamilySession()
    if (family) { setStudents(family.students); setView('kids') }
    else router.push('/dashboard')
  }

  const handleParentLoggedIn = () => { router.push('/parent') }

  if (view === 'loading') return (
    <div className="min-h-screen flex items-center justify-center"
      style={{ background: 'linear-gradient(160deg, #07040F, #2D1B69, #5C35D4)' }}>
      <div className="text-7xl animate-float" style={{ filter: 'drop-shadow(0 0 30px rgba(255,217,61,0.6))' }}>⭐</div>
    </div>
  )

  if (view === 'landing') return <LandingPage onRegister={() => setView('register')} onLogin={() => setView('parent-login')} />
  if (view === 'register') return <RegisterForm onDone={handleRegistered} onBack={() => setView('landing')} />
  if (view === 'kids') return <KidSelector students={students} onBack={() => setView('parent-login')} />
  if (view === 'parent-login') return <ParentLoginForm onDone={handleParentLoggedIn} onRegister={() => setView('register')} />
  return null
}
