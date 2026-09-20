import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * m8-2-1 §2 GUIDE APPEARS (45s = 1350 frames @ 30fps)
 *
 * Narrative beats:
 *   0–6s    A warm glow pulses in the center — something is arriving
 *   6–12s   The guide materializes (stylized friendly orb with face)
 *   12–22s  Caption: "Здраво! Јас сум твојот водич..."
 *   22–32s  Magic key appears, glowing gold, rotating slowly
 *   32–42s  Caption: "...а ова е магичниот клуч на алгебрата."
 *   42–45s  Hold + fade
 */
export const GuideAppears: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [1260, 1350], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // 0-6s: pulsing glow announces arrival
  const arrivalPulse = interpolate(frame, [0, 180], [0, 1], {extrapolateRight: 'clamp'});
  const pulseBeat = 0.6 + Math.sin(frame / 12) * 0.4;

  // 6-12s: guide materializes
  const guideEntry = Math.max(0, frame - 180);
  const guideScale = spring({frame: guideEntry, fps, config: {damping: 13, mass: 0.7}});
  const guideOp = interpolate(guideEntry, [0, 80], [0, 1], {extrapolateRight: 'clamp'});

  // gentle bob after arrival
  const guideBob = Math.sin(frame / 24) * 14;

  // 12-22s: greeting caption
  const greetingOp = interpolate(frame, [360, 450], [0, 1], {extrapolateRight: 'clamp'});
  const greetingOut = interpolate(frame, [840, 930], [1, 0], {extrapolateRight: 'clamp'});

  // 22-32s: magic key appears
  const keyEntry = Math.max(0, frame - 660);
  const keyOp = interpolate(keyEntry, [0, 60], [0, 1], {extrapolateRight: 'clamp'});
  const keyScale = spring({frame: keyEntry, fps, config: {damping: 14, mass: 0.8}});
  const keyRotate = interpolate(frame, [660, 1350], [0, 360]);

  // 32-42s: reveal caption
  const revealOp = interpolate(frame, [960, 1050], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        {/* arrival glow halo */}
        <div
          style={{
            position: 'absolute',
            left: 760,
            top: 380,
            width: 400,
            height: 400,
            borderRadius: '50%',
            background: `radial-gradient(circle, ${theme.prime}66 0%, transparent 70%)`,
            opacity: arrivalPulse * pulseBeat,
            transform: 'translate(0, 0)',
          }}
        />

        {/* the guide — a friendly orb with face */}
        <div
          style={{
            position: 'absolute',
            left: 960,
            top: 580 + guideBob,
            width: 220,
            height: 220,
            borderRadius: '50%',
            background: `radial-gradient(circle at 30% 30%, ${theme.prime} 0%, #f57f17 60%, #e65100 100%)`,
            border: `3px solid ${theme.prime}`,
            transform: `translate(-50%, -50%) scale(${guideScale})`,
            opacity: guideOp,
            boxShadow: `0 0 50px ${theme.prime}cc, 0 0 100px ${theme.prime}66`,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 18,
          }}
        >
          {/* eyes */}
          <div style={{display: 'flex', gap: 38}}>
            <div style={{width: 22, height: 32, borderRadius: 12, background: '#0d1b2e'}} />
            <div style={{width: 22, height: 32, borderRadius: 12, background: '#0d1b2e'}} />
          </div>
          {/* smile */}
          <div
            style={{
              width: 70,
              height: 36,
              borderBottom: '6px solid #0d1b2e',
              borderRadius: '0 0 50% 50%',
            }}
          />
        </div>

        {/* greeting caption */}
        <div
          style={{
            position: 'absolute',
            top: 220,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 48,
            color: theme.prime,
            fontWeight: 600,
            opacity: greetingOp * greetingOut,
            textShadow: `0 0 18px ${theme.prime}66`,
          }}
        >
          Здраво! Јас сум твојот водич...
        </div>

        {/* magic key */}
        <div
          style={{
            position: 'absolute',
            left: 1320,
            top: 580 + Math.sin(frame / 30) * 12,
            transform: `translate(-50%, -50%) scale(${keyScale}) rotate(${keyRotate}deg)`,
            opacity: keyOp,
            fontSize: 200,
            filter: `drop-shadow(0 0 25px ${theme.prime}aa)`,
            color: theme.prime,
          }}
        >
          🗝
        </div>

        {/* reveal caption */}
        <div
          style={{
            position: 'absolute',
            top: 880,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 48,
            color: theme.prime,
            fontWeight: 700,
            opacity: revealOp,
            textShadow: `0 0 22px ${theme.prime}aa`,
          }}
        >
          ...а ова е магичниот клуч на алгебрата.
        </div>
      </div>
    </Background>
  );
};
