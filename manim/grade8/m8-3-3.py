"""
m8-3-3  —  Плоштина, периметар и зафатнина
Математика 8, Единица 3: Геометрија

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Render:  manim -ql m8-3-3.py M833Scene
Output:  media/videos/m8-3-3/480p15/M833Scene.mp4
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


class M833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Должина чека.", font_size=42, color=BLUE),
            Text("Плоштина живее.", font_size=42, color=GREEN),
            Text("Волумен дише.", font_size=42, color=ORANGE),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.5)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.7)
            self.wait(0.35)

        f1 = Text("Геометријата не е премер.", font_size=34, color=WHITE2)
        f2 = Text("Геометријата е простор.", font_size=38, color=YELLOW, weight=BOLD)
        VGroup(f1, f2).arrange(DOWN, buff=0.35).move_to(DOWN * 1.8)
        self.play(FadeIn(f1, shift=UP * 0.2), run_time=0.7)
        self.play(Write(f2), run_time=1.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(beats, f1, f2)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  PERIMETER                                        ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("perimeter")
        title = section_title("Периметар  P  —  должина на работ")
        self.play(FadeIn(title), run_time=0.6)

        # Rectangle
        rect = Rectangle(width=3.0, height=1.8, color=BLUE,
                         fill_color=BLUE, fill_opacity=0.15, stroke_width=3)
        rect.move_to(LEFT * 3.5 + UP * 0.5)
        a_l = Text("a", font_size=24, color=YELLOW).next_to(rect, DOWN, buff=0.1)
        b_l = Text("b", font_size=24, color=YELLOW).next_to(rect, RIGHT, buff=0.1)
        p_rect = MathTex("P = 2(a+b)", font_size=34, color=BLUE).next_to(rect, DOWN, buff=0.7)

        self.play(Create(rect), FadeIn(a_l), FadeIn(b_l), Write(p_rect))
        self.wait(0.4)

        # Square
        sq = Square(side_length=2.0, color=GREEN,
                    fill_color=GREEN, fill_opacity=0.15, stroke_width=3)
        sq.move_to(UP * 0.5)
        sq_a = Text("a", font_size=24, color=YELLOW).next_to(sq, DOWN, buff=0.1)
        p_sq = MathTex("P = 4a", font_size=34, color=GREEN).next_to(sq, DOWN, buff=0.7)

        self.play(Create(sq), FadeIn(sq_a), Write(p_sq))
        self.wait(0.4)

        # Triangle
        tri = Polygon(
            [-1.0, -0.8, 0], [1.0, -0.8, 0], [0.2, 1.0, 0],
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.15, stroke_width=3,
        )
        tri.move_to(RIGHT * 3.0 + UP * 0.5)
        t_a = Text("a", font_size=22, color=YELLOW).move_to(tri.get_vertices()[0] + RIGHT * 1.0 + DOWN * 0.2)
        t_b = Text("b", font_size=22, color=YELLOW).move_to(tri.get_vertices()[1] + LEFT * 0.1 + UP * 0.4)
        t_c = Text("c", font_size=22, color=YELLOW).move_to(tri.get_vertices()[2] + LEFT * 0.9 + DOWN * 0.4)
        p_tri = MathTex("P = a+b+c", font_size=34, color=ORANGE).next_to(tri, DOWN, buff=0.5)

        self.play(Create(tri), FadeIn(t_a), FadeIn(t_b), FadeIn(t_c), Write(p_tri))
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, rect, a_l, b_l, p_rect, sq, sq_a, p_sq,
                                 tri, t_a, t_b, t_c, p_tri)), run_time=0.7)

        # Circle circumference
        title_c = section_title("Обиколка на круг", color=PURPLE)
        self.play(FadeIn(title_c), run_time=0.5)

        cir = Circle(radius=1.5, color=PURPLE,
                     fill_color=PURPLE, fill_opacity=0.15, stroke_width=3)
        cir.move_to(LEFT * 3.0)
        r_line = Line(cir.get_center(), cir.get_center() + RIGHT * 1.5,
                      color=YELLOW, stroke_width=3)
        r_lbl = Text("r", font_size=26, color=YELLOW).next_to(r_line, UP, buff=0.1)
        d_line = Line(cir.get_center() + LEFT * 1.5, cir.get_center() + RIGHT * 1.5,
                      color=ORANGE, stroke_width=2)
        d_lbl = Text("d", font_size=26, color=ORANGE).next_to(d_line, DOWN, buff=0.1)

        self.play(Create(cir))
        self.play(Create(r_line), FadeIn(r_lbl))
        self.play(Create(d_line), FadeIn(d_lbl))

        c_form = VGroup(
            MathTex("C = 2\\pi r", font_size=42, color=PURPLE),
            MathTex("C = \\pi d", font_size=42, color=ORANGE),
        ).arrange(DOWN, buff=0.5).move_to(RIGHT * 3.0)
        for f in c_form:
            self.play(Write(f), run_time=1.1)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title_c, cir, r_line, r_lbl, d_line, d_lbl, c_form)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  AREA                                             ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("area")
        title2 = section_title("Плоштина  A", color=GREEN)
        self.play(FadeIn(title2), run_time=0.6)

        # Rectangle with grid
        rect2 = Rectangle(width=3.0, height=2.0, color=BLUE,
                          fill_color=BLUE, fill_opacity=0.15, stroke_width=3)
        rect2.move_to(LEFT * 3.5 + UP * 0.6)
        # grid lines
        grid = VGroup()
        for i in range(1, 3):
            grid.add(Line(rect2.get_corner(DL) + RIGHT * i, rect2.get_corner(UL) + RIGHT * i,
                          color=BLUE, stroke_width=1.5, stroke_opacity=0.5))
        for j in range(1, 2):
            grid.add(Line(rect2.get_corner(DL) + UP * j, rect2.get_corner(DR) + UP * j,
                          color=BLUE, stroke_width=1.5, stroke_opacity=0.5))
        a_r = MathTex("A = a \\cdot b", font_size=34, color=BLUE).next_to(rect2, DOWN, buff=0.4)

        self.play(Create(rect2), Create(grid), Write(a_r))
        self.wait(0.4)

        # Square
        sq2 = Square(side_length=2.0, color=GREEN,
                     fill_color=GREEN, fill_opacity=0.15, stroke_width=3)
        sq2.move_to(UP * 0.6)
        a_s = MathTex("A = a^2", font_size=34, color=GREEN).next_to(sq2, DOWN, buff=0.4)
        self.play(Create(sq2), Write(a_s))
        self.wait(0.4)

        # Triangle with height
        tri2 = Polygon(
            [-1.2, -0.8, 0], [1.2, -0.8, 0], [-0.2, 0.9, 0],
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.15, stroke_width=3,
        )
        tri2.move_to(RIGHT * 3.5 + UP * 0.6)
        # base and height
        base_lbl = Text("a", font_size=22, color=YELLOW).next_to(tri2, DOWN, buff=0.1)
        h_line = DashedLine(
            tri2.get_vertices()[2],
            np.array([tri2.get_vertices()[2][0], tri2.get_vertices()[0][1], 0]),
            color=YELLOW, stroke_width=2,
        )
        h_lbl = Text("h", font_size=22, color=YELLOW).next_to(h_line, RIGHT, buff=0.1)
        a_t = MathTex("A = \\frac{a \\cdot h}{2}", font_size=32, color=ORANGE).next_to(tri2, DOWN, buff=0.4)
        self.play(Create(tri2), FadeIn(base_lbl), Create(h_line), FadeIn(h_lbl), Write(a_t))
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, rect2, grid, a_r, sq2, a_s, tri2,
                                 base_lbl, h_line, h_lbl, a_t)), run_time=0.7)

        # ── More: parallelogram, trapezium, circle ─────────────
        title2b = section_title("Уште плоштини", color=GREEN)
        self.play(FadeIn(title2b), run_time=0.5)

        # parallelogram
        par = Polygon(
            [-1.2, -0.7, 0], [1.0, -0.7, 0], [1.6, 0.7, 0], [-0.6, 0.7, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.15, stroke_width=3,
        ).move_to(LEFT * 4.0)
        par_a = MathTex("A = a \\cdot h", font_size=30, color=BLUE).next_to(par, DOWN, buff=0.3)
        par_t = Text("паралелограм", font_size=22, color=BLUE).next_to(par_a, DOWN, buff=0.1)

        # trapezium
        trap = Polygon(
            [-1.4, -0.7, 0], [1.4, -0.7, 0], [0.8, 0.7, 0], [-0.8, 0.7, 0],
            color=PURPLE, fill_color=PURPLE, fill_opacity=0.15, stroke_width=3,
        ).move_to(ORIGIN)
        trap_a = MathTex("A = \\frac{a+b}{2}\\cdot h", font_size=28, color=PURPLE).next_to(trap, DOWN, buff=0.3)
        trap_t = Text("трапез", font_size=22, color=PURPLE).next_to(trap_a, DOWN, buff=0.1)

        # circle
        cir2 = Circle(radius=1.0, color=YELLOW,
                      fill_color=YELLOW, fill_opacity=0.15, stroke_width=3).move_to(RIGHT * 4.0)
        cir_r = Line(cir2.get_center(), cir2.get_center() + RIGHT * 1.0,
                     color=YELLOW, stroke_width=2)
        cir_rl = Text("r", font_size=22, color=YELLOW).next_to(cir_r, UP, buff=0.05)
        cir_a = MathTex("A = \\pi r^2", font_size=32, color=YELLOW).next_to(cir2, DOWN, buff=0.3)
        cir_t = Text("круг", font_size=22, color=YELLOW).next_to(cir_a, DOWN, buff=0.1)

        self.play(LaggedStart(
            AnimationGroup(Create(par), Write(par_a), FadeIn(par_t)),
            AnimationGroup(Create(trap), Write(trap_a), FadeIn(trap_t)),
            AnimationGroup(Create(cir2), Create(cir_r), FadeIn(cir_rl), Write(cir_a), FadeIn(cir_t)),
            lag_ratio=0.4,
        ))
        self.wait(2.2)

        self.play(FadeOut(VGroup(title2b, par, par_a, par_t, trap, trap_a, trap_t,
                                 cir2, cir_r, cir_rl, cir_a, cir_t)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  VOLUME — 3D                                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("volume")
        title3 = section_title("Зафатнина  V  —  3D простор", color=ORANGE)
        self.play(FadeIn(title3), run_time=0.6)

        # We'll show 2D representations (since we want simple)
        # Cube
        cube_face = Square(side_length=1.6, color=GREEN,
                           fill_color=GREEN, fill_opacity=0.2, stroke_width=3)
        cube_face.move_to(LEFT * 4.5 + UP * 1.0)
        cube_offset = np.array([0.5, 0.4, 0])
        cube_back = Square(side_length=1.6, color=GREEN,
                           fill_color=GREEN, fill_opacity=0.1, stroke_width=2)
        cube_back.move_to(cube_face.get_center() + cube_offset)
        cube_edges = VGroup(
            Line(cube_face.get_corner(UL), cube_back.get_corner(UL), color=GREEN, stroke_width=2),
            Line(cube_face.get_corner(UR), cube_back.get_corner(UR), color=GREEN, stroke_width=2),
            Line(cube_face.get_corner(DR), cube_back.get_corner(DR), color=GREEN, stroke_width=2),
        )
        cube_lbl = MathTex("V = a^3", font_size=32, color=GREEN).next_to(cube_face, DOWN, buff=0.8)
        cube_name = Text("коцка", font_size=22, color=GREEN).next_to(cube_lbl, DOWN, buff=0.1)

        # Cuboid
        cb_face = Rectangle(width=2.0, height=1.2, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.2, stroke_width=3)
        cb_face.move_to(LEFT * 1.5 + UP * 1.0)
        cb_back = Rectangle(width=2.0, height=1.2, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.1, stroke_width=2)
        cb_back.move_to(cb_face.get_center() + cube_offset)
        cb_edges = VGroup(
            Line(cb_face.get_corner(UL), cb_back.get_corner(UL), color=BLUE, stroke_width=2),
            Line(cb_face.get_corner(UR), cb_back.get_corner(UR), color=BLUE, stroke_width=2),
            Line(cb_face.get_corner(DR), cb_back.get_corner(DR), color=BLUE, stroke_width=2),
        )
        cb_lbl = MathTex("V = a\\cdot b\\cdot c", font_size=28, color=BLUE).next_to(cb_face, DOWN, buff=0.8)
        cb_name = Text("квадар", font_size=22, color=BLUE).next_to(cb_lbl, DOWN, buff=0.1)

        # Cylinder
        cyl_top = Ellipse(width=1.8, height=0.5, color=PURPLE,
                          fill_color=PURPLE, fill_opacity=0.3, stroke_width=2)
        cyl_top.move_to(RIGHT * 1.8 + UP * 1.5)
        cyl_bot = Ellipse(width=1.8, height=0.5, color=PURPLE,
                          fill_color=PURPLE, fill_opacity=0.2, stroke_width=2)
        cyl_bot.move_to(RIGHT * 1.8 + UP * 0.3)
        cyl_side = VGroup(
            Line(cyl_top.get_left(), cyl_bot.get_left(), color=PURPLE, stroke_width=2),
            Line(cyl_top.get_right(), cyl_bot.get_right(), color=PURPLE, stroke_width=2),
        )
        cyl_lbl = MathTex("V = \\pi r^2 h", font_size=28, color=PURPLE).next_to(cyl_bot, DOWN, buff=0.7)
        cyl_name = Text("цилиндар", font_size=22, color=PURPLE).next_to(cyl_lbl, DOWN, buff=0.1)

        # Sphere
        sph = Circle(radius=0.9, color=YELLOW,
                     fill_color=YELLOW, fill_opacity=0.2, stroke_width=3)
        sph.move_to(RIGHT * 4.8 + UP * 1.0)
        sph_arc = Arc(radius=0.9, start_angle=PI, angle=PI,
                      color=YELLOW, stroke_width=1.5)
        sph_arc.move_to(sph.get_center())
        sph_lbl = MathTex("V = \\frac{4}{3}\\pi r^3", font_size=28, color=YELLOW).next_to(sph, DOWN, buff=0.7)
        sph_name = Text("сфера", font_size=22, color=YELLOW).next_to(sph_lbl, DOWN, buff=0.1)

        self.play(
            Create(cube_face), Create(cube_back), Create(cube_edges),
            Write(cube_lbl), FadeIn(cube_name),
        )
        self.play(
            Create(cb_face), Create(cb_back), Create(cb_edges),
            Write(cb_lbl), FadeIn(cb_name),
        )
        self.play(
            Create(cyl_top), Create(cyl_bot), Create(cyl_side),
            Write(cyl_lbl), FadeIn(cyl_name),
        )
        self.play(
            Create(sph), Create(sph_arc),
            Write(sph_lbl), FadeIn(sph_name),
        )
        self.wait(2.5)

        self.play(FadeOut(VGroup(title3, cube_face, cube_back, cube_edges, cube_lbl, cube_name,
                                 cb_face, cb_back, cb_edges, cb_lbl, cb_name,
                                 cyl_top, cyl_bot, cyl_side, cyl_lbl, cyl_name,
                                 sph, sph_arc, sph_lbl, sph_name)), run_time=0.7)

        # Cone and pyramid
        title3b = section_title("Конус и пирамида", color=ORANGE)
        self.play(FadeIn(title3b), run_time=0.5)

        cone_base = Ellipse(width=2.0, height=0.5, color=RED,
                            fill_color=RED, fill_opacity=0.2, stroke_width=2)
        cone_base.move_to(LEFT * 3.0 + DOWN * 0.5)
        cone_apex = np.array([cone_base.get_center()[0], cone_base.get_center()[1] + 2.0, 0])
        cone_sides = VGroup(
            Line(cone_base.get_left(), cone_apex, color=RED, stroke_width=2),
            Line(cone_base.get_right(), cone_apex, color=RED, stroke_width=2),
        )
        cone_lbl = MathTex("V = \\frac{1}{3}\\pi r^2 h", font_size=32, color=RED)
        cone_lbl.next_to(cone_base, DOWN, buff=0.5)

        pyr_base = Polygon(
            [-1.0, -0.3, 0], [1.0, -0.3, 0], [0.7, 0.2, 0], [-1.3, 0.2, 0],
            color=BLUE, fill_color=BLUE, fill_opacity=0.2, stroke_width=2,
        )
        pyr_base.move_to(RIGHT * 3.0 + DOWN * 0.5)
        pyr_apex = np.array([pyr_base.get_center()[0], pyr_base.get_center()[1] + 2.0, 0])
        pyr_sides = VGroup()
        for v in pyr_base.get_vertices():
            pyr_sides.add(Line(v, pyr_apex, color=BLUE, stroke_width=2))
        pyr_lbl = MathTex("V = \\frac{1}{3} \\cdot B \\cdot h", font_size=32, color=BLUE)
        pyr_lbl.next_to(pyr_base, DOWN, buff=0.5)

        self.play(Create(cone_base), Create(cone_sides), Write(cone_lbl))
        self.play(Create(pyr_base), Create(pyr_sides), Write(pyr_lbl))
        self.wait(2.0)

        self.play(FadeOut(VGroup(title3b, cone_base, cone_sides, cone_lbl,
                                 pyr_base, pyr_sides, pyr_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  CUBE EXAMPLE                                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cube_example")
        title4 = section_title("Пример: коцка a = 5 см")
        self.play(FadeIn(title4), run_time=0.5)

        # cube visual
        cf = Square(side_length=1.8, color=GREEN,
                    fill_color=GREEN, fill_opacity=0.2, stroke_width=3)
        cf.move_to(LEFT * 3.5)
        cb_b = Square(side_length=1.8, color=GREEN,
                      fill_color=GREEN, fill_opacity=0.1, stroke_width=2)
        cb_b.move_to(cf.get_center() + np.array([0.6, 0.5, 0]))
        c_edges = VGroup(
            Line(cf.get_corner(UL), cb_b.get_corner(UL), color=GREEN, stroke_width=2),
            Line(cf.get_corner(UR), cb_b.get_corner(UR), color=GREEN, stroke_width=2),
            Line(cf.get_corner(DR), cb_b.get_corner(DR), color=GREEN, stroke_width=2),
        )
        a_lbl = Text("a = 5 см", font_size=28, color=YELLOW).next_to(cf, DOWN, buff=0.3)

        self.play(Create(cf), Create(cb_b), Create(c_edges), FadeIn(a_lbl))
        self.wait(0.3)

        v_calc = MathTex(
            "V = a^3 = 5^3 = 125\\,\\text{см}^3",
            font_size=36, color=GREEN,
        )
        s_calc = MathTex(
            "S = 6a^2 = 6 \\cdot 25 = 150\\,\\text{см}^2",
            font_size=36, color=BLUE,
        )
        VGroup(v_calc, s_calc).arrange(DOWN, buff=0.5).move_to(RIGHT * 2.5)
        self.play(Write(v_calc), run_time=1.4)
        self.play(Write(s_calc), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(title4, cf, cb_b, c_edges, a_lbl, v_calc, s_calc)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  UNIT CONVERSION                                  ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("units")
        title5 = section_title("Претворање мерки", color=PURPLE)
        self.play(FadeIn(title5), run_time=0.5)

        conv = VGroup(
            MathTex("1\\,\\text{м}^2 = 10\\,000\\,\\text{см}^2",
                    font_size=40, color=GREEN),
            MathTex("1\\,\\text{м}^3 = 1\\,000\\,000\\,\\text{см}^3",
                    font_size=40, color=ORANGE),
            MathTex("1\\,\\text{м}^3 = 1000\\,\\text{литри}",
                    font_size=40, color=BLUE),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        for c in conv:
            self.play(Write(c), run_time=1.3)
            self.wait(0.3)
        self.wait(1.8)
        self.play(FadeOut(VGroup(title5, conv)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")
        sum_title = section_title("Заклучок")
        self.play(FadeIn(sum_title), run_time=0.5)

        s1 = Text("Периметар — должина.", font_size=34, color=BLUE)
        s2 = Text("Плоштина — површина.", font_size=34, color=GREEN)
        s3 = Text("Зафатнина — простор.", font_size=34, color=ORANGE)
        end = Text("Една, две, три димензии.",
                   font_size=40, color=YELLOW, weight=BOLD)

        VGroup(s1, s2, s3, end).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for s in [s1, s2, s3]:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.play(Write(end), run_time=1.4)
        self.wait(2.2)
        self.play(FadeOut(VGroup(sum_title, s1, s2, s3, end)), run_time=0.8)
