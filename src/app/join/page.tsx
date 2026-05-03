'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { joinAffiliate, affiliateLogin, checkCodeAvailable } from '@/lib/affiliate'

type View = 'signup' | 'login' | 'success'

function capitalizeWords(val: string) {
  return val.replace(/(^|\s)(\S)/g, (_, sp, ch) => sp + ch.toUpperCase())
}

function isCyrillicName(val: string) {
  return /^[Ѐ-ӿ\s\-]+$/.test(val.trim())
}

function isValidCode(val: string) {
  return /^[a-z0-9_-]{3,20}$/.test(val)
}

export default function JoinPage() {
  const router = useRouter()
  const [view, setView] = useState<View>('signup')

  // signup fields
  const [name, setName] = useState('')
  const [code, setCode] = useState('')
  const [codeStatus, setCodeStatus] = useState<'idle' | 'checking' | 'ok' | 'taken'>('idle')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [channel, setChannel] = useState('')
  const [payoutInfo, setPayoutInfo] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  // login fields
  const [loginEmail, setLoginEmail] = useState('')
  const [loginPassword, setLoginPassword] = useState('')
  const [loginError, setLoginError] = useState('')
  const [loginLoading, setLoginLoading] = useState(false)

  const handleCodeBlur = async () => {
    if (!code || !isValidCode(code)) return
    setCodeStatus('checking')
    const available = await checkCodeAvailable(code)
    setCodeStatus(available ? 'ok' : 'taken')
  }

  const handleSignup = async () => {
    setError('')
    if (!name.trim()) return setError('Внеси го твоето име.')
    if (!isCyrillicName(name)) return setError('Името мора да биде на кирилица.')
    if (!isValidCode(code)) return setError('Кодот мора да биде 3–20 знаци: само мали букви, бројки, - или _')
    if (codeStatus === 'taken') return setError('Овој код е зафатен. Одбери друг.')
    if (!email.includes('@')) return setError('Внеси валидна е-пошта.')
    if (password.length < 6) return setError('Лозинката мора да има барем 6 знаци.')
    if (!channel.trim()) return setError('Додади линк до твојот канал / профил.')
    setLoading(true)
    const result = await joinAffiliate({ name, code, email, password, channel, payoutInfo })
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    setView('success')
  }

  const handleLogin = async () => {
    setLoginError('')
    if (!loginEmail.trim() || !loginPassword.trim()) return setLoginError('Внеси е-пошта и лозинка.')
    setLoginLoading(true)
    const result = await affiliateLogin(loginEmail.trim().toLowerCase(), loginPassword)
    setLoginLoading(false)
    if (!result.ok) return setLoginError(result.error!)
    router.push('/affiliate')
  }

  if (view === 'success') return (
    <main className="min-h-screen flex items-center justify-center px-4"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>
      <div className="bg-white rounded-3xl p-8 max-w-md w-full text-center">
        <div className="text-6xl mb-4">🎉</div>
        <h1 className="text-2xl font-black mb-3" style={{ color: '#1A1A2E' }}>Пријавата е примена!</h1>
        <p className="font-semibold mb-2" style={{ color: '#6B6B8A' }}>
          Ќе ја разгледаме твојата пријава во рок од 24 часа.
        </p>
        <p className="text-sm mb-6" style={{ color: '#9B9BAA' }}>
          Кога ќе биде одобрена, ќе добиеш е-пошта и ќе можеш да влезеш на твојот партнерски профил.
        </p>
        <div className="rounded-2xl p-4 mb-6" style={{ background: '#F7F5FF' }}>
          <p className="text-xs font-black tracking-widest mb-1" style={{ color: '#5C35D4' }}>ТВОЈОТ ЛИНК (по одобрување)</p>
          <p className="font-black text-sm" style={{ color: '#1A1A2E' }}>
            super-dzvezda.mk/?ref={code}
          </p>
        </div>
        <button onClick={() => router.push('/')}
          className="text-sm font-bold" style={{ color: '#5C35D4' }}>
          ← Назад на почеток
        </button>
      </div>
    </main>
  )

  return (
    <main className="min-h-screen px-4 py-10"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>

      <div className="text-center mb-8">
        <div className="text-5xl mb-3">🤝</div>
        <h1 className="text-3xl font-black text-white">Партнерска програма</h1>
        <p className="text-purple-200 mt-2 max-w-sm mx-auto text-sm">
          Промовирај Супер Ѕвезда и заработи <span className="font-black text-yellow-300">30% комисија</span> на секоја претплата — секој месец.
        </p>
      </div>

      {/* How it works */}
      <div className="max-w-md mx-auto mb-6 grid grid-cols-3 gap-3">
        {[
          { icon: '🔗', title: 'Сподели линк', desc: 'Твој уникатен линк' },
          { icon: '📲', title: 'Некој се претплати', desc: 'Преку твојот линк' },
          { icon: '💰', title: 'Заработи 30%', desc: 'Секој месец, рекурентно' },
        ].map((s) => (
          <div key={s.title} className="bg-white/10 rounded-2xl p-3 text-center">
            <div className="text-2xl mb-1">{s.icon}</div>
            <div className="text-white font-black text-xs">{s.title}</div>
            <div className="text-purple-300 text-xs mt-0.5">{s.desc}</div>
          </div>
        ))}
      </div>

      <div className="max-w-md mx-auto">
        {/* Tab toggle */}
        <div className="flex gap-1 p-1 rounded-2xl mb-4" style={{ background: 'rgba(255,255,255,0.1)' }}>
          {(['signup', 'login'] as const).map((v) => (
            <button key={v} onClick={() => { setView(v); setError(''); setLoginError('') }}
              className="flex-1 py-2 rounded-xl font-black text-sm transition-all"
              style={{
                background: view === v ? 'white' : 'transparent',
                color: view === v ? '#5C35D4' : 'rgba(255,255,255,0.6)',
              }}>
              {v === 'signup' ? 'Пријави се' : 'Влези'}
            </button>
          ))}
        </div>

        {view === 'login' ? (
          <div className="bg-white rounded-3xl p-6 space-y-4">
            <h2 className="font-black text-lg" style={{ color: '#1A1A2E' }}>Партнерски вход</h2>
            {[
              { label: 'Е-ПОШТА', val: loginEmail, set: setLoginEmail, type: 'email', ph: 'ana@example.com' },
              { label: 'ЛОЗИНКА', val: loginPassword, set: setLoginPassword, type: 'password', ph: '••••••' },
            ].map(({ label, val, set, type, ph }) => (
              <div key={label}>
                <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                <input type={type} value={val} onChange={(e) => { set(e.target.value); setLoginError('') }}
                  onKeyDown={(e) => e.key === 'Enter' && handleLogin()}
                  placeholder={ph}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                  style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
            ))}
            {loginError && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {loginError}</p>
              </div>
            )}
            <button onClick={handleLogin} disabled={loginLoading}
              className="w-full py-4 rounded-2xl font-black text-white disabled:opacity-60 transition-all active:scale-95"
              style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              {loginLoading ? 'Се вчитува...' : 'Влези →'}
            </button>
          </div>
        ) : (
          <div className="bg-white rounded-3xl p-6 space-y-4">
            <h2 className="font-black text-lg" style={{ color: '#1A1A2E' }}>Твои информации</h2>

            {/* Name */}
            <div>
              <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>ПОЛНО ИМЕ</label>
              <input type="text" value={name}
                onChange={(e) => { setName(capitalizeWords(e.target.value)); setError('') }}
                placeholder="Марко Поповски"
                className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                style={{ borderColor: name ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
            </div>

            {/* Code */}
            <div>
              <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>ТВОЈ УНИКАТЕН КОД</label>
              <div className="relative">
                <input type="text" value={code}
                  onChange={(e) => { setCode(e.target.value.toLowerCase().replace(/[^a-z0-9_-]/g, '')); setCodeStatus('idle'); setError('') }}
                  onBlur={handleCodeBlur}
                  placeholder="marko7"
                  maxLength={20}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none pr-10"
                  style={{
                    borderColor: codeStatus === 'ok' ? '#6BCB77' : codeStatus === 'taken' ? '#FF6B6B' : code ? '#5C35D4' : '#E5E7EB',
                    color: '#1A1A2E', background: '#FAFAFA',
                  }} />
                {codeStatus === 'ok' && <span className="absolute right-3 top-3.5 text-lg">✅</span>}
                {codeStatus === 'taken' && <span className="absolute right-3 top-3.5 text-lg">❌</span>}
                {codeStatus === 'checking' && <span className="absolute right-3 top-3.5 text-sm" style={{ color: '#9B9BAA' }}>...</span>}
              </div>
              <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>
                Твојот линк: super-dzvezda.mk/?ref={code || 'marko7'}
              </p>
            </div>

            {/* Email + Password */}
            {[
              { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'marko@example.com' },
              { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: 'Минимум 6 знаци' },
            ].map(({ label, val, set, type, ph }) => (
              <div key={label}>
                <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                <input type={type} value={val} onChange={(e) => { set(e.target.value); setError('') }}
                  placeholder={ph}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                  style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
            ))}

            {/* Channel */}
            <div>
              <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>КАНАЛ / ПРОФИЛ</label>
              <input type="text" value={channel} onChange={(e) => { setChannel(e.target.value); setError('') }}
                placeholder="instagram.com/marko или tiktok.com/@marko"
                className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                style={{ borderColor: channel ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
            </div>

            {/* Payout info */}
            <div>
              <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>БАНКАРСКА СМЕТКА (за исплата)</label>
              <input type="text" value={payoutInfo} onChange={(e) => { setPayoutInfo(e.target.value); setError('') }}
                placeholder="Назив на банка · IBAN"
                className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                style={{ borderColor: payoutInfo ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>Може да ја додадеш подоцна.</p>
            </div>

            {error && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {error}</p>
              </div>
            )}

            {/* Commission info */}
            <div className="rounded-2xl p-4" style={{ background: '#F7F5FF', border: '1.5px solid #EDE9FF' }}>
              <p className="text-xs font-black" style={{ color: '#5C35D4' }}>💰 КОЛКУ МОЖЕШ ДА ЗАРАБОТИШ?</p>
              <p className="text-sm mt-1 font-semibold" style={{ color: '#3A3A5C' }}>
                10 активни претплати × €10 × 30% = <span className="font-black">€30/месец</span>
              </p>
              <p className="text-xs mt-0.5" style={{ color: '#9B9BAA' }}>Рекурентно — секој месец додека претплатата е активна.</p>
            </div>

            <button onClick={handleSignup} disabled={loading}
              className="w-full py-4 rounded-2xl font-black text-lg text-white disabled:opacity-60 transition-all active:scale-95"
              style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              {loading ? 'Се регистрира...' : 'Пријави се за партнер →'}
            </button>
          </div>
        )}
      </div>
    </main>
  )
}
