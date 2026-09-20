import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §7 — POWERS AND ROOTS
 * Powers: 2^1, 2^2, 2^3, 2^4 chips growing in size.
 * Roots: equations √16=4, √9=3, √4=2 fade in sequentially in teal.
 */
export const PowersRoots: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [320, 360], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const powers = [
    {exp: 1, val: 2},
    {exp: 2, val: 4},
    {exp: 3, val: 8},
    {exp: 4, val: 16},
  ];

  const showPowers = frame < 180;
  const showRoots = frame >= 180;

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Степени и корени" size={64} color={theme.power} y={80} />

        {showPowers && (
          <>
            <Caption text="Степени растат..." size={38} color={theme.power} y={170} delay={15} />
            {powers.map((p, i) => {
              const delay = 30 + i * 30;
              const f = Math.max(0, frame - delay);
              const scale = spring({frame: f, fps, config: {damping: 12, mass: 0.6}});
              const size = 60 + i * 35;
              const cx = 360 + i * 380;
              return (
                <div
                  key={i}
                  style={{
                    position: 'absolute',
                    left: cx,
                    top: 540,
                    transform: `translate(-50%, -50%) scale(${scale})`,
                    width: size * 1.6,
                    height: size * 1.6,
                    borderRadius: '50%',
                    border: `4px solid ${theme.power}`,
                    backgroundColor: `${theme.bg}cc`,
                    boxShadow: `0 0 30px ${theme.power}88`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontFamily: FONT_FAMILY,
                    color: theme.power,
                    fontSize: size,
                    fontWeight: 700,
                  }}
                >
                  {p.val}
                </div>
              );
            })}
            {powers.map((p, i) => {
              const delay = 35 + i * 30;
              const opacity = interpolate(frame, [delay, delay + 15], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              });
              const cx = 360 + i * 380;
              return (
                <div
                  key={'lab' + i}
                  style={{
                    position: 'absolute',
                    left: cx,
                    top: 820,
                    transform: 'translateX(-50%)',
                    fontFamily: FONT_FAMILY,
                    fontSize: 38,
                    color: theme.power,
                    opacity,
                  }}
                >
                  2<sup>{p.exp}</sup>
                </div>
              );
            })}
          </>
        )}

        {showRoots && (
          <>
            <Caption
              text="Корени се враќаат назад..."
              size={38}
              color={theme.root}
              y={170}
              delay={185}
            />
            {[
              {eq: '√16 = 4'},
              {eq: '√9 = 3'},
              {eq: '√4 = 2'},
            ].map((r, i) => {
              const delay = 200 + i * 30;
              const opacity = interpolate(frame, [delay, delay + 18], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              });
              return (
                <div
                  key={i}
                  style={{
                    position: 'absolute',
                    top: 380 + i * 110,
                    left: 0,
                    right: 0,
                    textAlign: 'center',
                    fontFamily: FONT_FAMILY,
                    fontSize: 72,
                    fontWeight: 700,
                    color: theme.root,
                    opacity,
                    textShadow: `0 0 18px ${theme.root}66`,
                  }}
                >
                  {r.eq}
                </div>
              );
            })}
          </>
        )}
      </div>
    </Background>
  );
};
