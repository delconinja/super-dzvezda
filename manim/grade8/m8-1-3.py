"""
m8-1-3  —  Дропки, децимални броеви, проценти, размери и пропорции
Математика 8, Единица 1: Броеви

Teaching narrative — Andonovski-style: fractions as half-stories,
percentages as portions of the whole, ratios as splits of fate.
Render:  manim -ql m8-1-3.py M813Scene
Output:  media/videos/m8-1-3/480p15/M813Scene.mp4
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


def pie_slice(start_angle, end_angle, radius=1.5, color=BLUE, fill_opacity=0.8):
    return Sector(
        outer_radius=radius,
        angle=end_angle - start_angle,
        start_angle=start_angle,
        fill_color=color, fill_opacity=fill_opacity,
        stroke_color=WHITE, stroke_width=2,
    )


class M813Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "Што е дропка? Скршен број?",
            font_size=44, color=YELLOW, weight=BOLD,
        )
        hook_q.to_edge(UP, buff=0.55)
        self.play(Write(hook_q), run_time=1.2)
        self.wait(0.6)

        answer = Text(
            "Не. Половина приказна.",
            font_size=36, color=WHITE2,
        )
        answer.next_to(hook_q, DOWN, buff=0.6)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(hook_q), FadeOut(answer), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  WHAT IS A FRACTION                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("def")

        title2 = section_title("Дропка")
        self.play(Write(title2), run_time=1.0)

        frac = MathTex(r"\frac{a}{b}", font_size=120, color=WHITE2)
        frac.shift(LEFT * 3.5)
        self.play(Write(frac), run_time=1.0)

        # Labels
        num_lbl = Text("броител", font_size=28, color=BLUE)
        num_lbl.next_to(frac, RIGHT, buff=1.5).shift(UP * 1.0)
        num_arr = Arrow(num_lbl.get_left(), frac.get_top() + RIGHT * 0.3,
                        color=BLUE, buff=0.1, stroke_width=3)
        denom_lbl = Text("именител", font_size=28, color=ORANGE)
        denom_lbl.next_to(frac, RIGHT, buff=1.5).shift(DOWN * 1.0)
        denom_arr = Arrow(denom_lbl.get_left(), frac.get_bottom() + RIGHT * 0.3,
                          color=ORANGE, buff=0.1, stroke_width=3)

        self.play(Write(num_lbl), GrowArrow(num_arr), run_time=0.8)
        self.play(Write(denom_lbl), GrowArrow(denom_arr), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title2), FadeOut(frac), FadeOut(num_lbl),
                  FadeOut(num_arr), FadeOut(denom_lbl), FadeOut(denom_arr),
                  run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 3.  TYPES: proper, improper, mixed                   ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("types")

        title3 = section_title("Видови дропки")
        self.play(Write(title3), run_time=0.8)

        proper = VGroup(
            MathTex(r"\frac{1}{2}", font_size=60, color=GREEN),
            Text("права", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        improper = VGroup(
            MathTex(r"\frac{5}{4}", font_size=60, color=ORANGE),
            Text("неправа", font_size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.3)
        mixed = VGroup(
            MathTex(r"1\frac{1}{2}", font_size=60, color=PURPLE),
            Text("мешана", font_size=24, color=PURPLE),
        ).arrange(DOWN, buff=0.3)

        types_grp = VGroup(proper, improper, mixed).arrange(RIGHT, buff=1.8)
        types_grp.shift(DOWN * 0.3)

        for grp in types_grp:
            self.play(FadeIn(grp, shift=UP * 0.3), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(title3), FadeOut(types_grp), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 4.  CONVERSIONS — fraction ↔ decimal ↔ percent       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conversions")

        title4 = section_title("Три облика — една вредност")
        self.play(Write(title4), run_time=0.9)

        rows_conv = [
            (r"\frac{1}{2}", "0{,}5", "50\\%", GREEN),
            (r"\frac{1}{4}", "0{,}25", "25\\%", BLUE),
            (r"\frac{3}{4}", "0{,}75", "75\\%", ORANGE),
        ]
        conv_grp = VGroup()
        for f, d, p, c in rows_conv:
            row = VGroup(
                MathTex(f, font_size=44, color=c),
                MathTex(r"=", font_size=40, color=WHITE2),
                MathTex(d, font_size=40, color=c),
                MathTex(r"=", font_size=40, color=WHITE2),
                MathTex(p, font_size=40, color=c),
            ).arrange(RIGHT, buff=0.5)
            conv_grp.add(row)
        conv_grp.arrange(DOWN, buff=0.5)
        conv_grp.shift(DOWN * 0.2)

        for row in conv_grp:
            self.play(Write(row), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(title4), FadeOut(conv_grp), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 5.  PIE CHART 3/4                                    ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pie")

        title5 = section_title("Три четвртини — слика")
        self.play(Write(title5), run_time=0.9)

        # Build full pie split into 4
        pie = VGroup()
        for i in range(4):
            color = GREEN if i < 3 else GREY
            opacity = 0.9 if i < 3 else 0.3
            s = pie_slice(
                start_angle=i * PI / 2,
                end_angle=(i + 1) * PI / 2,
                radius=1.8,
                color=color,
                fill_opacity=opacity,
            )
            pie.add(s)
        pie.shift(LEFT * 3 + DOWN * 0.3)

        for s in pie:
            self.play(FadeIn(s), run_time=0.3)
        self.wait(0.4)

        eq_label = MathTex(r"\frac{3}{4} = 0{,}75 = 75\%",
                           font_size=46, color=GREEN)
        eq_label.shift(RIGHT * 2.8)
        self.play(Write(eq_label), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(title5), FadeOut(pie), FadeOut(eq_label), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 6.  SIMPLIFYING — 6/8 = 3/4                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("simplify")

        title6 = section_title("Скратување")
        self.play(Write(title6), run_time=0.8)

        before = MathTex(r"\frac{6}{8}", font_size=80, color=WHITE2)
        before.shift(LEFT * 3)

        step = MathTex(r"\div 2", font_size=36, color=YELLOW)
        step.next_to(before, RIGHT, buff=0.8).shift(UP * 0.3)
        step2 = MathTex(r"\div 2", font_size=36, color=YELLOW)
        step2.next_to(before, RIGHT, buff=0.8).shift(DOWN * 0.3)

        arrow_s = Arrow(LEFT * 1.5, RIGHT * 1.5, color=YELLOW, buff=0)
        arrow_s.shift(RIGHT * 0.3)

        after = MathTex(r"\frac{3}{4}", font_size=80, color=GREEN)
        after.shift(RIGHT * 3)

        self.play(Write(before), run_time=0.8)
        self.play(GrowArrow(arrow_s), Write(step), Write(step2), run_time=0.8)
        self.play(Write(after), run_time=0.8)
        self.wait(0.5)

        simp_rule = callout("Подели горе и долу со ист број. Дропката останува иста.",
                            border=YELLOW, font_size=26, width=10.5)
        simp_rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(simp_rule, shift=UP * 0.2), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(title6), FadeOut(before), FadeOut(arrow_s),
                  FadeOut(step), FadeOut(step2),
                  FadeOut(after), FadeOut(simp_rule), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 7.  ADDITION WITH COMMON DENOMINATOR                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("add")

        title7 = section_title("Собирање — заеднички именител")
        self.play(Write(title7), run_time=0.8)

        step1 = MathTex(r"\frac{1}{2} + \frac{1}{3}", font_size=56, color=WHITE2)
        step1.shift(UP * 1.3)
        self.play(Write(step1), run_time=0.8)
        self.wait(0.4)

        step2 = MathTex(r"= \frac{3}{6} + \frac{2}{6}", font_size=56, color=YELLOW)
        step2.next_to(step1, DOWN, buff=0.4)
        self.play(Write(step2), run_time=1.0)
        self.wait(0.4)

        step3 = MathTex(r"= \frac{5}{6}", font_size=56, color=GREEN)
        step3.next_to(step2, DOWN, buff=0.4)
        self.play(Write(step3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title7), FadeOut(step1), FadeOut(step2),
                  FadeOut(step3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 8.  MULTIPLICATION & DIVISION                        ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mul_div")

        title8 = section_title("Множење и делење")
        self.play(Write(title8), run_time=0.8)

        mul_lbl = Text("Множи право:", font_size=28, color=BLUE)
        mul_lbl.shift(UP * 1.5 + LEFT * 4)
        mul_eq = MathTex(r"\frac{2}{3} \times \frac{3}{4} = \frac{6}{12} = \frac{1}{2}",
                         font_size=46, color=WHITE2)
        mul_eq.shift(UP * 1.5 + RIGHT * 0.5)
        self.play(Write(mul_lbl), Write(mul_eq), run_time=1.2)
        self.wait(0.5)

        div_lbl = Text("Преврти и помножи:", font_size=28, color=ORANGE)
        div_lbl.shift(DOWN * 0.3 + LEFT * 4)
        div_eq = MathTex(r"\frac{1}{2} \div \frac{1}{4} = \frac{1}{2} \times \frac{4}{1} = 2",
                         font_size=42, color=WHITE2)
        div_eq.shift(DOWN * 0.3 + RIGHT * 0.6)
        self.play(Write(div_lbl), Write(div_eq), run_time=1.2)
        self.wait(1.0)

        div_msg = callout("Делењето сечи. Множењето собира.",
                          border=YELLOW, font_size=28)
        div_msg.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(div_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(title8), FadeOut(mul_lbl), FadeOut(mul_eq),
                  FadeOut(div_lbl), FadeOut(div_eq), FadeOut(div_msg), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 9.  PERCENTAGES                                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("percent")

        title9 = section_title("Проценти")
        self.play(Write(title9), run_time=0.8)

        # Percentage bar
        bar_bg = Rectangle(width=8, height=0.7, color=GREY,
                           fill_color=DARK_CARD, fill_opacity=1, stroke_width=2)
        bar_bg.shift(UP * 1.0)
        bar_fill = Rectangle(width=8 * 0.25, height=0.7, color=GREEN,
                             fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        bar_fill.move_to(bar_bg.get_left(), aligned_edge=LEFT)
        bar_lbl = Text("25% од 80 = 20", font_size=32, color=GREEN)
        bar_lbl.next_to(bar_bg, UP, buff=0.3)

        self.play(Create(bar_bg), run_time=0.8)
        self.play(FadeIn(bar_fill, shift=RIGHT * 0.2), Write(bar_lbl), run_time=0.9)
        self.wait(0.5)

        up_eq = MathTex(r"+20\% \quad \rightarrow \quad \times 1{,}2",
                        font_size=40, color=GREEN)
        up_eq.shift(DOWN * 0.4)
        down_eq = MathTex(r"-30\% \quad \rightarrow \quad \times 0{,}7",
                          font_size=40, color=RED)
        down_eq.shift(DOWN * 1.3)

        self.play(Write(up_eq), run_time=0.9)
        self.play(Write(down_eq), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(title9), FadeOut(bar_bg), FadeOut(bar_fill),
                  FadeOut(bar_lbl), FadeOut(up_eq), FadeOut(down_eq), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 10. RATIOS AND PROPORTIONS                           ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ratios")

        title10 = section_title("Размери и пропорции")
        self.play(Write(title10), run_time=0.8)

        ratio = MathTex(r"6 : 8 = 3 : 4", font_size=48, color=WHITE2)
        ratio.shift(UP * 1.6)
        self.play(Write(ratio), run_time=1.0)
        self.wait(0.4)

        # Split bar 60 in 2:3
        split_lbl = Text("Подели 60 во однос 2 : 3", font_size=28, color=BLUE)
        split_lbl.shift(UP * 0.4)
        self.play(Write(split_lbl), run_time=0.8)

        bar2 = Rectangle(width=8, height=0.7, color=GREY,
                         fill_color=DARK_CARD, fill_opacity=1, stroke_width=2)
        bar2.shift(DOWN * 0.4)
        left_part = Rectangle(width=8 * 0.4, height=0.7, color=BLUE,
                              fill_color=BLUE, fill_opacity=0.85, stroke_width=0)
        left_part.move_to(bar2.get_left(), aligned_edge=LEFT)
        right_part = Rectangle(width=8 * 0.6, height=0.7, color=ORANGE,
                               fill_color=ORANGE, fill_opacity=0.85, stroke_width=0)
        right_part.move_to(bar2.get_right(), aligned_edge=RIGHT)

        l_lbl = MathTex("24", font_size=32, color=BLUE).next_to(left_part, DOWN, buff=0.2)
        r_lbl = MathTex("36", font_size=32, color=ORANGE).next_to(right_part, DOWN, buff=0.2)

        self.play(Create(bar2), run_time=0.6)
        self.play(FadeIn(left_part, shift=RIGHT * 0.2),
                  FadeIn(right_part, shift=LEFT * 0.2),
                  Write(l_lbl), Write(r_lbl), run_time=1.0)
        self.wait(0.5)

        prop = MathTex(r"3 : 5 = x : 20 \quad\Rightarrow\quad x = 12",
                       font_size=38, color=PURPLE)
        prop.to_edge(DOWN, buff=0.6)
        self.play(Write(prop), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(title10), FadeOut(ratio), FadeOut(split_lbl),
                  FadeOut(bar2), FadeOut(left_part), FadeOut(right_part),
                  FadeOut(l_lbl), FadeOut(r_lbl), FadeOut(prop), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 11. ANDONOVSKI MOMENT                                ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        and_lines = [
            "Дропка не е скршен број.",
            "Дропка е цел број на патот",
            "кон друг цел број.",
            "Само половина приказна.",
        ]
        and_grp = VGroup(*[
            Text(line, font_size=34,
                 color=YELLOW if i in (0, 3) else WHITE2,
                 weight=BOLD if i == 3 else NORMAL)
            for i, line in enumerate(and_lines)
        ]).arrange(DOWN, buff=0.35)
        and_grp.move_to(ORIGIN)

        for line in and_grp:
            self.play(Write(line), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(and_grp), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 12. SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title12 = section_title("Резиме", color=GREEN)
        self.play(Write(title12), run_time=1.0)

        bullets = [
            ("Дропка = броител / именител", BLUE),
            (r"\frac{1}{2} = 0{,}5 = 50\%", GREEN),
            ("Скрати со ист делител горе и долу", ORANGE),
            ("Множи право, дели — преврти", PURPLE),
            ("Однос 2:3 значи две дела према три", YELLOW),
        ]
        rows = VGroup()
        for txt, c in bullets:
            dot = Dot(radius=0.12, color=c)
            label = Tex(txt, font_size=28, color=WHITE2)
            row = VGroup(dot, label).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(title12, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        outro = Text("Половина денес. Цело утре.",
                     font_size=36, color=YELLOW, weight=BOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(Write(outro), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(title12), FadeOut(rows), FadeOut(outro), run_time=0.8)
        self.wait(0.3)
