"""
chem8-4-4  —  Хидроксиди и реакции со вода
Хемија 8, Единица 4: Хемиски реакции

Teaching narrative — Andonovski-style: alkali metals as
characters with personality, reactivity series as descent.
Render:  manim -ql chem8-4-4.py Chem844Scene
Output:  media/videos/chem8-4-4/480p15/Chem844Scene.mp4
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
PINK    = "#f48fb1"


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


class Chem844Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — ALKALI METAL PERSONALITIES
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Натриумот игра во вода.",
                  font_size=38, color=YELLOW, weight=BOLD)
        h2 = Text("Калиумот експлодира.",
                  font_size=38, color=RED, weight=BOLD)
        h3 = Text("Литиумот лазе.",
                  font_size=38, color=BLUE, weight=BOLD)
        h4 = Text("Иста група. Различен карактер.",
                  font_size=32, color=WHITE2)
        h5 = Text("Реактивноста расте надолу.",
                  font_size=34, color=GREEN, slant=ITALIC, weight=BOLD)
        hook = VGroup(h1, h2, h3, h4, h5).arrange(DOWN, buff=0.3)
        hook.move_to(ORIGIN)

        self.play(Write(h1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.3)
        self.play(Write(h3), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(h4), run_time=0.8)
        self.wait(0.3)
        self.play(Write(h5), run_time=1.1)
        self.wait(1.3)
        self.play(FadeOut(hook), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHAT IS A HYDROXIDE?
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е хидроксид?", BLUE)
        self.play(Write(title), run_time=0.8)

        defn = Text("Соединение со OH⁻ група.",
                    font_size=34, color=WHITE2)
        defn.move_to(UP * 1.4)
        self.play(Write(defn), run_time=1.1)
        self.wait(0.4)

        # Big OH group visualization
        oh_box = RoundedRectangle(width=4.0, height=2.0, corner_radius=0.3,
                                  fill_color=DARK_CARD, fill_opacity=1,
                                  stroke_color=PURPLE, stroke_width=2)
        oh_box.move_to(ORIGIN)

        o_atom = Circle(radius=0.45, fill_color=RED, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=1.5).move_to(LEFT * 0.7)
        o_lbl = Text("O", font_size=30, color="#0d1b2e", weight=BOLD).move_to(o_atom)
        h_atom = Circle(radius=0.32, fill_color=BLUE, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=1.5).move_to(RIGHT * 0.5)
        h_lbl = Text("H", font_size=24, color="#0d1b2e", weight=BOLD).move_to(h_atom)
        bond = Line(o_atom.get_right() + RIGHT * 0.05,
                    h_atom.get_left() + LEFT * 0.05,
                    color=WHITE2, stroke_width=4)
        minus = Text("⁻", font_size=36, color=YELLOW, weight=BOLD)
        minus.next_to(h_atom, UR, buff=0.05)
        oh_group = VGroup(oh_box, bond, o_atom, o_lbl, h_atom, h_lbl, minus)

        self.play(FadeIn(oh_box), run_time=0.5)
        self.play(FadeIn(o_atom), Write(o_lbl), run_time=0.6)
        self.play(Create(bond), run_time=0.4)
        self.play(FadeIn(h_atom), Write(h_lbl), run_time=0.5)
        self.play(Write(minus), run_time=0.5)
        self.wait(0.5)

        base = Text("Бази. Алкални. Спротивни на киселини.",
                    font_size=28, color=GREEN, weight=BOLD)
        base.to_edge(DOWN, buff=0.7)
        self.play(Write(base), run_time=1.2)
        self.wait(1.1)

        self.play(FadeOut(VGroup(title, defn, oh_group, base)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  METAL + WATER → HYDROXIDE + HYDROGEN
        # ══════════════════════════════════════════════════════════
        self.next_section("metal_water")

        title2 = section_title("Метал среќава вода", BLUE)
        self.play(Write(title2), run_time=0.8)

        story = Text("Парче натриум. Чаша вода. Драма.",
                     font_size=28, color=WHITE2)
        story.move_to(UP * 1.8)
        self.play(FadeIn(story), run_time=0.9)

        # Visual: Na piece on water
        water_surf = Rectangle(width=8.0, height=2.2,
                               fill_color=BLUE, fill_opacity=0.4,
                               stroke_color=BLUE, stroke_width=2)
        water_surf.move_to(DOWN * 0.5)
        wave_lbl = Text("H₂O", font_size=22, color=BLUE).move_to(water_surf.get_left() + RIGHT * 0.7 + DOWN * 0.2)

        na_piece = Circle(radius=0.3, fill_color=YELLOW, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=2)
        na_piece.move_to(LEFT * 2 + UP * 0.2)
        na_lbl = Text("Na", font_size=22, color="#0d1b2e", weight=BOLD).move_to(na_piece)
        na_g = VGroup(na_piece, na_lbl)

        # Hydrogen bubbles
        bubbles = VGroup(*[
            Circle(radius=0.08 + 0.04 * (i % 3),
                   fill_color=WHITE2, fill_opacity=0.7,
                   stroke_color=WHITE2, stroke_width=1)
            for i in range(7)
        ])
        for i, b in enumerate(bubbles):
            b.move_to(np.array([
                -1.4 + 0.4 * i,
                -0.3 + 0.15 * (i % 2),
                0
            ]))

        self.play(FadeIn(water_surf), Write(wave_lbl), run_time=0.7)
        self.play(FadeIn(na_g), run_time=0.6)
        self.play(*[FadeIn(b, shift=UP * 0.4) for b in bubbles], run_time=0.9)
        self.play(*[b.animate.shift(UP * 1.0) for b in bubbles],
                  na_g.animate.shift(LEFT * 0.5),
                  run_time=1.0)

        eq = MathTex(r"2\,Na", r"+", r"2\,H_2O", r"\to", r"2\,NaOH", r"+", r"H_2",
                     font_size=42)
        eq[0].set_color(YELLOW)
        eq[2].set_color(BLUE)
        eq[4].set_color(GREEN)
        eq[6].set_color(WHITE2)
        eq.move_to(DOWN * 2.4)
        self.play(Write(eq), run_time=1.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, story, water_surf, wave_lbl,
                                  na_g, bubbles, eq)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  METAL OXIDE + WATER — QUICKLIME
        # ══════════════════════════════════════════════════════════
        self.next_section("oxide_water")

        title3 = section_title("Оксид + вода", ORANGE)
        self.play(Write(title3), run_time=0.8)

        # CaO + H2O → Ca(OH)2
        cao = RoundedRectangle(width=2.0, height=1.4, corner_radius=0.2,
                               fill_color=WHITE2, fill_opacity=0.9,
                               stroke_color=GREY, stroke_width=2)
        cao_lbl = Text("CaO", font_size=28, color="#0d1b2e", weight=BOLD).move_to(cao)
        cao_sub = Text("живо вапно", font_size=20, color=YELLOW).next_to(cao, DOWN, buff=0.15)
        cao_g = VGroup(cao, cao_lbl, cao_sub).move_to(LEFT * 4 + UP * 0.1)

        plus = Text("+", font_size=44, color=WHITE2).move_to(LEFT * 1.8 + UP * 0.1)
        h2o_g = VGroup(
            Text("H₂O", font_size=32, color=BLUE, weight=BOLD),
        )
        h2o_g.move_to(LEFT * 0.5 + UP * 0.1)

        arrow = Arrow(LEFT * 0.2, RIGHT * 1.3, color=YELLOW,
                      buff=0.1, stroke_width=4).move_to(RIGHT * 0.5 + UP * 0.1)
        arrow_lbl = Text("+ топлина", font_size=20, color=ORANGE).next_to(arrow, UP, buff=0.1)

        prod = RoundedRectangle(width=2.4, height=1.4, corner_radius=0.2,
                                fill_color=WHITE2, fill_opacity=0.8,
                                stroke_color=GREEN, stroke_width=2)
        prod_lbl = Text("Ca(OH)₂", font_size=26, color="#0d1b2e", weight=BOLD).move_to(prod)
        prod_sub = Text("гасеноо вапно", font_size=20, color=GREEN).next_to(prod, DOWN, buff=0.15)
        prod_g = VGroup(prod, prod_lbl, prod_sub).move_to(RIGHT * 3.5 + UP * 0.1)

        self.play(FadeIn(cao_g), run_time=0.7)
        self.play(Write(plus), run_time=0.3)
        self.play(Write(h2o_g), run_time=0.5)
        self.play(GrowArrow(arrow), Write(arrow_lbl), run_time=0.7)
        self.play(FadeIn(prod_g), run_time=0.7)
        self.wait(0.5)

        eq2 = MathTex(r"CaO", r"+", r"H_2O", r"\to", r"Ca(OH)_2",
                      font_size=44)
        eq2[0].set_color(GREY)
        eq2[2].set_color(BLUE)
        eq2[4].set_color(GREEN)
        eq2.move_to(DOWN * 2.0)
        self.play(Write(eq2), run_time=1.3)
        self.wait(0.5)

        use = Text("Малтер. Цемент. Градежништво.",
                   font_size=26, color=YELLOW, slant=ITALIC)
        use.move_to(DOWN * 3.0)
        self.play(FadeIn(use), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, cao_g, plus, h2o_g,
                                  arrow, arrow_lbl, prod_g, eq2, use)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  REACTIVITY SERIES — DESCENT
        # ══════════════════════════════════════════════════════════
        self.next_section("reactivity")

        title4 = section_title("Реактивноста расте надолу", PURPLE)
        self.play(Write(title4), run_time=0.8)

        # Vertical list with growing intensity
        metals = [
            ("Li", "литиумот лазе по вода", BLUE),
            ("Na", "натриумот игра, бега, жоло", YELLOW),
            ("K", "калиумот пламне виолетово", PURPLE),
            ("Rb", "рубидиумот експлодира", ORANGE),
            ("Cs", "цезиумот — драма пред допир", RED),
        ]

        rows = VGroup()
        for sym, desc, col in metals:
            sym_t = Text(sym, font_size=34, color=col, weight=BOLD)
            sym_t.set_width(0.9)
            desc_t = Text(desc, font_size=24, color=WHITE2)
            row = VGroup(sym_t, desc_t).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
            rows.add(row)
        rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rows.next_to(title4, DOWN, buff=0.5)

        # Down arrow on the left
        d_arrow = Arrow(rows.get_corner(UL) + LEFT * 0.6 + UP * 0.1,
                        rows.get_corner(DL) + LEFT * 0.6 + DOWN * 0.1,
                        color=RED, stroke_width=6, buff=0)
        d_lbl = Text("реактивност ↑", font_size=22, color=RED)
        d_lbl.next_to(d_arrow, LEFT, buff=0.2).rotate(PI / 2)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.play(GrowArrow(d_arrow), FadeIn(d_lbl), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title4, rows, d_arrow, d_lbl)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  pH SCALE WITH INDICATOR
        # ══════════════════════════════════════════════════════════
        self.next_section("ph")

        title5 = section_title("pH скала", GREEN)
        self.play(Write(title5), run_time=0.8)

        # 14-step pH bar
        bar = VGroup()
        ph_colors = [
            "#d32f2f", "#e53935", "#f44336", "#ff7043",
            "#ffa726", "#ffca28", "#fff176", "#cddc39",
            "#9ccc65", "#66bb6a", "#26a69a", "#26c6da",
            "#42a5f5", "#5c6bc0", "#7e57c2",
        ]
        for i, col in enumerate(ph_colors):
            cell = Rectangle(width=0.7, height=1.0, fill_color=col,
                             fill_opacity=1, stroke_color="#0d1b2e", stroke_width=1)
            num = Text(str(i), font_size=20, color=WHITE2, weight=BOLD)
            num.next_to(cell, DOWN, buff=0.1)
            bar.add(VGroup(cell, num))
        bar.arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        bar.move_to(ORIGIN)

        self.play(LaggedStartMap(FadeIn, bar, lag_ratio=0.05), run_time=1.5)
        self.wait(0.4)

        # Labels
        acid_l = Text("кисело", font_size=26, color=RED, weight=BOLD)
        acid_l.next_to(bar, UP, buff=0.4).shift(LEFT * 4)
        neut_l = Text("неутрално", font_size=26, color=YELLOW, weight=BOLD)
        neut_l.next_to(bar, UP, buff=0.4)
        base_l = Text("базно", font_size=26, color=PURPLE, weight=BOLD)
        base_l.next_to(bar, UP, buff=0.4).shift(RIGHT * 4)

        self.play(FadeIn(acid_l), FadeIn(neut_l), FadeIn(base_l), run_time=0.8)
        self.wait(0.6)

        # Litmus mnemonic
        litmus = Text("Лакмус: црвено = кисело. Сино = базно.",
                      font_size=28, color=WHITE2)
        litmus.move_to(DOWN * 2.3)
        self.play(Write(litmus), run_time=1.3)
        self.wait(0.4)

        mem = Text("Памти: СИНа = БазНа.",
                   font_size=28, color=BLUE, weight=BOLD)
        mem.move_to(DOWN * 3.1)
        self.play(FadeIn(mem), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title5, bar, acid_l, neut_l, base_l,
                                  litmus, mem)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        c1 = Text("Метал среќава вода.",
                  font_size=34, color=YELLOW)
        c2 = Text("Се раѓа хидроксид.",
                  font_size=34, color=GREEN)
        c3 = Text("Водородот бега в воздух.",
                  font_size=32, color=BLUE)
        c4 = Text("Прв ред — мирно. Долен ред — драма.",
                  font_size=30, color=WHITE2, slant=ITALIC)
        c5 = Text("Реактивност.",
                  font_size=52, color=PURPLE, weight=BOLD)
        close = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, buff=0.35)
        close.move_to(ORIGIN)

        self.play(Write(c1), run_time=0.9)
        self.wait(0.2)
        self.play(Write(c2), run_time=0.9)
        self.wait(0.2)
        self.play(Write(c3), run_time=0.9)
        self.wait(0.2)
        self.play(FadeIn(c4), run_time=0.8)
        self.wait(0.3)
        self.play(Write(c5), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
        self.wait(0.4)
