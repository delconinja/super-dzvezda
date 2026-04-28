'use client'

export const dynamic = 'force-dynamic'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { supabase } from '@/lib/supabase'
import {
  adminGetAffiliates, adminSetAffiliateStatus, adminGetSubscriptions,
  adminGetPayouts, adminCreatePayout, adminMarkPaid,
  estimatedMonthlyEur, Affiliate, AffiliatePayout,
} from '@/lib/affiliate'

const ADMIN_EMAIL = 'delco.k.de@gmail.com'

type Tab = 'affiliates' | 'subscriptions' | 'payouts'

type AffiliateRow = Affiliate & { referral_count: number }
type SubRow = { id: string; status: string; created_at: string; affiliate_id: string | null; affiliates: { name: string; code: string } | null }
type PayoutRow = AffiliatePayout & { affiliates: { name: string; code: string } }

export default function AdminPage() {
  const router = useRouter()
  const [tab, setTab] = useState<Tab>('affiliates')
  const [loading, setLoading] = useState(true)

  const [affiliates, setAffiliates] = useState<AffiliateRow[]>([])
  const [subscriptions, setSubscriptions] = useState<SubRow[]>([])
  const [payouts, setPayouts] = useState<PayoutRow[]>([])

  // Create payout modal
  const [payoutModal, setPayoutModal] = useState<AffiliateRow | null>(null)
  const [payoutEur, setPayoutEur] = useState('')
  const [payoutPeriod, setPayoutPeriod] = useState('')
  const [payoutNote, setPayoutNote] = useState('')
  const [payoutLoading, setPayoutLoading] = useState(false)
  const [payoutError, setPayoutError] = useState('')

  useEffect(() => {
    const init = async () => {
      const { data: { user } } = await supabase.auth.getUser()
      if (!user || user.email !== ADMIN_EMAIL) { router.push('/'); return }
      const [affs, subs, pays] = await Promise.all([
        adminGetAffiliates(),
        adminGetSubscriptions(),
        adminGetPayouts(),
      ])
      setAffiliates(affs as AffiliateRow[])
      setSubscriptions(subs as SubRow[])
      setPayouts(pays as PayoutRow[])
      setLoading(false)
    }
    init()
  }, [router])

  const handleStatus = async (affiliateId: string, status: 'active' | 'suspended' | 'pending') => {
    await adminSetAffiliateStatus(affiliateId, status)
    setAffiliates((prev) => prev.map(a => a.id === affiliateId ? { ...a, status } : a))
  }

  const handleCreatePayout = async () => {
    if (!payoutModal) return
    setPayoutError('')
    const eur = parseFloat(payoutEur)
    if (!eur || eur <= 0) return setPayoutError('Внеси валиден износ.')
    if (!payoutPeriod.trim()) return setPayoutError('Внеси период (пр. Мај 2026).')
    setPayoutLoading(true)
    const result = await adminCreatePayout({
      affiliateId: payoutModal.id,
      amountEur: eur,
      amountMkd: Math.round(eur * 61.5),
      periodLabel: payoutPeriod.trim(),
      note: payoutNote.trim() || undefined,
    })
    setPayoutLoading(false)
    if (!result.ok) return setPayoutError(result.error!)
    const updated = await adminGetPayouts()
    setPayouts(updated as PayoutRow[])
    setPayoutModal(null); setPayoutEur(''); setPayoutPeriod(''); setPayoutNote('')
  }

  const handleMarkPaid = async (payoutId: string) => {
    await adminMarkPaid(payoutId)
    setPayouts(prev => prev.map(p => p.id === payoutId ? { ...p, status: 'paid', paid_at: new Date().toISOString() } : p))
  }

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: '#F7F5FF' }}>
      <div className="text-5xl animate-float">⭐</div>
    </div>
  )

  const pendingAffiliates = affiliates.filter(a => a.status === 'pending').length
  const totalActiveSubs = subscriptions.filter(s => s.status === 'active' || s.status === 'trial').length
  const totalReferredSubs = subscriptions.filter(s => s.affiliate_id).length
  const pendingPayoutTotal = payouts.filter(p => p.status === 'pending').reduce((s, p) => s + p.amount_eur, 0)

  return (
    <main className="min-h-screen" style={{ background: '#F7F5FF' }}>
      <header className="px-6 py-4 flex items-center justify-between"
        style={{ background: 'linear-gradient(135deg, #1A1A2E, #2D1B69)' }}>
        <div className="flex items-center gap-3">
          <span className="text-3xl">⭐</span>
          <div>
            <span className="text-white font-black">Супер Ѕвезда</span>
            <span className="ml-2 text-xs px-2 py-0.5 rounded-full font-black"
              style={{ background: '#FF6B6B', color: 'white' }}>ADMIN</span>
          </div>
        </div>
        <button onClick={() => { supabase.auth.signOut(); router.push('/') }}
          className="text-white/50 hover:text-white/80 text-sm font-bold">Излези</button>
      </header>

      <div className="max-w-4xl mx-auto px-6 py-8 space-y-6">

        {/* KPI strip */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {[
            { label: 'Чекаат одобрување', value: pendingAffiliates, color: '#FFD93D', icon: '⏳' },
            { label: 'Вкупно претплати', value: totalActiveSubs, color: '#6BCB77', icon: '✅' },
            { label: 'Реферирани', value: totalReferredSubs, color: '#5C35D4', icon: '🔗' },
            { label: 'Чека исплата', value: `€${pendingPayoutTotal.toFixed(0)}`, color: '#FF6B6B', icon: '💰' },
          ].map((k) => (
            <div key={k.label} className="bg-white rounded-2xl p-4 text-center"
              style={{ boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
              <div className="text-xl mb-0.5">{k.icon}</div>
              <div className="text-2xl font-black" style={{ color: k.color }}>{k.value}</div>
              <div className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>{k.label}</div>
            </div>
          ))}
        </div>

        {/* Tabs */}
        <div className="flex gap-1 p-1 rounded-2xl bg-white" style={{ boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          {([
            { key: 'affiliates', label: `Партнери (${affiliates.length})` },
            { key: 'subscriptions', label: `Претплати (${subscriptions.length})` },
            { key: 'payouts', label: `Исплати (${payouts.length})` },
          ] as { key: Tab; label: string }[]).map((t) => (
            <button key={t.key} onClick={() => setTab(t.key)}
              className="flex-1 py-2.5 rounded-xl font-black text-sm transition-all"
              style={{
                background: tab === t.key ? '#5C35D4' : 'transparent',
                color: tab === t.key ? 'white' : '#6B6B8A',
              }}>
              {t.label}
            </button>
          ))}
        </div>

        {/* AFFILIATES TAB */}
        {tab === 'affiliates' && (
          <div className="space-y-3">
            {affiliates.length === 0 && (
              <div className="bg-white rounded-3xl p-8 text-center">
                <p className="font-bold" style={{ color: '#9B9BAA' }}>Нема партнери уште.</p>
              </div>
            )}
            {affiliates.map((a) => (
              <div key={a.id} className="bg-white rounded-3xl p-5"
                style={{ boxShadow: '0 2px 12px rgba(0,0,0,0.06)', border: a.status === 'pending' ? '2px solid #FFD93D' : '2px solid transparent' }}>
                <div className="flex flex-wrap items-start gap-4">
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 flex-wrap">
                      <p className="font-black text-lg" style={{ color: '#1A1A2E' }}>{a.name}</p>
                      <span className="text-xs px-2 py-0.5 rounded-full font-black"
                        style={{
                          background: a.status === 'active' ? '#E8F8EA' : a.status === 'pending' ? '#FFF8E1' : '#FFE8E8',
                          color: a.status === 'active' ? '#2D7A35' : a.status === 'pending' ? '#B8860B' : '#C0392B',
                        }}>
                        {a.status === 'active' ? '✅ Активен' : a.status === 'pending' ? '⏳ Чека' : '🚫 Суспендиран'}
                      </span>
                    </div>
                    <p className="text-sm font-bold mt-0.5" style={{ color: '#5C35D4' }}>/?ref={a.code}</p>
                    {a.channel && <p className="text-xs mt-0.5" style={{ color: '#9B9BAA' }}>{a.channel}</p>}
                    <div className="flex gap-4 mt-2">
                      <span className="text-sm font-bold" style={{ color: '#1A1A2E' }}>👥 {a.referral_count} реф.</span>
                      <span className="text-sm font-bold" style={{ color: '#6BCB77' }}>
                        💰 ~€{estimatedMonthlyEur(a.referral_count).toFixed(0)}/мес
                      </span>
                    </div>
                    {a.payout_info && (
                      <p className="text-xs mt-1" style={{ color: '#9B9BAA' }}>🏦 {a.payout_info}</p>
                    )}
                  </div>
                  <div className="flex flex-col gap-2">
                    {a.status !== 'active' && (
                      <button onClick={() => handleStatus(a.id, 'active')}
                        className="px-4 py-2 rounded-xl text-sm font-black text-white transition-all active:scale-95"
                        style={{ background: '#6BCB77' }}>
                        ✅ Одобри
                      </button>
                    )}
                    {a.status !== 'suspended' && (
                      <button onClick={() => handleStatus(a.id, 'suspended')}
                        className="px-4 py-2 rounded-xl text-sm font-black transition-all active:scale-95"
                        style={{ background: '#FFE8E8', color: '#C0392B' }}>
                        🚫 Суспендирај
                      </button>
                    )}
                    {a.status === 'active' && (
                      <button onClick={() => setPayoutModal(a)}
                        className="px-4 py-2 rounded-xl text-sm font-black transition-all active:scale-95"
                        style={{ background: '#EDE9FF', color: '#5C35D4' }}>
                        💰 Исплати
                      </button>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* SUBSCRIPTIONS TAB */}
        {tab === 'subscriptions' && (
          <div className="bg-white rounded-3xl overflow-hidden" style={{ boxShadow: '0 2px 12px rgba(0,0,0,0.06)' }}>
            {subscriptions.length === 0 ? (
              <div className="p-8 text-center">
                <p className="font-bold" style={{ color: '#9B9BAA' }}>Нема претплати уште.</p>
              </div>
            ) : (
              <div className="divide-y" style={{ borderColor: '#F3F0FF' }}>
                {subscriptions.map((s) => (
                  <div key={s.id} className="px-5 py-4 flex items-center justify-between">
                    <div>
                      <span className="text-xs px-2 py-0.5 rounded-full font-black"
                        style={{
                          background: s.status === 'active' ? '#E8F8EA' : s.status === 'trial' ? '#EDE9FF' : '#FFE8E8',
                          color: s.status === 'active' ? '#2D7A35' : s.status === 'trial' ? '#5C35D4' : '#C0392B',
                        }}>
                        {s.status}
                      </span>
                      <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>
                        {new Date(s.created_at).toLocaleDateString('mk-MK')}
                      </p>
                    </div>
                    <div className="text-right">
                      {s.affiliates ? (
                        <p className="text-sm font-black" style={{ color: '#5C35D4' }}>
                          🔗 {s.affiliates.name} (/{s.affiliates.code})
                        </p>
                      ) : (
                        <p className="text-sm font-semibold" style={{ color: '#D1D5DB' }}>Органски</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* PAYOUTS TAB */}
        {tab === 'payouts' && (
          <div className="space-y-3">
            {payouts.length === 0 && (
              <div className="bg-white rounded-3xl p-8 text-center">
                <p className="font-bold" style={{ color: '#9B9BAA' }}>Нема исплати уште.</p>
              </div>
            )}
            {payouts.map((p) => (
              <div key={p.id} className="bg-white rounded-3xl p-5 flex items-center justify-between"
                style={{ boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
                <div>
                  <p className="font-black" style={{ color: '#1A1A2E' }}>{p.affiliates?.name}</p>
                  <p className="text-sm font-semibold" style={{ color: '#6B6B8A' }}>{p.period_label}</p>
                  {p.note && <p className="text-xs" style={{ color: '#9B9BAA' }}>{p.note}</p>}
                </div>
                <div className="text-right flex flex-col items-end gap-2">
                  <p className="text-xl font-black" style={{ color: '#1A1A2E' }}>€{p.amount_eur.toFixed(2)}</p>
                  <p className="text-xs" style={{ color: '#9B9BAA' }}>{p.amount_mkd} ден</p>
                  {p.status === 'pending' ? (
                    <button onClick={() => handleMarkPaid(p.id)}
                      className="px-3 py-1.5 rounded-xl text-xs font-black text-white transition-all active:scale-95"
                      style={{ background: '#6BCB77' }}>
                      ✅ Означи како платено
                    </button>
                  ) : (
                    <span className="text-xs font-black px-2 py-1 rounded-xl"
                      style={{ background: '#E8F8EA', color: '#2D7A35' }}>
                      ✅ Исплатено {p.paid_at ? new Date(p.paid_at).toLocaleDateString('mk-MK') : ''}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Create payout modal */}
      {payoutModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: 'rgba(0,0,0,0.5)' }}>
          <div className="bg-white rounded-3xl p-6 w-full max-w-sm space-y-4">
            <h2 className="font-black text-lg" style={{ color: '#1A1A2E' }}>
              Исплати на {payoutModal.name}
            </h2>
            {[
              { label: 'ИЗНОС (€)', val: payoutEur, set: setPayoutEur, ph: '30.00', type: 'number' },
              { label: 'ПЕРИОД', val: payoutPeriod, set: setPayoutPeriod, ph: 'Мај 2026', type: 'text' },
              { label: 'НАПОМЕНА (опционално)', val: payoutNote, set: setPayoutNote, ph: 'Банкарски трансфер', type: 'text' },
            ].map(({ label, val, set, ph, type }) => (
              <div key={label}>
                <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>{label}</label>
                <input type={type} value={val} onChange={(e) => { set(e.target.value); setPayoutError('') }}
                  placeholder={ph}
                  className="w-full px-4 py-3 rounded-2xl border-2 font-semibold outline-none"
                  style={{ borderColor: val ? '#5C35D4' : '#E5E7EB', color: '#1A1A2E', background: '#FAFAFA' }} />
              </div>
            ))}
            {payoutEur && (
              <p className="text-sm font-bold" style={{ color: '#6B6B8A' }}>
                = {Math.round(parseFloat(payoutEur || '0') * 61.5)} ден
              </p>
            )}
            {payoutError && (
              <div className="rounded-2xl px-4 py-3" style={{ background: '#FFE8E8' }}>
                <p className="text-sm font-bold" style={{ color: '#C0392B' }}>⚠️ {payoutError}</p>
              </div>
            )}
            <div className="flex gap-3">
              <button onClick={() => { setPayoutModal(null); setPayoutError('') }}
                className="flex-1 py-3 rounded-2xl font-black border-2 transition-all active:scale-95"
                style={{ borderColor: '#E5E7EB', color: '#6B6B8A' }}>
                Откажи
              </button>
              <button onClick={handleCreatePayout} disabled={payoutLoading}
                className="flex-1 py-3 rounded-2xl font-black text-white disabled:opacity-60 transition-all active:scale-95"
                style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
                {payoutLoading ? '...' : 'Зачувај'}
              </button>
            </div>
          </div>
        </div>
      )}
    </main>
  )
}
