"""
chem8-4-6  —  Реакции на неутрализација
Хемија 8, Единица 4: Киселини, бази и соли

Teaching narrative — Andonovski-style: three-beat punches,
neutralization as peacemaking, personification, one-word finishers.
Render:  manim -ql chem8-4-6.py Chem846Scene
Output:  media/videos/chem8-4-6/480p15/Chem846Scene.mp4
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


class Chem846Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Киселина и база.", font_size=44, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.4)

        opp = Text("Спротивни.", font_size=38, color=RED, weight=BOLD).move_to(UP*0.6)
        self.play(FadeIn(opp, shift=UP*0.2), run_time=0.7)
        self.wait(0.4)

        together = Text("Заедно — сол и вода.", font_size=36, color=GREEN).move_to(DOWN*0.2)
        self.play(Write(together), run_time=1.0)
        self.wait(0.4)

        balance = Text("Совршена рамнотежа.", font_size=32, color=BLUE).to_edge(DOWN, buff=1.2)
        peace   = Text("Хемијата прави мир од конфликт.",
                       font_size=30, color=ORANGE, weight=BOLD).to_edge(DOWN, buff=0.4)
        self.play(Write(balance), run_time=0.9)
        self.play(FadeIn(peace, shift=UP*0.2), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, opp, together, balance, peace)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ОСНОВНА ЕДНАЧКА                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("general_eq")

        t2 = section_title("Општо правило")
        self.play(Write(t2), run_time=0.8)

        gen = MathTex(
            r"\text{киселина}", r"+", r"\text{база}",
            r"\rightarrow",
            r"\text{сол}", r"+", r"\text{вода}",
            font_size=44,
        )
        gen[0].set_color(RED)
        gen[2].set_color(BLUE)
        gen[3].set_color(YELLOW)
        gen[4].set_color(GREEN)
        gen[6].set_color("#4fc3f7")
        gen.move_to(ORIGIN + UP*0.2)
        self.play(Write(gen), run_time=2.0)
        self.wait(0.8)

        c2 = callout("Кога киселина среќава база — раѓаат нешто ново.",
                     width=12.0, font_size=26, border=GREEN)
        c2.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(c2, shift=UP*0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, gen, c2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  КОНКРЕТЕН ПРИМЕР HCl + NaOH                     ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hcl_naoh")

        t3 = section_title("Пример: HCl + NaOH")
        self.play(Write(t3), run_time=0.8)

        # Two beakers
        def beaker(color, formula, name, color_label):
            body = VGroup(
                Polygon(
                    [-0.7, -0.9, 0], [0.7, -0.9, 0],
                    [0.85, 0.8, 0], [-0.85, 0.8, 0],
                    fill_color=DARK_CARD, fill_opacity=0.4,
                    stroke_color=WHITE2, stroke_width=2,
                ),
            )
            liquid = Polygon(
                [-0.62, -0.85, 0], [0.62, -0.85, 0],
                [0.72, 0.2, 0], [-0.72, 0.2, 0],
                fill_color=color, fill_opacity=0.85, stroke_opacity=0,
            )
            f = MathTex(formula, font_size=32, color=WHITE2).next_to(body, UP, buff=0.15)
            n = Text(name, font_size=20, color=color_label).next_to(body, DOWN, buff=0.2)
            return VGroup(body, liquid, f, n)

        bk_acid = beaker(RED, r"\text{HCl}", "киселина", RED).shift(LEFT*4.5 + DOWN*0.3)
        bk_base = beaker(BLUE, r"\text{NaOH}", "база", BLUE).shift(LEFT*1.2 + DOWN*0.3)

        plus = MathTex("+", font_size=52, color=YELLOW).shift(LEFT*2.9 + DOWN*0.3)
        arrow = Arrow(LEFT*0.3 + DOWN*0.3, RIGHT*1.2 + DOWN*0.3,
                      color=YELLOW, stroke_width=4, buff=0.05)

        bk_salt  = beaker(GREEN, r"\text{NaCl}", "сол", GREEN).shift(RIGHT*2.5 + DOWN*0.3)
        bk_water = beaker("#4fc3f7", r"\text{H}_2\text{O}", "вода", BLUE).shift(RIGHT*5.0 + DOWN*0.3)

        plus2 = MathTex("+", font_size=52, color=YELLOW).shift(RIGHT*3.75 + DOWN*0.3)

        self.play(FadeIn(bk_acid, shift=UP*0.2), run_time=0.6)
        self.play(Write(plus), run_time=0.4)
        self.play(FadeIn(bk_base, shift=UP*0.2), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(bk_salt, shift=UP*0.2), run_time=0.6)
        self.play(Write(plus2), run_time=0.4)
        self.play(FadeIn(bk_water, shift=UP*0.2), run_time=0.6)
        self.wait(0.7)

        # Formula full
        eq = MathTex(
            r"\text{HCl}", r"+", r"\text{NaOH}",
            r"\rightarrow",
            r"\text{NaCl}", r"+", r"\text{H}_2\text{O}",
            font_size=40,
        )
        eq[0].set_color(RED)
        eq[2].set_color(BLUE)
        eq[3].set_color(YELLOW)
        eq[4].set_color(GREEN)
        eq[6].set_color("#4fc3f7")
        eq.to_edge(DOWN, buff=0.4)
        self.play(Write(eq), run_time=2.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, bk_acid, bk_base, bk_salt, bk_water,
                                  plus, plus2, arrow, eq)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  pH СЕ ПРИБЛИЖУВА КОН 7                          ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ph_moves")

        t4 = section_title("pH се движи кон 7")
        self.play(Write(t4), run_time=0.8)

        # pH bar 0-14
        colors_ph = [
            "#d32f2f","#e53935","#ef5350","#ff7043","#ff9800",
            "#ffb74d","#ffd54f","#81c784","#4db6ac","#26a69a",
            "#42a5f5","#1e88e5","#5e35b1","#7b1fa2","#4a148c",
        ]
        cells = VGroup()
        cell_w = 0.7
        for i, col in enumerate(colors_ph):
            sq = Square(side_length=cell_w, fill_color=col, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=0.8)
            sq.shift(RIGHT*(i - 7)*cell_w)
            n = Text(str(i), font_size=16, color=WHITE2 if i != 7 else "#0d1b2e", weight=BOLD)
            n.move_to(sq)
            cells.add(VGroup(sq, n))
        cells.shift(UP*0.2)
        self.play(FadeIn(cells), run_time=0.9)

        # Two arrows moving toward 7
        a1 = Arrow(cells[1].get_bottom() + DOWN*0.7,
                   cells[7].get_bottom() + DOWN*0.2,
                   color=RED, stroke_width=4, buff=0.05)
        a1_l = Text("киселина расте кон 7", font_size=20, color=RED).next_to(a1, DOWN, buff=0.1).shift(LEFT*0.5)

        a2 = Arrow(cells[13].get_bottom() + DOWN*0.7,
                   cells[7].get_bottom() + DOWN*0.2,
                   color=BLUE, stroke_width=4, buff=0.05)
        a2_l = Text("база паѓа кон 7", font_size=20, color=BLUE).next_to(a2, DOWN, buff=0.1).shift(RIGHT*0.5)

        self.play(GrowArrow(a1), Write(a1_l), run_time=0.9)
        self.play(GrowArrow(a2), Write(a2_l), run_time=0.9)

        # Star at 7
        star = Star(n=6, outer_radius=0.35, inner_radius=0.15,
                    fill_color=GREEN, fill_opacity=1, stroke_color=WHITE2,
                    stroke_width=1.5).next_to(cells[7], UP, buff=0.2)
        self.play(FadeIn(star, scale=0.5), run_time=0.6)

        meet = Text("Се среќаваат во неутралност.",
                    font_size=26, color=GREEN).to_edge(DOWN, buff=0.4)
        self.play(Write(meet), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, cells, a1, a1_l, a2, a2_l, star, meet)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ПРАКТИЧНИ ПРИМЕНИ                               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("uses")

        t5 = section_title("Каде неутрализацијата работи?")
        self.play(Write(t5), run_time=0.8)

        def use_card(emoji_text, title_text, sub_text, color):
            box = RoundedRectangle(width=3.6, height=2.6, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            icon = Text(emoji_text, font_size=44, color=color, weight=BOLD)
            ttl  = Text(title_text, font_size=22, color=color, weight=BOLD)
            sub  = Text(sub_text, font_size=17, color=WHITE2)
            inner = VGroup(icon, ttl, sub).arrange(DOWN, buff=0.15).move_to(box)
            return VGroup(box, inner)

        c1 = use_card("анти-киселина", "Стомак",
                      "лекови гасат печење", RED).shift(LEFT*4.2 + DOWN*0.3)
        c2 = use_card("вар на поле", "Почва",
                      "вар поправа кисела земја", GREEN).shift(DOWN*0.3)
        c3 = use_card("паста за заби", "Уста",
                      "ги неутрализира кислините", BLUE).shift(RIGHT*4.2 + DOWN*0.3)

        for c in (c1, c2, c3):
            self.play(FadeIn(c, shift=UP*0.2), run_time=0.6)
        self.wait(1.2)

        bottom = Text("Од лек до нива — еден ист принцип.",
                      font_size=26, color=YELLOW).to_edge(DOWN, buff=0.3)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, c1, c2, c3, bottom)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CLOSER                                          ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Не борба.", font_size=42, color=RED, weight=BOLD)
        close1.move_to(UP*0.7)
        self.play(Write(close1), run_time=0.9)
        self.wait(0.3)

        close2 = Text("Не победа.", font_size=42, color=BLUE, weight=BOLD)
        close2.move_to(ORIGIN)
        self.play(Write(close2), run_time=0.9)
        self.wait(0.3)

        close3 = Text("Рамнотежа.", font_size=46, color=GREEN, weight=BOLD)
        close3.move_to(DOWN*0.8)
        self.play(Write(close3), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(close1, close2, close3)), run_time=0.7)
        self.wait(0.3)
