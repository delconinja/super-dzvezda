'use client'

interface Props {
  a: number   // angle at bottom-left (degrees)
  b: number   // angle at bottom-right (degrees)
  // third angle c = 180 - a - b (auto-calculated)
  kind?: 'acute' | 'right' | 'obtuse'
  color?: string
  showAngles?: boolean
}

export default function TriangleShape({
  a, b, kind, color = '#5C35D4', showAngles = true,
}: Props) {
  const W = 240
  const H = 140
  const pad = 28
  const baseY = H - pad
  const x1 = pad
  const x2 = W - pad
  const baseLen = x2 - x1

  // Law of sines to find apex position
  const aRad = (a * Math.PI) / 180
  const bRad = (b * Math.PI) / 180
  const c = 180 - a - b
  const cRad = (c * Math.PI) / 180

  const t1 = (baseLen * Math.sin(bRad)) / Math.sin(cRad)
  const apexX = x1 + t1 * Math.cos(aRad)
  const apexY = baseY - t1 * Math.sin(aRad)

  // Clamp apex within viewbox
  const ax = Math.max(pad, Math.min(W - pad, apexX))
  const ay = Math.max(pad, Math.min(baseY - 20, apexY))

  const pts = `${x1},${baseY} ${x2},${baseY} ${ax},${ay}`

  // Color by type
  const kindColor = kind === 'right' ? '#8B5CF6'
    : kind === 'obtuse' ? '#10B981'
    : kind === 'acute' ? '#3B82F6'
    : color

  // Right angle box size
  const boxSize = 12

  return (
    <svg width="100%" viewBox={`0 0 ${W} ${H}`} style={{ maxWidth: 280 }}>
      {/* Triangle fill */}
      <polygon points={pts}
        fill={`${kindColor}18`}
        stroke={kindColor}
        strokeWidth={2}
        strokeLinejoin="round"
      />

      {/* Right angle box at bottom-left if a=90 */}
      {a === 90 && (
        <rect x={x1} y={baseY - boxSize} width={boxSize} height={boxSize}
          fill="none" stroke={kindColor} strokeWidth={1.5} />
      )}
      {/* Right angle box at bottom-right if b=90 */}
      {b === 90 && (
        <rect x={x2 - boxSize} y={baseY - boxSize} width={boxSize} height={boxSize}
          fill="none" stroke={kindColor} strokeWidth={1.5} />
      )}

      {/* Angle labels */}
      {showAngles && (
        <>
          {/* Bottom-left angle */}
          <text x={x1 + 14} y={baseY - 6}
            textAnchor="start" fontSize={11} fontFamily="sans-serif"
            fontWeight={700} fill={kindColor}>
            {a}°
          </text>
          {/* Bottom-right angle */}
          <text x={x2 - 14} y={baseY - 6}
            textAnchor="end" fontSize={11} fontFamily="sans-serif"
            fontWeight={700} fill={kindColor}>
            {b}°
          </text>
          {/* Apex angle */}
          <text x={ax} y={ay - 6}
            textAnchor="middle" fontSize={11} fontFamily="sans-serif"
            fontWeight={700} fill={kindColor}>
            {c}°
          </text>
        </>
      )}
    </svg>
  )
}
