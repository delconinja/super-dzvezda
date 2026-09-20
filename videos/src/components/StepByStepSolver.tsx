import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {theme, FONT_FAMILY} from '../theme';

export type SolveStep = {
  expr: string;        // LaTeX-ish text, e.g. "3x + 2 = x + 10"
  note?: string;       // optional rationale shown below, e.g. "одземаме x од двете страни"
  highlight?: boolean; // if true: glowing emphasis (use for final answer)
};

/**
 * Generic step-by-step equation solver.
 * Each step appears with a fade+slide and stays on screen.
 * The final step gets a highlight glow.
 *
 * Beats it serves:
 *   §8  Simplify: 2(3x − 4) + x + 5 = 7x − 3
 *   §15 Solve: 2(x + 3) = 14 → x = 4
 *   §16 Solve: 3x + 2 = x + 10 → x = 4
 *   §17 Solve: 3(x − 2) + 4 = 2(x + 1) + 5 → x = 9
 *   §19 Mini challenge: 4y − 2(y − 5) = 18 → y = 4
 */
export const StepByStepSolver: React.FC<{
  title: string;
  steps: SolveStep[];
  durationFrames: number;
  accentColor?: string;
}> = ({title, steps, durationFrames, accentColor = theme.zero}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [durationFrames - 60, durationFrames - 10], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // 0-45 frames: title appears
  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Distribute steps evenly across the duration after title
  const stepRegionStart = 60;
  const stepRegionEnd = durationFrames - 60;
  const stepRegionLen = stepRegionEnd - stepRegionStart;
  const stepGap = stepRegionLen / steps.length;

  return (
    <div
      style={{
        opacity: fadeOut,
        width: '100%',
        height: '100%',
        position: 'relative',
        backgroundColor: theme.bg,
      }}
    >
      {/* title */}
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

      {/* steps stacked */}
      <div
        style={{
          position: 'absolute',
          top: 260,
          left: 0,
          right: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 32,
        }}
      >
        {steps.map((step, i) => {
          const stepEntry = stepRegionStart + i * stepGap;
          const f = Math.max(0, frame - stepEntry);
          const opacity = interpolate(f, [0, 25], [0, 1], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          const dx = interpolate(f, [0, 30], [-40, 0], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          });
          const scale = step.highlight
            ? spring({frame: f, fps, config: {damping: 12, mass: 0.55}})
            : 1;
          const color = step.highlight ? theme.prime : theme.whiteText;
          const glow = step.highlight ? `0 0 24px ${theme.prime}99` : 'none';

          return (
            <div
              key={i}
              style={{
                opacity,
                transform: `translateX(${dx}px) scale(${scale})`,
                fontFamily: FONT_FAMILY,
                textAlign: 'center',
                display: 'flex',
                flexDirection: 'column',
                gap: 6,
              }}
            >
              <div
                style={{
                  fontSize: step.highlight ? 72 : 54,
                  fontWeight: step.highlight ? 700 : 600,
                  color,
                  textShadow: glow,
                  letterSpacing: 1,
                }}
              >
                {step.expr}
              </div>
              {step.note ? (
                <div
                  style={{
                    fontSize: 26,
                    color: theme.subtle,
                    fontStyle: 'italic',
                  }}
                >
                  {step.note}
                </div>
              ) : null}
            </div>
          );
        })}
      </div>
    </div>
  );
};
