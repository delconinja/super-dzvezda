"""
chem8-3-2  —  Хемиски симболи
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: three-beat punches,
symbols as a universal language, one-word finishers.
Render:  manim -ql chem8-3-2.py Chem832Scene
Output:  media/videos/chem8-3-2/480p15/Chem832Scene.mp4
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


def element_tile(symbol, name, color, width=2.0, height=2.0):
    box = RoundedRectangle(width=width, height=height, corner_radius=0.18,
                            fill_color=DARK_CARD, fill_opacity=1,
                            stroke_color=color, stroke_width=2.5)
    s = Text(symbol, font_size=48, color=color, weight=BOLD)
    n = Text(name, font_size=18, color=WHITE2).next_to(s, DOWN, buff=0.15)
    inner = VGroup(s, n).move_to(box)
    return VGroup(box, inner)


class Chem832Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("H е водород.", font_size=44, color=BLUE, weight=BOLD)
        h2 = Text("O е кислород.", font_size=44, color=RED, weight=BOLD)
        h3 = Text("Au е злато.", font_size=44, color=YELLOW, weight=BOLD)
        group = VGroup(h1, h2, h3).arrange(DOWN, buff=0.45).move_to(UP*0.3)

        for h in (h1, h2, h3):
            self.play(Write(h), run_time=0.7)
            self.wait(0.2)
        self.wait(0.4)

        beat1 = Text("Една буква. Цел елемент.",
                     font_size=32, color=WHITE2).move_to(DOWN*2.1)
        self.play(Write(beat1), run_time=1.1)
        self.wait(0.5)

        finisher = Text("Хемијата зборува со јазик на симболи.",
                        font_size=30, color=GREEN, weight=BOLD).next_to(beat1, DOWN, buff=0.35)
        self.play(Write(finisher), run_time=1.3)
        self.wait(1.0)

        self.play(FadeOut(VGroup(group, beat1, finisher)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е СИМБОЛ                                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Хемиски симбол")
        self.play(Write(t2), run_time=0.8)

        defn = callout("1–2 букви — една меѓународна ознака за елемент.",
                       width=11.5, font_size=28)
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)

        # Rules
        rules = VGroup(
            Text("1. Прва буква — голема.", font_size=28, color=WHITE2),
            Text("2. Втора буква — мала.", font_size=28, color=WHITE2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN*0.3)
        for r in rules:
            self.play(Write(r), run_time=0.7)

        # Right vs wrong
        right = Text("Ca", font_size=44, color=GREEN, weight=BOLD).shift(LEFT*2.5 + DOWN*2.3)
        rl = Text("точно", font_size=20, color=GREEN).next_to(right, DOWN, buff=0.15)
        wrong = Text("CA", font_size=44, color=RED, weight=BOLD).shift(DOWN*2.3)
        wl = Text("грешка", font_size=20, color=RED).next_to(wrong, DOWN, buff=0.15)
        wrong2 = Text("cA", font_size=44, color=RED, weight=BOLD).shift(RIGHT*2.5 + DOWN*2.3)
        wl2 = Text("грешка", font_size=20, color=RED).next_to(wrong2, DOWN, buff=0.15)

        self.play(FadeIn(VGroup(right, rl)), run_time=0.6)
        self.play(FadeIn(VGroup(wrong, wl)), FadeIn(VGroup(wrong2, wl2)), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t2, defn, rules, right, rl, wrong, wl, wrong2, wl2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ИМИЊА ОД ЛАТИНСКИ                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("latin")

        t3 = section_title("Симболи од латински имиња")
        self.play(Write(t3), run_time=0.8)

        # Row 1: Fe / Au / Ag with Latin origins
        fe = element_tile("Fe", "железо", ORANGE).shift(LEFT*4.5 + UP*0.2)
        fe_lat = Text("Ferrum", font_size=22, color=GREY).next_to(fe, DOWN, buff=0.2)
        au = element_tile("Au", "злато", YELLOW).shift(UP*0.2)
        au_lat = Text("Aurum", font_size=22, color=GREY).next_to(au, DOWN, buff=0.2)
        ag = element_tile("Ag", "сребро", GREY).shift(RIGHT*4.5 + UP*0.2)
        ag_lat = Text("Argentum", font_size=22, color=GREY).next_to(ag, DOWN, buff=0.2)

        self.play(FadeIn(VGroup(fe, fe_lat), shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(VGroup(au, au_lat), shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(VGroup(ag, ag_lat), shift=UP*0.2), run_time=0.7)
        self.wait(0.5)

        # Row 2
        na = element_tile("Na", "натриум", PURPLE).shift(LEFT*4.5 + DOWN*2.3)
        na_lat = Text("Natrium", font_size=22, color=GREY).next_to(na, DOWN, buff=0.2)
        k = element_tile("K", "калиум", BLUE).shift(DOWN*2.3)
        k_lat = Text("Kalium", font_size=22, color=GREY).next_to(k, DOWN, buff=0.2)
        pb = element_tile("Pb", "олово", GREY).shift(RIGHT*4.5 + DOWN*2.3)
        pb_lat = Text("Plumbum", font_size=22, color=GREY).next_to(pb, DOWN, buff=0.2)

        self.play(FadeIn(VGroup(na, na_lat), shift=UP*0.2), run_time=0.6)
        self.play(FadeIn(VGroup(k, k_lat), shift=UP*0.2), run_time=0.6)
        self.play(FadeIn(VGroup(pb, pb_lat), shift=UP*0.2), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, fe, fe_lat, au, au_lat, ag, ag_lat,
                                  na, na_lat, k, k_lat, pb, pb_lat)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  IUPAC                                          ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("iupac")

        t4 = section_title("IUPAC — еден јазик за светот")
        self.play(Write(t4), run_time=0.8)

        # Au tile in centre, flags around
        au_big = element_tile("Au", "злато", YELLOW, width=2.6, height=2.6).move_to(ORIGIN)
        self.play(FadeIn(au_big, shift=UP*0.2), run_time=0.7)

        labels = [
            ("Македонија", UP*2.2 + LEFT*4.2),
            ("Кина", UP*2.2 + RIGHT*4.2),
            ("Германија", DOWN*2.4 + LEFT*4.2),
            ("Бразил", DOWN*2.4 + RIGHT*4.2),
        ]
        flags = VGroup()
        for txt, pos in labels:
            b = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.15,
                                  fill_color="#0d2b44", fill_opacity=1,
                                  stroke_color=BLUE, stroke_width=2).move_to(pos)
            l = Text(txt, font_size=22, color=WHITE2).move_to(b)
            au_inside = Text("Au", font_size=22, color=YELLOW, weight=BOLD).next_to(l, RIGHT, buff=0.2)
            grp = VGroup(b, l, au_inside)
            arrow = Arrow(start=au_big.get_center(), end=b.get_center(),
                          stroke_width=2, color=GREY, buff=1.4)
            flags.add(VGroup(grp, arrow))

        for fg in flags:
            self.play(FadeIn(fg), run_time=0.5)
        self.wait(1.2)

        one_lang = Text("Иста ознака. Секаде.",
                        font_size=30, color=GREEN).to_edge(DOWN, buff=0.4)
        self.play(Write(one_lang), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t4, au_big, flags, one_lang)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ИНДЕКС И КОЕФИЦИЕНТ                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("subscript")

        t5 = section_title("Долен индекс и коефициент")
        self.play(Write(t5), run_time=0.8)

        # H2O big
        h2o = MathTex(r"H_2 O", font_size=110, color=WHITE2).shift(UP*0.3)
        self.play(Write(h2o), run_time=1.0)

        # Annotations
        sub_arrow = Arrow(start=DOWN*2.0+LEFT*1.3, end=h2o.get_bottom()+RIGHT*0.0+DOWN*0.05,
                          stroke_width=2.5, color=YELLOW, buff=0.1)
        sub_lbl = Text("долен индекс = број атоми", font_size=22, color=YELLOW)
        sub_lbl.next_to(sub_arrow.get_start(), DOWN, buff=0.1)

        self.play(GrowArrow(sub_arrow), Write(sub_lbl), run_time=0.9)
        self.wait(0.5)

        two_h2o = MathTex(r"2\, H_2 O", font_size=90, color=WHITE2).move_to(h2o)
        self.play(Transform(h2o, two_h2o), run_time=0.9)

        coef_arrow = Arrow(start=UP*1.8+LEFT*3.0, end=h2o.get_left()+LEFT*0.05+UP*0.1,
                            stroke_width=2.5, color=ORANGE, buff=0.1)
        coef_lbl = Text("коефициент = број молекули",
                        font_size=22, color=ORANGE)
        coef_lbl.next_to(coef_arrow.get_start(), UP, buff=0.1)

        self.play(GrowArrow(coef_arrow), Write(coef_lbl), run_time=0.9)
        self.wait(0.5)

        sum_line = Text("2 H₂O → 4 H + 2 O вкупно.",
                        font_size=28, color=GREEN).to_edge(DOWN, buff=0.4)
        self.play(Write(sum_line), run_time=1.1)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t5, h2o, sub_arrow, sub_lbl,
                                  coef_arrow, coef_lbl, sum_line)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CO vs Co                                       ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("careful")

        t6 = section_title("CO не е Co", color=RED)
        self.play(Write(t6), run_time=0.8)

        left_box = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.2,
                                     fill_color=DARK_CARD, fill_opacity=1,
                                     stroke_color=BLUE, stroke_width=2).shift(LEFT*3.2 + DOWN*0.3)
        co_big = Text("CO", font_size=72, color=BLUE, weight=BOLD).move_to(left_box.get_center()+UP*0.4)
        co_lbl = Text("јаглерод-моноксид", font_size=22, color=WHITE2).next_to(co_big, DOWN, buff=0.3)
        co_note = Text("соединение", font_size=20, color=GREY).next_to(co_lbl, DOWN, buff=0.15)

        right_box = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.2,
                                      fill_color=DARK_CARD, fill_opacity=1,
                                      stroke_color=ORANGE, stroke_width=2).shift(RIGHT*3.2 + DOWN*0.3)
        co2_big = Text("Co", font_size=72, color=ORANGE, weight=BOLD).move_to(right_box.get_center()+UP*0.4)
        co2_lbl = Text("кобалт", font_size=22, color=WHITE2).next_to(co2_big, DOWN, buff=0.3)
        co2_note = Text("елемент", font_size=20, color=GREY).next_to(co2_lbl, DOWN, buff=0.15)

        self.play(FadeIn(left_box), Write(co_big), run_time=0.7)
        self.play(Write(co_lbl), Write(co_note), run_time=0.6)
        self.play(FadeIn(right_box), Write(co2_big), run_time=0.7)
        self.play(Write(co2_lbl), Write(co2_note), run_time=0.6)

        warn = Text("Една мала буква — две различни супстанци.",
                    font_size=26, color=RED).to_edge(DOWN, buff=0.4)
        self.play(Write(warn), run_time=1.2)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t6, left_box, co_big, co_lbl, co_note,
                                  right_box, co2_big, co2_lbl, co2_note, warn)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        f1 = Text("Без зборови.", font_size=46, color=YELLOW, weight=BOLD).move_to(UP*1.0)
        f2 = Text("Без преводи.", font_size=46, color=YELLOW, weight=BOLD).move_to(ORIGIN)
        f3 = Text("Симболи.", font_size=52, color=GREEN, weight=BOLD).move_to(DOWN*1.2)

        self.play(Write(f1), run_time=0.8)
        self.play(Write(f2), run_time=0.8)
        self.play(Write(f3), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(f1, f2, f3)), run_time=0.7)
        self.wait(0.3)
