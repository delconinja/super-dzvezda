import {Series, Audio, staticFile} from 'remotion';
import {theme} from '../theme';

import {TempHook} from '../scenes/TempHook';
import {PrimesStrip} from '../scenes/PrimesStrip';
import {NzdNzsVenn} from '../scenes/NzdNzsVenn';
import {MathPathFinal} from '../scenes/MathPathFinal';
import {AlgebraRecap} from '../scenes/AlgebraRecap';

import {SignRulesPanel} from '../components/SignRulesPanel';
import {NumberSetList} from '../components/NumberSetList';
import {EquationGallery} from '../components/EquationGallery';
import {StepByStepSolver} from '../components/StepByStepSolver';

/**
 * m8-1-1 — Цели броеви, степени и корени
 *
 * Built scene-by-scene from narrations/m8-1-1.md (BRO-strict, gpt-5).
 * Total: 18 beats ≈ 8.5 min @ 30fps.
 *
 * Every formula and example in the script appears on-screen in the
 * matching scene — number lists, sign-rule panels, factor decompositions,
 * powers, square roots, cube roots.
 */
export const M8_1_1: React.FC = () => (
  <>
    {/* Macedonian voice-over by Edge-TTS (Marija, neural). 6:48. */}
    <Audio src={staticFile('audio/m8-1-1.mp3')} />

    <Series>
    {/* §1 Hook — Kej temperature −2 → +5 (30s) */}
    <Series.Sequence durationInFrames={900}>
      <TempHook />
    </Series.Sequence>

    {/* §2 Integers definition + number line (30s) */}
    <Series.Sequence durationInFrames={900}>
      <NumberSetList
        title="Цели броеви"
        label="…, −3, −2, −1, 0, 1, 2, 3, …"
        numbers={[-3, -2, -1, 0, 1, 2, 3]}
        caption="Негативните се лево од нула, позитивните се десно."
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §3 Addition / subtraction sign rules (35s) */}
    <Series.Sequence durationInFrames={1050}>
      <SignRulesPanel
        title="Собирање со знаци"
        ruleSame="собери ги, задржи знакот"
        ruleDifferent="одземи помал од поголем, задржи знак на поголемиот"
        examples={[
          {expr: '5 + 3 = 8',          result: 'positive'},
          {expr: '−5 + (−3) = −8',     result: 'negative'},
          {expr: '5 + (−3) = 2',       result: 'positive'},
          {expr: '−5 + 3 = −2',        result: 'negative'},
        ]}
        durationFrames={1050}
      />
    </Series.Sequence>

    {/* §4 Step-by-step  5 + (−3) = 2 (35s) */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="Чекор по чекор: 5 + (−3)"
        accentColor={theme.zero}
        durationFrames={1050}
        steps={[
          {expr: '5 + (−3) = ?',           note: 'различни знаци'},
          {expr: 'споредуваме 5 vs 3',     note: 'поголемо е 5 → знак „+"'},
          {expr: '5 − 3 = 2',              note: 'одземи помал од поголем'},
          {expr: '5 + (−3) = 2',           note: 'резултат', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §5 Multiplication / division sign rules (30s) */}
    <Series.Sequence durationInFrames={900}>
      <SignRulesPanel
        title="Множење со знаци"
        ruleSame="истоимени → позитивно"
        ruleDifferent="разноимени → негативно"
        examples={[
          {expr: '5 × 3 = 15',          result: 'positive'},
          {expr: '(−5) × (−3) = 15',    result: 'positive'},
          {expr: '5 × (−3) = −15',      result: 'negative'},
          {expr: '(−5) × 3 = −15',      result: 'negative'},
        ]}
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §6 Factors of 12 (25s) */}
    <Series.Sequence durationInFrames={750}>
      <NumberSetList
        title="Делители на 12"
        label="броеви што го делат 12 без остаток"
        numbers={[1, 2, 3, 4, 6, 12]}
        caption="Со кои броеви 12 се дели рамномерно."
        durationFrames={750}
      />
    </Series.Sequence>

    {/* §6b Multiples of 4 (25s) */}
    <Series.Sequence durationInFrames={750}>
      <NumberSetList
        title="Содржатели на 4"
        label="броеви што се деливи со 4"
        numbers={[4, 8, 12, 16, 20]}
        trailingDots
        caption="Секој следен е зголемен за 4."
        durationFrames={750}
      />
    </Series.Sequence>

    {/* §7 NZD & NZS Venn-style (35s) */}
    <Series.Sequence durationInFrames={1050}>
      <NzdNzsVenn />
    </Series.Sequence>

    {/* §8 Prime numbers (30s) */}
    <Series.Sequence durationInFrames={900}>
      <PrimesStrip />
    </Series.Sequence>

    {/* §9 Factorization gallery (30s) */}
    <Series.Sequence durationInFrames={900}>
      <EquationGallery
        title="Прости множители"
        equations={[
          '12 = 2² × 3',
          '30 = 2 × 3 × 5',
          '100 = 2² × 5²',
          '500 = 2² × 5³',
        ]}
        accentColor={theme.prime}
        caption="Секој природен број = производ на прости броеви."
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §10 Step-by-step 500 = 2² × 5³ (35s) */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="500 = ?  (разложување)"
        accentColor={theme.prime}
        durationFrames={1050}
        steps={[
          {expr: '500 ÷ 2 = 250',          note: 'делиме со 2'},
          {expr: '250 ÷ 2 = 125',          note: 'пак со 2'},
          {expr: '125 ÷ 5 = 25',           note: 'делиме со 5'},
          {expr: '25 ÷ 5 = 5',             note: 'пак со 5'},
          {expr: '5 ÷ 5 = 1',              note: 'уште еднаш со 5'},
          {expr: '500 = 2² × 5³',          note: 'разложено', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §11 Powers (30s) */}
    <Series.Sequence durationInFrames={900}>
      <EquationGallery
        title="Степени"
        equations={[
          '2³ = 2 × 2 × 2 = 8',
          '5² = 5 × 5 = 25',
          '(−2)³ = −8',
          '(−2)² = 4',
        ]}
        accentColor={theme.power}
        caption="Парен експонент → плус; непарен експонент при негативна основа → минус."
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §12 Powers of 10 (25s) */}
    <Series.Sequence durationInFrames={750}>
      <EquationGallery
        title="Степени со основа 10"
        equations={[
          '10¹ = 10',
          '10² = 100',
          '10³ = 1 000',
          '10⁴ = 10 000',
        ]}
        accentColor={theme.power}
        caption="Експонентот = број на нули по единицата."
        durationFrames={750}
      />
    </Series.Sequence>

    {/* §13 Square roots (30s) */}
    <Series.Sequence durationInFrames={900}>
      <EquationGallery
        title="Квадратен корен"
        equations={[
          '√16 = 4    (4² = 16)',
          '√81 = 9    (9² = 81)',
          '√100 = 10  (10² = 100)',
        ]}
        accentColor={theme.root}
        caption="√a е број кој помножен сам со себе ја дава a."
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §14 Cube roots (30s) */}
    <Series.Sequence durationInFrames={900}>
      <EquationGallery
        title="Кубен корен"
        equations={[
          '³√8 = 2    (2³ = 8)',
          '³√27 = 3   (3³ = 27)',
          '³√64 = 4   (4³ = 64)',
        ]}
        accentColor={theme.root}
        caption="³√a е број чиј трет степен ја дава a."
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §15 Mini-check (25s) */}
    <Series.Sequence durationInFrames={750}>
      <StepByStepSolver
        title="Мини проверка"
        accentColor={theme.highlight}
        durationFrames={750}
        steps={[
          {expr: '(−2)² = 4',           note: 'истоимени знаци → плус'},
          {expr: '5 × (−3) = −15',      note: 'разноимени знаци → минус'},
          {expr: '√16 = 4',             note: '4² = 16',                highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §16 Concept recap (25s) */}
    <Series.Sequence durationInFrames={750}>
      <AlgebraRecap />
    </Series.Sequence>

    {/* §17 Final thought (25s) */}
    <Series.Sequence durationInFrames={750}>
      <MathPathFinal />
    </Series.Sequence>
    </Series>
  </>
);
