"""
chem8-3-5  —  Прости супстанци, соединенија и смеси
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: pure vs mixed, three lanes,
nature as character. One-word finishers.
Render:  manim -ql chem8-3-5.py Chem835Scene
Output:  media/videos/chem8-3-5/480p15/Chem835Scene.mp4
"""
from manim import *
import numpy as np
import random

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


def particle(pos, color, r=0.18):
    return Circle(radius=r, fill_color=color, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1).move_to(pos)


class Chem835Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Чистата супстанца има еден состав.",
                  font_size=38, color=YELLOW, weight=BOLD)
        h1.move_to(UP*1.5)
        h2 = Text("Секаде. Секогаш.",
                  font_size=34, color=WHITE2).next_to(h1, DOWN, buff=0.4)
        self.play(Write(h1), run_time=1.2)
        self.play(Write(h2), run_time=0.8)
        self.wait(0.5)

        h3 = Text("Смесата — се менува.",
                  font_size=38, color=ORANGE, weight=BOLD).move_to(DOWN*0.7)
        self.play(Write(h3), run_time=1.0)
        self.wait(0.3)

        h4 = Text("Како луѓе.", font_size=34, color=WHITE2)
        h5 = Text("Како животот.", font_size=34, color=GREEN, weight=BOLD)
        beats = VGroup(h4, h5).arrange(DOWN, buff=0.3).move_to(DOWN*2.4)
        self.play(Write(h4), run_time=0.7)
        self.play(Write(h5), run_time=0.9)
        self.wait(1.3)

        self.play(FadeOut(VGroup(h1, h2, h3, h4, h5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ТРИ ПАТЕКИ                                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_lanes")

        t2 = section_title("Три вида супстанци")
        self.play(Write(t2), run_time=0.8)

        # Lane: pure element
        b1 = RoundedRectangle(width=4.0, height=4.5, corner_radius=0.2,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=BLUE, stroke_width=2.5).shift(LEFT*4.5 + DOWN*0.2)
        l1 = Text("Проста супстанца", font_size=24, color=BLUE, weight=BOLD)
        l1.move_to(b1.get_top()+DOWN*0.4)
        # all same particles
        ones = VGroup()
        for i in range(12):
            x = random.uniform(-1.3, 1.3); y = random.uniform(-1.0, 0.8)
            ones.add(particle(b1.get_center() + np.array([x, y, 0]) + DOWN*0.1, BLUE))
        ex1 = MathTex(r"O_2,\, Fe", font_size=30, color=WHITE2).next_to(b1.get_bottom(), UP, buff=0.3)

        # Lane: compound
        b2 = RoundedRectangle(width=4.0, height=4.5, corner_radius=0.2,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=YELLOW, stroke_width=2.5).shift(DOWN*0.2)
        l2 = Text("Соединение", font_size=24, color=YELLOW, weight=BOLD)
        l2.move_to(b2.get_top()+DOWN*0.4)
        # H2O molecules (groups)
        twos = VGroup()
        for i in range(5):
            x = random.uniform(-1.0, 1.0); y = random.uniform(-0.8, 0.6)
            base = b2.get_center() + np.array([x, y, 0]) + DOWN*0.1
            o = particle(base, RED, r=0.22)
            h1p = particle(base + LEFT*0.3 + UP*0.2, BLUE, r=0.13)
            h2p = particle(base + RIGHT*0.3 + UP*0.2, BLUE, r=0.13)
            twos.add(VGroup(o, h1p, h2p))
        ex2 = MathTex(r"H_2 O,\, NaCl", font_size=30, color=WHITE2).next_to(b2.get_bottom(), UP, buff=0.3)

        # Lane: mixture
        b3 = RoundedRectangle(width=4.0, height=4.5, corner_radius=0.2,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=GREEN, stroke_width=2.5).shift(RIGHT*4.5 + DOWN*0.2)
        l3 = Text("Смеса", font_size=24, color=GREEN, weight=BOLD)
        l3.move_to(b3.get_top()+DOWN*0.4)
        threes = VGroup()
        colors_mix = [BLUE, RED, YELLOW, GREEN, ORANGE]
        for i in range(14):
            x = random.uniform(-1.3, 1.3); y = random.uniform(-1.0, 0.8)
            threes.add(particle(b3.get_center() + np.array([x, y, 0]) + DOWN*0.1,
                                random.choice(colors_mix)))
        ex3 = Text("воздух, морска вода", font_size=22, color=WHITE2).next_to(b3.get_bottom(), UP, buff=0.3)

        self.play(FadeIn(b1), Write(l1), run_time=0.5)
        self.play(FadeIn(ones), Write(ex1), run_time=0.7)
        self.play(FadeIn(b2), Write(l2), run_time=0.5)
        self.play(FadeIn(twos), Write(ex2), run_time=0.7)
        self.play(FadeIn(b3), Write(l3), run_time=0.5)
        self.play(FadeIn(threes), Write(ex3), run_time=0.7)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t2, b1, l1, ones, ex1,
                                  b2, l2, twos, ex2,
                                  b3, l3, threes, ex3)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  СПОРЕДБА                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        t3 = section_title("Споредба")
        self.play(Write(t3), run_time=0.8)

        headers = ["Карактеристика", "Прост", "Соединение", "Смеса"]
        rows = [
            ("Чиста?", "Да", "Да", "Не"),
            ("Точен сооднос?", "—", "Да", "Не"),
            ("Разделување", "—", "хемија", "физички"),
            ("Нови својства?", "—", "Да", "Не"),
        ]

        col_x = [-5.5, -1.8, 1.4, 4.5]
        header_y = 1.8
        h_objs = VGroup()
        for i, h in enumerate(headers):
            color = (YELLOW if i == 0 else
                     (BLUE if i == 1 else (YELLOW if i == 2 else GREEN)))
            t = Text(h, font_size=22, color=color, weight=BOLD).move_to(np.array([col_x[i], header_y, 0]))
            h_objs.add(t)
        self.play(Write(h_objs), run_time=0.8)

        for r_idx, row in enumerate(rows):
            row_y = header_y - 0.7 - r_idx*0.65
            for c_idx, val in enumerate(row):
                color = WHITE2 if c_idx == 0 else GREY
                if val == "Да": color = GREEN
                if val == "Не": color = RED
                t = Text(val, font_size=20, color=color).move_to(np.array([col_x[c_idx], row_y, 0]))
                self.play(FadeIn(t, shift=UP*0.1), run_time=0.18)

        self.wait(2.0)
        # Clean by camera scrub
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ХОМОГЕНИ vs ХЕТЕРОГЕНИ                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("homo_hetero")

        t4 = section_title("Хомогена или хетерогена?")
        self.play(Write(t4), run_time=0.8)

        # Homogeneous: salt water
        b_h = RoundedRectangle(width=5.5, height=4.0, corner_radius=0.2,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=2.5).shift(LEFT*3.2 + DOWN*0.3)
        l_h = Text("Хомогена", font_size=26, color=BLUE, weight=BOLD)
        l_h.move_to(b_h.get_top()+DOWN*0.4)
        # uniform color sea
        water = RoundedRectangle(width=4.5, height=2.0, corner_radius=0.1,
                                  fill_color=BLUE, fill_opacity=0.4,
                                  stroke_color=BLUE, stroke_width=1).move_to(b_h.get_center()+DOWN*0.1)
        eg_h = Text("солена вода, кафе, воздух", font_size=20, color=WHITE2).move_to(b_h.get_bottom()+UP*0.3)

        # Heterogeneous: rocks + sand visible chunks
        b_x = RoundedRectangle(width=5.5, height=4.0, corner_radius=0.2,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=ORANGE, stroke_width=2.5).shift(RIGHT*3.2 + DOWN*0.3)
        l_x = Text("Хетерогена", font_size=26, color=ORANGE, weight=BOLD)
        l_x.move_to(b_x.get_top()+DOWN*0.4)
        # visible chunks of different sizes/colors
        chunks = VGroup()
        for i in range(15):
            x = random.uniform(-1.8, 1.8); y = random.uniform(-0.9, 0.6)
            r = random.uniform(0.08, 0.22)
            color = random.choice([ORANGE, GREY, YELLOW, GREEN])
            c = Circle(radius=r, fill_color=color, fill_opacity=0.9,
                       stroke_color=WHITE2, stroke_width=0.5).move_to(b_x.get_center()+np.array([x,y,0])+DOWN*0.1)
            chunks.add(c)
        eg_x = Text("салата, муслици, песок", font_size=20, color=WHITE2).move_to(b_x.get_bottom()+UP*0.3)

        self.play(FadeIn(b_h), Write(l_h), FadeIn(water), Write(eg_h), run_time=0.9)
        self.play(FadeIn(b_x), Write(l_x), FadeIn(chunks), Write(eg_x), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t4, b_h, l_h, water, eg_h, b_x, l_x, chunks, eg_x)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ПРИМЕРИ ОД ЖИВОТ                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("life")

        t5 = section_title("Од секојдневие")
        self.play(Write(t5), run_time=0.8)

        def card(name, kind, color, pos):
            box = RoundedRectangle(width=4.0, height=2.0, corner_radius=0.18,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2)
            n = Text(name, font_size=26, color=WHITE2, weight=BOLD)
            k = Text(kind, font_size=20, color=color)
            inner = VGroup(n, k).arrange(DOWN, buff=0.2).move_to(box)
            return VGroup(box, inner).move_to(pos)

        c1 = card("злато", "проста супстанца", YELLOW, LEFT*4.2 + UP*1.5)
        c2 = card("вода (H₂O)", "соединение", BLUE, ORIGIN + UP*1.5)
        c3 = card("воздух", "смеса (хомогена)", GREEN, RIGHT*4.2 + UP*1.5)
        c4 = card("кислород (O₂)", "проста супстанца", BLUE, LEFT*4.2 + DOWN*1.5)
        c5 = card("сол (NaCl)", "соединение", YELLOW, ORIGIN + DOWN*1.5)
        c6 = card("морска вода", "смеса", ORANGE, RIGHT*4.2 + DOWN*1.5)

        cards = VGroup(c1, c2, c3, c4, c5, c6)
        self.play(LaggedStartMap(lambda m: FadeIn(m, shift=UP*0.2),
                                  cards, lag_ratio=0.12), run_time=2.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t5, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ВОЗДУХ — кратка приказна                       ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("air")

        t6 = section_title("Воздухот — смеса, не соединение")
        self.play(Write(t6), run_time=0.8)

        # Pie-ish bar: 78% N2, 21% O2, 1% other
        bar = RoundedRectangle(width=10.0, height=1.4, corner_radius=0.1,
                                fill_color=DARK_CARD, fill_opacity=0.6,
                                stroke_color=WHITE2, stroke_width=1).move_to(UP*0.3)
        # segments
        n2_seg = Rectangle(width=10.0*0.78, height=1.4,
                            fill_color=BLUE, fill_opacity=0.85,
                            stroke_width=0)
        o2_seg = Rectangle(width=10.0*0.21, height=1.4,
                            fill_color=GREEN, fill_opacity=0.85,
                            stroke_width=0)
        other_seg = Rectangle(width=10.0*0.01, height=1.4,
                               fill_color=ORANGE, fill_opacity=0.9,
                               stroke_width=0)
        # align left
        left_edge = bar.get_left()
        n2_seg.move_to(left_edge + RIGHT*(10.0*0.78/2))
        o2_seg.move_to(left_edge + RIGHT*(10.0*0.78 + 10.0*0.21/2))
        other_seg.move_to(left_edge + RIGHT*(10.0*0.99 + 10.0*0.01/2))

        self.play(FadeIn(bar), run_time=0.4)
        self.play(GrowFromEdge(n2_seg, LEFT), run_time=0.8)
        self.play(GrowFromEdge(o2_seg, LEFT), run_time=0.6)
        self.play(GrowFromEdge(other_seg, LEFT), run_time=0.4)

        legend = VGroup(
            VGroup(Square(side_length=0.25, fill_color=BLUE, fill_opacity=0.85, stroke_width=0),
                   Text("78% N₂", font_size=22, color=WHITE2)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.25, fill_color=GREEN, fill_opacity=0.85, stroke_width=0),
                   Text("21% O₂", font_size=22, color=WHITE2)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.25, fill_color=ORANGE, fill_opacity=0.9, stroke_width=0),
                   Text("1% CO₂, Ar, H₂O", font_size=22, color=WHITE2)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(bar, DOWN, buff=0.5)
        for l in legend:
            self.play(FadeIn(l, shift=RIGHT*0.2), run_time=0.4)

        msg = Text("Сооднос варира. Затоа смеса.",
                   font_size=26, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(msg), run_time=1.1)
        self.wait(1.4)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        c1f = Text("Чиста.", font_size=44, color=BLUE, weight=BOLD).move_to(UP*1.0)
        c2f = Text("Соединета.", font_size=44, color=YELLOW, weight=BOLD).move_to(ORIGIN)
        c3f = Text("Помешана.", font_size=54, color=GREEN, weight=BOLD).move_to(DOWN*1.2)

        self.play(Write(c1f), run_time=0.7)
        self.play(Write(c2f), run_time=0.7)
        self.play(Write(c3f), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(c1f, c2f, c3f)), run_time=0.7)
        self.wait(0.3)
