export type Grade = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

export type SubjectId = 'math' | 'biology' | 'chemistry' | 'science' | 'mk' | 'history' | 'tech' | 'english' | 'enviro' | 'society' | 'german'

export interface Subject {
  id: SubjectId
  name: string
  nameMk: string
  world: string
  color: string
  bgColor: string
  emoji: string
  unitsCount: number
  grades?: number[]
  flagCode?: string
}

export interface Unit {
  id: string
  subjectId: SubjectId
  grade: Grade
  title: string
  order: number
  lessonsCount: number
}

export interface Lesson {
  id: string
  unitId: string
  title: string
  content: string
  order: number
  exercisesCount: number
}

export type ExerciseType = 'multiple-choice' | 'fill-in' | 'true-false'

export interface Exercise {
  id: string
  lessonId: string
  type: ExerciseType
  question: string
  options?: string[]
  correctAnswer: string
  explanation?: string
  order: number
}

export interface Student {
  id: string
  name: string
  grade: Grade
  starsTotal: number
  streak: number
  createdAt: string
}

export interface Progress {
  studentId: string
  lessonId: string
  completed: boolean
  starsEarned: number
  attempts: number
}
