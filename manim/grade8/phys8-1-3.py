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


class Phys813Scene(Scene):
    def construct(self):
        self.hook()
        self.formula_def()
        self.formula_triangle()
        self.speed_table()
        self.avg_vs_instant()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Пешаци.  1.4 m/s.", font_size=46, color=WHITE2)
        line2 = Text("Светлина.  300 000 km/s.", font_size=46, color=YELLOW)
        line3 = Text("Истата формула.  Различни светови.", font_size=34, color=BLUE)
        grp = VGroup(line1, line2, line3).arrange(DOWN, buff=0.55)
        grp.move_to(ORIGIN)

        self.play(Write(line1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.3))
        self.wait(1.8)
        self.play(FadeOut(grp))

    # ── 2. ФОРМУЛА И ДЕФИНИЦИЈА ───────────────────────────────────────────────
    def formula_def(self):
        title = section_title("Брзина — дефиниција")
        self.play(Write(title))

        defn = Text(
            "Брзина е растојанието поминато за единица\nвреме во одредена насока.",
            font_size=30, color=WHITE2, line_spacing=1.4)
        defn.shift(UP * 1.0)
        self.play(FadeIn(defn))
        self.wait(0.8)

        formula_box = callout("v  =  s  /  t", width=6.0, border=GREEN, font_size=44)
        formula_box.shift(DOWN * 0.3)
        self.play(FadeIn(formula_box))
        self.wait(0.5)

        units = [
            ("v", BLUE,   "— брзина  [m/s]  или  [km/h]"),
            ("s", GREEN,  "— растојание  [m]  или  [km]"),
            ("t", ORANGE, "— време  [s]  или  [h]"),
        ]
        leg = VGroup()
        for sym, col, rest in units:
            r = VGroup(
                Text(sym, font_size=26, color=col, weight=BOLD),
                Text(rest, font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.2)
            leg.add(r)
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        leg.next_to(formula_box, DOWN, buff=0.5)

        self.play(LaggedStart(*[FadeIn(r) for r in leg], lag_ratio=0.2))
        self.wait(0.6)

        conv = callout("Конверзија:  km/h  ÷ 3.6  =  m/s    |    m/s  × 3.6  =  km/h",
                       width=10.5, border=PURPLE, font_size=24)
        conv.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(conv))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, defn, formula_box, leg, conv)))

    # ── 3. ФОРМУЛАРЕН ТРИАГОЛНИК ──────────────────────────────────────────────
    def formula_triangle(self):
        title = section_title("Формуларен триаголник", color=BLUE)
        self.play(Write(title))

        # Draw triangle
        tri_pts = [UP * 1.8, DOWN * 0.9 + LEFT * 1.8, DOWN * 0.9 + RIGHT * 1.8]
        tri = Polygon(*tri_pts, stroke_color=BLUE, stroke_width=3,
                      fill_color=DARK_CARD, fill_opacity=1)
        tri.shift(LEFT * 2.5 + DOWN * 0.2)

        top_lbl  = Text("v", font_size=38, color=YELLOW, weight=BOLD)
        bot_left = Text("s", font_size=38, color=GREEN, weight=BOLD)
        bot_rgt  = Text("t", font_size=38, color=ORANGE, weight=BOLD)

        top_lbl.move_to(tri.get_top() + DOWN * 0.55 + RIGHT * 0.0)
        bot_left.move_to(tri.get_bottom() + UP * 0.45 + LEFT * 0.85)
        bot_rgt.move_to(tri.get_bottom() + UP * 0.45 + RIGHT * 0.85)

        # Divider line inside triangle
        div = Line(tri.get_left() + RIGHT * 0.3, tri.get_right() + LEFT * 0.3,
                   stroke_color=GREY, stroke_width=1.5)
        div.shift(LEFT * 2.5 + DOWN * 0.2)  # align with triangle

        self.play(Create(tri), run_time=0.9)
        self.play(Write(top_lbl), Write(bot_left), Write(bot_rgt), Create(div))
        self.wait(0.4)

        # Derived formulas
        derives = [
            ("v  =  s ÷ t", YELLOW, RIGHT * 1.0 + UP * 1.2),
            ("s  =  v × t", GREEN,  RIGHT * 1.0 + UP * 0.2),
            ("t  =  s ÷ v", ORANGE, RIGHT * 1.0 + DOWN * 0.8),
        ]
        for fml, col, pos in derives:
            fb = callout(fml, width=5.0, border=col, font_size=30)
            fb.shift(pos + RIGHT * 0.8)
            self.play(FadeIn(fb), run_time=0.6)
            self.wait(0.3)

        instr = Text("Покрий ја величината — триаголникот покажува формула!",
                     font_size=23, color=GREY)
        instr.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(instr))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 4. ТАБЕЛА НА БРЗИНИ ───────────────────────────────────────────────────
    def speed_table(self):
        title = section_title("Споредба на брзини", color=GREEN)
        self.play(Write(title))

        data = [
            ("Полжав",        "0.001 m/s",   "0.004 km/h",  GREY),
            ("Пешак",         "1.4 m/s",     "5 km/h",      WHITE2),
            ("Велосипедист",  "8 m/s",       "30 km/h",     GREEN),
            ("Автомобил",     "28 m/s",      "100 km/h",    YELLOW),
            ("Авион",         "250 m/s",     "900 km/h",    ORANGE),
            ("Звук (воздух)", "340 m/s",     "1 225 km/h",  BLUE),
            ("Светлина",      "300 000 km/s","—",           PURPLE),
        ]

        headers = ["Предмет", "m/s", "km/h"]
        hdr_row = VGroup(*[Text(h, font_size=26, color=YELLOW, weight=BOLD) for h in headers])
        hdr_row.arrange(RIGHT, buff=1.8)
        hdr_row.shift(UP * 1.8)
        self.play(FadeIn(hdr_row))

        row_group = VGroup()
        for name, ms, kmh, col in data:
            r = VGroup(
                Text(name, font_size=23, color=col),
                Text(ms,   font_size=23, color=col),
                Text(kmh,  font_size=23, color=col),
            )
            r[0].set_x(hdr_row[0].get_x())
            r[1].set_x(hdr_row[1].get_x())
            r[2].set_x(hdr_row[2].get_x())
            row_group.add(r)

        row_group.arrange(DOWN, buff=0.3)
        row_group.shift(DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(r) for r in row_group], lag_ratio=0.12), run_time=1.8)
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, hdr_row, row_group)))

    # ── 5. ПРОСЕЧНА vs МОМЕНТНА БРЗИНА ────────────────────────────────────────
    def avg_vs_instant(self):
        title = section_title("Просечна и моментна брзина", color=ORANGE)
        self.play(Write(title))

        # Road with car
        road = Rectangle(width=10, height=0.6, fill_color="#1a1a2e",
                         fill_opacity=1, stroke_width=0)
        road.shift(DOWN * 0.5)
        dash = DashedLine(LEFT * 5, RIGHT * 5, dash_length=0.4,
                          stroke_color=YELLOW, stroke_width=2)
        dash.shift(DOWN * 0.5)

        start_dot = Dot(color=GREEN, radius=0.15).shift(LEFT * 4.5 + DOWN * 0.5)
        end_dot   = Dot(color=RED,   radius=0.15).shift(RIGHT * 4.5 + DOWN * 0.5)
        s_lbl = Text("A", font_size=22, color=GREEN).next_to(start_dot, UP, buff=0.2)
        e_lbl = Text("B", font_size=22, color=RED).next_to(end_dot, UP, buff=0.2)

        car = RegularPolygon(n=6, fill_color=BLUE, fill_opacity=1,
                             stroke_color=WHITE2, stroke_width=1.5, radius=0.35)
        car.shift(LEFT * 4.5 + DOWN * 0.5)

        self.play(Create(road), Create(dash))
        self.play(FadeIn(start_dot), FadeIn(end_dot), Write(s_lbl), Write(e_lbl))
        self.play(FadeIn(car))
        self.play(car.animate.shift(RIGHT * 9), run_time=2.5, rate_func=there_and_back_with_pause)

        avg_note = callout(
            "Просечна брзина:  v = вкупно растојание / вкупно време",
            width=10.5, border=GREEN, font_size=25)
        avg_note.to_edge(DOWN, buff=0.7)
        inst_note = callout(
            "Моментна брзина:  брзиномерот во дадена секунда",
            width=10.5, border=ORANGE, font_size=25)
        inst_note.to_edge(DOWN, buff=0.1)

        self.play(FadeIn(avg_note), FadeIn(inst_note))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 6. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (BLUE,   "v = s / t"),
            (GREEN,  "Единици: m/s  и  km/h"),
            (YELLOW, "Конверзија: ÷ 3.6 или × 3.6"),
            (ORANGE, "Просечна брзина: вкупен пат / вкупно време"),
            (PURPLE, "Моментна брзина: во дадена точка"),
            (RED,    "Светлина: 300 000 km/s — максимум!"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=27, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.37)
        rows.shift(DOWN * 0.3)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.18))
        self.wait(1.0)

        fin = Text("Истата формула. Различни светови. Еден закон.", font_size=29, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
