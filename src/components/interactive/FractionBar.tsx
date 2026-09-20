'use client'

// Pure SVG fraction bar.
// Renders N parts; some shaded. Optionally interactive (tap to toggle).

interface Props {
  parts: number
  shaded: number              // initial / displayed shaded count
  onTap?: (index: number) => void
  interactiveIndices?: Set<number>  // which indices are visually "shaded" in interactive mode
  width?: number
  height?: number
  showLabel?: boolean
}

export function FractionBar({
  parts,
  shaded,
  onTap,
  interactiveIndices,
  width = 360,
  height = 80,
  showLabel = true,
}: Props) {
  const partWidth = width / parts
  const isInteractive = !!onTap

  // In interactive mode, we read from interactiveIndices instead of `shaded`
  const isShaded = (i: number): boolean => {
    if (interactiveIndices) return interactiveIndices.has(i)
    return i < shaded
  }

  const shadedCount = interactiveIndices ? interactiveIndices.size : shaded

  return (
    <div className="flex flex-col items-center gap-2 select-none">
      <svg
        width={width}
        height={height}
        viewBox={`0 0 ${width} ${height}`}
        role="img"
        aria-label={`Fraction bar ${shadedCount} of ${parts}`}
      >
        {Array.from({ length: parts }).map((_, i) => {
          const filled = isShaded(i)
          return (
            <rect
              key={i}
              x={i * partWidth}
              y={0}
              width={partWidth}
              height={height}
              fill={filled ? '#5C35D4' : '#F4F1FF'}
              stroke="#3A1F8C"
              strokeWidth={2}
              onClick={() => onTap?.(i)}
              style={{
                cursor: isInteractive ? 'pointer' : 'default',
                transition: 'fill 200ms ease-out',
              }}
            />
          )
        })}
      </svg>
      {showLabel && (
        <div className="text-2xl font-semibold tabular-nums text-slate-800">
          {shadedCount}
          <span className="text-slate-400 mx-1">/</span>
          {parts}
        </div>
      )}
    </div>
  )
}
