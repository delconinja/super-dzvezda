import {Series} from 'remotion';
import {AlgebraHook} from '../scenes/AlgebraHook';
import {VariablesIntro} from '../scenes/VariablesIntro';
import {BalanceScale} from '../scenes/BalanceScale';
import {CombineLikeTerms} from '../scenes/CombineLikeTerms';
import {SubstitutionDemo} from '../scenes/SubstitutionDemo';
import {FunctionMachine} from '../scenes/FunctionMachine';
import {AlgebraRecap} from '../scenes/AlgebraRecap';
import {FinalThought} from '../scenes/FinalThought';
import {StepByStepSolver} from '../components/StepByStepSolver';
import {TalkingPoint} from '../components/TalkingPoint';
import {theme} from '../theme';

/**
 * m8-2-1 — Изрази, равенки и формули
 * Source: narrations/m8-2-1.md (gpt-5 teacher script, ~2170 words / ~12min narration)
 *
 * 21 beats mapped from the script (see M8_2_1.storyboard.md).
 * Total: 21,600 frames @ 30fps = 12 min.
 *
 * Polished custom scenes:  Hook, VariablesIntro, BalanceScale, CombineLikeTerms,
 *                          SubstitutionDemo, FunctionMachine, AlgebraRecap, FinalThought,
 *                          StepByStepSolver (used 4x)
 * TalkingPoint placeholders: §3, §4, §5, §10, §11, §12, §13, §18
 *                          (these get upgraded to proper visuals in next pass)
 */
export const M8_2_1: React.FC = () => (
  <Series>
    {/* §1 Hook — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <AlgebraHook />
    </Series.Sequence>

    {/* §2 Variables vs constants — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <VariablesIntro />
    </Series.Sequence>

    {/* §3 Formula vs function — 40s */}
    <Series.Sequence durationInFrames={1200}>
      <TalkingPoint
        heading="Формула или функција?"
        icon="📐"
        bullets={[
          'Формула е рецепт — кажува како се поврзани величините.',
          'P = a + b + c + d (периметар на четириаголник)',
          'Функција е машина — за секој влез има еден излез.',
          'f(x) = 2x + 3',
        ]}
        headingColor={theme.power}
        durationFrames={1200}
      />
    </Series.Sequence>

    {/* §4 Linear expressions: terms & coefficients — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <TalkingPoint
        heading="Линеарни изрази"
        icon="🧩"
        bullets={[
          'Променливите се во прв степен — нема x² или производи меѓу променливи',
          'Член: 2x, 3y, или −7',
          'Коефициент: бројот пред променливата (2 во 2x)',
        ]}
        headingColor={theme.zero}
        durationFrames={1050}
      />
    </Series.Sequence>

    {/* §5 Similar vs different terms — 30s */}
    <Series.Sequence durationInFrames={900}>
      <TalkingPoint
        heading="Слични и различни членови"
        icon="🍎🍐"
        bullets={[
          'Слични: иста променлива и иста степен — 3x, 5x, −2x',
          'Различни: различни променливи — 3x и 2y',
          'Слични со слични — никогаш не мешаме јаболка и круши.',
        ]}
        headingColor={theme.positive}
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §6 Combining like terms — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <CombineLikeTerms />
    </Series.Sequence>

    {/* §7 Distribution — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <TalkingPoint
        heading="Множење со загради"
        icon="📦"
        formula="3(x + 2) = 3x + 6"
        bullets={[
          '2(3x − 4) = 6x − 8',
          '−(x + 5) = −x − 5  (внимавај на знакот!)',
          'Секој член во заградата го чувствува множителот.',
        ]}
        headingColor={theme.power}
        durationFrames={1050}
      />
    </Series.Sequence>

    {/* §8 Worked simplify 2(3x-4) + x + 5 — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="Упрости: 2(3x − 4) + x + 5"
        accentColor={theme.zero}
        durationFrames={1050}
        steps={[
          {expr: '2(3x − 4) + x + 5',  note: 'почетен израз'},
          {expr: '6x − 8 + x + 5',     note: 'отвораме загради'},
          {expr: '(6x + x) + (−8 + 5)',note: 'групирај слични'},
          {expr: '7x − 3',             note: 'упростен израз', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §9 Substitution — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <SubstitutionDemo />
    </Series.Sequence>

    {/* §10 °F → °C — 40s */}
    <Series.Sequence durationInFrames={1200}>
      <StepByStepSolver
        title="50°F во Целзиус?"
        accentColor={theme.zero}
        durationFrames={1200}
        steps={[
          {expr: '°C = (°F − 32) × 5/9',  note: 'формула'},
          {expr: '°C = (50 − 32) × 5/9',  note: 'заменуваме °F = 50'},
          {expr: '°C = 18 × 5/9',         note: 'смалуваме'},
          {expr: '°C = 90 / 9',           note: 'множиме'},
          {expr: '°C = 10',               note: '10 степени Целзиус', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §11 Geometry formulas — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <TalkingPoint
        heading="Геометриски формули"
        icon="📏"
        bullets={[
          'Правоаголник: A = a × b  → 7×4 = 28 см²',
          'Триаголник:   A = (a × h) / 2',
          'Круг:          C = 2πr     A = πr²',
        ]}
        headingColor={theme.prime}
        durationFrames={1050}
      />
    </Series.Sequence>

    {/* §12 Speed-distance-time — 40s */}
    <Series.Sequence durationInFrames={1200}>
      <TalkingPoint
        heading="Брзина, време, растојание"
        icon="🚌"
        formula="v = s / t"
        bullets={[
          'Скопје → Велес: s = 50 км, v = 100 км/ч',
          't = s / v = 50 / 100 = 0,5 часа = 30 мин',
          'Велосипед од Кисела Вода до Центар: 6 км, 12 км/ч → 30 мин',
        ]}
        headingColor={theme.positive}
        durationFrames={1200}
      />
    </Series.Sequence>

    {/* §13 Profit — 30s */}
    <Series.Sequence durationInFrames={900}>
      <TalkingPoint
        heading="Профит во денари"
        icon="💰"
        formula="Профит = Приходи − Трошоци"
        bullets={[
          'Пазар во Охрид: ораси продадени за 1500 ден.',
          'Трошоци за набавка и превоз: 900 ден.',
          'Профит = 1500 − 900 = 600 ден.',
        ]}
        headingColor={theme.prime}
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §14 Solve x + 5 = 12 (balance scale) — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <BalanceScale />
    </Series.Sequence>

    {/* §15 Solve 2(x+3) = 14 — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="Реши: 2(x + 3) = 14"
        accentColor={theme.prime}
        durationFrames={1050}
        steps={[
          {expr: '2(x + 3) = 14',  note: 'почетна равенка'},
          {expr: '2x + 6 = 14',    note: 'отвораме загради'},
          {expr: '2x = 8',         note: 'одземаме 6 од двете страни'},
          {expr: 'x = 4',          note: 'делиме со 2', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §16 Solve 3x + 2 = x + 10 (variable both sides) — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="Реши: 3x + 2 = x + 10"
        accentColor={theme.prime}
        durationFrames={1050}
        steps={[
          {expr: '3x + 2 = x + 10',  note: 'променлива од двете страни'},
          {expr: '2x + 2 = 10',      note: 'одземаме x од двете страни'},
          {expr: '2x = 8',           note: 'одземаме 2 од двете страни'},
          {expr: 'x = 4',            note: 'делиме со 2', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §17 Function machine — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <FunctionMachine />
    </Series.Sequence>

    {/* §18 Common mistakes — 30s */}
    <Series.Sequence durationInFrames={900}>
      <TalkingPoint
        heading="Чести замки"
        icon="⚠️"
        bullets={[
          'Знаци: при −(x + 5), и плусот и x ги менуваат знакот',
          'Множење со загради: помножи СЕКОЈ член, не само првиот',
          'Пренос на член: всушност додаваш/одземаш на двете страни',
        ]}
        headingColor={theme.negative}
        durationFrames={900}
      />
    </Series.Sequence>

    {/* §19 Mini challenge — 35s */}
    <Series.Sequence durationInFrames={1050}>
      <StepByStepSolver
        title="Предизвик: 4y − 2(y − 5) = 18"
        accentColor={theme.prime}
        durationFrames={1050}
        steps={[
          {expr: '4y − 2(y − 5) = 18',  note: 'предизвик'},
          {expr: '4y − 2y + 10 = 18',   note: 'отвораме загради'},
          {expr: '2y + 10 = 18',        note: 'собираме слични'},
          {expr: '2y = 8',              note: 'одземаме 10'},
          {expr: 'y = 4',               note: 'делиме со 2', highlight: true},
        ]}
      />
    </Series.Sequence>

    {/* §20 Recap — 30s */}
    <Series.Sequence durationInFrames={900}>
      <AlgebraRecap />
    </Series.Sequence>

    {/* §21 Final thought — 25s */}
    <Series.Sequence durationInFrames={750}>
      <FinalThought />
    </Series.Sequence>
  </Series>
);
