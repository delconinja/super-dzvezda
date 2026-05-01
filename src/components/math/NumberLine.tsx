'use client'

interface Props {
  min: number
  max: number
  step?: number
  markers?: number[]
  highlightRange?: [number, number]
  color?: string
  showArrows?: boolean
}

export default function NumberLine({
  min, max, step = 1, markers = [], highlightRange, color = '#5C35D4', showArrows = true,
}: Props) {
  const W = 300
  const H = 72
  const padL = 24
  const padR = 24
  const lineY = 36
  const tickH = 8
  const range = max - min
  const lineW = W - padL - padR

  const toX = (n: number) => padL + ((n - min) / range) * lineW

  const ticks: number[] = []
  for (let i = min; i <= max; i += step) ticks.push(i)

  return (
    <svg width="100%" viewBox={`0 0 ${W} ${H}`} style={{ overflow: 'visible', maxWidth: 340 }}>
      {/* Highlight range */}
      {highlightRange && (
        <rect
          x={toX(highlightRange[0])}
          y={lineY - 6}
          width={toX(highlightRange[1]) - toX(highlightRange[0])}
          height={12}
          fill={color}
          opacity={0.18}
          rx={4}
        />
      )}

      {/* Main line */}
      <line x1={padL} y1={lineY} x2={W - padR} y2={lineY}
        stroke="#2D2D44" strokeWidth={2} strokeLinecap="round" />

      {/* Arrows */}
      {showArrows && (
        <>
          <polygon points={`${padL - 2},${lineY} ${padL + 9},${lineY - 4} ${padL + 9},${lineY + 4}`}
            fill="#2D2D44" />
          <polygon points={`${W - padR + 2},${lineY} ${W - padR - 9},${lineY - 4} ${W - padR - 9},${lineY + 4}`}
            fill="#2D2D44" />
        </>
      )}

      {/* Ticks and labels */}
      {ticks.map((n) => (
        <g key={n}>
          <line x1={toX(n)} y1={lineY - tickH} x2={toX(n)} y2={lineY + tickH}
            stroke="#2D2D44" strokeWidth={1.5} />
          <text x={toX(n)} y={lineY + tickH + 13}
            textAnchor="middle" fontSize={10} fontFamily="sans-serif"
            fill="#2D2D44" fontWeight={n === 0 ? 700 : 400}>
            {n}
          </text>
        </g>
      ))}

      {/* Markers (colored dots) */}
      {markers.map((n, i) => (
        <circle key={i} cx={toX(n)} cy={lineY} r={6}
          fill={color} stroke="white" strokeWidth={2} />
      ))}
    </svg>
  )
}
