"""
m8-1-2  —  Вредност, подредување и заокружување
Математика 8, Единица 1: Броеви

Teaching narrative — Andonovski-style: numbers as positions of power,
digits as actors with weight. Short punchy sentences, не...туку contrast.
Render:  manim -ql m8-1-2.py M812Scene
Output:  media/videos/m8-1-2/480p15/M812Scene.mp4
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


def place_column(label_text, digit_text, color=BLUE, width=1.3, height=2.2):
    col = RoundedRectangle(
        width=width, height=height, corner_radius=0.15,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    header = Text(label_text, font_size=20, color=color, weight=BOLD)
    header.move_to(col.get_top() + DOWN * 0.35)
    digit = Text(digit_text, font_size=56, color=WHITE2, weight=BOLD)
    digit.move_to(col.get_center() + DOWN * 0.2)
    return VGroup(col, header, digit)


class M812Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "Зошто 5 не е секогаш само пет?",
            font_size=44, color=YELLOW, weight=BOLD,
        )
        hook_q.to_edge(UP, buff=0.55)
        self.play(Write(hook_q), run_time=1.5)
        self.wait(0.7)

        answer = Text(
            "Зашто има место. Местото дава тежина.",
            font_size=34, color=WHITE2,
        )
        answer.next_to(hook_q, DOWN, buff=0.6)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(hook_q), FadeOut(answer), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  PLACE VALUE: 5,237                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("place_value_int")

        title2 = section_title("Вредност на цифрата")
        self.play(Write(title2), run_time=1.0)

        # 4 columns: thousands, hundreds, tens, ones
        cols_int = VGroup(
            place_column("илјади", "5", color=PURPLE),
            place_column("стотки", "2", color=BLUE),
            place_column("десетки", "3", color=GREEN),
            place_column("единици", "7", color=ORANGE),
        ).arrange(RIGHT, buff=0.25)
        cols_int.shift(DOWN * 0.2)

        self.play(*[FadeIn(c, shift=UP * 0.2) for c in cols_int], run_time=1.2)
        self.wait(0.6)

        # Show numeric decomposition
        decomp = MathTex(
            r"5237 = 5000 + 200 + 30 + 7",
            font_size=36, color=YELLOW,
        )
        decomp.to_edge(DOWN, buff=0.8)
        self.play(Write(decomp), run_time=1.3)
        self.wait(1.5)

        self.play(FadeOut(title2), FadeOut(cols_int), FadeOut(decomp), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  DECIMAL PLACE VALUE: 3,456                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("decimal_place")

        title3 = section_title("Децимални места")
        self.play(Write(title3), run_time=1.0)

        # 3 | , | 4 5 6
        whole = place_column("единици", "3", color=ORANGE)
        dot = Text(",", font_size=70, color=YELLOW, weight=BOLD)
        c1 = place_column("десетинки", "4", color=BLUE)
        c2 = place_column("стотинки", "5", color=GREEN)
        c3 = place_column("илјадинки", "6", color=PURPLE)

        dec_row = VGroup(whole, dot, c1, c2, c3).arrange(RIGHT, buff=0.2)
        dec_row.shift(DOWN * 0.1)
        self.play(*[FadeIn(c, shift=UP * 0.2) for c in [whole, dot, c1, c2, c3]],
                  run_time=1.2)
        self.wait(0.5)

        msg = callout("Десно од запирка — деловите. Лево — целините.",
                      border=YELLOW, font_size=28)
        msg.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(title3), FadeOut(dec_row), FadeOut(msg), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  × 10, ÷ 10 — DECIMAL POINT SLIDING               ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("times_ten")

        title4 = section_title("Помножи со 10, 100, 1000")
        self.play(Write(title4), run_time=1.0)

        n_start = MathTex("3{,}45", font_size=80, color=WHITE2)
        n_start.shift(UP * 0.5)
        self.play(Write(n_start), run_time=1.0)
        self.wait(0.5)

        arrow1 = Arrow(LEFT * 1.5, RIGHT * 1.5, color=YELLOW, buff=0).shift(DOWN * 0.6)
        lbl1 = Text("× 10", font_size=32, color=YELLOW).next_to(arrow1, UP, buff=0.1)
        self.play(GrowArrow(arrow1), Write(lbl1), run_time=0.6)

        n_mid = MathTex("34{,}5", font_size=80, color=GREEN)
        n_mid.shift(DOWN * 1.7)
        self.play(TransformFromCopy(n_start, n_mid), run_time=1.0)
        self.wait(0.6)

        rule_txt = Text("Запирката оди едно место надесно.", font_size=28, color=YELLOW)
        rule_txt.to_edge(DOWN, buff=0.6)
        self.play(Write(rule_txt), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(n_start), FadeOut(n_mid), FadeOut(arrow1),
                  FadeOut(lbl1), FadeOut(rule_txt), run_time=0.5)

        # ÷ 10
        n2 = MathTex("47{,}2", font_size=72, color=WHITE2)
        n2.shift(UP * 0.5)
        self.play(Write(n2), run_time=0.8)

        arr2 = Arrow(RIGHT * 1.5, LEFT * 1.5, color=ORANGE, buff=0).shift(DOWN * 0.6)
        lbl2 = Text("÷ 10", font_size=32, color=ORANGE).next_to(arr2, UP, buff=0.1)
        self.play(GrowArrow(arr2), Write(lbl2), run_time=0.6)

        n2_after = MathTex("4{,}72", font_size=72, color=GREEN)
        n2_after.shift(DOWN * 1.7)
        self.play(TransformFromCopy(n2, n2_after), run_time=1.0)
        self.wait(0.5)

        eq01 = MathTex(r"\times 0{,}1 = \div 10", font_size=40, color=PURPLE)
        eq01.to_edge(DOWN, buff=0.6)
        self.play(Write(eq01), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(title4), FadeOut(n2), FadeOut(n2_after),
            FadeOut(arr2), FadeOut(lbl2), FadeOut(eq01),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 5.  COMPARING DECIMALS                               ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        title5 = section_title("Споредување — место по место")
        self.play(Write(title5), run_time=1.0)

        compare1 = MathTex(r"3{,}2 \quad ? \quad 3{,}21", font_size=52, color=WHITE2)
        compare1.shift(UP * 1.2)
        self.play(Write(compare1), run_time=1.0)
        self.wait(0.5)

        align = MathTex(r"3{,}20 \quad < \quad 3{,}21", font_size=52, color=GREEN)
        align.shift(DOWN * 0.3)
        self.play(Write(align), run_time=1.2)
        self.wait(0.5)

        rule5 = callout("Изедначи ги местата. Потоа спореди цифра по цифра.",
                        border=YELLOW, font_size=26, width=10.0)
        rule5.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(rule5, shift=UP * 0.2), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(title5), FadeOut(compare1), FadeOut(align),
                  FadeOut(rule5), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ROUNDING                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rounding")

        title6 = section_title("Заокружување")
        self.play(Write(title6), run_time=1.0)

        rule6 = Text("Под 5 — надолу. 5 или повеќе — нагоре.",
                     font_size=30, color=WHITE2)
        rule6.next_to(title6, DOWN, buff=0.4)
        self.play(Write(rule6), run_time=1.2)
        self.wait(0.5)

        # Example 1: 3,75 → 3,8
        ex1 = MathTex(r"3{,}7\underline{5} \rightarrow 3{,}8",
                      font_size=48, color=GREEN)
        ex1.shift(UP * 0.2)
        self.play(Write(ex1), run_time=1.0)

        ex1_arrow = Text("одлучувачка цифра", font_size=22, color=YELLOW)
        ex1_arrow.next_to(ex1, DOWN, buff=0.4)
        arr1 = Arrow(ex1_arrow.get_top(), ex1.get_bottom() + LEFT * 0.5,
                     color=YELLOW, buff=0.05, stroke_width=3)
        self.play(GrowArrow(arr1), Write(ex1_arrow), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(ex1), FadeOut(ex1_arrow), FadeOut(arr1), run_time=0.4)

        # Example 2: 47,234 → 47,2 (one decimal)
        ex2 = MathTex(r"47{,}2\underline{3}4 \rightarrow 47{,}2",
                      font_size=48, color=GREEN)
        ex2.shift(UP * 0.2)
        self.play(Write(ex2), run_time=1.0)

        ex2_note = Text("Заокружено на една децимала", font_size=24, color=BLUE)
        ex2_note.next_to(ex2, DOWN, buff=0.5)
        self.play(Write(ex2_note), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title6), FadeOut(rule6), FadeOut(ex2),
                  FadeOut(ex2_note), run_time=0.5)

        # Example 3: 47.234 → 47.200 (to nearest hundred)
        title6b = section_title("Заокружување на стотка")
        self.play(Write(title6b), run_time=0.8)

        ex3 = MathTex(r"47\,\underline{2}34 \rightarrow 47\,200",
                      font_size=48, color=GREEN)
        ex3.shift(UP * 0.2)
        self.play(Write(ex3), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(title6b), FadeOut(ex3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 7.  ANDONOVSKI MOMENT                                ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        and_lines = [
            "Цифрата не е сама.",
            "Има позиција. Има тежина.",
            "Премести ja еден чекор —",
            "и сè се менува. Десет пати.",
        ]
        and_grp = VGroup(*[
            Text(line, font_size=34, color=YELLOW if i % 2 == 0 else WHITE2)
            for i, line in enumerate(and_lines)
        ]).arrange(DOWN, buff=0.35)
        and_grp.move_to(ORIGIN)

        for line in and_grp:
            self.play(Write(line), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(and_grp), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  REAL WORLD                                       ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("real_world")

        title8 = section_title("Каде живее ова", color=BLUE)
        self.play(Write(title8), run_time=0.8)

        items = [
            ("Цени во продавница: 1{,}99 ден.", ORANGE),
            ("Мерки во кујна: 0{,}5 л млеко", GREEN),
            ("Население: 2\\,083\\,000 жители", PURPLE),
        ]
        item_grp = VGroup()
        for txt, c in items:
            t = MathTex(txt, font_size=32, color=c)
            item_grp.add(t)
        item_grp.arrange(DOWN, buff=0.5)
        item_grp.next_to(title8, DOWN, buff=0.8)

        for it in item_grp:
            self.play(Write(it), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(title8), FadeOut(item_grp), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 9.  SUMMARY                                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title9 = section_title("Резиме", color=GREEN)
        self.play(Write(title9), run_time=1.0)

        bullets = [
            ("Местото на цифрата дава вредност", PURPLE),
            ("× 10 → запирка надесно. ÷ 10 → налево.", BLUE),
            ("× 0{,}1 = ÷ 10", ORANGE),
            ("Споредуваш цифра по цифра — почни лево", GREEN),
            ("Под 5 надолу, 5+ нагоре", YELLOW),
        ]
        rows = VGroup()
        for txt, c in bullets:
            dot = Dot(radius=0.12, color=c)
            label = Tex(txt, font_size=30, color=WHITE2)
            row = VGroup(dot, label).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(title9, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        outro = Text("Местото зборува. Слушај го.",
                     font_size=36, color=YELLOW, weight=BOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(Write(outro), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(title9), FadeOut(rows), FadeOut(outro), run_time=0.8)
        self.wait(0.3)
