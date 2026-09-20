/**
 * Locked color palette from narrations/m8-1-1.md §4 VISUAL LANGUAGE PLAN.
 * Same colors must be used in every lesson — global brand consistency.
 */
export const theme = {
  bg: '#0d1b2e',
  positive: '#81c784',   // Green
  negative: '#e57373',   // Red
  zero: '#4fc3f7',       // Blue
  prime: '#ffd54f',      // Gold
  power: '#ba68c8',      // Purple
  root: '#26c6da',       // Teal
  whiteText: '#eceff1',
  subtle: '#546e7a',
} as const;

export const FONT_FAMILY =
  '"Noto Sans", "Segoe UI", -apple-system, sans-serif';

export function colorForInt(n: number) {
  if (n > 0) return theme.positive;
  if (n < 0) return theme.negative;
  return theme.zero;
}
