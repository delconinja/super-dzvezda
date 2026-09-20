import {useCurrentFrame, interpolate} from 'remotion';
import {theme, FONT_FAMILY, colorForInt} from '../theme';

export const NumberLine: React.FC<{
  min?: number;
  max?: number;
  width?: number;
  y?: number;
  delay?: number;
}> = ({min = -6, max = 6, width = 1600, y = 540, delay = 0}) => {
  const frame = useCurrentFrame();
  const f = Math.max(0, frame - delay);

  const lineProgress = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const numbersProgress = interpolate(f, [25, 70], [0, 1], {extrapolateRight: 'clamp'});

  const totalRange = max - min;
  const leftX = (1920 - width) / 2;

  // Convert integer to x-coordinate on screen.
  const xFor = (n: number) => leftX + ((n - min) / totalRange) * width;

  const lineEndX = leftX + width * lineProgress;

  return (
    <svg
      width={1920}
      height={1080}
      style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
    >
      {/* main line */}
      <line
        x1={leftX}
        y1={y}
        x2={lineEndX}
        y2={y}
        stroke={theme.whiteText}
        strokeWidth={3}
      />
      {/* tick marks + integer labels */}
      {Array.from({length: totalRange + 1}, (_, i) => {
        const n = min + i;
        const x = xFor(n);
        const tickShown = lineProgress > i / totalRange;
        const labelProgress = Math.max(0, Math.min(1, (numbersProgress * (totalRange + 1) - i)));
        return (
          <g key={n} opacity={tickShown ? 1 : 0}>
            <line
              x1={x}
              y1={y - 10}
              x2={x}
              y2={y + 10}
              stroke={theme.whiteText}
              strokeWidth={2}
            />
            <text
              x={x}
              y={y + 50}
              fill={colorForInt(n)}
              fontFamily={FONT_FAMILY}
              fontSize={n === 0 ? 36 : 28}
              fontWeight={n === 0 ? 700 : 400}
              textAnchor="middle"
              opacity={labelProgress}
            >
              {n}
            </text>
          </g>
        );
      })}
    </svg>
  );
};

// Helper: convert integer value to absolute screen x coordinate
// (matches the geometry above so other components can place chips on the line)
export function numberLineXFor(
  n: number,
  {
    min = -6,
    max = 6,
    width = 1600,
  }: {min?: number; max?: number; width?: number} = {}
) {
  const leftX = (1920 - width) / 2;
  return leftX + ((n - min) / (max - min)) * width;
}
