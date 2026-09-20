import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {useEffect, useRef, useState} from 'react';
import rough from 'roughjs';
import {HandwriteText} from '../components/HandwriteText';

/**
 * BlackboardDemo — real "drawing on board" with stroke-by-stroke handwriting.
 *
 * Now uses HandwriteText (opentype.js → SVG paths → animated strokes).
 * Each character is drawn as the pen would draw it, not typed.
 *
 * 30s = 900 frames @ 30fps
 */

const BOARD = '#1f3d2c';
const CHALK = '#f5f5dc';
const CHALK_RED = '#ef9a9a';
const CHALK_YELLOW = '#fff59d';
const CHALK_DIM = '#a8a890';

export const BlackboardDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [840, 900], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Number line rough.js draws over frames 60–240
  const lineProgress = interpolate(frame, [60, 240], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Hop arrow draws over frames 540–720
  const arrowProgress = interpolate(frame, [540, 720], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        background: `radial-gradient(ellipse at center, ${BOARD} 0%, #15291e 80%)`,
        opacity: fadeOut,
        position: 'relative',
      }}
    >
      {/* chalk-dust texture */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'radial-gradient(circle at 20% 30%, rgba(255,255,255,0.04), transparent 40%),' +
            'radial-gradient(circle at 80% 70%, rgba(255,255,255,0.03), transparent 40%)',
          pointerEvents: 'none',
        }}
      />

      {/* Title written by hand */}
      <HandwriteText
        text="−5 + 3 = ?"
        x={680}
        y={180}
        fontSize={130}
        color={CHALK_YELLOW}
        strokeWidth={5}
        startFrame={20}
        framesPerChar={16}
      />

      {/* rough.js number line */}
      <ChalkNumberLine
        x1={240}
        x2={1680}
        y={620}
        min={-7}
        max={3}
        progress={lineProgress}
      />

      {/* Equation written by hand below the line */}
      <HandwriteText
        text="−5 + 3 = −2"
        x={620}
        y={840}
        fontSize={110}
        color={CHALK}
        strokeWidth={4}
        startFrame={270}
        framesPerChar={20}
      />

      {/* Hop arrow on the line */}
      {arrowProgress > 0 && (
        <ChalkHop
          fromXOnLine={-5}
          toXOnLine={-2}
          lineMin={-7}
          lineMax={3}
          x1={240}
          x2={1680}
          y={620}
          progress={arrowProgress}
        />
      )}
    </div>
  );
};

// ────────────────────────────────────────────────────────────────
// ChalkNumberLine — rough.js draws a chalk-textured number line
// ────────────────────────────────────────────────────────────────

const ChalkNumberLine: React.FC<{
  x1: number;
  x2: number;
  y: number;
  min: number;
  max: number;
  progress: number;
}> = ({x1, x2, y, min, max, progress}) => {
  const svgRef = useRef<SVGSVGElement>(null);
  const [linePaths, setLinePaths] = useState<string[]>([]);
  const [ticks, setTicks] = useState<Array<{d: string; n: number}>>([]);

  useEffect(() => {
    if (!svgRef.current) return;
    const rc = rough.svg(svgRef.current);

    // Main horizontal line
    const lineNode = rc.line(x1, y, x2, y, {
      roughness: 1.6,
      stroke: CHALK,
      strokeWidth: 4,
      bowing: 1.5,
    });
    setLinePaths(
      Array.from(lineNode.querySelectorAll('path')).map(
        (p) => p.getAttribute('d') || ''
      )
    );

    const tickList: Array<{d: string; n: number}> = [];
    for (let n = min; n <= max; n++) {
      const tickX = x1 + ((n - min) / (max - min)) * (x2 - x1);
      const node = rc.line(tickX, y - 18, tickX, y + 18, {
        roughness: 1.4,
        stroke: CHALK,
        strokeWidth: 3,
      });
      const d = Array.from(node.querySelectorAll('path'))
        .map((p) => p.getAttribute('d') || '')
        .join(' ');
      tickList.push({d, n});
    }
    setTicks(tickList);
  }, [x1, x2, y, min, max]);

  const totalLen = (x2 - x1) * 1.2;
  const drawn = totalLen * progress;

  return (
    <svg
      ref={svgRef}
      width="100%"
      height="100%"
      viewBox="0 0 1920 1080"
      style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
    >
      {linePaths.map((d, i) => (
        <path
          key={i}
          d={d}
          stroke={CHALK}
          strokeWidth={4}
          fill="none"
          strokeDasharray={totalLen}
          strokeDashoffset={totalLen - drawn}
          strokeLinecap="round"
        />
      ))}
      {progress > 0.55 &&
        ticks.map(({d, n}, i) => {
          const op = Math.max(
            0,
            Math.min(1, (progress - 0.55) * (ticks.length + 2) - i)
          );
          const labelX = x1 + ((n - min) / (max - min)) * (x2 - x1);
          return (
            <g key={n} opacity={op}>
              <path d={d} stroke={CHALK} strokeWidth={3} fill="none" />
              {/* Label as a small handwritten path via reusing HandwriteText is overkill;
                  for ticks we use regular SVG text but in chalk style. */}
              <text
                x={labelX}
                y={y + 70}
                textAnchor="middle"
                fontSize={36}
                fill={n === 0 ? CHALK_YELLOW : n < 0 ? CHALK_RED : CHALK_DIM}
                style={{fontFamily: 'serif', fontWeight: 400}}
              >
                {n}
              </text>
            </g>
          );
        })}
    </svg>
  );
};

// ────────────────────────────────────────────────────────────────
// ChalkHop — yellow chalk arc that draws live across the line
// ────────────────────────────────────────────────────────────────

const ChalkHop: React.FC<{
  fromXOnLine: number;
  toXOnLine: number;
  lineMin: number;
  lineMax: number;
  x1: number;
  x2: number;
  y: number;
  progress: number;
}> = ({fromXOnLine, toXOnLine, lineMin, lineMax, x1, x2, y, progress}) => {
  const fromX = x1 + ((fromXOnLine - lineMin) / (lineMax - lineMin)) * (x2 - x1);
  const toX = x1 + ((toXOnLine - lineMin) / (lineMax - lineMin)) * (x2 - x1);
  const midX = (fromX + toX) / 2;
  const arcTopY = y - 130;
  const pathLength = 400;
  const drawn = pathLength * progress;

  return (
    <svg
      width="100%"
      height="100%"
      viewBox="0 0 1920 1080"
      style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
    >
      <path
        d={`M ${fromX} ${y} Q ${midX} ${arcTopY} ${toX} ${y}`}
        stroke={CHALK_YELLOW}
        strokeWidth={5}
        fill="none"
        strokeDasharray={pathLength}
        strokeDashoffset={pathLength - drawn}
        strokeLinecap="round"
        style={{filter: 'drop-shadow(0 0 6px rgba(255,245,157,0.4))'}}
      />
      {progress >= 0.95 && (
        <polygon
          points={`${toX},${y} ${toX - 20},${y - 10} ${toX - 20},${y + 10}`}
          fill={CHALK_YELLOW}
        />
      )}
    </svg>
  );
};
