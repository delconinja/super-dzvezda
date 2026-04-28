'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'
import {
  getMyAffiliate, getMyReferrals, getMyPayouts,
  estimatedMonthlyEur, Affiliate, AffiliatePayout,
} from '@/lib/affiliate'

const BASE_URL = 'https://super-dzvezda.mk'

export default function AffiliatePage() {
  const router = useRouter()
  const [affiliate, setAffiliate] = useState<Affiliate | null>(null)
  const [referrals, setReferrals] = useState<{ status: string; created_at: string }[]>([])
  const [payouts, setPayouts] = useState<AffiliatePayout[]>([])
  const [loading, setLoading] = useState(true)
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    const init = async () => {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) { router.push('/join'); return }
      const aff = await getMyAffiliate()
      if (!aff) { router.push('/join'); return }
      setAffiliate(aff)
      if (aff.status === 'active') {
        const [refs, pays] = await Promise.all([getMyReferrals(aff.id), getMyPayouts(aff.id)])
        setReferrals(refs)
        setPayouts(pays)
      }
      setLoading(false)
    }
    init()
  }, [router])

  const handleCopy = () => {
    if (!affiliate) return
    navigator.clipboard.writeText(`${BASE_URL}/?ref=${affiliate.code}`)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const handleLogout = async () => {
    await supabase.auth.signOut()
    router.push('/join')
  }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center"
      style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69, #5C35D4)' }}>
      <div className="text-6xl animate-float">⭐</div>
    </div>
  )

  if (!affiliate) return null

  const activeReferrals = referrals.filter(r => r.status === 'active' || r.status === 'trial').length
  const totalReferrals = referrals.length
  const estMonthly = estimatedMonthlyEur(activeReferrals)
  const totalPaid = payouts.filter(p => p.status === 'paid').reduce((s, p) => s + p.amount_eur, 0)
  const pendingPayout = payouts.filter(p => p.status === 'pending').reduce((s, p) => s + p.amount_eur, 0)

  // PENDING state
  if (affiliate.status === 'pending') return (
    <main className="min-h-screen flex items-center justify-center px-4"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>
      <div className="bg-white rounded-3xl p-8 max-w-md w-full text-center">
        <div className="text-6xl mb-4">⏳</div>
        <h1 className="text-2xl font-black mb-3" style={{ color: '#1A1A2E' }}>Пријавата е во разгледување</h1>
        <p className="font-semibold mb-2" style={{ color: '#6B6B8A' }}>
          Здраво, {affiliate.name.split(' ')[0]}! Ти благодариме за пријавата.
        </p>
        <p className="text-sm mb-6" style={{ color: '#9B9BAA' }}>
          Ќе ја разгледаме во рок од 24 часа и ќе добиеш е-пошта со потврда.
        </p>
        <div className="rounded-2xl p-4 mb-6" style={{ background: '#F7F5FF' }}>
          <p className="text-xs font-black tracking-widest mb-1" style={{ color: '#5C35D4' }}>ТВОЈОТ КОД</p>
          <p className="text-xl font-black" style={{ color: '#1A1A2E' }}>{affiliate.code}</p>
        </div>
        <button onClick={handleLogout}
          className="text-sm font-bold" style={{ color: '#9B9BAA' }}>
          Излези
        </button>
      </div>
    </main>
  )

  // SUSPENDED state
  if (affiliate.status === 'suspended') return (
    <main className="min-h-screen flex items-center justify-center px-4"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>
      <div className="bg-white rounded-3xl p-8 max-w-md w-full text-center">
        <div className="text-6xl mb-4">🚫</div>
        <h1 className="text-2xl font-black mb-3" style={{ color: '#1A1A2E' }}>Профилот е суспендиран</h1>
        <p className="text-sm mb-6" style={{ color: '#9B9BAA' }}>
          Контактирај нè на info@super-dzvezda.mk за повеќе информации.
        </p>
        <button onClick={handleLogout} className="text-sm font-bold" style={{ color: '#9B9BAA' }}>Излези</button>
      </div>
    </main>
  )

  // ACTIVE state
  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center justify-between"
        style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)' }}>
        <div className="flex items-center gap-3">
          <span className="text-3xl">⭐</span>
          <div>
            <span className="text-white font-black">Супер Ѕвезда</span>
            <span className="ml-2 text-xs px-2 py-0.5 rounded-full font-black"
              style={{ background: '#6BCB77', color: 'white' }}>ПАРТНЕР</span>
          </div>
        </div>
        <button onClick={handleLogout}
          className="text-white/50 hover:text-white/80 text-sm font-bold transition-colors">
          Излези
        </button>
      </header>

      <div className="max-w-2xl mx-auto px-6 py-8 space-y-6">

        {/* Greeting */}
        <div>
          <p className="text-sm font-bold mb-1" style={{ color: '#6B6B8A' }}>ПАРТНЕРСКИ ПРОФИЛ</p>
          <h1 className="text-3xl font-black" style={{ color: '#1A1A2E' }}>
            Здраво, {affiliate.name.split(' ')[0]}! 👋
          </h1>
        </div>

        {/* Your link */}
        <div className="bg-white rounded-3xl p-5"
          style={{ boxShadow: '0 0 0 2px #5C35D4' }}>
          <p className="text-xs font-black tracking-widest mb-2" style={{ color: '#5C35D4' }}>ТВОЈОТ ЛИНК</p>
          <div className="flex items-center gap-3">
            <p className="flex-1 font-black text-sm break-all" style={{ color: '#1A1A2E' }}>
              {BASE_URL}/?ref={affiliate.code}
            </p>
            <button onClick={handleCopy}
              className="px-4 py-2.5 rounded-2xl font-black text-sm text-white flex-shrink-0 transition-all active:scale-95"
              style={{ background: copied ? '#6BCB77' : 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              {copied ? '✅ Копирано' : '📋 Копирај'}
            </button>
          </div>
        </div>

        {/* Stats grid */}
        <div className="grid grid-cols-2 gap-3">
          {[
            { label: 'Вкупно реферирани', value: totalReferrals, icon: '👥', color: '#5C35D4' },
            { label: 'Активни претплати', value: activeReferrals, icon: '✅', color: '#6BCB77' },
            { label: 'Проц. месечно', value: `€${estMonthly.toFixed(2)}`, icon: '💰', color: '#FFD93D' },
            { label: 'Вкупно исплатено', value: `€${totalPaid.toFixed(2)}`, icon: '🏦', color: '#FF6B6B' },
          ].map((s) => (
            <div key={s.label} className="bg-white rounded-3xl p-5"
              style={{ boxShadow: '0 2px 12px rgba(92,53,212,0.08)' }}>
              <div className="text-2xl mb-1">{s.icon}</div>
              <div className="text-2xl font-black" style={{ color: s.color }}>{s.value}</div>
              <div className="text-xs font-semibold mt-0.5" style={{ color: '#9B9BAA' }}>{s.label}</div>
            </div>
          ))}
        </div>

        {pendingPayout > 0 && (
          <div className="rounded-2xl p-4" style={{ background: '#FFF8E1', border: '1.5px solid #FFD93D' }}>
            <p className="font-black text-sm" style={{ color: '#1A1A2E' }}>
              💰 Чека исплата: <span style={{ color: '#FF9A3C' }}>€{pendingPayout.toFixed(2)}</span>
            </p>
            <p className="text-xs mt-0.5 font-semibold" style={{ color: '#9B9BAA' }}>
              Исплатите се обработуваат до 5-ти во месецот.
            </p>
          </div>
        )}

        {/* Marketing messages */}
        <div className="bg-white rounded-3xl p-5" style={{ boxShadow: '0 2px 12px rgba(92,53,212,0.08)' }}>
          <p className="text-xs font-black tracking-widest mb-3" style={{ color: '#5C35D4' }}>МАРКЕТИНГ ПОРАКИ</p>
          <div className="space-y-3">
            {[
              `🎓 Дали вашето дете учи во 5-9 одделение? Пробајте Супер Ѕвезда — македонска учебна платформа. 14 дена бесплатно! ${BASE_URL}/?ref=${affiliate.code}`,
              `⭐ Математика, Биологија, Хемија — со вежби и ѕвезди! Идеално за деца 5-9 одд. Пробај бесплатно: ${BASE_URL}/?ref=${affiliate.code}`,
              `💡 Постои апликација за македонски учебен план! Супер Ѕвезда — учи со игри, заработи ѕвезди, напредувај. ${BASE_URL}/?ref=${affiliate.code}`,
            ].map((msg, i) => (
              <div key={i} className="rounded-2xl p-3 text-sm font-semibold"
                style={{ background: '#F7F5FF', color: '#3A3A5C' }}>
                <p className="mb-2 leading-relaxed">{msg}</p>
                <button
                  onClick={() => { navigator.clipboard.writeText(msg) }}
                  className="text-xs font-black px-3 py-1 rounded-xl"
                  style={{ background: '#EDE9FF', color: '#5C35D4' }}>
                  📋 Копирај
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Payouts history */}
        {payouts.length > 0 && (
          <div className="bg-white rounded-3xl p-5" style={{ boxShadow: '0 2px 12px rgba(92,53,212,0.08)' }}>
            <p className="text-xs font-black tracking-widest mb-3" style={{ color: '#5C35D4' }}>ИСПЛАТИ</p>
            <div className="space-y-2">
              {payouts.map((p) => (
                <div key={p.id} className="flex items-center justify-between py-2 border-b last:border-0"
                  style={{ borderColor: '#F3F0FF' }}>
                  <div>
                    <p className="font-bold text-sm" style={{ color: '#1A1A2E' }}>{p.period_label}</p>
                    {p.note && <p className="text-xs" style={{ color: '#9B9BAA' }}>{p.note}</p>}
                  </div>
                  <div className="text-right">
                    <p className="font-black text-sm" style={{ color: '#1A1A2E' }}>€{p.amount_eur.toFixed(2)}</p>
                    <p className="text-xs font-semibold" style={{ color: p.status === 'paid' ? '#6BCB77' : '#FFD93D' }}>
                      {p.status === 'paid' ? '✅ Исплатено' : '⏳ Чека'}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Payout info */}
        {affiliate.payout_info && (
          <div className="rounded-2xl p-4" style={{ background: 'rgba(0,0,0,0.03)' }}>
            <p className="text-xs font-black tracking-widest mb-1" style={{ color: '#9B9BAA' }}>БАНКАРСКА СМЕТКА</p>
            <p className="text-sm font-semibold" style={{ color: '#3A3A5C' }}>{affiliate.payout_info}</p>
          </div>
        )}
      </div>
    </main>
  )
}
