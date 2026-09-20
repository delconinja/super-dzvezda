import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {theme, FONT_FAMILY} from '../theme';

export type SignRule = {
  expr: string;
  result: 'positive' | 'negative';
};

/**
 * Generic sign-rules panel — used for both addition and multiplication beats.
 * Shows the rule explanation + 4 worked examples.
 */
export const SignRulesPanel: React.FC<{
  title: string;
  ruleSame: string;        // e.g. "Ист знак → собери, задржи знак"
  ruleDifferent: string;   // e.g. "Различни знаци → одземи, задржи знак на поголемиот"
  examples: SignRule[];    // 4 examples, mixed signs
  durationFrames: number;
}> = ({title, ruleSame, ruleDifferent, examples, durationFrames}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(
    frame,
    [durationFrames - 60, durationFrames - 10],
    [1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
  );

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const sameOp = interpolate(frame, [60, 120], [0, 1], {extrapolateRight: 'clamp'});
  const diffOp = interpolate(frame, [220, 280], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 80,
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

        {/* Rule 1 */}
        <div
          style={{
            position: 'absolute',
            top: 220,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            color: theme.positive,
            opacity: sameOp,
          }}
        >
          <strong style={{color: theme.positive}}>✓ Ист знак:</strong> {ruleSame}
        </div>

        {/* Rule 2 */}
        <div
          style={{
            position: 'absolute',
            top: 320,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            color: theme.negative,
            opacity: diffOp,
          }}
        >
          <strong style={{color: theme.negative}}>⚡ Различни знаци:</strong> {ruleDifferent}
        </div>

        {/* Examples in 2x2 grid */}
        <div
          style={{
            position: 'absolute',
            top: 480,
            left: 0,
            right: 0,
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: 40,
            padding: '0 240px',
          }}
        >
          {examples.map((ex, i) => {
            const delay = 360 + i * 80;
            const f = Math.max(0, frame - delay);
            const op = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
            const scale = spring({frame: f, fps, config: {damping: 12, mass: 0.5}});
            const colour = ex.result === 'positive' ? theme.positive : theme.negative;
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT_FAMILY,
                  fontSize: 56,
                  fontWeight: 700,
                  color: colour,
                  textAlign: 'center',
                  opacity: op,
                  transform: `scale(${scale})`,
                  padding: '20px 0',
                  border: `2px solid ${colour}55`,
                  borderRadius: 16,
                  background: `${colour}11`,
                  textShadow: `0 0 14px ${colour}66`,
                }}
              >
                {ex.expr}
              </div>
            );
          })}
        </div>
      </div>
    </Background>
  );
};
