"""
chem8-3-3  —  Што е соединение?
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: drama of Na + Cl → NaCl,
elements as characters, new identities, one-word finishers.
Render:  manim -ql chem8-3-3.py Chem833Scene
Output:  media/videos/chem8-3-3/480p15/Chem833Scene.mp4
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


def atom_ball(symbol, color, r=0.55, font_size=26):
    c = Circle(radius=r, fill_color=color, fill_opacity=0.85,
                stroke_color=WHITE2, stroke_width=2)
    s = Text(symbol, font_size=font_size, color=WHITE2, weight=BOLD).move_to(c)
    return VGroup(c, s)


class Chem833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Натриум експлодира во вода.",
                  font_size=38, color=RED, weight=BOLD)
        h2 = Text("Хлор отрова.",
                  font_size=38, color=GREEN, weight=BOLD)
        h3 = Text("Заедно — обична сол.",
                  font_size=38, color=WHITE2, weight=BOLD)
        group = VGroup(h1, h2, h3).arrange(DOWN, buff=0.4).move_to(UP*0.3)

        for h in (h1, h2, h3):
            self.play(Write(h), run_time=0.8)
            self.wait(0.3)
        self.wait(0.4)

        f1 = Text("Хемијата ja прави магијата.",
                  font_size=30, color=YELLOW).move_to(DOWN*2.0)
        f2 = Text("Без волшебници.",
                  font_size=32, color=ORANGE, weight=BOLD).next_to(f1, DOWN, buff=0.3)
        self.play(Write(f1), run_time=1.0)
        self.play(Write(f2), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(group, f1, f2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                      ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е соединение?")
        self.play(Write(t2), run_time=0.8)

        defn = callout("Два или повеќе различни елементи — поврзани во точен сооднос.",
                       width=12.0, font_size=26)
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)

        # 2H + 1O always
        eq = MathTex(r"H_2 O", r"\;:\;", r"2\,H", r"\;+\;", r"1\,O",
                     font_size=64, color=WHITE2).move_to(DOWN*0.4)
        eq[0].set_color(BLUE)
        eq[2].set_color(YELLOW)
        eq[4].set_color(RED)
        self.play(Write(eq), run_time=1.2)
        self.wait(0.6)

        always = Text("Секогаш ист сооднос. Секогаш.",
                      font_size=30, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(always), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t2, defn, eq, always)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  DRAMA: Na + Cl → NaCl                          ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("drama")

        t3 = section_title("Драма во три чина")
        self.play(Write(t3), run_time=0.8)

        # Act 1: Sodium alone
        na = atom_ball("Na", PURPLE, r=0.7, font_size=30).shift(LEFT*3.5 + UP*0.2)
        na_lbl = Text("мек метал", font_size=22, color=WHITE2).next_to(na, DOWN, buff=0.25)
        na_note = Text("реагира експлозивно со вода", font_size=20, color=RED).next_to(na_lbl, DOWN, buff=0.15)

        cl = atom_ball("Cl", GREEN, r=0.7, font_size=30).shift(RIGHT*3.5 + UP*0.2)
        cl_lbl = Text("отровен гас", font_size=22, color=WHITE2).next_to(cl, DOWN, buff=0.25)
        cl_note = Text("зелен. опасен.", font_size=20, color=RED).next_to(cl_lbl, DOWN, buff=0.15)

        self.play(FadeIn(na, shift=UP*0.2), Write(na_lbl), Write(na_note), run_time=1.0)
        self.play(FadeIn(cl, shift=UP*0.2), Write(cl_lbl), Write(cl_note), run_time=1.0)
        self.wait(0.6)

        # Spark/explosion in middle
        spark = Text("⚡", font_size=80, color=YELLOW).move_to(ORIGIN+UP*0.2)
        self.play(FadeIn(spark, scale=1.5), run_time=0.5)
        self.play(
            na.animate.move_to(ORIGIN+UP*0.2+LEFT*0.55),
            cl.animate.move_to(ORIGIN+UP*0.2+RIGHT*0.55),
            FadeOut(spark),
            FadeOut(na_lbl), FadeOut(na_note),
            FadeOut(cl_lbl), FadeOut(cl_note),
            run_time=1.1,
        )

        bond = Line(na.get_right(), cl.get_left(), stroke_color=WHITE2, stroke_width=4)
        self.play(Create(bond), run_time=0.5)

        nacl_grp = VGroup(na, cl, bond)
        nacl_lbl = Text("NaCl — натриум-хлорид",
                        font_size=30, color=WHITE2, weight=BOLD).next_to(nacl_grp, DOWN, buff=0.5)
        salt = Text("обична сол", font_size=26, color=YELLOW).next_to(nacl_lbl, DOWN, buff=0.2)
        safe = Text("безбедна за јадење", font_size=22, color=GREEN).next_to(salt, DOWN, buff=0.15)

        self.play(Write(nacl_lbl), run_time=0.8)
        self.play(Write(salt), Write(safe), run_time=0.9)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t3, nacl_grp, nacl_lbl, salt, safe)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  НОВИ СВОЈСТВА                                  ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("new_props")

        t4 = section_title("Нови својства")
        self.play(Write(t4), run_time=0.8)

        # Table: Na | Cl | NaCl with descriptors
        def col(symbol, color, lines, x):
            box = RoundedRectangle(width=3.8, height=4.2, corner_radius=0.2,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            box.shift(x + DOWN*0.3)
            s = Text(symbol, font_size=48, color=color, weight=BOLD)
            s.move_to(box.get_top()+DOWN*0.6)
            txts = VGroup(*[Text(l, font_size=18, color=WHITE2)
                              for l in lines]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            txts.move_to(box.get_center()+DOWN*0.4)
            return VGroup(box, s, txts)

        c1 = col("Na", PURPLE,
                 ["мек, сјаен метал", "реагира со вода", "експлозивно"],
                 LEFT*4.5)
        c2 = col("Cl", GREEN,
                 ["зелен гас", "отровен", "силна миризба"],
                 ORIGIN)
        c3 = col("NaCl", YELLOW,
                 ["бел кристал", "растворлив", "безбеден"],
                 RIGHT*4.5)

        self.play(FadeIn(c1, shift=UP*0.2), run_time=0.6)
        self.play(FadeIn(c2, shift=UP*0.2), run_time=0.6)
        self.play(FadeIn(c3, shift=UP*0.2), run_time=0.6)
        self.wait(0.8)

        msg = Text("Соединение не наследува. Соединение создава.",
                   font_size=26, color=ORANGE).to_edge(DOWN, buff=0.4)
        self.play(Write(msg), run_time=1.2)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t4, c1, c2, c3, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ЧЕСТИ СОЕДИНЕНИЈА                             ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("examples")

        t5 = section_title("Соединенија околу тебе")
        self.play(Write(t5), run_time=0.8)

        def example_card(formula, name, color, pos):
            box = RoundedRectangle(width=4.0, height=1.7, corner_radius=0.18,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2)
            f = MathTex(formula, font_size=42, color=color)
            n = Text(name, font_size=20, color=WHITE2)
            inner = VGroup(f, n).arrange(DOWN, buff=0.15).move_to(box)
            return VGroup(box, inner).move_to(pos)

        e1 = example_card(r"H_2 O", "вода", BLUE, LEFT*4.3 + UP*1.5)
        e2 = example_card(r"CO_2", "јаглерод-диоксид", GREY, ORIGIN + UP*1.5)
        e3 = example_card(r"NaCl", "трпезна сол", YELLOW, RIGHT*4.3 + UP*1.5)
        e4 = example_card(r"CaCO_3", "варовник", ORANGE, LEFT*4.3 + DOWN*0.5)
        e5 = example_card(r"NH_3", "амонијак", PURPLE, ORIGIN + DOWN*0.5)
        e6 = example_card(r"Fe_2 O_3", "рѓа", RED, RIGHT*4.3 + DOWN*0.5)

        for e in (e1, e2, e3, e4, e5, e6):
            self.play(FadeIn(e, shift=UP*0.15), run_time=0.4)

        msg = Text("Секаде. Дома. Во тебе. Во воздух.",
                   font_size=28, color=GREEN).to_edge(DOWN, buff=0.4)
        self.play(Write(msg), run_time=1.1)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t5, e1, e2, e3, e4, e5, e6, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  СОЕДИНЕНИЕ vs СМЕСА                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vs_mixture")

        t6 = section_title("Соединение не е смеса", color=ORANGE)
        self.play(Write(t6), run_time=0.8)

        # Left: compound H2O — fixed
        left_box = RoundedRectangle(width=5.5, height=4.0, corner_radius=0.2,
                                     fill_color=DARK_CARD, fill_opacity=1,
                                     stroke_color=BLUE, stroke_width=2.5).shift(LEFT*3.2 + DOWN*0.2)
        comp_lbl = Text("Соединение", font_size=28, color=BLUE, weight=BOLD)
        comp_lbl.move_to(left_box.get_top()+DOWN*0.4)
        comp_eq = MathTex(r"H_2 O", font_size=64, color=WHITE2).move_to(left_box.get_center()+UP*0.1)
        comp_note = Text("точен сооднос 2:1", font_size=22, color=GREEN).next_to(comp_eq, DOWN, buff=0.3)
        comp_note2 = Text("се раздели само со реакција", font_size=18, color=GREY).next_to(comp_note, DOWN, buff=0.15)

        # Right: mixture sea water
        right_box = RoundedRectangle(width=5.5, height=4.0, corner_radius=0.2,
                                      fill_color=DARK_CARD, fill_opacity=1,
                                      stroke_color=GREEN, stroke_width=2.5).shift(RIGHT*3.2 + DOWN*0.2)
        mix_lbl = Text("Смеса", font_size=28, color=GREEN, weight=BOLD)
        mix_lbl.move_to(right_box.get_top()+DOWN*0.4)
        mix_eq = Text("вода + сол + ...", font_size=32, color=WHITE2).move_to(right_box.get_center()+UP*0.1)
        mix_note = Text("сооднос менлив", font_size=22, color=ORANGE).next_to(mix_eq, DOWN, buff=0.3)
        mix_note2 = Text("се раздели физички", font_size=18, color=GREY).next_to(mix_note, DOWN, buff=0.15)

        self.play(FadeIn(left_box), Write(comp_lbl), run_time=0.7)
        self.play(Write(comp_eq), Write(comp_note), Write(comp_note2), run_time=0.9)
        self.play(FadeIn(right_box), Write(mix_lbl), run_time=0.7)
        self.play(Write(mix_eq), Write(mix_note), Write(mix_note2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t6, left_box, comp_lbl, comp_eq, comp_note, comp_note2,
                                  right_box, mix_lbl, mix_eq, mix_note, mix_note2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        c1 = Text("Не мешање.", font_size=42, color=GREY, weight=BOLD).move_to(UP*1.0)
        c2 = Text("Не комбинирање.", font_size=42, color=GREY, weight=BOLD).move_to(ORIGIN)
        c3 = Text("Поврзување.", font_size=52, color=YELLOW, weight=BOLD).move_to(DOWN*1.2)

        self.play(Write(c1), run_time=0.7)
        self.play(Write(c2), run_time=0.7)
        self.play(Write(c3), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(c1, c2, c3)), run_time=0.7)
        self.wait(0.3)
