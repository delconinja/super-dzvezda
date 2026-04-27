'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { parentLogout, PLANS } from '@/lib/auth'

type Billing = 'monthly' | 'annual'

export default function TrialExpiredPage() {
  const router = useRouter()
  const [billing, setBilling] = useState<Billing>('monthly')

  const plans = [
    {
      key: 'individual',
      ...PLANS.individual,
      emoji: '⭐',
      color: '#5C35D4',
      bg: '#EDE9FF',
      highlight: false,
    },
    {
      key: 'family',
      ...PLANS.family,
      emoji: '👨‍👩‍👧‍👦',
      color: '#FF6B6B',
      bg: '#FFE8E8',
      highlight: true,
    },
    {
      key: 'school',
      ...PLANS.school,
      emoji: '🏫',
      color: '#6BCB77',
      bg: '#E8F8EA',
      highlight: false,
    },
  ]

  return (
    <main className="min-h-screen px-4 py-10"
      style={{ background: 'linear-gradient(135deg, #1A1A2E 0%, #2D1B69 50%, #5C35D4 100%)' }}>

      {/* Header */}
      <div className="text-center mb-8">
        <div className="text-6xl mb-3">⭐</div>
        <h1 className="text-3xl font-black text-white">Твојот пробен период заврши!</h1>
        <p className="text-purple-200 mt-2 max-w-sm mx-auto">
          Се надеваме дека ти се допадна Супер Ѕвезда. Одбери план и продолжи да учиш!
        </p>
      </div>

      {/* Billing toggle */}
      <div className="flex justify-center mb-8">
        <div className="bg-white/10 rounded-2xl p-1 flex gap-1">
          {(['monthly', 'annual'] as Billing[]).map((b) => (
            <button key={b} type="button" onClick={() => setBilling(b)}
              className="px-5 py-2 rounded-xl font-black text-sm transition-all duration-150"
              style={{
                background: billing === b ? '#FFD93D' : 'transparent',
                color: billing === b ? '#1A1A2E' : 'white',
              }}>
              {b === 'monthly' ? 'Месечно' : 'Годишно'}
              {b === 'annual' && (
                <span className="ml-1.5 text-xs px-1.5 py-0.5 rounded-full font-black"
                  style={{ background: '#6BCB77', color: 'white' }}>
                  -2 месеци
                </span>
              )}
            </button>
          ))}
        </div>
      </div>

      {/* Plan cards */}
      <div className="grid gap-4 max-w-lg mx-auto mb-8">
        {plans.map((plan) => (
          <div key={plan.key}
            className="rounded-3xl overflow-hidden"
            style={{
              boxShadow: plan.highlight ? '0 0 0 3px #FFD93D' : 'none',
            }}>
            {plan.highlight && (
              <div className="py-2 text-center text-sm font-black"
                style={{ background: '#FFD93D', color: '#1A1A2E' }}>
                ⭐ НАЈПОПУЛАРЕН ИЗБОР
              </div>
            )}
            <div className="p-5" style={{ background: 'white' }}>
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-3">
                  <span className="text-3xl">{plan.emoji}</span>
                  <div>
                    <div className="font-black text-lg" style={{ color: '#1A1A2E' }}>{plan.label}</div>
                    <div className="text-sm font-semibold" style={{ color: '#9B9BAA' }}>{plan.desc}</div>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-3xl font-black" style={{ color: plan.color }}>
                    €{billing === 'monthly' ? plan.price : Math.round(plan.annual / 12)}
                  </div>
                  <div className="text-xs font-semibold" style={{ color: '#9B9BAA' }}>
                    {billing === 'monthly'
                      ? '/месец'
                      : `€${plan.annual}/год`}
                  </div>
                </div>
              </div>

              {/* Features */}
              <ul className="space-y-1.5 mb-4">
                {getFeatures(plan.key).map((f) => (
                  <li key={f} className="flex items-center gap-2 text-sm font-semibold"
                    style={{ color: '#3A3A5C' }}>
                    <span style={{ color: '#6BCB77' }}>✓</span> {f}
                  </li>
                ))}
              </ul>

              <button type="button"
                className="w-full py-3.5 rounded-2xl font-black text-white transition-all active:scale-95"
                style={{ background: `linear-gradient(135deg, ${plan.color}, ${plan.color}cc)` }}>
                Претплати се →
              </button>

              {billing === 'annual' && (
                <p className="text-center text-xs mt-2 font-semibold" style={{ color: '#9B9BAA' }}>
                  Заштеди €{(plan.price * 12) - plan.annual} годишно
                </p>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Payment note */}
      <div className="max-w-lg mx-auto rounded-2xl p-4 mb-6"
        style={{ background: 'rgba(255,255,255,0.1)' }}>
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
      <div className="max-w-lg mx-auto rounded-2xl p-4 mb-6"
        style={{ background: 'rgba(255,217,61,0.15)', border: '1.5px solid rgba(255,217,61,0.4)' }}>
        <div className="flex items-start gap-3">
          <span className="text-xl">🚀</span>
          <div>
            <p className="text-yellow-300 font-black text-sm">Рана претплата — само за први 500!</p>
            <p className="text-yellow-100 text-xs mt-0.5">
              Поединец €5/мес · Семеен €9/мес — заклучена цена засекогаш
            </p>
          </div>
        </div>
      </div>

      <div className="text-center">
        <button type="button"
          onClick={() => { parentLogout(); router.push('/') }}
          className="text-purple-300 hover:text-white text-sm font-bold transition-colors">
          ← Назад на почеток
        </button>
      </div>
    </main>
  )
}

function getFeatures(plan: string): string[] {
  switch (plan) {
    case 'individual': return [
      'Сите предмети — Math, Bio, Hem',
      'Сите единици и лекции',
      'Домашни задачи',
      'Следење на напредок',
    ]
    case 'family': return [
      'Сè од Поединец × 3 деца',
      'Секое дете има свој профил и PIN',
      'Родителски преглед на напредок',
      'Приоритетна поддршка',
    ]
    case 'school': return [
      'До 35 ученици',
      'Наставнички портал',
      'Задавање домашни по одделение',
      'Извештаи за секој ученик',
      'Фактура за институции',
    ]
    default: return []
  }
}
