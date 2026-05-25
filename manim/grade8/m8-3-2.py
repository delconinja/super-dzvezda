"""
m8-3-2  —  Положба и движење
Математика 8, Единица 3: Геометрија

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Render:  manim -ql m8-3-2.py M832Scene
Output:  media/videos/m8-3-2/480p15/M832Scene.mp4
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


class M832Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text(
            "Точка не е место.",
            font_size=46, color=YELLOW, weight=BOLD,
        )
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)

        beats = VGroup(
            Text("Точка е координати.", font_size=38, color=BLUE),
            Text("Без координати — таа е никаде.", font_size=34, color=WHITE2),
            Text("Со два броја — секаде.", font_size=34, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.6)
            self.wait(0.3)

        self.wait(1.4)
        self.play(FadeOut(VGroup(hook, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  COORDINATE SYSTEM AND QUADRANTS                  ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("coord")
        title = section_title("Координатен систем")
        self.play(FadeIn(title), run_time=0.6)

        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=8.0, y_length=5.4,
            axis_config={"color": WHITE2, "stroke_width": 2,
                         "include_numbers": True, "font_size": 20},
            tips=True,
        )
        axes.move_to(DOWN * 0.2)
        x_lbl = Text("x", font_size=28, color=WHITE2).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = Text("y", font_size=28, color=WHITE2).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        origin = Dot(axes.c2p(0, 0), color=YELLOW, radius=0.1)
        origin_lbl = Text("(0,0)", font_size=20, color=YELLOW).next_to(origin, DR, buff=0.1)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl))
        self.play(FadeIn(origin), FadeIn(origin_lbl))
        self.wait(0.4)

        # Quadrant labels
        q1 = Text("I  (+,+)", font_size=26, color=GREEN).move_to(axes.c2p(3.0, 2.5))
        q2 = Text("II  (−,+)", font_size=26, color=BLUE).move_to(axes.c2p(-3.0, 2.5))
        q3 = Text("III  (−,−)", font_size=26, color=PURPLE).move_to(axes.c2p(-3.0, -2.5))
        q4 = Text("IV  (+,−)", font_size=26, color=ORANGE).move_to(axes.c2p(3.0, -2.5))
        self.play(LaggedStart(FadeIn(q1), FadeIn(q2), FadeIn(q3), FadeIn(q4), lag_ratio=0.2))
        self.wait(0.4)

        # Place sample points
        sample = [(3, 2, GREEN), (-2, 2, BLUE), (-3, -1, PURPLE), (2, -2, ORANGE)]
        sample_dots = VGroup()
        sample_labels = VGroup()
        for x, y, c in sample:
            d = Dot(axes.c2p(x, y), color=c, radius=0.1)
            lbl = Text(f"({x},{y})", font_size=20, color=c).next_to(d, UP, buff=0.1)
            sample_dots.add(d)
            sample_labels.add(lbl)
        self.play(LaggedStartMap(FadeIn, sample_dots, lag_ratio=0.2),
                  LaggedStartMap(FadeIn, sample_labels, lag_ratio=0.2))
        self.wait(2.0)

        self.play(FadeOut(VGroup(title, axes, x_lbl, y_lbl, origin, origin_lbl,
                                 q1, q2, q3, q4, sample_dots, sample_labels)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MIDPOINT                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("midpoint")
        title2 = section_title("Средна точка", color=GREEN)
        self.play(FadeIn(title2), run_time=0.5)

        formula = MathTex(
            "M = \\left(\\frac{x_1+x_2}{2},\\ \\frac{y_1+y_2}{2}\\right)",
            font_size=46, color=WHITE2,
        )
        formula.move_to(UP * 2.0)
        self.play(Write(formula), run_time=1.6)
        self.wait(0.6)

        axes2 = Axes(
            x_range=[0, 8, 1], y_range=[0, 12, 2],
            x_length=5.5, y_length=4.0,
            axis_config={"color": GREY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 18},
            tips=False,
        ).move_to(LEFT * 3.2 + DOWN * 0.8)
        self.play(Create(axes2), run_time=1.0)

        A = axes2.c2p(2, 4)
        B = axes2.c2p(6, 10)
        M = axes2.c2p(4, 7)
        dA = Dot(A, color=BLUE, radius=0.1)
        dB = Dot(B, color=ORANGE, radius=0.1)
        dM = Dot(M, color=GREEN, radius=0.12)
        lA = Text("A(2,4)", font_size=20, color=BLUE).next_to(dA, DL, buff=0.05)
        lB = Text("B(6,10)", font_size=20, color=ORANGE).next_to(dB, UR, buff=0.05)
        lM = Text("M(4,7)", font_size=22, color=GREEN, weight=BOLD).next_to(dM, UL, buff=0.1)
        seg = Line(A, B, color=GREY, stroke_width=2.5)

        self.play(FadeIn(dA), FadeIn(lA), FadeIn(dB), FadeIn(lB))
        self.play(Create(seg))
        self.wait(0.3)
        self.play(FadeIn(dM), FadeIn(lM))
        self.wait(0.4)

        calc = VGroup(
            MathTex("x_M = \\frac{2+6}{2} = 4", font_size=34, color=BLUE),
            MathTex("y_M = \\frac{4+10}{2} = 7", font_size=34, color=ORANGE),
            MathTex("M = (4, 7)", font_size=38, color=GREEN),
        ).arrange(DOWN, buff=0.35)
        calc.move_to(RIGHT * 3.0 + DOWN * 0.4)
        for c in calc:
            self.play(Write(c), run_time=1.0)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, formula, axes2, dA, lA, dB, lB, dM, lM, seg, calc)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ROTATION                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rotation")
        title3 = section_title("Ротација", color=BLUE)
        self.play(FadeIn(title3), run_time=0.5)

        axes3 = Axes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=5.0, y_length=5.0,
            axis_config={"color": GREY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 18},
            tips=False,
        ).move_to(LEFT * 3.5 + DOWN * 0.2)
        self.play(Create(axes3))

        p_start = axes3.c2p(2, 3)
        d_start = Dot(p_start, color=GREEN, radius=0.1)
        lbl_start = Text("(2,3)", font_size=20, color=GREEN).next_to(d_start, UR, buff=0.05)
        self.play(FadeIn(d_start), FadeIn(lbl_start))

        # animate rotation around origin 90 ccw
        target_p = axes3.c2p(-3, 2)
        arc = Arc(arc_center=axes3.c2p(0, 0),
                  radius=np.linalg.norm(p_start - axes3.c2p(0, 0)),
                  start_angle=np.arctan2(3, 2),
                  angle=np.deg2rad(90),
                  color=YELLOW, stroke_width=3)
        self.play(Create(arc), run_time=1.4)
        d_end = Dot(target_p, color=ORANGE, radius=0.1)
        lbl_end = Text("(−3,2)", font_size=20, color=ORANGE).next_to(d_end, UL, buff=0.05)
        self.play(FadeIn(d_end), FadeIn(lbl_end))

        rot_text = VGroup(
            Text("90° обратно од стрелка", font_size=26, color=YELLOW),
            MathTex("(x,y) \\to (-y, x)", font_size=36, color=WHITE2),
            MathTex("(2,3) \\to (-3, 2)", font_size=34, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        rot_text.move_to(RIGHT * 3.0 + UP * 0.2)
        for t in rot_text:
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title3, axes3, d_start, lbl_start, d_end, lbl_end, arc, rot_text)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  REFLECTION                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("reflection")
        title4 = section_title("Рефлексија", color=ORANGE)
        self.play(FadeIn(title4), run_time=0.5)

        axes4 = Axes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=4.8, y_length=4.8,
            axis_config={"color": GREY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 16},
            tips=False,
        ).move_to(LEFT * 3.5)
        self.play(Create(axes4))

        # x-axis mirror line is the x-axis itself, highlight it
        mirror = Line(axes4.c2p(-3.5, 0), axes4.c2p(3.5, 0), color=YELLOW, stroke_width=3)
        self.play(Create(mirror))

        pA = axes4.c2p(2, 2)
        pAr = axes4.c2p(2, -2)
        dA2 = Dot(pA, color=BLUE, radius=0.1)
        dAr = Dot(pAr, color=ORANGE, radius=0.1)
        lA2 = Text("(2,2)", font_size=18, color=BLUE).next_to(dA2, UR, buff=0.05)
        lAr = Text("(2,−2)", font_size=18, color=ORANGE).next_to(dAr, DR, buff=0.05)
        conn = DashedLine(pA, pAr, color=GREY, stroke_width=2)

        self.play(FadeIn(dA2), FadeIn(lA2))
        self.play(Create(conn))
        self.play(FadeIn(dAr), FadeIn(lAr))

        rules = VGroup(
            Text("Преку x-оска:", font_size=26, color=YELLOW),
            MathTex("(x,y) \\to (x, -y)", font_size=34, color=BLUE),
            Text("Преку y-оска:", font_size=26, color=YELLOW),
            MathTex("(x,y) \\to (-x, y)", font_size=34, color=GREEN),
            Text("Преку y = x:", font_size=26, color=YELLOW),
            MathTex("(x,y) \\to (y, x)", font_size=34, color=PURPLE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rules.move_to(RIGHT * 3.0)
        for r in rules:
            self.play(FadeIn(r, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title4, axes4, mirror, dA2, dAr, lA2, lAr, conn, rules)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  TRANSLATION                                      ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("translation")
        title5 = section_title("Транслација", color=GREEN)
        self.play(FadeIn(title5), run_time=0.5)

        axes5 = Axes(
            x_range=[-2, 6, 1], y_range=[-2, 6, 1],
            x_length=5.0, y_length=5.0,
            axis_config={"color": GREY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 18},
            tips=False,
        ).move_to(LEFT * 3.3)
        self.play(Create(axes5))

        # original triangle
        v1 = axes5.c2p(1, 1)
        v2 = axes5.c2p(2, 1)
        v3 = axes5.c2p(1, 2)
        tri1 = Polygon(v1, v2, v3, color=BLUE, fill_color=BLUE,
                       fill_opacity=0.2, stroke_width=3)
        # translated by (3, 2)
        v1b = axes5.c2p(4, 3)
        v2b = axes5.c2p(5, 3)
        v3b = axes5.c2p(4, 4)
        tri2 = Polygon(v1b, v2b, v3b, color=GREEN, fill_color=GREEN,
                       fill_opacity=0.2, stroke_width=3)
        arrow = Arrow(v1, v1b, color=YELLOW, buff=0, stroke_width=3,
                      max_tip_length_to_length_ratio=0.1)

        self.play(Create(tri1))
        self.wait(0.3)
        self.play(GrowArrow(arrow))
        self.play(TransformFromCopy(tri1, tri2), run_time=1.4)

        tr_text = VGroup(
            Text("Транслациски вектор:", font_size=24, color=YELLOW),
            MathTex("\\vec{v} = (3, 2)", font_size=40, color=WHITE2),
            MathTex("(x,y) \\to (x+3, y+2)", font_size=34, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        tr_text.move_to(RIGHT * 3.0)
        for t in tr_text:
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title5, axes5, tri1, tri2, arrow, tr_text)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  DILATION                                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dilation")
        title6 = section_title("Слични фигури  —  скалирање", color=PURPLE)
        self.play(FadeIn(title6), run_time=0.5)

        small = Polygon(
            [-0.7, -0.5, 0], [0.7, -0.5, 0], [0, 0.7, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.2, stroke_width=3,
        ).move_to(LEFT * 3.0)
        big = Polygon(
            [-1.4, -1.0, 0], [1.4, -1.0, 0], [0, 1.4, 0],
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.2, stroke_width=3,
        ).move_to(RIGHT * 2.0)

        self.play(Create(small))
        self.play(TransformFromCopy(small, big), run_time=1.4)

        k_box = callout("k = 2  →  растојанијата × 2",
                        width=8.0, border=PURPLE, font_size=30)
        k_box.shift(DOWN * 2.5)
        self.play(FadeIn(k_box))
        self.wait(1.8)

        self.play(FadeOut(VGroup(title6, small, big, k_box)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 8.  SCALE DRAWINGS                                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("scale")
        title7 = section_title("Размер на карта", color=BLUE)
        self.play(FadeIn(title7), run_time=0.5)

        scale1 = Text("1 : 100", font_size=44, color=YELLOW, weight=BOLD)
        explain1 = Text("1 см на хартија = 100 см во природа",
                        font_size=28, color=WHITE2)
        VGroup(scale1, explain1).arrange(DOWN, buff=0.3).move_to(UP * 1.5)
        self.play(Write(scale1))
        self.play(FadeIn(explain1))
        self.wait(0.8)

        scale2 = Text("1 : 50.000", font_size=44, color=ORANGE, weight=BOLD)
        explain2 = Text("1 см = 500 м  (на географска карта)",
                        font_size=28, color=WHITE2)
        VGroup(scale2, explain2).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        self.play(Write(scale2))
        self.play(FadeIn(explain2))
        self.wait(0.4)

        # visual ruler comparison
        small_r = Line(LEFT * 0.5, RIGHT * 0.5, color=YELLOW, stroke_width=5)
        small_r.shift(DOWN * 2.2 + LEFT * 2.5)
        big_r = Line(LEFT * 2.0, RIGHT * 2.0, color=ORANGE, stroke_width=5)
        big_r.shift(DOWN * 2.2 + RIGHT * 1.8)
        small_lbl = Text("1 см", font_size=22, color=YELLOW).next_to(small_r, DOWN, buff=0.15)
        big_lbl = Text("500 м (стварно)", font_size=22, color=ORANGE).next_to(big_r, DOWN, buff=0.15)
        self.play(Create(small_r), Create(big_r), FadeIn(small_lbl), FadeIn(big_lbl))
        self.wait(2.0)

        self.play(FadeOut(VGroup(title7, scale1, explain1, scale2, explain2,
                                 small_r, big_r, small_lbl, big_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 9.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")
        sum_title = section_title("Заклучок")
        self.play(FadeIn(sum_title), run_time=0.5)

        s1 = Text("Ротација — окрет.", font_size=34, color=BLUE)
        s2 = Text("Рефлексија — огледало.", font_size=34, color=ORANGE)
        s3 = Text("Транслација — поместување.", font_size=34, color=GREEN)
        s4 = Text("Скалирање — растегнување.", font_size=34, color=PURPLE)
        end = Text("Четири движења. Истиот свет.",
                   font_size=40, color=YELLOW, weight=BOLD)

        VGroup(s1, s2, s3, s4, end).arrange(DOWN, buff=0.32).move_to(ORIGIN)

        for s in [s1, s2, s3, s4]:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.5)
            self.wait(0.15)
        self.play(Write(end), run_time=1.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sum_title, s1, s2, s3, s4, end)), run_time=0.8)
