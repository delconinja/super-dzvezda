import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §6 Combining like terms — visual blocks combine
 * 3x + 5x → 8x; 4y − 2y → 2y; 3x + 2y + 5x → 8x + 2y
 * 35s = 1050 frames
 */
const VAR_X = '#ffd54f';
const VAR_Y = '#ba68c8';

export const CombineLikeTerms: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Demo 1 (0-280f): 3x + 5x = 8x
  const d1ShowExpr = interpolate(frame, [45, 90], [0, 1], {extrapolateRight: 'clamp'});
  const d1Combine = interpolate(frame, [180, 240], [0, 1], {extrapolateRight: 'clamp'});
  const d1Result = interpolate(frame, [220, 270], [0, 1], {extrapolateRight: 'clamp'});
  const d1Out = interpolate(frame, [300, 360], [1, 0], {extrapolateRight: 'clamp'});

  // Demo 2 (380-700f): 3x + 2y + 5x = 8x + 2y
  const d2Show = interpolate(frame, [390, 450], [0, 1], {extrapolateRight: 'clamp'});
  const d2Group = interpolate(frame, [540, 600], [0, 1], {extrapolateRight: 'clamp'});
  const d2Result = interpolate(frame, [620, 680], [0, 1], {extrapolateRight: 'clamp'});
  const d2Out = interpolate(frame, [720, 780], [1, 0], {extrapolateRight: 'clamp'});

  // Demo 3 (800-1000f): Warning - 3x + 2y stays as 3x + 2y
  const d3Show = interpolate(frame, [800, 870], [0, 1], {extrapolateRight: 'clamp'});

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
          Слични членови — собираме!
        </div>

        {/* Demo 1: 3x + 5x = 8x */}
        {frame < 360 && (
          <div
            style={{
              position: 'absolute',
              top: 350,
              left: 0,
              right: 0,
              textAlign: 'center',
              opacity: d1Show * d1Out,
              fontFamily: FONT_FAMILY,
            }}
          >
            <div style={{fontSize: 80, color: VAR_X, fontWeight: 700, textShadow: `0 0 20px ${VAR_X}66`}}>
              3x + 5x
            </div>
            {d1Combine > 0.1 && (
              <div
                style={{
                  fontSize: 56,
                  color: theme.subtle,
                  marginTop: 40,
                  opacity: d1Combine,
                }}
              >
                3 + 5 = 8
              </div>
            )}
            {d1Result > 0.1 && (
              <div
                style={{
                  fontSize: 110,
                  color: theme.prime,
                  fontWeight: 700,
                  marginTop: 30,
                  opacity: d1Result,
                  textShadow: `0 0 30px ${theme.prime}99`,
                  transform: `scale(${spring({frame: Math.max(0, frame - 220), fps, config: {damping: 12}})})`,
                }}
              >
                8x
              </div>
            )}
          </div>
        )}

        {/* Demo 2: 3x + 2y + 5x → group by variable → 8x + 2y */}
        {frame >= 380 && frame < 780 && (
          <div
            style={{
              position: 'absolute',
              top: 280,
              left: 0,
              right: 0,
              textAlign: 'center',
              opacity: d2Show * d2Out,
              fontFamily: FONT_FAMILY,
            }}
          >
            <div style={{fontSize: 64, fontWeight: 700}}>
              <span style={{color: VAR_X}}>3x</span>{' '}
              <span style={{color: theme.whiteText}}>+</span>{' '}
              <span style={{color: VAR_Y}}>2y</span>{' '}
              <span style={{color: theme.whiteText}}>+</span>{' '}
              <span style={{color: VAR_X}}>5x</span>
            </div>

            {d2Group > 0.1 && (
              <div
                style={{
                  marginTop: 50,
                  fontSize: 36,
                  color: theme.subtle,
                  opacity: d2Group,
                }}
              >
                ↓ групирај {' '}
                <span style={{color: VAR_X}}>x-членови</span>
                {' '}и{' '}
                <span style={{color: VAR_Y}}>y-членови</span>{' '}одделно
              </div>
            )}

            {d2Result > 0.1 && (
              <div
                style={{
                  marginTop: 50,
                  fontSize: 96,
                  fontWeight: 700,
                  opacity: d2Result,
                  transform: `scale(${spring({frame: Math.max(0, frame - 620), fps, config: {damping: 12}})})`,
                }}
              >
                <span style={{color: VAR_X, textShadow: `0 0 26px ${VAR_X}aa`}}>8x</span>{' '}
                <span style={{color: theme.whiteText}}>+</span>{' '}
                <span style={{color: VAR_Y, textShadow: `0 0 26px ${VAR_Y}aa`}}>2y</span>
              </div>
            )}
          </div>
        )}

        {/* Demo 3: Different terms cannot combine */}
        {frame >= 800 && (
          <div
            style={{
              position: 'absolute',
              top: 320,
              left: 0,
              right: 0,
              textAlign: 'center',
              opacity: d3Show,
              fontFamily: FONT_FAMILY,
            }}
          >
            <div style={{fontSize: 36, color: theme.subtle, marginBottom: 40, fontStyle: 'italic'}}>
              Различни членови не се мешаат:
            </div>
            <div style={{fontSize: 72, fontWeight: 700}}>
              <span style={{color: VAR_X, textShadow: `0 0 18px ${VAR_X}55`}}>3x</span>
              {' + '}
              <span style={{color: VAR_Y, textShadow: `0 0 18px ${VAR_Y}55`}}>2y</span>
              {' = '}
              <span style={{color: VAR_X, textShadow: `0 0 18px ${VAR_X}55`}}>3x</span>
              {' + '}
              <span style={{color: VAR_Y, textShadow: `0 0 18px ${VAR_Y}55`}}>2y</span>
            </div>
            <div style={{fontSize: 32, color: '#e57373', marginTop: 50, fontStyle: 'italic'}}>
              не мешаме јаболка и круши 🍎🍐
            </div>
          </div>
        )}
      </div>
    </Background>
  );
};
