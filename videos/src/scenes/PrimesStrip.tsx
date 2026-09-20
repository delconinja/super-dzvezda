import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §8 Primes — show the locked BRO list: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
 * Each appears as a gold ring with the number inside, staggered.
 * 30s = 900 frames @ 30fps
 */
const PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];

export const PrimesStrip: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [840, 900], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 100,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 56,
            fontWeight: 700,
            color: theme.prime,
            opacity: titleOp,
            textShadow: `0 0 20px ${theme.prime}66`,
          }}
        >
          Прости броеви — тули од кои се гради сè
        </div>
        <div
          style={{
            position: 'absolute',
            top: 230,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 28,
            color: theme.subtle,
            fontStyle: 'italic',
            opacity: interpolate(frame, [40, 100], [0, 1], {extrapolateRight: 'clamp'}),
          }}
        >
          броеви што имаат точно два делители: 1 и самиот себе
        </div>

        <div
          style={{
            position: 'absolute',
            top: 380,
            left: 0,
            right: 0,
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            gap: 36,
            padding: '0 200px',
          }}
        >
          {PRIMES.map((p, i) => {
            const delay = 80 + i * 50;
            const f = Math.max(0, frame - delay);
            const scale = spring({frame: f, fps, config: {damping: 12, mass: 0.6}});
            const op = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
            return (
              <div
                key={p}
                style={{
                  width: 130,
                  height: 130,
                  borderRadius: '50%',
                  border: `4px solid ${theme.prime}`,
                  background: `radial-gradient(circle at 30% 30%, ${theme.prime}33, transparent)`,
                  boxShadow: `0 0 30px ${theme.prime}66, inset 0 0 20px ${theme.prime}33`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: FONT_FAMILY,
                  fontSize: p < 10 ? 64 : 52,
                  fontWeight: 700,
                  color: theme.prime,
                  textShadow: `0 0 14px ${theme.prime}aa`,
                  opacity: op,
                  transform: `scale(${scale})`,
                }}
              >
                {p}
              </div>
            );
          })}
        </div>

        <div
          style={{
            position: 'absolute',
            bottom: 80,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 32,
            color: theme.subtle,
            opacity: interpolate(frame, [700, 780], [0, 1], {extrapolateRight: 'clamp'}),
          }}
        >
          ... и така натаму. Бесконечно многу.
        </div>
      </div>
    </Background>
  );
};
