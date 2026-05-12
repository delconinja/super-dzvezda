export type BadgeCategory = 'mastery' | 'consistency' | 'effort' | 'exploration'
export type BadgeTier = 'normal' | 'rare' | 'legendary'

export interface BadgeDef {
  id: string
  nameMk: string
  descMk: string
  emoji: string
  category: BadgeCategory
  tier: BadgeTier
  check: (stats: BadgeStats) => boolean
}

export interface BadgeStats {
  event: 'challenge_complete' | 'lesson_complete'
  // challenge-specific
  unitId?: string
  earnedYellow?: boolean
  earnedGreen?: boolean
  earnedBlue?: boolean
  isRetry?: boolean
  gainedNewStar?: boolean
  attempts?: number
  // aggregated from DB
  totalLessons: number
  totalBlueStars: number
  totalGreenStars: number
  totalYellowStars: number
  streakDays: number
  subjectsStudied: string[]
  completedUnitIds: string[]
  allUnitsBySubject: string[][]
}

export const BADGE_DEFS: BadgeDef[] = [
  // ── MASTERY ───────────────────────────────────────────────────────
  {
    id: 'first_challenge',
    nameMk: 'Прв Предизвик',
    descMk: 'Заврши го твојот прв предизвик',
    emoji: '🏁',
    category: 'mastery',
    tier: 'normal',
    check: ({ event }) => event === 'challenge_complete',
  },
  {
    id: 'perfect_easy',
    nameMk: 'Лесно Мајсторство',
    descMk: 'Одговори точно на сите лесни прашања на прв обид',
    emoji: '⭐',
    category: 'mastery',
    tier: 'normal',
    check: ({ event, earnedYellow }) => event === 'challenge_complete' && !!earnedYellow,
  },
  {
    id: 'perfect_hard',
    nameMk: 'Тешко Мајсторство',
    descMk: 'Одговори точно на сите тешки прашања на прв обид',
    emoji: '💎',
    category: 'mastery',
    tier: 'rare',
    check: ({ event, earnedBlue }) => event === 'challenge_complete' && !!earnedBlue,
  },
  {
    id: 'all_stars_unit',
    nameMk: 'Единица Мајстор',
    descMk: 'Освои ги сите три ѕвезди во еден предизвик',
    emoji: '🌟',
    category: 'mastery',
    tier: 'rare',
    check: ({ event, earnedYellow, earnedGreen, earnedBlue }) =>
      event === 'challenge_complete' && !!earnedYellow && !!earnedGreen && !!earnedBlue,
  },
  {
    id: 'five_blue_stars',
    nameMk: 'Сини 5',
    descMk: 'Освои вкупно 5 сини ѕвезди во предизвици',
    emoji: '🔵',
    category: 'mastery',
    tier: 'rare',
    check: ({ totalBlueStars }) => totalBlueStars >= 5,
  },

  // ── CONSISTENCY ───────────────────────────────────────────────────
  {
    id: 'streak_3',
    nameMk: '3 Дена',
    descMk: 'Учи 3 дена по ред',
    emoji: '🔥',
    category: 'consistency',
    tier: 'normal',
    check: ({ streakDays }) => streakDays >= 3,
  },
  {
    id: 'streak_7',
    nameMk: 'Неделен Учач',
    descMk: 'Учи 7 дена по ред',
    emoji: '🗓️',
    category: 'consistency',
    tier: 'rare',
    check: ({ streakDays }) => streakDays >= 7,
  },
  {
    id: 'streak_30',
    nameMk: 'Месечен Учач',
    descMk: 'Учи 30 дена по ред',
    emoji: '👑',
    category: 'consistency',
    tier: 'legendary',
    check: ({ streakDays }) => streakDays >= 30,
  },

  // ── EFFORT ────────────────────────────────────────────────────────
  {
    id: 'first_lesson',
    nameMk: 'Прва Лекција',
    descMk: 'Заврши ја твојата прва лекција',
    emoji: '📖',
    category: 'effort',
    tier: 'normal',
    check: ({ event, totalLessons }) => event === 'lesson_complete' && totalLessons >= 1,
  },
  {
    id: 'lesson_10',
    nameMk: '10 Лекции',
    descMk: 'Заврши 10 лекции',
    emoji: '📚',
    category: 'effort',
    tier: 'normal',
    check: ({ totalLessons }) => totalLessons >= 10,
  },
  {
    id: 'persistent',
    nameMk: 'Упорен',
    descMk: 'Обиди се на ист предизвик 3 или повеќе пати',
    emoji: '💪',
    category: 'effort',
    tier: 'normal',
    check: ({ event, attempts }) => event === 'challenge_complete' && (attempts ?? 0) >= 3,
  },
  {
    id: 'improver',
    nameMk: 'Напредок',
    descMk: 'Освои нова ѕвезда при повторен обид',
    emoji: '📈',
    category: 'effort',
    tier: 'rare',
    check: ({ event, isRetry, gainedNewStar }) =>
      event === 'challenge_complete' && !!isRetry && !!gainedNewStar,
  },

  // ── EXPLORATION ───────────────────────────────────────────────────
  {
    id: 'multi_subject',
    nameMk: 'Истражувач',
    descMk: 'Учи во 3 различни предмети',
    emoji: '🔭',
    category: 'exploration',
    tier: 'normal',
    check: ({ subjectsStudied }) => subjectsStudied.length >= 3,
  },
  {
    id: 'lesson_50',
    nameMk: '50 Лекции',
    descMk: 'Заврши 50 лекции',
    emoji: '🚀',
    category: 'exploration',
    tier: 'rare',
    check: ({ totalLessons }) => totalLessons >= 50,
  },
  {
    id: 'subject_champion',
    nameMk: 'Шампион',
    descMk: 'Заврши ги сите предизвици во еден предмет',
    emoji: '🏆',
    category: 'exploration',
    tier: 'legendary',
    check: ({ completedUnitIds, allUnitsBySubject }) =>
      allUnitsBySubject.some(
        unitIds => unitIds.length > 0 && unitIds.every(uid => completedUnitIds.includes(uid))
      ),
  },
]

export function evaluateNewBadges(stats: BadgeStats, alreadyEarnedIds: string[]): string[] {
  return BADGE_DEFS
    .filter(b => !alreadyEarnedIds.includes(b.id) && b.check(stats))
    .map(b => b.id)
}

export function getBadgeDef(id: string): BadgeDef | undefined {
  return BADGE_DEFS.find(b => b.id === id)
}

export const TIER_COLORS: Record<BadgeTier, { bg: string; border: string; label: string }> = {
  normal:    { bg: '#F7F5FF', border: '#C4B8FF', label: '#5C35D4' },
  rare:      { bg: '#FFF9E6', border: '#FFD93D', label: '#7A5800' },
  legendary: { bg: '#FFF0F8', border: '#FF6B9D', label: '#8B0043' },
}

export const CATEGORY_META: Record<BadgeCategory, { labelMk: string; emoji: string }> = {
  mastery:     { labelMk: 'Мајсторство',  emoji: '🎯' },
  consistency: { labelMk: 'Доследност',   emoji: '🔥' },
  effort:      { labelMk: 'Труд',         emoji: '💪' },
  exploration: { labelMk: 'Истражување',  emoji: '🔭' },
}
