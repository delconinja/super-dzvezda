"""
bio8-5-1  —  Што е вид? Дефиниција и видови варијација
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: three-beat punches,
species as identity, variation as fingerprint of life.
Render:  manim -ql bio8-5-1.py Bio851Scene
Output:  media/videos/bio8-5-1/480p15/Bio851Scene.mp4
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


def little_person(color=BLUE, height=1.0):
    """Returns a stylized human silhouette."""
    head = Circle(radius=0.18, color=color, fill_color=color, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(
        width=0.36, height=0.55, corner_radius=0.1,
        fill_color=color, fill_opacity=1, stroke_width=0,
    )
    body.next_to(head, DOWN, buff=0.05)
    legs_l = Line(body.get_bottom() + LEFT * 0.1, body.get_bottom() + LEFT * 0.12 + DOWN * 0.35,
                  color=color, stroke_width=4)
    legs_r = Line(body.get_bottom() + RIGHT * 0.1, body.get_bottom() + RIGHT * 0.12 + DOWN * 0.35,
                  color=color, stroke_width=4)
    g = VGroup(head, body, legs_l, legs_r)
    g.scale(height)
    return g


class Bio851Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Сите луѓе.",
                     font_size=52, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Еден вид.",                       font_size=50, color=BLUE,   weight=BOLD),
            Text("Но никои двајца исти.",           font_size=40, color=WHITE2),
            Text("Дури близнаци имаат разлики.",    font_size=36, color=ORANGE),
            Text("Тоа е варијација.",               font_size=44, color=GREEN,  weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(Write(line), run_time=0.9)
            self.wait(0.35)

        self.wait(1.0)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е ВИД?                                       ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("species_definition")

        t2 = section_title("Што е вид?")
        self.play(Write(t2), run_time=0.9)

        defn = callout("Вид = група живи суштества кои се размножуваат",
                       width=11.0, border=YELLOW, font_size=28)
        defn.next_to(t2, DOWN, buff=0.5)
        defn2 = callout("и даваат плодно потомство.",
                        width=11.0, border=YELLOW, font_size=28)
        defn2.next_to(defn, DOWN, buff=0.2)

        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(defn2, shift=UP * 0.2), run_time=0.7)
        self.wait(0.6)

        # examples row
        examples = VGroup(
            VGroup(
                Circle(radius=0.45, color=BLUE, fill_color=BLUE, fill_opacity=0.5),
                Text("Човек", font_size=24, color=WHITE2),
            ).arrange(DOWN, buff=0.25),
            VGroup(
                Circle(radius=0.45, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5),
                Text("Куче", font_size=24, color=WHITE2),
            ).arrange(DOWN, buff=0.25),
            VGroup(
                Circle(radius=0.45, color=GREEN, fill_color=GREEN, fill_opacity=0.5),
                Text("Мачка", font_size=24, color=WHITE2),
            ).arrange(DOWN, buff=0.25),
            VGroup(
                Circle(radius=0.45, color=PURPLE, fill_color=PURPLE, fill_opacity=0.5),
                Text("Делфин", font_size=24, color=WHITE2),
            ).arrange(DOWN, buff=0.25),
        ).arrange(RIGHT, buff=1.0).next_to(defn2, DOWN, buff=0.7)

        for ex in examples:
            self.play(FadeIn(ex, shift=UP * 0.2), run_time=0.5)

        self.wait(0.6)

        note = Text("Секој вид — своја приказна. Свои гени. Свои граници.",
                    font_size=28, color=YELLOW)
        note.next_to(examples, DOWN, buff=0.6)
        self.play(Write(note), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, defn, defn2, examples, note)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ВНАТРЕШНА ВАРИЈАЦИЈА                              ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("intraspecific")

        t3 = section_title("Внатре во еден вид")
        self.play(Write(t3), run_time=0.9)

        sub = Text("Сите луѓе припаѓаат на ист вид — Homo sapiens.",
                   font_size=30, color=WHITE2)
        sub.next_to(t3, DOWN, buff=0.4)
        self.play(Write(sub), run_time=1.0)
        self.wait(0.3)

        # row of differently-coloured people
        people_colors = [BLUE, ORANGE, GREEN, PURPLE, RED, YELLOW]
        people = VGroup(*[little_person(color=c, height=1.2) for c in people_colors])
        people.arrange(RIGHT, buff=0.6).next_to(sub, DOWN, buff=0.6)

        for p in people:
            self.play(FadeIn(p, shift=UP * 0.2), run_time=0.3)

        self.wait(0.4)

        # differences callout
        diffs = VGroup(
            Text("Висина.",          font_size=32, color=BLUE,   weight=BOLD),
            Text("Боја на коса.",    font_size=32, color=ORANGE, weight=BOLD),
            Text("Боја на очи.",     font_size=32, color=GREEN,  weight=BOLD),
            Text("Облик на лице.",   font_size=32, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(people, DOWN, buff=0.5)

        for d in diffs:
            self.play(Write(d), run_time=0.6)

        self.wait(0.6)

        punch = Text("Истиот вид. Различни лица.",
                     font_size=32, color=YELLOW, weight=BOLD)
        punch.next_to(diffs, DOWN, buff=0.5)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, sub, people, diffs, punch)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ДВА ТИПА ВАРИЈАЦИЈА                               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("two_types")

        t4 = section_title("Два типа варијација")
        self.play(Write(t4), run_time=0.9)

        # split panels
        left_panel = RoundedRectangle(
            width=5.5, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).shift(LEFT * 3.4 + DOWN * 0.3)
        right_panel = RoundedRectangle(
            width=5.5, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).shift(RIGHT * 3.4 + DOWN * 0.3)

        left_label = Text("Непрекината", font_size=34, color=BLUE, weight=BOLD)
        left_label.move_to(left_panel.get_top() + DOWN * 0.5)
        right_label = Text("Прекината", font_size=34, color=ORANGE, weight=BOLD)
        right_label.move_to(right_panel.get_top() + DOWN * 0.5)

        self.play(
            FadeIn(left_panel), FadeIn(right_panel),
            Write(left_label), Write(right_label),
            run_time=1.0,
        )

        left_items = VGroup(
            Text("Висина", font_size=28, color=WHITE2),
            Text("Тежина", font_size=28, color=WHITE2),
            Text("Должина на стапало", font_size=26, color=WHITE2),
            Text("Сите вредности", font_size=26, color=YELLOW),
            Text("во низа.", font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.25).next_to(left_label, DOWN, buff=0.4)

        right_items = VGroup(
            Text("Крвна група", font_size=28, color=WHITE2),
            Text("Закачена увка", font_size=28, color=WHITE2),
            Text("Виткање јазик", font_size=26, color=WHITE2),
            Text("Само неколку", font_size=26, color=YELLOW),
            Text("категории.", font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.25).next_to(right_label, DOWN, buff=0.4)

        for li, ri in zip(left_items, right_items):
            self.play(Write(li), Write(ri), run_time=0.45)

        self.wait(1.8)
        self.play(FadeOut(VGroup(
            t4, left_panel, right_panel, left_label, right_label,
            left_items, right_items)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  НЕПРЕКИНАТА — КРИВА                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("continuous_curve")

        t5 = section_title("Непрекината варијација", color=BLUE)
        self.play(Write(t5), run_time=0.9)

        axes = Axes(
            x_range=[140, 200, 10], y_range=[0, 20, 5],
            x_length=9, y_length=3.5,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        ).shift(DOWN * 0.5)
        x_lab = Text("Висина (cm)", font_size=24, color=WHITE2)
        x_lab.next_to(axes.x_axis, DOWN, buff=0.3)
        y_lab = Text("Број ученици", font_size=24, color=WHITE2)
        y_lab.rotate(PI/2).next_to(axes.y_axis, LEFT, buff=0.3)

        self.play(Create(axes), Write(x_lab), Write(y_lab), run_time=1.2)

        # bell curve
        curve = axes.plot(
            lambda x: 18 * np.exp(-((x - 170) ** 2) / 100.0),
            x_range=[140, 200], color=BLUE, stroke_width=4,
        )
        area = axes.get_area(curve, x_range=[140, 200], color=BLUE, opacity=0.25)

        self.play(Create(curve), run_time=1.4)
        self.play(FadeIn(area), run_time=0.8)

        punch5 = Text("Природата прави крива. Бел ѕвонец.",
                      font_size=30, color=YELLOW, weight=BOLD)
        punch5.to_edge(DOWN, buff=0.5)
        self.play(Write(punch5), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, axes, x_lab, y_lab, curve, area, punch5)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  ПРЕКИНАТА — КАТЕГОРИИ                           ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("discrete_bars")

        t6 = section_title("Прекината варијација", color=ORANGE)
        self.play(Write(t6), run_time=0.9)

        sub6 = Text("Крвни групи во една паралелка",
                    font_size=28, color=WHITE2)
        sub6.next_to(t6, DOWN, buff=0.3)
        self.play(Write(sub6), run_time=0.8)

        # bar chart
        groups = ["A", "B", "AB", "0"]
        counts = [11, 6, 3, 10]
        colors = [BLUE, GREEN, ORANGE, RED]
        bars = VGroup()
        labels = VGroup()
        nums = VGroup()
        base_y = -2.4
        for i, (g, c, col) in enumerate(zip(groups, counts, colors)):
            x = -3.5 + i * 2.2
            bar = Rectangle(
                width=1.4, height=c * 0.22,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=2,
            )
            bar.move_to([x, base_y + c * 0.11, 0])
            bars.add(bar)
            lab = Text(g, font_size=30, color=WHITE2, weight=BOLD)
            lab.move_to([x, base_y - 0.35, 0])
            labels.add(lab)
            num = Text(str(c), font_size=26, color=col, weight=BOLD)
            num.next_to(bar, UP, buff=0.15)
            nums.add(num)

        for bar, lab, num in zip(bars, labels, nums):
            self.play(GrowFromEdge(bar, DOWN), Write(lab), Write(num), run_time=0.4)

        self.wait(0.6)

        punch6 = Text("Категории. Не низа. Прескок.",
                      font_size=30, color=YELLOW, weight=BOLD)
        punch6.to_edge(DOWN, buff=0.5)
        self.play(Write(punch6), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t6, sub6, bars, labels, nums, punch6)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("Еден вид.",          font_size=54, color=YELLOW, weight=BOLD)
        final2 = Text("Илјадници лица.",    font_size=50, color=BLUE,   weight=BOLD)
        final3 = Text("Никое исто.",        font_size=46, color=ORANGE)
        final4 = Text("Варијација — отпечаток на животот.",
                      font_size=36, color=GREEN, weight=BOLD)

        finals = VGroup(final1, final2, final3, final4).arrange(DOWN, buff=0.45)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.9)
            self.wait(0.3)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
