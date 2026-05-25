"""
m8-4-1  —  Должина, маса и зафатнина
Математика 8, Единица 4: Мерење

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Render:  manim -ql m8-4-1.py M841Scene
Output:  media/videos/m8-4-1/480p15/M841Scene.mp4
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


def unit_step(label, color, pos):
    box = RoundedRectangle(
        width=1.8, height=1.0, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=3,
    ).move_to(pos)
    txt = Text(label, font_size=32, color=color, weight=BOLD).move_to(box)
    return VGroup(box, txt)


class M841Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Грам и километар.", font_size=44, color=YELLOW, weight=BOLD),
            Text("Различни.", font_size=38, color=WHITE2),
            Text("Но истиот свет.", font_size=38, color=BLUE),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.4)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)

        f1 = Text("Метричкиот систем не реди.", font_size=32, color=GREEN)
        f2 = Text("Метричкиот систем мисли.", font_size=40, color=ORANGE, weight=BOLD)
        VGroup(f1, f2).arrange(DOWN, buff=0.3).move_to(DOWN * 2.0)
        self.play(FadeIn(f1, shift=UP * 0.2), run_time=0.7)
        self.play(Write(f2), run_time=1.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(beats, f1, f2)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  LENGTH UNITS                                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("length")
        title = section_title("Должина  —  скали")
        self.play(FadeIn(title), run_time=0.6)

        # ladder of units
        mm = unit_step("мм", BLUE, LEFT * 5.5 + UP * 0.5)
        cm = unit_step("см", GREEN, LEFT * 2.0 + UP * 0.5)
        m = unit_step("м", YELLOW, RIGHT * 1.5 + UP * 0.5)
        km = unit_step("км", ORANGE, RIGHT * 5.0 + UP * 0.5)

        self.play(LaggedStart(FadeIn(mm), FadeIn(cm), FadeIn(m), FadeIn(km), lag_ratio=0.2))

        # arrows ×10, ×100, ×1000
        def mk_arrow(start, end, label, color):
            a = Arrow(start, end, color=color, buff=0.1, stroke_width=4,
                      max_tip_length_to_length_ratio=0.15)
            lbl = Text(label, font_size=24, color=color, weight=BOLD).next_to(a, UP, buff=0.1)
            return VGroup(a, lbl)

        a1 = mk_arrow(mm.get_right(), cm.get_left(), "× 10", YELLOW)
        a2 = mk_arrow(cm.get_right(), m.get_left(), "× 100", YELLOW)
        a3 = mk_arrow(m.get_right(), km.get_left(), "× 1000", YELLOW)
        self.play(LaggedStart(FadeIn(a1), FadeIn(a2), FadeIn(a3), lag_ratio=0.3))
        self.wait(0.6)

        # facts below
        facts = VGroup(
            Text("1 см = 10 мм", font_size=26, color=WHITE2),
            Text("1 м = 100 см = 1000 мм", font_size=26, color=WHITE2),
            Text("1 км = 1000 м", font_size=26, color=WHITE2),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 1.8)
        for f in facts:
            self.play(FadeIn(f, shift=UP * 0.1), run_time=0.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, mm, cm, m, km, a1, a2, a3, facts)),
                  run_time=0.7)

        # imperial conversions
        title_imp = section_title("Не-метрички мерки", color=GREY)
        self.play(FadeIn(title_imp), run_time=0.5)

        imp = VGroup(
            MathTex("1\\,\\text{милја} \\approx 1{,}6\\,\\text{км}",
                    font_size=44, color=BLUE),
            MathTex("1\\,\\text{јард} \\approx 0{,}914\\,\\text{м}",
                    font_size=44, color=GREEN),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        for i in imp:
            self.play(Write(i), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title_imp, imp)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MASS UNITS                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mass")
        title2 = section_title("Маса", color=GREEN)
        self.play(FadeIn(title2), run_time=0.5)

        # balance scale visual
        base = Line(LEFT * 0.8, RIGHT * 0.8, color=WHITE2, stroke_width=4)
        base.move_to(DOWN * 0.5)
        stem = Line(ORIGIN, UP * 1.5, color=WHITE2, stroke_width=4).move_to(UP * 0.25)
        bar = Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE2, stroke_width=4).move_to(UP * 1.0)
        left_pan = Polygon(
            [-2.8, 0.7, 0], [-2.2, 0.7, 0], [-2.4, 0.4, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.3,
        )
        right_pan = Polygon(
            [2.8, 0.7, 0], [2.2, 0.7, 0], [2.4, 0.4, 0],
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.3,
        )
        left_str = Line(LEFT * 2.5 + UP * 1.0, LEFT * 2.5 + UP * 0.7, color=WHITE2, stroke_width=2)
        right_str = Line(RIGHT * 2.5 + UP * 1.0, RIGHT * 2.5 + UP * 0.7, color=WHITE2, stroke_width=2)
        scale = VGroup(base, stem, bar, left_str, right_str, left_pan, right_pan)
        scale.shift(UP * 0.3)

        left_lbl = Text("1 кг", font_size=30, color=GREEN).next_to(left_pan, UP, buff=0.2)
        right_lbl = Text("1000 г", font_size=30, color=ORANGE).next_to(right_pan, UP, buff=0.2)

        self.play(Create(scale))
        self.play(FadeIn(left_lbl), FadeIn(right_lbl))
        self.wait(0.6)

        facts2 = VGroup(
            Text("1 г = 1000 мг", font_size=28, color=BLUE),
            Text("1 кг = 1000 г", font_size=28, color=GREEN),
            Text("1 тон = 1000 кг", font_size=28, color=ORANGE),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 2.4)
        for f in facts2:
            self.play(FadeIn(f, shift=UP * 0.1), run_time=0.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title2, scale, left_lbl, right_lbl, facts2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  VOLUME UNITS                                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("volume")
        title3 = section_title("Зафатнина", color=BLUE)
        self.play(FadeIn(title3), run_time=0.5)

        # measuring cylinder
        cyl = RoundedRectangle(
            width=1.8, height=4.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=0.5,
            stroke_color=BLUE, stroke_width=3,
        ).move_to(LEFT * 4.0 + DOWN * 0.2)
        # water level
        water = Rectangle(width=1.7, height=2.5, color=BLUE,
                          fill_color=BLUE, fill_opacity=0.5, stroke_width=0)
        water.move_to(cyl.get_bottom() + UP * 1.30)

        # tick marks
        ticks = VGroup()
        tick_labels = VGroup()
        for i, val in enumerate(["1000 мл", "750", "500", "250", "0"]):
            y_pos = cyl.get_bottom()[1] + 0.1 + i * 0.9
            t = Line([cyl.get_left()[0], y_pos, 0], [cyl.get_left()[0] + 0.25, y_pos, 0],
                     color=BLUE, stroke_width=2)
            ticks.add(t)
            tl = Text(val, font_size=18, color=WHITE2).next_to(t, LEFT, buff=0.1)
            tick_labels.add(tl)

        self.play(Create(cyl))
        self.play(Create(ticks), FadeIn(tick_labels))
        self.play(FadeIn(water), run_time=1.0)
        self.wait(0.4)

        facts3 = VGroup(
            Text("1 л = 1000 мл", font_size=30, color=BLUE),
            Text("1 м³ = 1000 л", font_size=30, color=GREEN),
            Text("1 см³ = 1 мл", font_size=30, color=ORANGE),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.5)
        for f in facts3:
            self.play(FadeIn(f, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, cyl, water, ticks, tick_labels, facts3)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  WATER SPECIAL CONNECTION                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("water")
        title4 = section_title("Вода  —  магичен сооднос", color=BLUE)
        self.play(FadeIn(title4), run_time=0.5)

        # water drop
        drop = Polygon(
            [0, 1, 0], [0.7, 0, 0], [0.4, -0.7, 0], [-0.4, -0.7, 0], [-0.7, 0, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.4, stroke_width=3,
        ).scale(0.8).move_to(LEFT * 4.0)
        self.play(Create(drop))

        magic = VGroup(
            MathTex("1\\,\\text{кг вода}", font_size=44, color=BLUE),
            MathTex("=", font_size=44, color=WHITE2),
            MathTex("1\\,\\text{литар}", font_size=44, color=GREEN),
            MathTex("=", font_size=44, color=WHITE2),
            MathTex("1000\\,\\text{см}^3", font_size=44, color=ORANGE),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 2.0)

        for m_ in magic:
            self.play(Write(m_), run_time=0.7)

        note = callout("маса ↔ зафатнина  —  поврзани со густина",
                       width=10.0, border=YELLOW, font_size=26)
        note.shift(DOWN * 3.0)
        self.play(FadeIn(note))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title4, drop, magic, note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  DENSITY                                          ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("density")
        title5 = section_title("Густина  D = m / V", color=ORANGE)
        self.play(FadeIn(title5), run_time=0.5)

        formula = MathTex(
            "D", "=", "\\frac{m}{V}",
            font_size=72, color=WHITE2,
        )
        formula[0].set_color(ORANGE)
        formula[2].set_color(BLUE)
        formula.move_to(UP * 1.8)
        self.play(Write(formula), run_time=1.4)
        self.wait(0.5)

        # three substances
        def density_card(name, value, color, pos):
            box = RoundedRectangle(
                width=3.0, height=1.6, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            ).move_to(pos)
            nm = Text(name, font_size=26, color=color, weight=BOLD)
            val = MathTex(value, font_size=28, color=WHITE2)
            VGroup(nm, val).arrange(DOWN, buff=0.15).move_to(box)
            return VGroup(box, nm, val)

        water_c = density_card("Вода", "1\\,\\text{г/см}^3", BLUE, LEFT * 4.0 + DOWN * 0.5)
        ice_c = density_card("Мраз", "0{,}92\\,\\text{г/см}^3", GREEN, ORIGIN + DOWN * 0.5)
        steel_c = density_card("Челик", "7{,}8\\,\\text{г/см}^3", GREY, RIGHT * 4.0 + DOWN * 0.5)

        self.play(LaggedStart(FadeIn(water_c), FadeIn(ice_c), FadeIn(steel_c), lag_ratio=0.3))
        self.wait(0.6)

        float_note = Text("мраз < вода  →  плови",
                          font_size=28, color=YELLOW, weight=BOLD)
        float_note.move_to(DOWN * 2.4)
        self.play(Write(float_note), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(VGroup(title5, formula, water_c, ice_c, steel_c, float_note)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  WORKED EXAMPLES                                  ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("examples")
        title6 = section_title("Примери", color=GREEN)
        self.play(FadeIn(title6), run_time=0.5)

        # Stone density example
        ex1_title = Text("1. Камен  200 г, 50 см³", font_size=28, color=YELLOW)
        ex1_title.move_to(UP * 1.8 + LEFT * 3.5)
        ex1_calc = MathTex(
            "D = \\frac{200}{50} = 4\\,\\text{г/см}^3",
            font_size=36, color=GREEN,
        )
        ex1_calc.next_to(ex1_title, DOWN, buff=0.3).align_to(ex1_title, LEFT)
        self.play(FadeIn(ex1_title))
        self.play(Write(ex1_calc), run_time=1.4)
        self.wait(0.6)

        # Apples cost
        ex2_title = Text("2. Јаболка  0,75 кг × 80 ден/кг", font_size=28, color=YELLOW)
        ex2_title.move_to(LEFT * 3.5 + UP * 0.1)
        ex2_calc = MathTex(
            "0{,}75 \\cdot 80 = 60\\,\\text{ден}",
            font_size=36, color=ORANGE,
        )
        ex2_calc.next_to(ex2_title, DOWN, buff=0.3).align_to(ex2_title, LEFT)
        self.play(FadeIn(ex2_title))
        self.play(Write(ex2_calc), run_time=1.4)
        self.wait(0.6)

        # Pool volume
        ex3_title = Text("3. Базен  3 × 5 × 2 м", font_size=28, color=YELLOW)
        ex3_title.move_to(LEFT * 3.5 + DOWN * 1.6)
        ex3_calc = MathTex(
            "V = 30\\,\\text{м}^3 = 30\\,000\\,\\text{литри}",
            font_size=36, color=BLUE,
        )
        ex3_calc.next_to(ex3_title, DOWN, buff=0.3).align_to(ex3_title, LEFT)
        self.play(FadeIn(ex3_title))
        self.play(Write(ex3_calc), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(title6, ex1_title, ex1_calc, ex2_title, ex2_calc,
                                 ex3_title, ex3_calc)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 8.  CHOOSING UNITS                                   ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("choose")
        title7 = section_title("Која мерка кога?", color=PURPLE)
        self.play(FadeIn(title7), run_time=0.5)

        rows = VGroup(
            VGroup(
                Text("мм", font_size=32, color=BLUE, weight=BOLD),
                Text("→  молив, инсект, дебелина", font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("м", font_size=32, color=GREEN, weight=BOLD),
                Text("→  соба, висина на човек", font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("км", font_size=32, color=ORANGE, weight=BOLD),
                Text("→  растојание помеѓу градови", font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN)

        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title7, rows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 9.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")
        sum_title = section_title("Заклучок")
        self.play(FadeIn(sum_title), run_time=0.5)

        s1 = Text("Должина — метар.", font_size=34, color=BLUE)
        s2 = Text("Маса — грам.", font_size=34, color=GREEN)
        s3 = Text("Зафатнина — литар.", font_size=34, color=ORANGE)
        s4 = Text("Сите три  —  истиот ред.", font_size=34, color=PURPLE)
        end = Text("Десет. Сто. Илјада.",
                   font_size=40, color=YELLOW, weight=BOLD)

        VGroup(s1, s2, s3, s4, end).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for s in [s1, s2, s3, s4]:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.5)
            self.wait(0.15)
        self.play(Write(end), run_time=1.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sum_title, s1, s2, s3, s4, end)), run_time=0.8)
