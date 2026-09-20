import {useCurrentFrame, interpolate} from 'remotion';
import {Background} from '../components/Background';
import {Title} from '../components/Title';
import {Caption} from '../components/Caption';
import {NumberLine} from '../components/NumberLine';
import {theme} from '../theme';

/**
 * Scene §1 — HOOK
 * Visual: title fades in, magical number line stretches across infinite space.
 */
export const Hook: React.FC<{
  title: string;
  hook: string;
}> = ({title, hook}) => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [180, 210], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <Background>
      <div style={{opacity: fadeOut, width: '100%', height: '100%'}}>
        <div style={{position: 'absolute', top: 140, left: 0, right: 0}}>
          <Title text={title} color={theme.zero} size={88} />
        </div>
        <Caption text={hook} size={42} color={theme.positive} y={320} delay={45} />
        <NumberLine min={-6} max={6} width={1600} y={720} delay={90} />
      </div>
    </Background>
  );
};
