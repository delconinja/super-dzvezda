"""
m8-2-2  —  Низи, функции и графици
Математика 8, Единица 2: Алгебра

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Math-specific: numbers and operations as characters with intentions.
Render:  manim -ql m8-2-2.py M822Scene
Output:  media/videos/m8-2-2/480p15/M822Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE    = "#4fc3f7"
YELLOW  = "#ffd54f"
GREEN   = "#81c784"
RED     = "#e57373"
GREY    = "#90a4ae"
ORANGE  = "#ffb74d"
PURPLE  = "#ce93d8"
WHITE2  = "#e8eaf0"
DARK_CARD = "#0f2233"


def callout(text, width=9.0, bg="#0d2b44", border=BLUE, font_size=28):
    box = RoundedRectangle(
        width=width, height=1.4, corner_radius=0.3,
        fill_color=bg, fill_opacity=1,
        stroke_color=border, stroke_width=2,
    )
    label = Text(text, font_size=font_size, color=WHITE2)
    label.move_to(box)
    return VGroup(box, label)


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


def num_node(value, color=BLUE, size=0.7):
    circle = Circle(radius=size, fill_color=DARK_CARD, fill_opacity=1,
                    stroke_color=color, stroke_width=3)
    label = Text(str(value), font_size=34, color=WHITE2, weight=BOLD)
    label.move_to(circle)
    return VGroup(circle, label)


class M822Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text(
            "Секоја низа има шепот.",
            font_size=46, color=YELLOW, weight=BOLD,
        )
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)
        self.wait(0.6)

        beats = VGroup(
            Text("Слушаш.", font_size=38, color=WHITE2),
            Text("Препознаваш.", font_size=38, color=BLUE),
            Text("Предвидуваш.", font_size=38, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.6)
            self.wait(0.3)

        finisher = Text("Тоа е низа.", font_size=42, color=ORANGE, weight=BOLD)
        finisher.next_to(beats, DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.2)
        self.wait(1.4)

        self.play(FadeOut(VGroup(hook, beats, finisher)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ARITHMETIC SEQUENCE                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("arithmetic")
        title = section_title("Аритметичка низа")
        self.play(FadeIn(title), run_time=0.7)

        seq_a = [2, 5, 8, 11]
        nodes_a = VGroup(*[num_node(v, color=BLUE) for v in seq_a])
        nodes_a.arrange(RIGHT, buff=1.3).move_to(UP * 0.3)
        self.play(LaggedStartMap(FadeIn, nodes_a, shift=UP * 0.2, lag_ratio=0.25))
        self.wait(0.5)

        # arrows with +3
        arrows_a = VGroup()
        labels_a = VGroup()
        for i in range(len(seq_a) - 1):
            start = nodes_a[i].get_right() + RIGHT * 0.05
            end = nodes_a[i + 1].get_left() + LEFT * 0.05
            arr = Arrow(start, end, color=YELLOW, stroke_width=4,
                        buff=0.05, max_tip_length_to_length_ratio=0.18)
            lbl = Text("+3", font_size=28, color=YELLOW, weight=BOLD)
            lbl.next_to(arr, UP, buff=0.1)
            arrows_a.add(arr)
            labels_a.add(lbl)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_a], lag_ratio=0.3))
        self.play(LaggedStartMap(FadeIn, labels_a, lag_ratio=0.3))
        self.wait(0.5)

        rule_a = callout("Постојана разлика  d = 3", width=8.0, border=YELLOW, font_size=30)
        rule_a.shift(DOWN * 2.0)
        self.play(FadeIn(rule_a, shift=UP * 0.2))
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, nodes_a, arrows_a, labels_a, rule_a)), run_time=0.7)

        # ── Geometric ────────────────────────────────────────────
        title2 = section_title("Геометриска низа", color=GREEN)
        self.play(FadeIn(title2), run_time=0.6)

        seq_g = [2, 6, 18, 54]
        nodes_g = VGroup(*[num_node(v, color=GREEN) for v in seq_g])
        nodes_g.arrange(RIGHT, buff=1.3).move_to(UP * 0.3)
        self.play(LaggedStartMap(FadeIn, nodes_g, shift=UP * 0.2, lag_ratio=0.25))

        arrows_g = VGroup()
        labels_g = VGroup()
        for i in range(len(seq_g) - 1):
            start = nodes_g[i].get_right() + RIGHT * 0.05
            end = nodes_g[i + 1].get_left() + LEFT * 0.05
            arr = Arrow(start, end, color=ORANGE, stroke_width=4,
                        buff=0.05, max_tip_length_to_length_ratio=0.18)
            lbl = Text("× 3", font_size=28, color=ORANGE, weight=BOLD)
            lbl.next_to(arr, UP, buff=0.1)
            arrows_g.add(arr)
            labels_g.add(lbl)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_g], lag_ratio=0.3))
        self.play(LaggedStartMap(FadeIn, labels_g, lag_ratio=0.3))

        rule_g = callout("Постојан количник  q = 3", width=8.0, border=ORANGE, font_size=30)
        rule_g.shift(DOWN * 2.0)
        self.play(FadeIn(rule_g, shift=UP * 0.2))
        self.wait(1.4)

        self.play(FadeOut(VGroup(title2, nodes_g, arrows_g, labels_g, rule_g)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  SQUARES, CUBES, FIBONACCI                        ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("special")
        title3 = section_title("Посебни низи", color=PURPLE)
        self.play(FadeIn(title3), run_time=0.6)

        # squares
        sq_label = Text("Квадрати  n²:", font_size=30, color=YELLOW)
        sq_label.move_to(UP * 1.6 + LEFT * 4.5)
        sq_vals = VGroup(*[num_node(v, color=YELLOW, size=0.55) for v in [1, 4, 9, 16, 25]])
        sq_vals.arrange(RIGHT, buff=0.6).next_to(sq_label, RIGHT, buff=0.5)
        self.play(FadeIn(sq_label), LaggedStartMap(FadeIn, sq_vals, lag_ratio=0.2))

        cu_label = Text("Кубови  n³:", font_size=30, color=ORANGE)
        cu_label.move_to(LEFT * 4.5 + UP * 0.1)
        cu_vals = VGroup(*[num_node(v, color=ORANGE, size=0.55) for v in [1, 8, 27, 64, 125]])
        cu_vals.arrange(RIGHT, buff=0.5).next_to(cu_label, RIGHT, buff=0.5)
        self.play(FadeIn(cu_label), LaggedStartMap(FadeIn, cu_vals, lag_ratio=0.2))

        fib_label = Text("Фибоначи:", font_size=30, color=GREEN)
        fib_label.move_to(LEFT * 4.5 + DOWN * 1.4)
        fib_vals = VGroup(*[num_node(v, color=GREEN, size=0.55) for v in [1, 1, 2, 3, 5, 8, 13]])
        fib_vals.arrange(RIGHT, buff=0.4).next_to(fib_label, RIGHT, buff=0.4)
        self.play(FadeIn(fib_label), LaggedStartMap(FadeIn, fib_vals, lag_ratio=0.2))
        self.wait(1.2)

        fib_note = Text("секој следен = збир од претходните два",
                        font_size=24, color=WHITE2)
        fib_note.next_to(fib_vals, DOWN, buff=0.4)
        self.play(FadeIn(fib_note))
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, sq_label, sq_vals, cu_label, cu_vals,
                                 fib_label, fib_vals, fib_note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  nth TERM FORMULA                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("nth_term")
        title4 = section_title("Општ член")
        self.play(FadeIn(title4), run_time=0.6)

        formula = MathTex(
            "a_n", "=", "a_1", "+", "(n-1)", "d",
            font_size=64, color=WHITE2,
        )
        formula[0].set_color(BLUE)
        formula[2].set_color(GREEN)
        formula[5].set_color(YELLOW)
        formula.move_to(UP * 1.6)
        self.play(Write(formula), run_time=1.8)
        self.wait(0.8)

        # example sequence
        ex_seq = [5, 9, 13, 17, 21]
        ex_nodes = VGroup(*[num_node(v, color=BLUE, size=0.55) for v in ex_seq])
        ex_nodes.arrange(RIGHT, buff=1.0).move_to(DOWN * 0.4)
        self.play(LaggedStartMap(FadeIn, ex_nodes, lag_ratio=0.2))

        d_label = Text("d = 4", font_size=30, color=YELLOW, weight=BOLD)
        d_label.next_to(ex_nodes, DOWN, buff=0.4)
        self.play(FadeIn(d_label))
        self.wait(0.5)

        solve = MathTex(
            "a_n = 5 + (n-1)\\cdot 4 = 4n + 1",
            font_size=42, color=GREEN,
        )
        solve.next_to(d_label, DOWN, buff=0.4)
        self.play(Write(solve), run_time=1.5)
        self.wait(0.8)

        check = MathTex(
            "a_5 = 4\\cdot 5 + 1 = 21 \\checkmark",
            font_size=36, color=ORANGE,
        )
        check.next_to(solve, DOWN, buff=0.3)
        self.play(Write(check), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title4, formula, ex_nodes, d_label, solve, check)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  FUNCTION MACHINE                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("function")
        title5 = section_title("Функција", color=BLUE)
        self.play(FadeIn(title5), run_time=0.6)

        f_formula = MathTex("f(x) = 2x + 3", font_size=56, color=WHITE2)
        f_formula.move_to(UP * 2.0)
        self.play(Write(f_formula), run_time=1.0)

        # machine box
        machine = RoundedRectangle(
            width=2.4, height=1.6, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=3,
        )
        machine.move_to(ORIGIN)
        m_label = Text("f", font_size=44, color=BLUE, weight=BOLD).move_to(machine)
        self.play(FadeIn(machine), FadeIn(m_label))

        in_label = Text("x", font_size=36, color=GREEN).move_to(LEFT * 4.0)
        out_label = Text("y", font_size=36, color=ORANGE).move_to(RIGHT * 4.0)
        in_arrow = Arrow(in_label.get_right() + RIGHT * 0.2,
                         machine.get_left() + LEFT * 0.05,
                         color=GREEN, buff=0.1, stroke_width=4)
        out_arrow = Arrow(machine.get_right() + RIGHT * 0.05,
                          out_label.get_left() + LEFT * 0.2,
                          color=ORANGE, buff=0.1, stroke_width=4)
        self.play(FadeIn(in_label), GrowArrow(in_arrow),
                  GrowArrow(out_arrow), FadeIn(out_label))
        self.wait(0.5)

        # values
        values = [(1, 5), (2, 7), (3, 9)]
        rows = VGroup()
        for x, y in values:
            row = MathTex(
                f"f({x}) = 2\\cdot{x} + 3 = {y}",
                font_size=32, color=WHITE2,
            )
            rows.add(row)
        rows.arrange(DOWN, buff=0.25).next_to(machine, DOWN, buff=0.7)

        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.5)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title5, f_formula, machine, m_label,
                                 in_label, out_label, in_arrow, out_arrow, rows)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  LINEAR GRAPH y = mx + c                          ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("linear")
        title6 = section_title("Линеарна функција  y = mx + c", color=GREEN)
        self.play(FadeIn(title6), run_time=0.6)

        # axes
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 10, 2],
            x_length=5.5, y_length=5.0,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_numbers": True,
                         "font_size": 22},
            tips=False,
        )
        axes.move_to(LEFT * 3.2 + DOWN * 0.3)
        self.play(Create(axes), run_time=1.2)

        # table
        table_lines = VGroup(
            Text("x   |   y", font_size=26, color=YELLOW, weight=BOLD),
            Text("0   |   3", font_size=24, color=WHITE2),
            Text("1   |   5", font_size=24, color=WHITE2),
            Text("2   |   7", font_size=24, color=WHITE2),
            Text("3   |   9", font_size=24, color=WHITE2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        table_lines.move_to(RIGHT * 2.5 + UP * 1.0)

        underline = Line(
            table_lines[0].get_left() + DOWN * 0.18,
            table_lines[0].get_right() + DOWN * 0.18,
            color=YELLOW,
        )
        self.play(FadeIn(table_lines), Create(underline))
        self.wait(0.4)

        # plot points
        pts = [(0, 3), (1, 5), (2, 7), (3, 9)]
        dots = VGroup()
        for x, y in pts:
            d = Dot(axes.c2p(x, y), color=ORANGE, radius=0.08)
            dots.add(d)
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.2))
        self.wait(0.3)

        line = axes.plot(lambda x: 2 * x + 3, x_range=[-0.5, 3.5],
                         color=GREEN, stroke_width=4)
        self.play(Create(line), run_time=1.2)
        self.wait(0.5)

        # slope triangle
        p1 = axes.c2p(1, 5)
        p2 = axes.c2p(2, 5)
        p3 = axes.c2p(2, 7)
        tri_h = Line(p1, p2, color=YELLOW, stroke_width=3)
        tri_v = Line(p2, p3, color=YELLOW, stroke_width=3)
        run_l = Text("1", font_size=22, color=YELLOW).next_to(tri_h, DOWN, buff=0.05)
        rise_l = Text("2", font_size=22, color=YELLOW).next_to(tri_v, RIGHT, buff=0.05)
        self.play(Create(tri_h), Create(tri_v),
                  FadeIn(run_l), FadeIn(rise_l))
        self.wait(0.5)

        m_box = callout("m = 2  (раст / врвеж)", width=4.6, border=YELLOW, font_size=24)
        m_box.move_to(RIGHT * 2.5 + DOWN * 1.0)
        c_box = callout("c = 3  (пресек со y)", width=4.6, border=GREEN, font_size=24)
        c_box.next_to(m_box, DOWN, buff=0.25)
        self.play(FadeIn(m_box), FadeIn(c_box))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title6, axes, table_lines, underline, dots, line,
                                 tri_h, tri_v, run_l, rise_l, m_box, c_box)),
                  run_time=0.7)

        # ── slope signs ──────────────────────────────────────
        title6b = section_title("Знакот на m", color=BLUE)
        self.play(FadeIn(title6b), run_time=0.5)

        ax_w = 3.5
        axs = []
        labels = ["m > 0  расте", "m < 0  опаѓа", "m = 0  хоризонтала"]
        cols = [GREEN, RED, GREY]
        fns = [lambda x: x, lambda x: -x, lambda x: 0]
        positions = [LEFT * 4.5, ORIGIN, RIGHT * 4.5]

        graphs_group = VGroup()
        for pos, lab, col, fn in zip(positions, labels, cols, fns):
            a = Axes(
                x_range=[-2, 2, 1], y_range=[-2, 2, 1],
                x_length=ax_w, y_length=ax_w,
                axis_config={"color": GREY, "stroke_width": 1.5},
                tips=False,
            ).move_to(pos + DOWN * 0.3)
            g = a.plot(fn, x_range=[-1.8, 1.8], color=col, stroke_width=4)
            t = Text(lab, font_size=24, color=col).next_to(a, DOWN, buff=0.2)
            graphs_group.add(VGroup(a, g, t))

        self.play(LaggedStartMap(FadeIn, graphs_group, lag_ratio=0.3, run_time=2.0))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title6b, graphs_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  REAL EXAMPLE — TAXI                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("real")
        title7 = section_title("Такси возење", color=ORANGE)
        self.play(FadeIn(title7), run_time=0.6)

        taxi_formula = MathTex(
            "y = 30x + 50",
            font_size=56, color=WHITE2,
        )
        taxi_formula.move_to(UP * 1.8)
        self.play(Write(taxi_formula))

        legend = VGroup(
            Text("50 ден  —  стартарина", font_size=26, color=GREEN),
            Text("30 ден  —  по километар", font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        legend.next_to(taxi_formula, DOWN, buff=0.4)
        self.play(FadeIn(legend))
        self.wait(0.6)

        calc1 = Text(
            "5 km:   y = 30·5 + 50 = 200 ден",
            font_size=30, color=BLUE,
        )
        calc2 = Text(
            "10 km:   y = 30·10 + 50 = 350 ден",
            font_size=30, color=ORANGE,
        )
        calc1.next_to(legend, DOWN, buff=0.5)
        calc2.next_to(calc1, DOWN, buff=0.3)
        self.play(Write(calc1), run_time=1.2)
        self.play(Write(calc2), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title7, taxi_formula, legend, calc1, calc2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 8.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")
        sum_title = section_title("Заклучок", color=YELLOW)
        self.play(FadeIn(sum_title), run_time=0.5)

        s1 = Text("Низа дава ред.", font_size=36, color=BLUE)
        s2 = Text("Функција дава правило.", font_size=36, color=GREEN)
        s3 = Text("График дава слика.", font_size=36, color=ORANGE)
        end = Text("Три јазици. Една приказна.",
                   font_size=40, color=YELLOW, weight=BOLD)

        VGroup(s1, s2, s3, end).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for s in [s1, s2, s3]:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.play(Write(end), run_time=1.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sum_title, s1, s2, s3, end)), run_time=0.8)
