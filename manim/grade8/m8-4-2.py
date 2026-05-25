"""
m8-4-2  —  Време
Математика 8, Единица 4: Мерки

Andonovski-style: време како лик, единиците како семејство.
Render:  manim -ql m8-4-2.py M842Scene
Output:  media/videos/m8-4-2/480p15/M842Scene.mp4
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


def unit_card(unit, value, color=BLUE, w=2.2, h=1.5):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    u = Text(unit, font_size=22, color=color, weight=BOLD)
    v = Text(value, font_size=24, color=WHITE2)
    u.move_to(box.get_top() + DOWN * 0.35)
    v.move_to(box.get_center() + DOWN * 0.15)
    return VGroup(box, u, v)


class M842Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text(
            "Време не запира. Време не молчи. Време не прости.",
            font_size=36, color=YELLOW, weight=BOLD,
        )
        hook.to_edge(UP, buff=1.0)
        self.play(Write(hook), run_time=2.0)

        sub = Text("Не доцни.", font_size=42, color=RED, weight=BOLD)
        sub.next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(hook), FadeOut(sub), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ЕДИНИЦИ ЗА ВРЕМЕ                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("units")

        title2 = section_title("Единици за време")
        self.play(Write(title2), run_time=1.0)

        units = [
            ("секунда", "s", BLUE),
            ("минута", "min", GREEN),
            ("час", "h", YELLOW),
            ("ден", "day", ORANGE),
            ("недела", "week", PURPLE),
            ("месец", "month", RED),
            ("година", "year", BLUE),
        ]

        cards = VGroup()
        for name, sym, col in units:
            cards.add(unit_card(name, sym, color=col, w=1.7, h=1.3))
        cards.arrange(RIGHT, buff=0.2)
        cards.shift(DOWN * 0.3)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.35)
        self.wait(1.2)

        small_to_big = Arrow(
            start=cards[0].get_bottom() + DOWN * 0.4,
            end=cards[-1].get_bottom() + DOWN * 0.4,
            color=YELLOW, stroke_width=4, buff=0.0,
        )
        lbl = Text("од најмала до најголема", font_size=22, color=WHITE2)
        lbl.next_to(small_to_big, DOWN, buff=0.2)
        self.play(GrowArrow(small_to_big), Write(lbl), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(title2), FadeOut(cards), FadeOut(small_to_big), FadeOut(lbl), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  КОНВЕРЗИИ                                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conversions")

        title3 = section_title("Претворања")
        self.play(Write(title3), run_time=1.0)

        rows = [
            "1 min = 60 s",
            "1 h = 60 min = 3600 s",
            "1 day = 24 h = 1440 min",
            "1 week = 7 days",
            "1 year = 365 days (или 366 — престапна)",
        ]

        eqs = VGroup()
        for r in rows:
            eqs.add(Text(r, font_size=30, color=WHITE2))
        eqs.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        eqs.shift(LEFT * 0.5)

        for e in eqs:
            self.play(Write(e), run_time=0.7)
        self.wait(1.5)

        bracket = Brace(eqs, RIGHT, color=YELLOW)
        bnote = Text("семејство кое брои себе си", font_size=22, color=YELLOW)
        bnote.next_to(bracket, RIGHT, buff=0.2)
        self.play(GrowFromCenter(bracket), Write(bnote), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(title3), FadeOut(eqs), FadeOut(bracket), FadeOut(bnote), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  12-ЧАСОВЕН vs 24-ЧАСОВЕН ФОРМАТ                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("format")

        title4 = section_title("12-часовен и 24-часовен формат")
        self.play(Write(title4), run_time=1.0)

        header_l = Text("12-часовен", font_size=30, color=BLUE, weight=BOLD)
        header_r = Text("24-часовен", font_size=30, color=GREEN, weight=BOLD)
        header_l.move_to(LEFT * 3.3 + UP * 1.8)
        header_r.move_to(RIGHT * 3.3 + UP * 1.8)
        self.play(Write(header_l), Write(header_r), run_time=0.8)

        pairs = [
            ("3:45 PM", "15:45"),
            ("12:00 AM (полноќ)", "00:00"),
            ("12:00 PM (пладне)", "12:00"),
            ("9:30 PM", "21:30"),
        ]

        rows_grp = VGroup()
        for left, right in pairs:
            l = Text(left, font_size=26, color=WHITE2)
            arr = Arrow(LEFT * 0.4, RIGHT * 0.4, color=YELLOW, stroke_width=4, buff=0.0)
            r = Text(right, font_size=26, color=WHITE2)
            row = VGroup(l, arr, r)
            l.move_to(LEFT * 3.3)
            arr.move_to(ORIGIN)
            r.move_to(RIGHT * 3.3)
            rows_grp.add(row)
        rows_grp.arrange(DOWN, buff=0.45)
        rows_grp.shift(DOWN * 0.3)

        # Recenter columns
        for row in rows_grp:
            row[0].set_x(-3.3)
            row[1].set_x(0)
            row[2].set_x(3.3)

        for row in rows_grp:
            self.play(FadeIn(row[0]), GrowArrow(row[1]), FadeIn(row[2]), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(title4), FadeOut(header_l), FadeOut(header_r), FadeOut(rows_grp), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ИЗМИНАТО ВРЕМЕ И СОБИРАЊЕ                       ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("elapsed")

        title5 = section_title("Изминато време")
        self.play(Write(title5), run_time=1.0)

        ex1 = Text("Од 8:30 до 11:15", font_size=32, color=WHITE2)
        ex1.move_to(UP * 1.7)
        self.play(Write(ex1), run_time=0.8)

        steps = VGroup(
            Text("8:30  →  11:00  =  2 h 30 min", font_size=26, color=WHITE2),
            Text("11:00 →  11:15  =  0 h 15 min", font_size=26, color=WHITE2),
            Text("Вкупно: 2 h 45 min", font_size=30, color=GREEN, weight=BOLD),
        )
        steps.arrange(DOWN, buff=0.3)
        steps.next_to(ex1, DOWN, buff=0.5)

        for s in steps:
            self.play(Write(s), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(ex1), FadeOut(steps), run_time=0.5)

        # Adding hours+minutes with carry
        ex2 = Text("Собирање со пренос", font_size=32, color=ORANGE, weight=BOLD)
        ex2.move_to(UP * 1.8)
        self.play(Write(ex2), run_time=0.8)

        add1 = MathTex(r"3\,h\,45\,min \;+\; 2\,h\,30\,min", font_size=42, color=WHITE2)
        add1.move_to(UP * 0.7)
        self.play(Write(add1), run_time=1.0)

        add2 = MathTex(r"=\; 5\,h\,75\,min", font_size=42, color=WHITE2)
        add2.next_to(add1, DOWN, buff=0.3)
        self.play(Write(add2), run_time=0.8)

        note = Text("75 min = 1 h + 15 min  →  префрли еден час", font_size=24, color=YELLOW)
        note.next_to(add2, DOWN, buff=0.3)
        self.play(Write(note), run_time=1.0)

        final = MathTex(r"=\; 6\,h\,15\,min", font_size=44, color=GREEN)
        final.next_to(note, DOWN, buff=0.3)
        self.play(Write(final), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(ex2), FadeOut(add1), FadeOut(add2), FadeOut(note), FadeOut(final), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ТРИАГОЛНИК v-s-t                                ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("speed_triangle")

        title6 = section_title("Брзина, патека, време")
        self.play(Write(title6), run_time=1.0)

        # Draw triangle divided into 3 parts: top = s, bottom-left = v, bottom-right = t
        tri = Polygon(
            UP * 1.6, LEFT * 1.8 + DOWN * 1.0, RIGHT * 1.8 + DOWN * 1.0,
            color=YELLOW, stroke_width=3, fill_color=DARK_CARD, fill_opacity=1,
        )
        tri.shift(LEFT * 3.0 + DOWN * 0.1)

        hline = Line(LEFT * 1.8, RIGHT * 1.8, color=YELLOW, stroke_width=3)
        hline.move_to(tri.get_center() + DOWN * 0.0)
        hline.shift(DOWN * 0.5)
        # Easier: use simple labels in triangle
        s_lbl = Text("s", font_size=44, color=BLUE, weight=BOLD).move_to(tri.get_center() + UP * 0.5)
        v_lbl = Text("v", font_size=44, color=GREEN, weight=BOLD).move_to(tri.get_center() + DOWN * 0.3 + LEFT * 0.7)
        t_lbl = Text("t", font_size=44, color=ORANGE, weight=BOLD).move_to(tri.get_center() + DOWN * 0.3 + RIGHT * 0.7)

        midline = Line(tri.get_left() + RIGHT * 0.0, tri.get_right() + LEFT * 0.0, color=YELLOW, stroke_width=2)
        midline.set_length(3.4)
        midline.move_to(tri.get_center() + DOWN * 0.0)
        vline = Line(midline.get_center() + UP * 0.0, midline.get_center() + DOWN * 1.0, color=YELLOW, stroke_width=2)

        self.play(Create(tri), run_time=1.0)
        self.play(Create(midline), Create(vline), run_time=0.8)
        self.play(Write(s_lbl), Write(v_lbl), Write(t_lbl), run_time=1.0)

        # Formulas on the right
        formulas = VGroup(
            MathTex(r"v = \frac{s}{t}", font_size=44, color=GREEN),
            MathTex(r"s = v \cdot t", font_size=44, color=BLUE),
            MathTex(r"t = \frac{s}{v}", font_size=44, color=ORANGE),
        )
        formulas.arrange(DOWN, buff=0.6)
        formulas.move_to(RIGHT * 3.0)

        for f in formulas:
            self.play(Write(f), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(tri), FadeOut(midline), FadeOut(vline),
                  FadeOut(s_lbl), FadeOut(v_lbl), FadeOut(t_lbl),
                  FadeOut(formulas), run_time=0.6)

        # Examples
        examples = VGroup(
            MathTex(r"80\,\tfrac{km}{h} \times 2{,}5\,h = 200\,km", font_size=36, color=WHITE2),
            MathTex(r"\tfrac{300\,km}{4\,h} = 75\,\tfrac{km}{h}", font_size=36, color=WHITE2),
            MathTex(r"\tfrac{150\,km}{60\,\tfrac{km}{h}} = 2{,}5\,h", font_size=36, color=WHITE2),
        )
        examples.arrange(DOWN, buff=0.5)
        examples.shift(DOWN * 0.2)
        for e in examples:
            self.play(Write(e), run_time=1.1)
        self.wait(1.5)

        self.play(FadeOut(title6), FadeOut(examples), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ПРОСЕЧНА БРЗИНА + ВРЕМЕНСКИ ЗОНИ                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("avg_zones")

        title7 = section_title("Просечна брзина")
        self.play(Write(title7), run_time=1.0)

        warn = Text("Не е просек од брзините — туку вкупна патека низ вкупно време.",
                    font_size=26, color=YELLOW)
        warn.move_to(UP * 1.8)
        self.play(Write(warn), run_time=1.5)

        ex = VGroup(
            Text("60 km за 1 h, потоа 40 km за 2 h", font_size=28, color=WHITE2),
            MathTex(r"v_{avg} = \frac{60 + 40}{1 + 2} = \frac{100}{3} \approx 33{,}3\,\tfrac{km}{h}",
                    font_size=36, color=GREEN),
        )
        ex.arrange(DOWN, buff=0.5)
        ex.shift(DOWN * 0.3)

        for e in ex:
            self.play(Write(e), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(title7), FadeOut(warn), FadeOut(ex), run_time=0.6)

        # Time zones
        title_z = section_title("Временски зони")
        self.play(Write(title_z), run_time=1.0)

        strip = Rectangle(width=11, height=1.2,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=BLUE, stroke_width=2)
        strip.shift(UP * 0.3)
        self.play(Create(strip), run_time=0.8)

        zones = [
            ("NYC\nUTC-5\n08:00", -4.3, RED),
            ("Лондон\nUTC+0\n13:00", -1.8, YELLOW),
            ("Скопје\nUTC+1\n14:00", 0.5, GREEN),
            ("Москва\nUTC+3\n16:00", 3.0, BLUE),
        ]

        zone_grp = VGroup()
        for label, x, col in zones:
            t = Text(label, font_size=18, color=col, weight=BOLD)
            t.move_to(np.array([x, 0.3, 0]))
            zone_grp.add(t)

        for z in zone_grp:
            self.play(FadeIn(z, shift=UP * 0.2), run_time=0.4)
        self.wait(1.0)

        note = Text("Кога во Скопје е 14:00, во Њујорк е 08:00 (6 часа разлика).",
                    font_size=24, color=WHITE2)
        note.shift(DOWN * 1.8)
        self.play(Write(note), run_time=1.5)
        self.wait(1.5)

        summer = Text("Лето: Скопје преминува во UTC+2 (CEST).",
                      font_size=22, color=ORANGE)
        summer.next_to(note, DOWN, buff=0.3)
        self.play(Write(summer), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(title_z), FadeOut(strip), FadeOut(zone_grp),
                  FadeOut(note), FadeOut(summer), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  CLOSING                                         ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        close = Text("Времето не чека. Затоа го мериме.",
                     font_size=38, color=YELLOW, weight=BOLD)
        close.move_to(ORIGIN)
        self.play(Write(close), run_time=1.5)
        self.wait(2.0)

        self.play(FadeOut(close), run_time=0.8)
