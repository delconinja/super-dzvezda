import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §17 Function as a machine
 * f(x) = 2x + 3
 * Inputs 1, -2 → outputs 5, -1
 * 35s = 1050 frames
 */
export const FunctionMachine: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // Machine appears
  const machineOp = interpolate(frame, [60, 150], [0, 1], {extrapolateRight: 'clamp'});
  const machineScale = spring({
    frame: Math.max(0, frame - 60),
    fps,
    config: {damping: 14, mass: 0.6},
  });

  // Function label
  const labelOp = interpolate(frame, [150, 210], [0, 1], {extrapolateRight: 'clamp'});

  // First demo: input 1 → 5  (frames 270-540)
  const demo1InputX = interpolate(frame, [300, 420], [380, 750], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const demo1Visible = frame >= 270 && frame < 660;
  const demo1OutputX = interpolate(frame, [440, 560], [1170, 1540], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Second demo: input -2 → -1  (frames 660-960)
  const demo2InputX = interpolate(frame, [690, 810], [380, 750], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const demo2Visible = frame >= 660;
  const demo2OutputX = interpolate(frame, [830, 950], [1170, 1540], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const MACHINE_X = 960;
  const MACHINE_Y = 540;

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
            fontWeight: 700,
            color: theme.power,
            opacity: titleOp,
          }}
        >
          Функцијата е машина
        </div>

        {/* Conveyor track */}
        <svg width={1920} height={1080} style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}>
          <line x1={200} y1={MACHINE_Y} x2={1720} y2={MACHINE_Y} stroke={theme.subtle} strokeWidth={4} strokeDasharray="14 8" opacity={machineOp * 0.6} />
        </svg>

        {/* Machine body */}
        <div
          style={{
            position: 'absolute',
            left: MACHINE_X,
            top: MACHINE_Y,
            transform: `translate(-50%, -50%) scale(${machineScale})`,
            opacity: machineOp,
            width: 360,
            height: 260,
            borderRadius: 28,
            background: `linear-gradient(135deg, ${theme.power} 0%, #5e35b1 100%)`,
            border: `4px solid ${theme.prime}`,
            boxShadow: `0 0 50px ${theme.power}99, inset 0 0 30px ${theme.bg}aa`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontFamily: FONT_FAMILY,
            color: theme.whiteText,
            fontSize: 64,
            fontWeight: 700,
            textShadow: '0 0 20px #ffffff66',
          }}
        >
          f(x) = 2x + 3
        </div>

        {/* Labels */}
        <div
          style={{
            position: 'absolute',
            left: 200,
            top: MACHINE_Y - 100,
            color: theme.positive,
            fontFamily: FONT_FAMILY,
            fontSize: 30,
            opacity: labelOp,
            fontWeight: 600,
          }}
        >
          ▶ ВЛЕЗ
        </div>
        <div
          style={{
            position: 'absolute',
            right: 200,
            top: MACHINE_Y - 100,
            color: theme.prime,
            fontFamily: FONT_FAMILY,
            fontSize: 30,
            opacity: labelOp,
            fontWeight: 600,
            textAlign: 'right',
          }}
        >
          ИЗЛЕЗ ▶
        </div>

        {/* Demo 1: 1 → 5 */}
        {demo1Visible && frame < 660 && (
          <>
            <div
              style={{
                position: 'absolute',
                left: demo1InputX,
                top: MACHINE_Y - 30,
                fontFamily: FONT_FAMILY,
                fontSize: 80,
                fontWeight: 700,
                color: theme.positive,
                textShadow: `0 0 25px ${theme.positive}88`,
                opacity: interpolate(frame, [270, 320], [0, 1], {extrapolateRight: 'clamp'}) *
                         interpolate(frame, [410, 430], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
              }}
            >
              1
            </div>
            <div
              style={{
                position: 'absolute',
                left: demo1OutputX,
                top: MACHINE_Y - 40,
                fontFamily: FONT_FAMILY,
                fontSize: 100,
                fontWeight: 700,
                color: theme.prime,
                textShadow: `0 0 30px ${theme.prime}aa`,
                opacity: interpolate(frame, [430, 470], [0, 1], {extrapolateRight: 'clamp'}),
              }}
            >
              5
            </div>
          </>
        )}

        {/* Demo 2: -2 → -1 */}
        {demo2Visible && (
          <>
            <div
              style={{
                position: 'absolute',
                left: demo2InputX,
                top: MACHINE_Y - 30,
                fontFamily: FONT_FAMILY,
                fontSize: 80,
                fontWeight: 700,
                color: theme.negative,
                textShadow: `0 0 25px ${theme.negative}88`,
                opacity: interpolate(frame, [660, 710], [0, 1], {extrapolateRight: 'clamp'}) *
                         interpolate(frame, [800, 820], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}),
              }}
            >
              −2
            </div>
            <div
              style={{
                position: 'absolute',
                left: demo2OutputX,
                top: MACHINE_Y - 40,
                fontFamily: FONT_FAMILY,
                fontSize: 100,
                fontWeight: 700,
                color: theme.negative,
                textShadow: `0 0 30px ${theme.negative}aa`,
                opacity: interpolate(frame, [820, 860], [0, 1], {extrapolateRight: 'clamp'}),
              }}
            >
              −1
            </div>
          </>
        )}

        {/* Caption */}
        <div
          style={{
            position: 'absolute',
            bottom: 100,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            color: theme.subtle,
            fontStyle: 'italic',
            opacity: interpolate(frame, [900, 960], [0, 1], {extrapolateRight: 'clamp'}),
          }}
        >
          Едно правило, еден излез за секој влез.
        </div>
      </div>
    </Background>
  );
};
