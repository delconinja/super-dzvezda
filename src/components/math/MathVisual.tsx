'use client'

import NumberLine from './NumberLine'
import PlaceValueTable from './PlaceValueTable'
import FractionBar from './FractionBar'
import FractionCircle from './FractionCircle'
import RectangleShape from './RectangleShape'

export interface VisualProps {
  type: 'number-line' | 'place-value' | 'fraction-bar' | 'fraction-circle' | 'rectangle'
  // number-line
  min?: number
  max?: number
  step?: number
  markers?: number[]
  highlightRange?: [number, number]
  // place-value
  number?: number
  highlightCol?: number
  compact?: boolean
  // fraction
  numerator?: number
  denominator?: number
  // rectangle
  width?: number
  height?: number
  unit?: string
  showArea?: boolean
  isSquare?: boolean
  // shared
  color?: string
}

export default function MathVisual({ type, color, ...props }: VisualProps) {
  const c = color || '#5C35D4'

  if (type === 'number-line') return (
    <NumberLine
      min={props.min ?? -5}
      max={props.max ?? 5}
      step={props.step ?? 1}
      markers={props.markers}
      highlightRange={props.highlightRange}
      color={c}
    />
  )

  if (type === 'place-value') return (
    <PlaceValueTable
      number={props.number ?? 0}
      highlightCol={props.highlightCol}
      compact={props.compact}
    />
  )

  if (type === 'fraction-bar') return (
    <FractionBar
      numerator={props.numerator ?? 1}
      denominator={props.denominator ?? 4}
      color={c}
    />
  )

  if (type === 'fraction-circle') return (
    <FractionCircle
      numerator={props.numerator ?? 1}
      denominator={props.denominator ?? 4}
      color={c}
    />
  )

  if (type === 'rectangle') return (
    <RectangleShape
      width={props.width ?? 10}
      height={props.height ?? 5}
      unit={props.unit ?? 'cm'}
      color={c}
      showArea={props.showArea}
      isSquare={props.isSquare}
    />
  )

  return null
}
