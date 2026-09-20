import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {NumberLine, numberLineXFor} from '../components/NumberLine';
import {IntegerChip} from '../components/IntegerChip';
import {HopArrow} from '../components/HopArrow';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §3 — ADDITION WITH SIGNS
 * Demo A: 2 + 3 = 5  (same-sign merge — green)
 * Demo B: 5 + (-3) = 2  (different-sign collision — red arrow leftward)
 */
export const AdditionSigns: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [330, 360], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const lineY = 600;

  // Demo A: 2 + 3 = 5  (frames 0..160)
  const captionA = frame < 175;

  // Demo B: 5 + (-3) = 2  (frames 175..360)
  const captionB = frame >= 175;

  const chipAX = interpolate(frame, [60, 100], [numberLineXFor(2), numberLineXFor(5)], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const chipBX = interpolate(
    frame,
    [225, 265],
    [numberLineXFor(5), numberLineXFor(2)],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
  );

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption
          text={captionA ? 'Истите знаци се обединуваат' : 'Различни знаци се судираат'}
          size={56}
          color={captionA ? theme.positive : theme.negative}
          y={100}
        />
        <NumberLine min={-7} max={7} width={1700} y={lineY} delay={20} />

        {/* Demo A: 2 + 3 = 5 */}
        {captionA && (
          <>
            <IntegerChip value={2} size={60} delay={40} x={chipAX} y={lineY - 100} />
            <HopArrow
              fromX={numberLineXFor(2)}
              toX={numberLineXFor(5)}
              y={lineY}
              color={theme.positive}
              delay={55}
              duration={40}
            />
            {frame >= 105 && (
              <IntegerChip
                value={5}
                size={70}
                delay={105}
                x={numberLineXFor(5)}
                y={lineY - 100}
              />
            )}
            {frame >= 120 && (
              <div
                style={{
                  position: 'absolute',
                  bottom: 80,
                  left: 0,
                  right: 0,
                  textAlign: 'center',
                  fontFamily: FONT_FAMILY,
                  fontSize: 64,
                  fontWeight: 700,
                  color: theme.positive,
                  textShadow: `0 0 18px ${theme.positive}66`,
                  opacity: interpolate(frame, [120, 140], [0, 1], {extrapolateRight: 'clamp'}),
                }}
              >
                2 + 3 = 5
              </div>
            )}
          </>
        )}

        {/* Demo B: 5 + (-3) = 2 */}
        {captionB && (
          <>
            <IntegerChip
              value={frame < 270 ? 5 : 2}
              size={frame < 270 ? 60 : 70}
              delay={195}
              x={chipBX}
              y={lineY - 100}
              color={frame < 270 ? theme.positive : theme.zero}
            />
            <HopArrow
              fromX={numberLineXFor(5)}
              toX={numberLineXFor(2)}
              y={lineY}
              color={theme.negative}
              delay={215}
              duration={40}
            />
            {frame >= 285 && (
              <div
                style={{
                  position: 'absolute',
                  bottom: 80,
                  left: 0,
                  right: 0,
                  textAlign: 'center',
                  fontFamily: FONT_FAMILY,
                  fontSize: 64,
                  fontWeight: 700,
                  color: theme.zero,
                  textShadow: `0 0 18px ${theme.zero}66`,
                  opacity: interpolate(frame, [285, 305], [0, 1], {extrapolateRight: 'clamp'}),
                }}
              >
                5 + (−3) = 2
              </div>
            )}
          </>
        )}
      </div>
    </Background>
  );
};
