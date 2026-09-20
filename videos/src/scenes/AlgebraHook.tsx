import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * m8-2-1 §1 HOOK (60s = 1800 frames @ 30fps)
 *
 * Narrative beats:
 *   0–6s   Pure darkness, room slowly fades in (a few distant stars/particles)
 *   6–14s  "Замисли темна, мистериозна соба..."  (caption fades in)
 *   14–22s Single letter "x" emerges from the dark, glowing
 *   22–32s More letters drift in: y, n, a, k, b — each from a different direction
 *   32–44s Letters arrange into a loose pattern, gently floating
 *   44–55s Title appears: "Изрази, равенки и формули"
 *   55–60s Hold + fade out
 */
export const AlgebraHook: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [1700, 1800], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Background atmosphere: drifting dust particles
  const particles = Array.from({length: 25}).map((_, i) => ({
    x: ((i * 137) % 1920),
    y: ((i * 211) % 1080),
    drift: Math.sin((frame + i * 50) / 60) * 18,
    op: interpolate(frame, [60, 180], [0, 0.4], {extrapolateRight: 'clamp'}),
  }));

  const captionOp = interpolate(frame, [180, 280], [0, 1], {extrapolateRight: 'clamp'});
  const captionOut = interpolate(frame, [1200, 1300], [1, 0], {extrapolateRight: 'clamp'});

  // Letters with their target positions and entry times
  const letters = [
    {ch: 'x', x: 480, y: 720, color: '#ffd54f', entry: 420},
    {ch: 'y', x: 1440, y: 720, color: '#4fc3f7', entry: 510},
    {ch: 'n', x: 720, y: 540, color: '#ba68c8', entry: 600},
    {ch: 'a', x: 1200, y: 540, color: '#81c784', entry: 690},
    {ch: 'k', x: 960, y: 880, color: '#ffb74d', entry: 780},
    {ch: 'b', x: 960, y: 400, color: '#e57373', entry: 870},
  ];

  // Title appears 44s in
  const titleOp = interpolate(frame, [1320, 1410], [0, 1], {extrapolateRight: 'clamp'});
  const titleScale = spring({
    frame: Math.max(0, frame - 1320),
    fps,
    config: {damping: 16, mass: 0.7},
  });

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        {/* drifting dust particles for atmosphere */}
        {particles.map((p, i) => (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: p.x + p.drift,
              top: p.y,
              width: 4,
              height: 4,
              borderRadius: '50%',
              backgroundColor: '#ffffff',
              opacity: p.op * (0.4 + Math.sin((frame + i * 7) / 30) * 0.3),
              boxShadow: '0 0 8px #ffffff',
            }}
          />
        ))}

        {/* mystery caption */}
        <div
          style={{
            position: 'absolute',
            top: 300,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 38,
            color: '#90a4ae',
            opacity: captionOp * captionOut,
            fontStyle: 'italic',
            lineHeight: 1.5,
          }}
        >
          Замисли темна, мистериозна соба...<br />
          полна со светкави знаци и обрасци.
        </div>

        {/* floating letters */}
        {letters.map((l, i) => {
          const f = Math.max(0, frame - l.entry);
          const scale = spring({frame: f, fps, config: {damping: 14, mass: 0.6}});
          const opacity = interpolate(f, [0, 30], [0, 1], {extrapolateRight: 'clamp'});
          const drift = {
            x: Math.sin((frame + i * 35) / 40) * 14,
            y: Math.cos((frame + i * 35) / 50) * 10,
          };
          // soft pulse on glow
          const pulse = 0.6 + Math.sin((frame + i * 23) / 20) * 0.25;

          return (
            <div
              key={l.ch}
              style={{
                position: 'absolute',
                left: l.x + drift.x,
                top: l.y + drift.y,
                transform: `translate(-50%, -50%) scale(${scale})`,
                fontFamily: FONT_FAMILY,
                fontSize: 130,
                fontWeight: 700,
                color: l.color,
                opacity,
                textShadow: `0 0 ${30 + pulse * 30}px ${l.color}, 0 0 ${60 + pulse * 40}px ${l.color}88`,
              }}
            >
              {l.ch}
            </div>
          );
        })}

        {/* title appears late */}
        <div
          style={{
            position: 'absolute',
            top: 140,
            left: 0,
            right: 0,
            textAlign: 'center',
            opacity: titleOp,
            transform: `scale(${titleScale})`,
            fontFamily: FONT_FAMILY,
            fontSize: 92,
            fontWeight: 700,
            color: theme.zero,
            textShadow: `0 0 30px ${theme.zero}88`,
          }}
        >
          Изрази, равенки и формули
        </div>
      </div>
    </Background>
  );
};
