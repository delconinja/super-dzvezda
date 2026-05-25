"""
chem8-4-2  —  Реактанти, продукти, балансирање равенки
Хемија 8, Единица 4: Хемиски реакции

Teaching narrative — Andonovski-style: three-beat punches,
atoms as characters, conservation as drama.
Render:  manim -ql chem8-4-2.py Chem842Scene
Output:  media/videos/chem8-4-2/480p15/Chem842Scene.mp4
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


def atom(pos, label_text, color, r=0.32):
    c = Circle(radius=r, fill_color=color, fill_opacity=1,
               stroke_color=WHITE2, stroke_width=1.5).move_to(pos)
    lbl = Text(label_text, font_size=22, color="#0d1b2e", weight=BOLD).move_to(pos)
    return VGroup(c, lbl)


class Chem842Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — LAVOISIER
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Ништо не се губи.",
                  font_size=42, color=YELLOW, weight=BOLD)
        h2 = Text("Ништо не се добива.",
                  font_size=42, color=YELLOW, weight=BOLD)
        h3 = Text("Сè се претвора.",
                  font_size=42, color=GREEN, weight=BOLD)
        h4 = Text("Лавоазјé го виде. 1789 година.",
                  font_size=32, color=WHITE2)
        h5 = Text("Истина до денеска.",
                  font_size=34, color=ORANGE, slant=ITALIC)
        hook = VGroup(h1, h2, h3, h4, h5).arrange(DOWN, buff=0.3)
        hook.move_to(ORIGIN)

        self.play(Write(h1), run_time=0.9)
        self.wait(0.3)
        self.play(Write(h2), run_time=0.9)
        self.wait(0.3)
        self.play(Write(h3), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(h4), run_time=0.8)
        self.wait(0.4)
        self.play(Write(h5), run_time=1.0)
        self.wait(1.3)
        self.play(FadeOut(hook), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ANATOMY OF AN EQUATION
        # ══════════════════════════════════════════════════════════
        self.next_section("anatomy")

        title = section_title("Анатомија на равенка", BLUE)
        self.play(Write(title), run_time=0.8)

        eq = MathTex(r"\text{Реактанти}", r"\;\to\;", r"\text{Продукти}",
                     font_size=54)
        eq[0].set_color(BLUE)
        eq[1].set_color(YELLOW)
        eq[2].set_color(GREEN)
        eq.move_to(UP * 0.8)
        self.play(Write(eq), run_time=1.3)
        self.wait(0.5)

        # Bullets
        b1 = Text("Реактанти — што влегува.",
                  font_size=28, color=BLUE)
        b2 = Text("Стрелка — се случува.",
                  font_size=28, color=YELLOW)
        b3 = Text("Продукти — што излегува.",
                  font_size=28, color=GREEN)
        bs = VGroup(b1, b2, b3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        bs.next_to(eq, DOWN, buff=0.7)
        for b in bs:
            self.play(FadeIn(b, shift=RIGHT * 0.15), run_time=0.6)
        self.wait(0.9)

        self.play(FadeOut(VGroup(title, eq, bs)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  WHY BALANCE? — ATOMS COUNTED
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        title2 = section_title("Зошто балансирање?", YELLOW)
        self.play(Write(title2), run_time=0.8)

        rule = VGroup(
            Text("Атоми не се создаваат.",
                 font_size=32, color=WHITE2),
            Text("Атоми не нестануваат.",
                 font_size=32, color=WHITE2),
            Text("Само се пресоредуваат.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        rule.move_to(UP * 0.5)

        for line in rule:
            self.play(Write(line), run_time=0.8)
            self.wait(0.2)
        self.wait(0.6)

        side_rule = Text("Број на атоми — ист на двете страни.",
                         font_size=28, color=ORANGE, slant=ITALIC)
        side_rule.next_to(rule, DOWN, buff=0.55)
        self.play(FadeIn(side_rule), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, rule, side_rule)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — BALANCING H2 + O2 → H2O
        # ══════════════════════════════════════════════════════════
        self.next_section("balance_water")

        title3 = section_title("Пример: водата", BLUE)
        self.play(Write(title3), run_time=0.8)

        # Step 1: unbalanced
        step1_lbl = Text("Чекор 1 — не балансирано", font_size=26, color=GREY)
        step1_lbl.move_to(UP * 2.0)
        step1 = MathTex(r"H_2", r"+", r"O_2", r"\to", r"H_2O", font_size=58)
        step1[0].set_color(BLUE)
        step1[2].set_color(RED)
        step1[4].set_color(GREEN)
        step1.move_to(UP * 0.8)

        count1 = MathTex(
            r"\text{Лева: } 2H,\ 2O \quad\big|\quad \text{Десна: } 2H,\ 1O",
            font_size=32, color=WHITE2)
        count1.move_to(DOWN * 0.4)

        warn = Text("Кислородот фали еден!",
                    font_size=28, color=RED, weight=BOLD)
        warn.move_to(DOWN * 1.5)

        self.play(FadeIn(step1_lbl), Write(step1), run_time=1.2)
        self.play(Write(count1), run_time=1.0)
        self.play(FadeIn(warn), run_time=0.7)
        self.wait(1.2)

        # Step 2: put 2 in front of H2O
        self.play(FadeOut(VGroup(step1_lbl, count1, warn)), run_time=0.4)

        coef_2_water = MathTex("2", font_size=58, color=YELLOW).next_to(step1[4], LEFT, buff=0.15)
        self.play(Write(coef_2_water), run_time=0.7)

        count2 = MathTex(
            r"\text{Лева: } 2H,\ 2O \quad\big|\quad \text{Десна: } 4H,\ 2O",
            font_size=32, color=WHITE2)
        count2.move_to(DOWN * 0.4)
        warn2 = Text("Сега водородот фали.",
                     font_size=28, color=RED, weight=BOLD)
        warn2.move_to(DOWN * 1.5)
        self.play(Write(count2), FadeIn(warn2), run_time=1.0)
        self.wait(1.0)

        # Step 3: put 2 in front of H2
        self.play(FadeOut(VGroup(count2, warn2)), run_time=0.3)
        coef_2_h2 = MathTex("2", font_size=58, color=YELLOW).next_to(step1[0], LEFT, buff=0.15)
        self.play(Write(coef_2_h2), run_time=0.7)

        count3 = MathTex(
            r"\text{Лева: } 4H,\ 2O \quad\big|\quad \text{Десна: } 4H,\ 2O",
            font_size=32, color=GREEN)
        count3.move_to(DOWN * 0.4)
        ok = Text("Балансирана!",
                  font_size=36, color=GREEN, weight=BOLD)
        ok.move_to(DOWN * 1.5)
        self.play(Write(count3), FadeIn(ok), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title3, step1, coef_2_water, coef_2_h2, count3, ok)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  METHANE COMBUSTION — CH4 + 2O2 → CO2 + 2H2O
        # ══════════════════════════════════════════════════════════
        self.next_section("methane")

        title4 = section_title("Согорување: метан", ORANGE)
        self.play(Write(title4), run_time=0.8)

        story = Text("Метан гори. Кислородот стапка по стапка.",
                     font_size=28, color=WHITE2)
        story.move_to(UP * 1.7)
        self.play(FadeIn(story), run_time=0.8)

        eq2 = MathTex(r"CH_4", r"+", r"2\,O_2", r"\to", r"CO_2", r"+", r"2\,H_2O",
                      font_size=56)
        eq2[0].set_color(BLUE)
        eq2[2].set_color(RED)
        eq2[4].set_color(GREY)
        eq2[6].set_color(GREEN)
        eq2.move_to(UP * 0.2)
        self.play(Write(eq2), run_time=1.7)
        self.wait(0.6)

        check = VGroup(
            Text("C: 1 = 1", font_size=28, color=GREEN),
            Text("H: 4 = 4", font_size=28, color=GREEN),
            Text("O: 4 = 4", font_size=28, color=GREEN),
        ).arrange(RIGHT, buff=0.7)
        check.next_to(eq2, DOWN, buff=0.7)
        for c in check:
            self.play(FadeIn(c), run_time=0.5)
        self.wait(0.6)

        verdict = Text("Сè се совпаѓа. Сè се пресоредува.",
                       font_size=28, color=GREEN, weight=BOLD)
        verdict.next_to(check, DOWN, buff=0.5)
        self.play(Write(verdict), run_time=1.1)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, story, eq2, check, verdict)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  RULES — NEVER CHANGE SUBSCRIPTS
        # ══════════════════════════════════════════════════════════
        self.next_section("rules")

        title5 = section_title("Правила", PURPLE)
        self.play(Write(title5), run_time=0.8)

        bad = MathTex(r"H_2 \to H_3", font_size=50, color=RED)
        bad_x = Text("✗ Никогаш!", font_size=30, color=RED, weight=BOLD)
        bad_g = VGroup(bad, bad_x).arrange(RIGHT, buff=0.6)
        bad_g.move_to(UP * 1.2)
        self.play(Write(bad), run_time=0.8)
        self.play(FadeIn(bad_x), run_time=0.5)
        self.wait(0.5)

        good = MathTex(r"2\,H_2", font_size=50, color=GREEN)
        good_v = Text("✓ Само коефициент!", font_size=30, color=GREEN, weight=BOLD)
        good_g = VGroup(good, good_v).arrange(RIGHT, buff=0.6)
        good_g.move_to(DOWN * 0.1)
        self.play(Write(good), run_time=0.8)
        self.play(FadeIn(good_v), run_time=0.5)
        self.wait(0.6)

        list_rules = VGroup(
            Text("• Долни индекси — не се пипаат.", font_size=26, color=WHITE2),
            Text("• Коефициенти — пред формула.", font_size=26, color=WHITE2),
            Text("• Најмал број — секогаш.", font_size=26, color=WHITE2),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        list_rules.move_to(DOWN * 1.7)
        for r in list_rules:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.55)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title5, bad_g, good_g, list_rules)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        c1 = Text("Атоми влегуваат. Атоми излегуваат.",
                  font_size=32, color=BLUE)
        c2 = Text("Истиот број. Друг распоред.",
                  font_size=32, color=YELLOW)
        c3 = Text("Балансирано — значи вистинито.",
                  font_size=30, color=WHITE2, slant=ITALIC)
        c4 = Text("Брои.",
                  font_size=58, color=GREEN, weight=BOLD)
        close = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.4)
        close.move_to(ORIGIN)

        self.play(Write(c1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(c2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(c3), run_time=0.9)
        self.wait(0.4)
        self.play(Write(c4), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
        self.wait(0.4)
