import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * m8-2-1 §4 BALANCE SCALE — formulas as a rule that keeps things equal (75s = 2250 frames).
 *
 * Narrative beats:
 *   0–8s    Caption sets up: "Формулите се правила што одржуваат рамнотежа..."
 *   8–22s   Scale draws in (base, beam, pans), starts level
 *   22–35s  Left pan: 'x + 5' appears. Right pan: '12'. Scale stays balanced.
 *   35–50s  Both sides labeled; arrow shows "must stay equal"
 *   50–65s  Tip: take 5 off the left, scale would tip — show wobble + recovery
 *   65–75s  Caption: "Што правиме на едната страна, мора и на другата."
 */
export const BalanceScale: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [2160, 2250], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // 0-8s: setup caption
  const setupOp = interpolate(frame, [30, 150], [0, 1], {extrapolateRight: 'clamp'});
  const setupOut = interpolate(frame, [600, 720], [1, 0], {extrapolateRight: 'clamp'});

  // 8-22s: scale draws in
  const baseOp = interpolate(frame, [240, 330], [0, 1], {extrapolateRight: 'clamp'});
  const beamOp = interpolate(frame, [330, 440], [0, 1], {extrapolateRight: 'clamp'});

  // 22-35s: contents appear
  const leftOp = interpolate(frame, [660, 780], [0, 1], {extrapolateRight: 'clamp'});
  const rightOp = interpolate(frame, [780, 900], [0, 1], {extrapolateRight: 'clamp'});

  // 35-50s: "must stay equal" arrow
  const eqArrowOp = interpolate(frame, [1050, 1170], [0, 1], {extrapolateRight: 'clamp'});
  const eqArrowOut = interpolate(frame, [1400, 1500], [1, 0], {extrapolateRight: 'clamp'});

  // 50-65s: wobble demo (scale tips left then recovers)
  // tilt angle in degrees as a function of frame
  let tilt = 0;
  if (frame >= 1500 && frame <= 1950) {
    const f = (frame - 1500) / 450; // 0..1
    // tip down then recover
    tilt = Math.sin(f * Math.PI * 2) * -8;
  }

  // 65-75s: closing caption
  const closingOp = interpolate(frame, [1950, 2070], [0, 1], {extrapolateRight: 'clamp'});

  // Scale geometry (in screen px)
  const centerX = 960;
  const baseY = 880;
  const beamY = 560;
  const beamHalf = 380;
  const panRadius = 110;

  // pan positions tilt with the beam
  const tiltRad = (tilt * Math.PI) / 180;
  const leftPan = {
    x: centerX - beamHalf * Math.cos(tiltRad),
    y: beamY + beamHalf * Math.sin(tiltRad),
  };
  const rightPan = {
    x: centerX + beamHalf * Math.cos(tiltRad),
    y: beamY - beamHalf * Math.sin(tiltRad),
  };

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        {/* setup caption */}
        <div
          style={{
            position: 'absolute',
            top: 120,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 50,
            fontWeight: 600,
            color: '#4fc3f7',
            opacity: setupOp * setupOut,
            textShadow: '0 0 18px #4fc3f766',
          }}
        >
          Формулите се правила
          <br />
          што одржуваат рамнотежа...
        </div>

        {/* SVG scale */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
        >
          {/* base + pillar */}
          <g opacity={baseOp}>
            <rect
              x={centerX - 90}
              y={baseY}
              width={180}
              height={28}
              fill="#90a4ae"
              rx={8}
            />
            <rect
              x={centerX - 14}
              y={beamY}
              width={28}
              height={baseY - beamY}
              fill="#90a4ae"
            />
            <circle cx={centerX} cy={beamY} r={20} fill="#cfd8dc" />
          </g>

          {/* beam */}
          <g opacity={beamOp}>
            <line
              x1={leftPan.x}
              y1={leftPan.y}
              x2={rightPan.x}
              y2={rightPan.y}
              stroke="#cfd8dc"
              strokeWidth={10}
              strokeLinecap="round"
            />
            {/* chains */}
            <line
              x1={leftPan.x}
              y1={leftPan.y}
              x2={leftPan.x}
              y2={leftPan.y + 90}
              stroke="#78909c"
              strokeWidth={3}
            />
            <line
              x1={rightPan.x}
              y1={rightPan.y}
              x2={rightPan.x}
              y2={rightPan.y + 90}
              stroke="#78909c"
              strokeWidth={3}
            />
            {/* pans */}
            <ellipse
              cx={leftPan.x}
              cy={leftPan.y + 100}
              rx={panRadius}
              ry={24}
              fill="#4fc3f7"
              opacity={0.7}
            />
            <ellipse
              cx={rightPan.x}
              cy={rightPan.y + 100}
              rx={panRadius}
              ry={24}
              fill="#81c784"
              opacity={0.7}
            />
          </g>
        </svg>

        {/* left pan content: x + 5 */}
        <div
          style={{
            position: 'absolute',
            left: leftPan.x,
            top: leftPan.y + 50,
            transform: 'translate(-50%, -50%)',
            opacity: leftOp,
            fontFamily: FONT_FAMILY,
            fontSize: 76,
            fontWeight: 700,
            color: '#ffd54f',
            textShadow: '0 0 18px #ffd54f88',
          }}
        >
          x + 5
        </div>

        {/* right pan content: 12 */}
        <div
          style={{
            position: 'absolute',
            left: rightPan.x,
            top: rightPan.y + 50,
            transform: 'translate(-50%, -50%)',
            opacity: rightOp,
            fontFamily: FONT_FAMILY,
            fontSize: 80,
            fontWeight: 700,
            color: '#4fc3f7',
            textShadow: '0 0 18px #4fc3f788',
          }}
        >
          12
        </div>

        {/* equals must hold — banner */}
        <div
          style={{
            position: 'absolute',
            top: 380,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 42,
            fontWeight: 600,
            color: '#ba68c8',
            opacity: eqArrowOp * eqArrowOut,
            textShadow: '0 0 14px #ba68c866',
          }}
        >
          ↔ двете страни мора да останат еднакви ↔
        </div>

        {/* closing caption */}
        <div
          style={{
            position: 'absolute',
            top: 80,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 48,
            fontWeight: 700,
            color: '#ba68c8',
            opacity: closingOp,
            textShadow: '0 0 18px #ba68c888',
          }}
        >
          Што правиме на едната страна,
          <br />
          мора и на другата.
        </div>
      </div>
    </Background>
  );
};
