import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Caption} from '../components/Caption';
import {theme, FONT_FAMILY} from '../theme';

/**
 * Scene §4 — MULTIPLICATION SIGN RULES
 * Four rules appear one by one; same-sign → positive (green), different-sign → negative (red).
 */
export const MultiplicationRules: React.FC = () => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [220, 250], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const rules: {expr: string; color: string; hint: string}[] = [
    {expr: '(+) × (+) = (+)', color: theme.positive, hint: 'истиот знак → позитивно'},
    {expr: '(−) × (−) = (+)', color: theme.positive, hint: 'истиот знак → позитивно'},
    {expr: '(+) × (−) = (−)', color: theme.negative, hint: 'различни знаци → негативно'},
    {expr: '(−) × (+) = (−)', color: theme.negative, hint: 'различни знаци → негативно'},
  ];

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <Caption text="Множење: правила за знаци" size={62} color={theme.power} y={100} />

        <div
          style={{
            position: 'absolute',
            top: 280,
            left: 0,
            right: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 24,
          }}
        >
          {rules.map((rule, i) => {
            const delay = 30 + i * 35;
            const opacity = interpolate(frame, [delay, delay + 18], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const dx = interpolate(frame, [delay, delay + 20], [-30, 0], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 32,
                  opacity,
                  transform: `translateX(${dx}px)`,
                  fontFamily: FONT_FAMILY,
                }}
              >
                <div
                  style={{
                    fontSize: 56,
                    fontWeight: 700,
                    color: rule.color,
                    textShadow: `0 0 14px ${rule.color}55`,
                    minWidth: 460,
                  }}
                >
                  {rule.expr}
                </div>
                <div style={{fontSize: 32, color: theme.subtle}}>{rule.hint}</div>
              </div>
            );
          })}
        </div>
      </div>
    </Background>
  );
};
