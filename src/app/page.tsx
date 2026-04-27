'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { getFamilySession, loginWithPin, register, parentLogin, StudentProfile } from '@/lib/auth'

const GRADES = [5, 6, 7, 8, 9] as const

// ── STAR BACKGROUND ───────────────────────────────────────────────
function Stars() {
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {[...Array(18)].map((_, i) => (
        <span key={i} className="absolute animate-float select-none"
          style={{ left: `${(i * 41 + 7) % 100}%`, top: `${(i * 29 + 13) % 100}%`,
            fontSize: `${i % 3 === 0 ? 2 : i % 3 === 1 ? 1.2 : 0.8}rem`,
            opacity: 0.2 + (i % 4) * 0.07, animationDelay: `${(i * 0.4) % 3}s`,
            color: '#FFD93D' }}>★</span>
      ))}
    </div>
  )
}

// ── REGISTER FORM ─────────────────────────────────────────────────
function RegisterForm({ onDone }: { onDone: () => void }) {
  const [parentName, setParentName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [studentName, setStudentName] = useState('')
  const [grade, setGrade] = useState<number | null>(null)
  const [pin, setPin] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleRegister = async () => {
    setError('')
    if (!parentName.trim()) return setError('Внеси го твоето ime.')
    if (!email.includes('@')) return setError('Внеси валидна е-пошта.')
    if (password.length < 6) return setError('Лозинката мора да има барем 6 знаци.')
    if (!studentName.trim()) return setError('Внеси го името на детето.')
    if (!grade) return setError('Одбери одделение.')
    if (pin.length !== 4) return setError('PIN мора да има точно 4 цифри.')
    setLoading(true)
    const result = await register({
      email: email.trim().toLowerCase(), password,
      parentName: parentName.trim(), studentName: studentName.trim(),
      grade, pin,
    })
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    onDone()
  }

  return (
    <div className="bg-white rounded-3xl shadow-2xl overflow-hidden w-full max-w-md">
      <div className="p-3 text-center" style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
        <p className="text-white font-black text-sm">🎉 14 дена бесплатно — без кредитна картичка!</p>
      </div>
      <div className="p-6 space-y-4">
        <h2 className="text-xl font-black text-center" style={{ color: '#1A1A2E' }}>Креирај семеен профил</h2>

        <div className="space-y-3">
          <p className="text-xs font-black tracking-widest" style={{ color: '#9B9BAA' }}>РОДИТЕЛ</p>
          {[
            { label: 'ИМЕ', val: parentName, set: setParentName, type: 'text', ph: 'Ана Петровска' },
            { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'ana@example.com' },
            { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: 'Минимум 6 знаци' },
          ].map(({ label, val, set, type, ph }) => (
            <div key={label}>
              <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>{label}</label>
              <input type={type} value={val} onChange={(e) => { set(e.target.value); setError('') }}
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
            <input type="text" value={studentName} onChange={(e) => { setStudentName(e.target.value); setError('') }}
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
                  style={{ background: grade === g ? '#5C35D4' : 'white',
                    color: grade === g ? '#FFD93D' : '#5C35D4',
                    borderColor: grade === g ? '#5C35D4' : '#E5E7EB' }}>
                  {g}
                </button>
              ))}
            </div>
          </div>

          <div>
            <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>
              PIN ЗА ДЕТЕТО (4 цифри)
            </label>
            <input type="password" inputMode="numeric" maxLength={4}
              value={pin} onChange={(e) => { setPin(e.target.value.replace(/\D/g, '')); setError('') }}
              placeholder="1234"
              className="w-full px-4 py-4 rounded-2xl border-2 font-black text-2xl text-center outline-none tracking-widest"
              style={{ borderColor: pin.length === 4 ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
            <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>
              Детето го користи овој PIN секој ден
            </p>
          </div>
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
  )
}

// ── KID SELECTOR ──────────────────────────────────────────────────
function KidSelector({ students, onBack }: { students: StudentProfile[]; onBack: () => void }) {
  const router = useRouter()
  const [selected, setSelected] = useState<StudentProfile | null>(
    students.length === 1 ? students[0] : null
  )
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
      if (!result.ok) {
        setTimeout(() => { setPin(''); setError(result.error!) }, 300)
      } else {
        router.push('/dashboard')
      }
    }
  }

  const handleBackspace = () => setPin((p) => p.slice(0, -1))

  const KEYS = ['1','2','3','4','5','6','7','8','9','⌫','0','✓']

  return (
    <div className="w-full max-w-sm">
      {/* Student cards */}
      {!selected || students.length > 1 ? (
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
      ) : null}

      {/* PIN pad */}
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

          {/* PIN dots */}
          <div className="flex justify-center gap-4 mb-4">
            {[0,1,2,3].map((i) => (
              <div key={i} className="w-4 h-4 rounded-full transition-all duration-150"
                style={{ background: i < pin.length ? '#5C35D4' : '#E5E7EB',
                  transform: i < pin.length ? 'scale(1.2)' : 'scale(1)' }} />
            ))}
          </div>

          {error && <p className="text-center text-sm font-bold mb-3" style={{ color: '#FF6B6B' }}>⚠️ {error}</p>}

          {/* Numpad */}
          <div className="grid grid-cols-3 gap-2">
            {KEYS.map((k) => (
              <button key={k} type="button"
                onClick={() => k === '⌫' ? handleBackspace() : k === '✓' ? null : handlePin(k)}
                className="py-4 rounded-2xl text-xl font-black transition-all active:scale-90"
                style={{
                  background: k === '⌫' ? '#FFE8E8' : k === '✓' ? '#5C35D4' : '#F7F5FF',
                  color: k === '⌫' ? '#FF6B6B' : k === '✓' ? 'white' : '#1A1A2E',
                }}>
                {k}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Parent access */}
      <button type="button" onClick={onBack}
        className="w-full mt-5 text-center text-sm font-bold text-white/40 hover:text-white/70 transition-colors py-2">
        🔑 Родителски пристап
      </button>
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
    <div className="bg-white rounded-3xl shadow-2xl p-7 w-full max-w-sm">
      <h2 className="text-xl font-black text-center mb-5" style={{ color: '#1A1A2E' }}>
        🔑 Родителски пристап
      </h2>
      <div className="space-y-4">
        <div>
          <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>Е-ПОШТА</label>
          <input type="email" value={email} onChange={(e) => { setEmail(e.target.value); setError('') }}
            placeholder="ana@example.com"
            className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
            style={{ borderColor: email ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
        </div>
        <div>
          <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>ЛОЗИНКА</label>
          <input type="password" value={password} onChange={(e) => { setPassword(e.target.value); setError('') }}
            placeholder="Твојата лозинка"
            onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
            className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
            style={{ borderColor: password ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
        </div>
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
        <p className="text-center text-sm font-semibold" style={{ color: '#9B9BAA' }}>
          Немаш профил?{' '}
          <button type="button" onClick={onRegister} className="font-black" style={{ color: '#5C35D4' }}>
            Регистрирај се
          </button>
        </p>
      </div>
    </div>
  )
}

// ── MAIN PAGE ─────────────────────────────────────────────────────
type View = 'loading' | 'kids' | 'parent-login' | 'register'

export default function HomePage() {
  const router = useRouter()
  const [view, setView] = useState<View>('loading')
  const [students, setStudents] = useState<StudentProfile[]>([])

  useEffect(() => {
    const family = getFamilySession()
    if (family && family.students.length > 0) {
      setStudents(family.students)
      setView('kids')
    } else {
      setView('register')
    }
  }, [])

  const handleRegistered = () => {
    const family = getFamilySession()
    if (family) { setStudents(family.students); setView('kids') }
    else router.push('/dashboard')
  }

  const handleParentLoggedIn = () => {
    const family = getFamilySession()
    if (family && family.students.length > 0) {
      setStudents(family.students)
      setView('kids')
    } else {
      router.push('/dashboard')
    }
  }

  if (view === 'loading') return (
    <main className="min-h-screen flex items-center justify-center"
      style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69, #5C35D4)' }}>
      <div className="text-6xl animate-float">⭐</div>
    </main>
  )

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-4 relative overflow-hidden"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>
      <Stars />

      <div className="relative z-10 w-full flex flex-col items-center">
        <div className="text-center mb-6">
          <div className="text-6xl mb-2 animate-float">⭐</div>
          <h1 className="text-4xl font-black text-white">Супер Ѕвезда</h1>
          <p className="text-purple-300 mt-1">Учи, вежбај, сјај!</p>
        </div>

        {view === 'kids' && (
          <KidSelector students={students} onBack={() => setView('parent-login')} />
        )}
        {view === 'register' && (
          <RegisterForm onDone={handleRegistered} />
        )}
        {view === 'parent-login' && (
          <ParentLoginForm
            onDone={handleParentLoggedIn}
            onRegister={() => setView('register')}
          />
        )}
      </div>
    </main>
  )
}
