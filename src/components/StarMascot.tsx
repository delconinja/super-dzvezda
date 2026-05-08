'use client'

import { useEffect, useState } from 'react'

interface Props {
  talking: boolean
  size?: number
}

export default function StarMascot({ talking, size = 64 }: Props) {
  const [mouthOpen, setMouthOpen] = useState(false)

  useEffect(() => {
    if (!talking) { setMouthOpen(false); return }
    const id = setInterval(() => setMouthOpen((m) => !m), 220)
    return () => clearInterval(id)
  }, [talking])

  return (
    <div
      style={{ width: size, height: size }}
      className={talking ? 'star-mascot-talk' : 'star-mascot-idle'}
    >
      <svg viewBox="-60 -60 120 120" width={size} height={size}>
        {/* Outer glow layer */}
        <path
          d="M0,-55 L12.9,-17.8 L52.3,-17 L20.9,6.8 L32.3,44.5 L0,22 L-32.3,44.5 L-20.9,6.8 L-52.3,-17 L-12.9,-17.8 Z"
          fill="#FFE566"
          opacity="0.35"
          transform="scale(1.13)"
        />
        {/* Star body */}
        <path
          d="M0,-55 L12.9,-17.8 L52.3,-17 L20.9,6.8 L32.3,44.5 L0,22 L-32.3,44.5 L-20.9,6.8 L-52.3,-17 L-12.9,-17.8 Z"
          fill="#FFD93D"
          stroke="#F0B800"
          strokeWidth="2"
        />
        {/* Left eye */}
        <circle cx="-16" cy="-8" r="8.5" fill="white" />
        <circle cx="-14" cy="-7" r="4.8" fill="#1A1A2E" />
        <circle cx="-11" cy="-11" r="2" fill="white" />
        {/* Right eye */}
        <circle cx="16" cy="-8" r="8.5" fill="white" />
        <circle cx="18" cy="-7" r="4.8" fill="#1A1A2E" />
        <circle cx="21" cy="-11" r="2" fill="white" />
        {/* Cheeks */}
        <circle cx="-26" cy="4" r="8" fill="#FFB3B3" opacity="0.55" />
        <circle cx="26"  cy="4" r="8" fill="#FFB3B3" opacity="0.55" />
        {/* Mouth */}
        {mouthOpen ? (
          <g>
            <ellipse cx="0" cy="16" rx="11" ry="8" fill="#C0392B" />
            <rect x="-8" y="12" width="16" height="4" fill="white" rx="1.5" />
          </g>
        ) : (
          <path
            d="M-11,12 Q0,22 11,12"
            stroke="#1A1A2E"
            strokeWidth="3"
            fill="none"
            strokeLinecap="round"
          />
        )}
      </svg>
    </div>
  )
}
