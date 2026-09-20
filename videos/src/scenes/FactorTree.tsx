import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {IntegerChip} from '../components/IntegerChip';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §5 — FACTORS AND MULTIPLES
 * Show factors of 12 fanned around the central chip; show multiples of 3 in a column.
 */
export const FactorTree: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [240, 270], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const factors = [1, 2, 3, 4, 6, 12];
  const multiples = [3, 6, 9, 12, 15, 18];
  const centerX = 620;
  const centerY = 600;

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Делители и содржатели" size={56} color={theme.prime} y={80} />
        <Caption text="Делители на 12" size={36} color={theme.prime} y={170} delay={20} />

        <IntegerChip
          value={12}
          size={90}
          delay={40}
          x={centerX}
          y={centerY}
          color={theme.zero}
        />

        {/* fan factors around 12 */}
        <svg
          width={1920}
          height={1080}
          style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
        >
          {factors.map((f, i) => {
            const angle = Math.PI * (0.55 + (i / (factors.length - 1)) * 0.9);
            const dx = Math.cos(angle) * 260;
            const dy = Math.sin(angle) * -180;
            const x = centerX + dx;
            const y = centerY + dy;
            const lineProgress = interpolate(frame, [70 + i * 8, 90 + i * 8], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            return (
              <line
                key={f}
                x1={centerX}
                y1={centerY}
                x2={centerX + dx * lineProgress}
                y2={centerY + dy * lineProgress}
                stroke={theme.subtle}
                strokeWidth={2}
                opacity={lineProgress}
              />
            );
          })}
        </svg>

        {factors.map((f, i) => {
          const angle = Math.PI * (0.55 + (i / (factors.length - 1)) * 0.9);
          const dx = Math.cos(angle) * 260;
          const dy = Math.sin(angle) * -180;
          return (
            <IntegerChip
              key={f}
              value={f}
              size={54}
              delay={80 + i * 10}
              x={centerX + dx}
              y={centerY + dy}
              color={theme.prime}
            />
          );
        })}

        {/* multiples column on the right */}
        <Caption text="Содржатели на 3" size={36} color={theme.positive} y={170} delay={140} />
        {multiples.map((m, i) => {
          const delay = 160 + i * 12;
          return (
            <div
              key={m}
              style={{
                position: 'absolute',
                left: 1480,
                top: 260 + i * 95,
                transform: 'translate(-50%, -50%)',
              }}
            >
              <IntegerChip
                value={m}
                size={44}
                delay={delay}
                x={0}
                y={0}
                color={theme.positive}
              />
            </div>
          );
        })}
      </div>
    </Background>
  );
};
