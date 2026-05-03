'use client'

interface Props {
  width: number   // display label (actual dimension)
  height: number
  unit?: string
  color?: string
  showArea?: boolean
  isSquare?: boolean
}

export default function RectangleShape({
  width, height, unit = 'cm', color = '#5C35D4', showArea = false, isSquare = false,
}: Props) {
  const svgW = 240
  const svgH = 130

  // Scale to fit nicely
  const aspect = width / height
  let rW = 160, rH = 80
  if (aspect > 2) { rW = 180; rH = 60 }
  if (aspect < 0.6) { rW = 80; rH = 110 }
  if (isSquare) { rW = 100; rH = 100 }

  const rX = (svgW - rW) / 2
  const rY = (svgH - rH) / 2

  const areaVal = width * height

  return (
    <svg width="100%" viewBox={`0 0 ${svgW} ${svgH}`} style={{ maxWidth: 280 }}>
      {/* Rectangle fill */}
      <rect x={rX} y={rY} width={rW} height={rH}
        fill={`${color}18`} stroke={color} strokeWidth={2} rx={3} />

      {/* Width label (top) */}
      <text x={rX + rW / 2} y={rY - 8}
        textAnchor="middle" fontSize={13} fontFamily="sans-serif"
        fontWeight={700} fill={color}>
        {width} {unit}
      </text>

      {/* Height label (right side) */}
      <text x={rX + rW + 10} y={rY + rH / 2 + 5}
        textAnchor="start" fontSize={13} fontFamily="sans-serif"
        fontWeight={700} fill={color}>
        {height} {unit}
      </text>

      {/* Area label inside */}
      {showArea && (
        <text x={rX + rW / 2} y={rY + rH / 2 + 6}
          textAnchor="middle" fontSize={14} fontFamily="sans-serif"
          fontWeight={800} fill={color} opacity={0.6}>
          {areaVal} {unit}²
        </text>
      )}

      {/* Dimension arrows */}
      {/* Top arrow */}
      <line x1={rX} y1={rY - 4} x2={rX + rW} y2={rY - 4}
        stroke={color} strokeWidth={1} opacity={0.4} />
      {/* Right arrow */}
      <line x1={rX + rW + 4} y1={rY} x2={rX + rW + 4} y2={rY + rH}
        stroke={color} strokeWidth={1} opacity={0.4} />
    </svg>
  )
}
