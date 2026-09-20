import {useCurrentFrame, interpolate} from 'remotion';

/**
 * Curved arc from `fromX` to `toX` along a horizontal y baseline.
 * Animates draw progress from 0..1 across `duration` frames.
 */
export const HopArrow: React.FC<{
  fromX: number;
  toX: number;
  y: number;
  color: string;
  delay?: number;
  duration?: number;
  height?: number;
}> = ({fromX, toX, y, color, delay = 0, duration = 25, height = 90}) => {
  const frame = useCurrentFrame();
  const f = Math.max(0, frame - delay);
  const progress = interpolate(f, [0, duration], [0, 1], {extrapolateRight: 'clamp'});

  const midX = (fromX + toX) / 2;
  const arcTopY = y - height;
  const currentX = fromX + (toX - fromX) * progress;
  const currentY = y + (4 * (arcTopY - y) * progress * (1 - progress));

  // Build the curve up to current progress as a quadratic Bezier from (fromX, y) → (currentX, currentY)
  const cpX = (fromX + currentX) / 2;
  const cpY = y + (4 * (arcTopY - y) * (progress / 2) * (1 - progress / 2));

  return (
    <svg
      width={1920}
      height={1080}
      style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
    >
      <path
        d={`M ${fromX} ${y} Q ${cpX} ${cpY} ${currentX} ${currentY}`}
        stroke={color}
        strokeWidth={5}
        fill="none"
        strokeLinecap="round"
      />
      {progress > 0.05 ? (
        <circle cx={currentX} cy={currentY} r={9} fill={color} />
      ) : null}
      {progress >= 1 ? (
        <polygon
          points={`${toX},${y} ${toX - (toX > fromX ? 18 : -18)},${y - 10} ${
            toX - (toX > fromX ? 18 : -18)
          },${y + 10}`}
          fill={color}
        />
      ) : null}
    </svg>
  );
};
