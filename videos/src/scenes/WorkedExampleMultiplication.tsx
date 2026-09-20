import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §9 — WORKED EXAMPLE 2
 * 5 × (−3) = −15 shown as 5 visual groups of three red blocks each.
 */
export const WorkedExampleMultiplication: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const fadeOut = interpolate(frame, [260, 290], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Пример 2: 5 × (−3) = ?" size={64} color={theme.power} y={80} />
        <Caption text="5 групи од −3" size={42} color={theme.negative} y={200} delay={30} />

        {/* 5 columns of 3 red squares */}
        <div
          style={{
            position: 'absolute',
            top: 360,
            left: 0,
            right: 0,
            display: 'flex',
            justifyContent: 'center',
            gap: 60,
          }}
        >
          {Array.from({length: 5}).map((_, gIdx) => {
            const delayBase = 60 + gIdx * 20;
            return (
              <div
                key={gIdx}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  gap: 14,
                  alignItems: 'center',
                }}
              >
                {Array.from({length: 3}).map((_, sIdx) => {
                  const delay = delayBase + sIdx * 6;
                  const f = Math.max(0, frame - delay);
                  const scale = spring({frame: f, fps, config: {damping: 14, mass: 0.4}});
                  const opacity = interpolate(f, [0, 12], [0, 1], {
                    extrapolateLeft: 'clamp',
                    extrapolateRight: 'clamp',
                  });
                  return (
                    <div
                      key={sIdx}
                      style={{
                        width: 96,
                        height: 96,
                        borderRadius: 14,
                        border: `3px solid ${theme.negative}`,
                        backgroundColor: `${theme.negative}55`,
                        opacity,
                        transform: `scale(${scale})`,
                      }}
                    />
                  );
                })}
                <div
                  style={{
                    fontFamily: FONT_FAMILY,
                    fontSize: 38,
                    color: theme.negative,
                    fontWeight: 700,
                    opacity: interpolate(frame, [delayBase + 20, delayBase + 35], [0, 1], {
                      extrapolateLeft: 'clamp',
                      extrapolateRight: 'clamp',
                    }),
                  }}
                >
                  −3
                </div>
              </div>
            );
          })}
        </div>

        {/* counted line */}
        <div
          style={{
            position: 'absolute',
            top: 800,
            left: 0,
            right: 0,
            textAlign: 'center',
            fontFamily: FONT_FAMILY,
            fontSize: 40,
            color: theme.negative,
            opacity: interpolate(frame, [180, 200], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          5 × 3 = 15 негативни блока
        </div>

        {/* final result */}
        {frame >= 215 && (
          <div
            style={{
              position: 'absolute',
              top: 900,
              left: 0,
              right: 0,
              textAlign: 'center',
              fontFamily: FONT_FAMILY,
              fontSize: 88,
              fontWeight: 700,
              color: theme.negative,
              opacity: interpolate(frame, [215, 235], [0, 1], {extrapolateRight: 'clamp'}),
              textShadow: `0 0 24px ${theme.negative}88`,
            }}
          >
            5 × (−3) = −15
          </div>
        )}
      </div>
    </Background>
  );
};
