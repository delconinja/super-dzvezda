"""
phys8-3-2  —  Сенки
Физика 8, Единица 3: Светлина

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-3-2.py Phys832Scene
Output:  media/videos/phys8-3-2/480p15/Phys832Scene.mp4
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


class Phys832Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Зошто постои сенка?",
                    font_size=50, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.2)
        self.wait(0.7)

        ans1 = Text("Затоа што светлината оди праволиниски.", font_size=32, color=WHITE2)
        ans2 = Text("И не може да поминe низ непроѕирни предмети.", font_size=32, color=WHITE2)
        ans1.shift(UP * 0.3)
        ans2.next_to(ans1, DOWN, buff=0.3)
        self.play(FadeIn(ans1, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeIn(ans2, shift=UP * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hook), FadeOut(ans1), FadeOut(ans2))

        # ══════════════════════════════════════════════════════════
        # 2.  ТОЧКАСТ ИЗВОР → ОСТРА СЕНКА                    ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("point_source")

        hdr = section_title("Точкаст извор → остра сенка")
        self.play(Write(hdr), run_time=0.9)

        # point source (small)
        pt_src = Dot(LEFT * 5.5 + UP * 0.5, color=YELLOW, radius=0.18)
        pt_lbl = Text("Точкаст\nизвор", font_size=18, color=YELLOW)
        pt_lbl.next_to(pt_src, UP, buff=0.15)

        # opaque object
        obj = Rectangle(width=0.5, height=1.4,
                        fill_color=GREY, fill_opacity=1, stroke_width=0)
        obj.move_to(LEFT * 1.5 + UP * 0.5)
        obj_lbl = Text("Непроѕирен\nпредмет", font_size=18, color=GREY)
        obj_lbl.next_to(obj, UP, buff=0.1)

        # shadow (triangle behind object)
        shadow = Polygon(
            obj.get_corner(UR),
            obj.get_corner(DR),
            np.array([5.0, -2.5, 0]),
            np.array([5.0, 3.0,  0]),
            fill_color="#050f1a",
            fill_opacity=0.92,
            stroke_width=0,
        )

        # rays from point source
        ray_top = Line(pt_src.get_center(), obj.get_corner(UR),
                       color=YELLOW, stroke_width=2, stroke_opacity=0.7)
        ray_bot = Line(pt_src.get_center(), obj.get_corner(DR),
                       color=YELLOW, stroke_width=2, stroke_opacity=0.7)
        ray_ext_top = DashedLine(obj.get_corner(UR), np.array([5.0, 3.2, 0]),
                                 color=GREY, stroke_width=1.5, dash_length=0.14)
        ray_ext_bot = DashedLine(obj.get_corner(DR), np.array([5.0, -2.7, 0]),
                                 color=GREY, stroke_width=1.5, dash_length=0.14)

        shadow_lbl = Text("Потполна\nсенка (умбра)", font_size=20, color=BLUE)
        shadow_lbl.move_to(np.array([3.0, 0.3, 0]))

        self.play(FadeIn(pt_src), Write(pt_lbl))
        self.play(FadeIn(obj), Write(obj_lbl))
        self.play(Create(ray_top), Create(ray_bot))
        self.play(FadeIn(shadow), Create(ray_ext_top), Create(ray_ext_bot))
        self.play(Write(shadow_lbl))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr, pt_src, pt_lbl, obj, obj_lbl, shadow,
            ray_top, ray_bot, ray_ext_top, ray_ext_bot, shadow_lbl,
        ]])

        # ══════════════════════════════════════════════════════════
        # 3.  ПРОШИРЕН ИЗВОР → УМБРА + PENUMBRA               ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("extended_source")

        hdr2 = section_title("Проширен извор → умбра + полусенка")
        self.play(Write(hdr2), run_time=0.9)

        ext_src = Circle(radius=0.55, fill_color=YELLOW, fill_opacity=0.9,
                         stroke_width=0)
        ext_src.shift(LEFT * 5.2 + UP * 0.0)
        ext_lbl = Text("Проширен\nизвор", font_size=18, color=YELLOW)
        ext_lbl.next_to(ext_src, UP, buff=0.12)

        obj2 = Rectangle(width=0.5, height=1.4,
                         fill_color=GREY, fill_opacity=1, stroke_width=0)
        obj2.move_to(LEFT * 1.5 + UP * 0.0)

        # umbra (dark core)
        umbra = Polygon(
            obj2.get_corner(UR),
            obj2.get_corner(DR),
            np.array([2.0, -0.5, 0]),
            np.array([2.0, 0.5, 0]),
            fill_color="#020a14",
            fill_opacity=0.95,
            stroke_width=0,
        )
        umbra_lbl = Text("Умбра\n(потполна сенка)", font_size=19, color=BLUE)
        umbra_lbl.move_to(np.array([1.2, 0.0, 0]))

        # penumbra (lighter)
        pen_top = Polygon(
            ext_src.get_top(),
            obj2.get_corner(UR),
            np.array([4.5, 2.8, 0]),
            fill_color="#0d1b2e",
            fill_opacity=0.6,
            stroke_width=0,
        )
        pen_bot = Polygon(
            ext_src.get_bottom(),
            obj2.get_corner(DR),
            np.array([4.5, -2.8, 0]),
            fill_color="#0d1b2e",
            fill_opacity=0.6,
            stroke_width=0,
        )
        pen_lbl = Text("Полусенка\n(penumbra)", font_size=19, color=ORANGE)
        pen_lbl.move_to(np.array([3.2, 1.5, 0]))

        self.play(FadeIn(ext_src), Write(ext_lbl))
        self.play(FadeIn(obj2))
        self.play(FadeIn(pen_top), FadeIn(pen_bot))
        self.play(FadeIn(umbra))
        self.play(Write(umbra_lbl), Write(pen_lbl))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr2, ext_src, ext_lbl, obj2, umbra, umbra_lbl,
            pen_top, pen_bot, pen_lbl,
        ]])

        # ══════════════════════════════════════════════════════════
        # 4.  ЗАТЕМНУВАЊА — СОНЧЕВО И МЕСЕЧЕВО                ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("eclipses")

        hdr3 = section_title("Затемнувања")
        self.play(Write(hdr3), run_time=0.8)

        # Solar eclipse — left side
        sun_e = Circle(radius=0.55, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sun_e.shift(LEFT * 5.5 + UP * 1.5)
        sun_lbl = Text("Сонце", font_size=18, color=YELLOW)
        sun_lbl.next_to(sun_e, DOWN, buff=0.12)

        moon_e = Circle(radius=0.35, fill_color="#1a1a2e", fill_opacity=1,
                        stroke_color=GREY, stroke_width=1.5)
        moon_e.shift(LEFT * 2.8 + UP * 1.5)
        moon_lbl = Text("Месечина", font_size=18, color=GREY)
        moon_lbl.next_to(moon_e, DOWN, buff=0.12)

        earth_e = Circle(radius=0.28, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        earth_e.shift(LEFT * 0.5 + UP * 1.5)
        earth_lbl = Text("Земја", font_size=18, color=BLUE)
        earth_lbl.next_to(earth_e, DOWN, buff=0.12)

        sol_title = Text("Сончево затемнување", font_size=22, color=YELLOW, weight=BOLD)
        sol_title.move_to(LEFT * 2.5 + UP * 2.9)

        self.play(FadeIn(sun_e), Write(sun_lbl))
        self.play(FadeIn(moon_e), Write(moon_lbl))
        self.play(FadeIn(earth_e), Write(earth_lbl))
        self.play(Write(sol_title))

        sol_arr1 = Arrow(sun_e.get_right(), moon_e.get_left(),
                         color=YELLOW, buff=0.05, stroke_width=2)
        sol_arr2 = Arrow(moon_e.get_right(), earth_e.get_left(),
                         color=GREY, buff=0.05, stroke_width=2)
        self.play(GrowArrow(sol_arr1), GrowArrow(sol_arr2))

        sol_note = Text("Месечината ја блокира сончевата светлина → сенка на Земја",
                        font_size=19, color=WHITE2)
        sol_note.move_to(LEFT * 2.8 + UP * 0.6)
        self.play(FadeIn(sol_note, shift=UP * 0.15))
        self.wait(1.0)

        # Lunar eclipse — right side
        sun_l = Circle(radius=0.55, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sun_l.shift(LEFT * 0.2 + DOWN * 1.5)
        sun_llbl = Text("Сонце", font_size=18, color=YELLOW)
        sun_llbl.next_to(sun_l, DOWN, buff=0.12)

        earth_l = Circle(radius=0.28, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        earth_l.shift(RIGHT * 2.5 + DOWN * 1.5)
        earth_llbl = Text("Земја", font_size=18, color=BLUE)
        earth_llbl.next_to(earth_l, DOWN, buff=0.12)

        moon_l = Circle(radius=0.25, fill_color=RED, fill_opacity=0.8, stroke_width=0)
        moon_l.shift(RIGHT * 5.0 + DOWN * 1.5)
        moon_llbl = Text("Месечина\n(поцрвенува!)", font_size=17, color=RED)
        moon_llbl.next_to(moon_l, DOWN, buff=0.12)

        lun_title = Text("Месечево затемнување", font_size=22, color=BLUE, weight=BOLD)
        lun_title.move_to(RIGHT * 2.5 + DOWN * 0.1)

        self.play(FadeIn(sun_l), Write(sun_llbl))
        self.play(FadeIn(earth_l), Write(earth_llbl))
        self.play(FadeIn(moon_l), Write(moon_llbl))
        self.play(Write(lun_title))

        lun_arr1 = Arrow(sun_l.get_right(), earth_l.get_left(),
                         color=YELLOW, buff=0.05, stroke_width=2)
        lun_arr2 = Arrow(earth_l.get_right(), moon_l.get_left(),
                         color=GREY, buff=0.05, stroke_width=2)
        self.play(GrowArrow(lun_arr1), GrowArrow(lun_arr2))

        lun_note = Text("Земјата фрла сенка врз Месечината → поцрвенува",
                        font_size=19, color=WHITE2)
        lun_note.move_to(RIGHT * 2.5 + DOWN * 2.8)
        self.play(FadeIn(lun_note, shift=UP * 0.15))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr3,
            sun_e, sun_lbl, moon_e, moon_lbl, earth_e, earth_lbl,
            sol_title, sol_arr1, sol_arr2, sol_note,
            sun_l, sun_llbl, earth_l, earth_llbl, moon_l, moon_llbl,
            lun_title, lun_arr1, lun_arr2, lun_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 5.  ПРАКТИЧНА ПРИМЕНА                               ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("practical")

        hdr4 = section_title("Практична примена на сенките")
        self.play(Write(hdr4), run_time=0.8)

        apps = VGroup(
            callout("Сонченик — покажува час преку сенка", width=10.0, border=YELLOW, font_size=24),
            callout("Мерење висина на дрво со слични триаголници", width=10.0, border=GREEN, font_size=24),
            callout("Пројекција во кино — сенка на филм → слика на ѕид", width=10.0, border=ORANGE, font_size=24),
        ).arrange(DOWN, buff=0.4)
        apps.shift(DOWN * 0.3)

        for app in apps:
            self.play(FadeIn(app, shift=DOWN * 0.2), run_time=0.55)
            self.wait(0.45)

        self.wait(1.5)
        self.play(FadeOut(hdr4), FadeOut(apps))

        # ══════════════════════════════════════════════════════════
        # 6.  АНDONОВСКИ МОМЕНТ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Сенката не е темнина.",   WHITE2, 36),
            ("Сенката е отсуство",      WHITE2, 36),
            ("на светлина.",            WHITE2, 36),
            ("Мала разлика.",           WHITE2, 32),
            ("Огромно значење.",        YELLOW, 48),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.36)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.42)

        self.play(Indicate(grp[-1], scale_factor=1.2, color=YELLOW))
        self.wait(3.0)

        self.play(FadeOut(grp))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                          ~9 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=44, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        bullets = [
            (BLUE,   "Сенка = зона без светлина зад непроѕирен предмет"),
            (WHITE2, "Умбра = потполна сенка; полусенка = делумна"),
            (YELLOW, "Сончево: Месечина помеѓу Сонце и Земја"),
            (ORANGE, "Месечево: Земја помеѓу Сонце и Месечина (Месечот поцрвенува)"),
            (GREEN,  "Практика: сонченик, мерење висина"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=22, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.shift(DOWN * 0.65 + RIGHT * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.5)
            self.wait(0.42)

        self.wait(3.0)
