import {useCurrentFrame, interpolate} from 'remotion';
import {theme, FONT_FAMILY} from '../theme';

export const Caption: React.FC<{
  text: string;
  size?: number;
  color?: string;
  y?: number;
  delay?: number;
}> = ({text, size = 48, color = theme.whiteText, y = 110, delay = 0}) => {
  const frame = useCurrentFrame();
  const f = Math.max(0, frame - delay);
  const opacity = interpolate(f, [0, 15], [0, 1], {extrapolateRight: 'clamp'});
  const dy = interpolate(f, [0, 20], [12, 0], {extrapolateRight: 'clamp'});

  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: y + dy,
        textAlign: 'center',
        opacity,
        fontFamily: FONT_FAMILY,
        fontSize: size,
        color,
        fontWeight: 600,
        textShadow: `0 0 12px ${color}44`,
      }}
    >
      {text}
    </div>
  );
};
