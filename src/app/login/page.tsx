'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { parentLogin, isDevAdminUser, getFamilySession, loginWithPin, updateStudentPin, getProgress, StudentProfile } from '@/lib/auth'
import StarMascot from '@/components/StarMascot'

type ResetStep = 'auth' | 'newpin' | 'done'

// ── KID FULL-SCREEN SELECTOR ──────────────────────────────────────
function KidFullScreen({ students, onParentClick }: { students: StudentProfile[]; onParentClick: () => void }) {
  const router = useRouter()
  const [selected, setSelected] = useState<StudentProfile | null>(null)
  const [pin, setPin] = useState('')
  const [error, setError] = useState('')
  const [liveStars, setLiveStars] = useState<Record<string, number>>({})

  // Reset-PIN flow
  const [resetStep, setResetStep] = useState<ResetStep | null>(null)
  const [resetEmail, setResetEmail] = useState('')
  const [resetPassword, setResetPassword] = useState('')
  const [resetError, setResetError] = useState('')
  const [resetLoading, setResetLoading] = useState(false)
  const [newPin, setNewPin] = useState('')

  useEffect(() => {
    Promise.all(
      students.map(async (s) => {
        const progress = await getProgress(s.id)
        const total = progress.reduce((sum, p) => sum + p.stars_earned, 0)
        return [s.id, total] as [string, number]
      })
    ).then(entries => setLiveStars(Object.fromEntries(entries)))
  }, [students])

  const clearSelected = () => {
    setSelected(null); setPin(''); setError('')
    setResetStep(null); setResetEmail(''); setResetPassword(''); setResetError(''); setNewPin('')
  }

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

  const handleResetAuth = async () => {
    setResetError('')
    if (!resetEmail.trim() || !resetPassword.trim()) return setResetError('Внеси е-пошта и лозинка.')
    setResetLoading(true)
    const result = await parentLogin(resetEmail.trim().toLowerCase(), resetPassword)
    setResetLoading(false)
    if (!result.ok) return setResetError('Погрешна е-пошта или лозинка.')
    setResetStep('newpin')
  }

  const handleNewPin = async (digit: string) => {
    if (newPin.length >= 4) return
    const next = newPin + digit
    setNewPin(next)
    setResetError('')
    if (next.length === 4) {
      if (!selected) return
      setResetLoading(true)
      const result = await updateStudentPin(selected.id, next)
      setResetLoading(false)
      if (!result.ok) {
        setTimeout(() => { setNewPin(''); setResetError(result.error!) }, 300)
        return
      }
      // Update local state so the kid can log in immediately with the new PIN
      setSelected({ ...selected, pin: next })
      setResetStep('done')
      setTimeout(() => { setResetStep(null); setNewPin(''); setPin('') }, 1800)
    }
  }

  const KEYS = ['1','2','3','4','5','6','7','8','9','⌫','0','✓']

  const AVATAR_COLORS = [
    'linear-gradient(135deg, #7B5CE5, #A889F0)',
    'linear-gradient(135deg, #F59E0B, #FCD34D)',
    'linear-gradient(135deg, #10B981, #6EE7B7)',
  ]

  if (selected) {
    const avatarBg = AVATAR_COLORS[students.indexOf(selected) % AVATAR_COLORS.length]

    // ── RESET: parent auth ──
    if (resetStep === 'auth') {
      return (
        <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
          style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>
          <button type="button" onClick={() => setResetStep(null)}
            className="self-start mb-6 text-sm font-bold" style={{ color: '#7B5CE5' }}>← Назад</button>
          <div className="w-full max-w-xs">
            <div className="text-center mb-6">
              <div className="text-3xl mb-2">🔐</div>
              <h2 className="text-xl font-black" style={{ color: '#1A1A2E' }}>Потврди со родителска лозинка</h2>
              <p className="text-sm font-semibold mt-1" style={{ color: '#9B9BAA' }}>
                За да го ресетираш PIN-от на {selected.name}
              </p>
            </div>
            <div className="bg-white rounded-3xl p-5 space-y-4" style={{ border: '2px solid #EDE9FF' }}>
              {[
                { label: 'Е-ПОШТА', val: resetEmail, set: setResetEmail, type: 'email', ph: 'roditel@example.com' },
                { label: 'ЛОЗИНКА', val: resetPassword, set: setResetPassword, type: 'password', ph: '••••••••' },
              ].map(({ label, val, set, type, ph }) => (
                <div key={label}>
                  <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                  <input type={type} value={val}
                    onChange={e => { set(e.target.value); setResetError('') }}
                    onKeyDown={e => e.key === 'Enter' && handleResetAuth()}
                    placeholder={ph}
                    className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                    style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
                </div>
              ))}
              {resetError && (
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {resetError}</p>
              )}
              <button type="button" onClick={handleResetAuth} disabled={resetLoading}
                className="w-full py-4 rounded-2xl font-black text-white transition-all active:scale-95 disabled:opacity-60"
                style={{ background: '#5C35D4' }}>
                {resetLoading ? 'Се проверува...' : 'Потврди →'}
              </button>
            </div>
          </div>
        </div>
      )
    }

    // ── RESET: new PIN entry ──
    if (resetStep === 'newpin' || resetStep === 'done') {
      return (
        <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
          style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>
          <div className="w-full max-w-xs">
            <div className="text-center mb-8">
              <div className="w-20 h-20 rounded-3xl flex items-center justify-center text-4xl font-black text-white mx-auto mb-3"
                style={{ background: avatarBg }}>
                {selected.name[0].toUpperCase()}
              </div>
              {resetStep === 'done' ? (
                <>
                  <div className="text-4xl mb-2">✅</div>
                  <h2 className="text-xl font-black" style={{ color: '#2D7A35' }}>PIN успешно сменет!</h2>
                </>
              ) : (
                <>
                  <h2 className="text-xl font-black" style={{ color: '#1A1A2E' }}>Нов PIN за {selected.name}</h2>
                  <p className="text-sm font-semibold mt-1" style={{ color: '#9B9BAA' }}>Внеси 4 цифри</p>
                </>
              )}
            </div>

            {resetStep === 'newpin' && (
              <>
                <div className="flex justify-center gap-5 mb-6">
                  {[0,1,2,3].map(i => (
                    <div key={i} className="w-4 h-4 rounded-full transition-all duration-150"
                      style={{ background: i < newPin.length ? '#10B981' : '#E5E7EB', transform: i < newPin.length ? 'scale(1.3)' : 'scale(1)' }} />
                  ))}
                </div>
                {resetError && <p className="text-center text-sm font-bold mb-4" style={{ color: '#FF6B6B' }}>⚠️ {resetError}</p>}
                <div className="bg-white rounded-3xl p-4" style={{ border: '2px solid #D4F5EC', boxShadow: '0 4px 20px rgba(16,185,129,0.08)' }}>
                  <div className="grid grid-cols-3 gap-2.5">
                    {KEYS.map(k => (
                      <button key={k} type="button"
                        onClick={() => k === '⌫' ? setNewPin(p => p.slice(0,-1)) : k !== '✓' ? handleNewPin(k) : undefined}
                        disabled={resetLoading}
                        className="py-4 rounded-2xl text-2xl font-black transition-all active:scale-90 disabled:opacity-50"
                        style={{
                          background: k === '⌫' ? '#FFE8E8' : k === '✓' ? '#10B981' : '#F0FFF8',
                          color: k === '⌫' ? '#FF6B6B' : k === '✓' ? 'white' : '#1A1A2E',
                        }}>
                        {k}
                      </button>
                    ))}
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      )
    }

    // ── NORMAL: PIN entry ──
    return (
      <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
        style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>
        <button type="button" onClick={clearSelected}
          className="self-start mb-6 text-sm font-bold flex items-center gap-1"
          style={{ color: '#7B5CE5' }}>
          ← Назад
        </button>

        <div className="w-full max-w-xs">
          {/* Avatar + greeting */}
          <div className="text-center mb-8">
            <div className="w-20 h-20 rounded-3xl flex items-center justify-center text-4xl font-black text-white mx-auto mb-3"
              style={{ background: avatarBg, boxShadow: '0 8px 24px rgba(92,53,212,0.25)' }}>
              {selected.name[0].toUpperCase()}
            </div>
            <h2 className="text-2xl font-black" style={{ color: '#1A1A2E' }}>Здраво, {selected.name}!</h2>
            <p className="text-sm font-semibold mt-1" style={{ color: '#9B9BAA' }}>Внеси го твојот PIN</p>
          </div>

          {/* PIN dots */}
          <div className="flex justify-center gap-5 mb-6">
            {[0,1,2,3].map((i) => (
              <div key={i} className="w-4 h-4 rounded-full transition-all duration-150"
                style={{
                  background: i < pin.length ? '#5C35D4' : '#E5E7EB',
                  transform: i < pin.length ? 'scale(1.3)' : 'scale(1)',
                }} />
            ))}
          </div>

          {error && (
            <p className="text-center text-sm font-bold mb-4" style={{ color: '#FF6B6B' }}>⚠️ {error}</p>
          )}

          {/* Keypad */}
          <div className="bg-white rounded-3xl p-4" style={{ border: '2px solid #EDE9FF', boxShadow: '0 4px 20px rgba(92,53,212,0.08)' }}>
            <div className="grid grid-cols-3 gap-2.5">
              {KEYS.map((k) => (
                <button key={k} type="button"
                  onClick={() => k === '⌫' ? setPin(p => p.slice(0,-1)) : k !== '✓' ? handlePin(k) : undefined}
                  className="py-4 rounded-2xl text-2xl font-black transition-all active:scale-90"
                  style={{
                    background: k === '⌫' ? '#FFE8E8' : k === '✓' ? '#5C35D4' : '#F0EBFF',
                    color: k === '⌫' ? '#FF6B6B' : k === '✓' ? 'white' : '#1A1A2E',
                  }}>
                  {k}
                </button>
              ))}
            </div>
          </div>

          {/* Forgot PIN */}
          <button type="button" onClick={() => { setResetStep('auth'); setResetEmail(''); setResetPassword(''); setResetError('') }}
            className="w-full mt-4 text-sm font-semibold text-center transition-colors"
            style={{ color: '#C4C4D4' }}>
            Заборавен PIN?
          </button>
        </div>

        {/* Parent link */}
        <button type="button" onClick={onParentClick}
          className="mt-8 text-sm font-semibold transition-colors"
          style={{ color: '#C4C4D4' }}>
          Родителски профил →
        </button>
      </div>
    )
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
      style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>

      {/* Logo */}
      <div className="text-center mb-10">
        <StarMascot mood="calm" size={100} className="mx-auto" />
        <h1 className="text-3xl font-black mt-1" style={{ color: '#1A1A2E' }}>Супер Ѕвезда</h1>
        <p className="text-base font-semibold mt-1" style={{ color: '#9B9BAA' }}>Кој учи денес? 👋</p>
      </div>

      {/* Kid cards */}
      <div className="w-full max-w-sm space-y-3">
        {students.map((s, idx) => (
          <button key={s.id} type="button"
            onClick={() => { setSelected(s); setPin(''); setError('') }}
            className="w-full bg-white rounded-3xl p-5 flex items-center gap-4 transition-all active:scale-95"
            style={{ border: '2px solid #EDE9FF', boxShadow: '0 4px 16px rgba(92,53,212,0.08)' }}>
            <div className="w-16 h-16 rounded-2xl flex items-center justify-center text-3xl font-black text-white flex-shrink-0"
              style={{ background: AVATAR_COLORS[idx % AVATAR_COLORS.length] }}>
              {s.name[0].toUpperCase()}
            </div>
            <div className="text-left flex-1">
              <div className="text-xl font-black" style={{ color: '#1A1A2E' }}>{s.name}</div>
              <div className="text-sm font-semibold mt-0.5" style={{ color: '#9B9BAA' }}>
                {s.grade}-то одделение · ⭐ {s.id in liveStars ? liveStars[s.id] : s.stars_total}
              </div>
            </div>
            <div className="text-2xl" style={{ color: '#C4C4D4' }}>›</div>
          </button>
        ))}
      </div>

      {/* Parent link */}
      <button type="button" onClick={onParentClick}
        className="mt-12 text-sm font-semibold transition-colors"
        style={{ color: '#C4C4D4' }}>
        Родителски профил →
      </button>
    </div>
  )
}

// ── PARENT LOGIN FORM ─────────────────────────────────────────────
function ParentLoginForm({ onBack, hasFamily }: { onBack?: () => void; hasFamily: boolean }) {
  const router = useRouter()
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
    const isAdmin = await isDevAdminUser()
    router.push(isAdmin ? '/admin' : '/parent')
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
      style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>

      {/* Logo */}
      <div className="text-center mb-8">
        <StarMascot mood="calm" size={88} className="mx-auto" />
        <h1 className="text-3xl font-black mt-1" style={{ color: '#1A1A2E' }}>Супер Ѕвезда</h1>
      </div>

      <div className="w-full max-w-sm">
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
                onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
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

          <button type="button" onClick={handleLogin} disabled={loading}
            className="w-full py-4 rounded-2xl text-base font-black text-white transition-all active:scale-95 disabled:opacity-60"
            style={{ background: '#5C35D4', boxShadow: '0 4px 16px rgba(92,53,212,0.25)' }}>
            {loading ? 'Се логира...' : 'Влези →'}
          </button>

          <a href="/reset-password"
            className="block text-center text-sm font-semibold"
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

        {hasFamily && onBack && (
          <button type="button" onClick={onBack}
            className="w-full mt-4 text-sm font-semibold text-center"
            style={{ color: '#9B9BAA' }}>
            ← Назад кон деца
          </button>
        )}

        {!hasFamily && (
          <button onClick={() => router.push('/')}
            className="w-full mt-4 text-sm font-bold text-center"
            style={{ color: '#7B5CE5' }}>
            ← Назад на почеток
          </button>
        )}
      </div>
    </main>
  )
}

// ── MAIN ──────────────────────────────────────────────────────────
export default function LoginPage() {
  const [students, setStudents] = useState<StudentProfile[] | null>(null)
  const [showParent, setShowParent] = useState(false)
  const [ready, setReady] = useState(false)

  useEffect(() => {
    const family = getFamilySession()
    if (family && family.students.length > 0) {
      setStudents(family.students)
    }
    setReady(true)
  }, [])

  if (!ready) return null

  const hasFamily = !!(students && students.length > 0)

  if (hasFamily && !showParent) {
    return (
      <KidFullScreen
        students={students!}
        onParentClick={() => setShowParent(true)}
      />
    )
  }

  return (
    <ParentLoginForm
      hasFamily={hasFamily}
      onBack={hasFamily ? () => setShowParent(false) : undefined}
    />
  )
}
