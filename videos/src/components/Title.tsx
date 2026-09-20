import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {theme, FONT_FAMILY} from '../theme';

export const Title: React.FC<{
  text: string;
  color?: string;
  size?: number;
  bold?: boolean;
  delay?: number;
}> = ({text, color = theme.zero, size = 84, bold = true, delay = 0}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const f = Math.max(0, frame - delay);
  const opacity = interpolate(f, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  const scale = spring({frame: f, fps, config: {damping: 14, mass: 0.6}});

  return (
    <div
      style={{
        fontFamily: FONT_FAMILY,
        fontSize: size,
        color,
        fontWeight: bold ? 700 : 400,
        textAlign: 'center',
        opacity,
        transform: `scale(${scale})`,
        textShadow: `0 0 20px ${color}55`,
      }}
    >
      {text}
    </div>
  );
};
