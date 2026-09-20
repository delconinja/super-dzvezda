'use client'

// SVG circular pie (pizza). N equal slices, M shaded.
// Optional onTap per slice for interactivity.

interface PieProps {
  parts: number
  shadedIndices: Set<number>      // which slice indices are "shaded" / topping
  onTapSlice?: (index: number) => void
  size?: number
  pulseIndex?: number             // pulse a single slice (e.g. invitation to tap)
  crustColor?: string
  toppingColor?: string
  doughColor?: string
}

export function Pie({
  parts,
  shadedIndices,
  onTapSlice,
  size = 260,
  pulseIndex,
  crustColor = '#92400E',
  toppingColor = '#DC2626',
  doughColor = '#FEF3C7',
}: PieProps) {
  const cx = size / 2
  const cy = size / 2
  const r = size / 2 - 6
  const interactive = !!onTapSlice

  const sliceFor = (i: number) => {
    const startA = (i / parts) * 2 * Math.PI - Math.PI / 2
    const endA = ((i + 1) / parts) * 2 * Math.PI - Math.PI / 2
    const x1 = cx + r * Math.cos(startA)
    const y1 = cy + r * Math.sin(startA)
    const x2 = cx + r * Math.cos(endA)
    const y2 = cy + r * Math.sin(endA)
    const largeArc = endA - startA > Math.PI ? 1 : 0
    if (parts === 1) {
      // whole circle
      return `M ${cx - r},${cy} a ${r},${r} 0 1,0 ${r * 2},0 a ${r},${r} 0 1,0 -${r * 2},0`
    }
    return `M ${cx},${cy} L ${x1},${y1} A ${r},${r} 0 ${largeArc},1 ${x2},${y2} Z`
  }

  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      {/* outer crust */}
      <circle cx={cx} cy={cy} r={r + 4} fill={crustColor} />

      {Array.from({ length: parts }).map((_, i) => {
        const isShaded = shadedIndices.has(i)
        const isPulse = pulseIndex === i
        return (
          <path
            key={i}
            d={sliceFor(i)}
            fill={isShaded ? toppingColor : doughColor}
            stroke="#92400E"
            strokeWidth={2}
            onClick={() => onTapSlice?.(i)}
            style={{
              cursor: interactive ? 'pointer' : 'default',
              transition: 'fill 250ms ease-out',
              transformOrigin: `${cx}px ${cy}px`,
              animation: isPulse ? 'pulse-slice 1.2s ease-in-out infinite' : undefined,
            }}
          />
        )
      })}

      <style>{`
        @keyframes pulse-slice {
          0%,100% { opacity: 1; }
          50% { opacity: 0.65; }
        }
      `}</style>
    </svg>
  )
}
