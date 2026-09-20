'use client'

import { useEffect, useMemo, useState } from 'react'
import { Widget, type WidgetEvent } from './Widgets'
import type { InteractiveLessonSpec, NarrationBeat } from '@/lib/interactive/types'

type Phase = 'enter' | 'progressing' | 'success' | 'wrong' | 'hint-shown'

interface Props {
  spec: InteractiveLessonSpec
}

function pickBeat(beats: NarrationBeat[], phase: Phase): NarrationBeat | null {
  // map phase → trigger preference, falling back to a sensible default
  const order: Record<Phase, NarrationBeat['trigger'][]> = {
    enter: ['enter'],
    progressing: ['on-progress', 'enter'],
    success: ['on-success', 'enter'],
    wrong: ['on-wrong', 'enter'],
    'hint-shown': ['on-hint', 'on-wrong', 'enter'],
  }
  for (const t of order[phase]) {
    const found = beats.find((b) => b.trigger === t)
    if (found) return found
  }
  return beats[0] ?? null
}

export function LessonRunner({ spec }: Props) {
  const [sceneIdx, setSceneIdx] = useState(0)
  const [phase, setPhase] = useState<Phase>('enter')
  const [resetKey, setResetKey] = useState(0)
  const [missCount, setMissCount] = useState(0)

  const scene = spec.scenes[sceneIdx]
  const isLast = sceneIdx === spec.scenes.length - 1

  useEffect(() => {
    setPhase('enter')
    setMissCount(0)
  }, [sceneIdx])

  const currentBeat = useMemo(
    () => pickBeat(scene.narration, phase),
    [scene, phase],
  )

  const onWidgetEvent = (e: WidgetEvent) => {
    if (e.kind === 'progress') {
      if (phase === 'enter') setPhase('progressing')
    } else if (e.kind === 'success') {
      setPhase('success')
    } else if (e.kind === 'wrong') {
      const next = missCount + 1
      setMissCount(next)
      setPhase(next >= 2 ? 'hint-shown' : 'wrong')
    }
  }

  const next = () => {
    if (isLast) return
    setSceneIdx(sceneIdx + 1)
    setResetKey((k) => k + 1)
  }

  const retry = () => {
    setPhase('enter')
    setResetKey((k) => k + 1)
  }

  const progress =
    ((sceneIdx + (phase === 'success' ? 1 : 0)) / spec.scenes.length) * 100

  return (
    <div className="min-h-screen bg-gradient-to-b from-indigo-50 to-white p-6">
      <div className="max-w-3xl mx-auto">
        {/* Header */}
        <div className="mb-6">
          <div className="text-xs uppercase tracking-wider text-indigo-500 font-medium">
            {spec.bro_topic}
          </div>
          <h1 className="text-3xl font-bold text-slate-900">{spec.title}</h1>
          <div className="mt-3 h-2 bg-slate-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-indigo-500 transition-all duration-500"
              style={{ width: `${progress}%` }}
            />
          </div>
          <div className="mt-1 text-sm text-slate-500">
            Сцена {sceneIdx + 1} од {spec.scenes.length}
          </div>
        </div>

        {/* Scene card */}
        <div className="bg-white rounded-3xl shadow-lg p-6 sm:p-8">
          {scene.prompt && (
            <p className="text-slate-700 text-xl mb-4 text-center font-medium">
              {scene.prompt}
            </p>
          )}

          {/* Widget */}
          <div className="my-6 flex justify-center">
            <Widget widget={scene.widget} emit={onWidgetEvent} resetKey={resetKey} />
          </div>

          {/* Bottom subtitle bar — tutor speaks here, updates with progress */}
          <SubtitleBar
            beat={currentBeat}
            phase={phase}
            isLast={isLast}
            onNext={next}
            onRetry={retry}
          />
        </div>

        <p className="text-center text-xs text-slate-400 mt-6">
          Прототип · Synthesis-стил · без звук · OpenAI-генериран спец
        </p>
      </div>
    </div>
  )
}

function SubtitleBar({
  beat,
  phase,
  isLast,
  onNext,
  onRetry,
}: {
  beat: NarrationBeat | null
  phase: Phase
  isLast: boolean
  onNext: () => void
  onRetry: () => void
}) {
  const baseColors: Record<Phase, string> = {
    enter: 'bg-amber-50 border-amber-300 text-amber-900',
    progressing: 'bg-indigo-50 border-indigo-300 text-indigo-900',
    success: 'bg-emerald-50 border-emerald-300 text-emerald-900',
    wrong: 'bg-red-50 border-red-300 text-red-900',
    'hint-shown': 'bg-amber-50 border-amber-400 text-amber-900',
  }
  const icons: Record<Phase, string> = {
    enter: '🎙',
    progressing: '🎙',
    success: '🎉',
    wrong: '🤔',
    'hint-shown': '💡',
  }

  return (
    <div className={`border-l-4 rounded-lg p-4 ${baseColors[phase]}`}>
      <div className="text-xs uppercase font-semibold mb-1 opacity-70">
        {icons[phase]} Тутор
      </div>
      <p className="text-lg leading-relaxed">{beat?.text ?? '…'}</p>

      {phase === 'success' && (
        <div className="mt-4 flex justify-end">
          <button
            type="button"
            onClick={onNext}
            disabled={isLast}
            className="px-5 py-2.5 rounded-xl bg-emerald-600 text-white font-semibold hover:bg-emerald-700 disabled:opacity-50"
          >
            {isLast ? 'Готово 🎉' : 'Следно →'}
          </button>
        </div>
      )}

      {(phase === 'wrong' || phase === 'hint-shown') && (
        <div className="mt-4 flex justify-end">
          <button
            type="button"
            onClick={onRetry}
            className="px-5 py-2.5 rounded-xl bg-white border-2 text-slate-700 font-semibold hover:bg-slate-50"
          >
            Пробај пак
          </button>
        </div>
      )}
    </div>
  )
}
