'use client'

export const dynamic = 'force-dynamic'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'
import {
  getStudents, getSubscription, addStudent, parentLogout,
  setActiveStudent, trialDaysLeft, isTrialExpired,
  StudentProfile, Subscription,
} from '@/lib/auth'
import TownSchoolPicker from '@/components/TownSchoolPicker'

const GRADES = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const

const GRADE_COLORS = ['#5C35D4', '#6BCB77', '#FF6B6B', '#FFD93D', '#FF9A3C', '#7B5CE5', '#FF6B6B', '#6BCB77', '#FFD93D']

function kidColor(grade: number) {
  return GRADE_COLORS[(grade - 1) % GRADE_COLORS.length]
}

function ordinal(g: number) {
  return `${g}-то одд.`
}

function capitalizeWords(val: string) {
  return val.replace(/(^|\s)(\S)/g, (_, sp, ch) => sp + ch.toUpperCase())
}

function isCyrillicName(val: string) {
  return /^[Ѐ-ӿ\s\-]+$/.test(val.trim())
}

export default function ParentPage() {
  const router = useRouter()
  const [parentName, setParentName] = useState('')
  const [students, setStudents] = useState<StudentProfile[]>([])
  const [sub, setSub] = useState<Subscription | null>(null)
  const [loading, setLoading] = useState(true)

  const [showAdd, setShowAdd] = useState(false)
  const [newName, setNewName] = useState('')
  const [newGrade, setNewGrade] = useState<number | null>(null)
  const [newPin, setNewPin] = useState('')
  const [newTown, setNewTown] = useState('')
  const [newSchool, setNewSchool] = useState('')
  const [addError, setAddError] = useState('')
  const [addLoading, setAddLoading] = useState(false)

  useEffect(() => {
    const init = async () => {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) { router.push('/'); return }
      setParentName(user.user_metadata?.full_name || user.email || 'Родитело')
      const [studs, subscription] = await Promise.all([getStudents(), getSubscription()])
      setStudents(studs)
      setSub(subscription)
      setLoading(false)
    }
    init()
  }, [router])

  const handleSelectKid = (student: StudentProfile) => {
    setActiveStudent(student)
    router.push('/dashboard')
  }

  const handleAddKid = async () => {
    setAddError('')
    if (!newName.trim()) return setAddError('Внеси го името на детето.')
    if (!isCyrillicName(newName)) return setAddError('Името мора да биде на кирилица.')
    if (!newGrade) return setAddError('Одбери одделение.')
    if (newPin.length !== 4) return setAddError('PIN мора да има 4 цифри.')
    setAddLoading(true)
    const result = await addStudent({ studentName: newName.trim(), grade: newGrade, pin: newPin, town: newTown || undefined, school: newSchool || undefined })
    setAddLoading(false)
    if (!result.ok) return setAddError(result.error!)
    setStudents((prev) => [...prev, result.student!])
    setNewName(''); setNewGrade(null); setNewPin(''); setNewTown(''); setNewSchool(''); setShowAdd(false)
  }

  const handleLogout = async () => {
    await parentLogout()
    router.push('/')
  }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center"
      style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69, #5C35D4)' }}>
      <div className="text-6xl animate-float">⭐</div>
    </div>
  )

  const daysLeft = sub ? trialDaysLeft(sub) : 0
  const expired = sub ? isTrialExpired(sub) : false
  const trialColor = expired ? '#FF6B6B' : daysLeft <= 3 ? '#FF6B6B' : daysLeft <= 7 ? '#FFD93D' : '#6BCB77'
  const canAdd = students.length < 3

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>

      {/* Header */}
      <header className="px-6 py-4 flex items-center justify-between"
        style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)' }}>
        <div className="flex items-center gap-3">
          <span className="text-3xl">⭐</span>
          <span className="text-white font-black text-xl">Супер Ѕвезда</span>
        </div>
        <button onClick={handleLogout}
          className="text-white/50 hover:text-white/90 text-sm font-bold transition-colors">
          Излези
        </button>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8 space-y-6">

        {/* Greeting */}
        <div>
          <p className="text-sm font-bold mb-1" style={{ color: '#6B6B8A' }}>РОДИТЕЛСКИ ПРОФИЛ</p>
          <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>
            Здраво, {parentName.split(' ')[0]}! 👪
          </h1>
        </div>

        {/* Subscription status */}
        {sub && (
          <div className="rounded-3xl p-5 flex items-center justify-between"
            style={{ background: `${trialColor}18`, border: `2px solid ${trialColor}55` }}>
            <div>
              <p className="text-xs font-black tracking-widest mb-1" style={{ color: trialColor }}>
                {sub.status === 'active' ? 'АКТИВНА ПРЕТПЛАТА' : expired ? 'ПРОБЕН ПЕРИОД — ИСТЕЧЕН' : 'ПРОБЕН ПЕРИОД'}
              </p>
              <p className="text-2xl font-black" style={{ color: '#1A1A2E' }}>
                {sub.status === 'active'
                  ? 'Активна'
                  : expired
                    ? 'Истечен'
                    : `${daysLeft} ${daysLeft === 1 ? 'ден' : 'дена'} останати`}
              </p>
            </div>
            {(sub.status === 'trial' || expired) && (
              <button
                onClick={() => router.push('/trial-expired')}
                className="px-5 py-3 rounded-2xl text-sm font-black text-white transition-all active:scale-95"
                style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                Надгради ↗
              </button>
            )}
          </div>
        )}

        {/* Kids section */}
        <div>
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-black" style={{ color: '#1A1A2E' }}>
              Моите деца
              <span className="ml-2 text-sm font-bold px-2 py-0.5 rounded-full"
                style={{ background: '#EDE9FF', color: '#5C35D4' }}>
                {students.length}/3
              </span>
            </h2>
            {canAdd && !showAdd && (
              <button onClick={() => setShowAdd(true)}
                className="px-4 py-2 rounded-2xl text-sm font-black text-white transition-all active:scale-95"
                style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                + Додади дете
              </button>
            )}
          </div>

          {students.length === 0 && !showAdd && (
            <div className="rounded-3xl p-8 text-center bg-white">
              <p className="text-4xl mb-3">👧</p>
              <p className="font-bold" style={{ color: '#6B6B8A' }}>Нема додадени деца.</p>
              <p className="text-sm mt-1" style={{ color: '#9B9BAA' }}>Додади го првото дете за да почне учењето!</p>
            </div>
          )}

          <div className="space-y-3">
            {students.map((s) => (
              <div key={s.id} className="bg-white rounded-3xl p-5 flex items-center gap-4"
                style={{ boxShadow: '0 2px 12px rgba(92,53,212,0.08)' }}>
                <div className="w-14 h-14 rounded-2xl flex items-center justify-center text-2xl font-black text-white flex-shrink-0"
                  style={{ background: `linear-gradient(135deg, ${kidColor(s.grade)}, ${kidColor(s.grade)}bb)` }}>
                  {s.name[0].toUpperCase()}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="font-black text-lg leading-tight" style={{ color: '#1A1A2E' }}>{s.name}</p>
                  <p className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>{ordinal(s.grade)}</p>
                  {s.school && <p className="text-xs font-semibold" style={{ color: '#B39DDB' }}>🏫 {s.school}</p>}
                  {!s.school && s.town && <p className="text-xs font-semibold" style={{ color: '#B39DDB' }}>📍 {s.town}</p>}
                  <div className="flex items-center gap-3 mt-1">
                    <span className="text-sm font-bold" style={{ color: '#FFD93D' }}>⭐ {s.stars_total}</span>
                    {s.streak > 0 && (
                      <span className="text-sm font-bold" style={{ color: '#FF6B6B' }}>🔥 {s.streak}</span>
                    )}
                  </div>
                </div>
                <button onClick={() => handleSelectKid(s)}
                  className="px-4 py-2 rounded-2xl text-sm font-black text-white flex-shrink-0 transition-all active:scale-95"
                  style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                  Учи →
                </button>
              </div>
            ))}
          </div>

          {/* Add kid form */}
          {showAdd && (
            <div className="mt-3 bg-white rounded-3xl p-6 space-y-4"
              style={{ boxShadow: '0 2px 20px rgba(92,53,212,0.12)', border: '2px solid #EDE9FF' }}>
              <h3 className="font-black text-lg" style={{ color: '#1A1A2E' }}>Ново дете</h3>

              <div>
                <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>
                  ИМЕ НА ДЕТЕТО
                </label>
                <input type="text" value={newName}
                  onChange={(e) => { setNewName(capitalizeWords(e.target.value)); setAddError('') }}
                  placeholder="Марко"
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold text-base outline-none"
                  style={{ borderColor: newName ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>

              <div>
                <label className="block text-xs font-black mb-2 tracking-widest" style={{ color: '#6B6B8A' }}>
                  ОДДЕЛЕНИЕ
                </label>
                <div className="grid grid-cols-5 gap-2">
                  {GRADES.map((g) => (
                    <button key={g} type="button" onClick={() => { setNewGrade(g); setAddError('') }}
                      className="py-3 rounded-2xl text-lg font-black border-2 transition-all duration-150"
                      style={{
                        background: newGrade === g ? '#5C35D4' : 'white',
                        color: newGrade === g ? '#FFD93D' : '#5C35D4',
                        borderColor: newGrade === g ? '#5C35D4' : '#E5E7EB',
                      }}>
                      {g}
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>
                  PIN (4 цифри)
                </label>
                <input type="password" inputMode="numeric" maxLength={4}
                  value={newPin} onChange={(e) => { setNewPin(e.target.value.replace(/\D/g, '')); setAddError('') }}
                  placeholder="1234"
                  className="w-full px-4 py-4 rounded-2xl border-2 font-black text-2xl text-center outline-none tracking-widest"
                  style={{ borderColor: newPin.length === 4 ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>

              <TownSchoolPicker
                town={newTown} school={newSchool}
                onTownChange={setNewTown} onSchoolChange={setNewSchool}
              />

              {addError && (
                <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                  <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {addError}</p>
                </div>
              )}

              <div className="flex gap-3">
                <button type="button" onClick={() => { setShowAdd(false); setNewName(''); setNewGrade(null); setNewPin(''); setAddError('') }}
                  className="flex-1 py-3 rounded-2xl text-base font-black border-2 transition-all active:scale-95"
                  style={{ borderColor: '#E5E7EB', color: '#6B6B8A', background: 'white' }}>
                  Откажи
                </button>
                <button type="button" onClick={handleAddKid} disabled={addLoading}
                  className="flex-1 py-3 rounded-2xl text-base font-black text-white transition-all active:scale-95 disabled:opacity-60"
                  style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                  {addLoading ? 'Зачувува...' : 'Зачувај ⭐'}
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Back to kid selector */}
        {students.length > 0 && (
          <button onClick={() => router.push('/')}
            className="w-full py-3 rounded-2xl text-sm font-bold text-center transition-all"
            style={{ color: '#6B6B8A' }}>
            ← Назад кон избор на дете
          </button>
        )}
      </div>
    </main>
  )
}
