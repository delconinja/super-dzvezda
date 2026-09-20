'use client'

import { useState } from 'react'
import { FractionBar } from './FractionBar'
import { Pie } from './Pie'
import { SplittablePie } from './SplittablePie'
import type {
  WidgetConfig,
  TapShadeConfig,
  IdentifyConfig,
  FractionPairConfig,
  SplittablePieConfig,
} from '@/lib/interactive/types'

export type WidgetEvent =
  | { kind: 'progress' }      // kid did something
  | { kind: 'success' }
  | { kind: 'wrong' }

interface WidgetProps {
  widget: WidgetConfig
  emit: (e: WidgetEvent) => void
  resetKey: number
}

export function Widget({ widget, emit, resetKey }: WidgetProps) {
  switch (widget.type) {
    case 'tap-shade':
      return <TapShade config={widget.config} emit={emit} key={resetKey} />
    case 'identify':
      return <Identify config={widget.config} emit={emit} key={resetKey} />
    case 'fraction-pair':
      return <FractionPair config={widget.config} emit={emit} key={resetKey} />
    case 'splittable-pie':
      return <SplittablePieWidget config={widget.config} emit={emit} key={resetKey} />
    case 'fraction-bar':
      return <FractionBar parts={widget.config.parts} shaded={widget.config.shaded} />
  }
}

// ─── helpers ──────────────────────────────────────────────────────

function ChoiceVisual({
  shape,
  parts,
  shaded,
  width = 220,
  height = 64,
}: {
  shape: 'bar' | 'pie'
  parts: number
  shaded: number
  width?: number
  height?: number
}) {
  if (shape === 'pie') {
    return (
      <Pie
        parts={parts}
        shadedIndices={new Set(Array.from({ length: shaded }, (_, i) => i))}
        size={Math.min(width, 160)}
      />
    )
  }
  return <FractionBar parts={parts} shaded={shaded} width={width} height={height} showLabel={false} />
}

// ─── TAP-SHADE ──────────────────────────────────────────────────

function TapShade({ config, emit }: { config: TapShadeConfig; emit: (e: WidgetEvent) => void }) {
  const [shadedSet, setShadedSet] = useState<Set<number>>(new Set())
  const [submitted, setSubmitted] = useState(false)
  const [firstAction, setFirstAction] = useState(false)

  const toggle = (i: number) => {
    if (submitted) return
    if (!firstAction) {
      setFirstAction(true)
      emit({ kind: 'progress' })
    }
    const next = new Set(shadedSet)
    if (next.has(i)) next.delete(i)
    else next.add(i)
    setShadedSet(next)
  }

  const submit = () => {
    if (submitted) return
    setSubmitted(true)
    const correct = shadedSet.size === config.target
    emit({ kind: correct ? 'success' : 'wrong' })
  }

  const wrong = submitted && shadedSet.size !== config.target

  return (
    <div className="flex flex-col items-center gap-6">
      <FractionBar
        parts={config.parts}
        shaded={0}
        onTap={toggle}
        interactiveIndices={shadedSet}
      />
      <button
        type="button"
        onClick={submit}
        disabled={submitted || shadedSet.size === 0}
        className={`px-6 py-3 rounded-xl font-semibold transition ${
          submitted
            ? wrong
              ? 'bg-red-100 text-red-700'
              : 'bg-emerald-500 text-white'
            : 'bg-indigo-600 text-white disabled:bg-slate-200 disabled:text-slate-400 hover:bg-indigo-700'
        }`}
      >
        {submitted ? (wrong ? 'Не точно' : 'Точно!') : 'Провери'}
      </button>
    </div>
  )
}

// ─── IDENTIFY ──────────────────────────────────────────────────

function Identify({ config, emit }: { config: IdentifyConfig; emit: (e: WidgetEvent) => void }) {
  const [chosen, setChosen] = useState<number | null>(null)
  const shape = config.shape ?? 'bar'

  const pick = (i: number) => {
    if (chosen !== null) return
    setChosen(i)
    emit({ kind: config.choices[i].isCorrect ? 'success' : 'wrong' })
  }

  return (
    <div className="flex flex-col items-center gap-6 w-full">
      <p className="text-slate-700 text-lg font-medium text-center">{config.question}</p>
      <div className="grid grid-cols-2 gap-4 w-full max-w-2xl">
        {config.choices.map((c, i) => {
          const isChosen = chosen === i
          const shown = chosen !== null
          let ring = 'ring-slate-200'
          let bg = 'bg-white'
          if (shown && isChosen) {
            ring = c.isCorrect ? 'ring-emerald-500' : 'ring-red-500'
            bg = c.isCorrect ? 'bg-emerald-50' : 'bg-red-50'
          } else if (shown && c.isCorrect) {
            ring = 'ring-emerald-300'
          }
          return (
            <button
              key={i}
              type="button"
              onClick={() => pick(i)}
              disabled={chosen !== null}
              aria-label={`${c.shaded} од ${c.parts}`}
              title={`${c.shaded}/${c.parts}`}
              className={`rounded-2xl p-4 flex items-center justify-center min-h-[140px] ring-2 ${ring} ${bg} transition ${
                chosen === null ? 'hover:ring-indigo-400 cursor-pointer' : 'cursor-default'
              }`}
            >
              <ChoiceVisual shape={shape} parts={c.parts} shaded={c.shaded} />
            </button>
          )
        })}
      </div>
    </div>
  )
}

// ─── FRACTION PAIR ──────────────────────────────────────────────

function FractionPair({
  config,
  emit,
}: {
  config: FractionPairConfig
  emit: (e: WidgetEvent) => void
}) {
  const [revealed, setRevealed] = useState(false)

  const reveal = () => {
    if (revealed) return
    setRevealed(true)
    emit({ kind: 'success' })
  }

  return (
    <div className="flex flex-col items-center gap-6 w-full">
      <div className="flex gap-8 items-center">
        <FractionBar parts={config.left.parts} shaded={config.left.shaded} width={220} height={70} />
        <div className="text-3xl font-bold text-slate-400">?</div>
        <FractionBar parts={config.right.parts} shaded={config.right.shaded} width={220} height={70} />
      </div>
      {revealed ? (
        <div className="text-2xl font-semibold text-emerald-700">
          {config.left.shaded}/{config.left.parts} = {config.right.shaded}/{config.right.parts} ✓
        </div>
      ) : (
        <button
          type="button"
          onClick={reveal}
          className="px-6 py-3 rounded-xl bg-indigo-600 text-white font-semibold hover:bg-indigo-700"
        >
          Спореди
        </button>
      )}
    </div>
  )
}

// ─── SPLITTABLE PIE ─────────────────────────────────────────────

function SplittablePieWidget({
  config,
  emit,
}: {
  config: SplittablePieConfig
  emit: (e: WidgetEvent) => void
}) {
  return (
    <SplittablePie
      startParts={config.startParts}
      startShadedCount={config.startShaded}
      finalParts={config.finalParts}
      compareTarget={config.compareTo}
      onStageChange={(stage) => {
        if (stage === 'split') emit({ kind: 'progress' })
      }}
      onComplete={() => emit({ kind: 'success' })}
    />
  )
}
