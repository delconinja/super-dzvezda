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


class Phys816Scene(Scene):
    def construct(self):
        self.hook()
        self.first_law()
        self.second_law()
        self.third_law()
        self.examples_all_three()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Третиот закон е поетски.", font_size=46, color=YELLOW)
        line2 = Text("На секое туркање — одговор.", font_size=38, color=WHITE2)
        line3 = Text("На секоја акција — реакција.", font_size=38, color=BLUE)
        line4 = Text("Вселената е фер.", font_size=42, color=GREEN)
        grp = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.45)
        self.play(Write(line1))
        self.wait(0.3)
        for ln in [line2, line3, line4]:
            self.play(FadeIn(ln, shift=UP * 0.25))
            self.wait(0.4)
        self.wait(1.5)
        self.play(FadeOut(grp))

    # ── 2. FIRST LAW — INERTIA ────────────────────────────────────────────────
    def first_law(self):
        title = section_title("Прв Њутнов закон — Инерција", color=BLUE)
        self.play(Write(title))

        defn = callout(
            "Телото мирува или се движи рамномерно ако нема нето-сила.",
            width=10.5, border=BLUE, font_size=26)
        defn.shift(UP * 1.6)
        self.play(FadeIn(defn))
        self.wait(0.5)

        # Car + passenger visual
        car_body = RoundedRectangle(width=3.4, height=1.2, corner_radius=0.3,
            fill_color="#1a3555", fill_opacity=1, stroke_color=BLUE, stroke_width=2)
        car_body.shift(LEFT * 1.5 + DOWN * 0.5)

        wheel1 = Circle(radius=0.28, fill_color=DARK_CARD, fill_opacity=1,
                        stroke_color=GREY, stroke_width=2)
        wheel1.move_to(car_body.get_bottom() + LEFT * 0.9 + DOWN * 0.15)
        wheel2 = wheel1.copy().move_to(car_body.get_bottom() + RIGHT * 0.9 + DOWN * 0.15)

        passenger = Circle(radius=0.22, fill_color=ORANGE, fill_opacity=1,
                           stroke_color=YELLOW, stroke_width=2)
        passenger.move_to(car_body.get_center() + UP * 0.1)

        car_grp = VGroup(car_body, wheel1, wheel2, passenger)
        self.play(FadeIn(car_grp))

        # Car brakes — car stops, passenger keeps moving
        brake_lbl = Text("Сопирање!", font_size=26, color=RED).shift(RIGHT * 2.8 + UP * 0.3)
        self.play(Write(brake_lbl))
        # car stops
        self.play(car_grp.animate.shift(RIGHT * 0.3), run_time=0.5)
        # passenger continues
        p_copy = passenger.copy()
        self.add(p_copy)
        self.play(p_copy.animate.shift(RIGHT * 1.8), run_time=1.0)

        note = Text("Патникот продолжува напред — инерција!", font_size=24, color=WHITE2)
        note.shift(DOWN * 2.2)
        self.play(FadeIn(note))
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, defn, car_grp, p_copy, brake_lbl, note)))

    # ── 3. SECOND LAW ─────────────────────────────────────────────────────────
    def second_law(self):
        title = section_title("Втор Њутнов закон  —  F = m × a", color=GREEN)
        self.play(Write(title))

        formula_box = callout("F  =  m  ×  a", width=6.0, border=GREEN, font_size=44)
        formula_box.shift(UP * 1.5)
        self.play(FadeIn(formula_box))

        legends = [
            ("F", RED,    " — сила  [N]"),
            ("m", ORANGE, " — маса  [kg]"),
            ("a", BLUE,   " — забрзување  [m/s²]"),
        ]
        leg = VGroup()
        for sym, col, rest in legends:
            r = VGroup(
                Text(sym, font_size=26, color=col, weight=BOLD),
                Text(rest, font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.15)
            leg.add(r)
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        leg.shift(UP * 0.2)
        self.play(LaggedStart(*[FadeIn(r) for r in leg], lag_ratio=0.2))

        # Box on surface with force arrow
        box = Square(side_length=0.8, fill_color=ORANGE, fill_opacity=1,
                     stroke_color=YELLOW, stroke_width=2)
        box.shift(LEFT * 1.5 + DOWN * 1.6)
        surface = Line(LEFT * 4, RIGHT * 4, stroke_color=GREY, stroke_width=2)
        surface.shift(DOWN * 2.0)
        force_arrow = Arrow(start=box.get_left() + LEFT * 1.2, end=box.get_left(),
                            buff=0, color=RED, stroke_width=3)
        f_lbl = Text("F = 20 N", font_size=20, color=RED).next_to(force_arrow, UP, buff=0.12)
        m_lbl = Text("m = 4 kg", font_size=20, color=ORANGE).move_to(box)

        self.play(Create(surface), FadeIn(box), Write(m_lbl))
        self.play(GrowArrow(force_arrow), Write(f_lbl))
        self.wait(0.3)

        # Result
        result = callout("a = F/m = 20/4 = 5 m/s²", width=7.0, border=YELLOW, font_size=28)
        result.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(result))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, formula_box, leg, box, surface,
                                  force_arrow, f_lbl, m_lbl, result)))

    # ── 4. THIRD LAW ──────────────────────────────────────────────────────────
    def third_law(self):
        title = section_title("Трет Њутнов закон  —  Акција-Реакција", color=ORANGE)
        self.play(Write(title))

        defn = callout(
            "На секоја акција постои еднаква и спротивна реакција.",
            width=10.5, border=ORANGE, font_size=26)
        defn.shift(UP * 1.6)
        self.play(FadeIn(defn))

        # Rocket visual
        rocket_body = RoundedRectangle(width=0.8, height=2.2, corner_radius=0.35,
            fill_color="#2a3f6f", fill_opacity=1, stroke_color=BLUE, stroke_width=2)
        rocket_body.shift(LEFT * 2.5 + DOWN * 0.2)

        tip = Triangle(fill_color=RED, fill_opacity=1, stroke_width=0)
        tip.scale(0.4)
        tip.next_to(rocket_body, UP, buff=-0.1)

        exhaust = Arrow(start=rocket_body.get_bottom(),
                        end=rocket_body.get_bottom() + DOWN * 1.5,
                        buff=0, color=ORANGE, stroke_width=3)
        ex_lbl = Text("Гасови надолу", font_size=20, color=ORANGE)
        ex_lbl.next_to(exhaust, DOWN, buff=0.1)

        rocket_arrow = Arrow(start=rocket_body.get_top(),
                             end=rocket_body.get_top() + UP * 1.5,
                             buff=0, color=GREEN, stroke_width=3)
        rk_lbl = Text("Ракетата нагоре", font_size=20, color=GREEN)
        rk_lbl.next_to(rocket_arrow, UP, buff=0.1)

        self.play(FadeIn(VGroup(rocket_body, tip)))
        self.play(GrowArrow(exhaust), Write(ex_lbl))
        self.play(GrowArrow(rocket_arrow), Write(rk_lbl))
        self.wait(0.5)

        # Walk example
        walk_txt = Text(
            "Ходање: стапалото турка наназад\n→ земјата турка напред",
            font_size=25, color=WHITE2, line_spacing=1.4)
        walk_txt.shift(RIGHT * 2.5 + DOWN * 0.5)
        self.play(FadeIn(walk_txt))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, defn, rocket_body, tip,
                                  exhaust, ex_lbl, rocket_arrow, rk_lbl, walk_txt)))

    # ── 5. ALL THREE — QUICK PANEL ────────────────────────────────────────────
    def examples_all_three(self):
        title = section_title("Три закони — преглед", color=PURPLE)
        self.play(Write(title))

        laws = [
            ("I закон", BLUE,   "Инерција\nАко Fнето=0 → нема промена"),
            ("II закон", GREEN,  "F = m × a\nПоголема сила → поголемо a"),
            ("III закон", ORANGE, "Акција = −Реакција\nСекогаш во пар"),
        ]
        cards = VGroup()
        for name, col, desc in laws:
            card = RoundedRectangle(width=3.6, height=3.0, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.5)
            t_name = Text(name, font_size=30, color=col, weight=BOLD)
            t_name.next_to(card.get_top(), DOWN, buff=0.35)
            t_desc = Text(desc, font_size=21, color=WHITE2, line_spacing=1.35)
            t_desc.move_to(card.get_center() + DOWN * 0.1)
            cards.add(VGroup(card, t_name, t_desc))

        cards.arrange(RIGHT, buff=0.55)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c, scale=0.88) for c in cards], lag_ratio=0.25))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, cards)))

    # ── 6. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (BLUE,   "I закон: без нето-сила → нема промена на движење"),
            (GREEN,  "II закон: F = m × a"),
            (ORANGE, "III закон: акција = −реакција, секогаш во пар"),
            (PURPLE, "Инерција: отпор кон промена на движење"),
            (YELLOW, "Единица за сила: Њутн  [N] = kg·m/s²"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=26, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.shift(DOWN * 0.25)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.2))
        self.wait(1.0)

        fin = Text("Три закони. Еден универзум. Сè е предвидливо.", font_size=28, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
