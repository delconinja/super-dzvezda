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


class Phys814Scene(Scene):
    def construct(self):
        self.hook()
        self.axes_intro()
        self.stationary_graph()
        self.constant_velocity_graph()
        self.changing_velocity_graph()
        self.slope_formula()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Еден графикон.", font_size=50, color=YELLOW)
        line2 = Text("Три приказни.", font_size=50, color=BLUE)
        line3 = Text("Читај го и ќе ги знаеш сите.", font_size=36, color=WHITE2)
        grp = VGroup(line1, line2, line3).arrange(DOWN, buff=0.55)
        self.play(Write(line1))
        self.wait(0.3)
        self.play(Write(line2))
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.3))
        self.wait(1.8)
        self.play(FadeOut(grp))

    # ── 2. AXES INTRO ─────────────────────────────────────────────────────────
    def axes_intro(self):
        title = section_title("Графикон растојание–време")
        self.play(Write(title))

        info = [
            ("Оска X  →  Време  t  [s]",      ORANGE),
            ("Оска Y  ↑  Растојание  s  [m]",  GREEN),
        ]
        cards = VGroup()
        for txt, col in info:
            c = callout(txt, width=8.0, border=col, font_size=28)
            cards.add(c)
        cards.arrange(DOWN, buff=0.5)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.3))
        self.wait(0.8)

        rule = callout("Наклонот на линијата = брзина = Δs / Δt",
                       width=9.0, border=YELLOW, font_size=26)
        rule.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(rule))
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, cards, rule)))

    # ── HELPER: build axes ────────────────────────────────────────────────────
    def _make_axes(self, x_range, y_range, x_len=5.5, y_len=3.5):
        ax = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_len,
            y_length=y_len,
            axis_config={"color": GREY, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.2},
            x_axis_config={"numbers_to_include": np.arange(x_range[0], x_range[1]+1, x_range[2])},
            y_axis_config={"numbers_to_include": np.arange(y_range[0], y_range[1]+1, y_range[2])},
        )
        x_lbl = Text("Време  t  [s]", font_size=20, color=ORANGE)
        y_lbl = Text("Растојание  s  [m]", font_size=20, color=GREEN)
        x_lbl.next_to(ax.x_axis.get_right(), DOWN + RIGHT, buff=0.15)
        y_lbl.next_to(ax.y_axis.get_top(), UP + LEFT, buff=0.1)
        y_lbl.rotate(PI / 2)
        return ax, x_lbl, y_lbl

    # ── 3. STATIONARY ─────────────────────────────────────────────────────────
    def stationary_graph(self):
        title = section_title("Случај 1: Мирување", color=RED)
        self.play(Write(title))

        ax, xl, yl = self._make_axes([0, 5, 1], [0, 5, 1])
        ax_grp = VGroup(ax, xl, yl)
        ax_grp.shift(LEFT * 2.5 + DOWN * 0.3)
        self.play(Create(ax), Write(xl), Write(yl))

        line = ax.plot(lambda t: 3, x_range=[0, 5], color=RED, stroke_width=3)
        dot  = Dot(color=RED, radius=0.15).move_to(ax.c2p(0, 3))
        self.play(Create(line), run_time=1.2)
        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(ax.c2p(5, 3)), run_time=1.8)

        exp = VGroup(
            Text("Хоризонтална линија", font_size=27, color=RED, weight=BOLD),
            Text("→  нема промена на растојание", font_size=24, color=WHITE2),
            Text("→  телото МИРУВА", font_size=24, color=WHITE2),
            Text("→  брзина  v = 0", font_size=24, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        exp.shift(RIGHT * 2.8 + DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(e) for e in exp], lag_ratio=0.2))
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, ax_grp, line, dot, exp)))

    # ── 4. CONSTANT VELOCITY ──────────────────────────────────────────────────
    def constant_velocity_graph(self):
        title = section_title("Случај 2: Рамномерно движење", color=GREEN)
        self.play(Write(title))

        ax, xl, yl = self._make_axes([0, 5, 1], [0, 10, 2])
        ax_grp = VGroup(ax, xl, yl)
        ax_grp.shift(LEFT * 2.5 + DOWN * 0.3)
        self.play(Create(ax), Write(xl), Write(yl))

        line = ax.plot(lambda t: 2 * t, x_range=[0, 5], color=GREEN, stroke_width=3)
        dot  = Dot(color=GREEN, radius=0.15).move_to(ax.c2p(0, 0))
        self.play(Create(line), run_time=1.2)
        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(ax.c2p(5, 10)), run_time=2.0)

        # Slope triangle
        p1 = ax.c2p(1, 2)
        p2 = ax.c2p(3, 2)
        p3 = ax.c2p(3, 6)
        tri = Polygon(p1, p2, p3, stroke_color=YELLOW, stroke_width=2,
                      fill_color=YELLOW, fill_opacity=0.12)
        dt_lbl = Text("Δt = 2 s", font_size=20, color=ORANGE).move_to((p1 + p2) / 2 + DOWN * 0.25)
        ds_lbl = Text("Δs = 4 m", font_size=20, color=GREEN).move_to((p2 + p3) / 2 + RIGHT * 0.5)
        self.play(Create(tri), Write(dt_lbl), Write(ds_lbl))

        exp = VGroup(
            Text("Права линија нагоре", font_size=27, color=GREEN, weight=BOLD),
            Text("→  растојанието расте рамномерно", font_size=24, color=WHITE2),
            Text("→  ПОСТОЈАНА брзина", font_size=24, color=WHITE2),
            Text("v = Δs/Δt = 4/2 = 2 m/s", font_size=24, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        exp.shift(RIGHT * 2.8 + DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(e) for e in exp], lag_ratio=0.2))
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, ax_grp, line, dot, tri, dt_lbl, ds_lbl, exp)))

    # ── 5. CHANGING VELOCITY (curved) ─────────────────────────────────────────
    def changing_velocity_graph(self):
        title = section_title("Случај 3: Нерамномерно движење", color=ORANGE)
        self.play(Write(title))

        ax, xl, yl = self._make_axes([0, 5, 1], [0, 25, 5])
        ax_grp = VGroup(ax, xl, yl)
        ax_grp.shift(LEFT * 2.5 + DOWN * 0.3)
        self.play(Create(ax), Write(xl), Write(yl))

        curve = ax.plot(lambda t: t ** 2, x_range=[0, 5], color=ORANGE, stroke_width=3)
        dot   = Dot(color=ORANGE, radius=0.15).move_to(ax.c2p(0, 0))
        self.play(Create(curve), run_time=1.5)
        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(ax.c2p(5, 25)), run_time=2.2,
                  rate_func=rate_functions.ease_in_quad)

        exp = VGroup(
            Text("Крива линија", font_size=27, color=ORANGE, weight=BOLD),
            Text("→  брзината се менува", font_size=24, color=WHITE2),
            Text("→  поголем наклон = поголема брзина", font_size=24, color=WHITE2),
            Text("→  забрзување или забавување", font_size=24, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        exp.shift(RIGHT * 2.8 + DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(e) for e in exp], lag_ratio=0.2))
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, ax_grp, curve, dot, exp)))

    # ── 6. SLOPE FORMULA ──────────────────────────────────────────────────────
    def slope_formula(self):
        title = section_title("Наклон = Брзина", color=BLUE)
        self.play(Write(title))

        formula_box = callout("v  =  Δs  /  Δt", width=6.5, border=BLUE, font_size=42)
        formula_box.shift(UP * 1.0)
        self.play(FadeIn(formula_box))
        self.wait(0.4)

        steeper_txt = Text(
            "Поголем наклон  →  поголема брзина\n"
            "Помал наклон  →  помала брзина\n"
            "Хоризонтална  →  v = 0  (мирување)",
            font_size=26, color=WHITE2, line_spacing=1.45)
        steeper_txt.shift(DOWN * 0.8)
        self.play(FadeIn(steeper_txt))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, formula_box, steeper_txt)))

    # ── 7. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (RED,    "Хоризонтална линија  →  мирување  (v = 0)"),
            (GREEN,  "Права нагоре  →  постојана брзина"),
            (ORANGE, "Поголем наклон  →  поголема брзина"),
            (BLUE,   "Крива  →  нерамномерно движење"),
            (YELLOW, "v = Δs / Δt  (наклон на графикон)"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=27, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.shift(DOWN * 0.3)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.2))
        self.wait(1.0)

        fin = Text("Еден графикон. Три приказни. Читај го.", font_size=30, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
