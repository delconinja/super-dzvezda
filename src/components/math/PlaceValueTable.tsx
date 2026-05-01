'use client'

// Column config: label, short label, color
const COLS = [
  { label: 'Сто илјади', short: 'СИ', color: '#F59E42', textColor: '#7A4A00' },
  { label: 'Дес. илјади', short: 'ДИ', color: '#FBBF24', textColor: '#7A4A00' },
  { label: 'Ед. илјади', short: 'ЕИ', color: '#FDE68A', textColor: '#7A4A00' },
  { label: 'Стотки',     short: 'С',  color: '#86EFAC', textColor: '#14532D' },
  { label: 'Десетки',    short: 'Д',  color: '#6EE7B7', textColor: '#064E3B' },
  { label: 'Единици',    short: 'Е',  color: '#5EEAD4', textColor: '#134E4A' },
]

interface Props {
  number: number
  highlightCol?: number  // 0=СИ … 5=Е
  compact?: boolean
}

export default function PlaceValueTable({ number, highlightCol, compact = false }: Props) {
  const digits = String(number).padStart(6, ' ').split('').map(d => d.trim())

  const cellH = compact ? 36 : 44
  const headerH = compact ? 26 : 32
  const fontSize = compact ? 11 : 12
  const digitSize = compact ? 18 : 22

  const totalW = 300
  const colW = totalW / 6

  return (
    <svg width="100%" viewBox={`0 0 ${totalW} ${headerH + cellH}`}
      style={{ maxWidth: 340, borderRadius: 10, overflow: 'hidden' }}>

      {COLS.map((col, i) => {
        const x = i * colW
        const isHighlighted = highlightCol === i
        const digit = digits[i] || ''

        return (
          <g key={i}>
            {/* Header cell */}
            <rect x={x} y={0} width={colW} height={headerH}
              fill={col.color}
              opacity={isHighlighted ? 1 : 0.65}
            />
            <text x={x + colW / 2} y={headerH / 2 + fontSize * 0.38}
              textAnchor="middle" fontSize={fontSize} fontFamily="sans-serif"
              fontWeight={700} fill={col.textColor}>
              {col.short}
            </text>

            {/* Digit cell */}
            <rect x={x} y={headerH} width={colW} height={cellH}
              fill={isHighlighted ? col.color : 'white'}
              opacity={isHighlighted ? 0.35 : 1}
              stroke="#E5E7EB" strokeWidth={0.5}
            />
            <text x={x + colW / 2} y={headerH + cellH / 2 + digitSize * 0.38}
              textAnchor="middle" fontSize={digitSize} fontFamily="sans-serif"
              fontWeight={800} fill={isHighlighted ? col.textColor : '#1A1A2E'}>
              {digit}
            </text>

            {/* Column divider */}
            {i > 0 && (
              <line x1={x} y1={0} x2={x} y2={headerH + cellH}
                stroke="#D1D5DB" strokeWidth={0.8} />
            )}

            {/* Highlight outline */}
            {isHighlighted && (
              <rect x={x + 1} y={1} width={colW - 2} height={headerH + cellH - 2}
                fill="none" stroke={col.color} strokeWidth={2.5}
                rx={2} opacity={0.9}
              />
            )}
          </g>
        )
      })}

      {/* Outer border */}
      <rect x={0} y={0} width={totalW} height={headerH + cellH}
        fill="none" stroke="#D1D5DB" strokeWidth={1} rx={2} />
    </svg>
  )
}
