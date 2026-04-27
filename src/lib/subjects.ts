import { Subject } from '@/types'

export const SUBJECTS: Subject[] = [
  {
    id: 'math',
    name: 'Mathematics',
    nameMk: 'Математика',
    world: 'Кристални пештери',
    color: '#5C35D4',
    bgColor: '#EDE9FF',
    emoji: '🔮',
    unitsCount: 4,
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
  },
]

export const getSubject = (id: string) =>
  SUBJECTS.find((s) => s.id === id)
