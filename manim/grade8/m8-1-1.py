"""
m8-1-1  —  Цели броеви, степени и корени
Математика 8, Единица 1: Броеви

Teaching narrative — Andonovski-style: numbers as characters,
operations as verbs of life. Short punchy sentences, не...туку contrast,
rhetorical questions that answer themselves.
Render:  manim -ql m8-1-1.py M811Scene
Output:  media/videos/m8-1-1/480p15/M811Scene.mp4
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


def num_chip(value, color=BLUE, size=0.7):
    box = RoundedRectangle(
        width=size * 1.4, height=size * 1.2, corner_radius=0.15,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    label = Text(str(value), font_size=int(size * 40), color=WHITE2, weight=BOLD)
    label.move_to(box)
    return VGroup(box, label)


class M811Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "Што е најголемиот број? А најмалиот?",
            font_size=44, color=YELLOW, weight=BOLD,
        )
        hook_q.to_edge(UP, buff=0.55)
        self.play(Write(hook_q), run_time=1.5)
        self.wait(0.6)

        answer = Text(
            "Не постои. Има само патување.",
            font_size=36, color=WHITE2,
        )
        answer.next_to(hook_q, DOWN, buff=0.6)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(hook_q), FadeOut(answer), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  NUMBER LINE — ЦЕЛИ БРОЕВИ                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("number_line")

        title2 = section_title("Цели броеви")
        self.play(Write(title2), run_time=1.0)

        nline = NumberLine(
            x_range=[-5, 5, 1],
            length=11,
            color=GREY,
            include_numbers=True,
            font_size=26,
            label_direction=DOWN,
        )
        nline.shift(DOWN * 0.4)
        self.play(Create(nline), run_time=1.5)

        # Zero highlight
        zero_dot = Dot(nline.n2p(0), color=YELLOW, radius=0.14)
        zero_lbl = Text("нула", font_size=24, color=YELLOW).next_to(zero_dot, UP, buff=0.25)
        self.play(GrowFromCenter(zero_dot), Write(zero_lbl), run_time=0.8)
        self.wait(0.4)

        # Negative side
        neg_brace = Brace(
            Line(nline.n2p(-5), nline.n2p(-0.2)), direction=UP, color=RED
        )
        neg_lbl = Text("негативни", font_size=24, color=RED).next_to(neg_brace, UP, buff=0.1)
        self.play(GrowFromCenter(neg_brace), Write(neg_lbl), run_time=0.8)

        # Positive side
        pos_brace = Brace(
            Line(nline.n2p(0.2), nline.n2p(5)), direction=UP, color=GREEN
        )
        pos_lbl = Text("позитивни", font_size=24, color=GREEN).next_to(pos_brace, UP, buff=0.1)
        self.play(GrowFromCenter(pos_brace), Write(pos_lbl), run_time=0.8)
        self.wait(1.0)

        line_msg = callout("Линијата нема крај. Има само правец.", border=YELLOW)
        line_msg.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(line_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(title2), FadeOut(nline), FadeOut(zero_dot), FadeOut(zero_lbl),
            FadeOut(neg_brace), FadeOut(neg_lbl),
            FadeOut(pos_brace), FadeOut(pos_lbl),
            FadeOut(line_msg),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 3.  SIGN RULES — Собирање / одземање                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sign_add")

        title3 = section_title("Знаците зборуваат")
        self.play(Write(title3), run_time=1.0)

        rule_add = Text("Исти знаци → собирај. Различни → одземи.", font_size=30, color=WHITE2)
        rule_add.next_to(title3, DOWN, buff=0.5)
        self.play(Write(rule_add), run_time=1.2)
        self.wait(0.5)

        ex1 = MathTex("(+3) + (+5) = +8", font_size=42, color=GREEN)
        ex2 = MathTex("(-3) + (-5) = -8", font_size=42, color=GREEN)
        ex3 = MathTex("(+7) + (-3) = +4", font_size=42, color=ORANGE)
        ex4 = MathTex("(-7) + (+3) = -4", font_size=42, color=ORANGE)
        examples = VGroup(ex1, ex2, ex3, ex4).arrange(DOWN, buff=0.35)
        examples.next_to(rule_add, DOWN, buff=0.5)

        for ex in examples:
            self.play(Write(ex), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(title3), FadeOut(rule_add), FadeOut(examples), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  SIGN RULES GRID — множење / делење               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sign_grid")

        title4 = section_title("Множење и делење — мрежа на знаци")
        self.play(Write(title4), run_time=1.0)

        # 4-cell grid
        cells = []
        labels_top = [Text("+", font_size=44, color=GREEN, weight=BOLD),
                      Text("−", font_size=44, color=RED, weight=BOLD)]
        labels_left = [Text("+", font_size=44, color=GREEN, weight=BOLD),
                       Text("−", font_size=44, color=RED, weight=BOLD)]
        results = [["+", "−"], ["−", "+"]]
        result_colors = [[GREEN, RED], [RED, GREEN]]

        grid = VGroup()
        for r in range(2):
            for c in range(2):
                cell = RoundedRectangle(
                    width=2.0, height=1.6, corner_radius=0.15,
                    fill_color=DARK_CARD, fill_opacity=1,
                    stroke_color=BLUE, stroke_width=2,
                )
                cell.move_to(RIGHT * (c * 2.2) + DOWN * (r * 1.8))
                txt = Text(results[r][c], font_size=60, color=result_colors[r][c], weight=BOLD)
                txt.move_to(cell)
                grid.add(VGroup(cell, txt))
        grid.move_to(ORIGIN + DOWN * 0.3)

        # Top headers
        top_grp = VGroup(*labels_top).arrange(RIGHT, buff=1.8)
        top_grp.next_to(grid, UP, buff=0.3)
        top_grp.shift(RIGHT * 0.05)

        left_grp = VGroup(*labels_left).arrange(DOWN, buff=1.5)
        left_grp.next_to(grid, LEFT, buff=0.3)
        left_grp.shift(UP * 0.05)

        self.play(Create(grid), run_time=1.5)
        self.play(Write(top_grp), Write(left_grp), run_time=0.8)
        self.wait(0.8)

        rule_grid = callout("Исти → плус. Различни → минус.", border=YELLOW, font_size=30)
        rule_grid.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(rule_grid, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        # Andonovski moment
        and1 = Text("Минус по минус е плус. Парадокс?", font_size=32, color=YELLOW)
        and2 = Text("Не. Тоа е законот.", font_size=32, color=WHITE2)
        and3 = Text("Математиката не лаже. Никогаш.", font_size=32, color=YELLOW, weight=BOLD)
        ands = VGroup(and1, and2, and3).arrange(DOWN, buff=0.3)
        ands.move_to(ORIGIN)

        self.play(FadeOut(title4), FadeOut(grid), FadeOut(top_grp),
                  FadeOut(left_grp), FadeOut(rule_grid), run_time=0.6)
        for a in ands:
            self.play(Write(a), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(ands), run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 5.  GCD / LCM — НЗД и НСС                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("gcd_lcm")

        title5 = section_title("Делители и содржатели")
        self.play(Write(title5), run_time=1.0)

        # Divisors of 12
        div12 = Text("Делители на 12:", font_size=30, color=WHITE2)
        div12.shift(UP * 1.6 + LEFT * 3.5)
        div_nums = VGroup(*[num_chip(n, color=BLUE) for n in [1, 2, 3, 4, 6, 12]])
        div_nums.arrange(RIGHT, buff=0.2)
        div_nums.next_to(div12, RIGHT, buff=0.3)

        # Divisors of 18
        div18 = Text("Делители на 18:", font_size=30, color=WHITE2)
        div18.shift(UP * 0.4 + LEFT * 3.5)
        div_nums2 = VGroup(*[num_chip(n, color=PURPLE) for n in [1, 2, 3, 6, 9, 18]])
        div_nums2.arrange(RIGHT, buff=0.2)
        div_nums2.next_to(div18, RIGHT, buff=0.3)

        self.play(Write(div12), Create(div_nums), run_time=1.0)
        self.play(Write(div18), Create(div_nums2), run_time=1.0)
        self.wait(0.6)

        gcd = MathTex(r"\text{НЗД}(12, 18) = 6", font_size=42, color=GREEN)
        gcd.shift(DOWN * 0.9)
        self.play(Write(gcd), run_time=1.0)
        self.wait(0.6)

        lcm = MathTex(r"\text{НСС}(12, 18) = 36", font_size=42, color=ORANGE)
        lcm.shift(DOWN * 1.9)
        self.play(Write(lcm), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(title5), FadeOut(div12), FadeOut(div18),
            FadeOut(div_nums), FadeOut(div_nums2),
            FadeOut(gcd), FadeOut(lcm),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 6.  PRIMES                                           ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("primes")

        title6 = section_title("Прости броеви")
        self.play(Write(title6), run_time=1.0)

        prime_def = Text("Точно два делители: 1 и самиот.", font_size=30, color=WHITE2)
        prime_def.next_to(title6, DOWN, buff=0.5)
        self.play(Write(prime_def), run_time=1.0)

        primes = [2, 3, 5, 7, 11, 13]
        prime_chips = VGroup(*[num_chip(n, color=YELLOW, size=0.9) for n in primes])
        prime_chips.arrange(RIGHT, buff=0.3)
        prime_chips.next_to(prime_def, DOWN, buff=0.7)
        for chip in prime_chips:
            self.play(GrowFromCenter(chip), run_time=0.3)
        self.wait(0.6)

        prime_msg = callout("Простите се темелите. Сè друго е нивен производ.",
                            border=YELLOW, font_size=28)
        prime_msg.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(prime_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title6), FadeOut(prime_def), FadeOut(prime_chips),
                  FadeOut(prime_msg), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  PRIME FACTORIZATION TREE — 12 = 2² × 3           ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("factor_tree")

        title7 = section_title("Растав на прости множители")
        self.play(Write(title7), run_time=1.0)

        root = num_chip(12, color=YELLOW, size=1.0)
        root.move_to(UP * 1.8)

        # Level 1
        n2 = num_chip(2, color=BLUE, size=0.9)
        n6 = num_chip(6, color=ORANGE, size=0.9)
        n2.move_to(LEFT * 1.5 + UP * 0.4)
        n6.move_to(RIGHT * 1.5 + UP * 0.4)

        # Level 2
        n2b = num_chip(2, color=BLUE, size=0.9)
        n3 = num_chip(3, color=BLUE, size=0.9)
        n2b.move_to(RIGHT * 0.3 + DOWN * 1.0)
        n3.move_to(RIGHT * 2.7 + DOWN * 1.0)

        line1 = Line(root.get_bottom(), n2.get_top(), color=GREY, stroke_width=2)
        line2 = Line(root.get_bottom(), n6.get_top(), color=GREY, stroke_width=2)
        line3 = Line(n6.get_bottom(), n2b.get_top(), color=GREY, stroke_width=2)
        line4 = Line(n6.get_bottom(), n3.get_top(), color=GREY, stroke_width=2)

        self.play(GrowFromCenter(root), run_time=0.5)
        self.play(Create(line1), Create(line2), GrowFromCenter(n2), GrowFromCenter(n6),
                  run_time=0.8)
        self.play(Create(line3), Create(line4), GrowFromCenter(n2b), GrowFromCenter(n3),
                  run_time=0.8)
        self.wait(0.5)

        result = MathTex(r"12 = 2^2 \times 3", font_size=48, color=GREEN)
        result.to_edge(DOWN, buff=0.8)
        self.play(Write(result), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(title7), FadeOut(root), FadeOut(n2), FadeOut(n6),
            FadeOut(n2b), FadeOut(n3),
            FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4),
            FadeOut(result),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 8.  POWERS — степени                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("powers")

        title8 = section_title("Степени")
        self.play(Write(title8), run_time=1.0)

        pow_def = MathTex(r"2^3 = 2 \times 2 \times 2 = 8", font_size=44, color=WHITE2)
        pow_def.shift(UP * 1.5)
        self.play(Write(pow_def), run_time=1.2)
        self.wait(0.5)

        # Power tower
        tower_base = Square(side_length=1.2, color=BLUE, fill_color=DARK_CARD, fill_opacity=1)
        tower_base.shift(DOWN * 1.5)
        tower_mid = Square(side_length=1.0, color=BLUE, fill_color=DARK_CARD, fill_opacity=1)
        tower_mid.next_to(tower_base, UP, buff=0.0)
        tower_top = Square(side_length=0.8, color=BLUE, fill_color=DARK_CARD, fill_opacity=1)
        tower_top.next_to(tower_mid, UP, buff=0.0)

        lbl_b = Text("2", font_size=32, color=YELLOW).move_to(tower_base)
        lbl_m = Text("2", font_size=28, color=YELLOW).move_to(tower_mid)
        lbl_t = Text("2", font_size=24, color=YELLOW).move_to(tower_top)

        tower = VGroup(tower_base, lbl_b, tower_mid, lbl_m, tower_top, lbl_t)
        tower.move_to(LEFT * 3 + DOWN * 0.4)

        self.play(FadeIn(tower_base), FadeIn(lbl_b), run_time=0.4)
        self.play(FadeIn(tower_mid), FadeIn(lbl_m), run_time=0.4)
        self.play(FadeIn(tower_top), FadeIn(lbl_t), run_time=0.4)

        eight = Text("= 8", font_size=44, color=GREEN, weight=BOLD)
        eight.next_to(tower, RIGHT, buff=1.2)
        self.play(Write(eight), run_time=0.7)
        self.wait(0.8)

        # Sign of negatives raised
        neg_rules = VGroup(
            MathTex(r"(-2)^3 = -8", font_size=38, color=RED),
            MathTex(r"(-2)^2 = +4", font_size=38, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        neg_rules.move_to(RIGHT * 3.2 + DOWN * 0.4)

        self.play(Write(neg_rules[0]), run_time=0.7)
        self.play(Write(neg_rules[1]), run_time=0.7)
        self.wait(1.0)

        odd_even = callout("Непарен степен — знакот живее. Парен — знакот умира.",
                           border=YELLOW, font_size=26)
        odd_even.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(odd_even, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title8), FadeOut(pow_def), FadeOut(tower), FadeOut(eight),
            FadeOut(neg_rules), FadeOut(odd_even),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 9.  ROOTS — корени                                   ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("roots")

        title9 = section_title("Корени — обратниот пат")
        self.play(Write(title9), run_time=1.0)

        sq_root = MathTex(r"\sqrt{16} = 4", font_size=52, color=GREEN)
        sq_root.shift(UP * 0.8 + LEFT * 2.5)
        cube_root = MathTex(r"\sqrt[3]{8} = 2", font_size=52, color=ORANGE)
        cube_root.shift(UP * 0.8 + RIGHT * 2.5)

        self.play(Write(sq_root), run_time=1.0)
        self.play(Write(cube_root), run_time=1.0)
        self.wait(0.6)

        explain = VGroup(
            Text("Степенот експлодира.", font_size=32, color=YELLOW),
            Text("Коренот враќа дома.", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.4)
        explain.shift(DOWN * 1.2)
        self.play(Write(explain[0]), run_time=0.8)
        self.play(Write(explain[1]), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(title9), FadeOut(sq_root), FadeOut(cube_root),
                  FadeOut(explain), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 10.  SUMMARY                                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title10 = section_title("Резиме", color=GREEN)
        self.play(Write(title10), run_time=1.0)

        bullets = [
            ("Цели броеви: негативни, нула, позитивни", BLUE),
            ("Исти знаци собирај. Различни одземи.", YELLOW),
            ("НЗД дели заедно. НСС множи заедно.", PURPLE),
            ("Простите се темелите.", ORANGE),
            ("Степенот експлодира. Коренот враќа.", GREEN),
        ]
        rows = VGroup()
        for txt, c in bullets:
            dot = Dot(radius=0.12, color=c)
            label = Text(txt, font_size=26, color=WHITE2)
            row = VGroup(dot, label).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        rows.next_to(title10, DOWN, buff=0.6)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        outro = Text("Бројот не е знак. Бројот е приказна.",
                     font_size=34, color=YELLOW, weight=BOLD)
        outro.to_edge(DOWN, buff=0.5)
        self.play(Write(outro), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(title10), FadeOut(rows), FadeOut(outro), run_time=0.8)
        self.wait(0.3)
