"""
chem8-2-4  —  Метали и легури
Хемија 8, Единица 2: Материјали околу нас

Teaching narrative — Andonovski-style: three-beat punches,
metals as characters who join into stronger alloys, не...туку, finishers.
Render:  manim -ql chem8-2-4.py Chem824Scene
Output:  media/videos/chem8-2-4/480p15/Chem824Scene.mp4
"""
from manim import *
import numpy as np
import random

config.background_color = "#0d1b2e"

BLUE      = "#4fc3f7"
YELLOW    = "#ffd54f"
GREEN     = "#81c784"
RED       = "#e57373"
GREY      = "#90a4ae"
ORANGE    = "#ffb74d"
PURPLE    = "#ce93d8"
WHITE2    = "#e8eaf0"
DARK_CARD = "#0f2233"

COPPER    = "#c87533"
TIN       = "#c0c0c0"
ZINC      = "#a8a8a8"
IRON      = "#5a6f8a"
CARBON    = "#2b2b2b"
CHROMIUM  = "#c5d3e0"


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


def atom(pos, color, r=0.22):
    return Circle(radius=r, fill_color=color, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1.5).move_to(pos)


class Chem824Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Чистиот бакар е мек.",
                  font_size=42, color=COPPER, weight=BOLD)
        h2 = Text("Чистиот калај е кршлив.",
                  font_size=42, color=TIN, weight=BOLD)
        h1.move_to(UP * 1.9)
        h2.next_to(h1, DOWN, buff=0.35)

        self.play(Write(h1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.5)

        line2 = Text("Заедно — бронза.",
                     font_size=42, color=ORANGE, weight=BOLD)
        line2.next_to(h2, DOWN, buff=0.5)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.3)

        line3 = Text("Силна.",
                     font_size=40, color=YELLOW, weight=BOLD)
        line3.next_to(line2, DOWN, buff=0.35)
        self.play(Write(line3), run_time=0.9)
        self.wait(0.4)

        line4 = Text("Не случајно историјата има Бронзено доба.",
                     font_size=28, color=WHITE2)
        line4.next_to(line3, DOWN, buff=0.35)
        self.play(Write(line4), run_time=1.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(h1, h2, line2, line3, line4)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                       ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е легура?")
        self.play(Write(t2), run_time=0.9)

        d1 = callout(
            "Легура = смеса од два или повеќе метали.",
            width=11.5, font_size=28,
        )
        d1.next_to(t2, DOWN, buff=0.7)
        self.play(FadeIn(d1), run_time=0.8)
        self.wait(0.5)

        d2 = Text("Понекогаш — метал + неметал. (на пр. железо + јаглерод)",
                  font_size=26, color=WHITE2)
        d2.next_to(d1, DOWN, buff=0.5)
        self.play(Write(d2), run_time=1.4)
        self.wait(0.4)

        d3 = Text("Цел: подобри својства.", font_size=34, color=YELLOW, weight=BOLD)
        d3.next_to(d2, DOWN, buff=0.5)
        self.play(Write(d3), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, d1, d2, d3)))

        # ══════════════════════════════════════════════════════════
        # 3.  МЕХАНИЗАМ — чист метал vs легура                 ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("lattice_mechanism")

        t3 = section_title("Што се случува внатре?")
        self.play(Write(t3), run_time=0.9)

        # Two panels side by side
        pure_panel = RoundedRectangle(
            width=5.6, height=4.5, corner_radius=0.22,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=COPPER, stroke_width=3,
        ).move_to(LEFT*3.4 + DOWN*0.4)
        alloy_panel = RoundedRectangle(
            width=5.6, height=4.5, corner_radius=0.22,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=3,
        ).move_to(RIGHT*3.4 + DOWN*0.4)

        pure_title = Text("Чист бакар", font_size=26, color=COPPER, weight=BOLD)
        pure_title.next_to(pure_panel.get_top(), DOWN, buff=0.2)
        alloy_title = Text("Бронза (Cu + Sn)", font_size=26, color=YELLOW, weight=BOLD)
        alloy_title.next_to(alloy_panel.get_top(), DOWN, buff=0.2)

        self.play(FadeIn(pure_panel), FadeIn(alloy_panel),
                  Write(pure_title), Write(alloy_title), run_time=1.0)

        # Pure lattice — regular grid of copper
        pure_atoms = VGroup()
        for i in range(5):
            for j in range(5):
                a = atom(pure_panel.get_center() + np.array([
                    -1.6 + j*0.8, -1.4 + i*0.66, 0]),
                    color=COPPER, r=0.22)
                pure_atoms.add(a)
        self.play(FadeIn(pure_atoms), run_time=0.9)
        self.wait(0.3)

        # Alloy lattice — copper with random tin atoms (larger, different color)
        random.seed(11)
        alloy_atoms = VGroup()
        tin_positions = {(1,2), (2,4), (3,1), (4,3), (0,3), (2,0)}
        for i in range(5):
            for j in range(5):
                pos = alloy_panel.get_center() + np.array([
                    -1.6 + j*0.8, -1.4 + i*0.66, 0])
                if (i, j) in tin_positions:
                    a = atom(pos, color=TIN, r=0.28)
                else:
                    a = atom(pos, color=COPPER, r=0.22)
                alloy_atoms.add(a)
        self.play(FadeIn(alloy_atoms), run_time=0.9)
        self.wait(0.4)

        # Slip arrow in pure (easy) — atoms slide
        slip_pure = Arrow(start=LEFT*0.8, end=RIGHT*0.8, color=GREEN,
                          stroke_width=4, buff=0.05)
        slip_pure.move_to(pure_panel.get_center() + DOWN*1.9)
        slip_lab_pure = Text("лизга — мек",
                             font_size=22, color=GREEN, weight=BOLD)
        slip_lab_pure.next_to(slip_pure, DOWN, buff=0.1)
        self.play(GrowArrow(slip_pure), Write(slip_lab_pure), run_time=0.9)
        self.wait(0.3)

        # Blocked in alloy
        block_x = Cross(stroke_color=RED, stroke_width=6, scale_factor=0.5)
        block_x.move_to(alloy_panel.get_center() + DOWN*1.9)
        block_lab = Text("блокирани — цврст",
                         font_size=22, color=RED, weight=BOLD)
        block_lab.next_to(block_x, DOWN, buff=0.1)
        self.play(Create(block_x), Write(block_lab), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, pure_panel, alloy_panel, pure_title,
                                  alloy_title, pure_atoms, alloy_atoms,
                                  slip_pure, slip_lab_pure,
                                  block_x, block_lab)))

        # ══════════════════════════════════════════════════════════
        # 4.  ГАЛЕРИЈА — 4 легури                              ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("gallery")

        t4 = section_title("Четири легури. Четири улоги.")
        self.play(Write(t4), run_time=0.9)

        def alloy_card(name, formula, use, c1_color, c2_color, pos):
            box = RoundedRectangle(
                width=5.6, height=2.8, corner_radius=0.22,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=YELLOW, stroke_width=2,
            ).move_to(pos)
            nm = Text(name, font_size=28, color=YELLOW, weight=BOLD)
            nm.move_to(box.get_center() + UP*0.95)

            # Two atom circles + plus sign
            a1 = Circle(radius=0.32, fill_color=c1_color, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=2)
            a1.move_to(box.get_center() + LEFT*1.6 + UP*0.0)
            a2 = Circle(radius=0.32, fill_color=c2_color, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=2)
            a2.move_to(box.get_center() + LEFT*0.6 + UP*0.0)
            plus = Text("+", font_size=32, color=WHITE2, weight=BOLD)
            plus.move_to(box.get_center() + LEFT*1.1 + UP*0.0)

            fr = MathTex(formula, color=WHITE2, font_size=30)
            fr.move_to(box.get_center() + RIGHT*1.3 + UP*0.0)

            us = Text(use, font_size=20, color=WHITE2)
            us.move_to(box.get_center() + DOWN*0.85)
            return VGroup(box, nm, a1, a2, plus, fr, us)

        c1 = alloy_card("Бронза", "Cu + Sn", "статуи, ѕвонца",
                        COPPER, TIN, LEFT*3.2 + UP*1.4)
        c2 = alloy_card("Месинг", "Cu + Zn", "инструменти, рачки",
                        COPPER, ZINC, RIGHT*3.2 + UP*1.4)
        c3 = alloy_card("Челик", "Fe + C", "мостови, мотори",
                        IRON, CARBON, LEFT*3.2 + DOWN*1.9)
        c4 = alloy_card("Нерѓ. челик", "Fe + Cr + Ni", "кујна, медицина",
                        IRON, CHROMIUM, RIGHT*3.2 + DOWN*1.9)

        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.play(FadeIn(c3), run_time=0.6)
        self.play(FadeIn(c4), run_time=0.6)
        self.wait(2.4)

        self.play(FadeOut(VGroup(t4, c1, c2, c3, c4)))

        # ══════════════════════════════════════════════════════════
        # 5.  ИСТОРИЈА — лента на времето                      ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("timeline")

        t5 = section_title("Историја — три доба.")
        self.play(Write(t5), run_time=0.9)

        timeline = Line(LEFT*5.5, RIGHT*5.5, color=WHITE2, stroke_width=3)
        timeline.move_to(DOWN*0.4)
        self.play(Create(timeline), run_time=0.9)

        def era_marker(label, year, body, color, x):
            dot = Dot(point=[x, -0.4, 0], color=color, radius=0.12)
            yr = Text(year, font_size=22, color=color, weight=BOLD)
            yr.move_to([x, 0.2, 0])
            nm = Text(label, font_size=24, color=WHITE2, weight=BOLD)
            nm.move_to([x, 0.7, 0])
            bd = Text(body, font_size=18, color=WHITE2)
            bd.move_to([x, -1.0, 0])
            return VGroup(dot, yr, nm, bd)

        e1 = era_marker("Каменото доба", "≈ 2.5M пр.н.е.",
                        "камен, дрво", GREY, -5.0)
        e2 = era_marker("Бронзено доба", "≈ 3300 пр.н.е.",
                        "Cu + Sn → бронза", COPPER, -1.5)
        e3 = era_marker("Железно доба", "≈ 1200 пр.н.е.",
                        "Fe, потоа челик", IRON, 2.0)
        e4 = era_marker("Денеска", "21. век",
                        ">1000 легури", YELLOW, 5.2)

        for e in [e1, e2, e3, e4]:
            self.play(FadeIn(e), run_time=0.55)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t5, timeline, e1, e2, e3, e4)))

        # ══════════════════════════════════════════════════════════
        # 6.  СОВРЕМЕНО — три современи легури                 ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("modern")

        t6 = section_title("Денеска — легури со памет.")
        self.play(Write(t6), run_time=0.9)

        def modern_card(title, body, color, pos):
            box = RoundedRectangle(
                width=4.0, height=3.2, corner_radius=0.22,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            ).move_to(pos)
            tt = Text(title, font_size=24, color=color, weight=BOLD)
            tt.next_to(box.get_top(), DOWN, buff=0.25)
            bb = Text(body, font_size=20, color=WHITE2)
            bb.move_to(box.get_center() + DOWN*0.15)
            return VGroup(box, tt, bb)

        m1 = modern_card("Титаниум", "лесен, цврст.\nимпланти.",
                         BLUE, LEFT*4.4 + DOWN*0.4)
        m2 = modern_card("Нитинол", "паметна форма.\nбрекети, стент.",
                         PURPLE, DOWN*0.4)
        m3 = modern_card("Дуралумин", "Al + Cu + Mg.\nавиони.",
                         GREEN, RIGHT*4.4 + DOWN*0.4)

        self.play(FadeIn(m1), run_time=0.6)
        self.play(FadeIn(m2), run_time=0.6)
        self.play(FadeIn(m3), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t6, m1, m2, m3)))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни.")
        self.play(Write(t7), run_time=0.8)

        b1 = callout("Легура = смеса. Двајца → еден посилен.",
                     width=11.0, border=BLUE, font_size=28)
        b1.move_to(UP*1.6)
        b2 = callout("Бронза, месинг, челик — историја преку легури.",
                     width=11.0, border=COPPER, font_size=28)
        b2.next_to(b1, DOWN, buff=0.35)
        b3 = callout("Различни атоми блокираат лизгање. Цврстина — раѓа.",
                     width=11.0, border=YELLOW, font_size=28)
        b3.next_to(b2, DOWN, buff=0.35)

        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.0)

        finisher = Text("Заедно.", font_size=54, color=YELLOW, weight=BOLD)
        finisher.next_to(b3, DOWN, buff=0.55)
        self.play(Write(finisher), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, b1, b2, b3, finisher)))
        self.wait(0.5)
