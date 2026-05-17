'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { register } from '@/lib/auth'
import TownSchoolPicker from '@/components/TownSchoolPicker'

const GRADES = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const

function capitalizeWords(val: string) {
  return val.replace(/(^|\s)(\S)/g, (_, sp, ch) => sp + ch.toUpperCase())
}
function isCyrillicName(val: string) {
  return /^[Ѐ-ӿ\s\-]+$/.test(val.trim())
}

export default function RegisterPage() {
  const router = useRouter()
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
    const result = await register({
      email: email.trim().toLowerCase(),
      password,
      parentName: parentName.trim(),
      studentName: studentName.trim(),
      grade,
      pin,
      town: town || undefined,
      school: school || undefined,
    })
    setLoading(false)
    if (!result.ok) return setError(result.error!)
    router.push('/parent')
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-5 py-10"
      style={{ background: 'linear-gradient(160deg, #EDE9FF 0%, #D4F5EC 100%)' }}>

      {/* Logo */}
      <div className="text-center mb-6">
        <div className="text-5xl mb-2 animate-float">⭐</div>
        <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>Супер Ѕвезда</h1>
      </div>

      <div className="w-full max-w-md">
        <div className="bg-white rounded-3xl shadow-sm overflow-hidden" style={{ border: '2px solid #EDE9FF' }}>
          {/* Banner */}
          <div className="p-3 text-center font-black text-sm text-white"
            style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
            🎉 14 дена бесплатно — без кредитна картичка!
          </div>

          <div className="p-6 space-y-4">
            <h2 className="text-xl font-black text-center" style={{ color: '#1A1A2E' }}>Креирај семеен профил</h2>

            {/* Parent fields */}
            <div className="space-y-3">
              <p className="text-xs font-black tracking-widest" style={{ color: '#9B9BAA' }}>РОДИТЕЛ</p>
              {[
                { label: 'ИМЕ И ПРЕЗИМЕ', val: parentName, set: setParentName, type: 'text', ph: 'Ана Петровска', transform: capitalizeWords },
                { label: 'Е-ПОШТА', val: email, set: setEmail, type: 'email', ph: 'ana@example.com' },
                { label: 'ЛОЗИНКА', val: password, set: setPassword, type: 'password', ph: 'Минимум 6 знаци' },
              ].map(({ label, val, set, type, ph, transform }: { label: string; val: string; set: (v: string) => void; type: string; ph: string; transform?: (v: string) => string }) => (
                <div key={label}>
                  <label className="block text-xs font-black mb-1" style={{ color: '#6B6B8A' }}>{label}</label>
                  <input type={type} value={val}
                    onChange={(e) => { set(transform ? transform(e.target.value) : e.target.value); setError('') }}
                    placeholder={ph}
                    className="w-full px-4 py-3 rounded-2xl border-2 font-semibold text-base outline-none"
                    style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
                </div>
              ))}
            </div>

            {/* Kid fields */}
            <div className="border-t pt-3 space-y-3" style={{ borderColor: '#EDE9FF' }}>
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
                      style={{
                        background: grade === g ? '#5C35D4' : '#F0EBFF',
                        color: grade === g ? 'white' : '#5C35D4',
                        borderColor: grade === g ? '#5C35D4' : 'transparent',
                      }}>
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
              style={{ background: '#5C35D4', boxShadow: '0 4px 16px rgba(92,53,212,0.25)' }}>
              {loading ? 'Се регистрира...' : 'Почни со учење! ⭐'}
            </button>
          </div>
        </div>

        <button onClick={() => router.push('/login')}
          className="mt-5 w-full text-center text-sm font-bold py-2 transition-colors"
          style={{ color: '#7B5CE5' }}>
          ← Назад кон Влези
        </button>
      </div>
    </main>
  )
}
