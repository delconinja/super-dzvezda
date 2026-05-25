from manim import *
import numpy as np

config.background_color = "#0d1b2e"
BLUE   = "#4fc3f7"
YELLOW = "#ffd54f"
GREEN  = "#81c784"
RED    = "#e57373"
GREY   = "#90a4ae"
ORANGE = "#ffb74d"
PURPLE = "#ce93d8"
WHITE2 = "#e8eaf0"
DARK_CARD = "#0f2233"


def callout(text, width=9.0, bg="#0d2b44", border=BLUE, font_size=28):
    box = RoundedRectangle(width=width, height=1.4, corner_radius=0.3,
        fill_color=bg, fill_opacity=1, stroke_color=border, stroke_width=2)
    label = Text(text, font_size=font_size, color=WHITE2)
    label.move_to(box)
    return VGroup(box, label)


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


class Phys815Scene(Scene):
    def construct(self):
        self.hook()
        self.vt_intro()
        self.three_line_types()
        self.acceleration_formula()
        self.area_under_graph()
        self.free_fall()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Поголем наклон — поголемо забрзување.", font_size=42, color=YELLOW)
        line2 = Text("Земјата никогаш не заборава:", font_size=36, color=WHITE2)
        line3 = Text("g = 9.8 m/s²   Секогаш.", font_size=46, color=BLUE)
        grp = VGroup(line1, line2, line3).arrange(DOWN, buff=0.55)
        self.play(Write(line1))
        self.wait(0.4)
        self.play(FadeIn(line2))
        self.wait(0.3)
        self.play(Write(line3))
        self.wait(1.8)
        self.play(FadeOut(grp))

    # ── 2. v-t GRAPH INTRO ────────────────────────────────────────────────────
    def vt_intro(self):
        title = section_title("Графикон брзина–време")
        self.play(Write(title))

        info = [
            ("Оска X  →  Време  t  [s]",     ORANGE),
            ("Оска Y  ↑  Брзина  v  [m/s]",  BLUE),
        ]
        cards = VGroup()
        for txt, col in info:
            c = callout(txt, width=8.0, border=col, font_size=28)
            cards.add(c)
        cards.arrange(DOWN, buff=0.5)
        cards.shift(DOWN * 0.1)

        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.3))
        self.wait(0.6)

        rule = callout("Наклон = забрзување   |   Плоштина = изминато растојание",
                       width=10.5, border=YELLOW, font_size=24)
        rule.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(rule))
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, cards, rule)))

    # ── HELPER ────────────────────────────────────────────────────────────────
    def _make_vt_axes(self, shift=ORIGIN):
        ax = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 12, 2],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.2},
            x_axis_config={"numbers_to_include": [0, 2, 4, 6]},
            y_axis_config={"numbers_to_include": [0, 4, 8, 12]},
        )
        xl = Text("t [s]", font_size=20, color=ORANGE)
        yl = Text("v [m/s]", font_size=20, color=BLUE)
        xl.next_to(ax.x_axis.get_right(), DOWN + RIGHT, buff=0.12)
        yl.next_to(ax.y_axis.get_top(), UP, buff=0.1)
        grp = VGroup(ax, xl, yl)
        grp.shift(shift)
        return ax, xl, yl, grp

    # ── 3. THREE LINE TYPES ───────────────────────────────────────────────────
    def three_line_types(self):
        title = section_title("Три вида линии на v-t графикон", color=GREEN)
        self.play(Write(title))

        configs = [
            ("Постојана брзина",  GREEN,  lambda t: 6,          [0, 6]),
            ("Забрзување",        YELLOW, lambda t: 2 * t,      [0, 6]),
            ("Забавување",        RED,    lambda t: 12 - 2 * t, [0, 6]),
        ]

        # Three mini axes side by side
        panels = VGroup()
        for label, col, func, xr in configs:
            ax = Axes(
                x_range=[0, 6, 2], y_range=[0, 12, 4],
                x_length=3.2, y_length=2.2,
                axis_config={"color": GREY, "stroke_width": 1.5,
                             "include_tip": True, "tip_length": 0.15},
            )
            line = ax.plot(func, x_range=xr, color=col, stroke_width=2.8)
            lbl = Text(label, font_size=22, color=col, weight=BOLD)
            lbl.next_to(ax, DOWN, buff=0.2)
            panels.add(VGroup(ax, line, lbl))

        panels.arrange(RIGHT, buff=0.8)
        panels.shift(DOWN * 0.3)
        self.play(LaggedStart(*[Create(p) for p in panels], lag_ratio=0.3), run_time=2.0)
        self.wait(1.0)

        note = callout("Хоризонтала: a=0   |   Нагоре: a>0   |   Надолу: a<0",
                       width=10.5, border=GREY, font_size=23)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, panels, note)))

    # ── 4. ACCELERATION FORMULA ───────────────────────────────────────────────
    def acceleration_formula(self):
        title = section_title("Забрзување — формула", color=ORANGE)
        self.play(Write(title))

        formula_box = callout("a  =  (v − u) / t", width=7.0, border=ORANGE, font_size=40)
        formula_box.shift(UP * 1.5)
        self.play(FadeIn(formula_box))

        legends = [
            ("a", ORANGE, " — забрзување  [m/s²]"),
            ("v", BLUE,   " — крајна брзина  [m/s]"),
            ("u", GREEN,  " — почетна брзина  [m/s]"),
            ("t", YELLOW, " — време  [s]"),
        ]
        leg = VGroup()
        for sym, col, rest in legends:
            r = VGroup(
                Text(sym, font_size=25, color=col, weight=BOLD),
                Text(rest, font_size=25, color=WHITE2),
            ).arrange(RIGHT, buff=0.15)
            leg.add(r)
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        leg.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(r) for r in leg], lag_ratio=0.2))

        # Example calculation
        ex = callout(
            "Пример: u=0, v=20 m/s, t=4 s  →  a = (20−0)/4 = 5 m/s²",
            width=10.5, border=GREEN, font_size=24)
        ex.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(ex))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, formula_box, leg, ex)))

    # ── 5. AREA UNDER GRAPH = DISTANCE ────────────────────────────────────────
    def area_under_graph(self):
        title = section_title("Плоштина = Растојание", color=PURPLE)
        self.play(Write(title))

        ax, xl, yl, ax_grp = self._make_vt_axes(shift=LEFT * 2.2 + DOWN * 0.3)
        self.play(Create(ax), Write(xl), Write(yl))

        # Constant speed v=6 for t=[0,5]
        line = ax.plot(lambda t: 6, x_range=[0, 5], color=GREEN, stroke_width=3)
        self.play(Create(line), run_time=1.0)

        # Shade the area
        area = ax.get_area(line, x_range=[0, 5], color=GREEN, opacity=0.25)
        self.play(FadeIn(area))

        # Dimension labels
        w_line = Line(ax.c2p(0, 0), ax.c2p(5, 0), stroke_color=YELLOW, stroke_width=2)
        h_line = Line(ax.c2p(0, 0), ax.c2p(0, 6), stroke_color=BLUE, stroke_width=2)
        w_lbl  = Text("t = 5 s", font_size=22, color=YELLOW).next_to(w_line, DOWN, buff=0.2)
        h_lbl  = Text("v = 6 m/s", font_size=22, color=BLUE).next_to(h_line, LEFT, buff=0.2)
        self.play(Create(w_line), Create(h_line), Write(w_lbl), Write(h_lbl))

        exp = VGroup(
            Text("Плоштина = v × t", font_size=28, color=PURPLE, weight=BOLD),
            Text("= 6 × 5 = 30 m", font_size=32, color=WHITE2),
            Text("= изминатото растојание!", font_size=26, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        exp.shift(RIGHT * 2.6 + DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(e) for e in exp], lag_ratio=0.25))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 6. FREE FALL ──────────────────────────────────────────────────────────
    def free_fall(self):
        title = section_title("Слободен пад  —  g = 9.8 m/s²", color=RED)
        self.play(Write(title))

        # Ball drop animation
        ball = Circle(radius=0.3, fill_color=ORANGE, fill_opacity=1,
                      stroke_color=YELLOW, stroke_width=2)
        ball.shift(UP * 2.8)
        ground = Line(LEFT * 5, RIGHT * 5, stroke_color=GREY, stroke_width=2)
        ground.shift(DOWN * 2.5)
        g_lbl = Text("земја", font_size=20, color=GREY).next_to(ground, DOWN, buff=0.15)

        self.play(Create(ground), Write(g_lbl), FadeIn(ball))
        self.play(ball.animate.shift(DOWN * 5.3),
                  run_time=1.8, rate_func=rate_functions.ease_in_quad)
        self.wait(0.2)

        g_box = callout("g = 9.8 m/s²  (забрзување на гравитација)",
                        width=9.0, border=RED, font_size=28)
        g_box.shift(UP * 1.5 + RIGHT * 0.5)
        self.play(FadeIn(g_box))

        tbl_data = [
            ("1 s →", "9.8 m/s",  YELLOW),
            ("2 s →", "19.6 m/s", ORANGE),
            ("3 s →", "29.4 m/s", RED),
        ]
        tbl = VGroup()
        for t_lbl, v_lbl, col in tbl_data:
            r = VGroup(
                Text(t_lbl, font_size=25, color=GREY),
                Text(v_lbl, font_size=25, color=col),
            ).arrange(RIGHT, buff=0.4)
            tbl.add(r)
        tbl.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        tbl.shift(RIGHT * 0.5 + DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(r) for r in tbl], lag_ratio=0.2))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 7. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (GREEN,  "Хоризонтална линија  →  постојана брзина  (a=0)"),
            (YELLOW, "Линија нагоре  →  забрзување  (a>0)"),
            (RED,    "Линија надолу  →  забавување  (a<0)"),
            (ORANGE, "a = (v − u) / t  [m/s²]"),
            (PURPLE, "Плоштина под v-t графикон = растојание"),
            (BLUE,   "Слободен пад:  g = 9.8 m/s²  — секогаш"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=26, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.37)
        rows.shift(DOWN * 0.2)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.18))
        self.wait(1.0)

        fin = Text("Земјата никогаш не заборава. g = 9.8 m/s². Секогаш.", font_size=28, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
