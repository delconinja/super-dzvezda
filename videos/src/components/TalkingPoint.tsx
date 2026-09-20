import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {theme, FONT_FAMILY} from '../theme';
import {Background} from './Background';

/**
 * Generic "talking point" beat — used as a stand-in until a custom
 * scene gets built for this concept. Shows:
 *   - a heading
 *   - an emoji/icon for visual hook
 *   - 2–4 bullet-points or one chunk of explanation text
 *   - optional formula display
 */
export const TalkingPoint: React.FC<{
  heading: string;
  icon?: string;
  bullets?: string[];
  formula?: string;
  headingColor?: string;
  durationFrames: number;
}> = ({
  heading,
  icon,
  bullets = [],
  formula,
  headingColor = theme.zero,
  durationFrames,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(
    frame,
    [durationFrames - 60, durationFrames - 10],
    [1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
  );

  const headingOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const headingScale = spring({frame, fps, config: {damping: 14, mass: 0.6}});
  const iconOp = interpolate(frame, [40, 90], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        {/* heading */}
        <div
          style={{
            position: 'absolute',
            top: 130,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 58,
            fontWeight: 700,
            color: headingColor,
            opacity: headingOp,
            transform: `scale(${headingScale})`,
            textShadow: `0 0 22px ${headingColor}66`,
          }}
        >
          {heading}
        </div>

        {/* icon */}
        {icon ? (
          <div
            style={{
              position: 'absolute',
              top: 300,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontSize: 180,
              opacity: iconOp,
              filter: `drop-shadow(0 0 30px ${headingColor}aa)`,
            }}
          >
            {icon}
          </div>
        ) : null}

        {/* formula */}
        {formula ? (
          <div
            style={{
              position: 'absolute',
              top: icon ? 540 : 340,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 78,
              fontWeight: 700,
              color: theme.prime,
              opacity: interpolate(frame, [120, 180], [0, 1], {extrapolateRight: 'clamp'}),
              textShadow: `0 0 24px ${theme.prime}88`,
              letterSpacing: 2,
            }}
          >
            {formula}
          </div>
        ) : null}

        {/* bullets */}
        {bullets.length > 0 ? (
          <div
            style={{
              position: 'absolute',
              top: icon ? 700 : (formula ? 520 : 320),
              left: 0,
              right: 0,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 24,
            }}
          >
            {bullets.map((b, i) => {
              const delay = 150 + i * 60;
              const op = interpolate(frame, [delay, delay + 30], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              });
              const dx = interpolate(frame, [delay, delay + 30], [-30, 0], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              });
              return (
                <div
                  key={i}
                  style={{
                    fontFamily: FONT_FAMILY,
                    fontSize: 34,
                    color: theme.whiteText,
                    opacity: op,
                    transform: `translateX(${dx}px)`,
                    maxWidth: 1400,
                    textAlign: 'center',
                  }}
                >
                  {b}
                </div>
              );
            })}
          </div>
        ) : null}
      </div>
    </Background>
  );
};
