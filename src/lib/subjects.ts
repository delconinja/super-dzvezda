import { Subject } from '@/types'

const ALL_SUBJECTS: (Subject & { grades: number[] })[] = [
  {
    id: 'math',
    name: 'Mathematics',
    nameMk: 'Математика',
    world: 'Кристални пештери',
    color: '#5C35D4',
    bgColor: '#EDE9FF',
    emoji: '🔮',
    unitsCount: 4,
    grades: [5, 6, 7, 8, 9],
  },
  {
    id: 'mk',
    name: 'Macedonian Language',
    nameMk: 'Македонски јазик',
    world: 'Зборовен свет',
    color: '#E84393',
    bgColor: '#FFE8F5',
    emoji: '📖',
    unitsCount: 7,
    grades: [5, 6],
  },
  {
    id: 'science',
    name: 'Natural Sciences',
    nameMk: 'Природни науки',
    world: 'Планетата Земја',
    color: '#6BCB77',
    bgColor: '#E8F8EA',
    emoji: '🌍',
    unitsCount: 5,
    grades: [5, 6],
  },
  {
    id: 'biology',
    name: 'Biology',
    nameMk: 'Биологија',
    world: 'Џунгла свет',
    color: '#6BCB77',
    bgColor: '#E8F8EA',
    emoji: '🌿',
    unitsCount: 4,
    grades: [7, 8, 9],
  },
  {
    id: 'chemistry',
    name: 'Chemistry',
    nameMk: 'Хемија',
    world: 'Вулкан лаб',
    color: '#FF6B6B',
    bgColor: '#FFE8E8',
    emoji: '⚗️',
    unitsCount: 4,
    grades: [7, 8, 9],
  },
]

export const SUBJECTS: Subject[] = ALL_SUBJECTS

export function getSubjectsForGrade(grade: number): Subject[] {
  return ALL_SUBJECTS.filter((s) => s.grades.includes(grade))
}

export const getSubject = (id: string) =>
  ALL_SUBJECTS.find((s) => s.id === id)
