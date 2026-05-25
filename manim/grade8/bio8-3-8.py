"""
bio8-3-8  —  Ензими и температура
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
enzymes as keys, denaturation as silence forever, lock and key.
Render:  manim -ql bio8-3-8.py Bio838Scene
Output:  media/videos/bio8-3-8/480p15/Bio838Scene.mp4
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


def make_enzyme_shape(color=YELLOW, scale=1.0):
    """Pac-man-like shape with a notch — the 'lock'."""
    body = Circle(radius=0.8 * scale, color=color,
                  fill_opacity=0.85, stroke_width=2.5)
    notch = Triangle(color="#0d1b2e",
                     fill_opacity=1, stroke_width=0)
    notch.scale(0.45 * scale)
    notch.move_to(body.get_right() + LEFT * 0.35 * scale)
    notch.rotate(PI / 2)
    return VGroup(body, notch)


def make_substrate(color=GREEN, scale=1.0):
    """Triangle that fits the enzyme notch — the 'key'."""
    sub = Triangle(color=color, fill_opacity=0.9, stroke_width=2.5)
    sub.scale(0.4 * scale)
    sub.rotate(-PI / 2)
    return sub


class Bio838Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~24 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Ензимот има форма.",
                 font_size=40, color=YELLOW, weight=BOLD),
            Text("Како клуч.",
                 font_size=36, color=ORANGE),
            Text("Подгрееш — клучот се крши.",
                 font_size=34, color=RED, weight=BOLD),
            Text("Не работи повеќе.",
                 font_size=34, color=GREY),
            Text("Замолчува.",
                 font_size=40, color=PURPLE, weight=BOLD),
            Text("Засекогаш.",
                 font_size=44, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.35).to_edge(UP, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.85)
            self.wait(0.2)
        self.wait(1.0)
        self.play(FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е ЕНЗИМ                                      ~24 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е ензим?")
        self.play(Write(t2), run_time=0.7)

        defn = callout(
            "Ензим = биолошки катализатор.\n"
            "Забрзува хемиски реакции, без да се троши.",
            width=11.5, font_size=26, border=YELLOW,
        )
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.9)
        self.wait(0.5)

        # show a simple reaction with vs without enzyme
        no_enz = Text("Без ензим: бавно", font_size=26, color=GREY)
        no_enz.shift(LEFT * 3.3 + DOWN * 0.5)

        bar_slow = Rectangle(width=2.0, height=0.4, color=GREY,
                             fill_opacity=0.6, stroke_width=1.5)
        bar_slow.next_to(no_enz, DOWN, buff=0.3)

        with_enz = Text("Со ензим: брзо", font_size=26, color=GREEN, weight=BOLD)
        with_enz.shift(RIGHT * 3.3 + DOWN * 0.5)

        bar_fast = Rectangle(width=4.5, height=0.4, color=GREEN,
                             fill_opacity=0.85, stroke_width=1.5)
        bar_fast.next_to(with_enz, DOWN, buff=0.3)

        self.play(FadeIn(no_enz), FadeIn(with_enz), run_time=0.7)
        self.play(GrowFromEdge(bar_slow, LEFT), run_time=0.8)
        self.play(GrowFromEdge(bar_fast, LEFT), run_time=1.0)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t2, defn, no_enz, with_enz,
                                 bar_slow, bar_fast)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  МОДЕЛ КЛУЧ-БРАВА                                 ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("lock_key")

        t3 = section_title("Модел: клуч–брава", color=ORANGE)
        self.play(Write(t3), run_time=0.7)

        enzyme = make_enzyme_shape(YELLOW, scale=1.0)
        enzyme.shift(LEFT * 3 + DOWN * 0.3)
        enz_lbl = Text("ензим", font_size=22, color=YELLOW)
        enz_lbl.next_to(enzyme, DOWN, buff=0.3)

        substrate = make_substrate(GREEN, scale=1.0)
        substrate.shift(RIGHT * 3.5 + DOWN * 0.3)
        sub_lbl = Text("супстрат", font_size=22, color=GREEN)
        sub_lbl.next_to(substrate, DOWN, buff=0.3)

        self.play(FadeIn(enzyme, shift=RIGHT * 0.2),
                  FadeIn(enz_lbl), run_time=0.7)
        self.play(FadeIn(substrate, shift=LEFT * 0.2),
                  FadeIn(sub_lbl), run_time=0.7)
        self.wait(0.3)

        # substrate moves into enzyme
        target_pos = enzyme[0].get_right() + LEFT * 0.35
        self.play(substrate.animate.move_to(target_pos),
                  sub_lbl.animate.next_to(target_pos, DOWN * 3, buff=0.5),
                  run_time=1.1)
        self.wait(0.4)

        bind_lbl = Text("се поврзуваат",
                        font_size=24, color=YELLOW, weight=BOLD)
        bind_lbl.next_to(enzyme, UP, buff=0.3)
        self.play(Write(bind_lbl), run_time=0.7)
        self.wait(0.4)

        # split substrate into two halves
        half1 = make_substrate(GREEN, scale=0.7)
        half1.move_to(substrate.get_center())
        half2 = make_substrate(GREEN, scale=0.7)
        half2.move_to(substrate.get_center())

        self.play(
            FadeOut(substrate),
            FadeIn(half1),
            FadeIn(half2),
            run_time=0.4,
        )
        self.play(
            half1.animate.shift(RIGHT * 1.5 + UP * 0.4),
            half2.animate.shift(RIGHT * 1.5 + DOWN * 0.4),
            run_time=0.9,
        )

        cleave_lbl = Text("супстратот се разградува",
                          font_size=22, color=GREEN)
        cleave_lbl.next_to(half1, RIGHT, buff=0.3)
        cleave_lbl.shift(DOWN * 0.4)
        self.play(FadeIn(cleave_lbl), run_time=0.6)
        self.wait(0.6)

        rule = callout(
            "Формата мора да одговара. Точно. Само така.",
            width=11.0, font_size=26, border=ORANGE,
        )
        rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t3, enzyme, enz_lbl, sub_lbl, bind_lbl,
                                 half1, half2, cleave_lbl, rule)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ОПТИМАЛНА ТЕМПЕРАТУРА                            ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("temperature")

        t4 = section_title("Оптимална температура", color=RED)
        self.play(Write(t4), run_time=0.7)

        # graph axes
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 1, 0.25],
            x_length=8.5,
            y_length=3.2,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        )
        axes.shift(DOWN * 0.5)

        x_label = Text("температура (°C)", font_size=22, color=WHITE2)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("активност", font_size=22, color=WHITE2)
        y_label.next_to(axes.y_axis, LEFT, buff=0.2)
        y_label.rotate(PI / 2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.0)

        # human enzyme curve — peak at 37°C
        def human_curve(x):
            # gaussian-ish, peaks at 37, drops sharply after 45
            if x < 37:
                return 0.95 * np.exp(-((x - 37) ** 2) / 600)
            else:
                return 0.95 * np.exp(-((x - 37) ** 2) / 60)

        curve = axes.plot(human_curve, x_range=[0, 60], color=GREEN, stroke_width=4)
        self.play(Create(curve), run_time=1.5)

        # peak marker
        peak_dot = Dot(axes.c2p(37, human_curve(37)), color=YELLOW, radius=0.1)
        peak_lbl = Text("37 °C", font_size=22, color=YELLOW, weight=BOLD)
        peak_lbl.next_to(peak_dot, UP, buff=0.2)
        self.play(FadeIn(peak_dot), Write(peak_lbl), run_time=0.7)
        self.wait(0.4)

        # thermophile curve — peak at 95
        def thermo_curve(x):
            if x < 95:
                return 0.85 * np.exp(-((x - 95) ** 2) / 800)
            else:
                return 0.85 * np.exp(-((x - 95) ** 2) / 30)

        thermo = axes.plot(thermo_curve, x_range=[40, 100],
                           color=PURPLE, stroke_width=4)
        self.play(Create(thermo), run_time=1.3)

        thermo_dot = Dot(axes.c2p(95, thermo_curve(95)),
                         color=PURPLE, radius=0.1)
        thermo_lbl = Text("термофили: 95 °C",
                          font_size=20, color=PURPLE)
        thermo_lbl.next_to(thermo_dot, UP, buff=0.15)
        self.play(FadeIn(thermo_dot), Write(thermo_lbl), run_time=0.7)
        self.wait(0.7)

        # legend
        legend = VGroup(
            Text("• Човек: 37 °C", font_size=20, color=GREEN),
            Text("• Термофили: ~95 °C", font_size=20, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend.to_corner(DR, buff=0.4).shift(UP * 0.3)
        self.play(FadeIn(legend, shift=LEFT * 0.2), run_time=0.6)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t4, axes, x_label, y_label, curve,
                                 peak_dot, peak_lbl, thermo, thermo_dot,
                                 thermo_lbl, legend)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ДЕНАТУРАЦИЈА                                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("denaturation")

        t5 = section_title("Денатурација", color=RED)
        self.play(Write(t5), run_time=0.7)

        intro5 = Text("Над оптималната температура — клучот се крши.",
                      font_size=26, color=WHITE2)
        intro5.next_to(t5, DOWN, buff=0.3)
        self.play(FadeIn(intro5), run_time=0.7)
        self.wait(0.3)

        # intact enzyme
        enz_ok = make_enzyme_shape(YELLOW, scale=1.0)
        enz_ok.shift(LEFT * 4 + DOWN * 0.3)
        ok_lbl = Text("активен", font_size=22, color=GREEN)
        ok_lbl.next_to(enz_ok, DOWN, buff=0.3)
        temp_ok = Text("37 °C", font_size=24, color=YELLOW, weight=BOLD)
        temp_ok.next_to(enz_ok, UP, buff=0.3)

        self.play(FadeIn(enz_ok), FadeIn(ok_lbl), FadeIn(temp_ok), run_time=0.7)

        arrow_d = Arrow(LEFT * 1.7, RIGHT * 1.7, color=RED, buff=0.2)
        arrow_d.shift(DOWN * 0.3)
        arrow_lbl = Text("> 60 °C", font_size=22, color=RED, weight=BOLD)
        arrow_lbl.next_to(arrow_d, UP, buff=0.15)
        self.play(GrowArrow(arrow_d), FadeIn(arrow_lbl), run_time=0.7)

        # denatured = warped blob
        warped = VMobject(color=RED, stroke_width=2.5,
                          fill_color=ORANGE, fill_opacity=0.7)
        warped.set_points_as_corners([
            [0.3, 0.6, 0],
            [0.9, 0.3, 0],
            [0.5, -0.2, 0],
            [1.0, -0.4, 0],
            [0.4, -0.8, 0],
            [-0.2, -0.5, 0],
            [-0.7, -0.1, 0],
            [-0.4, 0.5, 0],
            [0.3, 0.6, 0],
        ])
        warped.shift(RIGHT * 4 + DOWN * 0.3)
        warped_lbl = Text("денатуриран", font_size=22, color=RED)
        warped_lbl.next_to(warped, DOWN, buff=0.3)
        temp_bad = Text("80 °C", font_size=24, color=RED, weight=BOLD)
        temp_bad.next_to(warped, UP, buff=0.3)

        self.play(FadeIn(warped, shift=LEFT * 0.2),
                  FadeIn(warped_lbl), FadeIn(temp_bad),
                  run_time=0.8)
        self.wait(0.5)

        warning5 = callout(
            "Денатурацијата е неповратна. Засекогаш.",
            width=10.5, font_size=26, border=RED, bg="#3a1010",
        )
        warning5.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(warning5, shift=UP * 0.2), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(t5, intro5, enz_ok, ok_lbl, temp_ok,
                                 arrow_d, arrow_lbl, warped, warped_lbl,
                                 temp_bad, warning5)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  pH ЗАВИСНОСТ                                     ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ph")

        t6 = section_title("Зависност од pH", color=BLUE)
        self.play(Write(t6), run_time=0.7)

        intro6 = Text("Не само температура. pH исто така.",
                      font_size=28, color=WHITE2)
        intro6.next_to(t6, DOWN, buff=0.3)
        self.play(FadeIn(intro6), run_time=0.7)
        self.wait(0.3)

        # pH scale
        ph_axes = Axes(
            x_range=[0, 14, 2],
            y_range=[0, 1, 0.25],
            x_length=8.5,
            y_length=2.6,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        )
        ph_axes.shift(DOWN * 0.3)
        ph_xlbl = Text("pH", font_size=22, color=WHITE2)
        ph_xlbl.next_to(ph_axes.x_axis, DOWN, buff=0.25)
        self.play(Create(ph_axes), FadeIn(ph_xlbl), run_time=0.9)

        # pepsin curve — peak at ~2
        def pepsin_curve(x):
            return 0.95 * np.exp(-((x - 2) ** 2) / 4)

        pepsin_plot = ph_axes.plot(pepsin_curve, x_range=[0, 7],
                                   color=RED, stroke_width=4)
        pepsin_lbl = Text("пепсин", font_size=20, color=RED, weight=BOLD)
        pepsin_lbl.move_to(ph_axes.c2p(2, 1.1))

        # trypsin curve — peak at ~8
        def trypsin_curve(x):
            return 0.95 * np.exp(-((x - 8) ** 2) / 4)

        trypsin_plot = ph_axes.plot(trypsin_curve, x_range=[4, 13],
                                    color=GREEN, stroke_width=4)
        trypsin_lbl = Text("трипсин", font_size=20, color=GREEN, weight=BOLD)
        trypsin_lbl.move_to(ph_axes.c2p(8, 1.1))

        self.play(Create(pepsin_plot), FadeIn(pepsin_lbl), run_time=1.2)
        self.wait(0.3)
        self.play(Create(trypsin_plot), FadeIn(trypsin_lbl), run_time=1.2)
        self.wait(0.5)

        notes = VGroup(
            Text("• Пепсин: кисело (желудник)", font_size=22, color=RED),
            Text("• Трипсин: алкално (тенко црево)", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        notes.to_edge(DOWN, buff=0.4)
        for n in notes:
            self.play(FadeIn(n, shift=RIGHT * 0.15), run_time=0.5)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t6, intro6, ph_axes, ph_xlbl, pepsin_plot,
                                 pepsin_lbl, trypsin_plot, trypsin_lbl, notes)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conclusion")

        t7 = section_title("Заклучок", color=GREEN)
        self.play(Write(t7), run_time=0.7)

        final = VGroup(
            Text("Ензимот е клуч.",
                 font_size=34, color=YELLOW, weight=BOLD),
            Text("Има точна форма.",
                 font_size=32, color=ORANGE),
            Text("Топлина и pH — го кршат.",
                 font_size=32, color=RED, weight=BOLD),
            Text("Замолчува.",
                 font_size=44, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(t7, DOWN, buff=0.7)

        for line in final:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.85)
            self.wait(0.25)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t7, final)), run_time=0.8)
        self.wait(0.4)
