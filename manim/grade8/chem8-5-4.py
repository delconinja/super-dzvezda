"""
chem8-5-4  —  Согорување на горива и животна средина
Хемија 8, Единица 5: Органска хемија

Teaching narrative — Andonovski-style: three-beat punches,
combustion as transaction, environment as accounting,
one-word finishers.
Render:  manim -ql chem8-5-4.py Chem854Scene
Output:  media/videos/chem8-5-4/480p15/Chem854Scene.mp4
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


class Chem854Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — cenata                                   ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Согорувањето дава енергија.",
                  font_size=42, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.3)
        self.wait(0.4)

        but_lines = VGroup(
            Text("Но дава и CO₂.", font_size=34, color=RED),
            Text("Дава и SO₂.", font_size=34, color=RED),
            Text("Дава и чад.", font_size=34, color=GREY),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN + UP*0.2)

        for line in but_lines:
            self.play(FadeIn(line, shift=UP*0.2), run_time=0.55)
            self.wait(0.2)

        prices = VGroup(
            Text("Цената на топлината.", font_size=30, color=ORANGE),
            Text("Цената на брзината.", font_size=30, color=ORANGE),
            Text("Цената на сè.", font_size=36, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.6)

        for p in prices:
            self.play(FadeIn(p, shift=UP*0.2), run_time=0.55)
            self.wait(0.2)

        self.wait(1.0)
        self.play(FadeOut(VGroup(h1, but_lines, prices)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  COMPLETE COMBUSTION                             ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("complete")

        title = section_title("Целосно согорување", color=GREEN)
        self.play(Write(title), run_time=0.8)

        eq = MathTex(
            r"\mathrm{CH_4}", "+", r"\mathrm{2\,O_2}",
            r"\rightarrow", r"\mathrm{CO_2}", "+", r"\mathrm{2\,H_2O}",
            font_size=52,
        )
        eq[0].set_color(YELLOW)
        eq[2].set_color(BLUE)
        eq[4].set_color(GREEN)
        eq[6].set_color(BLUE)
        eq.move_to(ORIGIN + UP*0.5)

        self.play(Write(eq), run_time=2.0)
        self.wait(0.5)

        # labels under each term
        lbls = VGroup(
            Text("метан", font_size=20, color=GREY).next_to(eq[0], DOWN, buff=0.3),
            Text("доволно\nкислород", font_size=18, color=GREY)
                .next_to(eq[2], DOWN, buff=0.3),
            Text("јаглерод-\nдиоксид", font_size=18, color=GREY)
                .next_to(eq[4], DOWN, buff=0.3),
            Text("вода", font_size=20, color=GREY).next_to(eq[6], DOWN, buff=0.3),
        )
        self.play(FadeIn(lbls), run_time=0.8)
        self.wait(0.8)

        good = callout("Чист пламен. Сино.",
                       width=8, bg=DARK_CARD, border=GREEN, font_size=28)
        good.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(good, shift=UP*0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, eq, lbls, good)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  INCOMPLETE COMBUSTION                           ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("incomplete")

        title2 = section_title("Нецелосно согорување", color=RED)
        self.play(Write(title2), run_time=0.8)

        eq2 = MathTex(
            r"\mathrm{2\,CH_4}", "+", r"\mathrm{3\,O_2}",
            r"\rightarrow", r"\mathrm{2\,CO}", "+", r"\mathrm{4\,H_2O}",
            font_size=44,
        )
        eq2[0].set_color(YELLOW)
        eq2[2].set_color(BLUE)
        eq2[4].set_color(RED)
        eq2[6].set_color(BLUE)
        eq2.move_to(ORIGIN + UP*0.8)

        self.play(Write(eq2), run_time=1.6)
        self.wait(0.4)

        warn_label = Text("малку кислород → CO!",
                          font_size=24, color=YELLOW)
        warn_label.next_to(eq2, DOWN, buff=0.4)
        self.play(FadeIn(warn_label), run_time=0.6)
        self.wait(0.5)

        # dangers
        dangers = VGroup(
            Text("CO — јаглерод-моноксид.",
                 font_size=26, color=RED, weight=BOLD),
            Text("Без боја. Без мирис. Отровен.",
                 font_size=24, color=GREY),
            Text("Чад — нечисто согорување.",
                 font_size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.25)
        dangers.to_edge(DOWN, buff=0.5)

        for d in dangers:
            self.play(FadeIn(d, shift=UP*0.2), run_time=0.5)
            self.wait(0.2)

        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, eq2, warn_label, dangers)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  CO2 RISE — 280 → 420 ppm                        ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("co2_rise")

        title3 = section_title("Стаклена градина", color=ORANGE)
        self.play(Write(title3), run_time=0.8)

        # axes — CO2 ppm rising
        axes = Axes(
            x_range=[1800, 2025, 25],
            y_range=[250, 450, 50],
            x_length=9,
            y_length=4,
            axis_config={"color": GREY, "include_tip": False,
                         "stroke_width": 2},
            x_axis_config={
                "numbers_to_include": [1800, 1850, 1900, 1950, 2000],
                "font_size": 18,
            },
            y_axis_config={
                "numbers_to_include": [300, 350, 400],
                "font_size": 18,
            },
        ).move_to(DOWN*0.2)

        x_lbl = Text("година", font_size=18, color=GREY)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = Text("CO₂ (ppm)", font_size=18, color=GREY)
        y_lbl.next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.2)

        # CO2 curve — slow rise to 1950, steep after
        def co2_func(year):
            if year < 1900:
                return 280 + (year - 1800) * 0.1
            elif year < 1950:
                return 290 + (year - 1900) * 0.4
            else:
                return 310 + (year - 1950) * 1.5

        curve = axes.plot(
            lambda x: co2_func(x),
            x_range=[1800, 2025],
            color=RED, stroke_width=4,
        )

        self.play(Create(curve), run_time=2.2)
        self.wait(0.4)

        # endpoints
        start_dot = Dot(axes.c2p(1800, 280), color=GREEN, radius=0.08)
        start_lbl = Text("280 ppm", font_size=18, color=GREEN)
        start_lbl.next_to(start_dot, UP, buff=0.2)

        end_dot = Dot(axes.c2p(2025, co2_func(2025)), color=RED, radius=0.10)
        end_lbl = Text("420+ ppm", font_size=20, color=RED, weight=BOLD)
        end_lbl.next_to(end_dot, UP, buff=0.2)

        self.play(GrowFromCenter(start_dot), FadeIn(start_lbl), run_time=0.6)
        self.play(GrowFromCenter(end_dot), FadeIn(end_lbl), run_time=0.6)
        self.wait(0.8)

        warming = Text("Земјата задржува повеќе топлина.",
                       font_size=24, color=ORANGE)
        warming.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(warming), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, axes, x_lbl, y_lbl, curve,
                                 start_dot, start_lbl, end_dot, end_lbl,
                                 warming)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ACID RAIN + PARTICULATES                        ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("acid_rain")

        title4 = section_title("Кисел дожд. Чад.", color=RED)
        self.play(Write(title4), run_time=0.8)

        # SO2 + NOx → acid rain
        so2 = MathTex(r"\mathrm{SO_2}", font_size=44, color=YELLOW)
        nox = MathTex(r"\mathrm{NO_x}", font_size=44, color=ORANGE)
        plus = MathTex("+", font_size=44, color=WHITE2)
        h2o = MathTex(r"\mathrm{H_2O}", font_size=44, color=BLUE)
        arrow = MathTex(r"\rightarrow", font_size=44, color=WHITE2)
        acid = MathTex(r"\mathrm{H_2SO_4,\ HNO_3}", font_size=40, color=RED)

        eq_acid = VGroup(so2, Text("+", font_size=36, color=WHITE2),
                         nox, plus, h2o, arrow, acid)
        eq_acid.arrange(RIGHT, buff=0.3).move_to(UP*1.4)

        self.play(Write(eq_acid), run_time=2.0)
        self.wait(0.5)

        acid_lbl = Text("кисел дожд", font_size=26, color=RED, weight=BOLD)
        acid_lbl.next_to(eq_acid, DOWN, buff=0.4)
        self.play(FadeIn(acid_lbl), run_time=0.5)

        damages = VGroup(
            Text("Уништува шуми.", font_size=24, color=GREEN),
            Text("Уништува споменици.", font_size=24, color=GREY),
            Text("Закиселува езера.", font_size=24, color=BLUE),
        ).arrange(DOWN, buff=0.2)
        damages.move_to(DOWN*1.0)

        for d in damages:
            self.play(FadeIn(d, shift=UP*0.15), run_time=0.45)
            self.wait(0.15)

        # particulates
        particulates = Text("Цврсти честички — болни бели дробови.",
                            font_size=22, color=ORANGE)
        particulates.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(particulates), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title4, eq_acid, acid_lbl,
                                 damages, particulates)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  HYDROGEN — CLEAN FUEL                           ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hydrogen")

        title5 = section_title("Водород — најчистото гориво",
                               color=BLUE)
        self.play(Write(title5), run_time=0.9)

        eq_h = MathTex(
            r"\mathrm{2\,H_2}", "+", r"\mathrm{O_2}",
            r"\rightarrow", r"\mathrm{2\,H_2O}",
            font_size=56,
        )
        eq_h[0].set_color(BLUE)
        eq_h[2].set_color(BLUE)
        eq_h[4].set_color(GREEN)
        eq_h.move_to(ORIGIN + UP*0.4)

        self.play(Write(eq_h), run_time=1.8)
        self.wait(0.4)

        only_water = Text("Само вода.",
                          font_size=42, color=GREEN, weight=BOLD)
        only_water.next_to(eq_h, DOWN, buff=0.6)
        self.play(Write(only_water), run_time=1.0)
        self.wait(0.4)

        no_carbon = Text("Без CO₂. Без CO. Без чад.",
                         font_size=26, color=WHITE2)
        no_carbon.next_to(only_water, DOWN, buff=0.4)
        self.play(FadeIn(no_carbon), run_time=0.6)
        self.wait(0.8)

        idn = Text("Иднината.",
                   font_size=44, color=YELLOW, weight=BOLD)
        idn.to_edge(DOWN, buff=0.6)
        self.play(Write(idn), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title5, eq_h, only_water, no_carbon, idn)),
                  run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 7.  FINISHER                                        ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("finisher")

        final = VGroup(
            Text("Секое гориво има цена.", font_size=36, color=WHITE2),
            Text("Прашањето е — кој ја плаќа.",
                 font_size=32, color=ORANGE),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for f in final:
            self.play(FadeIn(f, shift=UP*0.2), run_time=0.8)
            self.wait(0.3)

        self.wait(1.0)

        finisher = Text("Сè.", font_size=60, color=RED, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.7)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(final, finisher)), run_time=1.0)
        self.wait(0.4)
