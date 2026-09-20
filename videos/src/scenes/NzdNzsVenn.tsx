import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §7 NZD and NZS demo
 * Two overlapping sets, the overlap highlights NZD (12 & 18 → 6)
 * Then second pane: NZS for 4 & 6 → 12 via the multiples-sequence
 * 35s = 1050 frames
 */
const VAR1 = theme.zero;
const VAR2 = theme.power;
const COMMON = theme.prime;

export const NzdNzsVenn: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [990, 1050], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

  // PHASE 1 (0-500f): NZD of 12 & 18
  // Phase 2 (520-1000f): NZS of 4 & 6
  const phase = frame < 520 ? 1 : 2;
  const phaseStart = phase === 1 ? 0 : 520;
  const local = frame - phaseStart;

  if (phase === 1) {
    // Factors of 12: 1, 2, 3, 4, 6, 12
    // Factors of 18: 1, 2, 3, 6, 9, 18
    // Common: 1, 2, 3, 6  →  NZD = 6
    const leftOp = interpolate(local, [40, 100], [0, 1], {extrapolateRight: 'clamp'});
    const rightOp = interpolate(local, [150, 210], [0, 1], {extrapolateRight: 'clamp'});
    const overlapOp = interpolate(local, [280, 340], [0, 1], {extrapolateRight: 'clamp'});
    const answerOp = interpolate(local, [400, 460], [0, 1], {extrapolateRight: 'clamp'});

    const onlyA = [4, 12];
    const onlyB = [9, 18];
    const common = [1, 2, 3, 6];

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
              color: theme.prime,
              opacity: titleOp,
            }}
          >
            НЗД — Најголем заеднички делител на 12 и 18
          </div>

          {/* Two big set headers */}
          <div
            style={{
              position: 'absolute',
              top: 240,
              left: 360,
              fontFamily: FONT_FAMILY,
              fontSize: 36,
              color: VAR1,
              opacity: leftOp,
            }}
          >
            Делители на 12
          </div>
          <div
            style={{
              position: 'absolute',
              top: 240,
              right: 360,
              fontFamily: FONT_FAMILY,
              fontSize: 36,
              color: VAR2,
              opacity: rightOp,
              textAlign: 'right',
            }}
          >
            Делители на 18
          </div>

          {/* Left only */}
          <Chips xs={onlyA} colour={VAR1} top={320} left={360} opacity={leftOp} />
          {/* Right only */}
          <Chips xs={onlyB} colour={VAR2} top={320} right={360} opacity={rightOp} />

          {/* Common */}
          <div
            style={{
              position: 'absolute',
              top: 530,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 30,
              color: COMMON,
              opacity: overlapOp,
            }}
          >
            ⤵ Заеднички делители ⤵
          </div>
          <div
            style={{
              position: 'absolute',
              top: 600,
              left: 0,
              right: 0,
              display: 'flex',
              justifyContent: 'center',
              gap: 24,
              opacity: overlapOp,
            }}
          >
            {common.map((n, i) => (
              <div
                key={n}
                style={{
                  width: 110,
                  height: 110,
                  borderRadius: 20,
                  border: `3px solid ${COMMON}`,
                  background: `${COMMON}22`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: FONT_FAMILY,
                  fontSize: 56,
                  fontWeight: 700,
                  color: COMMON,
                  textShadow: `0 0 14px ${COMMON}aa`,
                  transform: `scale(${spring({frame: Math.max(0, local - 280 - i * 30), fps, config: {damping: 12, mass: 0.5}})})`,
                }}
              >
                {n}
              </div>
            ))}
          </div>

          {/* NZD answer */}
          <div
            style={{
              position: 'absolute',
              top: 800,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 80,
              fontWeight: 700,
              color: COMMON,
              opacity: answerOp,
              transform: `scale(${spring({frame: Math.max(0, local - 400), fps, config: {damping: 12}})})`,
              textShadow: `0 0 28px ${COMMON}aa`,
            }}
          >
            НЗД(12, 18) = 6
          </div>
        </div>
      </Background>
    );
  }

  // PHASE 2: NZS of 4 & 6 → 12
  const titleOp2 = interpolate(local, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
  const row1Op = interpolate(local, [60, 120], [0, 1], {extrapolateRight: 'clamp'});
  const row2Op = interpolate(local, [180, 240], [0, 1], {extrapolateRight: 'clamp'});
  const ansOp = interpolate(local, [320, 380], [0, 1], {extrapolateRight: 'clamp'});

  const mults4 = [4, 8, 12, 16, 20];
  const mults6 = [6, 12, 18, 24];

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
            color: theme.prime,
            opacity: titleOp2,
          }}
        >
          НЗС — Најмал заеднички содржател на 4 и 6
        </div>

        <div
          style={{
            position: 'absolute',
            top: 280,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            color: VAR1,
            opacity: row1Op,
          }}
        >
          Содржатели на 4:&nbsp;
          {mults4.map((n) => (
            <span
              key={n}
              style={{
                color: n === 12 ? COMMON : VAR1,
                fontWeight: n === 12 ? 700 : 400,
                fontSize: n === 12 ? 56 : 42,
                margin: '0 12px',
                textShadow: n === 12 ? `0 0 18px ${COMMON}aa` : 'none',
              }}
            >
              {n}
            </span>
          ))}
          <span style={{color: theme.subtle}}>…</span>
        </div>

        <div
          style={{
            position: 'absolute',
            top: 460,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 36,
            color: VAR2,
            opacity: row2Op,
          }}
        >
          Содржатели на 6:&nbsp;
          {mults6.map((n) => (
            <span
              key={n}
              style={{
                color: n === 12 ? COMMON : VAR2,
                fontWeight: n === 12 ? 700 : 400,
                fontSize: n === 12 ? 56 : 42,
                margin: '0 12px',
                textShadow: n === 12 ? `0 0 18px ${COMMON}aa` : 'none',
              }}
            >
              {n}
            </span>
          ))}
          <span style={{color: theme.subtle}}>…</span>
        </div>

        <div
          style={{
            position: 'absolute',
            top: 720,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 80,
            fontWeight: 700,
            color: COMMON,
            opacity: ansOp,
            transform: `scale(${spring({frame: Math.max(0, local - 320), fps, config: {damping: 12}})})`,
            textShadow: `0 0 28px ${COMMON}aa`,
          }}
        >
          НЗС(4, 6) = 12
        </div>
      </div>
    </Background>
  );
};

const Chips: React.FC<{
  xs: number[];
  colour: string;
  top: number;
  left?: number;
  right?: number;
  opacity: number;
}> = ({xs, colour, top, left, right, opacity}) => (
  <div
    style={{
      position: 'absolute',
      top,
      ...(left !== undefined ? {left} : {}),
      ...(right !== undefined ? {right} : {}),
      display: 'flex',
      gap: 12,
      opacity,
    }}
  >
    {xs.map((n) => (
      <div
        key={n}
        style={{
          width: 80,
          height: 80,
          borderRadius: 14,
          border: `2px solid ${colour}`,
          background: `${colour}22`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: 'Noto Sans, sans-serif',
          fontSize: 40,
          fontWeight: 700,
          color: colour,
        }}
      >
        {n}
      </div>
    ))}
  </div>
);
