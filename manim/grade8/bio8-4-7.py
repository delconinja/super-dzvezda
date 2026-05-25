"""
bio8-4-7  —  Крвни групи и трансфузија
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
A, B, AB, O — wrong match catastrophe, right match a saved life.
Render:  manim -ql bio8-4-7.py Bio847Scene
Output:  media/videos/bio8-4-7/480p15/Bio847Scene.mp4
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


def rbc_with_antigens(antigens, color=RED, pos=ORIGIN, radius=0.5):
    """Returns a small RBC with antigen markers."""
    cell = Circle(radius=radius, color=color,
                  fill_color=color, fill_opacity=0.85,
                  stroke_color=WHITE2, stroke_width=1.5)
    cell.move_to(pos)
    grp = VGroup(cell)

    n = len(antigens)
    if n > 0:
        angles = np.linspace(0, TAU, n, endpoint=False)
        for ant, ang in zip(antigens, angles):
            color_a = YELLOW if ant == "A" else (BLUE if ant == "B" else GREY)
            tri = Triangle(color=color_a, fill_color=color_a,
                           fill_opacity=0.95, stroke_color=WHITE2,
                           stroke_width=1)
            tri.scale(0.12)
            tri.move_to(pos + radius * 1.0 * np.array([np.cos(ang), np.sin(ang), 0]))
            tri.rotate(ang - PI / 2)
            grp.add(tri)
    return grp


class Bio847Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Не секоја крв е иста.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)

        beats = VGroup(
            Text("A, B, AB, O.",
                 font_size=40, color=BLUE, weight=BOLD),
            Text("Плус, минус.",
                 font_size=34, color=ORANGE),
            Text("Погрешен спој — катастрофа.",
                 font_size=32, color=RED, weight=BOLD),
            Text("Точен спој — спасување живот.",
                 font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ABO SYSTEM — 4 GROUPS                            ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("abo")

        title = section_title("ABO систем — четири групи")
        self.play(Write(title), run_time=0.8)

        # 4 RBC representations
        groups = [
            ("A",  ["A", "A", "A"],     LEFT * 4.5),
            ("B",  ["B", "B", "B"],     LEFT * 1.5),
            ("AB", ["A", "B", "A", "B"], RIGHT * 1.5),
            ("O",  [],                  RIGHT * 4.5),
        ]
        cells_g = VGroup()
        labels_g = VGroup()
        for name, ants, pos in groups:
            cell = rbc_with_antigens(ants, color=RED,
                                     pos=pos + UP * 0.7, radius=0.6)
            lbl_name = Text(name, font_size=40, color=YELLOW, weight=BOLD)
            lbl_name.move_to(pos + DOWN * 0.6)
            cells_g.add(cell)
            labels_g.add(lbl_name)

        self.play(LaggedStart(*[FadeIn(c, scale=0.6) for c in cells_g],
                              lag_ratio=0.2), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(l) for l in labels_g],
                              lag_ratio=0.2), run_time=0.8)

        # antigen legend
        leg = VGroup(
            Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.95).scale(0.18),
            Text("антиген A", font_size=22, color=YELLOW),
            Triangle(color=BLUE, fill_color=BLUE, fill_opacity=0.95).scale(0.18),
            Text("антиген B", font_size=22, color=BLUE),
        ).arrange(RIGHT, buff=0.3)
        leg.move_to(DOWN * 1.8)

        self.play(FadeIn(leg), run_time=0.7)

        # explanation
        note = callout("A има антиген A. B има антиген B. AB има обата. O нема ништо.",
                       width=13.0, border=GREEN, font_size=22)
        note.move_to(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, cells_g, labels_g, leg, note)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  RH FACTOR                                        ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rh")

        title = section_title("Rh фактор — плус или минус", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        # two cells — one with Rh marker, one without
        cell_plus = Circle(radius=1.0, color=RED,
                           fill_color=RED, fill_opacity=0.85,
                           stroke_color=WHITE2, stroke_width=2)
        cell_plus.move_to(LEFT * 3.5 + UP * 0.3)

        # purple markers around it
        rh_markers = VGroup()
        for ang in np.linspace(0, TAU, 6, endpoint=False):
            sq = RegularPolygon(n=4, color=PURPLE,
                                fill_color=PURPLE, fill_opacity=0.95,
                                stroke_color=WHITE2, stroke_width=1)
            sq.scale(0.18).move_to(cell_plus.get_center() +
                                   1.0 * np.array([np.cos(ang), np.sin(ang), 0]))
            sq.rotate(ang - PI / 4)
            rh_markers.add(sq)

        lbl_plus = Text("Rh+", font_size=44, color=PURPLE, weight=BOLD)
        lbl_plus.next_to(cell_plus, DOWN, buff=0.5)
        plus_desc = Text("има Rh антиген", font_size=22, color=WHITE2)
        plus_desc.next_to(lbl_plus, DOWN, buff=0.25)

        # negative cell — no markers
        cell_minus = Circle(radius=1.0, color=RED,
                            fill_color=RED, fill_opacity=0.85,
                            stroke_color=WHITE2, stroke_width=2)
        cell_minus.move_to(RIGHT * 3.5 + UP * 0.3)

        lbl_minus = Text("Rh−", font_size=44, color=BLUE, weight=BOLD)
        lbl_minus.next_to(cell_minus, DOWN, buff=0.5)
        minus_desc = Text("нема Rh антиген", font_size=22, color=WHITE2)
        minus_desc.next_to(lbl_minus, DOWN, buff=0.25)

        self.play(Create(cell_plus), Create(cell_minus), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(m, scale=0.5) for m in rh_markers],
                              lag_ratio=0.1), run_time=0.9)
        self.play(FadeIn(lbl_plus), FadeIn(plus_desc),
                  FadeIn(lbl_minus), FadeIn(minus_desc), run_time=0.7)

        note = callout("85% од луѓето се Rh+, само 15% се Rh−",
                       width=10.0, border=YELLOW, font_size=24)
        note.move_to(DOWN * 2.7)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, cell_plus, cell_minus, rh_markers,
                                 lbl_plus, plus_desc, lbl_minus, minus_desc,
                                 note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  WRONG MATCH — AGGLUTINATION                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("wrong")

        title = section_title("Погрешен спој — катастрофа", color=RED)
        self.play(Write(title), run_time=0.8)

        # left side — donor B blood into recipient A
        donor_lbl = Text("Донатор: B", font_size=26, color=BLUE, weight=BOLD)
        donor_lbl.move_to(LEFT * 4.0 + UP * 2.4)
        recip_lbl = Text("Прима: A", font_size=26, color=YELLOW, weight=BOLD)
        recip_lbl.move_to(LEFT * 4.0 + UP * 1.7)

        # donor cells with B antigens
        donor_cells = VGroup(*[
            rbc_with_antigens(["B", "B"], color=RED,
                              pos=LEFT * 4.0 + DOWN * 0.5 + RIGHT * (i * 0.9 - 1.0),
                              radius=0.3)
            for i in range(3)
        ])

        # recipient antibodies — anti-B (small Y shapes as antibodies)
        anti_b = VGroup()
        for i in range(5):
            base = Line(ORIGIN, UP * 0.3, color=BLUE, stroke_width=3)
            l = Line(UP * 0.3, UP * 0.5 + LEFT * 0.15,
                     color=BLUE, stroke_width=3)
            r = Line(UP * 0.3, UP * 0.5 + RIGHT * 0.15,
                     color=BLUE, stroke_width=3)
            y = VGroup(base, l, r)
            y.move_to(LEFT * (4.0 + np.random.uniform(-1.2, 1.2)) +
                      DOWN * np.random.uniform(0.7, 1.5))
            anti_b.add(y)
        ab_lbl = Text("анти-B антитела", font_size=20, color=BLUE)
        ab_lbl.move_to(LEFT * 4.0 + DOWN * 2.3)

        # right side — agglutination result
        clump = VGroup()
        for x, y in [(2.0, 0.5), (2.5, 0.7), (2.4, 0.0), (3.0, 0.3),
                     (2.7, -0.5), (3.2, -0.2), (3.5, 0.4)]:
            c = Circle(radius=0.32, color=RED,
                       fill_color=RED, fill_opacity=0.9,
                       stroke_color=DARK_CARD, stroke_width=1.5)
            c.move_to(RIGHT * x + UP * y)
            clump.add(c)

        clump_lbl = Text("аглутинација — клетките се лепат",
                         font_size=22, color=RED, weight=BOLD)
        clump_lbl.move_to(RIGHT * 3.0 + UP * 1.7)

        # consequences below clump
        cons = VGroup(
            Text("закнирани капилари", font_size=20, color=ORANGE),
            Text("оштетени бубрези",   font_size=20, color=ORANGE),
            Text("шок и смрт",         font_size=22, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        cons.move_to(RIGHT * 3.0 + DOWN * 1.6)

        self.play(FadeIn(donor_lbl), FadeIn(recip_lbl), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(c) for c in donor_cells],
                              lag_ratio=0.15), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(y, scale=0.5) for y in anti_b],
                              lag_ratio=0.1), FadeIn(ab_lbl), run_time=0.9)

        big_arr = Arrow(LEFT * 1.5, RIGHT * 1.0, color=RED,
                        buff=0, stroke_width=6)
        big_arr.move_to(UP * 0.0)
        self.play(GrowArrow(big_arr), run_time=0.6)

        self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in clump],
                              lag_ratio=0.1),
                  FadeIn(clump_lbl), run_time=1.0)
        for c in cons:
            self.play(FadeIn(c, shift=LEFT * 0.2), run_time=0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, donor_lbl, recip_lbl, donor_cells,
                                 anti_b, ab_lbl, big_arr, clump, clump_lbl, cons)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  COMPATIBILITY MATRIX                             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("matrix")

        title = section_title("Кој на кого може")
        self.play(Write(title), run_time=0.8)

        # 5x5 grid (header + 4 rows)
        cell_w = 1.4
        cell_h = 0.7
        grid_origin = LEFT * 3.0 + UP * 1.4

        headers_x = ["прима↓ \\ дава→", "O", "A", "B", "AB"]
        headers_y = ["O", "A", "B", "AB"]
        # compatibility: rows = recipient, cols = donor
        # True = can receive
        comp = [
            [True,  False, False, False],  # O receives only O
            [True,  True,  False, False],  # A receives O, A
            [True,  False, True,  False],  # B receives O, B
            [True,  True,  True,  True],   # AB receives all
        ]

        grid_elems = VGroup()
        # top row labels
        for i, h in enumerate(headers_x):
            box = RoundedRectangle(width=cell_w, height=cell_h,
                                   corner_radius=0.1,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=YELLOW, stroke_width=1.5)
            box.move_to(grid_origin + RIGHT * i * cell_w)
            font_size = 16 if i == 0 else 24
            color = ORANGE if i == 0 else YELLOW
            t = Text(h, font_size=font_size, color=color, weight=BOLD)
            t.move_to(box)
            grid_elems.add(VGroup(box, t))

        for r in range(4):
            # left header
            box = RoundedRectangle(width=cell_w, height=cell_h,
                                   corner_radius=0.1,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=YELLOW, stroke_width=1.5)
            box.move_to(grid_origin + DOWN * (r + 1) * cell_h)
            t = Text(headers_y[r], font_size=24, color=YELLOW, weight=BOLD)
            t.move_to(box)
            grid_elems.add(VGroup(box, t))

            for c in range(4):
                cellb = RoundedRectangle(width=cell_w, height=cell_h,
                                         corner_radius=0.1,
                                         fill_color=DARK_CARD, fill_opacity=1,
                                         stroke_color=WHITE2, stroke_width=1)
                cellb.move_to(grid_origin + RIGHT * (c + 1) * cell_w +
                              DOWN * (r + 1) * cell_h)
                if comp[r][c]:
                    sym = Text("✓", font_size=32, color=GREEN, weight=BOLD)
                    cellb.set_stroke(GREEN, width=1.5)
                else:
                    sym = Text("✗", font_size=32, color=RED, weight=BOLD)
                    cellb.set_stroke(RED, width=1.5)
                sym.move_to(cellb)
                grid_elems.add(VGroup(cellb, sym))

        self.play(LaggedStart(*[FadeIn(e) for e in grid_elems],
                              lag_ratio=0.04), run_time=2.5)

        # highlights — O universal donor, AB universal recipient
        note1 = callout("O− — универзален донатор",
                        width=6.5, border=BLUE, font_size=22)
        note1.move_to(RIGHT * 4.0 + UP * 1.5)
        note2 = callout("AB+ — универзален примач",
                        width=6.5, border=GREEN, font_size=22)
        note2.move_to(RIGHT * 4.0 + DOWN * 0.0)

        self.play(FadeIn(note1), run_time=0.7)
        self.play(FadeIn(note2), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, grid_elems, note1, note2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  POPULATION FREQUENCY + IMPORTANCE                ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("frequency")

        title = section_title("Распределба и значење")
        self.play(Write(title), run_time=0.8)

        # bar chart — % of each blood group (rough world)
        freq = [
            ("O+",  37, GREEN),
            ("A+",  33, YELLOW),
            ("B+",  10, BLUE),
            ("AB+",  3, PURPLE),
            ("O−",   7, ORANGE),
            ("A−",   6, RED),
            ("B−",   2, GREY),
            ("AB−",  1, WHITE2),
        ]

        bars = VGroup()
        bar_labels = VGroup()
        max_h = 3.0
        for i, (n, p, col) in enumerate(freq):
            h = (p / 40) * max_h
            bar = Rectangle(width=0.7, height=max(h, 0.15),
                            fill_color=col, fill_opacity=0.85,
                            stroke_color=WHITE2, stroke_width=1)
            bar.move_to(LEFT * 5.0 + RIGHT * i * 1.2 + DOWN * 1.3 + UP * h / 2)
            lbl = Text(n, font_size=18, color=col, weight=BOLD)
            lbl.next_to(bar, DOWN, buff=0.15)
            pct = Text(f"{p}%", font_size=16, color=WHITE2)
            pct.next_to(bar, UP, buff=0.1)
            bars.add(bar)
            bar_labels.add(VGroup(lbl, pct))

        # x-axis line
        base_line = Line(LEFT * 5.5 + DOWN * 1.35,
                         RIGHT * 4.5 + DOWN * 1.35,
                         color=GREY, stroke_width=1.5)

        self.play(Create(base_line), run_time=0.4)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                              lag_ratio=0.1), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(l) for l in bar_labels],
                              lag_ratio=0.1), run_time=1.0)

        # importance bottom note
        why = VGroup(
            Text("Зошто е важно:", font_size=22, color=YELLOW, weight=BOLD),
            Text("• трансфузија на крв", font_size=20, color=WHITE2),
            Text("• бременост (Rh некомпатибилност)", font_size=20, color=WHITE2),
            Text("• трансплантација на органи", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        why.move_to(DOWN * 2.6)

        for w in why:
            self.play(FadeIn(w, shift=LEFT * 0.2), run_time=0.35)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, base_line, bars, bar_labels, why)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Четири групи: A, B, AB, O.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Плус или минус — Rh фактор.",
                 font_size=28, color=PURPLE),
            Text("O− дава на сите. AB+ прима од сите.",
                 font_size=26, color=BLUE),
            Text("Погрешен спој — катастрофа.",
                 font_size=28, color=RED, weight=BOLD),
            Text("Точен спој — спасен живот.",
                 font_size=30, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.6)

        for b in bullets:
            self.play(Write(b), run_time=0.6)
            self.wait(0.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
