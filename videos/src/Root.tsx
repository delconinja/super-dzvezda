import {Composition} from 'remotion';
import {M8_1_1} from './lessons/M8_1_1';
import {M8_2_1} from './lessons/M8_2_1';
import {BlackboardDemoLesson} from './lessons/BlackboardDemo';

/**
 * Root registers every lesson composition for the Remotion Studio
 * and the CLI renderer (`npx remotion render`).
 */
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="m8-1-1"
        component={M8_1_1}
        durationInFrames={15000}  /* 500s = 8.3min — 18 beats from BRO-strict script */
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="m8-2-1"
        component={M8_2_1}
        durationInFrames={21600}  /* 720s = 12min @ 30fps */
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="blackboard-demo"
        component={BlackboardDemoLesson}
        durationInFrames={900}  /* 30s @ 30fps */
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
