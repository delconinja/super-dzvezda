import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §1 HOOK — "Кеј, термометарот покажува −2, до пладне +5"
 * 30s = 900 frames.
 */
const POSITIVE = theme.positive;
const NEGATIVE = theme.negative;
const ZERO = theme.zero;

export const TempHook: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [840, 900], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const titleOp = interpolate(frame, [0, 40], [0, 1], {extrapolateRight: 'clamp'});
  const titleScale = spring({frame, fps, config: {damping: 14, mass: 0.6}});

  const thermOp = interpolate(frame, [80, 160], [0, 1], {extrapolateRight: 'clamp'});

  // mercury moves from -2 up to +5 between frames 240-540
  const tempValue = interpolate(frame, [240, 540], [-2, 5], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Thermometer geometry: vertical bar centered at x=960
  const THERM_X = 960;
  const THERM_TOP = 280;
  const THERM_BOTTOM = 820;
  const THERM_RANGE_MIN = -10;
  const THERM_RANGE_MAX = 10;
  const yForTemp = (t: number) =>
    THERM_BOTTOM -
    ((t - THERM_RANGE_MIN) / (THERM_RANGE_MAX - THERM_RANGE_MIN)) *
      (THERM_BOTTOM - THERM_TOP);

  const mercuryTopY = yForTemp(tempValue);
  const isCold = tempValue < 0;

  const questionOp = interpolate(frame, [600, 720], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        {/* Title */}
        <div
          style={{
            position: 'absolute',
            top: 100,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 64,
            fontWeight: 700,
            color: ZERO,
            opacity: titleOp,
            transform: `scale(${titleScale})`,
            textShadow: `0 0 20px ${ZERO}66`,
          }}
        >
          Утро на Кејот...
        </div>

        {/* Thermometer */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none', opacity: thermOp}}
        >
          {/* outer tube */}
          <rect
            x={THERM_X - 40}
            y={THERM_TOP - 20}
            width={80}
            height={THERM_BOTTOM - THERM_TOP + 40}
            rx={36}
            fill="none"
            stroke={theme.whiteText}
            strokeWidth={4}
          />
          {/* bulb */}
          <circle cx={THERM_X} cy={THERM_BOTTOM + 60} r={60} fill={isCold ? NEGATIVE : POSITIVE}
            opacity={0.9}
          />
          {/* mercury */}
          <rect
            x={THERM_X - 22}
            y={mercuryTopY}
            width={44}
            height={THERM_BOTTOM + 60 - mercuryTopY}
            fill={isCold ? NEGATIVE : POSITIVE}
            opacity={0.9}
          />
          {/* tick marks every 2 degrees */}
          {Array.from({length: 11}, (_, i) => -10 + i * 2).map((t) => {
            const y = yForTemp(t);
            const colour = t > 0 ? POSITIVE : t < 0 ? NEGATIVE : ZERO;
            return (
              <g key={t}>
                <line
                  x1={THERM_X + 50}
                  y1={y}
                  x2={THERM_X + 70}
                  y2={y}
                  stroke={colour}
                  strokeWidth={3}
                />
                <text
                  x={THERM_X + 90}
                  y={y + 10}
                  fill={colour}
                  fontFamily={FONT_FAMILY}
                  fontSize={28}
                  fontWeight={t === 0 ? 700 : 400}
                >
                  {t > 0 ? `+${t}` : t}°
                </text>
              </g>
            );
          })}
        </svg>

        {/* Current value label */}
        <div
          style={{
            position: 'absolute',
            top: yForTemp(tempValue) - 60,
            left: THERM_X - 280,
            fontFamily: FONT_FAMILY,
            fontSize: 56,
            fontWeight: 700,
            color: isCold ? NEGATIVE : POSITIVE,
            opacity: thermOp,
            textShadow: `0 0 18px ${(isCold ? NEGATIVE : POSITIVE)}aa`,
            transition: 'color 0.3s',
          }}
        >
          {tempValue >= 0 ? `+${Math.round(tempValue)}°` : `${Math.round(tempValue)}°`}
        </div>

        {/* Question */}
        <div
          style={{
            position: 'absolute',
            bottom: 80,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 44,
            color: ZERO,
            opacity: questionOp,
            fontStyle: 'italic',
          }}
        >
          Колку се „покачила" температурата?
        </div>
      </div>
    </Background>
  );
};
