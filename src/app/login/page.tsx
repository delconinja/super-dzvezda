'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { parentLogin, isDevAdminUser, getFamilySession, loginWithPin, setActiveStudent, getProgress, StudentProfile } from '@/lib/auth'

type Tab = 'parent' | 'kid'

// ── KID PIN SELECTOR ──────────────────────────────────────────────
function KidSelector({ students }: { students: StudentProfile[] }) {
  const router = useRouter()
  const [selected, setSelected] = useState<StudentProfile | null>(students.length === 1 ? students[0] : null)
  const [pin, setPin] = useState('')
  const [error, setError] = useState('')
  const [liveStars, setLiveStars] = useState<Record<string, number>>({})

  useEffect(() => {
    Promise.all(
      students.map(async (s) => {
        const progress = await getProgress(s.id)
        const total = progress.reduce((sum, p) => sum + p.stars_earned, 0)
        return [s.id, total] as [string, number]
      })
    ).then(entries => setLiveStars(Object.fromEntries(entries)))
  }, [students])

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
    <div>
      {(!selected || students.length > 1) && (
        <div className="mb-4">
          <h2 className="text-lg font-black text-center mb-4" style={{ color: '#1A1A2E' }}>Кој учи денес? 👋</h2>
          <div className="grid gap-3">
            {students.map((s) => (
              <button key={s.id} type="button"
                onClick={() => { setSelected(s); setPin(''); setError('') }}
                className="bg-white rounded-3xl p-4 flex items-center gap-4 transition-all active:scale-95"
                style={{ border: selected?.id === s.id ? '2px solid #5C35D4' : '2px solid #E5E7EB' }}>
                <div className="w-12 h-12 rounded-2xl flex items-center justify-center text-2xl font-black text-white"
                  style={{ background: 'linear-gradient(135deg, #7B5CE5, #A889F0)' }}>
                  {s.name[0].toUpperCase()}
                </div>
                <div className="text-left">
                  <div className="text-base font-black" style={{ color: '#1A1A2E' }}>{s.name}</div>
                  <div className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>
                    {s.grade}-то одд. · ⭐ {s.id in liveStars ? liveStars[s.id] : s.stars_total}
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>
      )}

      {selected && (
        <div className="bg-white rounded-3xl p-5" style={{ border: '2px solid #EDE9FF' }}>
          {students.length > 1 && (
            <button type="button" onClick={() => { setSelected(null); setPin('') }}
              className="text-sm font-bold mb-3 block" style={{ color: '#9B9BAA' }}>← Назад</button>
          )}
          <div className="text-center mb-4">
            <div className="w-12 h-12 rounded-2xl flex items-center justify-center text-xl font-black text-white mx-auto mb-2"
              style={{ background: 'linear-gradient(135deg, #7B5CE5, #A889F0)' }}>
              {selected.name[0].toUpperCase()}
            </div>
            <p className="font-black text-base" style={{ color: '#1A1A2E' }}>Здраво, {selected.name}!</p>
            <p className="text-sm" style={{ color: '#9B9BAA' }}>Внеси го твојот PIN</p>
          </div>
          <div className="flex justify-center gap-4 mb-4">
            {[0,1,2,3].map((i) => (
              <div key={i} className="w-3.5 h-3.5 rounded-full transition-all duration-150"
                style={{ background: i < pin.length ? '#5C35D4' : '#E5E7EB', transform: i < pin.length ? 'scale(1.2)' : 'scale(1)' }} />
            ))}
          </div>
          {error && <p className="text-center text-sm font-bold mb-3" style={{ color: '#FF6B6B' }}>⚠️ {error}</p>}
          <div className="grid grid-cols-3 gap-2">
            {KEYS.map((k) => (
              <button key={k} type="button"
                onClick={() => k === '⌫' ? setPin(p => p.slice(0,-1)) : k !== '✓' ? handlePin(k) : undefined}
                className="py-3.5 rounded-2xl text-xl font-black transition-all active:scale-90"
                style={{
                  background: k === '⌫' ? '#FFE8E8' : k === '✓' ? '#5C35D4' : '#F0EBFF',
                  color: k === '⌫' ? '#FF6B6B' : k === '✓' ? 'white' : '#1A1A2E',
                }}>
                {k}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

// ── MAIN LOGIN PAGE ───────────────────────────────────────────────
export default function LoginPage() {
  const router = useRouter()
  const [tab, setTab] = useState<Tab>('parent')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [students, setStudents] = useState<StudentProfile[] | null>(null)

  useEffect(() => {
    const family = getFamilySession()
    if (family && family.students.length > 0) {
      setStudents(family.students)
    }
  }, [])

  const handleParentLogin = async () => {
    setError('')
    if (!email.trim() || !password.trim()) return setError('Внеси е-пошта и лозинка.')
    setLoading(true)
    const result = await parentLogin(email.trim().toLowerCase(), password)
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    const isAdmin = await isDevAdminUser()
    router.push(isAdmin ? '/admin' : '/parent')
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
      style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>

      {/* Logo */}
      <div className="text-center mb-8">
        <div className="text-5xl mb-2 animate-float">⭐</div>
        <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>Супер Ѕвезда</h1>
      </div>

      <div className="w-full max-w-sm">
        {/* Tabs */}
        <div className="flex gap-1 p-1 rounded-2xl mb-4"
          style={{ background: 'rgba(255,255,255,0.6)' }}>
          {([
            { key: 'parent' as Tab, label: '👨‍👩‍👧 Родител' },
            { key: 'kid' as Tab,    label: '🧒 Дете' },
          ]).map((t) => (
            <button key={t.key} onClick={() => setTab(t.key)}
              className="flex-1 py-2.5 rounded-xl font-black text-sm transition-all"
              style={{
                background: tab === t.key ? 'white' : 'transparent',
                color: tab === t.key ? '#5C35D4' : '#9B9BAA',
                boxShadow: tab === t.key ? '0 2px 8px rgba(0,0,0,0.08)' : 'none',
              }}>
              {t.label}
            </button>
          ))}
        </div>

        {/* Parent login */}
        {tab === 'parent' && (
          <div className="bg-white rounded-3xl shadow-sm p-6 space-y-4"
            style={{ border: '2px solid #EDE9FF' }}>
            <h2 className="text-lg font-black text-center" style={{ color: '#1A1A2E' }}>Родителски пристап</h2>
            {[
              { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'ana@example.com' },
              { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: '••••••••' },
            ].map(({ label, val, set, type, ph }) => (
              <div key={label}>
                <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                <input type={type} value={val}
                  onChange={(e) => { set(e.target.value); setError('') }}
                  onKeyDown={(e) => e.key === 'Enter' && handleParentLogin()}
                  placeholder={ph}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                  style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
            ))}
            {error && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {error}</p>
              </div>
            )}
            <button type="button" onClick={handleParentLogin} disabled={loading}
              className="w-full py-4 rounded-2xl text-base font-black text-white transition-all active:scale-95 disabled:opacity-60"
              style={{ background: '#5C35D4', boxShadow: '0 4px 16px rgba(92,53,212,0.25)' }}>
              {loading ? 'Се логира...' : 'Влези →'}
            </button>
            <a href="/reset-password"
              className="block text-center text-sm font-semibold transition-colors"
              style={{ color: '#9B9BAA' }}>
              Заборавена лозинка?
            </a>
            <div className="flex items-center gap-3">
              <div className="flex-1 h-px" style={{ background: '#E5E7EB' }} />
              <span className="text-xs font-semibold" style={{ color: '#C4C4D4' }}>или</span>
              <div className="flex-1 h-px" style={{ background: '#E5E7EB' }} />
            </div>
            <button type="button" onClick={() => router.push('/register')}
              className="w-full py-3 rounded-2xl text-sm font-black border-2 transition-all active:scale-95"
              style={{ borderColor: '#5C35D4', color: '#5C35D4', background: 'white' }}>
              Нема профил? Регистрирај се →
            </button>
          </div>
        )}

        {/* Kid PIN login */}
        {tab === 'kid' && (
          <div>
            {students && students.length > 0 ? (
              <KidSelector students={students} />
            ) : (
              <div className="bg-white rounded-3xl p-8 text-center" style={{ border: '2px solid #EDE9FF' }}>
                <div className="text-5xl mb-4">🔐</div>
                <p className="font-black text-base mb-2" style={{ color: '#1A1A2E' }}>Нема зачуван профил</p>
                <p className="text-sm font-semibold mb-5" style={{ color: '#6B6B8A' }}>
                  Родителот треба прво да се најави за да може детето да влезе со PIN.
                </p>
                <button type="button" onClick={() => setTab('parent')}
                  className="w-full py-3 rounded-2xl font-black text-sm text-white"
                  style={{ background: '#5C35D4' }}>
                  Влези како родител →
                </button>
              </div>
            )}
          </div>
        )}
      </div>

      <button onClick={() => router.push('/')}
        className="mt-6 text-sm font-bold transition-colors"
        style={{ color: '#7B5CE5' }}>
        ← Назад на почеток
      </button>
    </main>
  )
}
