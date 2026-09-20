import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §2 Variables vs constants
 * "Буквите x, y, a, b се променливи. Бројот π или 5 е константа."
 * 35s = 1050 frames
 */
export const VariablesIntro: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Title appears
  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Left column: VARIABLES (yellow)
  const varColOp = interpolate(frame, [60, 120], [0, 1], {extrapolateRight: 'clamp'});
  const varLabelOp = interpolate(frame, [120, 180], [0, 1], {extrapolateRight: 'clamp'});

  // Right column: CONSTANTS (blue)
  const constColOp = interpolate(frame, [420, 480], [0, 1], {extrapolateRight: 'clamp'});
  const constLabelOp = interpolate(frame, [480, 540], [0, 1], {extrapolateRight: 'clamp'});

  // Demo: x can change value
  const xValueChange = Math.floor(interpolate(frame, [600, 900], [3, 7], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  }));
  const demoOp = interpolate(frame, [600, 660], [0, 1], {extrapolateRight: 'clamp'});

  const variables = ['x', 'y', 'a', 'b', 'n'];
  const constants = ['π', '5', '3.14', '−7'];

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
            fontSize: 52,
            color: theme.zero,
            fontWeight: 700,
            opacity: titleOp,
          }}
        >
          Букви во алгебра
        </div>

        {/* LEFT: VARIABLES */}
        <div
          style={{
            position: 'absolute',
            left: 280,
            top: 280,
            opacity: varColOp,
            fontFamily: FONT_FAMILY,
            textAlign: 'center',
          }}
        >
          <div
            style={{
              fontSize: 36,
              fontWeight: 700,
              color: '#ffd54f',
              marginBottom: 24,
              opacity: varLabelOp,
            }}
          >
            ПРОМЕНЛИВИ
          </div>
          <div style={{display: 'flex', gap: 36, justifyContent: 'center'}}>
            {variables.map((v, i) => {
              const f = Math.max(0, frame - (60 + i * 40));
              const scale = spring({frame: f, fps, config: {damping: 13, mass: 0.5}});
              return (
                <div
                  key={v}
                  style={{
                    transform: `scale(${scale})`,
                    fontSize: 96,
                    fontWeight: 700,
                    color: '#ffd54f',
                    textShadow: '0 0 25px #ffd54f88',
                  }}
                >
                  {v}
                </div>
              );
            })}
          </div>
          <div
            style={{
              marginTop: 28,
              fontSize: 26,
              color: theme.subtle,
              fontStyle: 'italic',
              opacity: varLabelOp,
            }}
          >
            тајни што ги откриваме
          </div>
        </div>

        {/* RIGHT: CONSTANTS */}
        <div
          style={{
            position: 'absolute',
            right: 280,
            top: 280,
            opacity: constColOp,
            fontFamily: FONT_FAMILY,
            textAlign: 'center',
          }}
        >
          <div
            style={{
              fontSize: 36,
              fontWeight: 700,
              color: theme.zero,
              marginBottom: 24,
              opacity: constLabelOp,
            }}
          >
            КОНСТАНТИ
          </div>
          <div style={{display: 'flex', gap: 28, justifyContent: 'center'}}>
            {constants.map((c, i) => {
              const f = Math.max(0, frame - (420 + i * 40));
              const scale = spring({frame: f, fps, config: {damping: 13, mass: 0.5}});
              return (
                <div
                  key={c}
                  style={{
                    transform: `scale(${scale})`,
                    fontSize: 80,
                    fontWeight: 700,
                    color: theme.zero,
                    textShadow: `0 0 25px ${theme.zero}88`,
                  }}
                >
                  {c}
                </div>
              );
            })}
          </div>
          <div
            style={{
              marginTop: 28,
              fontSize: 26,
              color: theme.subtle,
              fontStyle: 'italic',
              opacity: constLabelOp,
            }}
          >
            фиксни вредности
          </div>
        </div>

        {/* Demo: x is changing */}
        <div
          style={{
            position: 'absolute',
            bottom: 80,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 44,
            color: '#ffd54f',
            opacity: demoOp,
          }}
        >
          Денес x = <span style={{fontSize: 60, color: theme.prime, fontWeight: 700, textShadow: '0 0 18px #ffd54f88'}}>{xValueChange}</span>,
          утре x = <span style={{fontSize: 60, color: theme.prime, fontWeight: 700, textShadow: '0 0 18px #ffd54f88'}}>?</span>
        </div>
      </div>
    </Background>
  );
};
