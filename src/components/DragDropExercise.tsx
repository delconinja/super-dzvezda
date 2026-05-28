'use client'

import { useState } from 'react'

export interface DragDropItem {
  id: string
  label: string
  shapeType: 'circle' | 'triangle' | 'square' | 'cube'
}

export interface DragDropTarget {
  id: string
  label: string
  correctItemId: string
}

interface Props {
  items: DragDropItem[]
  targets: DragDropTarget[]
  color: string
  explanation: string
  onComplete: () => void
}

function ShapeSVG({ type }: { type: string }) {
  if (type === 'circle') return (
    <svg width="64" height="64" viewBox="0 0 80 80">
      <circle cx="40" cy="40" r="36" fill="#FF6B6B" stroke="white" strokeWidth="3"/>
    </svg>
  )
  if (type === 'triangle') return (
    <svg width="64" height="64" viewBox="0 0 80 80">
      <polygon points="40,6 74,72 6,72" fill="#FFD93D" stroke="white" strokeWidth="3"/>
    </svg>
  )
  if (type === 'square') return (
    <svg width="64" height="64" viewBox="0 0 80 80">
      <rect x="8" y="8" width="64" height="64" rx="6" fill="#4CAF50" stroke="white" strokeWidth="3"/>
    </svg>
  )
  if (type === 'cube') return (
    <svg width="64" height="64" viewBox="0 0 80 80">
      <polygon points="10,40 10,68 38,76 38,48" fill="#1565C0"/>
      <polygon points="10,40 38,48 68,36 40,28" fill="#64B5F6"/>
      <polygon points="38,48 68,36 68,64 38,76" fill="#1976D2"/>
    </svg>
  )
  return null
}

export default function DragDropExercise({ items, targets, color, explanation, onComplete }: Props) {
  const [selectedItemId, setSelectedItemId] = useState<string | null>(null)
  const [placed, setPlaced] = useState<Record<string, string>>({})
  const [shakeTarget, setShakeTarget] = useState<string | null>(null)
  const [done, setDone] = useState(false)

  const placedItemIds = Object.values(placed)

  const handleItemTap = (itemId: string) => {
    if (done) return
    if (placedItemIds.includes(itemId)) return
    setSelectedItemId(prev => prev === itemId ? null : itemId)
  }

  const handleTargetTap = (targetId: string) => {
    if (done || !selectedItemId) return
    const target = targets.find(t => t.id === targetId)!
    if (placed[targetId]) return

    if (target.correctItemId === selectedItemId) {
      const next = { ...placed, [targetId]: selectedItemId }
      setPlaced(next)
      setSelectedItemId(null)
      if (Object.keys(next).length === targets.length) {
        setDone(true)
        setTimeout(onComplete, 600)
      }
    } else {
      setShakeTarget(targetId)
      setTimeout(() => setShakeTarget(null), 400)
    }
  }

  return (
    <div className="flex flex-col gap-5">

      {/* Items row */}
      <div className="flex justify-center gap-4 flex-wrap">
        {items.map(item => {
          const isPlaced = placedItemIds.includes(item.id)
          const isSelected = selectedItemId === item.id
          return (
            <button key={item.id}
              onClick={() => handleItemTap(item.id)}
              disabled={isPlaced || done}
              className="flex flex-col items-center gap-1 p-3 rounded-2xl transition-all active:scale-95"
              style={{
                background: isSelected ? `${color}20` : 'white',
                border: `3px solid ${isSelected ? color : '#E8EAF0'}`,
                opacity: isPlaced ? 0 : 1,
                transform: isSelected ? 'scale(1.08)' : 'scale(1)',
                boxShadow: isSelected ? `0 0 0 4px ${color}40` : '0 2px 8px rgba(0,0,0,0.08)',
                cursor: isPlaced ? 'default' : 'pointer',
                transition: 'all 0.2s',
              }}>
              <ShapeSVG type={item.shapeType} />
            </button>
          )
        })}
      </div>

      {/* Instruction */}
      {!done && (
        <p className="text-center text-sm font-bold" style={{ color: '#9B9BAA' }}>
          {selectedItemId
            ? '👆 Сега допри го вистинското поле подолу'
            : '👆 Допри форма за да ја избереш'}
        </p>
      )}

      {/* Targets row */}
      <div className="flex justify-center gap-4 flex-wrap">
        {targets.map(target => {
          const placedItemId = placed[target.id]
          const placedItem = items.find(i => i.id === placedItemId)
          const isShaking = shakeTarget === target.id
          const isReady = !!selectedItemId && !placedItemId && !done

          return (
            <button key={target.id}
              onClick={() => handleTargetTap(target.id)}
              disabled={!!placedItemId || done}
              className={`flex flex-col items-center justify-center gap-2 p-3 rounded-2xl transition-all ${isShaking ? 'animate-shake' : ''}`}
              style={{
                minWidth: 88,
                minHeight: 100,
                background: placedItemId ? '#EDFFF2' : isReady ? `${color}10` : '#F7F7FA',
                border: `3px dashed ${placedItemId ? '#4CAF50' : isReady ? color : '#D1D5DB'}`,
                cursor: placedItemId || done ? 'default' : isReady ? 'pointer' : 'default',
                transition: 'all 0.2s',
              }}>
              {placedItem
                ? <ShapeSVG type={placedItem.shapeType} />
                : <span style={{ fontSize: 28, opacity: 0.2 }}>?</span>
              }
              <span className="text-xs font-black" style={{ color: placedItemId ? '#2E7D32' : '#6B6B8A' }}>
                {target.label}
              </span>
              {placedItemId && <span style={{ color: '#4CAF50', fontSize: 16 }}>✓</span>}
            </button>
          )
        })}
      </div>

      {/* Success + explanation */}
      {done && (
        <div className="rounded-2xl overflow-hidden animate-fade-up" style={{ border: '2px solid #4CAF50' }}>
          <div className="px-4 py-2" style={{ background: '#4CAF50' }}>
            <span className="font-black text-sm text-white">✓ Точно! Браво!</span>
          </div>
          <div className="px-4 py-3" style={{ background: '#EDFFF2' }}>
            <p className="text-sm font-semibold leading-relaxed" style={{ color: '#1A1A2E' }}>
              {explanation}
            </p>
          </div>
        </div>
      )}

      <style>{`
        @keyframes shake {
          0%, 100% { transform: translateX(0); }
          20% { transform: translateX(-6px); }
          40% { transform: translateX(6px); }
          60% { transform: translateX(-4px); }
          80% { transform: translateX(4px); }
        }
        .animate-shake { animation: shake 0.35s ease-in-out; }
      `}</style>
    </div>
  )
}
