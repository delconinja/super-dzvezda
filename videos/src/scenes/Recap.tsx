import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §10 — RECAP
 * Four-bullet summary using the locked palette colors, then a closing line.
 */
export const Recap: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [240, 270], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const bullets: {text: string; color: string}[] = [
    {text: '• Цели броеви: позитивни, негативни и нула', color: theme.positive},
    {text: '• Истите знаци се обединуваат, различни се судираат', color: theme.negative},
    {text: '• Простите броеви се градивните блокови', color: theme.prime},
    {text: '• Степени растат, корени се враќаат', color: theme.power},
  ];

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Резиме" size={88} color={theme.zero} y={120} />

        <div
          style={{
            position: 'absolute',
            top: 320,
            left: 200,
            right: 200,
            display: 'flex',
            flexDirection: 'column',
            gap: 32,
          }}
        >
          {bullets.map((b, i) => {
            const delay = 30 + i * 30;
            const opacity = interpolate(frame, [delay, delay + 20], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const dx = interpolate(frame, [delay, delay + 25], [-50, 0], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            return (
              <div
                key={i}
                style={{
                  fontFamily: FONT_FAMILY,
                  fontSize: 42,
                  color: b.color,
                  opacity,
                  transform: `translateX(${dx}px)`,
                  fontWeight: 600,
                }}
              >
                {b.text}
              </div>
            );
          })}
        </div>

        {/* closing line */}
        <div
          style={{
            position: 'absolute',
            bottom: 160,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 54,
            fontWeight: 700,
            color: theme.prime,
            opacity: interpolate(frame, [180, 210], [0, 1], {extrapolateRight: 'clamp'}),
            textShadow: `0 0 18px ${theme.prime}66`,
          }}
        >
          Сега ги познаваш тајните на броевите!
        </div>
      </div>
    </Background>
  );
};
