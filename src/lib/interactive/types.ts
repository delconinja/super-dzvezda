// Spec types for interactive (Synthesis-style) lessons.
// In production, the OpenAI agent generates these from the BRO corpus.

export type WidgetType =
  | 'fraction-bar'
  | 'fraction-pair'
  | 'tap-shade'
  | 'identify'
  | 'pizza-pick'
  | 'splittable-pie'

export interface FractionBarConfig {
  parts: number
  shaded: number
  label?: string
}

export interface TapShadeConfig {
  parts: number
  target: number
}

export interface IdentifyChoice {
  parts: number
  shaded: number
  isCorrect: boolean
  shape?: 'bar' | 'pie'   // visual style of the choice
}

export interface IdentifyConfig {
  question: string
  choices: IdentifyChoice[]
  shape?: 'bar' | 'pie'   // default shape for all choices
}

export interface FractionPairConfig {
  left: { parts: number; shaded: number }
  right: { parts: number; shaded: number }
}

export interface SplittablePieConfig {
  startParts: number
  startShaded: number
  finalParts: number
  compareTo?: { parts: number; shaded: number }
}

export type WidgetConfig =
  | { type: 'fraction-bar'; config: FractionBarConfig }
  | { type: 'tap-shade'; config: TapShadeConfig }
  | { type: 'identify'; config: IdentifyConfig }
  | { type: 'fraction-pair'; config: FractionPairConfig }
  | { type: 'splittable-pie'; config: SplittablePieConfig }

// A single narration beat — line the tutor says at a specific moment.
// `trigger` says when it plays: 'enter' (on scene load), 'on-progress'
// (after first interaction), 'on-success', 'on-wrong'.
export interface NarrationBeat {
  trigger: 'enter' | 'on-progress' | 'on-success' | 'on-wrong' | 'on-hint'
  text: string
}

export interface Scene {
  id: string
  narration: NarrationBeat[]  // tutor speaks throughout
  prompt?: string             // visible instruction on screen
  widget: WidgetConfig
  hint?: string
  successMessage?: string
}

export interface InteractiveLessonSpec {
  lessonId: string
  title: string
  bro_topic: string
  scenes: Scene[]
}
