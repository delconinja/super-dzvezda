'use client'

interface Props {
  numerator: number
  denominator: number
  color?: string
  size?: number
}

export default function FractionCircle({
  numerator, denominator, color = '#5C35D4', size = 90,
}: Props) {
  const cx = size / 2
  const cy = size / 2
  const r = size / 2 - 4

  const slices = Array.from({ length: denominator }).map((_, i) => {
    const startAngle = (i / denominator) * 2 * Math.PI - Math.PI / 2
    const endAngle = ((i + 1) / denominator) * 2 * Math.PI - Math.PI / 2
    const x1 = cx + r * Math.cos(startAngle)
    const y1 = cy + r * Math.sin(startAngle)
    const x2 = cx + r * Math.cos(endAngle)
    const y2 = cy + r * Math.sin(endAngle)
    const largeArc = denominator === 1 ? 1 : 0
    return { i, x1, y1, x2, y2, largeArc, filled: i < numerator }
  })

  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      {/* Background circle */}
      <circle cx={cx} cy={cy} r={r} fill="#F3F4F6" stroke="#D1D5DB" strokeWidth={1.5} />

      {/* Filled slices */}
      {slices.map(({ i, x1, y1, x2, y2, largeArc, filled }) => (
        filled && (
          <path key={i}
            d={`M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`}
            fill={color} opacity={0.85}
          />
        )
      ))}

      {/* Slice dividers */}
      {slices.map(({ i, x1, y1 }) => (
        <line key={`d${i}`} x1={cx} y1={cy} x2={x1} y2={y1}
          stroke="white" strokeWidth={1.5} />
      ))}

      {/* Outer ring */}
      <circle cx={cx} cy={cy} r={r} fill="none" stroke={color} strokeWidth={1.5} />
    </svg>
  )
}
