import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Stack of equations, each fading in stacked vertically.
 * Used for:
 *   - Factorization gallery: 12 = 2² × 3,  30 = 2 × 3 × 5, ...
 *   - Powers of 10: 10¹ = 10, 10² = 100, ...
 *   - Square roots: √16 = 4, √81 = 9, √100 = 10
 *   - Cube roots:   ³√8 = 2, ³√27 = 3, ³√64 = 4
 *   - Powers: 2³ = 2 × 2 × 2 = 8, etc.
 */
export const EquationGallery: React.FC<{
  title: string;
  equations: string[];
  accentColor?: string;
  caption?: string;
  durationFrames: number;
}> = ({title, equations, accentColor = theme.prime, caption, durationFrames}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(
    frame,
    [durationFrames - 60, durationFrames - 10],
    [1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
  );

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Distribute equations across the available frames after title
  const regionStart = 60;
  const regionEnd = durationFrames - 100;
  const gap = (regionEnd - regionStart) / Math.max(1, equations.length);

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 100,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 56,
            fontWeight: 700,
            color: accentColor,
            opacity: titleOp,
            textShadow: `0 0 18px ${accentColor}66`,
          }}
        >
          {title}
        </div>

        <div
          style={{
            position: 'absolute',
            top: 260,
            left: 0,
            right: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 36,
          }}
        >
          {equations.map((eq, i) => {
            const entry = regionStart + i * gap;
            const f = Math.max(0, frame - entry);
            const op = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
            const scale = spring({frame: f, fps, config: {damping: 13, mass: 0.55}});
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT_FAMILY,
                  fontSize: 76,
                  fontWeight: 700,
                  color: theme.whiteText,
                  opacity: op,
                  transform: `scale(${scale})`,
                  textShadow: `0 0 14px ${accentColor}33`,
                  letterSpacing: 2,
                }}
              >
                {eq}
              </div>
            );
          })}
        </div>

        {caption && (
          <div
            style={{
              position: 'absolute',
              bottom: 80,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 32,
              color: theme.subtle,
              fontStyle: 'italic',
              opacity: interpolate(
                frame,
                [durationFrames - 200, durationFrames - 140],
                [0, 1],
                {extrapolateRight: 'clamp'}
              ),
            }}
          >
            {caption}
          </div>
        )}
      </div>
    </Background>
  );
};
