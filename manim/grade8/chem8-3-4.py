"""
chem8-3-4  —  Хемиски формули
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: formulae as grammar of chemistry,
not magic, one-word finishers.
Render:  manim -ql chem8-3-4.py Chem834Scene
Output:  media/videos/chem8-3-4/480p15/Chem834Scene.mp4
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


class Chem834Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Две букви.", font_size=46, color=YELLOW, weight=BOLD)
        h2 = Text("Два броеви.", font_size=46, color=YELLOW, weight=BOLD)
        h3 = Text("И знаеш сè.", font_size=46, color=WHITE2, weight=BOLD)
        group = VGroup(h1, h2, h3).arrange(DOWN, buff=0.35).move_to(UP*0.5)

        for h in (h1, h2, h3):
            self.play(Write(h), run_time=0.7)
            self.wait(0.2)
        self.wait(0.5)

        h2o = MathTex(r"H_2 O", font_size=90, color=BLUE).move_to(DOWN*1.8)
        water_lbl = Text("Тоа е вода.", font_size=30, color=WHITE2).next_to(h2o, DOWN, buff=0.3)
        self.play(Write(h2o), run_time=0.8)
        self.play(Write(water_lbl), run_time=0.8)
        self.wait(0.5)

        finish = Text("Не магија. Граматика.",
                      font_size=30, color=GREEN, weight=BOLD).next_to(water_lbl, DOWN, buff=0.3)
        self.play(Write(finish), run_time=1.1)
        self.wait(1.3)

        self.play(FadeOut(VGroup(group, h2o, water_lbl, finish)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                      ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Хемиска формула")
        self.play(Write(t2), run_time=0.8)

        defn = callout("Симболи + бројки. Кој елемент? Колку атоми?",
                       width=11.5, font_size=28)
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)
        self.wait(0.4)

        # Big H2O dissected
        h2o_big = MathTex(r"H", r"_2", r"O", font_size=130, color=WHITE2).move_to(DOWN*0.3)
        h2o_big[0].set_color(BLUE)
        h2o_big[1].set_color(YELLOW)
        h2o_big[2].set_color(RED)
        self.play(Write(h2o_big), run_time=1.0)

        # Arrows + labels
        lbl_h = Text("елемент H", font_size=22, color=BLUE)
        lbl_h.next_to(h2o_big[0], DOWN, buff=0.7).shift(LEFT*0.2)
        lbl_2 = Text("2 атоми", font_size=22, color=YELLOW)
        lbl_2.next_to(h2o_big[1], DOWN, buff=0.7).shift(RIGHT*0.1)
        lbl_o = Text("елемент O", font_size=22, color=RED)
        lbl_o.next_to(h2o_big[2], DOWN, buff=0.7).shift(RIGHT*0.2)

        self.play(Write(lbl_h), Write(lbl_2), Write(lbl_o), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, defn, h2o_big, lbl_h, lbl_2, lbl_o)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ЧЕТЕЊЕ ФОРМУЛА                                ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("read")

        t3 = section_title("Како се чита формула?")
        self.play(Write(t3), run_time=0.8)

        # CO2 example
        co2 = MathTex(r"CO_2", font_size=100, color=WHITE2).move_to(LEFT*4.0 + UP*0.5)
        co2_brk = VGroup(
            Text("1 C", font_size=28, color=GREY),
            Text("2 O", font_size=28, color=RED),
            Text("3 атоми вкупно", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(co2, DOWN, buff=0.4)

        self.play(Write(co2), run_time=0.8)
        for line in co2_brk:
            self.play(Write(line), run_time=0.5)
        self.wait(0.4)

        # CaCO3
        caco3 = MathTex(r"CaCO_3", font_size=100, color=WHITE2).move_to(RIGHT*4.0 + UP*0.5)
        caco3_brk = VGroup(
            Text("1 Ca", font_size=28, color=ORANGE),
            Text("1 C", font_size=28, color=GREY),
            Text("3 O", font_size=28, color=RED),
            Text("5 атоми вкупно", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(caco3, DOWN, buff=0.4)

        self.play(Write(caco3), run_time=0.8)
        for line in caco3_brk:
            self.play(Write(line), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t3, co2, co2_brk, caco3, caco3_brk)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ЗАГРАДИ                                        ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("parens")

        t4 = section_title("Загради во формула")
        self.play(Write(t4), run_time=0.8)

        # Mg(OH)2
        f = MathTex(r"Mg(OH)_2", font_size=120, color=WHITE2).move_to(UP*0.6)
        self.play(Write(f), run_time=1.0)

        # Step expansion
        step1 = Text("1 Mg", font_size=30, color=ORANGE).shift(LEFT*4.0 + DOWN*1.5)
        step2 = Text("2 × (O+H)", font_size=30, color=BLUE).shift(DOWN*1.5)
        step3 = Text("= 2 O + 2 H", font_size=30, color=GREEN).shift(RIGHT*4.0 + DOWN*1.5)

        self.play(Write(step1), run_time=0.7)
        self.play(Write(step2), run_time=0.7)
        self.play(Write(step3), run_time=0.7)
        self.wait(0.5)

        total = Text("Вкупно: 1 Mg + 2 O + 2 H = 5 атоми",
                     font_size=30, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(total), run_time=1.2)
        self.wait(1.3)

        rule = callout("Загради * долен индекс = за сите внатре.",
                       width=11.5, font_size=26, border=ORANGE)
        rule.next_to(t4, DOWN, buff=0.5)
        self.play(FadeOut(f), FadeIn(rule, shift=UP*0.2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t4, rule, step1, step2, step3, total)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ВАЛЕНТНОСТ И БАЛАНС                            ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("valence")

        t5 = section_title("Валентност — колку врски?")
        self.play(Write(t5), run_time=0.8)

        # Table of valences
        v_table = VGroup()
        rows = [
            ("1", "H, Na, K, Cl", BLUE),
            ("2", "O, Mg, Ca, Zn", GREEN),
            ("3", "Al, N", ORANGE),
            ("4", "C, Si", PURPLE),
        ]
        for i, (v, elems, color) in enumerate(rows):
            v_label = Text(f"v = {v}", font_size=26, color=color, weight=BOLD)
            e_label = Text(elems, font_size=24, color=WHITE2)
            line = VGroup(v_label, e_label).arrange(RIGHT, buff=0.6, aligned_edge=ORIGIN)
            v_table.add(line)
        v_table.arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(LEFT*3.5 + DOWN*0.2)
        for line in v_table:
            self.play(Write(line), run_time=0.5)

        # Right: example AlCl3
        arrow_eq = MathTex(r"Al + Cl \to AlCl_3", font_size=42, color=WHITE2)
        arrow_eq.shift(RIGHT*3.5 + UP*1.5)
        balance = VGroup(
            Text("v(Al) = 3", font_size=24, color=ORANGE),
            Text("v(Cl) = 1", font_size=24, color=GREEN),
            Text("3 Cl за 1 Al", font_size=24, color=YELLOW),
            MathTex(r"AlCl_3", font_size=48, color=WHITE2),
        ).arrange(DOWN, buff=0.25).next_to(arrow_eq, DOWN, buff=0.3)

        self.play(Write(arrow_eq), run_time=0.8)
        for line in balance:
            self.play(Write(line), run_time=0.5)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t5, v_table, arrow_eq, balance)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ЧЕСТИ ФОРМУЛИ                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("common")

        t6 = section_title("Формули што мораш да ги знаеш")
        self.play(Write(t6), run_time=0.8)

        def fcard(formula, name, color, pos):
            box = RoundedRectangle(width=3.8, height=1.4, corner_radius=0.18,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2)
            f = MathTex(formula, font_size=36, color=color)
            n = Text(name, font_size=18, color=WHITE2)
            inner = VGroup(f, n).arrange(DOWN, buff=0.1).move_to(box)
            return VGroup(box, inner).move_to(pos)

        c1 = fcard(r"H_2 O", "вода", BLUE, LEFT*4.2 + UP*1.8)
        c2 = fcard(r"CO_2", "ј.-диоксид", GREY, ORIGIN + UP*1.8)
        c3 = fcard(r"NaCl", "сол", YELLOW, RIGHT*4.2 + UP*1.8)
        c4 = fcard(r"HCl", "кисел.", GREEN, LEFT*4.2 + UP*0.1)
        c5 = fcard(r"H_2 SO_4", "сулф. кис.", RED, ORIGIN + UP*0.1)
        c6 = fcard(r"NaOH", "сода кауст.", PURPLE, RIGHT*4.2 + UP*0.1)
        c7 = fcard(r"CaCO_3", "варовник", ORANGE, LEFT*4.2 + DOWN*1.6)
        c8 = fcard(r"NH_3", "амонијак", BLUE, ORIGIN + DOWN*1.6)
        c9 = fcard(r"Fe_2 O_3", "рѓа", RED, RIGHT*4.2 + DOWN*1.6)

        all_cards = VGroup(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        self.play(LaggedStartMap(lambda m: FadeIn(m, shift=UP*0.15), all_cards,
                                  lag_ratio=0.12), run_time=2.5)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t6, all_cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        c1f = Text("Формула пишува.", font_size=42, color=YELLOW, weight=BOLD).move_to(UP*1.0)
        c2f = Text("Формула брои.", font_size=42, color=YELLOW, weight=BOLD).move_to(ORIGIN)
        c3f = Text("Граматика.", font_size=54, color=GREEN, weight=BOLD).move_to(DOWN*1.2)

        self.play(Write(c1f), run_time=0.7)
        self.play(Write(c2f), run_time=0.7)
        self.play(Write(c3f), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(c1f, c2f, c3f)), run_time=0.7)
        self.wait(0.3)
