import { BadgeDef, TIER_COLORS } from '@/lib/badges'

interface Props {
  badge: BadgeDef
  earnedAt?: string
  size?: 'sm' | 'md'
}

export default function BadgeCard({ badge, earnedAt, size = 'md' }: Props) {
  const tier = TIER_COLORS[badge.tier]
  const isSm = size === 'sm'

  return (
    <div className="flex items-center gap-3 rounded-2xl"
      style={{
        background: tier.bg,
        border: `2px solid ${tier.border}`,
        padding: isSm ? '10px 12px' : '14px 16px',
      }}>
      <span style={{ fontSize: isSm ? '1.4rem' : '1.8rem', lineHeight: 1 }}>{badge.emoji}</span>
      <div className="flex-1 min-w-0">
        <p className="font-black truncate" style={{ color: tier.label, fontSize: isSm ? '0.8rem' : '0.9rem' }}>
          {badge.nameMk}
        </p>
        {!isSm && (
          <p className="text-xs font-semibold mt-0.5" style={{ color: '#9B9BAA' }}>{badge.descMk}</p>
        )}
        {earnedAt && (
          <p className="text-xs font-semibold" style={{ color: '#C4C4D4' }}>
            {new Date(earnedAt).toLocaleDateString('mk-MK', { day: 'numeric', month: 'short' })}
          </p>
        )}
      </div>
      <span className="text-xs font-black px-2 py-0.5 rounded-full flex-shrink-0"
        style={{ background: tier.border, color: tier.label }}>
        {badge.tier === 'legendary' ? 'ЛЕГЕНДА' : badge.tier === 'rare' ? 'РЕТКА' : 'ЗНАЧКА'}
      </span>
    </div>
  )
}
