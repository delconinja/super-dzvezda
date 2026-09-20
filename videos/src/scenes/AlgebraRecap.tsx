import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §20 RECAP — 6 takeaways with locked-color labels.
 * Heading "Денес научивме..." then bullet-list rises in sequence.
 * 30s = 900 frames
 */
export const AlgebraRecap: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [840, 900], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const titleOp = interpolate(frame, [0, 40], [0, 1], {extrapolateRight: 'clamp'});
  const titleScale = spring({frame, fps, config: {damping: 14, mass: 0.6}});

  const items = [
    {text: 'буквите како тајни броеви',           color: '#ffd54f'},
    {text: 'формулите како рецепти',               color: theme.zero},
    {text: 'функциите како машинки',               color: theme.power},
    {text: 'слични членови се собираат',           color: theme.positive},
    {text: 'рамнотежата мора да остане',           color: theme.prime},
    {text: 'внимавај на знаци кога има минус',     color: theme.negative},
  ];

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
            fontSize: 72,
            fontWeight: 700,
            color: theme.zero,
            opacity: titleOp,
            transform: `scale(${titleScale})`,
            textShadow: `0 0 22px ${theme.zero}88`,
          }}
        >
          Денес научивме...
        </div>

        <div
          style={{
            position: 'absolute',
            top: 280,
            left: 240,
            right: 240,
            display: 'flex',
            flexDirection: 'column',
            gap: 40,
          }}
        >
          {items.map((it, i) => {
            const delay = 80 + i * 80;
            const op = interpolate(frame, [delay, delay + 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const dx = interpolate(frame, [delay, delay + 40], [-60, 0], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 24,
                  fontFamily: FONT_FAMILY,
                  fontSize: 42,
                  color: it.color,
                  opacity: op,
                  transform: `translateX(${dx}px)`,
                  fontWeight: 600,
                  textShadow: `0 0 14px ${it.color}55`,
                }}
              >
                <span style={{fontSize: 30}}>●</span>
                <span>{it.text}</span>
              </div>
            );
          })}
        </div>
      </div>
    </Background>
  );
};
