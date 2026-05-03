import { supabase } from './supabase'

export interface Affiliate {
  id: string
  user_id: string
  name: string
  code: string
  channel: string | null
  payout_info: string | null
  status: 'pending' | 'active' | 'suspended'
  created_at: string
}

export interface AffiliatePayout {
  id: string
  affiliate_id: string
  amount_eur: number
  amount_mkd: number
  period_label: string
  status: 'pending' | 'paid'
  paid_at: string | null
  note: string | null
  created_at: string
}

// ── REF TRACKING ─────────────────────────────────────────────────
export function saveAffiliateRef(code: string) {
  if (typeof window === 'undefined') return
  if (!localStorage.getItem('affiliate_ref')) {
    localStorage.setItem('affiliate_ref', code)
  }
}

export function getAffiliateRef(): string | null {
  if (typeof window === 'undefined') return null
  return localStorage.getItem('affiliate_ref')
}

export function clearAffiliateRef() {
  if (typeof window !== 'undefined') localStorage.removeItem('affiliate_ref')
}

// ── SIGNUP ────────────────────────────────────────────────────────
export async function joinAffiliate(data: {
  name: string
  code: string
  email: string
  password: string
  channel: string
  payoutInfo: string
}): Promise<{ ok: boolean; error?: string }> {
  try {
    const { data: authData, error: authError } = await supabase.auth.signUp({
      email: data.email.trim().toLowerCase(),
      password: data.password,
      options: { data: { full_name: data.name } },
    })
    if (authError) return { ok: false, error: authError.message }
    if (!authData.user) return { ok: false, error: 'Регистрацијата не успеа.' }

    if (!authData.session) {
      await supabase.auth.signInWithPassword({ email: data.email, password: data.password })
    }

    const { error } = await supabase.from('affiliates').insert({
      user_id: authData.user.id,
      name: data.name.trim(),
      code: data.code.toLowerCase().trim(),
      channel: data.channel.trim() || null,
      payout_info: data.payoutInfo.trim() || null,
    })
    if (error) {
      if (error.code === '23505') return { ok: false, error: 'Овој код е веќе зафатен. Одбери друг.' }
      return { ok: false, error: 'Грешка: ' + error.message }
    }
    return { ok: true }
  } catch (e: unknown) {
    return { ok: false, error: String(e) }
  }
}

export async function affiliateLogin(
  email: string,
  password: string,
): Promise<{ ok: boolean; error?: string }> {
  const { error } = await supabase.auth.signInWithPassword({ email, password })
  if (error) return { ok: false, error: 'Погрешна е-пошта или лозинка.' }
  return { ok: true }
}

export async function checkCodeAvailable(code: string): Promise<boolean> {
  const { data } = await supabase.from('affiliates').select('id').eq('code', code.toLowerCase()).maybeSingle()
  return !data
}

// ── AFFILIATE PROFILE ─────────────────────────────────────────────
export async function getMyAffiliate(): Promise<Affiliate | null> {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return null
    const { data } = await supabase.from('affiliates').select('*').eq('user_id', user.id).maybeSingle()
    return data || null
  } catch { return null }
}

export async function getMyReferrals(affiliateId: string): Promise<{ status: string; created_at: string }[]> {
  try {
    const { data } = await supabase
      .from('subscriptions').select('status, created_at').eq('affiliate_id', affiliateId)
    return data || []
  } catch { return [] }
}

export async function getMyPayouts(affiliateId: string): Promise<AffiliatePayout[]> {
  try {
    const { data } = await supabase
      .from('affiliate_payouts').select('*').eq('affiliate_id', affiliateId)
      .order('created_at', { ascending: false })
    return data || []
  } catch { return [] }
}

export function estimatedMonthlyEur(activeCount: number): number {
  return Math.round(activeCount * 10 * 0.3 * 100) / 100
}

// ── ADMIN ─────────────────────────────────────────────────────────
export async function adminGetAffiliates(): Promise<(Affiliate & { referral_count: number })[]> {
  try {
    const { data: affiliates } = await supabase.from('affiliates').select('*').order('created_at', { ascending: false })
    if (!affiliates) return []
    const rows = await Promise.all(affiliates.map(async (a) => {
      const { count } = await supabase
        .from('subscriptions').select('*', { count: 'exact', head: true }).eq('affiliate_id', a.id)
      return { ...a, referral_count: count || 0 }
    }))
    return rows
  } catch { return [] }
}

export async function adminSetAffiliateStatus(
  affiliateId: string,
  status: 'active' | 'suspended' | 'pending',
): Promise<void> {
  await supabase.from('affiliates').update({ status }).eq('id', affiliateId)
}

export async function adminGetSubscriptions(): Promise<{ id: string; status: string; created_at: string; affiliate_id: string | null; affiliates: { name: string; code: string } | null }[]> {
  try {
    const { data } = await supabase
      .from('subscriptions')
      .select('id, status, created_at, affiliate_id, affiliates(name, code)')
      .order('created_at', { ascending: false })
    return (data as never) || []
  } catch { return [] }
}

export async function adminGetPayouts(): Promise<(AffiliatePayout & { affiliates: { name: string; code: string } })[]> {
  try {
    const { data } = await supabase
      .from('affiliate_payouts')
      .select('*, affiliates(name, code)')
      .order('created_at', { ascending: false })
    return (data as never) || []
  } catch { return [] }
}

export async function adminCreatePayout(data: {
  affiliateId: string
  amountEur: number
  amountMkd: number
  periodLabel: string
  note?: string
}): Promise<{ ok: boolean; error?: string }> {
  const { error } = await supabase.from('affiliate_payouts').insert({
    affiliate_id: data.affiliateId,
    amount_eur: data.amountEur,
    amount_mkd: data.amountMkd,
    period_label: data.periodLabel,
    note: data.note || null,
  })
  if (error) return { ok: false, error: error.message }
  return { ok: true }
}

export async function adminMarkPaid(payoutId: string): Promise<void> {
  await supabase.from('affiliate_payouts')
    .update({ status: 'paid', paid_at: new Date().toISOString() })
    .eq('id', payoutId)
}
