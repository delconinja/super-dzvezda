"""
m8-1-4  —  Математички операции
Математика 8, Единица 1: Броеви

Teaching narrative — Andonovski-style: order as law, operations as
verbs of life. Short punchy sentences, не...туку contrast.
Render:  manim -ql m8-1-4.py M814Scene
Output:  media/videos/m8-1-4/480p15/M814Scene.mp4
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


def order_step(rank, name, sample, color):
    box = RoundedRectangle(
        width=8.5, height=0.95, corner_radius=0.15,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    rank_lbl = Text(str(rank), font_size=42, color=color, weight=BOLD)
    rank_lbl.move_to(box.get_left() + RIGHT * 0.5)
    name_lbl = Text(name, font_size=28, color=WHITE2)
    name_lbl.move_to(box.get_center() + LEFT * 1.6)
    sample_lbl = Text(sample, font_size=28, color=color)
    sample_lbl.move_to(box.get_right() + LEFT * 1.5)
    return VGroup(box, rank_lbl, name_lbl, sample_lbl)


class M814Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "3 + 2 × 4 = ?",
            font_size=64, color=YELLOW, weight=BOLD,
        )
        hook_q.shift(UP * 0.3)
        self.play(Write(hook_q), run_time=1.2)
        self.wait(0.6)

        wrong = Text("20?  Не!", font_size=44, color=RED, weight=BOLD)
        wrong.next_to(hook_q, DOWN, buff=0.7)
        self.play(Write(wrong), run_time=0.8)
        self.wait(1.0)

        right = Text("Одговорот е 11. Зошто?", font_size=36, color=GREEN)
        right.next_to(wrong, DOWN, buff=0.4)
        self.play(Write(right), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(hook_q), FadeOut(wrong), FadeOut(right), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ORDER OF OPERATIONS — CASCADE                    ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pemdas")

        title2 = section_title("Редот на операциите")
        self.play(Write(title2), run_time=1.0)

        steps = [
            order_step(1, "Загради", "( )", YELLOW),
            order_step(2, "Степени", "^", PURPLE),
            order_step(3, "Множење / делење", "× ÷", BLUE),
            order_step(4, "Собирање / одземање", "+ −", GREEN),
        ]
        cascade = VGroup(*steps).arrange(DOWN, buff=0.25)
        cascade.shift(DOWN * 0.2)

        for s in steps:
            self.play(FadeIn(s, shift=LEFT * 0.3), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(title2), FadeOut(cascade), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 3.  WORKED EXAMPLE — 3 + 2 × 4                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ex1")

        title3 = section_title("Пример 1")
        self.play(Write(title3), run_time=0.8)

        line1 = MathTex(r"3 + 2 \times 4", font_size=58, color=WHITE2)
        line1.shift(UP * 1.5)
        self.play(Write(line1), run_time=0.8)
        self.wait(0.4)

        line2 = MathTex(r"= 3 + 8", font_size=58, color=BLUE)
        line2.shift(UP * 0.3)
        note1 = Text("прво множењето", font_size=24, color=BLUE)
        note1.next_to(line2, RIGHT, buff=0.6)
        self.play(Write(line2), Write(note1), run_time=1.0)
        self.wait(0.4)

        line3 = MathTex(r"= 11", font_size=64, color=GREEN, weight=BOLD)
        line3.shift(DOWN * 1.0)
        self.play(Write(line3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title3), FadeOut(line1), FadeOut(line2),
                  FadeOut(note1), FadeOut(line3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE WITH BRACKETS                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ex2")

        title4 = section_title("Со загради — друг свет")
        self.play(Write(title4), run_time=0.8)

        l1 = MathTex(r"(3 + 2) \times 4", font_size=58, color=WHITE2)
        l1.shift(UP * 1.2)
        l2 = MathTex(r"= 5 \times 4", font_size=58, color=YELLOW)
        l2.shift(UP * 0.0)
        l3 = MathTex(r"= 20", font_size=64, color=GREEN, weight=BOLD)
        l3.shift(DOWN * 1.2)

        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=0.9)
        self.play(Write(l3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title4), FadeOut(l1), FadeOut(l2), FadeOut(l3), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 5.  EXAMPLE WITH POWER — 2 + 3² × 2                  ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ex3")

        title5 = section_title("Со степен")
        self.play(Write(title5), run_time=0.8)

        s1 = MathTex(r"2 + 3^2 \times 2", font_size=56, color=WHITE2)
        s1.shift(UP * 1.5)
        s2 = MathTex(r"= 2 + 9 \times 2", font_size=56, color=PURPLE)
        s2.shift(UP * 0.4)
        s3 = MathTex(r"= 2 + 18", font_size=56, color=BLUE)
        s3.shift(DOWN * 0.7)
        s4 = MathTex(r"= 20", font_size=62, color=GREEN, weight=BOLD)
        s4.shift(DOWN * 1.9)

        notes = [
            ("прво степенот", PURPLE, s2),
            ("потоа множењето", BLUE, s3),
            ("на крај собирање", GREEN, s4),
        ]

        self.play(Write(s1), run_time=0.7)
        for line, (note_txt, c, target) in zip([s2, s3, s4], notes):
            note = Text(note_txt, font_size=22, color=c)
            note.next_to(target, RIGHT, buff=0.5)
            self.play(Write(line), Write(note), run_time=0.8)
        self.wait(1.5)

        # Andonovski moment
        self.play(FadeOut(title5), FadeOut(s1), FadeOut(s2), FadeOut(s3),
                  FadeOut(s4), *[FadeOut(m) for m in self.mobjects if isinstance(m, Text)],
                  run_time=0.5)

        and_lines = [
            "Прво заградите.",
            "Потоа степените.",
            "Потоа множењето.",
            "Потоа собирањето.",
            "Редот не е препорака. Редот е закон.",
        ]
        colors_and = [YELLOW, PURPLE, BLUE, GREEN, YELLOW]
        and_grp = VGroup(*[
            Text(line, font_size=32, color=c,
                 weight=BOLD if i == 4 else NORMAL)
            for i, (line, c) in enumerate(zip(and_lines, colors_and))
        ]).arrange(DOWN, buff=0.3)
        and_grp.move_to(ORIGIN)

        for line in and_grp:
            self.play(Write(line), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(and_grp), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 6.  MENTAL MATH TRICKS                               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mental")

        title6 = section_title("Трикови во главата", color=ORANGE)
        self.play(Write(title6), run_time=0.9)

        # Card 1 — halving
        card1 = RoundedRectangle(
            width=10, height=1.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        )
        card1.shift(UP * 1.5)
        c1_lbl = MathTex(r"50\%\text{ од }80 = 40 \quad 25\% = 20 \quad 12{,}5\% = 10",
                         font_size=32, color=BLUE)
        c1_lbl.move_to(card1)

        # Card 2 — distributive
        card2 = RoundedRectangle(
            width=10, height=1.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        )
        card2.shift(UP * 0.2)
        c2_lbl = MathTex(r"102 \times 5 = (100\times 5) + (2\times 5) = 510",
                         font_size=30, color=GREEN)
        c2_lbl.move_to(card2)

        # Card 3 — known facts
        card3 = RoundedRectangle(
            width=10, height=1.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        )
        card3.shift(DOWN * 1.1)
        c3_lbl = MathTex(r"20\times 38=760 \Rightarrow 21\times 38=798",
                         font_size=32, color=ORANGE)
        c3_lbl.move_to(card3)

        for box, lbl in [(card1, c1_lbl), (card2, c2_lbl), (card3, c3_lbl)]:
            self.play(Create(box), Write(lbl), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(title6),
                  FadeOut(card1), FadeOut(c1_lbl),
                  FadeOut(card2), FadeOut(c2_lbl),
                  FadeOut(card3), FadeOut(c3_lbl),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  POWERS OF 2 — STAIRCASE                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pow2")

        title7 = section_title("Степени на 2 — скала")
        self.play(Write(title7), run_time=0.8)

        pows = [(2, 4), (3, 8), (4, 16), (5, 32), (10, 1024)]
        stair = VGroup()
        x_start = -5.5
        for i, (exp, val) in enumerate(pows):
            h = 0.4 + i * 0.35
            block = Rectangle(
                width=1.6, height=h,
                fill_color=BLUE, fill_opacity=0.4 + i * 0.1,
                stroke_color=BLUE, stroke_width=2,
            )
            block.move_to(np.array([x_start + i * 1.9, -2 + h / 2, 0]))

            lbl = MathTex(rf"2^{{{exp}}}={val}", font_size=24, color=WHITE2)
            lbl.next_to(block, UP, buff=0.15)
            stair.add(VGroup(block, lbl))

        for s in stair:
            self.play(GrowFromEdge(s[0], DOWN), Write(s[1]), run_time=0.5)
        self.wait(1.5)

        cubes_lbl = Text("Кубови: 1, 8, 27, 64, 125", font_size=30, color=PURPLE)
        cubes_lbl.to_edge(DOWN, buff=0.4)
        self.play(Write(cubes_lbl), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(title7), FadeOut(stair), FadeOut(cubes_lbl), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 8.  DECIMAL DIVISION TRICK                           ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("div_trick")

        title8 = section_title("Делење со децимала — трик")
        self.play(Write(title8), run_time=0.8)

        d1 = MathTex(r"4{,}8 \div 0{,}6", font_size=52, color=WHITE2)
        d1.shift(UP * 1.5)
        self.play(Write(d1), run_time=0.8)

        arr = Arrow(UP * 0.5, DOWN * 0.5, color=YELLOW, buff=0)
        arr.shift(UP * 0.7)
        mul_note = Text("× 10 и горе и долу", font_size=26, color=YELLOW)
        mul_note.next_to(arr, RIGHT, buff=0.4)
        self.play(GrowArrow(arr), Write(mul_note), run_time=0.8)

        d2 = MathTex(r"48 \div 6 = 8", font_size=56, color=GREEN, weight=BOLD)
        d2.shift(DOWN * 0.5)
        self.play(Write(d2), run_time=1.0)
        self.wait(1.0)

        d_msg = callout("× помал од 1 — резултатот станува помал.",
                        border=BLUE, font_size=28)
        d_msg.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(d_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title8), FadeOut(d1), FadeOut(d2), FadeOut(arr),
                  FadeOut(mul_note), FadeOut(d_msg), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 9.  INVERSE CHECK                                    ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("inverse")

        title9 = section_title("Проверка со обратната операција")
        self.play(Write(title9), run_time=0.9)

        check1 = MathTex(r"24 + 38 = 62", font_size=46, color=WHITE2)
        check1.shift(UP * 0.7)
        check2 = MathTex(r"62 - 38 = 24 \checkmark", font_size=46, color=GREEN)
        check2.shift(DOWN * 0.5)

        self.play(Write(check1), run_time=0.8)
        self.play(Write(check2), run_time=1.0)
        self.wait(1.0)

        inv_msg = callout("Собирање и одземање — еден предмет, две страни.",
                          border=YELLOW, font_size=26, width=10.5)
        inv_msg.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(inv_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(title9), FadeOut(check1), FadeOut(check2),
                  FadeOut(inv_msg), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 10. SUMMARY                                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title10 = section_title("Резиме", color=GREEN)
        self.play(Write(title10), run_time=1.0)

        bullets = [
            ("Загради → степени → ×÷ → +−", YELLOW),
            ("102×5 = (100×5)+(2×5)", GREEN),
            ("Половина, четвртина, осмина — лесно", BLUE),
            ("2¹⁰ = 1024 — секој програмер знае", PURPLE),
            ("Делење со 0{,}6 → помножи и горе и долу", ORANGE),
        ]
        rows = VGroup()
        for txt, c in bullets:
            dot = Dot(radius=0.12, color=c)
            label = Tex(txt, font_size=28, color=WHITE2)
            row = VGroup(dot, label).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(title10, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        outro = Text("Редот спасува. Знаците зборуваат.",
                     font_size=36, color=YELLOW, weight=BOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(Write(outro), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(title10), FadeOut(rows), FadeOut(outro), run_time=0.8)
        self.wait(0.3)
