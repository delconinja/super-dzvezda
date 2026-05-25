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


class Phys818Scene(Scene):
    def construct(self):
        self.hook()
        self.gravity_law()
        self.mass_vs_weight()
        self.g_table()
        self.free_fall_and_terminal()
        self.orbits()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Месечина пад.", font_size=52, color=BLUE)
        line2 = Text("Секој миг.", font_size=44, color=WHITE2)
        line3 = Text("Но никогаш не стига.", font_size=44, color=YELLOW)
        line4 = Text("Тоа е орбита.  Вечен пад без дно.", font_size=32, color=ORANGE)
        grp = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.48)
        for ln in [line1, line2, line3]:
            self.play(Write(ln), run_time=0.9)
            self.wait(0.3)
        self.play(FadeIn(line4, shift=UP * 0.3))
        self.wait(1.8)
        self.play(FadeOut(grp))

    # ── 2. UNIVERSAL GRAVITATION ──────────────────────────────────────────────
    def gravity_law(self):
        title = section_title("Њутнов закон за гравитација")
        self.play(Write(title))

        formula_box = callout(
            "F  =  G  ×  m₁ × m₂  /  r²",
            width=9.5, border=BLUE, font_size=36)
        formula_box.shift(UP * 1.5)
        self.play(FadeIn(formula_box))

        legends = [
            ("F",  YELLOW, " — гравитациска сила  [N]"),
            ("G",  GREEN,  " — гравитациска константа  6.67×10⁻¹¹ N·m²/kg²"),
            ("m₁,m₂", ORANGE, " — маси на телата  [kg]"),
            ("r",  RED,    " — растојание меѓу центрите  [m]"),
        ]
        leg = VGroup()
        for sym, col, rest in legends:
            r = VGroup(
                Text(sym, font_size=24, color=col, weight=BOLD),
                Text(rest, font_size=24, color=WHITE2),
            ).arrange(RIGHT, buff=0.15)
            leg.add(r)
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        leg.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(r) for r in leg], lag_ratio=0.2))

        note = callout(
            "Секоја маса привлекува секоја друга маса. Секогаш. Насекаде.",
            width=10.5, border=PURPLE, font_size=23)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, formula_box, leg, note)))

    # ── 3. MASS vs WEIGHT ─────────────────────────────────────────────────────
    def mass_vs_weight(self):
        title = section_title("Маса и тежина", color=GREEN)
        self.play(Write(title))

        # Two panel comparison
        cards_data = [
            ("МАСА  m", BLUE,
             "количина материја\nединица: kg\nне зависи од локација\nконстантна насекаде"),
            ("ТЕЖИНА  W", ORANGE,
             "W = m × g\nединица: N\nзависи од g\nсе менува на различни тела"),
        ]
        cards = VGroup()
        for name, col, desc in cards_data:
            card = RoundedRectangle(width=5.0, height=3.8, corner_radius=0.3,
                fill_color=DARK_CARD, fill_opacity=1, stroke_color=col, stroke_width=2.5)
            t_name = Text(name, font_size=28, color=col, weight=BOLD)
            t_name.next_to(card.get_top(), DOWN, buff=0.35)
            t_desc = Text(desc, font_size=22, color=WHITE2, line_spacing=1.4)
            t_desc.move_to(card.get_center() + DOWN * 0.1)
            cards.add(VGroup(card, t_name, t_desc))

        cards.arrange(RIGHT, buff=0.7)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in cards], lag_ratio=0.3))
        self.wait(0.5)

        ex = callout(
            "Пример: m = 60 kg  →  W = 60 × 9.8 = 588 N  (на Земјата)",
            width=10.5, border=YELLOW, font_size=24)
        ex.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(ex))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, cards, ex)))

    # ── 4. g TABLE ────────────────────────────────────────────────────────────
    def g_table(self):
        title = section_title("g на различни небески тела", color=YELLOW)
        self.play(Write(title))

        data = [
            ("Земја",     "9.8 m/s²",  "588 N",  BLUE),
            ("Месечина",  "1.6 m/s²",  "96 N",   GREY),
            ("Марс",      "3.7 m/s²",  "222 N",  RED),
            ("Јупитер",   "24.8 m/s²", "1 488 N", ORANGE),
            ("Сонце",     "274 m/s²",  "16 440 N",YELLOW),
        ]

        hdr = VGroup(
            Text("Тело",    font_size=26, color=WHITE2, weight=BOLD),
            Text("g",       font_size=26, color=WHITE2, weight=BOLD),
            Text("W (60 kg)", font_size=26, color=WHITE2, weight=BOLD),
        ).arrange(RIGHT, buff=1.6)
        hdr.shift(UP * 1.8)
        self.play(FadeIn(hdr))

        sep = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=GREY, stroke_width=1.2)
        sep.next_to(hdr, DOWN, buff=0.18)
        self.play(Create(sep))

        rows = VGroup()
        for name, gval, wval, col in data:
            r = VGroup(
                Text(name,  font_size=24, color=col),
                Text(gval,  font_size=24, color=col),
                Text(wval,  font_size=24, color=col),
            )
            r[0].set_x(hdr[0].get_x())
            r[1].set_x(hdr[1].get_x())
            r[2].set_x(hdr[2].get_x())
            rows.add(r)

        rows.arrange(DOWN, buff=0.32)
        rows.shift(DOWN * 0.25)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.15), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, hdr, sep, rows)))

    # ── 5. FREE FALL & TERMINAL VELOCITY ──────────────────────────────────────
    def free_fall_and_terminal(self):
        title = section_title("Слободен пад и гранична брзина", color=ORANGE)
        self.play(Write(title))

        # Two objects fall together
        ball1 = Circle(radius=0.28, fill_color=ORANGE,
                       fill_opacity=1, stroke_color=YELLOW, stroke_width=2)
        ball2 = Circle(radius=0.45, fill_color=GREEN,
                       fill_opacity=1, stroke_color=WHITE2, stroke_width=2)
        ball1.shift(LEFT * 1.5 + UP * 2.4)
        ball2.shift(RIGHT * 1.5 + UP * 2.4)
        lbl1 = Text("1 kg", font_size=20, color=YELLOW).move_to(ball1)
        lbl2 = Text("5 kg", font_size=20, color=WHITE2).move_to(ball2)

        ground = Line(LEFT * 6, RIGHT * 6, stroke_color=GREY, stroke_width=2)
        ground.shift(DOWN * 2.4)
        self.play(Create(ground), FadeIn(ball1), FadeIn(ball2), Write(lbl1), Write(lbl2))
        self.play(
            ball1.animate.shift(DOWN * 4.8),
            ball2.animate.shift(DOWN * 4.8),
            lbl1.animate.shift(DOWN * 4.8),
            lbl2.animate.shift(DOWN * 4.8),
            run_time=1.8, rate_func=rate_functions.ease_in_quad)
        self.wait(0.2)

        equal_note = callout(
            "Без отпор на воздух — сите паѓаат со исто забрзување g!",
            width=10.5, border=GREEN, font_size=24)
        equal_note.shift(UP * 1.5)
        self.play(FadeIn(equal_note))
        self.wait(0.6)

        terminal_box = callout(
            "Гранична брзина: отпор воздух = тежина → постојана брзина\n"
            "Пример: падобранец ~56 m/s, отворен падобран ~5 m/s",
            width=10.5, bg="#0d2b44", border=PURPLE, font_size=22)
        terminal_box.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(terminal_box))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 6. ORBITS ─────────────────────────────────────────────────────────────
    def orbits(self):
        title = section_title("Орбита = вечен пад", color=BLUE)
        self.play(Write(title))

        # Earth
        earth = Circle(radius=0.7, fill_color="#1a3555", fill_opacity=1,
                       stroke_color=BLUE, stroke_width=2.5)
        earth_lbl = Text("Земја", font_size=20, color=BLUE).move_to(earth)
        self.play(FadeIn(earth), Write(earth_lbl))

        # Orbit path
        orbit = Circle(radius=2.3, stroke_color=GREY, stroke_width=1.5,
                       fill_opacity=0)
        self.play(Create(orbit), run_time=1.0)

        # Moon moving around
        moon = Circle(radius=0.3, fill_color=GREY, fill_opacity=1,
                      stroke_color=WHITE2, stroke_width=1.5)
        moon.shift(RIGHT * 2.3)
        moon_lbl = Text("Месечина", font_size=17, color=WHITE2)
        moon_lbl.next_to(moon, UP, buff=0.12)

        # Velocity arrow + gravity arrow
        vel_arrow = Arrow(start=moon.get_center(),
                          end=moon.get_center() + UP * 1.2,
                          buff=0, color=GREEN, stroke_width=2.5)
        vel_lbl = Text("v (напред)", font_size=18, color=GREEN)
        vel_lbl.next_to(vel_arrow, RIGHT, buff=0.12)

        grav_arrow = Arrow(start=moon.get_center(),
                           end=moon.get_center() + LEFT * 1.2,
                           buff=0, color=RED, stroke_width=2.5)
        grav_lbl = Text("g (кон Земја)", font_size=18, color=RED)
        grav_lbl.next_to(grav_arrow, DOWN, buff=0.12)

        self.play(FadeIn(moon), Write(moon_lbl))
        self.play(GrowArrow(vel_arrow), Write(vel_lbl))
        self.play(GrowArrow(grav_arrow), Write(grav_lbl))
        self.wait(0.5)

        # Orbit explanation
        explain = callout(
            "Месечината паѓа кон Земјата — но се движи толку брзо\n"
            "странично, дека Земјата постојано „бега" под неа.",
            width=10.5, border=BLUE, font_size=22)
        explain.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(explain))
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects))

    # ── 7. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (BLUE,   "F = G×m₁×m₂/r²  (Њутнов закон за гравитација)"),
            (GREEN,  "Маса [kg] ≠ Тежина [N].  W = m × g"),
            (YELLOW, "g на Земја = 9.8 m/s²   (на Месечина = 1.6 m/s²)"),
            (ORANGE, "Без воздух — сите тела паѓаат со исто g"),
            (PURPLE, "Гранична брзина: отпор = тежина"),
            (RED,    "Орбита = вечен пад + странична брзина"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=25, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.37)
        rows.shift(DOWN * 0.2)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.18))
        self.wait(1.0)

        fin = Text("Вечен пад без дно. Тоа е орбита. Тоа е гравитација.", font_size=27, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
