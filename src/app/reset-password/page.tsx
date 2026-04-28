'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'

export default function ResetPasswordPage() {
  const router = useRouter()
  const [email, setEmail] = useState('')
  const [sent, setSent] = useState(false)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleReset = async () => {
    setError('')
    if (!email.includes('@')) return setError('Внеси валидна е-пошта.')
    setLoading(true)
    const { error: err } = await supabase.auth.resetPasswordForEmail(
      email.trim().toLowerCase(),
      { redirectTo: `${window.location.origin}/update-password` },
    )
    setLoading(false)
    if (err) return setError('Грешка: ' + err.message)
    setSent(true)
  }

  return (
    <main className="min-h-screen flex items-center justify-center px-5 relative overflow-hidden"
      style={{ background: 'linear-gradient(160deg, #07040F 0%, #130726 30%, #2D1B69 70%, #5C35D4 100%)' }}>

      <div className="w-full max-w-sm">
        <div className="text-center mb-8">
          <div className="text-5xl mb-2 animate-float">⭐</div>
          <h1 className="text-3xl font-black text-white">Супер Ѕвезда</h1>
        </div>

        <div className="bg-white rounded-3xl shadow-2xl p-7">
          {sent ? (
            <div className="text-center">
              <div className="text-5xl mb-4">📧</div>
              <h2 className="text-xl font-black mb-3" style={{ color: '#1A1A2E' }}>Провери ја е-поштата!</h2>
              <p className="text-sm font-semibold mb-6" style={{ color: '#6B6B8A' }}>
                Ти пративме линк за ресетирање на лозинката на <span className="font-black" style={{ color: '#5C35D4' }}>{email}</span>.
              </p>
              <p className="text-xs mb-6" style={{ color: '#9B9BAA' }}>
                Не го гледаш? Провери ја папката Spam.
              </p>
              <button onClick={() => router.push('/')}
                className="w-full py-3 rounded-2xl font-black text-white"
                style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                ← Назад на почеток
              </button>
            </div>
          ) : (
            <>
              <h2 className="text-xl font-black text-center mb-1" style={{ color: '#1A1A2E' }}>🔑 Заборавена лозинка</h2>
              <p className="text-sm text-center font-semibold mb-5" style={{ color: '#9B9BAA' }}>
                Внеси ја е-поштата и ќе ти пратиме линк.
              </p>
              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>Е-ПОШТА</label>
                  <input type="email" value={email}
                    onChange={(e) => { setEmail(e.target.value); setError('') }}
                    onKeyDown={(e) => e.key === 'Enter' && handleReset()}
                    placeholder="ana@example.com"
                    className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                    style={{ borderColor: email ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
                </div>
                {error && (
                  <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                    <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {error}</p>
                  </div>
                )}
                <button onClick={handleReset} disabled={loading}
                  className="w-full py-4 rounded-2xl text-lg font-black text-white disabled:opacity-60 transition-all active:scale-95"
                  style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                  {loading ? 'Се испраќа...' : 'Испрати линк →'}
                </button>
                <button onClick={() => router.push('/')}
                  className="w-full py-2 text-sm font-bold text-center" style={{ color: '#9B9BAA' }}>
                  ← Назад
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </main>
  )
}
