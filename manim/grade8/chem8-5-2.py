"""
chem8-5-2  —  Алкани и хомологни низи
Хемија 8, Единица 5: Органска хемија

Teaching narrative — Andonovski-style: three-beat punches,
molecules as personalities, same recipe different length,
one-word finishers.
Render:  manim -ql chem8-5-2.py Chem852Scene
Output:  media/videos/chem8-5-2/480p15/Chem852Scene.mp4
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


def C_atom(pos, r=0.28):
    c = Circle(radius=r, fill_color=YELLOW, fill_opacity=1,
               stroke_color=WHITE2, stroke_width=2).move_to(pos)
    t = Text("C", font_size=22, color="#0d1b2e", weight=BOLD).move_to(pos)
    return VGroup(c, t)


def H_atom(pos, r=0.20):
    c = Circle(radius=r, fill_color=BLUE, fill_opacity=1,
               stroke_color=WHITE2, stroke_width=1.5).move_to(pos)
    t = Text("H", font_size=18, color="#0d1b2e", weight=BOLD).move_to(pos)
    return VGroup(c, t)


def bond(p1, p2, color=WHITE2, width=3):
    return Line(p1, p2, color=color, stroke_width=width)


def build_alkane(n, center=ORIGIN, scale=0.9):
    """Build CnH(2n+2) structural formula at center."""
    g = VGroup()
    spacing = 1.1 * scale
    # carbon positions in a row
    start_x = -((n-1)/2) * spacing
    c_positions = [center + RIGHT*(start_x + i*spacing) for i in range(n)]

    # C-C bonds
    for i in range(n-1):
        g.add(bond(c_positions[i], c_positions[i+1]))

    # C atoms
    for p in c_positions:
        g.add(C_atom(p, r=0.26*scale))

    # H atoms: each carbon gets H above, H below; end carbons get extras
    for i, p in enumerate(c_positions):
        # H up
        h_up_pos = p + UP*0.85*scale
        g.add(bond(p, h_up_pos))
        g.add(H_atom(h_up_pos, r=0.18*scale))
        # H down
        h_down_pos = p + DOWN*0.85*scale
        g.add(bond(p, h_down_pos))
        g.add(H_atom(h_down_pos, r=0.18*scale))
        # end carbons: extra H on outer side
        if i == 0:
            h_left_pos = p + LEFT*0.85*scale
            g.add(bond(p, h_left_pos))
            g.add(H_atom(h_left_pos, r=0.18*scale))
        if i == n-1:
            h_right_pos = p + RIGHT*0.85*scale
            g.add(bond(p, h_right_pos))
            g.add(H_atom(h_right_pos, r=0.18*scale))

    return g


class Chem852Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Метан.", font_size=46, color=YELLOW, weight=BOLD),
            Text("Етан.", font_size=46, color=GREEN, weight=BOLD),
            Text("Пропан.", font_size=46, color=ORANGE, weight=BOLD),
            Text("Бутан.", font_size=46, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.3).move_to(UP*0.8)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.5)

        self.wait(0.5)

        denials = VGroup(
            Text("Не букви.", font_size=32, color=GREY),
            Text("Не зборови.", font_size=32, color=GREY),
            Text("Семејство.", font_size=40, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.25).next_to(beats, DOWN, buff=0.6)

        for d in denials:
            self.play(FadeIn(d), run_time=0.5)
            self.wait(0.2)

        self.wait(1.0)
        self.play(FadeOut(VGroup(beats, denials)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  METHANE  CH4                                    ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("methane")

        title = section_title("Метан — CH₄", color=YELLOW)
        self.play(Write(title), run_time=0.8)

        ch4 = build_alkane(1, center=ORIGIN + UP*0.2, scale=1.0)
        self.play(Create(ch4), run_time=1.6)

        formula = MathTex(r"\mathrm{CH_4}", font_size=52, color=GREEN)
        formula.to_edge(DOWN, buff=1.4)
        self.play(Write(formula), run_time=0.8)

        info = VGroup(
            Text("Еден јаглерод. Четири водороди.",
                 font_size=26, color=WHITE2),
            Text("Природен гас. Прв во семејството.",
                 font_size=24, color=GREY),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(info), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, ch4, formula, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ETHANE  C2H6                                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ethane")

        title2 = section_title("Етан — C₂H₆", color=GREEN)
        self.play(Write(title2), run_time=0.7)

        c2h6 = build_alkane(2, center=ORIGIN + UP*0.2, scale=0.95)
        self.play(Create(c2h6), run_time=1.6)

        formula2 = MathTex(r"\mathrm{C_2H_6}", font_size=52, color=GREEN)
        formula2.to_edge(DOWN, buff=1.4)
        self.play(Write(formula2), run_time=0.7)

        diff = Text("Додаде еден CH₂. Поголемо.",
                    font_size=26, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(diff), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title2, c2h6, formula2, diff)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  PROPANE & BUTANE                                ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("propane_butane")

        title3 = section_title("Пропан и бутан", color=ORANGE)
        self.play(Write(title3), run_time=0.7)

        # propane left, butane right
        c3h8 = build_alkane(3, center=LEFT*3.5 + UP*0.2, scale=0.75)
        c4h10 = build_alkane(4, center=RIGHT*2.8 + UP*0.2, scale=0.7)

        self.play(Create(c3h8), run_time=1.4)
        self.play(Create(c4h10), run_time=1.5)

        lbl1 = MathTex(r"\mathrm{C_3H_8}", font_size=36, color=ORANGE)
        lbl1.next_to(c3h8, DOWN, buff=0.6)
        lbl2 = MathTex(r"\mathrm{C_4H_{10}}", font_size=36, color=RED)
        lbl2.next_to(c4h10, DOWN, buff=0.6)

        self.play(Write(lbl1), Write(lbl2), run_time=0.8)
        self.wait(0.6)

        gas_note = Text("Гас за плински боци. Гас за запалки.",
                        font_size=24, color=WHITE2)
        gas_note.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(gas_note), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title3, c3h8, c4h10, lbl1, lbl2, gas_note)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  HOMOLOGOUS SERIES                               ~36 s
        # ══════════════════════════════════════════════════════════
        self.next_section("homologous")

        title4 = section_title("Хомологна низа", color=PURPLE)
        self.play(Write(title4), run_time=0.8)

        # Table-style
        header = VGroup(
            Text("Име", font_size=26, color=YELLOW, weight=BOLD),
            Text("Формула", font_size=26, color=YELLOW, weight=BOLD),
            Text("n", font_size=26, color=YELLOW, weight=BOLD),
        ).arrange(RIGHT, buff=2.0)
        header.to_edge(UP, buff=1.3)

        rows_data = [
            ("Метан", r"\mathrm{CH_4}", "1", GREEN),
            ("Етан", r"\mathrm{C_2H_6}", "2", GREEN),
            ("Пропан", r"\mathrm{C_3H_8}", "3", ORANGE),
            ("Бутан", r"\mathrm{C_4H_{10}}", "4", ORANGE),
            ("Пентан", r"\mathrm{C_5H_{12}}", "5", RED),
        ]

        rows = VGroup()
        for name, fmla, n, col in rows_data:
            row = VGroup(
                Text(name, font_size=24, color=col),
                MathTex(fmla, font_size=30, color=WHITE2),
                Text(n, font_size=24, color=col),
            ).arrange(RIGHT, buff=2.0)
            rows.add(row)
        rows.arrange(DOWN, buff=0.25)
        rows.next_to(header, DOWN, buff=0.3)

        # align columns
        for r in rows:
            r[0].align_to(header[0], LEFT)
            r[1].align_to(header[1], LEFT).shift(LEFT*0.2)
            r[2].align_to(header[2], LEFT)

        self.play(FadeIn(header), run_time=0.6)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT*0.2), run_time=0.5)
        self.wait(0.6)

        gen_box = RoundedRectangle(
            width=8, height=1.2, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=3,
        ).to_edge(DOWN, buff=0.5)
        gen_formula = MathTex(r"\mathrm{C_nH_{2n+2}}",
                              font_size=44, color=YELLOW)
        gen_formula.move_to(gen_box)
        self.play(Create(gen_box), run_time=0.6)
        self.play(Write(gen_formula), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title4, header, rows, gen_box, gen_formula)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  NAMING — PREFIXES                               ~24 s
        # ══════════════════════════════════════════════════════════
        self.next_section("naming")

        title5 = section_title("Истиот рецепт. Различна должина.",
                               color=YELLOW)
        self.play(Write(title5), run_time=1.0)

        prefixes_data = [
            ("мет-", "1 C", GREEN),
            ("ет-", "2 C", GREEN),
            ("проп-", "3 C", ORANGE),
            ("бут-", "4 C", RED),
        ]

        cards = VGroup()
        for prefix, count, col in prefixes_data:
            box = RoundedRectangle(
                width=2.6, height=1.6, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            p_lbl = Text(prefix, font_size=28, color=col, weight=BOLD)
            c_lbl = Text(count, font_size=22, color=WHITE2)
            VGroup(p_lbl, c_lbl).arrange(DOWN, buff=0.15).move_to(box)
            cards.add(VGroup(box, p_lbl, c_lbl))
        cards.arrange(RIGHT, buff=0.3).move_to(ORIGIN)

        for c in cards:
            self.play(FadeIn(c, shift=UP*0.2), run_time=0.45)
        self.wait(0.6)

        suffix = Text("+ -ан = алкан",
                      font_size=32, color=YELLOW)
        suffix.next_to(cards, DOWN, buff=0.6)
        self.play(Write(suffix), run_time=0.7)
        self.wait(0.5)

        finisher = Text("Семејство.",
                        font_size=42, color=PURPLE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title5, cards, suffix, finisher)),
                  run_time=0.9)
        self.wait(0.4)
