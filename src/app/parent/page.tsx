'use client'

export const dynamic = 'force-dynamic'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'
import {
  getStudents, getSubscription, addStudent, parentLogout,
  setActiveStudent, trialDaysLeft, isTrialExpired,
  familyMonthlyMkd, familyAnnualMkd, isDevAdminUser,
  pauseSubscription, cancelSubscription,
  StudentProfile, Subscription,
} from '@/lib/auth'
import TownSchoolPicker from '@/components/TownSchoolPicker'
import { getBadgeDef, TIER_COLORS } from '@/lib/badges'

const GRADES = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const

const MK_MONTHS = ['Јануари','Февруари','Март','Април','Мај','Јуни',
  'Јули','Август','Септември','Октомври','Ноември','Декември']

interface InvoiceRecord {
  id: string
  periodLabel: string
  issuedAt: Date
  amountEur: number
  amountMkd: number
  description: string
}

function generateInvoices(sub: Subscription): InvoiceRecord[] {
  if (sub.status === 'trial' || !sub.subscribed_until || !sub.price_paid) return []

  const start = new Date(sub.trial_ends_at)
  const end   = new Date(sub.subscribed_until)
  const kids  = sub.max_students || 1
  const eur   = sub.price_paid
  const invoices: InvoiceRecord[] = []

  if (sub.billing === 'annual') {
    invoices.push({
      id: `${start.getFullYear()}-G-001`,
      periodLabel: String(start.getFullYear()),
      issuedAt: start,
      amountEur: eur,
      amountMkd: familyAnnualMkd(kids),
      description: `Годишна претплата · ${kids} ${kids === 1 ? 'дете' : 'деца'}`,
    })
  } else {
    let cursor = new Date(start)
    let idx = 1
    while (cursor < end) {
      const y = cursor.getFullYear()
      const m = cursor.getMonth()
      invoices.push({
        id: `${y}-M-${String(idx).padStart(3, '0')}`,
        periodLabel: `${MK_MONTHS[m]} ${y}`,
        issuedAt: new Date(cursor),
        amountEur: eur,
        amountMkd: familyMonthlyMkd(kids),
        description: `Месечна претплата · ${kids} ${kids === 1 ? 'дете' : 'деца'}`,
      })
      cursor.setMonth(cursor.getMonth() + 1)
      idx++
    }
  }

  return invoices.reverse()
}

const GRADE_COLORS = ['#FFD93D', '#FF9A3C', '#FF6B6B', '#6BCB77', '#7B5CE5', '#FF6B9D', '#4ECDC4', '#45B7D1', '#96CEB4']

function kidColor(grade: number) {
  return GRADE_COLORS[(grade - 1) % GRADE_COLORS.length]
}

function gradeOrdSuffix(g: number) {
  if (g === 1) return 'во'
  if (g === 2) return 'ро'
  if (g === 7 || g === 8) return 'мо'
  return 'то'
}

function ordinal(g: number) {
  return `${g}-${gradeOrdSuffix(g)} одд.`
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
  const [parentId, setParentId] = useState<string | null>(null)

  const [isAdmin, setIsAdmin] = useState(false)
  const [showManage, setShowManage] = useState(false)
  const [cancelStep, setCancelStep] = useState<'idle' | 'confirm'>('idle')
  const [manageLoading, setManageLoading] = useState(false)
  const [manageError, setManageError] = useState('')
  const [showAdd, setShowAdd] = useState(false)
  const [newName, setNewName] = useState('')
  const [newGrade, setNewGrade] = useState<number | null>(null)
  const [newPin, setNewPin] = useState('')
  const [newTown, setNewTown] = useState('')
  const [newSchool, setNewSchool] = useState('')
  const [addError, setAddError] = useState('')
  const [addLoading, setAddLoading] = useState(false)
  const [latestBadges, setLatestBadges] = useState<Record<string, { badge_id: string; earned_at: string }>>({})


  useEffect(() => {
    const init = async () => {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) { router.push('/'); return }
      setParentName(user.user_metadata?.full_name || user.email || 'Родитело')
      setParentId(user.id)
      const [studs, subscription, adminFlag] = await Promise.all([getStudents(), getSubscription(), isDevAdminUser()])
      setStudents(studs)
      setSub(subscription)
      setIsAdmin(adminFlag)
      setLoading(false)

      // Fetch latest badge per student (non-blocking)
      if (studs.length > 0) {
        Promise.all(
          studs.map(s =>
            fetch(`/api/badges?studentId=${s.id}`)
              .then(r => r.json())
              .then((data: { badge_id: string; earned_at: string }[]) =>
                data.length > 0 ? { id: s.id, badge: data[0] } : null
              )
              .catch(() => null)
          )
        ).then(results => {
          const map: Record<string, { badge_id: string; earned_at: string }> = {}
          results.forEach(r => { if (r) map[r.id] = r.badge })
          setLatestBadges(map)
        })
      }
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

  const handlePause = async () => {
    setManageLoading(true); setManageError('')
    const result = await pauseSubscription()
    setManageLoading(false)
    if (!result.ok) return setManageError(result.error!)
    setSub(prev => prev ? { ...prev, status: 'paused' } : prev)
    setShowManage(false)
  }

  const handleCancel = async () => {
    setManageLoading(true); setManageError('')
    const result = await cancelSubscription()
    setManageLoading(false)
    if (!result.ok) return setManageError(result.error!)
    setSub(prev => prev ? { ...prev, status: 'cancelled' } : prev)
    setCancelStep('idle'); setShowManage(false)
  }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center"
      style={{ background: '#F8F5FF' }}>
      <div className="text-6xl animate-float">⭐</div>
    </div>
  )

  const daysLeft = sub ? trialDaysLeft(sub) : 0
  const expired = sub ? isTrialExpired(sub) : false
  // Admins without a real subscription see a mock active card so all UI is visible
  const effectiveSub: Subscription | null = sub ?? (isAdmin ? {
    status: 'active', plan: 'individual', price_paid: 10, max_students: 1,
    billing: 'monthly', trial_ends_at: new Date().toISOString(),
    subscribed_until: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString(),
  } : null)
  const trialColor = effectiveSub?.status === 'active' ? '#6BCB77'
    : expired ? '#FF6B6B' : daysLeft <= 3 ? '#FF6B6B' : daysLeft <= 7 ? '#FFD93D' : '#6BCB77'
  const canAdd = students.length < 3

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>

      {/* Header */}
      <header className="px-6 py-4 flex items-center justify-between"
        style={{ background: 'linear-gradient(135deg, #8B6FE8, #A889F0)' }}>
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
        {effectiveSub && (
          <div className="rounded-3xl overflow-hidden"
            style={{ border: `2px solid ${trialColor}55` }}>
            <div className="p-5 flex items-center justify-between"
              style={{ background: `${trialColor}18` }}>
              <div>
                {isAdmin && !sub && (
                  <p className="text-xs font-black tracking-widest mb-1" style={{ color: '#9B9BAA' }}>
                    АДМИН ПРЕГЛЕД
                  </p>
                )}
                <p className="text-xs font-black tracking-widest mb-1" style={{ color: trialColor }}>
                  {effectiveSub.status === 'active' ? 'АКТИВНА ПРЕТПЛАТА'
                    : effectiveSub.status === 'paused' ? 'ПАУЗИРАНА ПРЕТПЛАТА'
                    : expired ? 'ПРОБЕН ПЕРИОД — ИСТЕЧЕН'
                    : 'ПРОБЕН ПЕРИОД'}
                </p>
                <p className="text-2xl font-black" style={{ color: '#1A1A2E' }}>
                  {effectiveSub.status === 'active' ? 'Активна'
                    : effectiveSub.status === 'paused' ? 'Паузирана'
                    : expired ? 'Истечен'
                    : `${daysLeft} ${daysLeft === 1 ? 'ден' : 'дена'} останати`}
                </p>
              </div>
              <div className="flex flex-col items-end gap-2">
                {(effectiveSub.status === 'trial' || expired) && (
                  <button onClick={() => router.push('/trial-expired')}
                    className="px-5 py-3 rounded-2xl text-sm font-black text-white transition-all active:scale-95"
                    style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                    Надгради ↗
                  </button>
                )}
                {effectiveSub.status === 'active' && (
                  <button onClick={() => { setShowManage(v => !v); setCancelStep('idle'); setManageError('') }}
                    className="text-xs font-black transition-colors"
                    style={{ color: trialColor }}>
                    Управување со претплата {showManage ? '▲' : '▼'}
                  </button>
                )}
              </div>
            </div>

            {showManage && effectiveSub.status === 'active' && (
              <div className="p-4 space-y-3 bg-white">

                {/* Invoices */}
                {(() => {
                  const invoices = sub ? generateInvoices(sub) : []
                  return (
                    <div>
                      <p className="text-xs font-black tracking-widest mb-2" style={{ color: '#9B9BAA' }}>🧾 ФАКТУРИ</p>
                      {invoices.length === 0 ? (
                        <p className="text-sm font-semibold text-center py-3 rounded-2xl" style={{ background: '#F7F5FF', color: '#9B9BAA' }}>
                          Уште нема фактури.
                        </p>
                      ) : (
                        <div className="space-y-2">
                          {invoices.map(inv => (
                            <div key={inv.id} className="flex items-center justify-between px-4 py-3 rounded-2xl"
                              style={{ background: '#F7F5FF' }}>
                              <div className="min-w-0">
                                <p className="font-black text-sm leading-tight" style={{ color: '#1A1A2E' }}>{inv.periodLabel}</p>
                                <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>{inv.description}</p>
                              </div>
                              <div className="text-right flex-shrink-0 ml-3">
                                <p className="font-black text-sm" style={{ color: '#5C35D4' }}>€{inv.amountEur}</p>
                                <span className="text-xs font-black px-2 py-0.5 rounded-full" style={{ background: '#E8F8EA', color: '#2E7D32' }}>✓ Платено</span>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )
                })()}

                <div className="h-px" style={{ background: '#E8E8F0' }} />

                {cancelStep !== 'confirm' && (
                  <button onClick={handlePause} disabled={manageLoading}
                    className="w-full flex items-center gap-3 p-3 rounded-2xl border-2 text-left transition-all active:scale-[0.99] disabled:opacity-60"
                    style={{ borderColor: '#E5E7EB' }}>
                    <span className="text-xl">🔄</span>
                    <div>
                      <p className="font-black text-sm" style={{ color: '#1A1A2E' }}>Паузирај претплата</p>
                      <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>Претплатата ќе биде паузирана до наредниот период</p>
                    </div>
                  </button>
                )}

                {cancelStep === 'idle' ? (
                  <button onClick={() => setCancelStep('confirm')}
                    className="w-full flex items-center gap-3 p-3 rounded-2xl border-2 text-left transition-all active:scale-[0.99]"
                    style={{ borderColor: '#FFD0D0' }}>
                    <span className="text-xl">❌</span>
                    <div>
                      <p className="font-black text-sm" style={{ color: '#E53935' }}>Откажи претплата</p>
                      <p className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>Пристапот продолжува до крај на тековниот период</p>
                    </div>
                  </button>
                ) : (
                  <div className="rounded-2xl p-4" style={{ background: '#FFF0F0', border: '2px solid #FFCDD2' }}>
                    <p className="font-black text-sm mb-1" style={{ color: '#C62828' }}>Дали си сигурен?</p>
                    <p className="text-xs font-semibold mb-3" style={{ color: '#6B6B8A' }}>
                      Претплатата ќе заврши на{' '}
                      {effectiveSub.subscribed_until
                        ? new Date(effectiveSub.subscribed_until).toLocaleDateString('mk-MK')
                        : 'крај на периодот'}.
                      До тогаш имаш целосен пристап.
                    </p>
                    <div className="flex gap-2">
                      <button onClick={() => setCancelStep('idle')}
                        className="flex-1 py-2.5 rounded-xl font-black text-sm border-2 transition-all active:scale-95"
                        style={{ borderColor: '#E5E7EB', color: '#6B6B8A', background: 'white' }}>
                        Назад
                      </button>
                      <button onClick={handleCancel} disabled={manageLoading}
                        className="flex-1 py-2.5 rounded-xl font-black text-sm text-white transition-all active:scale-95 disabled:opacity-60"
                        style={{ background: '#E53935' }}>
                        {manageLoading ? 'Се откажува...' : 'Да, откажи'}
                      </button>
                    </div>
                  </div>
                )}

                {manageError && (
                  <p className="text-xs font-bold text-center pt-1" style={{ color: '#E53935' }}>{manageError}</p>
                )}
              </div>
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
                  {latestBadges[s.id] && (() => {
                    const def = getBadgeDef(latestBadges[s.id].badge_id)
                    if (!def) return null
                    const tier = TIER_COLORS[def.tier]
                    return (
                      <div className="flex items-center gap-1.5 mt-1.5 px-2 py-1 rounded-xl w-fit"
                        style={{ background: tier.bg, border: `1.5px solid ${tier.border}` }}>
                        <span style={{ fontSize: '0.9rem' }}>{def.emoji}</span>
                        <span className="text-xs font-black" style={{ color: tier.label }}>{def.nameMk}</span>
                      </div>
                    )
                  })()}
                </div>
                <div className="flex items-center gap-2 flex-shrink-0">
                  <button onClick={() => router.push(`/parent/progress/${s.id}`)}
                    className="px-4 py-2 rounded-2xl text-sm font-black text-white transition-all active:scale-95"
                    style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                    Напредок →
                  </button>
                  <button onClick={() => handleSelectKid(s)}
                    className="px-3 py-2 rounded-2xl text-sm font-semibold border-2 transition-all active:scale-95"
                    style={{ borderColor: '#5C35D4', color: '#5C35D4', background: 'white' }}>
                    Учи
                  </button>
                </div>
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
