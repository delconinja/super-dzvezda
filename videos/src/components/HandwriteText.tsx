import {useCurrentFrame, interpolate} from 'remotion';
import {useEffect, useState} from 'react';
import opentype from 'opentype.js';

/**
 * HandwriteText — renders text by converting each glyph into an SVG path
 * and animating its stroke from 0 → full length so it looks like the
 * pen is drawing each character.
 *
 * NOT typewriter behavior — actual stroke animation per character.
 *
 * Loads the Patrick Hand TTF from Google Fonts on first mount.
 */

type CharPath = {
  ch: string;
  d: string;          // SVG path data
  length: number;     // path length (for stroke animation)
  x: number;          // horizontal advance position
};

const FONT_URL =
  'https://fonts.gstatic.com/s/patrickhand/v23/LDI1apSQOAYtSuYWp8ZhfYeMWcjKm7sp8g.ttf';

// Module-level cache so we don't reload the font for every component instance
let cachedFont: opentype.Font | null = null;
let fontLoadPromise: Promise<opentype.Font> | null = null;

function loadFont(): Promise<opentype.Font> {
  if (cachedFont) return Promise.resolve(cachedFont);
  if (fontLoadPromise) return fontLoadPromise;
  fontLoadPromise = fetch(FONT_URL)
    .then((r) => r.arrayBuffer())
    .then((buf) => opentype.parse(buf))
    .then((font) => {
      cachedFont = font;
      return font;
    });
  return fontLoadPromise;
}

export const HandwriteText: React.FC<{
  text: string;
  x: number;
  y: number;
  fontSize?: number;
  color?: string;
  strokeWidth?: number;
  startFrame?: number;
  framesPerChar?: number;
  glow?: boolean;
}> = ({
  text,
  x,
  y,
  fontSize = 96,
  color = '#f5f5dc',
  strokeWidth = 4,
  startFrame = 0,
  framesPerChar = 14,
  glow = true,
}) => {
  const frame = useCurrentFrame();
  const [paths, setPaths] = useState<CharPath[]>([]);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let cancelled = false;
    loadFont().then((font) => {
      if (cancelled) return;
      // Use opentype to lay out the string at the requested size
      const otPath = font.getPath(text, x, y, fontSize);
      const fullSvg = otPath.toSVG(2);
      // Split per-character so we can stagger the stroke animation.
      // We re-lay out each character independently to know its width.
      const result: CharPath[] = [];
      let cursorX = x;
      for (const ch of text) {
        const glyph = font.charToGlyph(ch);
        const advance = (glyph.advanceWidth ?? 0) * (fontSize / font.unitsPerEm);
        if (ch === ' ') {
          cursorX += advance;
          continue;
        }
        const charPath = font.getPath(ch, cursorX, y, fontSize);
        const pathData = charPath.toPathData(2);

        // Measure path length: build a temporary SVG path and use getTotalLength
        const tmp = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        tmp.setAttribute('d', pathData);
        // getTotalLength only works once the element is in DOM, but
        // most browsers also let SVGPathElement.getTotalLength() work
        // off-document. If it returns 0, fall back to an estimate.
        let len = 0;
        try {
          len = tmp.getTotalLength();
        } catch (e) {
          len = pathData.length * 2;
        }
        if (!len) len = advance * 2; // safety fallback

        result.push({ch, d: pathData, length: len, x: cursorX});
        cursorX += advance;
      }
      void fullSvg;
      setPaths(result);
      setReady(true);
    });
    return () => {
      cancelled = true;
    };
  }, [text, x, y, fontSize]);

  if (!ready) {
    return null;
  }

  return (
    <svg
      width="100%"
      height="100%"
      viewBox="0 0 1920 1080"
      style={{position: 'absolute', top: 0, left: 0, pointerEvents: 'none'}}
    >
      {paths.map((p, i) => {
        const charStart = startFrame + i * framesPerChar;
        const charEnd = charStart + framesPerChar;
        const progress = interpolate(frame, [charStart, charEnd], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        const drawn = p.length * progress;
        return (
          <path
            key={i}
            d={p.d}
            stroke={color}
            strokeWidth={strokeWidth}
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeDasharray={p.length}
            strokeDashoffset={p.length - drawn}
            style={glow ? {filter: `drop-shadow(0 0 6px ${color}aa)`} : undefined}
          />
        );
      })}
    </svg>
  );
};
