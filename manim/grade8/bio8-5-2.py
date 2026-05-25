"""
bio8-5-2  —  Гени и наследување — основи
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: DNA as book,
genes as words, inheritance as silent translation.
Render:  manim -ql bio8-5-2.py Bio852Scene
Output:  media/videos/bio8-5-2/480p15/Bio852Scene.mp4
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


def dna_helix(width=4.0, color1=BLUE, color2=ORANGE, rungs=10):
    """Returns a stylized DNA double helix."""
    g = VGroup()
    xs = np.linspace(-width/2, width/2, 200)
    strand1 = VMobject(stroke_color=color1, stroke_width=4)
    strand2 = VMobject(stroke_color=color2, stroke_width=4)
    pts1 = [np.array([x, 0.45 * np.sin(x * 2.0), 0]) for x in xs]
    pts2 = [np.array([x, -0.45 * np.sin(x * 2.0), 0]) for x in xs]
    strand1.set_points_smoothly(pts1)
    strand2.set_points_smoothly(pts2)
    g.add(strand1, strand2)
    rung_xs = np.linspace(-width/2 + 0.2, width/2 - 0.2, rungs)
    for x in rung_xs:
        y1 = 0.45 * np.sin(x * 2.0)
        y2 = -0.45 * np.sin(x * 2.0)
        line = Line([x, y1, 0], [x, y2, 0], color=GREY, stroke_width=2)
        g.add(line)
    return g


class Bio852Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("ДНК е книга.",       font_size=52, color=YELLOW, weight=BOLD)
        hook2 = Text("Гените се зборови.", font_size=46, color=BLUE,   weight=BOLD)
        hook3 = Text("Хромозомите се поглавја.", font_size=42, color=ORANGE)
        hook4 = Text("Цела приказна — во една клетка.",
                     font_size=36, color=GREEN, weight=BOLD)

        beats = VGroup(hook1, hook2, hook3, hook4).arrange(DOWN, buff=0.5)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(Write(b), run_time=1.0)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е ГЕН?                                       ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("what_is_gene")

        t2 = section_title("Што е ген?")
        self.play(Write(t2), run_time=0.9)

        helix = dna_helix(width=6.0, rungs=14)
        helix.shift(UP * 0.5)
        self.play(Create(helix), run_time=1.4)

        defn = callout("Ген = парче ДНК кое кодира една особина.",
                       width=10.5, border=YELLOW, font_size=28)
        defn.next_to(helix, DOWN, buff=0.7)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.8)

        # highlight one "gene" segment
        seg = Rectangle(
            width=1.0, height=1.4,
            stroke_color=YELLOW, stroke_width=3,
            fill_color=YELLOW, fill_opacity=0.15,
        )
        seg.move_to(helix.get_center() + LEFT * 1.5)
        seg_label = Text("еден ген", font_size=22, color=YELLOW)
        seg_label.next_to(seg, UP, buff=0.15)

        self.play(Create(seg), Write(seg_label), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, helix, defn, seg, seg_label)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ХРОМОЗОМИ                                         ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chromosomes")

        t3 = section_title("Хромозоми")
        self.play(Write(t3), run_time=0.9)

        sub = Text("Кај човек: 23 пара = 46 хромозоми.",
                   font_size=30, color=WHITE2)
        sub.next_to(t3, DOWN, buff=0.3)
        self.play(Write(sub), run_time=1.0)

        # draw 23 pairs in a grid
        pairs = VGroup()
        for i in range(23):
            row = i // 8
            col = i % 8
            x = -5.0 + col * 1.3
            y = -0.5 - row * 1.4
            chrom1 = RoundedRectangle(
                width=0.22, height=0.85, corner_radius=0.1,
                fill_color=BLUE, fill_opacity=0.85, stroke_width=0,
            ).move_to([x - 0.15, y, 0])
            chrom2 = RoundedRectangle(
                width=0.22, height=0.85, corner_radius=0.1,
                fill_color=ORANGE, fill_opacity=0.85, stroke_width=0,
            ).move_to([x + 0.15, y, 0])
            num = Text(str(i + 1), font_size=14, color=GREY)
            num.next_to(VGroup(chrom1, chrom2), DOWN, buff=0.08)
            pairs.add(VGroup(chrom1, chrom2, num))

        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in pairs],
                              lag_ratio=0.05), run_time=2.0)

        self.wait(0.5)

        explain = Text("Половина од мајка. Половина од татко.",
                       font_size=30, color=YELLOW, weight=BOLD)
        explain.to_edge(DOWN, buff=0.4)
        self.play(Write(explain), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, sub, pairs, explain)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  АЛЕЛИ — ДОМИНАНТЕН/РЕЦЕСИВЕН                     ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("alleles")

        t4 = section_title("Алели")
        self.play(Write(t4), run_time=0.9)

        defn4 = callout("Алел = различна верзија на ист ген.",
                        width=10.0, border=YELLOW, font_size=28)
        defn4.next_to(t4, DOWN, buff=0.4)
        self.play(FadeIn(defn4, shift=UP * 0.2), run_time=0.8)

        # two big letters
        big_A = Text("A", font_size=120, color=BLUE, weight=BOLD)
        big_a = Text("a", font_size=120, color=ORANGE, weight=BOLD)
        big_A.shift(LEFT * 2.5 + DOWN * 0.5)
        big_a.shift(RIGHT * 2.5 + DOWN * 0.5)

        dom = Text("доминантен", font_size=28, color=BLUE, weight=BOLD)
        dom.next_to(big_A, DOWN, buff=0.3)
        rec = Text("рецесивен", font_size=28, color=ORANGE, weight=BOLD)
        rec.next_to(big_a, DOWN, buff=0.3)

        self.play(Write(big_A), Write(dom), run_time=0.9)
        self.play(Write(big_a), Write(rec), run_time=0.9)
        self.wait(0.4)

        rule = Text("Ако се сретнат — доминантниот командува.",
                    font_size=30, color=YELLOW, weight=BOLD)
        rule.to_edge(DOWN, buff=0.4)
        self.play(Write(rule), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t4, defn4, big_A, big_a, dom, rec, rule)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ПЕНЕТОВ КВАДРАТ                                  ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("punnett")

        t5 = section_title("Пенетов квадрат")
        self.play(Write(t5), run_time=0.9)

        sub5 = Text("Како се мешаат алели?",
                    font_size=28, color=WHITE2)
        sub5.next_to(t5, DOWN, buff=0.3)
        self.play(Write(sub5), run_time=0.8)

        # 2x2 grid
        cell_size = 1.2
        grid = VGroup()
        labels_alleles = [["A", "a"], ["A", "a"]]
        contents = [["AA", "Aa"], ["Aa", "aa"]]
        content_colors = [[BLUE, GREEN], [GREEN, ORANGE]]

        offset_x = 0.0
        offset_y = -0.6

        # parent labels (top row)
        for j, lab in enumerate(["A", "a"]):
            t = Text(lab, font_size=40, color=BLUE, weight=BOLD)
            t.move_to([offset_x + (j - 0.5) * cell_size, offset_y + 1.5 * cell_size, 0])
            grid.add(t)
        # parent labels (left col)
        for i, lab in enumerate(["A", "a"]):
            t = Text(lab, font_size=40, color=ORANGE, weight=BOLD)
            t.move_to([offset_x - 1.5 * cell_size, offset_y + (0.5 - i) * cell_size, 0])
            grid.add(t)

        # cells
        cells = VGroup()
        for i in range(2):
            for j in range(2):
                cell = Square(
                    side_length=cell_size,
                    stroke_color=WHITE2, stroke_width=2,
                    fill_color=DARK_CARD, fill_opacity=1,
                )
                cell.move_to([offset_x + (j - 0.5) * cell_size,
                              offset_y + (0.5 - i) * cell_size, 0])
                cells.add(cell)
        grid.add(cells)

        self.play(Create(grid), run_time=1.5)

        # fill in
        for i in range(2):
            for j in range(2):
                t = Text(contents[i][j], font_size=34,
                         color=content_colors[i][j], weight=BOLD)
                t.move_to(cells[i * 2 + j])
                self.play(Write(t), run_time=0.5)

        self.wait(0.4)

        result = VGroup(
            Text("AA : Aa : aa  =  1 : 2 : 1",
                 font_size=32, color=YELLOW, weight=BOLD),
            Text("3 со доминантна особина, 1 со рецесивна.",
                 font_size=28, color=WHITE2),
        ).arrange(DOWN, buff=0.25)
        result.to_edge(DOWN, buff=0.4)

        for r in result:
            self.play(Write(r), run_time=0.9)

        self.wait(1.8)
        self.play(FadeOut(VGroup(t5, sub5, grid, result, *self.mobjects)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  ПРИМЕР: БОЈА НА ОЧИ                              ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("eye_color")

        t6 = section_title("Боја на очи")
        self.play(Write(t6), run_time=0.9)

        # two parents
        mom_eye = VGroup(
            Circle(radius=0.45, color=WHITE2, fill_color=WHITE2, fill_opacity=1, stroke_width=0),
            Circle(radius=0.2, color="#5a3a1f", fill_color="#5a3a1f", fill_opacity=1, stroke_width=0),
        )
        mom_eye[1].move_to(mom_eye[0])
        mom_label = Text("Мајка: Bb", font_size=26, color=ORANGE, weight=BOLD)
        mom_group = VGroup(mom_eye, mom_label).arrange(DOWN, buff=0.25)
        mom_group.shift(LEFT * 3.5 + UP * 0.5)

        dad_eye = VGroup(
            Circle(radius=0.45, color=WHITE2, fill_color=WHITE2, fill_opacity=1, stroke_width=0),
            Circle(radius=0.2, color="#1f5a8a", fill_color="#1f5a8a", fill_opacity=1, stroke_width=0),
        )
        dad_eye[1].move_to(dad_eye[0])
        dad_label = Text("Татко: bb", font_size=26, color=BLUE, weight=BOLD)
        dad_group = VGroup(dad_eye, dad_label).arrange(DOWN, buff=0.25)
        dad_group.shift(RIGHT * 3.5 + UP * 0.5)

        self.play(FadeIn(mom_group, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(dad_group, shift=UP * 0.2), run_time=0.7)

        # arrows down
        arrow_l = Arrow(mom_group.get_bottom(), DOWN * 0.7 + LEFT * 1.5,
                        color=GREY, buff=0.2)
        arrow_r = Arrow(dad_group.get_bottom(), DOWN * 0.7 + RIGHT * 1.5,
                        color=GREY, buff=0.2)
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.8)

        # outcomes
        out_brown = Text("50% кафена (Bb)", font_size=30, color="#8a5a2f", weight=BOLD)
        out_brown.shift(LEFT * 2.5 + DOWN * 2.2)
        out_blue = Text("50% сина (bb)", font_size=30, color=BLUE, weight=BOLD)
        out_blue.shift(RIGHT * 2.5 + DOWN * 2.2)

        self.play(Write(out_brown), Write(out_blue), run_time=1.0)
        self.wait(0.5)

        punch = Text("Гените одлучуваат. Шансата меша.",
                     font_size=30, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.4)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            t6, mom_group, dad_group, arrow_l, arrow_r,
            out_brown, out_blue, punch)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("ДНК — книга на животот.",
                      font_size=46, color=YELLOW, weight=BOLD)
        final2 = Text("Гените — букви.",
                      font_size=42, color=BLUE,   weight=BOLD)
        final3 = Text("Алели — варијанти.",
                      font_size=40, color=ORANGE, weight=BOLD)
        final4 = Text("Наследувањето — препишување.",
                      font_size=38, color=GREEN, weight=BOLD)

        finals = VGroup(final1, final2, final3, final4).arrange(DOWN, buff=0.45)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.9)
            self.wait(0.3)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
