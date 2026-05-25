"""
phys8-2-2  —  Пренесување на енергија
Физика 8, Единица 2: Енергија

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-2-2.py Phys822Scene
Output:  media/videos/phys8-2-2/480p15/Phys822Scene.mp4
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


class Phys822Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Сонцето е 150 милиони km оддалечено.",
                    font_size=38, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)
        self.wait(0.6)

        sub = Text("Сепак те грее. Сепак те загрева. Зошто?",
                   font_size=32, color=WHITE2)
        sub.next_to(hook, DOWN, buff=0.35)
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.5)

        intro = Text("Зрачење.", font_size=60, color=ORANGE, weight=BOLD)
        intro.shift(DOWN * 0.8)
        self.play(Write(intro))
        self.play(Indicate(intro, scale_factor=1.2, color=ORANGE))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [hook, sub, intro]])

        # ══════════════════════════════════════════════════════════
        # 2.  ТРИ НАЧИНИ НА ПРЕНОС — три-панел изглед        ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_methods")

        hdr = section_title("Три начини на пренесување на енергија")
        self.play(Write(hdr), run_time=1.0)
        self.wait(0.5)

        # --- Panel A: Спроводливост ---
        pan_a = RoundedRectangle(
            width=4.2, height=5.0, corner_radius=0.35,
            fill_color="#0b2418", fill_opacity=1,
            stroke_color=RED, stroke_width=2,
        ).shift(LEFT * 4.5 + DOWN * 0.8)
        ta_title = Text("Спроводливост", font_size=24, color=RED, weight=BOLD)
        ta_title.next_to(pan_a.get_top(), DOWN, buff=0.3)
        ta_sub = Text("директен допир", font_size=19, color=GREY)
        ta_sub.next_to(ta_title, DOWN, buff=0.08)

        # metal bar gradient
        bar_left  = Rectangle(width=1.0, height=0.4,
                              fill_color=RED, fill_opacity=1, stroke_width=0)
        bar_mid   = Rectangle(width=1.0, height=0.4,
                              fill_color=ORANGE, fill_opacity=1, stroke_width=0)
        bar_right = Rectangle(width=1.0, height=0.4,
                              fill_color=GREY, fill_opacity=1, stroke_width=0)
        bar_grp   = VGroup(bar_left, bar_mid, bar_right).arrange(RIGHT, buff=0)
        bar_grp.next_to(ta_sub, DOWN, buff=0.6)
        heat_lbl = Text("топло → студено", font_size=18, color=GREY)
        heat_lbl.next_to(bar_grp, DOWN, buff=0.25)
        cond_note = VGroup(
            Text("Добри водачи:", font_size=18, color=WHITE2),
            Text("метали (бакар, сребро)", font_size=17, color=ORANGE),
            Text("Изолатори:", font_size=18, color=WHITE2),
            Text("дрво, пластика, воздух", font_size=17, color=GREEN),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        cond_note.next_to(heat_lbl, DOWN, buff=0.3)

        self.play(Create(pan_a))
        self.play(Write(ta_title), Write(ta_sub))
        self.play(FadeIn(bar_grp), Write(heat_lbl))
        self.play(FadeIn(cond_note))
        self.wait(0.6)

        # --- Panel B: Конвекција ---
        pan_b = RoundedRectangle(
            width=4.2, height=5.0, corner_radius=0.35,
            fill_color="#0d2233", fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).shift(DOWN * 0.8)
        tb_title = Text("Конвекција", font_size=24, color=ORANGE, weight=BOLD)
        tb_title.next_to(pan_b.get_top(), DOWN, buff=0.3)
        tb_sub = Text("движење на флуид", font_size=19, color=GREY)
        tb_sub.next_to(tb_title, DOWN, buff=0.08)

        # convection arrows
        up_arr1   = Arrow(ORIGIN + DOWN * 0.7, ORIGIN + UP * 0.7,
                          color=RED, buff=0, stroke_width=4)
        down_arr1 = Arrow(ORIGIN + UP * 0.7 + RIGHT * 0.9,
                          ORIGIN + DOWN * 0.7 + RIGHT * 0.9,
                          color=BLUE, buff=0, stroke_width=4)
        conv_arr = VGroup(up_arr1, down_arr1)
        conv_arr.next_to(tb_sub, DOWN, buff=0.4)
        hot_t = Text("топло ↑", font_size=18, color=RED)
        hot_t.next_to(up_arr1, LEFT, buff=0.1)
        cold_t = Text("ладно ↓", font_size=18, color=BLUE)
        cold_t.next_to(down_arr1, RIGHT, buff=0.1)

        self.play(Create(pan_b))
        self.play(Write(tb_title), Write(tb_sub))
        self.play(FadeIn(conv_arr), Write(hot_t), Write(cold_t))
        self.wait(0.6)

        # --- Panel C: Зрачење ---
        pan_c = RoundedRectangle(
            width=4.2, height=5.0, corner_radius=0.35,
            fill_color="#1f1408", fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2,
        ).shift(RIGHT * 4.5 + DOWN * 0.8)
        tc_title = Text("Зрачење", font_size=24, color=YELLOW, weight=BOLD)
        tc_title.next_to(pan_c.get_top(), DOWN, buff=0.3)
        tc_sub = Text("електромагнетни бранови", font_size=17, color=GREY)
        tc_sub.next_to(tc_title, DOWN, buff=0.08)

        sun = Circle(radius=0.38, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sun.next_to(tc_sub, DOWN, buff=0.45)
        rays = VGroup(*[
            Line(sun.get_center(), sun.get_center() + rotate_vector(RIGHT * 0.9, PI * i / 4),
                 color=YELLOW, stroke_width=2)
            for i in range(8)
        ])
        earth = Circle(radius=0.22, fill_color=BLUE, fill_opacity=1, stroke_width=0)
        earth.next_to(sun, RIGHT, buff=1.1)
        vac_note = Text("навакуум — без матерјал!", font_size=16, color=ORANGE)
        vac_note.next_to(earth, DOWN, buff=0.35)
        dark_note = VGroup(
            Text("Темни бои: апсорбираат повеќе", font_size=16, color=WHITE2),
            Text("Светли бои: одбиваат повеќе", font_size=16, color=GREY),
        ).arrange(DOWN, buff=0.1)
        dark_note.next_to(vac_note, DOWN, buff=0.25)

        self.play(Create(pan_c))
        self.play(Write(tc_title), Write(tc_sub))
        self.play(FadeIn(sun), Create(rays))
        self.play(FadeIn(earth))
        self.play(Write(vac_note), FadeIn(dark_note))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr,
            pan_a, ta_title, ta_sub, bar_grp, heat_lbl, cond_note,
            pan_b, tb_title, tb_sub, conv_arr, hot_t, cold_t,
            pan_c, tc_title, tc_sub, sun, rays, earth, vac_note, dark_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 3.  КОНВЕКЦИСКА ЈАМКА — детал                       ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("convection_cycle")

        hdr2 = section_title("Конвекциска јамка")
        self.play(Write(hdr2), run_time=0.9)

        pot = Rectangle(width=3.6, height=2.2, corner_radius=0.1,
                        fill_color="#0b1e30", fill_opacity=1,
                        stroke_color=GREY, stroke_width=3)
        pot.shift(DOWN * 0.4)
        flame = Triangle(fill_color=ORANGE, fill_opacity=1, stroke_width=0)
        flame.scale(0.35)
        flame.next_to(pot, DOWN, buff=0.08)

        steps = [
            "1. Топла течност се крева нагоре",
            "2. Се лади на врвот",
            "3. Ладна паѓа надолу",
            "4. Се загрева повторно → циклус",
        ]
        step_grp = VGroup()
        for s in steps:
            step_grp.add(Text(s, font_size=22, color=WHITE2))
        step_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        step_grp.shift(RIGHT * 3.0 + DOWN * 0.3)

        self.play(FadeIn(pot), FadeIn(flame))
        for step in step_grp:
            self.play(FadeIn(step, shift=RIGHT * 0.25), run_time=0.5)
            self.wait(0.55)

        self.wait(1.5)
        self.play(FadeOut(hdr2), FadeOut(pot), FadeOut(flame), FadeOut(step_grp))

        # ══════════════════════════════════════════════════════════
        # 4.  ТЕРМОС — практичен пример                       ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("thermos")

        hdr3 = section_title("Термосот — совршен изолатор")
        self.play(Write(hdr3), run_time=0.9)

        outer = RoundedRectangle(
            width=2.0, height=4.5, corner_radius=0.4,
            fill_color=GREY, fill_opacity=0.3,
            stroke_color=GREY, stroke_width=2,
        ).shift(LEFT * 3.2)
        inner = RoundedRectangle(
            width=1.3, height=3.8, corner_radius=0.3,
            fill_color="#0b1e30", fill_opacity=1,
            stroke_color=BLUE, stroke_width=1.5,
        ).move_to(outer)

        layers = VGroup(
            Text("вакуум → нема конвекција", font_size=19, color=BLUE),
            Text("сребрна лога → нема зрачење", font_size=19, color=YELLOW),
            Text("пластичен затворач → нема спроводливост", font_size=19, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        layers.shift(RIGHT * 1.5)

        lines = VGroup()
        for i, layer in enumerate(layers):
            ln = DashedLine(outer.get_right(), layer.get_left() + LEFT * 0.15,
                            color=GREY, dash_length=0.12, stroke_width=1.5)
            lines.add(ln)

        self.play(Create(outer), Create(inner))
        for layer, line in zip(layers, lines):
            self.play(FadeIn(layer, shift=RIGHT * 0.2), Create(line), run_time=0.6)
            self.wait(0.4)

        self.wait(2.0)
        self.play(FadeOut(hdr3), FadeOut(outer), FadeOut(inner),
                  FadeOut(layers), FadeOut(lines))

        # ══════════════════════════════════════════════════════════
        # 5.  АНDONОВСКИ МОМЕНТ                               ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Сонцето те грее низ вселена.",     WHITE2, 34),
            ("Без материја.",                     WHITE2, 34),
            ("Само бранови.",                     WHITE2, 34),
            ("Зрачењето — единствениот начин", WHITE2, 28),
            ("да патуваш низ ништо.",             YELLOW, 38),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.38)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.45)

        self.play(Indicate(grp[-1], scale_factor=1.2, color=YELLOW))
        self.wait(3.0)

        self.play(FadeOut(grp))

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЗИМЕ                                          ~9 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=44, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        bullets = [
            (RED,    "Спроводливост — директен допир, претежно цврсти тела"),
            (ORANGE, "Конвекција — движење на флуид, топло нагоре, ладно надолу"),
            (YELLOW, "Зрачење — електромагнетни бранови, работи во вакуум"),
            (GREEN,  "Термос: вакуум + сребро + пластика = изолација"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=23, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        rows.shift(DOWN * 0.65 + RIGHT * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.55)
            self.wait(0.5)

        self.wait(3.0)
