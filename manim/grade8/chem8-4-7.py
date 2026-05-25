"""
chem8-4-7  —  Рѓосување и заштита од корозија
Хемија 8, Единица 4: Киселини, бази и соли (продолжение)

Teaching narrative — Andonovski-style: three-beat punches,
iron as a crying character, zinc as sacrifice, one-word finishers.
Render:  manim -ql chem8-4-7.py Chem847Scene
Output:  media/videos/chem8-4-7/480p15/Chem847Scene.mp4
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
RUST    = "#b85c2e"


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


class Chem847Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Железото плаче.", font_size=46, color=GREY, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.4)

        beats = VGroup(
            Text("Со вода.", font_size=34, color=BLUE),
            Text("Со кислород.", font_size=34, color=YELLOW),
            Text("Со време.", font_size=34, color=ORANGE),
        ).arrange(DOWN, buff=0.3).move_to(UP*0.1)
        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
            self.wait(0.2)
        self.wait(0.4)

        result = Text("Резултат — рѓа.", font_size=36, color=RUST, weight=BOLD).move_to(DOWN*1.4)
        self.play(Write(result), run_time=0.9)
        self.wait(0.5)

        butt = Text("Но има начин.", font_size=30, color=WHITE2).to_edge(DOWN, buff=1.1)
        sac  = Text("Цинкот се жртвува.", font_size=30, color=GREEN, weight=BOLD).to_edge(DOWN, buff=0.6)
        live = Text("За железото да живее.", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.15)
        self.play(Write(butt), run_time=0.8)
        self.play(Write(sac), run_time=0.8)
        self.play(Write(live), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats, result, butt, sac, live)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е РЃОСУВАЊЕ                                 ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("what_is_rust")

        t2 = section_title("Што е рѓосување?")
        self.play(Write(t2), run_time=0.8)

        defn = callout("Рѓосување — бавна реакција на железо со вода и кислород.",
                       width=12.5, font_size=26)
        defn.next_to(t2, DOWN, buff=0.4)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)
        self.wait(0.5)

        # Equation
        eq = MathTex(
            r"\text{Fe}", r"+", r"\text{O}_2", r"+", r"\text{H}_2\text{O}",
            r"\rightarrow",
            r"\text{Fe}_2\text{O}_3 \cdot x\text{H}_2\text{O}",
            font_size=42,
        )
        eq[0].set_color(GREY)
        eq[2].set_color(YELLOW)
        eq[4].set_color(BLUE)
        eq[5].set_color(WHITE2)
        eq[6].set_color(RUST)
        eq.move_to(ORIGIN + DOWN*0.2)
        self.play(Write(eq), run_time=2.2)
        self.wait(0.6)

        legend = VGroup(
            Text("Fe = железо", font_size=22, color=GREY),
            Text("O₂ = кислород", font_size=22, color=YELLOW),
            Text("H₂O = вода", font_size=22, color=BLUE),
            Text("Fe₂O₃·xH₂O = рѓа", font_size=22, color=RUST, weight=BOLD),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(legend, shift=UP*0.2), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, defn, eq, legend)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ТРИ СОСТОЈБИ — ЕКСПЕРИМЕНТ                      ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_tests")

        t3 = section_title("Три ексери — три услови")
        self.play(Write(t3), run_time=0.8)

        sub = Text("Кога рѓоса? Кога не?", font_size=26, color=WHITE2)
        sub.next_to(t3, DOWN, buff=0.25)
        self.play(Write(sub), run_time=0.8)
        self.wait(0.3)

        def tube_setup(condition, result_color, result_text, ex_color):
            body = RoundedRectangle(width=1.4, height=3.2, corner_radius=0.3,
                                    fill_color=DARK_CARD, fill_opacity=0.7,
                                    stroke_color=WHITE2, stroke_width=2)
            nail = Rectangle(width=0.18, height=1.6, fill_color=ex_color,
                             fill_opacity=1, stroke_color=WHITE2, stroke_width=1)
            head = Circle(radius=0.18, fill_color=ex_color, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1)
            head.next_to(nail, UP, buff=-0.05)
            nail_group = VGroup(nail, head).move_to(body.get_center() + UP*0.2)
            cond = Text(condition, font_size=18, color=WHITE2)
            cond.next_to(body, UP, buff=0.15)
            res = Text(result_text, font_size=20, color=result_color, weight=BOLD)
            res.next_to(body, DOWN, buff=0.25)
            return VGroup(body, nail_group, cond, res)

        ts1 = tube_setup("вода + воздух", RUST, "рѓоса", RUST).shift(LEFT*4.2 + DOWN*0.3)
        ts2 = tube_setup("само вода", GREEN, "не рѓоса", GREY).shift(DOWN*0.3)
        ts3 = tube_setup("само воздух", GREEN, "не рѓоса", GREY).shift(RIGHT*4.2 + DOWN*0.3)

        for ts in (ts1, ts2, ts3):
            self.play(FadeIn(ts, shift=UP*0.2), run_time=0.7)
        self.wait(0.6)

        # Highlight winner (ts1)
        glow = SurroundingRectangle(ts1, color=RUST, buff=0.2, stroke_width=3)
        self.play(Create(glow), run_time=0.8)
        self.wait(0.6)

        verdict = callout("Без двата — нема рѓа. Со двата — пропаст.",
                          width=12.0, font_size=26, border=RUST)
        verdict.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(verdict, shift=UP*0.2), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, sub, ts1, ts2, ts3, glow, verdict)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  МЕТОДИ ЗА ЗАШТИТА                               ~38 s
        # ══════════════════════════════════════════════════════════
        self.next_section("protection")

        t4 = section_title("Како се штити железото?")
        self.play(Write(t4), run_time=0.8)

        def method_card(title_text, sub_text, color):
            box = RoundedRectangle(width=4.0, height=1.8, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            ttl = Text(title_text, font_size=24, color=color, weight=BOLD)
            sub = Text(sub_text, font_size=18, color=WHITE2)
            inner = VGroup(ttl, sub).arrange(DOWN, buff=0.18).move_to(box)
            return VGroup(box, inner)

        m1 = method_card("Боење",        "слој фарба — нема воздух",     BLUE)
        m2 = method_card("Поцинкување",  "цинк ја крие железото",        GREEN)
        m3 = method_card("Подмачкување", "масло го затвора",              YELLOW)
        m4 = method_card("Жртвена анода","цинкот рѓа наместо железото",  ORANGE)
        m5 = method_card("Нерѓосувачки челик", "Fe + Cr + Ni = легура",   PURPLE)

        row1 = VGroup(m1, m2, m3).arrange(RIGHT, buff=0.35).shift(UP*0.6)
        row2 = VGroup(m4, m5).arrange(RIGHT, buff=0.35).shift(DOWN*1.5)

        for m in (m1, m2, m3, m4, m5):
            self.play(FadeIn(m, shift=UP*0.2), run_time=0.55)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t4, m1, m2, m3, m4, m5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ЖРТВЕНА АНОДА — ЗООМ                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sacrificial")

        t5 = section_title("Жртвената анода")
        self.play(Write(t5), run_time=0.8)

        # Iron pipe + zinc block
        pipe = Rectangle(width=6.0, height=0.7, fill_color=GREY, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1.5).shift(DOWN*0.2)
        pipe_lbl = Text("железна цевка (Fe)", font_size=22, color=WHITE2).next_to(pipe, UP, buff=0.15)

        zinc = Rectangle(width=0.9, height=0.9, fill_color=GREEN, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1.5).next_to(pipe, DOWN, buff=0.7)
        zinc_lbl = Text("цинк (Zn)", font_size=20, color=GREEN, weight=BOLD).next_to(zinc, DOWN, buff=0.15)

        wire = Line(pipe.get_bottom() + DOWN*0.05, zinc.get_top() + UP*0.05,
                    color=YELLOW, stroke_width=2.5)

        self.play(FadeIn(pipe), Write(pipe_lbl), run_time=0.8)
        self.play(FadeIn(zinc, shift=UP*0.2), Write(zinc_lbl), Create(wire), run_time=0.9)
        self.wait(0.5)

        # Show zinc shrinking
        sacrifice = Text("Цинкот се троши. Железото живее.",
                         font_size=28, color=ORANGE, weight=BOLD)
        sacrifice.to_edge(DOWN, buff=0.4)
        self.play(zinc.animate.stretch_to_fit_height(0.55).set_fill(opacity=0.7),
                  Write(sacrifice), run_time=1.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, pipe, pipe_lbl, zinc, zinc_lbl,
                                  wire, sacrifice)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CLOSER                                          ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Рѓата не прости.", font_size=42, color=RUST, weight=BOLD)
        close1.move_to(UP*0.7)
        self.play(Write(close1), run_time=1.0)
        self.wait(0.3)

        close2 = Text("Но науката не седи.", font_size=42, color=YELLOW, weight=BOLD)
        close2.move_to(ORIGIN)
        self.play(Write(close2), run_time=1.0)
        self.wait(0.3)

        close3 = Text("Штити.", font_size=50, color=GREEN, weight=BOLD)
        close3.move_to(DOWN*0.9)
        self.play(Write(close3), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(close1, close2, close3)), run_time=0.7)
        self.wait(0.3)
