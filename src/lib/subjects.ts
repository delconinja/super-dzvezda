import { Subject, SubjectId } from '@/types'

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
    category: 'core',
    grades: [1, 2, 3, 4, 5, 6, 7, 8, 9],
  },
  {
    id: 'mk',
    name: 'Macedonian Language',
    nameMk: 'Македонски јазик',
    world: 'Зборовен свет',
    color: '#E84393',
    bgColor: '#FFE8F5',
    emoji: '📖',
    flagCode: 'mk',
    unitsCount: 7,
    category: 'core',
    grades: [1, 2, 3, 4, 5, 6, 7, 8, 9],
  },
  {
    id: 'english',
    name: 'English',
    nameMk: 'Англиски јазик',
    world: 'English World',
    color: '#DC2626',
    bgColor: '#FEE2E2',
    emoji: '🌐',
    flagCode: 'gb',
    unitsCount: 4,
    category: 'core',
    grades: [1, 2, 3, 4, 5, 6, 7, 8, 9],
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
    category: 'science',
    grades: [1, 2, 3, 4, 5, 6],
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
    category: 'science',
    grades: [7, 8, 9],
  },
  {
    id: 'physics',
    name: 'Physics',
    nameMk: 'Физика',
    world: 'Физичка лабораторија',
    color: '#0EA5E9',
    bgColor: '#E0F2FE',
    emoji: '⚛️',
    unitsCount: 3,
    category: 'science',
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
    category: 'science',
    grades: [7, 8, 9],
  },
  {
    id: 'tech',
    name: 'Technical Education & Informatics',
    nameMk: 'Техничко и информатика',
    world: 'Дигитален свет',
    color: '#0EA5E9',
    bgColor: '#E0F2FE',
    emoji: '💻',
    unitsCount: 4,
    category: 'science',
    grades: [4, 5, 6, 7],
  },
  {
    id: 'innovation',
    name: 'Innovation',
    nameMk: 'Иновации',
    world: 'Иноваторски свет',
    color: '#F97316',
    bgColor: '#FFEDD5',
    emoji: '💡',
    unitsCount: 5,
    category: 'science',
    grades: [9],
  },
  {
    id: 'society',
    name: 'Society',
    nameMk: 'Општество',
    world: 'Светот околу мене',
    color: '#7C3AED',
    bgColor: '#EDE9FE',
    emoji: '🏘️',
    unitsCount: 4,
    category: 'social',
    grades: [1, 2, 3],
  },
  {
    id: 'history',
    name: 'History & Society',
    nameMk: 'Историја и општество',
    world: 'Временска машина',
    color: '#F59E0B',
    bgColor: '#FEF3C7',
    emoji: '🏛️',
    unitsCount: 7,
    category: 'social',
    grades: [4, 5, 6, 7, 8, 9],
  },
  {
    id: 'geography',
    name: 'Geography',
    nameMk: 'Географија',
    world: 'Светски патник',
    color: '#16A34A',
    bgColor: '#DCFCE7',
    emoji: '🌍',
    unitsCount: 4,
    category: 'social',
    grades: [7, 8, 9],
  },
  {
    id: 'civics',
    name: 'Civic Education',
    nameMk: 'Граѓанско образование',
    world: 'Граѓански свет',
    color: '#7C3AED',
    bgColor: '#EDE9FE',
    emoji: '🏛️',
    unitsCount: 6,
    category: 'social',
    grades: [7, 8, 9],
  },
  {
    id: 'french',
    name: 'French',
    nameMk: 'Француски јазик',
    world: 'Le Monde Français',
    color: '#2563EB',
    bgColor: '#EFF6FF',
    emoji: '🇫🇷',
    flagCode: 'fr',
    unitsCount: 3,
    category: 'languages',
    grades: [6, 7, 8, 9],
  },
  {
    id: 'german',
    name: 'German',
    nameMk: 'Германски јазик',
    world: 'Deutsch Welt',
    color: '#F59E0B',
    bgColor: '#FEF3C7',
    emoji: '🇩🇪',
    flagCode: 'de',
    unitsCount: 3,
    category: 'languages',
    grades: [6, 7, 8, 9],
  },
  {
    id: 'italian',
    name: 'Italian',
    nameMk: 'Италијански јазик',
    world: 'Il Mondo Italiano',
    color: '#16A34A',
    bgColor: '#DCFCE7',
    emoji: '🇮🇹',
    flagCode: 'it',
    unitsCount: 3,
    category: 'languages',
    grades: [],
  },
  {
    id: 'russian',
    name: 'Russian',
    nameMk: 'Руски јазик',
    world: 'Русский мир',
    color: '#1565C0',
    bgColor: '#E3F2FD',
    emoji: '🇷🇺',
    flagCode: 'ru',
    unitsCount: 3,
    category: 'languages',
    grades: [],
  },
]

// Display order across the platform:
// 1. mk (Македонски)
// 2. math (Математика)
// 3. Civic/History group: society → history → civics → geography
// 4. Natural sciences group: science → biology → chemistry → physics → innovation → tech
// 5. Languages group: english → german → french → italian → russian
const DISPLAY_ORDER: SubjectId[] = [
  'mk',
  'math',
  // civic/history group
  'society',
  'history',
  'civics',
  'geography',
  // natural sciences group
  'science',
  'biology',
  'chemistry',
  'physics',
  'innovation',
  'tech',
  // languages group
  'english',
  'german',
  'french',
  'italian',
  'russian',
]

function sortByDisplayOrder(subjects: Subject[]): Subject[] {
  return [...subjects].sort((a, b) => {
    const ai = DISPLAY_ORDER.indexOf(a.id)
    const bi = DISPLAY_ORDER.indexOf(b.id)
    return (ai === -1 ? 999 : ai) - (bi === -1 ? 999 : bi)
  })
}

export const SUBJECTS: Subject[] = sortByDisplayOrder(ALL_SUBJECTS)

export function getAllSubjects(): Subject[] {
  return SUBJECTS
}

export function getSubjectsForGrade(grade: number): Subject[] {
  const filtered = grade === 0 ? ALL_SUBJECTS : ALL_SUBJECTS.filter((s) => s.grades.includes(grade))
  return sortByDisplayOrder(filtered)
}

export const getSubject = (id: string) =>
  ALL_SUBJECTS.find((s) => s.id === id)

export function gradeOrdinal(g: number): string {
  if (g === 1) return 'во'
  if (g === 2) return 'ро'
  if (g === 7 || g === 8) return 'мо'
  return 'то'
}
