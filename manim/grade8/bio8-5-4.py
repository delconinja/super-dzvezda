"""
bio8-5-4  —  Истражување на варијација кај растенија
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: Mendel watching peas,
laws beneath chaos, environment as silent sculptor.
Render:  manim -ql bio8-5-4.py Bio854Scene
Output:  media/videos/bio8-5-4/480p15/Bio854Scene.mp4
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


def make_pea(color=GREEN, wrinkled=False, scale=1.0):
    """Returns a pea shape — smooth or wrinkled."""
    if wrinkled:
        # bumpy outline
        pts = []
        for theta in np.linspace(0, TAU, 60):
            r = 0.5 + 0.07 * np.sin(theta * 6)
            pts.append(np.array([r * np.cos(theta), r * np.sin(theta), 0]))
        m = VMobject(stroke_color=color, stroke_width=3,
                     fill_color=color, fill_opacity=0.85)
        m.set_points_smoothly(pts + [pts[0]])
    else:
        m = Circle(radius=0.5, color=color,
                   fill_color=color, fill_opacity=0.85, stroke_width=3)
    m.scale(scale)
    return m


def make_leaf(color=GREEN, length=1.5):
    """Returns a stylized leaf shape."""
    pts = []
    n = 40
    for t in np.linspace(0, 1, n):
        x = t * length
        w = 0.35 * np.sin(t * PI)
        pts.append(np.array([x, w, 0]))
    for t in np.linspace(1, 0, n):
        x = t * length
        w = -0.35 * np.sin(t * PI)
        pts.append(np.array([x, w, 0]))
    m = VMobject(stroke_color="#3a7a3a", stroke_width=2,
                 fill_color=color, fill_opacity=0.85)
    m.set_points_smoothly(pts)
    return m


class Bio854Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Мендел гледал грашок.",       font_size=48, color=YELLOW, weight=BOLD)
        hook2 = Text("Зелен, жолт, мазен, набран.", font_size=42, color=GREEN,  weight=BOLD)
        hook3 = Text("Не случајно.",                 font_size=44, color=ORANGE, weight=BOLD)
        hook4 = Text("Закони.",                      font_size=50, color=BLUE,   weight=BOLD)
        hook5 = Text("Закони на наследувањето.",
                     font_size=38, color=PURPLE, weight=BOLD)

        beats = VGroup(hook1, hook2, hook3, hook4, hook5).arrange(DOWN, buff=0.4)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(Write(b), run_time=0.9)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ВАРИЈАЦИЈА КАЈ РАСТЕНИЈА                          ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("plant_variation")

        t2 = section_title("Варијација кај растенија")
        self.play(Write(t2), run_time=0.9)

        # 4 different plants
        plant_cols = [GREEN, "#5a9a3a", "#9acc6e", "#3a7a3a"]
        plants = VGroup()
        for i, col in enumerate(plant_cols):
            stem = Line(ORIGIN, UP * (1.2 + 0.3 * i),
                        color="#3a7a3a", stroke_width=4)
            leaf1 = make_leaf(color=col, length=0.8 + 0.15 * i)
            leaf1.rotate(PI / 6).move_to(stem.get_top() + LEFT * 0.3 + UP * 0.1)
            leaf2 = make_leaf(color=col, length=0.7 + 0.15 * i)
            leaf2.rotate(-PI / 6).flip(UP).move_to(stem.get_top() + RIGHT * 0.3 + UP * 0.1)
            p = VGroup(stem, leaf1, leaf2)
            plants.add(p)

        plants.arrange(RIGHT, buff=1.0, aligned_edge=DOWN).next_to(t2, DOWN, buff=0.8)

        for p in plants:
            self.play(FadeIn(p, shift=UP * 0.2), run_time=0.5)

        self.wait(0.4)

        traits = VGroup(
            Text("Големина на лист.",   font_size=28, color=GREEN, weight=BOLD),
            Text("Облик на лист.",      font_size=28, color=BLUE, weight=BOLD),
            Text("Боја на цвет.",       font_size=28, color=PURPLE, weight=BOLD),
            Text("Боја и облик на семе.", font_size=28, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.25).next_to(plants, DOWN, buff=0.7)

        for tr in traits:
            self.play(Write(tr), run_time=0.5)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t2, plants, traits)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  МЕНДЕЛ И ГРАШОК                                   ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mendel")

        t3 = section_title("Грегор Мендел", color=PURPLE)
        self.play(Write(t3), run_time=0.9)

        sub3 = Text("Австриски монах. 1860-ти. Манастирска градина.",
                    font_size=26, color=WHITE2)
        sub3.next_to(t3, DOWN, buff=0.25)
        self.play(Write(sub3), run_time=1.0)

        # 4 pea pairs showing traits
        # Smooth green
        sg = VGroup(make_pea(color=GREEN, wrinkled=False, scale=0.9),
                    Text("мазно, зелено", font_size=20, color=GREEN)).arrange(DOWN, buff=0.2)
        # Wrinkled green
        wg = VGroup(make_pea(color=GREEN, wrinkled=True, scale=0.9),
                    Text("набрано, зелено", font_size=20, color=GREEN)).arrange(DOWN, buff=0.2)
        # Smooth yellow
        sy = VGroup(make_pea(color=YELLOW, wrinkled=False, scale=0.9),
                    Text("мазно, жолто", font_size=20, color=YELLOW)).arrange(DOWN, buff=0.2)
        # Wrinkled yellow
        wy = VGroup(make_pea(color=YELLOW, wrinkled=True, scale=0.9),
                    Text("набрано, жолто", font_size=20, color=YELLOW)).arrange(DOWN, buff=0.2)

        peas = VGroup(sg, wg, sy, wy).arrange(RIGHT, buff=0.8).next_to(sub3, DOWN, buff=0.7)

        for p in peas:
            self.play(FadeIn(p, shift=UP * 0.2), run_time=0.6)

        self.wait(0.4)

        observ = Text("Прокрстосувал растенија. Бројал семиња. 7 особини.",
                      font_size=26, color=YELLOW)
        observ.next_to(peas, DOWN, buff=0.7)
        self.play(Write(observ), run_time=1.1)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, sub3, peas, observ)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ЗАКОНОТ — 3 : 1                                  ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mendel_law")

        t4 = section_title("Закон на Мендел: 3 : 1", color=YELLOW)
        self.play(Write(t4), run_time=0.9)

        # F1 row — all dominant
        f1 = VGroup(*[make_pea(color=YELLOW, wrinkled=False, scale=0.6) for _ in range(4)])
        f1.arrange(RIGHT, buff=0.3)
        f1_lab = Text("F1: сите жолти (доминантно)",
                      font_size=26, color=YELLOW, weight=BOLD)
        f1_group = VGroup(f1_lab, f1).arrange(DOWN, buff=0.25)
        f1_group.shift(UP * 1.2)

        self.play(Write(f1_lab), run_time=0.6)
        for pea in f1:
            self.play(FadeIn(pea, scale=0.8), run_time=0.2)

        self.wait(0.4)

        # F2 row — 3 yellow + 1 green
        f2_peas = VGroup(
            make_pea(color=YELLOW, wrinkled=False, scale=0.6),
            make_pea(color=YELLOW, wrinkled=False, scale=0.6),
            make_pea(color=YELLOW, wrinkled=False, scale=0.6),
            make_pea(color=GREEN,  wrinkled=False, scale=0.6),
        )
        f2_peas.arrange(RIGHT, buff=0.3)
        f2_lab = Text("F2: 3 жолти : 1 зелено",
                      font_size=26, color=GREEN, weight=BOLD)
        f2_group = VGroup(f2_lab, f2_peas).arrange(DOWN, buff=0.25)
        f2_group.shift(DOWN * 0.3)

        self.play(Write(f2_lab), run_time=0.6)
        for pea in f2_peas:
            self.play(FadeIn(pea, scale=0.8), run_time=0.2)

        self.wait(0.5)

        # ratio formula
        ratio = MathTex(r"\frac{3}{4} \, : \, \frac{1}{4}",
                        font_size=48, color=YELLOW)
        ratio.shift(DOWN * 1.8)
        self.play(Write(ratio), run_time=0.9)

        rule = Text("Рецесивната особина не исчезнува. Се крие.",
                    font_size=28, color=WHITE2, weight=BOLD)
        rule.to_edge(DOWN, buff=0.4)
        self.play(Write(rule), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t4, f1_group, f2_group, ratio, rule)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ГЕНЕТСКИ ИЛИ СРЕДИНСКИ?                          ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("genes_vs_environment")

        t5 = section_title("Гените или средината?")
        self.play(Write(t5), run_time=0.9)

        # split panel
        left_panel = RoundedRectangle(
            width=5.7, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).shift(LEFT * 3.3 + DOWN * 0.3)
        right_panel = RoundedRectangle(
            width=5.7, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).shift(RIGHT * 3.3 + DOWN * 0.3)

        left_label = Text("Гени", font_size=34, color=BLUE, weight=BOLD)
        left_label.move_to(left_panel.get_top() + DOWN * 0.4)
        right_label = Text("Средина", font_size=34, color=ORANGE, weight=BOLD)
        right_label.move_to(right_panel.get_top() + DOWN * 0.4)

        self.play(FadeIn(left_panel), FadeIn(right_panel),
                  Write(left_label), Write(right_label), run_time=1.0)

        left_items = VGroup(
            Text("Боја на цвет", font_size=26, color=WHITE2),
            Text("Облик на лист", font_size=26, color=WHITE2),
            Text("Боја на семе", font_size=26, color=WHITE2),
            Text("Тип на корен", font_size=26, color=WHITE2),
        ).arrange(DOWN, buff=0.3).next_to(left_label, DOWN, buff=0.45)

        right_items = VGroup(
            Text("Висина (вода!)", font_size=26, color=WHITE2),
            Text("Големина на лист", font_size=26, color=WHITE2),
            Text("Број на цветови", font_size=26, color=WHITE2),
            Text("Време на цветање", font_size=26, color=WHITE2),
        ).arrange(DOWN, buff=0.3).next_to(right_label, DOWN, buff=0.45)

        for li, ri in zip(left_items, right_items):
            self.play(Write(li), Write(ri), run_time=0.5)

        self.wait(0.4)

        bottom = Text("Истиот ген. Различна средина. Различен резултат.",
                      font_size=28, color=YELLOW, weight=BOLD)
        bottom.to_edge(DOWN, buff=0.3)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t5, left_panel, right_panel,
                                  left_label, right_label,
                                  left_items, right_items, bottom)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  МЕРЕЊЕ НА ЛИСТОВИ                                ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("leaf_measurement")

        t6 = section_title("Мерење на листови", color=GREEN)
        self.play(Write(t6), run_time=0.9)

        sub6 = Text("Земи 30 листови. Измери должина. Прави графикон.",
                    font_size=26, color=WHITE2)
        sub6.next_to(t6, DOWN, buff=0.3)
        self.play(Write(sub6), run_time=1.0)

        # bell curve of leaf lengths
        axes = Axes(
            x_range=[3, 11, 1], y_range=[0, 12, 2],
            x_length=8, y_length=3.2,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        ).shift(DOWN * 0.6)
        x_lab = Text("Должина на лист (cm)", font_size=22, color=WHITE2)
        x_lab.next_to(axes.x_axis, DOWN, buff=0.3)
        y_lab = Text("Број листови", font_size=22, color=WHITE2)
        y_lab.rotate(PI / 2).next_to(axes.y_axis, LEFT, buff=0.3)

        self.play(Create(axes), Write(x_lab), Write(y_lab), run_time=1.2)

        # bars
        leaf_data = [(4, 1), (5, 3), (6, 7), (7, 11), (8, 7), (9, 3), (10, 1)]
        bars = VGroup()
        for x_val, c in leaf_data:
            bar_w = 0.9
            bar_h = c * 0.255
            bar = Rectangle(
                width=bar_w, height=bar_h,
                fill_color=GREEN, fill_opacity=0.75,
                stroke_color=GREEN, stroke_width=2,
            )
            # position via axes
            base = axes.c2p(x_val, 0)
            top = axes.c2p(x_val, c)
            center = (base + top) / 2
            bar.move_to(center)
            bar.stretch_to_fit_width(bar_w)
            bar.stretch_to_fit_height(abs(top[1] - base[1]))
            bars.add(bar)

        for bar in bars:
            self.play(GrowFromEdge(bar, DOWN), run_time=0.3)

        punch6 = Text("Пак крива. Пак ѕвонец. Пак — варијација.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch6.to_edge(DOWN, buff=0.3)
        self.play(Write(punch6), run_time=1.0)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t6, sub6, axes, x_lab, y_lab, bars, punch6)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("Растенија — исто како луѓе.",
                      font_size=40, color=GREEN, weight=BOLD)
        final2 = Text("Гените даваат основа.",
                      font_size=38, color=BLUE, weight=BOLD)
        final3 = Text("Средината ја извајува.",
                      font_size=38, color=ORANGE, weight=BOLD)
        final4 = Text("Мендел го дешифрираше шумот.",
                      font_size=34, color=YELLOW)

        finals = VGroup(final1, final2, final3, final4).arrange(DOWN, buff=0.5)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.9)
            self.wait(0.3)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
