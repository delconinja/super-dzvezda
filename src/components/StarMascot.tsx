'use client'

import { useEffect, useState } from 'react'

export type StarMood = 'calm' | 'energetic' | 'talking'

interface Props {
  mood?: StarMood
  /** @deprecated use mood="talking" */
  talking?: boolean
  size?: number
  className?: string
}

const EYE_R = 8.5

export default function StarMascot({ mood: moodProp, talking, size = 64, className = '' }: Props) {
  const mood: StarMood = moodProp ?? (talking ? 'talking' : 'calm')

  const [blink, setBlink] = useState(false)
  const [mouthOpen, setMouthOpen] = useState(false)

  // Blink timer — not used while talking (mouth dominates attention)
  useEffect(() => {
    if (mood === 'talking') return
    const interval = mood === 'energetic' ? 2000 : 4500
    const id = setInterval(() => {
      setBlink(true)
      setTimeout(() => setBlink(false), 130)
    }, interval)
    return () => clearInterval(id)
  }, [mood])

  // Talking mouth
  useEffect(() => {
    if (mood !== 'talking') { setMouthOpen(false); return }
    const id = setInterval(() => setMouthOpen(m => !m), 220)
    return () => clearInterval(id)
  }, [mood])

  const wrapClass =
    mood === 'calm'      ? 'star-mascot-calm'      :
    mood === 'energetic' ? 'star-mascot-energetic'  :
                           'star-mascot-talk'

  const eyeRy = blink ? EYE_R * 0.07 : EYE_R

  // viewBox: x [-60,60], y [-78,60] → 120 wide, 138 tall
  const vbW = 120, vbH = 138
  const aspect = vbH / vbW // ~1.15

  return (
    <div className={`${wrapClass} ${className}`}
      style={{ display: 'inline-block', width: size, height: size * aspect, lineHeight: 0 }}>
      <svg viewBox={`-60 -78 ${vbW} ${vbH}`} width={size} height={size * aspect}>
        <defs>
          <radialGradient id="sm-body" cx="35%" cy="25%" r="70%">
            <stop offset="0%"   stopColor="#FFEE88" />
            <stop offset="50%"  stopColor="#FFD000" />
            <stop offset="100%" stopColor="#F59E0B" />
          </radialGradient>
        </defs>

        {/* ── GRADUATION CAP ── */}
        {/* cylindrical body sitting on the top star point (0, -55) */}
        <rect x="-9" y="-72" width="18" height="18" rx="3" fill="#5C35D4" />
        {/* flat mortarboard */}
        <rect x="-20" y="-72" width="40" height="6" rx="2.5" fill="#7B5CE5" />
        {/* tassel cord */}
        <line x1="20" y1="-69" x2="28" y2="-56" stroke="#FFD700" strokeWidth="2.2" strokeLinecap="round" />
        {/* tassel ball */}
        <circle cx="28" cy="-53" r="3.5" fill="#FFD700" />

        {/* ── STAR GLOW HALO ── */}
        <path
          d="M0,-55 L12.9,-17.8 L52.3,-17 L20.9,6.8 L32.3,44.5 L0,22 L-32.3,44.5 L-20.9,6.8 L-52.3,-17 L-12.9,-17.8 Z"
          fill="#FFE566" opacity="0.32" transform="scale(1.12)"
        />

        {/* ── STAR BODY ── */}
        <path
          d="M0,-55 L12.9,-17.8 L52.3,-17 L20.9,6.8 L32.3,44.5 L0,22 L-32.3,44.5 L-20.9,6.8 L-52.3,-17 L-12.9,-17.8 Z"
          fill="url(#sm-body)" stroke="#E0A000" strokeWidth="1.8" strokeLinejoin="round"
        />

        {/* ── FACE ── */}
        {/* Left eye */}
        <ellipse cx="-16" cy="-8" rx={EYE_R} ry={eyeRy} fill="white" />
        {!blink && <>
          <circle cx="-14" cy="-7"  r="4.8" fill="#1A1A2E" />
          <circle cx="-11" cy="-11" r="2"   fill="white" />
        </>}

        {/* Right eye */}
        <ellipse cx="16" cy="-8" rx={EYE_R} ry={eyeRy} fill="white" />
        {!blink && <>
          <circle cx="18" cy="-7"  r="4.8" fill="#1A1A2E" />
          <circle cx="21" cy="-11" r="2"   fill="white" />
        </>}

        {/* Cheeks */}
        <circle cx="-27" cy="4" r="8" fill={mood === 'energetic' ? '#FFB800' : '#FFB3B3'} opacity="0.48" />
        <circle cx="27"  cy="4" r="8" fill={mood === 'energetic' ? '#FFB800' : '#FFB3B3'} opacity="0.48" />

        {/* Mouth */}
        {mood === 'talking' && mouthOpen ? (
          <g>
            <ellipse cx="0" cy="16" rx="11" ry="8" fill="#C0392B" />
            <rect x="-8" y="12" width="16" height="4" fill="white" rx="1.5" />
          </g>
        ) : mood === 'energetic' ? (
          <path d="M-14,10 Q0,27 14,10" stroke="#B8860B" strokeWidth="3.2" fill="none" strokeLinecap="round" />
        ) : (
          <path d="M-11,12 Q0,22 11,12" stroke="#1A1A2E" strokeWidth="3"   fill="none" strokeLinecap="round" />
        )}

        {/* ── CALM SPARKLES ── */}
        {mood === 'calm' && <>
          <text className="spark-calm-1" x="57"  y="-30" fontSize="11" fill="#FFD700" textAnchor="middle">✦</text>
          <text className="spark-calm-2" x="-57" y="-14" fontSize="9"  fill="#FFD700" textAnchor="middle">✦</text>
          <text className="spark-calm-3" x="52"  y="46"  fontSize="8"  fill="#FFD700" textAnchor="middle">✦</text>
        </>}

        {/* ── ENERGETIC SPARKLES ── */}
        {mood === 'energetic' && <>
          <text className="spark-e-1" x="58"  y="-28" fontSize="14" textAnchor="middle">⭐</text>
          <text className="spark-e-2" x="-58" y="-16" fontSize="11" textAnchor="middle">✨</text>
          <text className="spark-e-3" x="55"  y="46"  fontSize="13" textAnchor="middle">⭐</text>
          <text className="spark-e-4" x="-54" y="44"  fontSize="10" textAnchor="middle">✨</text>
        </>}
      </svg>
    </div>
  )
}
