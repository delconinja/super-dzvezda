import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {IntegerChip} from '../components/IntegerChip';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §6 — PRIMES + FACTOR TREE
 * Glowing gold "stars" for primes, then 12 = 2 × 2 × 3 decomposes downward.
 */
export const Primes: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [260, 290], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const primes = [2, 3, 5, 7, 11, 13, 17, 19];

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption
          text="Прости броеви — ѕвезди на математиката"
          size={50}
          color={theme.prime}
          y={80}
        />

        {/* prime stars row */}
        {primes.map((p, i) => {
          const delay = 20 + i * 10;
          const f = Math.max(0, frame - delay);
          const scale = spring({frame: f, fps, config: {damping: 11, mass: 0.55}});
          const cx = 220 + i * 200;
          const cy = 280;
          return (
            <div
              key={p}
              style={{
                position: 'absolute',
                left: cx,
                top: cy,
                width: 130,
                height: 130,
                transform: `translate(-50%, -50%) scale(${scale})`,
                borderRadius: '50%',
                border: `4px solid ${theme.prime}`,
                background: `radial-gradient(circle, ${theme.prime}44 0%, transparent 70%)`,
                boxShadow: `0 0 35px ${theme.prime}aa, inset 0 0 20px ${theme.prime}66`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: theme.bg,
                fontFamily: FONT_FAMILY,
                fontSize: 50,
                fontWeight: 700,
              }}
            >
              {p}
            </div>
          );
        })}

        {/* factor tree: 12 → 4,3 → 2,2 */}
        <IntegerChip value={12} size={60} delay={120} x={960} y={500} color={theme.zero} />
        <IntegerChip value={4} size={50} delay={160} x={830} y={650} color={theme.whiteText} />
        <IntegerChip value={3} size={50} delay={160} x={1090} y={650} color={theme.prime} />
        <IntegerChip value={2} size={42} delay={195} x={760} y={780} color={theme.prime} />
        <IntegerChip value={2} size={42} delay={195} x={900} y={780} color={theme.prime} />

        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
        >
          {[
            {x1: 960, y1: 540, x2: 830, y2: 610, delay: 145},
            {x1: 960, y1: 540, x2: 1090, y2: 610, delay: 145},
            {x1: 830, y1: 690, x2: 760, y2: 745, delay: 180},
            {x1: 830, y1: 690, x2: 900, y2: 745, delay: 180},
          ].map((l, i) => {
            const op = interpolate(frame, [l.delay, l.delay + 15], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            return (
              <line
                key={i}
                x1={l.x1}
                y1={l.y1}
                x2={l.x2}
                y2={l.y2}
                stroke={theme.subtle}
                strokeWidth={2}
                opacity={op}
              />
            );
          })}
        </svg>

        <div
          style={{
            position: 'absolute',
            bottom: 60,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 58,
            fontWeight: 700,
            color: theme.prime,
            textShadow: `0 0 18px ${theme.prime}66`,
            opacity: interpolate(frame, [220, 240], [0, 1], {extrapolateRight: 'clamp'}),
          }}
        >
          12 = 2 × 2 × 3
        </div>
      </div>
    </Background>
  );
};
