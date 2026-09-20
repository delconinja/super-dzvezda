import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * §21 FINAL THOUGHT — one memorable line, lingering.
 * "Формулите се рецепти, равенките се рамнотежа,
 *  а променливите се тајни што ги откриваме чекор по чекор."
 * 25s = 750 frames
 */
export const FinalThought: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [690, 750], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const lines = [
    {text: 'Формулите се ',           accent: 'рецепти',   color: theme.zero},
    {text: 'Равенките се ',           accent: 'рамнотежа', color: theme.prime},
    {text: 'А променливите се ',      accent: 'тајни',     color: '#ffd54f'},
    {text: 'што ги откриваме ',       accent: 'чекор по чекор', color: theme.positive},
  ];

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%', position: 'relative'}}>
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            gap: 40,
          }}
        >
          {lines.map((l, i) => {
            const delay = 60 + i * 90;
            const op = interpolate(frame, [delay, delay + 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const scale = spring({
              frame: Math.max(0, frame - delay),
              fps,
              config: {damping: 14, mass: 0.6},
            });
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT_FAMILY,
                  fontSize: 56,
                  color: theme.whiteText,
                  fontWeight: 500,
                  opacity: op,
                  transform: `scale(${scale})`,
                  textAlign: 'center',
                }}
              >
                {l.text}
                <span style={{color: l.color, fontWeight: 700, textShadow: `0 0 22px ${l.color}88`}}>
                  {l.accent}
                </span>
                {i < lines.length - 1 ? '.' : '.'}
              </div>
            );
          })}
        </div>
      </div>
    </Background>
  );
};
