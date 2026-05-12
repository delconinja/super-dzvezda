import type { ExerciseData, LessonData, NarrationCue } from './content'

// ── V2 Flow Block Types ───────────────────────────────────────────

export interface VideoInteractionPoint {
  time: number
  pause: boolean
  type: 'multiple_choice'
  question: string
  options: string[]
  correctAnswer: string
  explanation: string
}

export interface VideoFlowBlock {
  type: 'video'
  provider: 'youtube' | 'local'
  url: string
  interactionPoints?: VideoInteractionPoint[]
  narration?: NarrationCue[]
}

export interface ConceptFlowBlock {
  type: 'concept_blocks'
  blocks: Array<{ type: 'text'; content: string }>
}

export interface GuidedPracticeBlock {
  type: 'guided_practice'
  exercises: ExerciseData[]
}

export interface QuizBlock {
  type: 'quiz'
  mode: 'mastery_check'
  passingScore: number
  questions: ExerciseData[]
}

export interface SummaryBlock {
  type: 'summary'
  content: string
}

export type LessonFlowBlock =
  | VideoFlowBlock
  | ConceptFlowBlock
  | GuidedPracticeBlock
  | QuizBlock
  | SummaryBlock

export interface LessonDataV2 {
  id: string
  title: string
  order: number
  learningObjectives: string[]
  lessonFlow: LessonFlowBlock[]
  xpReward: number
  unlockNext: boolean
  isTest?: boolean
  isChallenge?: boolean
}

// ── Converter: LessonData (V1) → LessonDataV2 ────────────────────

export function convertToV2(lesson: LessonData, index = 0): LessonDataV2 {
  const flow: LessonFlowBlock[] = []

  if (lesson.videoUrl) {
    flow.push({
      type: 'video',
      provider: 'local',
      url: lesson.videoUrl,
      interactionPoints: lesson.videoQuizzes?.map(vq => ({
        time: vq.timestamp,
        pause: true,
        type: 'multiple_choice' as const,
        question: vq.question,
        options: vq.options,
        correctAnswer: vq.correctAnswer,
        explanation: '',
      })),
      narration: lesson.videoNarration,
    })
  }

  if (lesson.content) {
    flow.push({
      type: 'concept_blocks',
      blocks: [{ type: 'text', content: lesson.content }],
    })
  }

  const exercises = lesson.exercises ?? []
  const quizCount = exercises.length >= 4 ? 2 : exercises.length >= 2 ? 1 : 0
  const practiceExercises = exercises.slice(0, exercises.length - quizCount)
  const quizExercises = exercises.slice(exercises.length - quizCount)

  if (practiceExercises.length > 0) {
    flow.push({ type: 'guided_practice', exercises: practiceExercises })
  }

  if (quizExercises.length > 0) {
    flow.push({ type: 'quiz', mode: 'mastery_check', passingScore: 80, questions: quizExercises })
  }

  const summaryTitle =
    lesson.content?.split('\n').find(line => line.startsWith('## '))?.replace('## ', '') ??
    lesson.title

  flow.push({ type: 'summary', content: summaryTitle })

  return {
    id: lesson.id,
    title: lesson.title,
    order: index + 1,
    learningObjectives: [],
    lessonFlow: flow,
    xpReward: 50,
    unlockNext: !lesson.isTest,
    isTest: lesson.isTest,
    isChallenge: lesson.isChallenge,
  }
}

// ── Accessors ────────────────────────────────────────────────────

export function v2GetPracticeCount(lesson: LessonDataV2): number {
  const b = lesson.lessonFlow.find(b => b.type === 'guided_practice') as GuidedPracticeBlock | undefined
  return b?.exercises.length ?? 0
}

export function v2GetQuizBlock(lesson: LessonDataV2): QuizBlock | undefined {
  return lesson.lessonFlow.find(b => b.type === 'quiz') as QuizBlock | undefined
}
