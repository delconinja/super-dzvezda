import {AbsoluteFill} from 'remotion';
import {theme} from '../theme';

export const Background: React.FC<{children?: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: theme.bg}}>{children}</AbsoluteFill>
);
