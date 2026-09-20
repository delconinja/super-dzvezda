import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {NumberLine, numberLineXFor} from '../components/NumberLine';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §2 — INTEGERS INTRO
 * Reveal positive (green), negative (red), and zero (blue) groups
 * one at a time with labels.
 */
export const IntegersIntro: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [220, 250], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const lineY = 540;

  const zeroShow = interpolate(frame, [60, 80], [0, 1], {extrapolateRight: 'clamp'});
  const posShow = interpolate(frame, [110, 130], [0, 1], {extrapolateRight: 'clamp'});
  const negShow = interpolate(frame, [160, 180], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Што се цели броеви?" size={62} color={theme.zero} y={120} />
        <NumberLine min={-6} max={6} width={1600} y={lineY} delay={30} />

        {/* zero glow */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, opacity: zeroShow}}
        >
          <circle
            cx={numberLineXFor(0)}
            cy={lineY}
            r={36}
            fill="none"
            stroke={theme.zero}
            strokeWidth={4}
          />
          <text
            x={numberLineXFor(0)}
            y={lineY - 80}
            fill={theme.zero}
            fontFamily={FONT_FAMILY}
            fontSize={36}
            fontWeight={700}
            textAnchor="middle"
          >
            нула
          </text>
        </svg>

        {/* positives */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, opacity: posShow}}
        >
          {[1, 2, 3, 4, 5, 6].map((n) => (
            <circle
              key={n}
              cx={numberLineXFor(n)}
              cy={lineY}
              r={22}
              fill="none"
              stroke={theme.positive}
              strokeWidth={3}
            />
          ))}
          <text
            x={numberLineXFor(3)}
            y={lineY - 80}
            fill={theme.positive}
            fontFamily={FONT_FAMILY}
            fontSize={32}
            fontWeight={700}
            textAnchor="middle"
          >
            позитивни
          </text>
        </svg>

        {/* negatives */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, opacity: negShow}}
        >
          {[-6, -5, -4, -3, -2, -1].map((n) => (
            <circle
              key={n}
              cx={numberLineXFor(n)}
              cy={lineY}
              r={22}
              fill="none"
              stroke={theme.negative}
              strokeWidth={3}
            />
          ))}
          <text
            x={numberLineXFor(-3)}
            y={lineY - 80}
            fill={theme.negative}
            fontFamily={FONT_FAMILY}
            fontSize={32}
            fontWeight={700}
            textAnchor="middle"
          >
            негативни
          </text>
        </svg>
      </div>
    </Background>
  );
};
