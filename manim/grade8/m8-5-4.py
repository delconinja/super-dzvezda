"""
m8-5-4  —  Веројатност
Математика 8, Единица 5: Ракување со податоци

Andonovski-style: шансата не е магија, шансата е математика.
Render:  manim -ql m8-5-4.py M854Scene
Output:  media/videos/m8-5-4/480p15/M854Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE      = "#4fc3f7"
YELLOW    = "#ffd54f"
GREEN     = "#81c784"
RED       = "#e57373"
GREY      = "#90a4ae"
ORANGE    = "#ffb74d"
PURPLE    = "#ce93d8"
WHITE2    = "#e8eaf0"
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


def die_face(value, color=BLUE, size=1.0):
    """Draw a die with dots."""
    box = RoundedRectangle(
        width=size, height=size, corner_radius=0.12,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    dots = VGroup()
    # positions relative to center (unit cell)
    layouts = {
        1: [(0, 0)],
        2: [(-0.25, 0.25), (0.25, -0.25)],
        3: [(-0.25, 0.25), (0, 0), (0.25, -0.25)],
        4: [(-0.25, 0.25), (0.25, 0.25), (-0.25, -0.25), (0.25, -0.25)],
        5: [(-0.25, 0.25), (0.25, 0.25), (0, 0), (-0.25, -0.25), (0.25, -0.25)],
        6: [(-0.25, 0.25), (0.25, 0.25), (-0.25, 0), (0.25, 0),
            (-0.25, -0.25), (0.25, -0.25)],
    }
    for (dx, dy) in layouts.get(value, []):
        d = Dot(point=np.array([dx * size, dy * size, 0]),
                radius=size * 0.07, color=WHITE2)
        dots.add(d)
    g = VGroup(box, dots)
    return g


class M854Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Шансата не е магија.", font_size=40, color=RED, weight=BOLD)
        h2 = Text("Шансата е математика.", font_size=40, color=GREEN, weight=BOLD)
        h3 = Text("Брои поволни. Брои сите. Подели.",
                  font_size=32, color=YELLOW, weight=BOLD)
        h4 = Text("Тоа е сè.", font_size=36, color=WHITE2, weight=BOLD)

        hooks = VGroup(h1, h2, h3, h4).arrange(DOWN, buff=0.4)
        hooks.move_to(ORIGIN)
        for h in hooks:
            self.play(Write(h), run_time=0.9)
        self.wait(1.8)
        self.play(FadeOut(hooks), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  СКАЛА 0–1                                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("scale")

        title2 = section_title("Скала на веројатност")
        self.play(Write(title2), run_time=1.0)

        scale = NumberLine(
            x_range=[0, 1.01, 0.25],
            length=10,
            color=GREY,
            include_numbers=True,
            decimal_number_config={"num_decimal_places": 2},
            font_size=24,
            label_direction=DOWN,
        )
        scale.move_to(ORIGIN)
        self.play(Create(scale), run_time=1.0)

        markers = [
            (0.0,  "невозможно", RED),
            (0.25, "малку веројатно", ORANGE),
            (0.5,  "еднаква шанса", YELLOW),
            (0.75, "веројатно", GREEN),
            (1.0,  "сигурно", BLUE),
        ]

        for x, lbl, col in markers:
            dot = Dot(scale.n2p(x), color=col, radius=0.12)
            t = Text(lbl, font_size=22, color=col, weight=BOLD)
            t.move_to(scale.n2p(x) + UP * 0.8)
            self.play(FadeIn(dot, scale=0.5), Write(t), run_time=0.5)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  ФОРМУЛА + КОЦКА                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("formula_dice")

        title3 = section_title("Формула на веројатност")
        self.play(Write(title3), run_time=1.0)

        formula = MathTex(
            r"P(A) = \frac{\text{поволни исходи}}{\text{сите исходи}}",
            font_size=42, color=YELLOW,
        )
        formula.move_to(UP * 1.7)
        self.play(Write(formula), run_time=1.2)

        # Show all 6 dice faces
        dice = VGroup(*[die_face(i + 1, color=BLUE, size=1.0) for i in range(6)])
        dice.arrange(RIGHT, buff=0.25)
        dice.move_to(DOWN * 0.2)
        for d in dice:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.3)
        self.wait(0.5)

        # P(6) = 1/6
        # Highlight die 6
        self.play(dice[5][0].animate.set_stroke(color=GREEN, width=5), run_time=0.5)

        p6 = MathTex(r"P(6) = \frac{1}{6}", font_size=38, color=GREEN)
        p6.move_to(DOWN * 1.8)
        self.play(Write(p6), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(p6), dice[5][0].animate.set_stroke(color=BLUE, width=2),
                  run_time=0.5)

        # P(even) = 3/6 = 1/2
        for i in [1, 3, 5]:
            self.play(dice[i][0].animate.set_stroke(color=YELLOW, width=5),
                      run_time=0.2)

        peven = MathTex(r"P(\text{парен}) = \frac{3}{6} = \frac{1}{2}",
                        font_size=38, color=YELLOW)
        peven.move_to(DOWN * 1.8)
        self.play(Write(peven), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ФОРМИ + ПАРИЦА                                  ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("forms_coin")

        title4 = section_title("Три форми на еден број")
        self.play(Write(title4), run_time=1.0)

        # Coin
        coin = Circle(radius=0.8, color=YELLOW, fill_color="#d4a017", fill_opacity=0.8,
                      stroke_width=3)
        coin_lbl = Text("ПАРИЦА", font_size=18, color=DARK_CARD, weight=BOLD)
        coin_grp = VGroup(coin, coin_lbl)
        coin_grp.move_to(UP * 1.3)

        self.play(FadeIn(coin_grp, scale=0.8), run_time=0.8)

        text_q = Text("P(глава) = ?", font_size=32, color=WHITE2)
        text_q.next_to(coin_grp, DOWN, buff=0.4)
        self.play(Write(text_q), run_time=0.8)

        forms = VGroup(
            MathTex(r"\frac{1}{2}", font_size=44, color=BLUE),
            Text("=", font_size=44, color=WHITE2),
            MathTex(r"0{,}5", font_size=44, color=GREEN),
            Text("=", font_size=44, color=WHITE2),
            MathTex(r"50\%", font_size=44, color=ORANGE),
        )
        forms.arrange(RIGHT, buff=0.4)
        forms.move_to(DOWN * 1.3)

        for f in forms:
            self.play(Write(f), run_time=0.6)

        sub = Text("Дропка. Децимала. Процент.", font_size=26, color=YELLOW, weight=BOLD)
        sub.move_to(DOWN * 2.5)
        self.play(Write(sub), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  КОМПЛЕМЕНТАРНИ + ТЕОР vs ЕКСП                   ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("complement_theory")

        title5 = section_title("Комплемент")
        self.play(Write(title5), run_time=1.0)

        rule = MathTex(r"P(A) + P(\overline{A}) = 1", font_size=48, color=YELLOW)
        rule.move_to(UP * 1.5)
        self.play(Write(rule), run_time=1.0)

        ex = VGroup(
            Text("Ако P(дожд) = 0,3", font_size=32, color=BLUE),
            MathTex(r"P(\text{нема дожд}) = 1 - 0{,}3 = 0{,}7",
                    font_size=34, color=GREEN),
        )
        ex.arrange(DOWN, buff=0.5)
        ex.move_to(DOWN * 0.3)

        for e in ex:
            self.play(Write(e), run_time=1.0)

        idea = Text("Што не може да биде — е она што не е.",
                    font_size=26, color=ORANGE)
        idea.move_to(DOWN * 2.3)
        self.play(Write(idea), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # Theoretical vs experimental
        title_te = section_title("Теориска и експериментална")
        self.play(Write(title_te), run_time=1.0)

        theo = callout(
            "Теориска: од формула.   P(6) = 1/6 ≈ 16,7%",
            width=11, bg="#0d2b44", border=BLUE, font_size=26,
        )
        exp = callout(
            "Експериментална: од обиди.   12/60 = 20%",
            width=11, bg="#0d2b44", border=GREEN, font_size=26,
        )
        theo.move_to(UP * 1.0)
        exp.move_to(DOWN * 0.6)

        self.play(FadeIn(theo, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(exp, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)

        law = Text("Закон на големи броеви: со повеќе обиди — се доближува до теориската.",
                   font_size=22, color=YELLOW)
        law.move_to(DOWN * 2.4)
        self.play(Write(law), run_time=1.5)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ДРВО НА ДВЕ ПАРИЦИ                              ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("tree")

        title6 = section_title("Независни настани: две парици")
        self.play(Write(title6), run_time=1.0)

        rule_i = MathTex(r"P(A \text{ и } B) = P(A) \times P(B)",
                         font_size=36, color=YELLOW)
        rule_i.move_to(UP * 2.0)
        self.play(Write(rule_i), run_time=1.0)

        # Tree
        root = Dot(LEFT * 4.5 + DOWN * 0.3, color=WHITE2, radius=0.08)

        # First flip — H and T
        h1_pos = LEFT * 2.5 + UP * 1.2
        t1_pos = LEFT * 2.5 + DOWN * 1.7

        h1_dot = Dot(h1_pos, color=BLUE, radius=0.08)
        t1_dot = Dot(t1_pos, color=RED, radius=0.08)
        h1_lbl = Text("Г", font_size=24, color=BLUE, weight=BOLD).next_to(h1_dot, LEFT, buff=0.15)
        t1_lbl = Text("П", font_size=24, color=RED, weight=BOLD).next_to(t1_dot, LEFT, buff=0.15)

        line1 = Line(root.get_center(), h1_pos, color=GREY, stroke_width=2)
        line2 = Line(root.get_center(), t1_pos, color=GREY, stroke_width=2)

        # Second flip
        hh = LEFT * 0.5 + UP * 1.8
        ht = LEFT * 0.5 + UP * 0.5
        th = LEFT * 0.5 + DOWN * 1.0
        tt = LEFT * 0.5 + DOWN * 2.3

        leaves = [
            (hh, "ГГ", BLUE),
            (ht, "ГП", PURPLE),
            (th, "ПГ", PURPLE),
            (tt, "ПП", RED),
        ]

        leaf_lines = [
            Line(h1_pos, hh, color=GREY, stroke_width=2),
            Line(h1_pos, ht, color=GREY, stroke_width=2),
            Line(t1_pos, th, color=GREY, stroke_width=2),
            Line(t1_pos, tt, color=GREY, stroke_width=2),
        ]

        self.play(FadeIn(root), run_time=0.4)
        self.play(Create(line1), Create(line2),
                  FadeIn(h1_dot), FadeIn(t1_dot),
                  Write(h1_lbl), Write(t1_lbl),
                  run_time=1.0)

        for ll in leaf_lines:
            self.play(Create(ll), run_time=0.25)

        leaf_grp = VGroup()
        for pos, name, col in leaves:
            d = Dot(pos, color=col, radius=0.08)
            t = Text(name, font_size=24, color=col, weight=BOLD)
            t.next_to(d, RIGHT, buff=0.15)
            leaf_grp.add(d, t)
        self.play(FadeIn(leaf_grp), run_time=0.8)

        # Probability calculation
        prob = MathTex(r"P(\text{ГГ}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}",
                       font_size=34, color=GREEN)
        prob.move_to(RIGHT * 3.5 + DOWN * 0.2)
        self.play(Write(prob), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ДВЕ КОЦКИ — ЗБИР=7                              ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("two_dice")

        title7 = section_title("Две коцки: збир = 7")
        self.play(Write(title7), run_time=1.0)

        # 6x6 grid
        grid_size = 0.7
        grid = VGroup()
        cell_map = {}
        for r in range(6):
            for c in range(6):
                d1 = r + 1
                d2 = c + 1
                cell = Square(side_length=grid_size,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=GREY, stroke_width=1)
                cell.move_to(np.array([
                    -2.5 + c * grid_size,
                    1.5 - r * grid_size, 0,
                ]))
                txt = Text(str(d1 + d2), font_size=18, color=WHITE2)
                txt.move_to(cell.get_center())
                g = VGroup(cell, txt)
                grid.add(g)
                cell_map[(d1, d2)] = g

        # Row/col labels
        x_lbls = VGroup()
        for c in range(6):
            t = Text(str(c + 1), font_size=20, color=BLUE, weight=BOLD)
            t.move_to(np.array([-2.5 + c * grid_size, 1.5 + grid_size, 0]))
            x_lbls.add(t)
        y_lbls = VGroup()
        for r in range(6):
            t = Text(str(r + 1), font_size=20, color=GREEN, weight=BOLD)
            t.move_to(np.array([-2.5 - grid_size, 1.5 - r * grid_size, 0]))
            y_lbls.add(t)

        d1_lbl = Text("Коцка 1", font_size=20, color=BLUE, weight=BOLD)
        d1_lbl.move_to(np.array([0.5, 1.5 + grid_size * 2.0, 0]))
        d2_lbl = Text("Коцка 2", font_size=20, color=GREEN, weight=BOLD)
        d2_lbl.move_to(np.array([-2.5 - grid_size * 2.0, -0.25, 0]))
        d2_lbl.rotate(90 * DEGREES)

        self.play(Create(grid), run_time=2.0)
        self.play(Write(x_lbls), Write(y_lbls), Write(d1_lbl), Write(d2_lbl),
                  run_time=1.0)
        self.wait(0.8)

        # Highlight cells where sum = 7
        seven_pairs = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
        anims = []
        for d1, d2 in seven_pairs:
            cell = cell_map[(d1, d2)][0]
            anims.append(cell.animate.set_fill(YELLOW, opacity=0.7))
        self.play(*anims, run_time=1.2)
        self.wait(0.8)

        result = MathTex(r"P(\text{збир}=7) = \frac{6}{36} = \frac{1}{6}",
                         font_size=38, color=YELLOW)
        result.move_to(RIGHT * 3.5 + UP * 0.0)
        self.play(Write(result), run_time=1.5)

        note = Text("6 поволни од 36 сите.", font_size=22, color=WHITE2)
        note.move_to(RIGHT * 3.5 + DOWN * 1.0)
        self.play(Write(note), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  МЕЃУСЕБНО ИСКЛУЧУВАЧКИ + CLOSING               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("exclusive_close")

        title8 = section_title("Меѓусебно исклучувачки настани")
        self.play(Write(title8), run_time=1.0)

        rule = MathTex(r"P(A \text{ или } B) = P(A) + P(B)",
                       font_size=40, color=YELLOW)
        rule.move_to(UP * 1.6)
        self.play(Write(rule), run_time=1.2)

        ex = MathTex(r"P(3 \text{ или } 5) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}",
                     font_size=36, color=GREEN)
        ex.move_to(DOWN * 0.0)
        self.play(Write(ex), run_time=1.5)

        note = Text("Кога не можат истовремено — едноставно собирај.",
                    font_size=24, color=WHITE2)
        note.move_to(DOWN * 1.5)
        self.play(Write(note), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        close = Text("Веројатноста не ветува. Само пресметува.",
                     font_size=36, color=YELLOW, weight=BOLD)
        close.move_to(ORIGIN)
        self.play(Write(close), run_time=1.8)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
