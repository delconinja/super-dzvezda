import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §9 Substitution: x = 3, y = 5 → evaluate
 * Three sub-examples evaluated in sequence:
 *   2x + y = 11
 *   x² + 2y = 19
 *   3x − y = 4
 * 35s = 1050 frames
 */
const VAR_X = '#ffd54f';
const VAR_Y = '#ba68c8';

export const SubstitutionDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Setup x=3, y=5
  const setupOp = interpolate(frame, [60, 130], [0, 1], {extrapolateRight: 'clamp'});

  // Three examples (each ~280f)
  const examples = [
    {expr: '2x + y', plugged: '2(3) + 5', result: '= 11', start: 180},
    {expr: 'x² + 2y', plugged: '3² + 2(5)', result: '= 19', start: 480},
    {expr: '3x − y', plugged: '3(3) − 5', result: '= 4',  start: 780},
  ];

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 80,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 52,
            fontWeight: 700,
            color: theme.zero,
            opacity: titleOp,
          }}
        >
          Замена на броеви во израз
        </div>

        {/* x = 3, y = 5 setup */}
        <div
          style={{
            position: 'absolute',
            top: 220,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 48,
            opacity: setupOp,
          }}
        >
          Ако{' '}
          <span style={{color: VAR_X, fontWeight: 700, fontSize: 64, textShadow: `0 0 18px ${VAR_X}88`}}>
            x = 3
          </span>
          {' '}и{' '}
          <span style={{color: VAR_Y, fontWeight: 700, fontSize: 64, textShadow: `0 0 18px ${VAR_Y}88`}}>
            y = 5
          </span>
        </div>

        {/* Three substitution rows */}
        <div
          style={{
            position: 'absolute',
            top: 400,
            left: 0,
            right: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 60,
            fontFamily: FONT_FAMILY,
          }}
        >
          {examples.map((ex, i) => {
            const exprOp = interpolate(frame, [ex.start, ex.start + 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const pluggedOp = interpolate(frame, [ex.start + 60, ex.start + 100], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const resultOp = interpolate(frame, [ex.start + 130, ex.start + 170], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const resultScale = spring({
              frame: Math.max(0, frame - ex.start - 130),
              fps,
              config: {damping: 12, mass: 0.5},
            });
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 30,
                  fontSize: 44,
                  fontWeight: 600,
                }}
              >
                <div style={{opacity: exprOp, color: theme.whiteText, minWidth: 200, textAlign: 'right'}}>
                  {ex.expr}
                </div>
                <div style={{opacity: pluggedOp, color: theme.subtle, minWidth: 240}}>
                  → {ex.plugged}
                </div>
                <div
                  style={{
                    opacity: resultOp,
                    color: theme.prime,
                    fontWeight: 700,
                    fontSize: 56,
                    transform: `scale(${resultScale})`,
                    textShadow: `0 0 20px ${theme.prime}99`,
                  }}
                >
                  {ex.result}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </Background>
  );
};
