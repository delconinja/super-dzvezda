import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Final closing scene — "Бројната права е наш патоказ — ... прошетка покрај Вардар, не маратон."
 * 25s = 750 frames
 */
export const MathPathFinal: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [690, 750], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const lines = [
    {text: 'Знакот ни кажува ',     accent: 'насока',        colour: theme.zero},
    {text: 'Степените нè качуваат по ', accent: 'скали',     colour: theme.power},
    {text: 'Корените нè ',           accent: 'враќаат назад', colour: theme.root},
    {text: 'Простите броеви се ',    accent: 'тулите',        colour: theme.prime},
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
            fontSize: 64,
            fontWeight: 700,
            color: theme.positive,
            opacity: interpolate(frame, [0, 40], [0, 1], {extrapolateRight: 'clamp'}),
            textShadow: `0 0 20px ${theme.positive}66`,
          }}
        >
          Бројната права е наш патоказ.
        </div>

        <div
          style={{
            position: 'absolute',
            top: 280,
            left: 0,
            right: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 30,
          }}
        >
          {lines.map((l, i) => {
            const delay = 80 + i * 90;
            const op = interpolate(frame, [delay, delay + 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const scale = spring({frame: Math.max(0, frame - delay), fps, config: {damping: 14, mass: 0.6}});
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT_FAMILY,
                  fontSize: 48,
                  color: theme.whiteText,
                  opacity: op,
                  transform: `scale(${scale})`,
                  textAlign: 'center',
                }}
              >
                {l.text}
                <span
                  style={{
                    color: l.colour,
                    fontWeight: 700,
                    textShadow: `0 0 18px ${l.colour}88`,
                  }}
                >
                  {l.accent}
                </span>
                .
              </div>
            );
          })}
        </div>

        <div
          style={{
            position: 'absolute',
            bottom: 100,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 40,
            color: theme.prime,
            fontStyle: 'italic',
            opacity: interpolate(frame, [560, 640], [0, 1], {extrapolateRight: 'clamp'}),
            textShadow: `0 0 18px ${theme.prime}66`,
          }}
        >
          Математиката е прошетка покрај Вардар, не маратон.
        </div>
      </div>
    </Background>
  );
};
