"""
bio8-5-3  —  Мерење на варијација кај луѓе
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: nature loves the average,
extremes allowed, the bell curve as silent law.
Render:  manim -ql bio8-5-3.py Bio853Scene
Output:  media/videos/bio8-5-3/480p15/Bio853Scene.mp4
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


class Bio853Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Висини на класа.",     font_size=50, color=YELLOW, weight=BOLD)
        hook2 = Text("Прави крива.",          font_size=48, color=BLUE,   weight=BOLD)
        hook3 = Text("Бел ѕвонец.",           font_size=46, color=ORANGE, weight=BOLD)
        hook4 = Text("Природата сака просек.", font_size=38, color=GREEN)
        hook5 = Text("Но не наметнува. Дозволува екстреми.",
                     font_size=32, color=WHITE2)

        beats = VGroup(hook1, hook2, hook3, hook4, hook5).arrange(DOWN, buff=0.4)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(Write(b), run_time=0.9)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО МЕРИМЕ?                                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("what_to_measure")

        t2 = section_title("Што мериме кај луѓе?")
        self.play(Write(t2), run_time=0.9)

        traits = VGroup(
            VGroup(
                Text("Висина", font_size=30, color=BLUE, weight=BOLD),
                Text("непрекината", font_size=22, color=GREY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Тежина", font_size=30, color=GREEN, weight=BOLD),
                Text("непрекината", font_size=22, color=GREY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Виткање јазик", font_size=30, color=ORANGE, weight=BOLD),
                Text("прекината", font_size=22, color=GREY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Боја на очи", font_size=30, color=PURPLE, weight=BOLD),
                Text("прекината", font_size=22, color=GREY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                Text("Крвна група", font_size=30, color=RED, weight=BOLD),
                Text("прекината", font_size=22, color=GREY),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=0.6).next_to(t2, DOWN, buff=0.7)

        for tr in traits:
            self.play(FadeIn(tr, shift=UP * 0.2), run_time=0.5)

        self.wait(0.5)

        rule = callout("Непрекината → крива. Прекината → столбови.",
                       width=11.0, border=YELLOW, font_size=28)
        rule.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, traits, rule)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ВИСИНА — ХИСТОГРАМ                                ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("height_histogram")

        t3 = section_title("Висина — непрекината", color=BLUE)
        self.play(Write(t3), run_time=0.9)

        sub3 = Text("30 ученици од 8 одделение",
                    font_size=26, color=WHITE2)
        sub3.next_to(t3, DOWN, buff=0.25)
        self.play(Write(sub3), run_time=0.8)

        # histogram bins
        bins = ["145-150", "150-155", "155-160", "160-165",
                "165-170", "170-175", "175-180"]
        counts = [1, 3, 6, 10, 6, 3, 1]
        bar_w = 1.05
        base_y = -2.7
        bars = VGroup()
        bin_labels = VGroup()
        bar_objs = []

        for i, (b, c) in enumerate(zip(bins, counts)):
            x = -3.5 + i * (bar_w + 0.05)
            bar = Rectangle(
                width=bar_w, height=c * 0.35,
                fill_color=BLUE, fill_opacity=0.85,
                stroke_color=BLUE, stroke_width=2,
            )
            bar.move_to([x, base_y + c * 0.175, 0])
            bars.add(bar)
            bar_objs.append(bar)
            lab = Text(b, font_size=16, color=GREY)
            lab.next_to(bar, DOWN, buff=0.12)
            bin_labels.add(lab)

        for bar, lab in zip(bars, bin_labels):
            self.play(GrowFromEdge(bar, DOWN), Write(lab), run_time=0.35)

        self.wait(0.4)

        # draw bell curve over the bars
        curve = ParametricFunction(
            lambda t: np.array([
                -3.5 + t * 6 * (bar_w + 0.05) / 6.0 * 6.0,  # span
                base_y + 0.175 + 10 * 0.35 * np.exp(-((t - 3) ** 2) / 1.5),
                0,
            ]),
            t_range=[0, 6],
            color=YELLOW, stroke_width=4,
        )
        # simpler approach: just place a curve manually
        curve_pts = []
        for t in np.linspace(0, 6, 100):
            x = -3.5 + bar_w / 2 + t * (bar_w + 0.05)
            y = base_y + 10 * 0.35 * np.exp(-((t - 3) ** 2) / 1.5)
            curve_pts.append(np.array([x, y, 0]))
        bell = VMobject(stroke_color=YELLOW, stroke_width=5)
        bell.set_points_smoothly(curve_pts)

        self.play(Create(bell), run_time=1.5)
        self.wait(0.3)

        center_label = Text("Просек ~165 cm", font_size=24, color=YELLOW)
        center_label.move_to([0, 1.7, 0])
        self.play(Write(center_label), run_time=0.8)

        punch3 = Text("Многу во средина. Малку на крајот.",
                      font_size=28, color=WHITE2, weight=BOLD)
        punch3.to_edge(DOWN, buff=0.3)
        self.play(Write(punch3), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, sub3, bars, bin_labels, bell,
                                  center_label, punch3)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ВИТКАЊЕ ЈАЗИК — ПРЕКИНАТО                        ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("tongue_rolling")

        t4 = section_title("Виткање јазик — прекинато", color=ORANGE)
        self.play(Write(t4), run_time=0.9)

        sub4 = Text("Можеш или не можеш. Среден исход нема.",
                    font_size=28, color=WHITE2)
        sub4.next_to(t4, DOWN, buff=0.3)
        self.play(Write(sub4), run_time=1.0)

        # 2 big bars
        bar_yes = Rectangle(
            width=2.0, height=3.2,
            fill_color=GREEN, fill_opacity=0.85,
            stroke_color=GREEN, stroke_width=2,
        ).shift(LEFT * 2.0 + DOWN * 0.5)
        bar_no = Rectangle(
            width=2.0, height=1.5,
            fill_color=RED, fill_opacity=0.85,
            stroke_color=RED, stroke_width=2,
        ).shift(RIGHT * 2.0 + DOWN * 1.35)

        lab_yes = Text("Можат: 21",  font_size=28, color=GREEN, weight=BOLD)
        lab_yes.next_to(bar_yes, UP, buff=0.2)
        lab_no = Text("Не можат: 9", font_size=28, color=RED, weight=BOLD)
        lab_no.next_to(bar_no, UP, buff=0.2)

        cat_yes = Text("Да", font_size=30, color=WHITE2, weight=BOLD)
        cat_yes.next_to(bar_yes, DOWN, buff=0.25)
        cat_no = Text("Не", font_size=30, color=WHITE2, weight=BOLD)
        cat_no.next_to(bar_no, DOWN, buff=0.25)

        self.play(GrowFromEdge(bar_yes, DOWN), Write(lab_yes), Write(cat_yes), run_time=0.7)
        self.play(GrowFromEdge(bar_no, DOWN), Write(lab_no), Write(cat_no), run_time=0.7)

        self.wait(0.5)

        punch4 = Text("Две категории. Без средина.",
                      font_size=30, color=YELLOW, weight=BOLD)
        punch4.to_edge(DOWN, buff=0.3)
        self.play(Write(punch4), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t4, sub4, bar_yes, bar_no,
                                  lab_yes, lab_no, cat_yes, cat_no, punch4)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  БОЈА НА ОЧИ                                       ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("eye_color_bars")

        t5 = section_title("Боја на очи", color=PURPLE)
        self.play(Write(t5), run_time=0.9)

        eye_data = [
            ("Кафена", "#8a5a2f", 15),
            ("Сина",   BLUE,      8),
            ("Зелена", GREEN,     4),
            ("Сива",   GREY,      3),
        ]
        eye_bars = VGroup()
        eye_labels = VGroup()
        eye_nums = VGroup()
        base_y = -2.5
        for i, (name, col, c) in enumerate(eye_data):
            x = -3.6 + i * 2.4
            bar = Rectangle(
                width=1.6, height=c * 0.25,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=2,
            )
            bar.move_to([x, base_y + c * 0.125, 0])
            eye_bars.add(bar)
            lab = Text(name, font_size=24, color=WHITE2)
            lab.next_to(bar, DOWN, buff=0.2)
            eye_labels.add(lab)
            num = Text(str(c), font_size=24, color=col, weight=BOLD)
            num.next_to(bar, UP, buff=0.15)
            eye_nums.add(num)

        for bar, lab, num in zip(eye_bars, eye_labels, eye_nums):
            self.play(GrowFromEdge(bar, DOWN), Write(lab), Write(num), run_time=0.4)

        self.wait(0.5)

        punch5 = Text("Кафена доминира. Сива — реткост.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch5.to_edge(DOWN, buff=0.3)
        self.play(Write(punch5), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, eye_bars, eye_labels, eye_nums, punch5)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  КРВНИ ГРУПИ                                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("blood_types")

        t6 = section_title("Крвни групи", color=RED)
        self.play(Write(t6), run_time=0.9)

        sub6 = Text("Само 4 категории — A, B, AB, 0.",
                    font_size=28, color=WHITE2)
        sub6.next_to(t6, DOWN, buff=0.3)
        self.play(Write(sub6), run_time=0.9)

        blood = [
            ("A",  BLUE,   40),
            ("B",  GREEN,  10),
            ("AB", ORANGE,  5),
            ("0",  RED,    45),
        ]
        # pie chart
        pie = VGroup()
        pie_labels = VGroup()
        start_angle = PI / 2
        radius = 1.6
        center = np.array([0, -0.5, 0])
        for name, col, pct in blood:
            angle = pct / 100 * TAU
            sector = AnnularSector(
                inner_radius=0, outer_radius=radius,
                angle=angle, start_angle=start_angle,
                fill_color=col, fill_opacity=0.85,
                stroke_color=WHITE2, stroke_width=2,
            )
            sector.move_arc_center_to(center)
            pie.add(sector)
            mid = start_angle + angle / 2
            lab = Text(f"{name} ({pct}%)", font_size=22, color=col, weight=BOLD)
            lab.move_to(center + (radius + 0.6) * np.array([np.cos(mid), np.sin(mid), 0]))
            pie_labels.add(lab)
            start_angle += angle

        for s, l in zip(pie, pie_labels):
            self.play(FadeIn(s), Write(l), run_time=0.5)

        self.wait(0.5)

        punch6 = Text("Прекината — но богата на типови.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch6.to_edge(DOWN, buff=0.3)
        self.play(Write(punch6), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t6, sub6, pie, pie_labels, punch6)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("Мериме висини — добиваме крива.",
                      font_size=40, color=BLUE, weight=BOLD)
        final2 = Text("Броиме крвни групи — добиваме столбови.",
                      font_size=36, color=ORANGE, weight=BOLD)
        final3 = Text("Природа сака просек. Дозволува екстреми.",
                      font_size=34, color=YELLOW)
        final4 = Text("Варијација.",
                      font_size=46, color=GREEN, weight=BOLD)

        finals = VGroup(final1, final2, final3, final4).arrange(DOWN, buff=0.5)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.9)
            self.wait(0.3)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
