import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {theme, FONT_FAMILY, colorForInt} from '../theme';

export const IntegerChip: React.FC<{
  value: number;
  size?: number;
  delay?: number;
  color?: string;
  x?: number;
  y?: number;
}> = ({value, size = 70, delay = 0, color, x = 0, y = 0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const f = Math.max(0, frame - delay);
  const scale = spring({frame: f, fps, config: {damping: 12, mass: 0.5}});
  const chipColor = color ?? colorForInt(value);

  return (
    <div
      style={{
        position: 'absolute',
        left: x,
        top: y,
        transform: `translate(-50%, -50%) scale(${scale})`,
        width: size * 1.6,
        height: size * 1.6,
        borderRadius: '50%',
        border: `3px solid ${chipColor}`,
        boxShadow: `0 0 25px ${chipColor}88, inset 0 0 15px ${chipColor}44`,
        backgroundColor: `${theme.bg}cc`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: FONT_FAMILY,
        fontSize: size,
        fontWeight: 700,
        color: chipColor,
      }}
    >
      {value}
    </div>
  );
};
