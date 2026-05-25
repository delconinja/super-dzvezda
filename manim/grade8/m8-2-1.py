"""
m8-2-1  —  Изрази, равенки и формули
Математика 8, Единица 2: Алгебра

Teaching narrative — Andonovski-style: x is not unknown but a question,
letters as placeholders for life, balance scale as truth.
Render:  manim -ql m8-2-1.py M821Scene
Output:  media/videos/m8-2-1/480p15/M821Scene.mp4
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


def var_box(letter, color=BLUE, size=1.2):
    box = RoundedRectangle(
        width=size, height=size, corner_radius=0.18,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=3,
    )
    lbl = Text(letter, font_size=int(size * 50), color=color, weight=BOLD)
    lbl.move_to(box)
    return VGroup(box, lbl)


def balance_scale(left_label, right_label, left_color=BLUE, right_color=ORANGE):
    """Simple balance scale visualization."""
    base = Line(LEFT * 0.5, RIGHT * 0.5, color=GREY, stroke_width=4)
    base.shift(DOWN * 1.5)
    stand = Line(ORIGIN, UP * 1.0, color=GREY, stroke_width=4)
    stand.shift(DOWN * 1.5)
    beam = Line(LEFT * 2.5, RIGHT * 2.5, color=YELLOW, stroke_width=4)
    beam.shift(DOWN * 0.5)

    left_pan = Rectangle(width=1.8, height=0.2, color=left_color,
                         fill_color=left_color, fill_opacity=0.6, stroke_width=2)
    left_pan.shift(LEFT * 2.5 + DOWN * 0.7)
    right_pan = Rectangle(width=1.8, height=0.2, color=right_color,
                          fill_color=right_color, fill_opacity=0.6, stroke_width=2)
    right_pan.shift(RIGHT * 2.5 + DOWN * 0.7)

    left_txt = MathTex(left_label, font_size=44, color=WHITE2)
    left_txt.next_to(left_pan, UP, buff=0.2)
    right_txt = MathTex(right_label, font_size=44, color=WHITE2)
    right_txt.next_to(right_pan, UP, buff=0.2)

    return VGroup(base, stand, beam, left_pan, right_pan, left_txt, right_txt)


class M821Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "Што е x?",
            font_size=72, color=YELLOW, weight=BOLD,
        )
        hook_q.shift(UP * 0.3)
        self.play(Write(hook_q), run_time=1.0)
        self.wait(0.6)

        ans1 = Text("Не таен. Не непознат.", font_size=34, color=WHITE2)
        ans1.next_to(hook_q, DOWN, buff=0.7)
        ans2 = Text("Прашање — со одговор.", font_size=34, color=GREEN)
        ans2.next_to(ans1, DOWN, buff=0.3)

        self.play(Write(ans1), run_time=0.9)
        self.play(Write(ans2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(hook_q), FadeOut(ans1), FadeOut(ans2), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 2.  LETTERS AS PLACEHOLDERS                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("letters")

        title2 = section_title("Букви наместо броеви")
        self.play(Write(title2), run_time=1.0)

        boxes = VGroup(
            var_box("x", color=BLUE),
            var_box("y", color=GREEN),
            var_box("a", color=ORANGE),
            var_box("b", color=PURPLE),
        ).arrange(RIGHT, buff=0.5)
        boxes.shift(DOWN * 0.2)

        for b in boxes:
            self.play(GrowFromCenter(b), run_time=0.4)
        self.wait(0.5)

        sub_label = Text("Секоја буква чека број.", font_size=30, color=YELLOW)
        sub_label.to_edge(DOWN, buff=0.8)
        self.play(Write(sub_label), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(title2), FadeOut(boxes), FadeOut(sub_label), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 3.  VARIABLES vs CONSTANTS                           ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("var_const")

        title3 = section_title("Променливи и константи")
        self.play(Write(title3), run_time=0.9)

        var_lbl = Text("Променливи (се менуваат)", font_size=30, color=BLUE)
        var_lbl.shift(UP * 1.5 + LEFT * 3)
        var_ex = MathTex(r"x, \quad y, \quad t", font_size=48, color=BLUE)
        var_ex.shift(UP * 1.5 + RIGHT * 1.5)

        const_lbl = Text("Константи (фиксни)", font_size=30, color=ORANGE)
        const_lbl.shift(DOWN * 0.5 + LEFT * 3.3)
        const_ex = MathTex(r"\pi, \quad 3{,}14, \quad 7", font_size=48, color=ORANGE)
        const_ex.shift(DOWN * 0.5 + RIGHT * 1.5)

        self.play(Write(var_lbl), Write(var_ex), run_time=1.2)
        self.play(Write(const_lbl), Write(const_ex), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(title3), FadeOut(var_lbl), FadeOut(var_ex),
                  FadeOut(const_lbl), FadeOut(const_ex), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 4.  FORMULA vs FUNCTION                              ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("form_func")

        title4 = section_title("Формула наспроти функција")
        self.play(Write(title4), run_time=0.9)

        f_lbl = Text("Формула — правило за пресметка:", font_size=28, color=GREEN)
        f_lbl.shift(UP * 1.5)
        f_ex = MathTex(r"P = a + b + c + d", font_size=44, color=GREEN)
        f_ex.shift(UP * 0.7)

        func_lbl = Text("Функција — машина за број:", font_size=28, color=PURPLE)
        func_lbl.shift(DOWN * 0.3)
        func_ex = MathTex(r"f(x) = 2x + 3", font_size=44, color=PURPLE)
        func_ex.shift(DOWN * 1.1)

        self.play(Write(f_lbl), Write(f_ex), run_time=1.2)
        self.play(Write(func_lbl), Write(func_ex), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(title4), FadeOut(f_lbl), FadeOut(f_ex),
                  FadeOut(func_lbl), FadeOut(func_ex), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 5.  LIKE TERMS                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("like_terms")

        title5 = section_title("Слични членови")
        self.play(Write(title5), run_time=0.9)

        like1 = MathTex(r"3x", font_size=56, color=BLUE)
        like1.shift(UP * 1.3 + LEFT * 2.5)
        like2 = MathTex(r"5x", font_size=56, color=BLUE)
        like2.shift(UP * 1.3 + RIGHT * 2.5)
        like_lbl = Text("слични", font_size=28, color=GREEN, weight=BOLD)
        like_lbl.shift(UP * 1.3)

        self.play(Write(like1), Write(like2), Write(like_lbl), run_time=1.0)
        self.wait(0.5)

        unlike1 = MathTex(r"3x", font_size=56, color=BLUE)
        unlike1.shift(DOWN * 0.2 + LEFT * 2.5)
        unlike2 = MathTex(r"2y", font_size=56, color=ORANGE)
        unlike2.shift(DOWN * 0.2 + RIGHT * 2.5)
        unlike_lbl = Text("различни", font_size=28, color=RED, weight=BOLD)
        unlike_lbl.shift(DOWN * 0.2)

        self.play(Write(unlike1), Write(unlike2), Write(unlike_lbl), run_time=1.0)
        self.wait(0.5)

        simp_lbl = Text("Само сличните се собираат:", font_size=28, color=YELLOW)
        simp_lbl.shift(DOWN * 1.5 + LEFT * 2.5)
        simp_eq = MathTex(r"3x + 5x = 8x", font_size=42, color=GREEN)
        simp_eq.shift(DOWN * 1.5 + RIGHT * 2.2)

        self.play(Write(simp_lbl), Write(simp_eq), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(title5), FadeOut(like1), FadeOut(like2), FadeOut(like_lbl),
                  FadeOut(unlike1), FadeOut(unlike2), FadeOut(unlike_lbl),
                  FadeOut(simp_lbl), FadeOut(simp_eq), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 6.  DISTRIBUTIVE — 3(x+2) = 3x+6                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("distributive")

        title6 = section_title("Распоредување")
        self.play(Write(title6), run_time=0.8)

        d1 = MathTex(r"3(x + 2)", font_size=64, color=WHITE2)
        d1.shift(UP * 1.0)
        self.play(Write(d1), run_time=0.9)
        self.wait(0.3)

        d2 = MathTex(r"= 3 \cdot x + 3 \cdot 2", font_size=58, color=YELLOW)
        d2.shift(DOWN * 0.1)
        self.play(Write(d2), run_time=1.1)
        self.wait(0.3)

        d3 = MathTex(r"= 3x + 6", font_size=64, color=GREEN, weight=BOLD)
        d3.shift(DOWN * 1.3)
        self.play(Write(d3), run_time=0.9)
        self.wait(1.8)

        self.play(FadeOut(title6), FadeOut(d1), FadeOut(d2), FadeOut(d3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 7.  SUBSTITUTION                                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("substitution")

        title7 = section_title("Замена на бројот")
        self.play(Write(title7), run_time=0.9)

        intro = MathTex(r"\text{Ако } x = 3, \; y = 5",
                        font_size=40, color=BLUE)
        intro.shift(UP * 1.7)
        self.play(Write(intro), run_time=1.0)

        ex_a = MathTex(r"2x + y = 2 \cdot 3 + 5 = 11",
                       font_size=42, color=GREEN)
        ex_a.shift(UP * 0.3)
        ex_b = MathTex(r"x^2 + 2y = 9 + 10 = 19",
                       font_size=42, color=ORANGE)
        ex_b.shift(DOWN * 1.0)

        self.play(Write(ex_a), run_time=1.2)
        self.play(Write(ex_b), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(title7), FadeOut(intro),
                  FadeOut(ex_a), FadeOut(ex_b), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 8.  EQUATION SOLVING — BALANCE SCALE                 ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("balance")

        title8 = section_title("Равенката е терезија")
        self.play(Write(title8), run_time=0.9)

        scale = balance_scale("x + 5", "12", left_color=BLUE, right_color=ORANGE)
        scale.shift(DOWN * 0.2)
        self.play(Create(scale), run_time=1.5)
        self.wait(0.5)

        eq_msg = Text("Одземи 5 од обете страни:", font_size=26, color=YELLOW)
        eq_msg.to_edge(DOWN, buff=0.6)
        self.play(Write(eq_msg), run_time=0.8)
        self.wait(0.5)

        # Transform scale
        scale2 = balance_scale("x", "7", left_color=BLUE, right_color=GREEN)
        scale2.shift(DOWN * 0.2)
        self.play(Transform(scale, scale2), run_time=1.2)
        self.wait(0.5)

        answer_8 = MathTex(r"x = 7", font_size=56, color=GREEN, weight=BOLD)
        answer_8.to_edge(DOWN, buff=0.6)
        self.play(FadeOut(eq_msg), Write(answer_8), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(title8), FadeOut(scale), FadeOut(answer_8), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 9.  SOLVE 2(x+3)=14 — STEP BY STEP                   ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("solve_steps")

        title9 = section_title("Реши: 2(x+3) = 14")
        self.play(Write(title9), run_time=0.9)

        sv1 = MathTex(r"2(x + 3) = 14", font_size=44, color=WHITE2)
        sv1.shift(UP * 1.7)
        sv2 = MathTex(r"2x + 6 = 14", font_size=44, color=YELLOW)
        sv2.shift(UP * 0.7)
        sv3 = MathTex(r"2x = 8", font_size=44, color=BLUE)
        sv3.shift(DOWN * 0.3)
        sv4 = MathTex(r"x = 4", font_size=54, color=GREEN, weight=BOLD)
        sv4.shift(DOWN * 1.5)

        notes_solve = [
            ("распоредување", YELLOW, sv2),
            ("одземи 6 обете", BLUE, sv3),
            ("подели со 2", GREEN, sv4),
        ]

        self.play(Write(sv1), run_time=0.8)
        for line, (note_txt, c, target) in zip([sv2, sv3, sv4], notes_solve):
            note = Text(note_txt, font_size=22, color=c)
            note.next_to(target, RIGHT, buff=0.6)
            self.play(Write(line), Write(note), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(title9), FadeOut(sv1), FadeOut(sv2),
                  FadeOut(sv3), FadeOut(sv4),
                  *[FadeOut(m) for m in self.mobjects if isinstance(m, Text)],
                  run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 10. VARIABLES ON BOTH SIDES — 3x+2 = x+10            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("both_sides")

        title10 = section_title("Букви на двете страни")
        self.play(Write(title10), run_time=0.9)

        b1 = MathTex(r"3x + 2 = x + 10", font_size=46, color=WHITE2)
        b1.shift(UP * 1.5)
        b2 = MathTex(r"2x = 8", font_size=46, color=YELLOW)
        b2.shift(UP * 0.2)
        b3 = MathTex(r"x = 4", font_size=54, color=GREEN, weight=BOLD)
        b3.shift(DOWN * 1.0)

        self.play(Write(b1), run_time=0.9)
        self.play(Write(b2), run_time=1.0)
        self.play(Write(b3), run_time=0.9)
        self.wait(1.8)

        self.play(FadeOut(title10), FadeOut(b1), FadeOut(b2), FadeOut(b3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 11. REAL EXAMPLE — TEMPERATURE                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("real")

        title11 = section_title("Жива примена", color=BLUE)
        self.play(Write(title11), run_time=0.8)

        temp_formula = MathTex(
            r"^\circ C = (^\circ F - 32) \times \frac{5}{9}",
            font_size=48, color=ORANGE,
        )
        temp_formula.shift(UP * 0.6)
        self.play(Write(temp_formula), run_time=1.5)
        self.wait(0.4)

        example = MathTex(
            r"^\circ F = 50 \;\Rightarrow\; ^\circ C = 18 \times \tfrac{5}{9} = 10",
            font_size=36, color=GREEN,
        )
        example.shift(DOWN * 0.7)
        self.play(Write(example), run_time=1.5)
        self.wait(2.0)

        self.play(FadeOut(title11), FadeOut(temp_formula), FadeOut(example), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 12. ANDONOVSKI MOMENT                                ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        and_lines = [
            "x не е таен.",
            "x е прашање.",
            "Решавањето е одговор.",
            "Тоа е сè.",
        ]
        and_grp = VGroup(*[
            Text(line, font_size=40, color=YELLOW if i in (1, 3) else WHITE2,
                 weight=BOLD if i == 3 else NORMAL)
            for i, line in enumerate(and_lines)
        ]).arrange(DOWN, buff=0.35)
        and_grp.move_to(ORIGIN)

        for line in and_grp:
            self.play(Write(line), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(and_grp), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 13. SUMMARY                                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title13 = section_title("Резиме", color=GREEN)
        self.play(Write(title13), run_time=1.0)

        bullets = [
            ("Буквите чекаат броеви", BLUE),
            ("Слични членови се собираат", GREEN),
            ("3(x+2) = 3x + 6 — распоредување", ORANGE),
            ("Замена: ставаш број, добиваш резултат", PURPLE),
            ("Равенка = терезија. Чувај ја рамнотежата.", YELLOW),
        ]
        rows = VGroup()
        for txt, c in bullets:
            dot = Dot(radius=0.12, color=c)
            label = Text(txt, font_size=26, color=WHITE2)
            row = VGroup(dot, label).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(title13, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        outro = Text("Алгебрата не плаши. Алгебрата ослободува.",
                     font_size=34, color=YELLOW, weight=BOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(Write(outro), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(title13), FadeOut(rows), FadeOut(outro), run_time=0.8)
        self.wait(0.3)
