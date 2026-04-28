'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { parentLogout, PLANS, familyMonthlyEur, familyMonthlyMkd, familyAnnualEur, familyAnnualMkd } from '@/lib/auth'

type Billing = 'monthly' | 'annual'

export default function TrialExpiredPage() {
  const router = useRouter()
  const [billing, setBilling] = useState<Billing>('monthly')
  const [kids, setKids] = useState(1)

  const eurMonth = familyMonthlyEur(kids)
  const mkdMonth = familyMonthlyMkd(kids)
  const eurYear  = familyAnnualEur(kids)
  const mkdYear  = familyAnnualMkd(kids)

  const displayEur = billing === 'monthly' ? eurMonth : Math.round(eurYear / 12)
  const displayMkd = billing === 'monthly' ? mkdMonth : Math.round(mkdYear / 12)
  const saveEur    = eurMonth * 12 - eurYear
  const saveMkd    = mkdMonth * 12 - mkdYear

  return (
    <main className="min-h-screen px-4 py-10"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>

      {/* Header */}
      <div className="text-center mb-8">
        <div className="text-6xl mb-3">⭐</div>
        <h1 className="text-3xl font-black text-white">Твојот пробен период заврши!</h1>
        <p className="text-purple-200 mt-2 max-w-sm mx-auto">
          Одбери колку деца и продолжи да учите заедно!
        </p>
      </div>

      <div className="max-w-lg mx-auto space-y-4">

        {/* Main pricing card */}
        <div className="bg-white rounded-3xl overflow-hidden"
          style={{ boxShadow: '0 0 0 3px #FFD93D' }}>

          <div className="py-2.5 text-center text-sm font-black"
            style={{ background: '#FFD93D', color: '#1A1A2E' }}>
            ⭐ СЕМЕЕН ПЛАН — СИТЕ ПРЕДМЕТИ
          </div>

          <div className="p-6 space-y-5">

            {/* Billing toggle */}
            <div className="flex justify-center">
              <div className="rounded-2xl p-1 flex gap-1" style={{ background: '#F3F0FF' }}>
                {(['monthly', 'annual'] as Billing[]).map((b) => (
                  <button key={b} type="button" onClick={() => setBilling(b)}
                    className="px-5 py-2 rounded-xl font-black text-sm transition-all duration-150"
                    style={{
                      background: billing === b ? '#5C35D4' : 'transparent',
                      color: billing === b ? 'white' : '#5C35D4',
                    }}>
                    {b === 'monthly' ? 'Месечно' : 'Годишно'}
                    {b === 'annual' && (
                      <span className="ml-1.5 text-xs px-1.5 py-0.5 rounded-full font-black"
                        style={{ background: '#6BCB77', color: 'white' }}>
                        -2 мес
                      </span>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* Kid selector */}
            <div>
              <p className="text-xs font-black tracking-widest text-center mb-3" style={{ color: '#6B6B8A' }}>
                БРОЈ НА ДЕЦА
              </p>
              <div className="grid grid-cols-3 gap-2">
                {[1, 2, 3].map((n) => (
                  <button key={n} type="button" onClick={() => setKids(n)}
                    className="py-4 rounded-2xl font-black text-lg border-2 transition-all duration-150 relative"
                    style={{
                      background: kids === n ? '#5C35D4' : 'white',
                      color: kids === n ? '#FFD93D' : '#5C35D4',
                      borderColor: kids === n ? '#5C35D4' : '#E5E7EB',
                    }}>
                    {n} {n === 1 ? 'дете' : 'деца'}
                    {n === 3 && (
                      <span className="absolute -top-2.5 left-1/2 -translate-x-1/2 text-xs font-black px-2 py-0.5 rounded-full whitespace-nowrap"
                        style={{ background: '#6BCB77', color: 'white' }}>
                        3то бесплатно
                      </span>
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* Price display */}
            <div className="rounded-2xl p-5 text-center" style={{ background: '#F7F5FF' }}>
              <div className="flex items-end justify-center gap-2">
                <span className="text-5xl font-black" style={{ color: '#5C35D4' }}>€{displayEur}</span>
                <span className="text-lg font-black mb-1" style={{ color: '#9B9BAA' }}>/месец</span>
              </div>
              <p className="text-base font-black mt-1" style={{ color: '#6B6B8A' }}>
                {displayMkd} ден/месец
              </p>
              {billing === 'annual' && (
                <p className="text-sm font-bold mt-2" style={{ color: '#6BCB77' }}>
                  Заштеди €{saveEur} ({saveMkd} ден) годишно
                </p>
              )}
              {billing === 'annual' && (
                <p className="text-xs mt-1 font-semibold" style={{ color: '#9B9BAA' }}>
                  Наплата €{eurYear} ({mkdYear} ден) еднаш годишно
                </p>
              )}
            </div>

            {/* Breakdown */}
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm font-semibold"
                style={{ color: '#3A3A5C' }}>
                <span style={{ color: '#6BCB77' }}>✓</span>
                <span className="flex-1 ml-2">Прво дете</span>
                <span className="font-black">€10 / 600 ден</span>
              </div>
              <div className="flex items-center justify-between text-sm font-semibold"
                style={{ color: kids >= 2 ? '#3A3A5C' : '#C0C0C0' }}>
                <span style={{ color: kids >= 2 ? '#6BCB77' : '#D1D5DB' }}>✓</span>
                <span className="flex-1 ml-2">Второ дете</span>
                <span className="font-black">+€5 / +300 ден</span>
              </div>
              <div className="flex items-center justify-between text-sm font-semibold"
                style={{ color: kids >= 3 ? '#3A3A5C' : '#C0C0C0' }}>
                <span style={{ color: kids >= 3 ? '#6BCB77' : '#D1D5DB' }}>✓</span>
                <span className="flex-1 ml-2">Трето дете</span>
                <span className="font-black" style={{ color: '#6BCB77' }}>БЕСПЛАТНО 🎁</span>
              </div>
              <div className="border-t pt-2 flex items-center justify-between text-sm font-semibold" style={{ color: '#3A3A5C' }}>
                <span style={{ color: '#6BCB77' }}>✓</span>
                <span className="flex-1 ml-2">Сите предмети — Math, Bio, Hem</span>
              </div>
              <div className="flex items-center justify-between text-sm font-semibold" style={{ color: '#3A3A5C' }}>
                <span style={{ color: '#6BCB77' }}>✓</span>
                <span className="flex-1 ml-2">Секое дете свој профил + PIN</span>
              </div>
              <div className="flex items-center justify-between text-sm font-semibold" style={{ color: '#3A3A5C' }}>
                <span style={{ color: '#6BCB77' }}>✓</span>
                <span className="flex-1 ml-2">Родителски преглед на напредок</span>
              </div>
            </div>

            <button type="button"
              className="w-full py-4 rounded-2xl font-black text-lg text-white transition-all active:scale-95"
              style={{ background: 'linear-gradient(135deg, #5C35D4, #7B5CE5)' }}>
              Претплати се →
            </button>
          </div>
        </div>

        {/* School plan */}
        <div className="bg-white rounded-3xl p-5">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-3">
              <span className="text-3xl">🏫</span>
              <div>
                <div className="font-black text-lg" style={{ color: '#1A1A2E' }}>{PLANS.school.label}</div>
                <div className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>До 35 ученици</div>
              </div>
            </div>
            <div className="text-right">
              <div className="text-3xl font-black" style={{ color: '#6BCB77' }}>
                €{billing === 'monthly' ? PLANS.school.price : Math.round(PLANS.school.annual / 12)}
              </div>
              <div className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>
                {billing === 'monthly' ? '/месец' : `€${PLANS.school.annual}/год`}
              </div>
            </div>
          </div>
          <ul className="space-y-1.5 mb-4">
            {['До 35 ученици', 'Наставнички портал', 'Задавање домашни по одделение', 'Извештаи за секој ученик', 'Фактура за институции'].map((f) => (
              <li key={f} className="flex items-center gap-2 text-sm font-semibold" style={{ color: '#3A3A5C' }}>
                <span style={{ color: '#6BCB77' }}>✓</span> {f}
              </li>
            ))}
          </ul>
          <button type="button"
            className="w-full py-3.5 rounded-2xl font-black text-white transition-all active:scale-95"
            style={{ background: 'linear-gradient(135deg, #6BCB77, #4CAF50)' }}>
            Контактирај нè →
          </button>
        </div>

        {/* Payment note */}
        <div className="rounded-2xl p-4" style={{ background: 'rgba(255,255,255,0.1)' }}>
          <div className="flex items-start gap-3">
            <span className="text-xl">🏦</span>
            <div>
              <p className="text-white font-black text-sm">Плаќање преку МК банки</p>
              <p className="text-purple-200 text-xs mt-0.5">
                Casys · NestPay · Monri · Трансакција на сметка за претплата по фактура
              </p>
            </div>
          </div>
        </div>

        {/* Early adopter banner */}
        <div className="rounded-2xl p-4"
          style={{ background: 'rgba(255,217,61,0.15)', border: '1.5px solid rgba(255,217,61,0.4)' }}>
          <div className="flex items-start gap-3">
            <span className="text-xl">🚀</span>
            <div>
              <p className="text-yellow-300 font-black text-sm">Рана претплата — само за први 500!</p>
              <p className="text-yellow-100 text-xs mt-0.5">
                1 дете €5/мес · 2–3 деца €9/мес — заклучена цена засекогаш
              </p>
            </div>
          </div>
        </div>

        <div className="text-center pt-2">
          <button type="button"
            onClick={() => { parentLogout(); router.push('/') }}
            className="text-purple-300 hover:text-white text-sm font-bold transition-colors">
            ← Назад на почеток
          </button>
        </div>

      </div>
    </main>
  )
}
