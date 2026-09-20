import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {NumberLine, numberLineXFor} from '../components/NumberLine';
import {IntegerChip} from '../components/IntegerChip';
import {HopArrow} from '../components/HopArrow';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §8 — WORKED EXAMPLE 1
 * 5 + (−3) = 2 visualized step-by-step on a number line.
 * Steps explicitly labelled left-side, with synchronized animation right-side.
 */
export const WorkedExampleAddition: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [260, 290], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const lineY = 760;
  const min = -3;
  const max = 8;
  const width = 1500;
  const xFor = (n: number) => numberLineXFor(n, {min, max, width});

  const stepOpacity = (start: number) =>
    interpolate(frame, [start, start + 18], [0, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    });

  const chipX = interpolate(frame, [120, 170], [xFor(5), xFor(2)], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Пример 1: 5 + (−3) = ?" size={64} color={theme.zero} y={80} />

        {/* step list on the left */}
        <div
          style={{
            position: 'absolute',
            left: 110,
            top: 280,
            display: 'flex',
            flexDirection: 'column',
            gap: 28,
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            fontWeight: 600,
          }}
        >
          <div style={{color: theme.positive, opacity: stepOpacity(30)}}>
            Чекор 1: Започнуваме на 5
          </div>
          <div style={{color: theme.negative, opacity: stepOpacity(95)}}>
            Чекор 2: Се движиме 3 чекори лево
          </div>
          <div style={{color: theme.zero, opacity: stepOpacity(180)}}>
            Чекор 3: Завршуваме на 2
          </div>
        </div>

        <NumberLine min={min} max={max} width={width} y={lineY} delay={30} />

        {/* moving chip */}
        {frame >= 60 && (
          <IntegerChip
            value={frame < 175 ? 5 : 2}
            size={frame < 175 ? 60 : 75}
            delay={60}
            x={chipX}
            y={lineY - 100}
            color={frame < 175 ? theme.positive : theme.zero}
          />
        )}

        {/* hop arrow */}
        <HopArrow
          fromX={xFor(5)}
          toX={xFor(2)}
          y={lineY}
          color={theme.negative}
          delay={120}
          duration={45}
        />

        {/* result */}
        {frame >= 200 && (
          <div
            style={{
              position: 'absolute',
              top: 580,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 92,
              fontWeight: 700,
              color: theme.zero,
              opacity: interpolate(frame, [200, 220], [0, 1], {extrapolateRight: 'clamp'}),
              textShadow: `0 0 24px ${theme.zero}88`,
            }}
          >
            5 + (−3) = 2
          </div>
        )}
      </div>
    </Background>
  );
};
