'use client'

// The Synthesis "discovery" widget for equivalence.
// Start: pizza split in 2, one half topping → 1/2.
// Kid taps the topping half → it splits into 2 → now 2/4.
// They've PROVEN 1/2 = 2/4 by the act of splitting.
//
// Multi-beat narration callback fires as state changes so the LessonRunner
// can update what the tutor says.

import { useState } from 'react'
import { Pie } from './Pie'

export type SplitStage = 'initial' | 'split' | 'compared'

interface Props {
  startParts: number              // e.g. 2
  startShadedCount: number        // e.g. 1   (so 1/2)
  finalParts: number              // e.g. 4
  compareTarget?: { parts: number; shaded: number }   // optional right-side reference shown from start
  onStageChange?: (stage: SplitStage) => void
  onComplete?: () => void
}

export function SplittablePie({
  startParts,
  startShadedCount,
  finalParts,
  compareTarget,
  onStageChange,
  onComplete,
}: Props) {
  const [parts, setParts] = useState(startParts)
  const [shaded, setShaded] = useState<Set<number>>(
    new Set(Array.from({ length: startShadedCount }, (_, i) => i)),
  )
  const [stage, setStage] = useState<SplitStage>('initial')

  const multiplier = finalParts / startParts

  const handleTap = (i: number) => {
    if (stage !== 'initial') return
    if (!shaded.has(i)) return // only split a shaded slice

    // Multiply parts and shaded count
    setParts(finalParts)
    const nextShaded = new Set<number>()
    // each original shaded slice maps to `multiplier` new slices, in order
    Array.from(shaded)
      .sort((a, b) => a - b)
      .forEach((origIdx) => {
        for (let k = 0; k < multiplier; k++) {
          nextShaded.add(origIdx * multiplier + k)
        }
      })
    setShaded(nextShaded)
    setStage('split')
    onStageChange?.('split')

    // Auto-advance to "compared" after a moment so the kid sees the split land
    setTimeout(() => {
      setStage('compared')
      onStageChange?.('compared')
      onComplete?.()
    }, 1400)
  }

  return (
    <div className="flex flex-col items-center gap-6">
      <div className="flex gap-10 items-center">
        <div className="flex flex-col items-center gap-2">
          <Pie
            parts={parts}
            shadedIndices={shaded}
            onTapSlice={stage === 'initial' ? handleTap : undefined}
            pulseIndex={stage === 'initial' ? 0 : undefined}
            size={240}
          />
          <div className="text-2xl font-bold tabular-nums text-slate-800 transition-colors">
            {shaded.size} <span className="text-slate-400">/</span> {parts}
          </div>
        </div>

        {compareTarget && (
          <>
            <div className="text-4xl font-bold text-slate-400">
              {stage === 'compared' ? '=' : '?'}
            </div>
            <div className="flex flex-col items-center gap-2">
              <Pie
                parts={compareTarget.parts}
                shadedIndices={
                  new Set(Array.from({ length: compareTarget.shaded }, (_, i) => i))
                }
                size={240}
              />
              <div className="text-2xl font-bold tabular-nums text-slate-800">
                {compareTarget.shaded} <span className="text-slate-400">/</span> {compareTarget.parts}
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
