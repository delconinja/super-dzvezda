"""
chem8-2-3  —  Метали и неметали во периодниот систем
Хемија 8, Единица 2: Материјали околу нас

Teaching narrative — Andonovski-style: three-beat punches,
elements as characters, не...туку contrast, one-word finishers.
Render:  manim -ql chem8-2-3.py Chem823Scene
Output:  media/videos/chem8-2-3/480p15/Chem823Scene.mp4
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

METAL_COL    = "#5a9ad6"
METALLOID_COL = "#ce93d8"
NONMETAL_COL = "#ffb74d"


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


def element_cell(symbol, color, pos, size=0.55, txt_size=18):
    box = Square(side_length=size,
                 fill_color=color, fill_opacity=0.9,
                 stroke_color=WHITE2, stroke_width=1.2).move_to(pos)
    sym = Text(symbol, font_size=txt_size, color=WHITE2, weight=BOLD)
    sym.move_to(box)
    return VGroup(box, sym)


class Chem823Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Левата страна — метали.",
                  font_size=42, color=METAL_COL, weight=BOLD)
        h2 = Text("Десната — неметали.",
                  font_size=42, color=NONMETAL_COL, weight=BOLD)
        h3 = Text("Помеѓу — металоиди.",
                  font_size=42, color=METALLOID_COL, weight=BOLD)
        h1.move_to(UP * 1.8)
        h2.next_to(h1, DOWN, buff=0.35)
        h3.next_to(h2, DOWN, buff=0.35)

        self.play(Write(h1), run_time=0.9)
        self.wait(0.2)
        self.play(Write(h2), run_time=0.9)
        self.wait(0.2)
        self.play(Write(h3), run_time=0.9)
        self.wait(0.5)

        line2 = Text("Како луѓе.", font_size=36, color=WHITE2, weight=BOLD)
        line2.next_to(h3, DOWN, buff=0.55)
        self.play(Write(line2), run_time=0.9)
        self.wait(0.3)

        line3 = Text("Едни блескаат. Други молчат. Некои — на двете страни.",
                     font_size=28, color=YELLOW)
        line3.next_to(line2, DOWN, buff=0.35)
        self.play(Write(line3), run_time=1.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(h1, h2, h3, line2, line3)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА — Периоден систем                     ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е периоден систем?")
        self.play(Write(t2), run_time=0.9)

        d1 = callout(
            "Периоден систем = табела на сите хемиски елементи.",
            width=12.0, font_size=28,
        )
        d1.next_to(t2, DOWN, buff=0.6)
        self.play(FadeIn(d1), run_time=0.8)
        self.wait(0.5)

        d2 = Text("Подредени по атомски број — број на протони.",
                  font_size=28, color=WHITE2)
        d2.next_to(d1, DOWN, buff=0.45)
        self.play(Write(d2), run_time=1.3)
        self.wait(0.6)

        d3 = Text("Менделејев. 1869. Геније.",
                  font_size=36, color=YELLOW, weight=BOLD)
        d3.next_to(d2, DOWN, buff=0.5)
        self.play(Write(d3), run_time=1.3)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, d1, d2, d3)))

        # ══════════════════════════════════════════════════════════
        # 3.  ПРИКАЗ — поделба на табелата                     ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("table_regions")

        t3 = section_title("Три региони. Една табела.")
        self.play(Write(t3), run_time=0.9)

        # Simplified 7-row, 18-col grid
        # rows: 1..7 (we'll show 4 rows for visual clarity)
        # We'll mark squares as metal/metalloid/nonmetal/empty by row,col
        # Layout: x = -5 + col*0.6 ; y = 1.5 - row*0.55
        size = 0.5

        # Define which cells exist + classification for a stylized table
        # Group 1: col 1 (metal except H)
        # Group 2: col 2 (metals)
        # Groups 3..12 (transition): cols 3..12 (metals)
        # Groups 13..18 (cols 13..18): mix
        # Hydrogen at row1 col1 nonmetal; He at row1 col18 nonmetal
        rows = []
        # Period 1: H at col 1 (non-metal), He at col 18 (non-metal)
        rows.append({1: ('H', NONMETAL_COL), 18: ('He', NONMETAL_COL)})
        # Period 2: Li Be ... B C N O F Ne
        rows.append({
            1: ('Li', METAL_COL), 2: ('Be', METAL_COL),
            13: ('B', METALLOID_COL), 14: ('C', NONMETAL_COL),
            15: ('N', NONMETAL_COL), 16: ('O', NONMETAL_COL),
            17: ('F', NONMETAL_COL), 18: ('Ne', NONMETAL_COL),
        })
        # Period 3: Na Mg ... Al Si P S Cl Ar
        rows.append({
            1: ('Na', METAL_COL), 2: ('Mg', METAL_COL),
            13: ('Al', METAL_COL), 14: ('Si', METALLOID_COL),
            15: ('P', NONMETAL_COL), 16: ('S', NONMETAL_COL),
            17: ('Cl', NONMETAL_COL), 18: ('Ar', NONMETAL_COL),
        })
        # Period 4 (abridged transition metals)
        p4 = {1: ('K', METAL_COL), 2: ('Ca', METAL_COL)}
        for c, sym in zip(range(3, 13),
                          ['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn']):
            p4[c] = (sym, METAL_COL)
        p4[13] = ('Ga', METAL_COL)
        p4[14] = ('Ge', METALLOID_COL)
        p4[15] = ('As', METALLOID_COL)
        p4[16] = ('Se', NONMETAL_COL)
        p4[17] = ('Br', NONMETAL_COL)
        p4[18] = ('Kr', NONMETAL_COL)
        rows.append(p4)

        x_start = -5.4
        y_start = 1.5

        table_grp = VGroup()
        for r_idx, row in enumerate(rows):
            for col, (sym, col_color) in row.items():
                x = x_start + (col - 1) * size * 1.15
                y = y_start - r_idx * size * 1.15
                cell = element_cell(sym, col_color, [x, y, 0],
                                    size=size, txt_size=14)
                table_grp.add(cell)

        self.play(FadeIn(table_grp), run_time=1.2)
        self.wait(0.5)

        # Legend
        leg_box_metal = Square(side_length=0.4, fill_color=METAL_COL,
                               fill_opacity=0.9, stroke_color=WHITE2)
        leg_box_metal.move_to(LEFT*5.5 + DOWN*2.0)
        leg_t_metal = Text("Метали (~80%)", font_size=22, color=WHITE2)
        leg_t_metal.next_to(leg_box_metal, RIGHT, buff=0.15)

        leg_box_mloid = Square(side_length=0.4, fill_color=METALLOID_COL,
                               fill_opacity=0.9, stroke_color=WHITE2)
        leg_box_mloid.next_to(leg_t_metal, RIGHT, buff=0.6)
        leg_t_mloid = Text("Металоиди", font_size=22, color=WHITE2)
        leg_t_mloid.next_to(leg_box_mloid, RIGHT, buff=0.15)

        leg_box_nm = Square(side_length=0.4, fill_color=NONMETAL_COL,
                            fill_opacity=0.9, stroke_color=WHITE2)
        leg_box_nm.next_to(leg_t_mloid, RIGHT, buff=0.6)
        leg_t_nm = Text("Неметали", font_size=22, color=WHITE2)
        leg_t_nm.next_to(leg_box_nm, RIGHT, buff=0.15)

        legend = VGroup(leg_box_metal, leg_t_metal,
                        leg_box_mloid, leg_t_mloid,
                        leg_box_nm, leg_t_nm)
        legend.shift(RIGHT*0.4)
        self.play(FadeIn(legend), run_time=0.9)
        self.wait(0.6)

        # Diagonal line — separation
        # roughly from B (period 2, col 13) down to At-ish
        # We'll draw a thin line between metal and non-metal region
        diag = DashedLine(
            start=[x_start + 12*size*1.15 - size*0.5, y_start + size*0.6, 0],
            end=[x_start + 17*size*1.15 + size*0.6, y_start - 3*size*1.15 - size*0.5, 0],
            color=YELLOW, stroke_width=3, dash_length=0.12,
        )
        self.play(Create(diag), run_time=1.0)
        self.wait(0.4)

        line_label = Text("граница",
                          font_size=22, color=YELLOW, weight=BOLD)
        line_label.next_to(diag, RIGHT, buff=0.1).shift(UP*0.2)
        self.play(Write(line_label), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, table_grp, legend, diag, line_label)))

        # ══════════════════════════════════════════════════════════
        # 4.  СПОРЕДБА — две колони                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        t4 = section_title("Метал. Неметал. Што ги дели?")
        self.play(Write(t4), run_time=0.9)

        # Two big panels
        metal_panel = RoundedRectangle(
            width=6.0, height=4.8, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=METAL_COL, stroke_width=3,
        ).move_to(LEFT*3.4 + DOWN*0.3)
        nm_panel = RoundedRectangle(
            width=6.0, height=4.8, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=NONMETAL_COL, stroke_width=3,
        ).move_to(RIGHT*3.4 + DOWN*0.3)

        m_title = Text("МЕТАЛ", font_size=32, color=METAL_COL, weight=BOLD)
        m_title.next_to(metal_panel.get_top(), DOWN, buff=0.2)
        nm_title = Text("НЕМЕТАЛ", font_size=32, color=NONMETAL_COL, weight=BOLD)
        nm_title.next_to(nm_panel.get_top(), DOWN, buff=0.2)

        self.play(FadeIn(metal_panel), FadeIn(nm_panel),
                  Write(m_title), Write(nm_title), run_time=1.0)

        m_props = [
            "сјај — има",
            "спроводник",
            "кујен (пластичен)",
            "висока т. на топење",
            "висока густина",
        ]
        nm_props = [
            "сјај — нема",
            "изолатор",
            "кршлив",
            "ниска т. на топење",
            "ниска густина",
        ]

        y0 = 1.4
        for i, (mp, np_) in enumerate(zip(m_props, nm_props)):
            y = y0 - i*0.7
            mt = Text("• " + mp, font_size=22, color=WHITE2)
            mt.move_to([LEFT[0]*3.4 - 2.0, y, 0])
            mt.align_to(LEFT*5.4, LEFT)
            nmt = Text("• " + np_, font_size=22, color=WHITE2)
            nmt.move_to([3.4 - 2.0, y, 0])
            nmt.align_to(RIGHT*0.5, LEFT)
            self.play(FadeIn(mt), FadeIn(nmt), run_time=0.4)

        self.wait(1.8)

        self.play(FadeOut(VGroup(*[m for m in self.mobjects])))

        # ══════════════════════════════════════════════════════════
        # 5.  ПРИМЕРИ — три картички                           ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("examples")

        t5 = section_title("Со ликови — Fe, O, Si.")
        self.play(Write(t5), run_time=0.9)

        def char_card(symbol, name, role, color, pos):
            box = RoundedRectangle(
                width=4.0, height=3.5, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            ).move_to(pos)
            sym_circle = Circle(radius=0.7,
                                fill_color=color, fill_opacity=1,
                                stroke_color=WHITE2, stroke_width=2)
            sym_circle.move_to(box.get_center() + UP*0.8)
            sym = MathTex(symbol, color=WHITE2, font_size=40)
            sym.move_to(sym_circle)
            nm = Text(name, font_size=24, color=color, weight=BOLD)
            nm.move_to(box.get_center() + DOWN*0.2)
            rl = Text(role, font_size=20, color=WHITE2)
            rl.move_to(box.get_center() + DOWN*0.9)
            return VGroup(box, sym_circle, sym, nm, rl)

        c1 = char_card("Fe", "Железо", "метал — крв, мостови",
                       METAL_COL, LEFT*4.4 + DOWN*0.4)
        c2 = char_card("O", "Кислород", "неметал — дишење",
                       NONMETAL_COL, DOWN*0.4)
        c3 = char_card("Si", "Силициум", "металоид — чипови",
                       METALLOID_COL, RIGHT*4.4 + DOWN*0.4)

        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.play(FadeIn(c3), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t5, c1, c2, c3)))

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЗИМЕ                                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни.")
        self.play(Write(t7), run_time=0.8)

        b1 = callout("Лево — метали. Десно — неметали.",
                     width=11.0, border=METAL_COL, font_size=28)
        b1.move_to(UP*1.6)
        b2 = callout("На границата — металоиди.",
                     width=11.0, border=METALLOID_COL, font_size=28)
        b2.next_to(b1, DOWN, buff=0.35)
        b3 = callout("Метал блеска. Неметал молчи. Сите — потребни.",
                     width=11.0, border=YELLOW, font_size=28)
        b3.next_to(b2, DOWN, buff=0.35)

        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.0)

        finisher = Text("Менделејев.",
                        font_size=52, color=YELLOW, weight=BOLD)
        finisher.next_to(b3, DOWN, buff=0.55)
        self.play(Write(finisher), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, b1, b2, b3, finisher)))
        self.wait(0.5)
