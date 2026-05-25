"""
bio8-5-6  —  Природна селекција — Дарвин
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: epic of life,
Darwin as patient detective, 1859 as the year the world cracked open.
Render:  manim -ql bio8-5-6.py Bio856Scene
Output:  media/videos/bio8-5-6/480p15/Bio856Scene.mp4
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


def make_finch(beak_width=0.4, color=ORANGE):
    """Returns a stylized finch with variable beak size."""
    body = Ellipse(width=0.9, height=0.7,
                   fill_color=color, fill_opacity=1, stroke_width=0)
    head = Circle(radius=0.3, fill_color=color, fill_opacity=1, stroke_width=0)
    head.move_to(body.get_right() + RIGHT * 0.05)
    eye = Dot(head.get_center() + RIGHT * 0.1 + UP * 0.08,
              radius=0.04, color=BLACK)
    beak = Polygon(
        head.get_right(),
        head.get_right() + RIGHT * beak_width + UP * 0.06,
        head.get_right() + RIGHT * beak_width + DOWN * 0.06,
        fill_color="#5a3a1f", fill_opacity=1, stroke_width=0,
    )
    wing = Ellipse(width=0.5, height=0.3,
                   fill_color="#5a3a1f", fill_opacity=0.6, stroke_width=0)
    wing.move_to(body.get_center() + LEFT * 0.05 + DOWN * 0.05)
    return VGroup(body, head, eye, beak, wing)


def make_moth(color=WHITE2):
    """Returns a stylized peppered moth."""
    body = Ellipse(width=0.2, height=0.5,
                   fill_color="#3a3a3a", fill_opacity=1, stroke_width=0)
    wing_l = Ellipse(width=0.6, height=0.4,
                     fill_color=color, fill_opacity=0.9, stroke_width=1, stroke_color="#1a1a1a")
    wing_l.next_to(body, LEFT, buff=-0.05)
    wing_r = Ellipse(width=0.6, height=0.4,
                     fill_color=color, fill_opacity=0.9, stroke_width=1, stroke_color="#1a1a1a")
    wing_r.next_to(body, RIGHT, buff=-0.05)
    return VGroup(wing_l, wing_r, body)


class Bio856Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Дарвин патувал 5 години.",     font_size=46, color=YELLOW, weight=BOLD)
        hook2 = Text("Видел сè.",                     font_size=50, color=BLUE,   weight=BOLD)
        hook3 = Text("Размислувал 20 години.",        font_size=44, color=ORANGE, weight=BOLD)
        hook4 = Text("Потоа објавил.",                font_size=44, color=GREEN,  weight=BOLD)
        hook5 = Text("1859.",                          font_size=58, color=PURPLE, weight=BOLD)
        hook6 = Text("Целиот свет се промени.",       font_size=36, color=WHITE2, weight=BOLD)

        beats = VGroup(hook1, hook2, hook3, hook4, hook5, hook6).arrange(DOWN, buff=0.35)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(Write(b), run_time=0.85)
            self.wait(0.25)

        self.wait(1.5)
        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ХМС БИГЛ                                          ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("voyage")

        t2 = section_title("Патувањето на HMS Beagle", color=BLUE)
        self.play(Write(t2), run_time=0.9)

        sub = Text("1831 - 1836 · околу светот",
                   font_size=28, color=WHITE2)
        sub.next_to(t2, DOWN, buff=0.3)
        self.play(Write(sub), run_time=0.9)

        # simple map outline
        ellipse = Ellipse(width=10, height=4.5,
                          stroke_color=GREY, stroke_width=2,
                          fill_color="#0a1a2a", fill_opacity=0.7)
        ellipse.shift(DOWN * 0.5)
        self.play(Create(ellipse), run_time=1.0)

        # path with stops
        stops = [
            (-3.5, 0.3, "Англија"),
            (-2.0, -0.8, "Бразил"),
            (-3.0, -1.5, "Аргентина"),
            (-1.5, -1.2, "Галапагос"),
            (1.5, -1.0, "Австралија"),
            (3.5, 0.0, "Африка"),
        ]
        dots = VGroup()
        labels = VGroup()
        for x, y, name in stops:
            d = Dot([x, y - 0.5, 0], color=YELLOW, radius=0.1)
            l = Text(name, font_size=18, color=WHITE2).next_to(d, UP, buff=0.1)
            dots.add(d)
            labels.add(l)

        path_points = [d.get_center() for d in dots]
        path = VMobject(stroke_color=YELLOW, stroke_width=3)
        path.set_points_smoothly(path_points)

        for d, l in zip(dots, labels):
            self.play(FadeIn(d, scale=1.5), Write(l), run_time=0.35)

        self.play(Create(path), run_time=1.5)

        self.wait(0.8)

        punch2 = Text("Гледал. Бележел. Собирал примероци.",
                      font_size=26, color=YELLOW, weight=BOLD)
        punch2.to_edge(DOWN, buff=0.3)
        self.play(Write(punch2), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, sub, ellipse, dots, labels, path, punch2)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ЧЕТИРИ УСЛОВА                                     ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("four_conditions")

        t3 = section_title("Четири услова за природна селекција")
        self.play(Write(t3), run_time=0.9)

        conds = []
        cond_data = [
            ("1", "Варијација",        BLUE,   "Никои двајца не се исти."),
            ("2", "Наследување",       GREEN,  "Особините се пренесуваат на потомците."),
            ("3", "Селективен притисок", ORANGE, "Средината не дозволува сите да преживеат."),
            ("4", "Време",             PURPLE, "Многу генерации. Бавна промена."),
        ]

        groups = VGroup()
        for num, name, col, desc in cond_data:
            panel = RoundedRectangle(
                width=11.0, height=0.95, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(num, font_size=42, color=col, weight=BOLD)
            n.move_to(panel.get_left() + RIGHT * 0.5)
            ttl = Text(name, font_size=28, color=col, weight=BOLD)
            ttl.move_to(panel.get_left() + RIGHT * 2.2)
            ds = Text(desc, font_size=22, color=WHITE2)
            ds.move_to(panel.get_right() + LEFT * 3.0)
            groups.add(VGroup(panel, n, ttl, ds))

        groups.arrange(DOWN, buff=0.2).next_to(t3, DOWN, buff=0.5)

        for g in groups:
            self.play(FadeIn(g, shift=UP * 0.2), run_time=0.7)

        self.wait(0.4)

        punch3 = Text("Сите четири — и природата избира.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch3.to_edge(DOWN, buff=0.3)
        self.play(Write(punch3), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t3, groups, punch3)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ЧИНКИ ОД ГАЛАПАГОС                                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("finches")

        t4 = section_title("Чинките од Галапагос", color=ORANGE)
        self.play(Write(t4), run_time=0.9)

        sub4 = Text("Еден предок. Различни острови. Различни клунчиња.",
                    font_size=26, color=WHITE2)
        sub4.next_to(t4, DOWN, buff=0.3)
        self.play(Write(sub4), run_time=1.0)

        # 4 finches with different beak sizes
        finch_data = [
            (0.25, ORANGE,  "Семиња мали"),
            (0.55, "#c87a4a", "Семиња средни"),
            (0.85, RED,    "Семиња тврди"),
            (0.2,  YELLOW, "Инсекти"),
        ]
        finches = VGroup()
        for beak_w, col, food in finch_data:
            f = make_finch(beak_width=beak_w, color=col)
            label = Text(food, font_size=20, color=WHITE2)
            label.next_to(f, DOWN, buff=0.2)
            finches.add(VGroup(f, label))

        finches.arrange(RIGHT, buff=0.8).next_to(sub4, DOWN, buff=0.7)

        for f in finches:
            self.play(FadeIn(f, shift=UP * 0.2), run_time=0.6)

        self.wait(0.4)

        punch4 = Text("Една реликвија. Илјадници генерации. Нови видови.",
                      font_size=26, color=YELLOW, weight=BOLD)
        punch4.to_edge(DOWN, buff=0.3)
        self.play(Write(punch4), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t4, sub4, finches, punch4)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ПИПЕРНИ ПЕПЕРУТКИ                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("peppered_moth")

        t5 = section_title("Пиперни пеперутки", color=GREY)
        self.play(Write(t5), run_time=0.9)

        # before / after panels
        before = RoundedRectangle(
            width=5.7, height=4.3, corner_radius=0.3,
            fill_color="#d8d8d0", fill_opacity=0.85,
            stroke_color=WHITE2, stroke_width=2,
        ).shift(LEFT * 3.3 + DOWN * 0.3)
        after = RoundedRectangle(
            width=5.7, height=4.3, corner_radius=0.3,
            fill_color="#2a2a28", fill_opacity=0.95,
            stroke_color=GREY, stroke_width=2,
        ).shift(RIGHT * 3.3 + DOWN * 0.3)

        before_lab = Text("Пред индустријата", font_size=24, color="#2a2a2a", weight=BOLD)
        before_lab.move_to(before.get_top() + DOWN * 0.35)
        after_lab = Text("По индустријата", font_size=24, color=WHITE2, weight=BOLD)
        after_lab.move_to(after.get_top() + DOWN * 0.35)

        self.play(FadeIn(before), FadeIn(after),
                  Write(before_lab), Write(after_lab), run_time=1.0)

        # moths on each side
        # Before: mostly white, 1 dark
        before_moths = VGroup(
            make_moth(color=WHITE2),
            make_moth(color=WHITE2),
            make_moth(color=WHITE2),
            make_moth(color="#3a3a3a"),
        )
        for i, m in enumerate(before_moths):
            m.move_to(before.get_center() + np.array([
                -0.9 + (i % 2) * 1.8,
                -0.3 + (i // 2) * 0.9,
                0
            ]))

        after_moths = VGroup(
            make_moth(color="#3a3a3a"),
            make_moth(color="#3a3a3a"),
            make_moth(color="#3a3a3a"),
            make_moth(color=WHITE2),
        )
        for i, m in enumerate(after_moths):
            m.move_to(after.get_center() + np.array([
                -0.9 + (i % 2) * 1.8,
                -0.3 + (i // 2) * 0.9,
                0
            ]))

        for m in before_moths:
            self.play(FadeIn(m, scale=1.3), run_time=0.3)
        for m in after_moths:
            self.play(FadeIn(m, scale=1.3), run_time=0.3)

        self.wait(0.4)

        explain = Text("Чадот ги поцрни дрвјата. Светлите — видливи. Темните — преживуваат.",
                       font_size=22, color=YELLOW, weight=BOLD)
        explain.to_edge(DOWN, buff=0.3)
        self.play(Write(explain), run_time=1.4)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t5, before, after, before_lab, after_lab,
                                  before_moths, after_moths, explain)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  ПРИРОДНА VS ВЕШТАЧКА                              ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("natural_vs_artificial")

        t6 = section_title("Природна vs Вештачка селекција")
        self.play(Write(t6), run_time=0.9)

        left_panel = RoundedRectangle(
            width=5.7, height=4.0, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).shift(LEFT * 3.3 + DOWN * 0.3)
        right_panel = RoundedRectangle(
            width=5.7, height=4.0, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).shift(RIGHT * 3.3 + DOWN * 0.3)

        left_lab = Text("Природна", font_size=32, color=GREEN, weight=BOLD)
        left_lab.move_to(left_panel.get_top() + DOWN * 0.4)
        right_lab = Text("Вештачка", font_size=32, color=ORANGE, weight=BOLD)
        right_lab.move_to(right_panel.get_top() + DOWN * 0.4)

        self.play(FadeIn(left_panel), FadeIn(right_panel),
                  Write(left_lab), Write(right_lab), run_time=1.0)

        left_items = VGroup(
            Text("Бира — средината.", font_size=24, color=WHITE2),
            Text("Бавно. Илјадници години.", font_size=22, color=GREY),
            Text("Пример: чинки, моли.", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.3).next_to(left_lab, DOWN, buff=0.45)

        right_items = VGroup(
            Text("Бира — човекот.", font_size=24, color=WHITE2),
            Text("Брзо. Неколку генерации.", font_size=22, color=GREY),
            Text("Пример: кучиња, крави, пченица.", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.3).next_to(right_lab, DOWN, buff=0.45)

        for li, ri in zip(left_items, right_items):
            self.play(Write(li), Write(ri), run_time=0.55)

        self.wait(0.5)

        bottom = Text("Иста логика. Различен избирач.",
                      font_size=28, color=YELLOW, weight=BOLD)
        bottom.to_edge(DOWN, buff=0.3)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t6, left_panel, right_panel,
                                  left_lab, right_lab,
                                  left_items, right_items, bottom)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("Варијација постои.",         font_size=44, color=BLUE,   weight=BOLD)
        final2 = Text("Особините се наследуваат.",   font_size=40, color=GREEN,  weight=BOLD)
        final3 = Text("Средината избира.",           font_size=42, color=ORANGE, weight=BOLD)
        final4 = Text("Времето вае.",                font_size=44, color=PURPLE, weight=BOLD)
        final5 = Text("Така настануваат видовите.",  font_size=38, color=YELLOW, weight=BOLD)

        finals = VGroup(final1, final2, final3, final4, final5).arrange(DOWN, buff=0.4)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.85)
            self.wait(0.25)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
