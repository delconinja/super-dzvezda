'use client'

interface Props {
  numerator: number
  denominator: number
  color?: string
  showLabel?: boolean
  width?: number
}

export default function FractionBar({
  numerator, denominator, color = '#5C35D4', showLabel = true, width = 280,
}: Props) {
  const H = 44
  const barH = 28
  const barY = 6
  const segW = (width - 20) / denominator
  const startX = 10

  return (
    <svg width="100%" viewBox={`0 0 ${width} ${H}`} style={{ maxWidth: 320 }}>
      {/* Segments */}
      {Array.from({ length: denominator }).map((_, i) => {
        const x = startX + i * segW
        const filled = i < numerator
        return (
          <g key={i}>
            <rect x={x + 1} y={barY} width={segW - 2} height={barH}
              fill={filled ? color : '#F3F4F6'}
              rx={i === 0 ? 4 : i === denominator - 1 ? 4 : 2}
              stroke={filled ? color : '#D1D5DB'}
              strokeWidth={1}
            />
          </g>
        )
      })}

      {/* Outer border */}
      <rect x={startX} y={barY} width={width - 20} height={barH}
        fill="none" stroke={color} strokeWidth={1.5} rx={4} />

      {/* Fraction label */}
      {showLabel && (
        <text x={width / 2} y={barY + barH + 14}
          textAnchor="middle" fontSize={13} fontFamily="sans-serif"
          fontWeight={700} fill={color}>
          {numerator}/{denominator}
        </text>
      )}
    </svg>
  )
}
