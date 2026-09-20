'use client'

import { useState } from 'react'
import Link from 'next/link'
import { LessonRunner } from '@/components/interactive/LessonRunner'
import type { InteractiveLessonSpec } from '@/lib/interactive/types'

export default function SandboxPage() {
  const [topic, setTopic] = useState('Дропки — еквивалентни дропки')
  const [grade, setGrade] = useState(6)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [spec, setSpec] = useState<InteractiveLessonSpec | null>(null)
  const [usage, setUsage] = useState<{ prompt_tokens: number; completion_tokens: number } | null>(null)

  const generate = async () => {
    setLoading(true)
    setError(null)
    setSpec(null)
    setUsage(null)
    try {
      const r = await fetch('/api/sandbox/generate-lesson', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, grade }),
      })
      const json = await r.json()
      if (!r.ok) {
        setError(json.error + (json.detail ? ': ' + json.detail : ''))
        return
      }
      setSpec(json.spec)
      setUsage(json.usage ?? null)
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : String(e))
    } finally {
      setLoading(false)
    }
  }

  if (spec) {
    return (
      <div>
        <div className="bg-slate-100 p-3 flex gap-3 items-center justify-between border-b">
          <div className="text-sm text-slate-600">
            ✨ Лекција генерирана со OpenAI · {usage?.prompt_tokens ?? '?'} токени вход, {usage?.completion_tokens ?? '?'} излез
          </div>
          <button
            type="button"
            onClick={() => setSpec(null)}
            className="text-sm px-3 py-1.5 rounded bg-white border hover:bg-slate-50"
          >
            ← Нова лекција
          </button>
        </div>
        <LessonRunner spec={spec} />
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-slate-50 p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-2">Sandbox: OpenAI-генерирана лекција</h1>
        <p className="text-slate-600 mb-6">
          Внеси тема од BRO програма. OpenAI ќе ja претвори во интерактивна лекција (Synthesis-стил, со субтитли).
        </p>

        <div className="bg-white rounded-2xl shadow p-6 space-y-4">
          <label className="block">
            <span className="text-sm font-medium text-slate-700">Тема</span>
            <input
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="напр. Дропки — еквивалентни дропки"
              className="mt-1 w-full px-4 py-2.5 rounded-lg border-2 border-slate-200 focus:border-indigo-500 outline-none"
            />
          </label>

          <label className="block">
            <span className="text-sm font-medium text-slate-700">Одделение</span>
            <select
              value={grade}
              onChange={(e) => setGrade(Number(e.target.value))}
              className="mt-1 w-full px-4 py-2.5 rounded-lg border-2 border-slate-200 focus:border-indigo-500 outline-none"
            >
              {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((g) => (
                <option key={g} value={g}>
                  {g}-то одделение
                </option>
              ))}
            </select>
          </label>

          <button
            type="button"
            onClick={generate}
            disabled={loading || !topic.trim()}
            className="w-full px-6 py-3 rounded-xl bg-indigo-600 text-white font-semibold hover:bg-indigo-700 disabled:bg-slate-300"
          >
            {loading ? 'Генерира…' : 'Генерирај лекција'}
          </button>

          {error && (
            <div className="bg-red-50 border border-red-200 rounded p-3 text-sm text-red-700">
              {error}
            </div>
          )}
        </div>

        {/* Quick prompt presets */}
        <div className="mt-6 space-y-2">
          <div className="text-xs uppercase tracking-wider text-slate-500 font-medium">Брзи теми</div>
          {[
            { t: 'Дропки — еквивалентни дропки', g: 6 },
            { t: 'Прости броеви и сложени броеви', g: 6 },
            { t: 'Множества и подмножества', g: 6 },
            { t: 'Собирање на дропки со ист именител', g: 6 },
            { t: 'НЗД и НЗС', g: 6 },
            { t: 'Римски броеви — XL, XC, XLIX', g: 6 },
          ].map((p) => (
            <button
              key={p.t}
              type="button"
              onClick={() => {
                setTopic(p.t)
                setGrade(p.g)
              }}
              className="block w-full text-left px-4 py-2 rounded-lg bg-white border hover:bg-indigo-50 hover:border-indigo-200"
            >
              {p.t} <span className="text-xs text-slate-400">· {p.g}-то одд.</span>
            </button>
          ))}
        </div>

        <div className="mt-8 pt-6 border-t">
          <div className="text-xs uppercase tracking-wider text-slate-500 font-medium mb-2">Рачно-напишана референца</div>
          <Link
            href="/sandbox/interactive/math6-1-5"
            className="block p-4 bg-white rounded-xl border hover:border-indigo-300"
          >
            math6-1-5 · Дропки (хард-кодирано, без OpenAI)
          </Link>
        </div>
      </div>
    </div>
  )
}
