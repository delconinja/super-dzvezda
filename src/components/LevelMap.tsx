'use client'

import { useRef, useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { Subject } from '@/types'

const WAVE_XPCT = [50, 67, 78, 67, 50, 33, 22, 33]
const ROW_H = 130
const PAD_V = 70
const NODE_R = 34
const BOSS_R = 42
const GIFT_R = 28

export type MapNode = {
  id: string
  title: string
  type: 'lesson' | 'boss' | 'gift'
  lessonId?: string
  unitId?: string
  unitTitle?: string  // shown as label for first node of each unit
  stars: number
  locked: boolean
}

interface Props {
  nodes: MapNode[]
  subject: Subject
}

export default function LevelMap({ nodes, subject }: Props) {
  const router = useRouter()
  const containerRef = useRef<HTMLDivElement>(null)
  const [cW, setCW] = useState(340)

  useEffect(() => {
    const update = () => {
      if (containerRef.current) setCW(containerRef.current.offsetWidth)
    }
    update()
    window.addEventListener('resize', update)
    return () => window.removeEventListener('resize', update)
  }, [])

  const totalH = PAD_V + nodes.length * ROW_H + PAD_V

  function xOf(i: number): number {
    const node = nodes[i]
    if (node.type === 'boss' || node.type === 'gift') return cW / 2
    return cW * (WAVE_XPCT[i % WAVE_XPCT.length] / 100)
  }

  function yOf(i: number): number {
    return PAD_V + i * ROW_H
  }

  function rOf(i: number): number {
    const type = nodes[i].type
    if (type === 'boss') return BOSS_R
    if (type === 'gift') return GIFT_R
    return NODE_R
  }

  function handleClick(node: MapNode) {
    if (node.locked) return
    if (node.type === 'gift') return
    if (node.type === 'boss' && node.unitId) {
      router.push(`/challenge/${node.unitId}`)
    } else if (node.lessonId) {
      router.push(`/lesson/${node.lessonId}`)
    }
  }

  // Build SVG bezier segments between consecutive nodes
  const segments = nodes.slice(0, -1).map((node, i) => {
    const x1 = xOf(i), y1 = yOf(i)
    const x2 = xOf(i + 1), y2 = yOf(i + 1)
    const midY = (y1 + y2) / 2
    const done = node.stars > 0 || node.type === 'gift'
    return {
      d: `M ${x1} ${y1} C ${x1} ${midY}, ${x2} ${midY}, ${x2} ${y2}`,
      done,
    }
  })

  return (
    <div ref={containerRef} style={{ position: 'relative', width: '100%', height: totalH }}>
      {/* Winding path lines */}
      <svg
        style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: totalH, pointerEvents: 'none', overflow: 'visible' }}
        viewBox={`0 0 ${cW} ${totalH}`}
        preserveAspectRatio="none"
      >
        {segments.map((seg, i) => (
          <path
            key={i}
            d={seg.d}
            fill="none"
            stroke={seg.done ? subject.color : '#D1D5DB'}
            strokeWidth={5}
            strokeDasharray={seg.done ? undefined : '10 8'}
            strokeLinecap="round"
            opacity={0.5}
          />
        ))}
      </svg>

      {/* Nodes */}
      {nodes.map((node, i) => {
        const x = xOf(i)
        const y = yOf(i)
        const r = rOf(i)
        const done = node.stars > 0
        const isActive = !node.locked && !done && node.type !== 'gift'
        const isBoss = node.type === 'boss'
        const isGift = node.type === 'gift'
        const isRight = x > cW / 2

        const circleBg = node.locked
          ? '#E5E7EB'
          : isGift
          ? '#FFD93D'
          : isBoss
          ? 'linear-gradient(135deg, #7B5CE5, #A855F7)'
          : subject.color

        const icon = node.locked
          ? '🔒'
          : isGift
          ? '🎁'
          : isBoss
          ? '👾'
          : done
          ? '✓'
          : '▶'

        const labelX = isRight ? x + r + 10 : x - r - 10
        const labelAlign: React.CSSProperties['textAlign'] = isRight ? 'left' : 'right'
        const labelW = Math.min(cW * 0.35, 110)

        return (
          <div key={node.id}>
            {/* Unit title label above first node of each unit */}
            {node.unitTitle && (
              <div
                style={{
                  position: 'absolute',
                  left: x,
                  top: y - r - 28,
                  transform: 'translateX(-50%)',
                  fontSize: 10,
                  fontWeight: 900,
                  color: subject.color,
                  textAlign: 'center',
                  letterSpacing: '0.05em',
                  textTransform: 'uppercase',
                  whiteSpace: 'nowrap',
                  maxWidth: cW * 0.7,
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  pointerEvents: 'none',
                }}
              >
                {node.unitTitle}
              </div>
            )}

            {/* Circle button */}
            <div
              onClick={() => handleClick(node)}
              style={{
                position: 'absolute',
                left: x,
                top: y,
                transform: 'translate(-50%, -50%)',
                width: r * 2,
                height: r * 2,
                borderRadius: '50%',
                background: circleBg,
                border: `4px solid ${node.locked ? '#D1D5DB' : isGift ? '#F59E0B' : isBoss ? '#5C35D4' : done ? 'white' : 'white'}`,
                boxShadow: isActive
                  ? `0 0 0 6px ${subject.color}22, 0 4px 20px ${subject.color}50`
                  : isBoss && !node.locked
                  ? '0 4px 20px #7B5CE550'
                  : 'none',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: r * 0.65,
                color: node.locked ? '#9CA3AF' : 'white',
                fontWeight: 900,
                cursor: node.locked || isGift ? 'default' : 'pointer',
                transition: 'transform 0.15s',
                zIndex: 1,
              }}
              onMouseEnter={e => {
                if (!node.locked && !isGift) (e.currentTarget as HTMLDivElement).style.transform = 'translate(-50%, -50%) scale(1.08)'
              }}
              onMouseLeave={e => {
                (e.currentTarget as HTMLDivElement).style.transform = 'translate(-50%, -50%) scale(1)'
              }}
            >
              {icon}
            </div>

            {/* Stars (lessons only) */}
            {!isGift && !isBoss && (
              <div
                style={{
                  position: 'absolute',
                  left: x,
                  top: y + r + 4,
                  transform: 'translateX(-50%)',
                  display: 'flex',
                  gap: 2,
                  pointerEvents: 'none',
                }}
              >
                {[1, 2, 3].map(s => (
                  <span key={s} style={{ fontSize: 10, color: s <= node.stars ? '#FFD93D' : '#E5E7EB' }}>★</span>
                ))}
              </div>
            )}

            {/* Side label */}
            <div
              style={{
                position: 'absolute',
                left: labelX,
                top: y,
                transform: 'translateY(-50%)',
                width: labelW,
                textAlign: labelAlign,
                fontSize: isGift || isBoss ? 12 : 11,
                fontWeight: isBoss ? 900 : 700,
                color: node.locked ? '#9CA3AF' : isBoss ? '#5C35D4' : isGift ? '#D97706' : '#1A1A2E',
                lineHeight: 1.3,
                pointerEvents: 'none',
              }}
            >
              {isBoss ? 'ПРЕДИЗВИК' : isGift ? 'Награда!' : node.title}
            </div>
          </div>
        )
      })}
    </div>
  )
}
