"""
m8-3-1  —  Форми и геометриско размислување
Математика 8, Единица 3: Геометрија

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Render:  manim -ql m8-3-1.py M831Scene
Output:  media/videos/m8-3-1/480p15/M831Scene.mp4
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


class M831Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text(
            "Триаголникот собира до 180°.",
            font_size=44, color=YELLOW, weight=BOLD,
        )
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)

        beats = VGroup(
            Text("Секогаш.", font_size=38, color=WHITE2),
            Text("На Земја, на Месечина, во вселената.", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)

        finisher = Text("Геометријата нема исклучоци.",
                        font_size=40, color=ORANGE, weight=BOLD)
        finisher.next_to(beats, DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.4)
        self.wait(1.8)

        self.play(FadeOut(VGroup(hook, beats, finisher)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  TRIANGLE TYPES                                   ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("triangles")
        title = section_title("Видови триаголници")
        self.play(FadeIn(title), run_time=0.6)

        # Equilateral
        eq = Polygon(
            [-1, -0.8, 0], [1, -0.8, 0], [0, 0.93, 0],
            color=GREEN, fill_color=GREEN, fill_opacity=0.15, stroke_width=3,
        ).scale(0.7).move_to(LEFT * 4.5 + UP * 0.3)
        eq_lbl = Text("еднакво-\nстран", font_size=22, color=GREEN).next_to(eq, DOWN, buff=0.3)
        eq_info = Text("сите = 60°", font_size=20, color=WHITE2).next_to(eq_lbl, DOWN, buff=0.1)

        # Isosceles
        iso = Polygon(
            [-1, -0.8, 0], [1, -0.8, 0], [0, 1.3, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.15, stroke_width=3,
        ).scale(0.7).move_to(LEFT * 1.5 + UP * 0.3)
        iso_lbl = Text("рамно-\nкрак", font_size=22, color=BLUE).next_to(iso, DOWN, buff=0.3)
        iso_info = Text("2 страни =", font_size=20, color=WHITE2).next_to(iso_lbl, DOWN, buff=0.1)

        # Scalene
        sca = Polygon(
            [-1.1, -0.8, 0], [0.9, -0.8, 0], [-0.3, 1.0, 0],
            color=PURPLE, fill_color=PURPLE, fill_opacity=0.15, stroke_width=3,
        ).scale(0.7).move_to(RIGHT * 1.5 + UP * 0.3)
        sca_lbl = Text("разно-\nстран", font_size=22, color=PURPLE).next_to(sca, DOWN, buff=0.3)
        sca_info = Text("сите ≠", font_size=20, color=WHITE2).next_to(sca_lbl, DOWN, buff=0.1)

        # Right-angled
        rt = Polygon(
            [-0.8, -0.8, 0], [1.0, -0.8, 0], [-0.8, 1.0, 0],
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.15, stroke_width=3,
        ).scale(0.7).move_to(RIGHT * 4.5 + UP * 0.3)
        # small right angle square
        sq_mark = Square(side_length=0.15, color=ORANGE, stroke_width=2).move_to(
            rt.get_vertices()[0] + UP * 0.075 + RIGHT * 0.075)
        rt_lbl = Text("право-\nаголен", font_size=22, color=ORANGE).next_to(rt, DOWN, buff=0.3)
        rt_info = Text("еден = 90°", font_size=20, color=WHITE2).next_to(rt_lbl, DOWN, buff=0.1)

        all_tri = VGroup(eq, eq_lbl, eq_info, iso, iso_lbl, iso_info,
                         sca, sca_lbl, sca_info, rt, sq_mark, rt_lbl, rt_info)
        self.play(LaggedStartMap(FadeIn, all_tri, lag_ratio=0.12, run_time=2.5))
        self.wait(2.0)

        self.play(FadeOut(VGroup(title, all_tri)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ANGLE SUM 180°                                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("angles180")
        title2 = section_title("Збир на агли = 180°", color=GREEN)
        self.play(FadeIn(title2), run_time=0.6)

        tri = Polygon(
            [-2, -1.2, 0], [2, -1.2, 0], [0.4, 1.4, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.12, stroke_width=3,
        ).move_to(LEFT * 2 + DOWN * 0.2)

        a1 = Text("50°", font_size=28, color=YELLOW).move_to(
            tri.get_vertices()[0] + UP * 0.35 + RIGHT * 0.5)
        a2 = Text("70°", font_size=28, color=YELLOW).move_to(
            tri.get_vertices()[1] + UP * 0.35 + LEFT * 0.5)
        a3 = Text("?", font_size=36, color=RED, weight=BOLD).move_to(
            tri.get_vertices()[2] + DOWN * 0.45)

        self.play(Create(tri))
        self.play(FadeIn(a1), FadeIn(a2), FadeIn(a3))
        self.wait(0.5)

        eq1 = MathTex("50° + 70° + ? = 180°", font_size=40, color=WHITE2)
        eq2 = MathTex("? = 180° - 120° = 60°", font_size=44, color=GREEN)
        VGroup(eq1, eq2).arrange(DOWN, buff=0.4).move_to(RIGHT * 3.0 + UP * 0.2)
        self.play(Write(eq1), run_time=1.2)
        self.wait(0.4)
        self.play(Write(eq2), run_time=1.4)
        self.play(Transform(a3, Text("60°", font_size=28, color=GREEN, weight=BOLD).move_to(a3)))
        self.wait(1.6)

        self.play(FadeOut(VGroup(title2, tri, a1, a2, a3, eq1, eq2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  HYPOTENUSE                                       ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hypotenuse")
        title3 = section_title("Хипотенуза", color=ORANGE)
        self.play(FadeIn(title3), run_time=0.5)

        rt2 = Polygon(
            [-2, -1.2, 0], [2, -1.2, 0], [-2, 1.4, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.12, stroke_width=3,
        )
        sq2 = Square(side_length=0.25, color=BLUE, stroke_width=2).move_to(
            rt2.get_vertices()[0] + UP * 0.125 + RIGHT * 0.125)

        # mark hypotenuse
        hyp = Line(rt2.get_vertices()[1], rt2.get_vertices()[2],
                   color=ORANGE, stroke_width=6)
        hyp_lbl = Text("хипотенуза", font_size=28, color=ORANGE, weight=BOLD)
        hyp_lbl.next_to(hyp.get_center(), UR, buff=0.2)

        self.play(Create(rt2), Create(sq2))
        self.play(Create(hyp), FadeIn(hyp_lbl))
        self.wait(0.4)

        note = callout("спроти правиот агол  —  најдолгата страна",
                       width=8.5, border=ORANGE, font_size=26)
        note.shift(DOWN * 2.6)
        self.play(FadeIn(note))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title3, rt2, sq2, hyp, hyp_lbl, note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  QUADRILATERALS                                   ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("quad")
        title4 = section_title("Четириаголници", color=PURPLE)
        self.play(FadeIn(title4), run_time=0.6)

        # 6 shapes
        def make_quad(verts, color):
            return Polygon(*verts, color=color, fill_color=color,
                           fill_opacity=0.15, stroke_width=3)

        sq_s = make_quad([[-0.7,-0.7,0],[0.7,-0.7,0],[0.7,0.7,0],[-0.7,0.7,0]], GREEN)
        rect = make_quad([[-1.0,-0.5,0],[1.0,-0.5,0],[1.0,0.5,0],[-1.0,0.5,0]], BLUE)
        rhomb = make_quad([[0,-0.8,0],[0.8,0,0],[0,0.8,0],[-0.8,0,0]], YELLOW)
        para = make_quad([[-1.0,-0.5,0],[1.0,-0.5,0],[1.4,0.5,0],[-0.6,0.5,0]], ORANGE)
        trap = make_quad([[-1.0,-0.5,0],[1.0,-0.5,0],[0.6,0.5,0],[-0.6,0.5,0]], PURPLE)
        kite = make_quad([[0,-1.0,0],[0.6,0.0,0],[0,0.8,0],[-0.6,0.0,0]], RED)

        sq_s.move_to(LEFT * 4.5 + UP * 1.5)
        rect.move_to(ORIGIN + UP * 1.5)
        rhomb.move_to(RIGHT * 4.5 + UP * 1.5)
        para.move_to(LEFT * 4.5 + DOWN * 1.3)
        trap.move_to(ORIGIN + DOWN * 1.3)
        kite.move_to(RIGHT * 4.5 + DOWN * 1.3)

        labels = [
            (sq_s, "квадрат"), (rect, "правоаголник"), (rhomb, "ромб"),
            (para, "паралелограм"), (trap, "трапез"), (kite, "змеј"),
        ]
        full = VGroup()
        for shape, name in labels:
            full.add(shape)
            lbl = Text(name, font_size=22, color=WHITE2).next_to(shape, DOWN, buff=0.15)
            full.add(lbl)

        self.play(LaggedStartMap(FadeIn, full, lag_ratio=0.12, run_time=2.5))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title4, full)), run_time=0.7)

        # ── Sum of angles in quadrilateral ────────────────────
        title4b = section_title("Збир = 360°", color=GREEN)
        self.play(FadeIn(title4b), run_time=0.5)

        big_q = make_quad([[-2,-1.5,0],[2,-1.5,0],[2,1.5,0],[-2,1.5,0]], BLUE)
        big_q.move_to(LEFT * 2.5)
        ang_lbls = VGroup()
        positions = [
            (LEFT*2.5 + DOWN*1.0 + LEFT*0.5, "90°"),
            (LEFT*2.5 + DOWN*1.0 + RIGHT*1.5, "90°"),
            (LEFT*2.5 + UP*1.0 + RIGHT*1.5, "90°"),
            (LEFT*2.5 + UP*1.0 + LEFT*0.5, "90°"),
        ]
        for pos, txt in positions:
            ang_lbls.add(Text(txt, font_size=22, color=YELLOW).move_to(pos))

        self.play(Create(big_q))
        self.play(LaggedStartMap(FadeIn, ang_lbls, lag_ratio=0.2))

        sum_eq = MathTex("90°+90°+90°+90° = 360°",
                         font_size=36, color=GREEN)
        sum_eq.move_to(RIGHT * 3.0)
        self.play(Write(sum_eq), run_time=1.4)
        self.wait(1.8)
        self.play(FadeOut(VGroup(title4b, big_q, ang_lbls, sum_eq)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ANGLE TYPES                                      ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("angle_types")
        title5 = section_title("Видови агли")
        self.play(FadeIn(title5), run_time=0.5)

        def make_angle(deg, label, color, pos):
            r = 0.8
            arc = Arc(radius=r, start_angle=0,
                      angle=np.deg2rad(deg), color=color, stroke_width=4)
            line1 = Line(ORIGIN, RIGHT * (r + 0.3), color=WHITE2, stroke_width=3)
            end = np.array([np.cos(np.deg2rad(deg)), np.sin(np.deg2rad(deg)), 0]) * (r + 0.3)
            line2 = Line(ORIGIN, end, color=WHITE2, stroke_width=3)
            lbl = Text(label, font_size=22, color=color, weight=BOLD)
            grp = VGroup(line1, line2, arc, lbl)
            grp.move_to(pos)
            lbl.next_to(VGroup(line1, line2, arc), DOWN, buff=0.4)
            return grp

        acute = make_angle(45, "остар  <90°", BLUE, LEFT * 4.5 + UP * 0.3)
        right = make_angle(90, "прав  =90°", GREEN, LEFT * 1.5 + UP * 0.3)
        obtuse = make_angle(130, "тап  >90°", ORANGE, RIGHT * 1.8 + UP * 0.3)
        straight = make_angle(180, "испружен  180°", PURPLE, RIGHT * 4.8 + UP * 0.3)

        self.play(LaggedStart(FadeIn(acute), FadeIn(right), FadeIn(obtuse), FadeIn(straight),
                              lag_ratio=0.3))
        self.wait(2.5)

        self.play(FadeOut(VGroup(title5, acute, right, obtuse, straight)), run_time=0.7)

        # ── Complementary / supplementary ────────────────────
        title5b = section_title("Парови агли", color=BLUE)
        self.play(FadeIn(title5b), run_time=0.5)

        c1 = Text("Комплементарни:  збир 90°", font_size=30, color=GREEN)
        c2 = Text("Суплементарни:    збир 180°", font_size=30, color=ORANGE)
        c3 = Text("Вертикални:           еднакви", font_size=30, color=PURPLE)
        VGroup(c1, c2, c3).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(ORIGIN)
        for c in [c1, c2, c3]:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.5)
            self.wait(0.25)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title5b, c1, c2, c3)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  PARALLEL LINES WITH TRANSVERSAL                  ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("parallel")
        title6 = section_title("Паралелни со пресечник", color=ORANGE)
        self.play(FadeIn(title6), run_time=0.5)

        line1 = Line(LEFT * 5, RIGHT * 5, color=BLUE, stroke_width=3).shift(UP * 1.2)
        line2 = Line(LEFT * 5, RIGHT * 5, color=BLUE, stroke_width=3).shift(DOWN * 1.2)
        # transversal (sloped)
        tline = Line([-2.5, 2.5, 0], [2.5, -2.5, 0], color=ORANGE, stroke_width=3)

        self.play(Create(line1), Create(line2))
        self.play(Create(tline))
        self.wait(0.4)

        # mark angles with small dots
        # corresponding angles "F"
        d1 = Dot(line1.get_center() + LEFT*1.1 + UP*0.18, color=GREEN, radius=0.1)
        d2 = Dot(line2.get_center() + LEFT*1.1 + UP*0.18, color=GREEN, radius=0.1)
        cor_lbl = Text("F  —  соодветни", font_size=24, color=GREEN)
        cor_lbl.move_to(RIGHT * 3.5 + UP * 1.5)
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(cor_lbl))
        self.wait(0.5)

        # alternate Z
        z1 = Dot(line1.get_center() + RIGHT*0.4 + DOWN*0.18, color=YELLOW, radius=0.1)
        z2 = Dot(line2.get_center() + LEFT*0.4 + UP*0.18, color=YELLOW, radius=0.1)
        alt_lbl = Text("Z  —  наизменични", font_size=24, color=YELLOW)
        alt_lbl.move_to(RIGHT * 3.5 + UP * 0.5)
        self.play(FadeIn(z1), FadeIn(z2), FadeIn(alt_lbl))
        self.wait(0.5)

        # co-interior C
        c1d = Dot(line1.get_center() + RIGHT*0.4 + DOWN*0.18, color=PURPLE, radius=0.08)
        c2d = Dot(line2.get_center() + RIGHT*0.4 + UP*0.18, color=PURPLE, radius=0.08)
        co_lbl = Text("C  —  внатрешни (180°)", font_size=24, color=PURPLE)
        co_lbl.move_to(RIGHT * 3.5 + DOWN * 0.5)
        self.play(FadeIn(c1d), FadeIn(c2d), FadeIn(co_lbl))
        self.wait(2.0)

        self.play(FadeOut(VGroup(title6, line1, line2, tline, d1, d2, z1, z2,
                                 c1d, c2d, cor_lbl, alt_lbl, co_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 8.  SYMMETRY                                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("symmetry")
        title7 = section_title("Оски на симетрија", color=YELLOW)
        self.play(FadeIn(title7), run_time=0.5)

        # Square
        sq_sym = Square(side_length=1.6, color=GREEN, fill_color=GREEN,
                        fill_opacity=0.1, stroke_width=3).move_to(LEFT * 4.5)
        sq_axes = VGroup(
            Line(LEFT * 4.5 + UP * 1.0, LEFT * 4.5 + DOWN * 1.0, color=YELLOW),
            Line(LEFT * 5.5 + ORIGIN[1] * UP, LEFT * 3.5 + ORIGIN[1] * UP, color=YELLOW),
            DashedLine(LEFT * 5.3 + UP * 0.8, LEFT * 3.7 + DOWN * 0.8, color=YELLOW),
            DashedLine(LEFT * 5.3 + DOWN * 0.8, LEFT * 3.7 + UP * 0.8, color=YELLOW),
        )
        sq_lbl = Text("квадрат  —  4", font_size=24, color=GREEN).next_to(sq_sym, DOWN, buff=0.5)

        # Rectangle
        rc_sym = Rectangle(width=2.0, height=1.2, color=BLUE, fill_color=BLUE,
                           fill_opacity=0.1, stroke_width=3).move_to(LEFT * 1.0)
        rc_axes = VGroup(
            Line(LEFT * 1.0 + UP * 0.8, LEFT * 1.0 + DOWN * 0.8, color=YELLOW),
            Line(LEFT * 2.0, ORIGIN, color=YELLOW),
        )
        rc_lbl = Text("правоаголник  —  2", font_size=24, color=BLUE).next_to(rc_sym, DOWN, buff=0.5)

        # Circle
        cir_sym = Circle(radius=1.0, color=ORANGE, fill_color=ORANGE,
                         fill_opacity=0.1, stroke_width=3).move_to(RIGHT * 3.5)
        # several dashed axes
        cir_axes = VGroup()
        for ang in [0, 30, 60, 90, 120, 150]:
            d = np.deg2rad(ang)
            v = np.array([np.cos(d), np.sin(d), 0])
            cir_axes.add(DashedLine(
                RIGHT * 3.5 + v * 1.2, RIGHT * 3.5 - v * 1.2,
                color=YELLOW, stroke_width=1.5))
        cir_lbl = Text("круг  —  бесконечно", font_size=22, color=ORANGE).next_to(cir_sym, DOWN, buff=0.5)

        self.play(Create(sq_sym), Create(rc_sym), Create(cir_sym))
        self.play(LaggedStartMap(Create, sq_axes, lag_ratio=0.2),
                  LaggedStartMap(Create, rc_axes, lag_ratio=0.2),
                  LaggedStartMap(Create, cir_axes, lag_ratio=0.1))
        self.play(FadeIn(sq_lbl), FadeIn(rc_lbl), FadeIn(cir_lbl))
        self.wait(2.5)

        self.play(FadeOut(VGroup(title7, sq_sym, sq_axes, sq_lbl,
                                 rc_sym, rc_axes, rc_lbl,
                                 cir_sym, cir_axes, cir_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 9.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")
        sum_title = section_title("Заклучок")
        self.play(FadeIn(sum_title), run_time=0.5)

        s1 = Text("Триаголник — 180°.", font_size=34, color=BLUE)
        s2 = Text("Четириаголник — 360°.", font_size=34, color=GREEN)
        s3 = Text("Круг — бесконечни симетрии.", font_size=34, color=ORANGE)
        end = Text("Геометријата не лаже.",
                   font_size=40, color=YELLOW, weight=BOLD)

        VGroup(s1, s2, s3, end).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for s in [s1, s2, s3]:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.play(Write(end), run_time=1.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sum_title, s1, s2, s3, end)), run_time=0.8)
