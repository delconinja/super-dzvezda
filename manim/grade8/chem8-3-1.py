"""
chem8-3-1  —  Елементи и атоми
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: three-beat punches,
atoms as characters, personification, one-word finishers.
Render:  manim -ql chem8-3-1.py Chem831Scene
Output:  media/videos/chem8-3-1/480p15/Chem831Scene.mp4
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


def proton(pos, r=0.16):
    return Circle(radius=r, fill_color=RED, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1.2).move_to(pos)


def neutron(pos, r=0.16):
    return Circle(radius=r, fill_color=GREY, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1.2).move_to(pos)


def electron(pos, r=0.10):
    return Circle(radius=r, fill_color=BLUE, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1).move_to(pos)


class Chem831Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Сè на светот е направено од атоми.",
                     font_size=44, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.6)
        self.wait(0.6)

        beats = VGroup(
            Text("Книгата.", font_size=36, color=WHITE2),
            Text("Воздухот.", font_size=36, color=WHITE2),
            Text("Ти.", font_size=36, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
            self.wait(0.25)
        self.wait(0.5)

        small = Text("Тие се толку мали — но без нив, нема ништо.",
                     font_size=30, color=WHITE2).to_edge(DOWN, buff=1.2)
        self.play(Write(small), run_time=1.4)
        self.wait(0.4)
        never = Text("Никогаш.", font_size=38, color=RED, weight=BOLD)
        never.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(never, shift=UP*0.2), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, beats, small, never)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ЕЛЕМЕНТ                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("element")

        t2 = section_title("Што е елемент?")
        self.play(Write(t2), run_time=0.8)

        defn = callout("Елемент = чиста супстанца од еден вид атоми.",
                       width=11.0, font_size=28)
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)
        self.wait(0.4)

        # 118 grid of small element tiles
        tiles = VGroup()
        cols, rows = 14, 8
        for i in range(118):
            r = i // cols
            c = i % cols
            t = Square(side_length=0.32, fill_color=BLUE, fill_opacity=0.6,
                       stroke_color=WHITE2, stroke_width=0.5)
            t.move_to(np.array([(c-cols/2)*0.36, -(r-rows/2)*0.36 - 0.4, 0]))
            tiles.add(t)

        self.play(LaggedStartMap(FadeIn, tiles, lag_ratio=0.01), run_time=2.2)
        count = Text("118 познати елементи.", font_size=30, color=YELLOW)
        count.to_edge(DOWN, buff=0.6)
        self.play(Write(count), run_time=1.0)
        self.wait(1.0)

        self.play(FadeOut(VGroup(t2, defn, tiles, count)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  АТОМ — НАЈМАЛА ЕДИНИЦА                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("atom_smallest")

        t3 = section_title("Атомот — најмалата единица")
        self.play(Write(t3), run_time=0.8)

        # Apple → Earth → atom scale metaphor
        earth = Circle(radius=2.0, fill_color=GREEN, fill_opacity=0.5,
                       stroke_color=BLUE, stroke_width=3).shift(LEFT*3.5 + DOWN*0.3)
        earth_lbl = Text("Земја", font_size=24, color=WHITE2).next_to(earth, DOWN, buff=0.2)

        apple = Circle(radius=0.5, fill_color=RED, fill_opacity=0.9,
                       stroke_color=GREEN, stroke_width=2).shift(RIGHT*0.5 + DOWN*0.3)
        apple_lbl = Text("Јаболко", font_size=24, color=WHITE2).next_to(apple, DOWN, buff=0.2)

        atom_dot = Circle(radius=0.08, fill_color=YELLOW, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1).shift(RIGHT*3.8 + DOWN*0.3)
        atom_lbl = Text("Атом", font_size=24, color=WHITE2).next_to(atom_dot, DOWN, buff=0.2)

        self.play(FadeIn(earth), Write(earth_lbl), run_time=0.7)
        self.play(FadeIn(apple), Write(apple_lbl), run_time=0.6)
        self.play(FadeIn(atom_dot), Write(atom_lbl), run_time=0.6)

        c3 = callout("Ако јаболкото = Земја, атомот = јаболко.",
                     width=11.0, font_size=26)
        c3.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(c3, shift=UP*0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, earth, earth_lbl, apple, apple_lbl,
                                  atom_dot, atom_lbl, c3)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  СТРУКТУРА НА АТОМ                              ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("structure")

        t4 = section_title("Структура на атом")
        self.play(Write(t4), run_time=0.8)

        # Nucleus
        nucleus_pos = ORIGIN + DOWN*0.3
        protons = VGroup(
            proton(nucleus_pos + UP*0.12 + LEFT*0.12),
            proton(nucleus_pos + DOWN*0.12 + RIGHT*0.12),
            proton(nucleus_pos + UP*0.12 + RIGHT*0.18),
        )
        neutrons = VGroup(
            neutron(nucleus_pos + DOWN*0.18 + LEFT*0.10),
            neutron(nucleus_pos + UP*0.20 + LEFT*0.04),
            neutron(nucleus_pos + DOWN*0.05 + RIGHT*0.02),
        )

        # Two orbits
        orbit1 = Circle(radius=1.4, stroke_color=GREY, stroke_width=1.2,
                        fill_opacity=0).move_to(nucleus_pos)
        orbit2 = Circle(radius=2.4, stroke_color=GREY, stroke_width=1.2,
                        fill_opacity=0).move_to(nucleus_pos)

        e1 = electron(nucleus_pos + RIGHT*1.4)
        e2 = electron(nucleus_pos + LEFT*1.4)
        e3 = electron(nucleus_pos + UP*2.4)
        e4 = electron(nucleus_pos + DOWN*2.4)
        e5 = electron(nucleus_pos + RIGHT*2.4)
        e6 = electron(nucleus_pos + LEFT*2.4)

        self.play(FadeIn(protons), FadeIn(neutrons), run_time=0.8)
        nuc_lbl = Text("јадро", font_size=22, color=YELLOW).next_to(neutrons, DOWN, buff=0.05).shift(LEFT*1.5+DOWN*0.5)
        arrow_nuc = Arrow(start=nuc_lbl.get_top()+UP*0.05, end=nucleus_pos+DOWN*0.25,
                          stroke_width=2, color=YELLOW, buff=0.05)
        self.play(Write(nuc_lbl), GrowArrow(arrow_nuc), run_time=0.7)

        self.play(Create(orbit1), Create(orbit2), run_time=0.9)
        self.play(FadeIn(VGroup(e1,e2,e3,e4,e5,e6)), run_time=0.7)

        e_lbl = Text("електрони", font_size=22, color=BLUE).to_corner(UR, buff=0.7).shift(DOWN*1.2)
        self.play(Write(e_lbl), run_time=0.6)

        # Rotate electrons
        e_group_inner = VGroup(e1, e2)
        e_group_outer = VGroup(e3, e4, e5, e6)
        self.play(
            Rotate(e_group_inner, angle=2*PI, about_point=nucleus_pos),
            Rotate(e_group_outer, angle=-2*PI, about_point=nucleus_pos),
            run_time=3.0,
        )

        # Legend
        legend = VGroup(
            VGroup(proton(ORIGIN), Text("протон  +1", font_size=20, color=WHITE2).next_to(ORIGIN, RIGHT, buff=0.15)),
            VGroup(neutron(ORIGIN), Text("неутрон  0", font_size=20, color=WHITE2).next_to(ORIGIN, RIGHT, buff=0.15)),
            VGroup(electron(ORIGIN), Text("електрон  -1", font_size=20, color=WHITE2).next_to(ORIGIN, RIGHT, buff=0.15)),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).to_corner(DL, buff=0.5)
        self.play(FadeIn(legend), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t4, protons, neutrons, orbit1, orbit2,
                                  e1, e2, e3, e4, e5, e6, e_lbl, nuc_lbl,
                                  arrow_nuc, legend)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  АТОМСКИ БРОЈ                                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("atomic_number")

        t5 = section_title("Атомски број Z")
        self.play(Write(t5), run_time=0.8)

        zdef = callout("Z = број на протони. Тоа го дефинира елементот.",
                       width=11.5, font_size=28)
        zdef.next_to(t5, DOWN, buff=0.5)
        self.play(FadeIn(zdef, shift=UP*0.2), run_time=0.9)

        # Three element cards
        def el_card(symbol, name, z, color):
            box = RoundedRectangle(width=2.8, height=2.4, corner_radius=0.2,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            s = Text(symbol, font_size=52, color=color, weight=BOLD)
            n = Text(name, font_size=22, color=WHITE2).next_to(s, DOWN, buff=0.15)
            zt = Text(f"Z = {z}", font_size=22, color=YELLOW).next_to(n, DOWN, buff=0.12)
            inner = VGroup(s, n, zt).move_to(box)
            return VGroup(box, inner)

        c1 = el_card("O", "Кислород", 8, BLUE).shift(LEFT*4.0 + DOWN*0.5)
        c2 = el_card("Fe", "Железо", 26, ORANGE).shift(DOWN*0.5)
        c3 = el_card("Au", "Злато", 79, YELLOW).shift(RIGHT*4.0 + DOWN*0.5)

        for c in (c1, c2, c3):
            self.play(FadeIn(c, shift=UP*0.2), run_time=0.6)
        self.wait(1.0)

        bottom = Text("Промениш протон — друг елемент.",
                      font_size=28, color=GREEN).to_edge(DOWN, buff=0.4)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)

        self.play(FadeOut(VGroup(t5, zdef, c1, c2, c3, bottom)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  АТОМ / ЕЛЕМЕНТ / МОЛЕКУЛА                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        t6 = section_title("Атом, елемент, молекула")
        self.play(Write(t6), run_time=0.8)

        # One H atom
        h_atom = VGroup(
            Circle(radius=0.35, fill_color=BLUE, fill_opacity=0.8,
                   stroke_color=WHITE2, stroke_width=2),
            Text("H", font_size=28, color=WHITE2, weight=BOLD),
        ).shift(LEFT*4.2 + DOWN*0.2)
        h_lbl = Text("атом H", font_size=22, color=WHITE2).next_to(h_atom, DOWN, buff=0.3)

        # H2 molecule
        h2_a = Circle(radius=0.35, fill_color=BLUE, fill_opacity=0.8,
                      stroke_color=WHITE2, stroke_width=2).shift(LEFT*0.4)
        h2_b = Circle(radius=0.35, fill_color=BLUE, fill_opacity=0.8,
                      stroke_color=WHITE2, stroke_width=2).shift(RIGHT*0.4)
        h2_a_l = Text("H", font_size=24, color=WHITE2, weight=BOLD).move_to(h2_a)
        h2_b_l = Text("H", font_size=24, color=WHITE2, weight=BOLD).move_to(h2_b)
        h2 = VGroup(h2_a, h2_b, h2_a_l, h2_b_l).shift(DOWN*0.2)
        h2_lbl = Text("молекула H₂", font_size=22, color=WHITE2).next_to(h2, DOWN, buff=0.3)

        # H2O
        o = Circle(radius=0.45, fill_color=RED, fill_opacity=0.8,
                   stroke_color=WHITE2, stroke_width=2)
        h1a = Circle(radius=0.30, fill_color=BLUE, fill_opacity=0.8,
                     stroke_color=WHITE2, stroke_width=2).shift(LEFT*0.55 + UP*0.45)
        h1b = Circle(radius=0.30, fill_color=BLUE, fill_opacity=0.8,
                     stroke_color=WHITE2, stroke_width=2).shift(RIGHT*0.55 + UP*0.45)
        ol = Text("O", font_size=26, color=WHITE2, weight=BOLD).move_to(o)
        hla = Text("H", font_size=20, color=WHITE2, weight=BOLD).move_to(h1a)
        hlb = Text("H", font_size=20, color=WHITE2, weight=BOLD).move_to(h1b)
        h2o = VGroup(o, h1a, h1b, ol, hla, hlb).shift(RIGHT*4.0 + DOWN*0.4)
        h2o_lbl = Text("соединение H₂O", font_size=22, color=WHITE2).next_to(h2o, DOWN, buff=0.3)

        self.play(FadeIn(h_atom), Write(h_lbl), run_time=0.7)
        self.play(FadeIn(h2), Write(h2_lbl), run_time=0.7)
        self.play(FadeIn(h2o), Write(h2o_lbl), run_time=0.7)
        self.wait(1.0)

        final = callout("Еден атом. Многу атоми. Различни атоми — соединение.",
                        width=12.0, font_size=26, border=GREEN)
        final.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(final, shift=UP*0.2), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(VGroup(t6, h_atom, h_lbl, h2, h2_lbl,
                                  h2o, h2o_lbl, final)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Без атоми — нема свет.", font_size=42,
                      color=YELLOW, weight=BOLD)
        close1.move_to(UP*0.5)
        self.play(Write(close1), run_time=1.2)
        self.wait(0.5)

        close2 = Text("Со нив — сè.", font_size=42,
                      color=GREEN, weight=BOLD)
        close2.move_to(DOWN*0.6)
        self.play(Write(close2), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(close1, close2)), run_time=0.7)
        self.wait(0.3)
