import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Show a labelled list of numbers in a row of chips.
 * Used for:
 *   - "Делители на 12: 1, 2, 3, 4, 6, 12"
 *   - "Содржатели на 4: 4, 8, 12, 16, 20…"
 *   - "Заеднички делители на 12 и 18: 1, 2, 3, 6"
 */
export const NumberSetList: React.FC<{
  title: string;
  label: string;
  numbers: number[];
  trailingDots?: boolean;
  highlightLast?: boolean;
  highlightColor?: string;
  caption?: string;
  durationFrames: number;
}> = ({
  title,
  label,
  numbers,
  trailingDots = false,
  highlightLast = false,
  highlightColor = theme.prime,
  caption,
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

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const labelOp = interpolate(frame, [40, 90], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 110,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 56,
            fontWeight: 700,
            color: theme.zero,
            opacity: titleOp,
            textShadow: `0 0 18px ${theme.zero}66`,
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
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 40,
            color: theme.subtle,
            opacity: labelOp,
            letterSpacing: 1,
          }}
        >
          {label}
        </div>

        <div
          style={{
            position: 'absolute',
            top: 380,
            left: 0,
            right: 0,
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            alignItems: 'center',
            gap: 32,
            padding: '0 200px',
          }}
        >
          {numbers.map((n, i) => {
            const delay = 100 + i * 50;
            const f = Math.max(0, frame - delay);
            const scale = spring({frame: f, fps, config: {damping: 12, mass: 0.5}});
            const op = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
            const isHighlight = highlightLast && i === numbers.length - 1;
            const colour = isHighlight ? highlightColor : theme.whiteText;
            return (
              <div
                key={i}
                style={{
                  minWidth: 110,
                  height: 110,
                  borderRadius: 24,
                  border: `3px solid ${colour}88`,
                  background: isHighlight ? `${colour}33` : `${colour}11`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: FONT_FAMILY,
                  fontSize: 60,
                  fontWeight: 700,
                  color: colour,
                  opacity: op,
                  transform: `scale(${scale})`,
                  textShadow: isHighlight ? `0 0 18px ${colour}aa` : 'none',
                  padding: '0 18px',
                }}
              >
                {n}
              </div>
            );
          })}
          {trailingDots && (
            <div
              style={{
                fontFamily: FONT_FAMILY,
                fontSize: 80,
                color: theme.subtle,
                opacity: interpolate(
                  frame,
                  [100 + numbers.length * 50, 200 + numbers.length * 50],
                  [0, 1],
                  {extrapolateRight: 'clamp'}
                ),
              }}
            >
              …
            </div>
          )}
        </div>

        {caption && (
          <div
            style={{
              position: 'absolute',
              bottom: 100,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 32,
              color: theme.subtle,
              fontStyle: 'italic',
              opacity: interpolate(frame, [400, 480], [0, 1], {extrapolateRight: 'clamp'}),
            }}
          >
            {caption}
          </div>
        )}
      </div>
    </Background>
  );
};
