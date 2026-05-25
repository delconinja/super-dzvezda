"""
chem8-2-5  —  Периоден систем и групи на елементите
Хемија 8, Единица 2: Материјали околу нас

Teaching narrative — Andonovski-style: three-beat punches,
groups as families with traits, не...туку contrast, one-word finishers.
Render:  manim -ql chem8-2-5.py Chem825Scene
Output:  media/videos/chem8-2-5/480p15/Chem825Scene.mp4
"""
from manim import *
import numpy as np

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

ALKALI_COL    = "#ff7043"   # Group 1 — fiery
ALKEARTH_COL  = "#ffb74d"   # Group 2
TRANSITION_COL = "#90a4ae"  # Groups 3-12
HALOGEN_COL   = "#81c784"   # Group 17 — green/reactive nonmetal
NOBLE_COL     = "#ce93d8"   # Group 18 — purple/regal
OTHER_NM      = "#4fc3f7"   # other nonmetals
METALLOID_COL = "#a1887f"
POSTMETAL_COL = "#9ccc65"


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


def element_cell(symbol, color, pos, size=0.55, txt_size=16):
    box = Square(side_length=size,
                 fill_color=color, fill_opacity=0.9,
                 stroke_color=WHITE2, stroke_width=1.2).move_to(pos)
    sym = Text(symbol, font_size=txt_size, color=WHITE2, weight=BOLD)
    sym.move_to(box)
    return VGroup(box, sym)


class Chem825Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Менделејев го виде редот.",
                  font_size=44, color=YELLOW, weight=BOLD)
        h2 = Text("Каде друг гледал хаос.",
                  font_size=36, color=WHITE2)
        h1.move_to(UP * 1.6)
        h2.next_to(h1, DOWN, buff=0.35)

        self.play(Write(h1), run_time=1.2)
        self.wait(0.4)
        self.play(Write(h2), run_time=1.2)
        self.wait(0.5)

        year = Text("1869 година.", font_size=40, color=ORANGE, weight=BOLD)
        year.next_to(h2, DOWN, buff=0.55)
        self.play(Write(year), run_time=1.0)
        self.wait(0.3)

        line3 = Text("Цела хемија — една табела.",
                     font_size=32, color=WHITE2)
        line3.next_to(year, DOWN, buff=0.4)
        self.play(Write(line3), run_time=1.3)
        self.wait(0.4)

        finish = Text("Геније.",
                      font_size=48, color=YELLOW, weight=BOLD)
        finish.next_to(line3, DOWN, buff=0.5)
        self.play(Write(finish), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(h1, h2, year, line3, finish)))

        # ══════════════════════════════════════════════════════════
        # 2.  ПОРТРЕТ КАРТИЧКА                                 ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mendeleev")

        t2 = section_title("Димитриј Менделејев")
        self.play(Write(t2), run_time=0.9)

        # Portrait card — stylized
        card = RoundedRectangle(
            width=5.0, height=5.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=3,
        ).move_to(LEFT*3.5 + DOWN*0.3)

        # Stylized portrait — head shape with hair/beard
        head = Circle(radius=0.9, fill_color="#e8c39e", fill_opacity=1,
                      stroke_color=WHITE2, stroke_width=2)
        head.move_to(card.get_center() + UP*1.3)
        hair = Arc(radius=0.95, start_angle=PI*0.1, angle=PI*0.8,
                   color=GREY, stroke_width=14)
        hair.move_to(head.get_center() + UP*0.15)
        beard = Arc(radius=0.85, start_angle=PI*1.1, angle=PI*0.8,
                    color=GREY, stroke_width=14)
        beard.move_to(head.get_center() + DOWN*0.4)
        eye1 = Dot([head.get_center()[0] - 0.25, head.get_center()[1] + 0.1, 0],
                   radius=0.06, color=BLACK)
        eye2 = Dot([head.get_center()[0] + 0.25, head.get_center()[1] + 0.1, 0],
                   radius=0.06, color=BLACK)

        portrait = VGroup(head, hair, beard, eye1, eye2)

        info1 = Text("Руски хемичар",
                     font_size=22, color=WHITE2)
        info1.move_to(card.get_center() + DOWN*0.8)
        info2 = Text("1869 — првата табела",
                     font_size=22, color=YELLOW, weight=BOLD)
        info2.move_to(card.get_center() + DOWN*1.3)
        info3 = Text("Предвиде нови елементи",
                     font_size=20, color=WHITE2)
        info3.move_to(card.get_center() + DOWN*1.8)
        info4 = Text("Сите беа најдени.",
                     font_size=22, color=GREEN, weight=BOLD)
        info4.move_to(card.get_center() + DOWN*2.25)

        self.play(FadeIn(card), run_time=0.6)
        self.play(FadeIn(portrait), run_time=0.8)
        self.play(Write(info1), run_time=0.7)
        self.play(Write(info2), run_time=0.7)
        self.play(Write(info3), run_time=0.7)
        self.play(Write(info4), run_time=0.7)

        # Right side — quote
        quote = Text(
            "„Подреди ги по својства —\nи табелата ќе ти каже\nкаде се празните места."+'"',
            font_size=24, color=WHITE2,
        )
        quote.move_to(RIGHT*3.3 + DOWN*0.3)
        self.play(Write(quote), run_time=1.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t2, card, portrait, info1, info2, info3, info4, quote)))

        # ══════════════════════════════════════════════════════════
        # 3.  ТАБЕЛА — групи маркирани                         ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("table_groups")

        t3 = section_title("18 групи. 7 периоди.")
        self.play(Write(t3), run_time=0.9)

        # Build 4-row periodic table layout with group colors
        size = 0.5
        x_start = -5.4
        y_start = 1.5

        # Map (row, col) -> (symbol, color)
        cells = {}

        # Period 1
        cells[(0, 1)] = ('H', OTHER_NM)
        cells[(0, 18)] = ('He', NOBLE_COL)
        # Period 2
        p2 = ['Li','Be',None,None,None,None,None,None,None,None,None,None,
              'B','C','N','O','F','Ne']
        p2_cols = [ALKALI_COL, ALKEARTH_COL] + [None]*10 + [
            METALLOID_COL, OTHER_NM, OTHER_NM, OTHER_NM, HALOGEN_COL, NOBLE_COL]
        for c_idx, (sym, col) in enumerate(zip(p2, p2_cols)):
            if sym:
                cells[(1, c_idx + 1)] = (sym, col)
        # Period 3
        p3 = ['Na','Mg',None,None,None,None,None,None,None,None,None,None,
              'Al','Si','P','S','Cl','Ar']
        p3_cols = [ALKALI_COL, ALKEARTH_COL] + [None]*10 + [
            POSTMETAL_COL, METALLOID_COL, OTHER_NM, OTHER_NM, HALOGEN_COL, NOBLE_COL]
        for c_idx, (sym, col) in enumerate(zip(p3, p3_cols)):
            if sym:
                cells[(2, c_idx + 1)] = (sym, col)
        # Period 4 (abridged transition)
        p4_syms = ['K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn',
                   'Ga','Ge','As','Se','Br','Kr']
        p4_cols = [ALKALI_COL, ALKEARTH_COL] + [TRANSITION_COL]*10 + [
            POSTMETAL_COL, METALLOID_COL, METALLOID_COL,
            OTHER_NM, HALOGEN_COL, NOBLE_COL]
        for c_idx, (sym, col) in enumerate(zip(p4_syms, p4_cols)):
            cells[(3, c_idx + 1)] = (sym, col)

        table = VGroup()
        for (r, c), (sym, col) in cells.items():
            x = x_start + (c - 1) * size * 1.15
            y = y_start - r * size * 1.15
            table.add(element_cell(sym, col, [x, y, 0],
                                   size=size, txt_size=14))
        self.play(FadeIn(table), run_time=1.4)
        self.wait(0.5)

        # Highlight Group 1 with a labeled bracket
        g1_x = x_start + 0 * size * 1.15
        bracket_g1 = Rectangle(
            width=size*1.15, height=size*1.15*4 + 0.3,
            stroke_color=ALKALI_COL, stroke_width=4,
            fill_opacity=0,
        ).move_to([g1_x, y_start - 1.65 * size * 1.15, 0])
        lab_g1 = Text("Алкални\nметали",
                      font_size=18, color=ALKALI_COL, weight=BOLD)
        lab_g1.next_to(bracket_g1, DOWN, buff=0.1)
        self.play(Create(bracket_g1), Write(lab_g1), run_time=0.9)
        self.wait(0.4)

        # Group 17 — halogens
        g17_x = x_start + 16 * size * 1.15
        bracket_g17 = Rectangle(
            width=size*1.15, height=size*1.15*3 + 0.3,
            stroke_color=HALOGEN_COL, stroke_width=4,
            fill_opacity=0,
        ).move_to([g17_x, y_start - 2.15 * size * 1.15, 0])
        lab_g17 = Text("Халогени",
                       font_size=18, color=HALOGEN_COL, weight=BOLD)
        lab_g17.next_to(bracket_g17, DOWN, buff=0.1)
        self.play(Create(bracket_g17), Write(lab_g17), run_time=0.9)
        self.wait(0.4)

        # Group 18 — noble gases
        g18_x = x_start + 17 * size * 1.15
        bracket_g18 = Rectangle(
            width=size*1.15, height=size*1.15*4 + 0.3,
            stroke_color=NOBLE_COL, stroke_width=4,
            fill_opacity=0,
        ).move_to([g18_x, y_start - 1.65 * size * 1.15, 0])
        lab_g18 = Text("Благородни\nгасови",
                       font_size=18, color=NOBLE_COL, weight=BOLD)
        lab_g18.next_to(bracket_g18, UP, buff=0.1)
        self.play(Create(bracket_g18), Write(lab_g18), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, table,
                                  bracket_g1, lab_g1,
                                  bracket_g17, lab_g17,
                                  bracket_g18, lab_g18)))

        # ══════════════════════════════════════════════════════════
        # 4.  ФАМИЛИИ — три картички                           ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("families")

        t4 = section_title("Три фамилии. Три карактери.")
        self.play(Write(t4), run_time=0.9)

        def family_card(name, elements, trait, color, pos):
            box = RoundedRectangle(
                width=4.4, height=4.6, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            ).move_to(pos)
            nm = Text(name, font_size=24, color=color, weight=BOLD)
            nm.next_to(box.get_top(), DOWN, buff=0.25)

            # Element symbols stacked
            elem_g = VGroup()
            for i, e in enumerate(elements):
                cell = element_cell(e, color, [0, 0, 0],
                                    size=0.5, txt_size=18)
                cell.move_to(box.get_center() + UP*(0.8 - i*0.55))
                elem_g.add(cell)

            tr = Text(trait, font_size=20, color=WHITE2)
            tr.move_to(box.get_center() + DOWN*1.7)
            return VGroup(box, nm, elem_g, tr)

        f1 = family_card("Група 1 — алкални",
                         ["Li", "Na", "K", "Rb", "Cs"],
                         "огнени.\nекспло. со вода.",
                         ALKALI_COL, LEFT*4.6 + DOWN*0.3)
        f2 = family_card("Група 17 — халогени",
                         ["F", "Cl", "Br", "I"],
                         "реактивни.\nсе спојуваат со сè.",
                         HALOGEN_COL, DOWN*0.3)
        f3 = family_card("Група 18 — благородни",
                         ["He", "Ne", "Ar", "Kr", "Xe"],
                         "молчаливи.\nполна школка.",
                         NOBLE_COL, RIGHT*4.6 + DOWN*0.3)

        self.play(FadeIn(f1), run_time=0.7)
        self.play(FadeIn(f2), run_time=0.7)
        self.play(FadeIn(f3), run_time=0.7)
        self.wait(2.4)

        self.play(FadeOut(VGroup(t4, f1, f2, f3)))

        # ══════════════════════════════════════════════════════════
        # 5.  ТРЕНД — реактивност надолу во Гр. 1              ~24 s
        # ══════════════════════════════════════════════════════════
        self.next_section("trend")

        t5 = section_title("Тренд — реактивност во Група 1.")
        self.play(Write(t5), run_time=0.9)

        # Vertical column of Group 1 elements with reactivity bars
        elements = [("Li", "лесна реакција", 1.0),
                    ("Na", "брза", 1.8),
                    ("K", "пожар", 2.6),
                    ("Rb", "силна",  3.4),
                    ("Cs", "експлозивна", 4.2)]
        y_start = 2.0
        col_grp = VGroup()
        for i, (sym, note, bar) in enumerate(elements):
            y = y_start - i * 0.95
            cell = element_cell(sym, ALKALI_COL,
                                [LEFT[0]*4.5, y, 0],
                                size=0.7, txt_size=22)
            note_t = Text(note, font_size=20, color=WHITE2)
            note_t.move_to([LEFT[0]*2.5, y, 0])
            note_t.align_to(LEFT*3.6, LEFT)
            bar_bg = Rectangle(width=4.0, height=0.3,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=GREY, stroke_width=1)
            bar_bg.move_to([RIGHT[0]*1.5, y, 0])
            bar_fill = Rectangle(width=bar, height=0.3,
                                 fill_color=ORANGE, fill_opacity=0.9,
                                 stroke_width=0)
            bar_fill.align_to(bar_bg, LEFT)
            bar_fill.move_to([RIGHT[0]*1.5 - 2.0 + bar/2, y, 0])
            col_grp.add(VGroup(cell, note_t, bar_bg, bar_fill))

        for r in col_grp:
            self.play(FadeIn(r), run_time=0.4)

        # Big down-arrow
        arrow = Arrow(start=UP*2.2, end=DOWN*2.2,
                      color=YELLOW, buff=0.1, stroke_width=8)
        arrow.move_to(LEFT*5.7 + DOWN*0.2)
        ar_lab = Text("појака",
                      font_size=24, color=YELLOW, weight=BOLD)
        ar_lab.next_to(arrow, RIGHT, buff=0.05).shift(UP*0.0)
        ar_lab.move_to(arrow.get_center() + LEFT*0.55)
        self.play(GrowArrow(arrow), Write(ar_lab), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t5, col_grp, arrow, ar_lab)))

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЗИМЕ                                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни.")
        self.play(Write(t7), run_time=0.8)

        b1 = callout("Периоди — редови. Групи — колони.",
                     width=11.0, border=BLUE, font_size=28)
        b1.move_to(UP*1.6)
        b2 = callout("Иста група = иста фамилија. Иста природа.",
                     width=11.0, border=GREEN, font_size=28)
        b2.next_to(b1, DOWN, buff=0.35)
        b3 = callout("Алкални горат. Халогени напаѓаат. Благородни молчат.",
                     width=11.0, border=YELLOW, font_size=28)
        b3.next_to(b2, DOWN, buff=0.35)

        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.0)

        finisher = Text("Ред.",
                        font_size=58, color=YELLOW, weight=BOLD)
        finisher.next_to(b3, DOWN, buff=0.55)
        self.play(Write(finisher), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, b1, b2, b3, finisher)))
        self.wait(0.5)
