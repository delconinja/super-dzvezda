'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'

export default function UpdatePasswordPage() {
  const router = useRouter()
  const [password, setPassword] = useState('')
  const [confirm, setConfirm] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [done, setDone] = useState(false)
  const [ready, setReady] = useState(false)

  useEffect(() => {
    // Supabase puts the access token in the URL hash after redirect
    supabase.auth.onAuthStateChange((event) => {
      if (event === 'PASSWORD_RECOVERY') setReady(true)
    })
  }, [])

  const handleUpdate = async () => {
    setError('')
    if (password.length < 6) return setError('Лозинката мора да има барем 6 знаци.')
    if (password !== confirm) return setError('Лозинките не се совпаѓаат.')
    setLoading(true)
    const { error: err } = await supabase.auth.updateUser({ password })
    setLoading(false)
    if (err) return setError('Грешка: ' + err.message)
    setDone(true)
    setTimeout(() => router.push('/'), 2500)
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
          {done ? (
            <div className="text-center">
              <div className="text-5xl mb-4">✅</div>
              <h2 className="text-xl font-black mb-2" style={{ color: '#1A1A2E' }}>Лозинката е сменета!</h2>
              <p className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>Те пренасочуваме...</p>
            </div>
          ) : !ready ? (
            <div className="text-center py-4">
              <div className="text-4xl mb-3 animate-float">⏳</div>
              <p className="font-semibold" style={{ color: '#6B6B8A' }}>Се верификува линкот...</p>
            </div>
          ) : (
            <>
              <h2 className="text-xl font-black text-center mb-1" style={{ color: '#1A1A2E' }}>🔐 Нова лозинка</h2>
              <p className="text-sm text-center font-semibold mb-5" style={{ color: '#9B9BAA' }}>Внеси нова лозинка за твојот профил.</p>
              <div className="space-y-4">
                {[
                  { label: 'НОВА ЛОЗИНКА', val: password, set: setPassword, ph: 'Минимум 6 знаци' },
                  { label: 'ПОТВРДИ ЛОЗИНКА', val: confirm, set: setConfirm, ph: 'Повтори ја лозинката' },
                ].map(({ label, val, set, ph }) => (
                  <div key={label}>
                    <label className="block text-xs font-black mb-1.5 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                    <input type="password" value={val}
                      onChange={(e) => { set(e.target.value); setError('') }}
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
                <button onClick={handleUpdate} disabled={loading}
                  className="w-full py-4 rounded-2xl text-lg font-black text-white disabled:opacity-60 transition-all active:scale-95"
                  style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                  {loading ? 'Се зачувува...' : 'Зачувај лозинка →'}
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </main>
  )
}
