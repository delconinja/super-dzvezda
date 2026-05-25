"""
bio8-3-6  —  Дигестивен систем — патување низ телото
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
food as traveller, 9 metres as adventure, each organ a stop.
Render:  manim -ql bio8-3-6.py Bio836Scene
Output:  media/videos/bio8-3-6/480p15/Bio836Scene.mp4
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


def organ_node(name, color, radius=0.45):
    c = Circle(radius=radius, color=color, fill_opacity=0.7, stroke_width=2.5)
    label = Text(name, font_size=18, color=WHITE2, weight=BOLD)
    label.move_to(c)
    return VGroup(c, label)


class Bio836Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Залак леб.",
                     font_size=44, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.0)
        self.wait(0.3)

        beats = VGroup(
            Text("9 метри патување.",
                 font_size=38, color=ORANGE),
            Text("24 часа.",
                 font_size=36, color=BLUE),
            Text("Од уста до излез.",
                 font_size=34, color=GREEN),
            Text("Не случајно.",
                 font_size=36, color=RED, weight=BOLD),
            Text("Секој метар има задача.",
                 font_size=40, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.85)
            self.wait(0.2)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ПРЕГЛЕД НА ПАТОТ                                  ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("overview")

        t2 = section_title("Патот на залакот")
        self.play(Write(t2), run_time=0.8)

        organs = [
            ("Уста", BLUE),
            ("Хранопровод", ORANGE),
            ("Желудник", RED),
            ("Тенко црево", GREEN),
            ("Дебело црево", PURPLE),
            ("Ректум", YELLOW),
            ("Анус", GREY),
        ]

        nodes = VGroup()
        for name, color in organs:
            nodes.add(organ_node(name, color, radius=0.55))
        nodes.arrange(RIGHT, buff=0.25)
        nodes.scale(0.85)
        nodes.next_to(t2, DOWN, buff=1.0)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(
                nodes[i].get_right(), nodes[i + 1].get_left(),
                buff=0.05, stroke_width=3, color=WHITE2,
                max_tip_length_to_length_ratio=0.25,
            )
            arrows.add(a)

        for i, node in enumerate(nodes):
            self.play(FadeIn(node, shift=UP * 0.15), run_time=0.45)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(0.7)

        length_label = callout(
            "Вкупна должина: ≈ 9 метри",
            width=7.5, font_size=28, border=YELLOW,
        )
        length_label.next_to(nodes, DOWN, buff=0.9)
        self.play(FadeIn(length_label, shift=UP * 0.2), run_time=0.9)
        self.wait(0.5)

        time_label = callout(
            "Време на минување: 24–72 часа",
            width=7.5, font_size=28, border=ORANGE, bg="#3a2010",
        )
        time_label.next_to(length_label, DOWN, buff=0.3)
        self.play(FadeIn(time_label, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t2, nodes, arrows,
                                 length_label, time_label)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  УСТА                                             ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mouth")

        t3 = section_title("1. Уста", color=BLUE)
        self.play(Write(t3), run_time=0.7)

        mouth = organ_node("уста", BLUE, radius=1.1)
        mouth.shift(LEFT * 4 + DOWN * 0.4)
        self.play(FadeIn(mouth, shift=RIGHT * 0.2), run_time=0.7)

        tasks_m = VGroup(
            Text("• Забите кршат залакот.", font_size=26, color=WHITE2),
            Text("• Плунката навлажнува.", font_size=26, color=WHITE2),
            Text("• Амилаза почнува хемија.", font_size=26, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        tasks_m.next_to(mouth, RIGHT, buff=0.8)

        for t in tasks_m:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.6)

        self.wait(0.4)
        finisher_m = Text("Старт. Веднаш. Без чекање.",
                          font_size=28, color=YELLOW, weight=BOLD)
        finisher_m.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher_m), run_time=0.9)
        self.wait(0.7)

        self.play(FadeOut(VGroup(t3, mouth, tasks_m, finisher_m)),
                  run_time=0.5)

        # ══════════════════════════════════════════════════════════
        # 4.  ХРАНОПРОВОД + ЖЕЛУДНИК                            ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("esophagus_stomach")

        t4 = section_title("2. Хранопровод и желудник", color=ORANGE)
        self.play(Write(t4), run_time=0.7)

        # esophagus = vertical tube
        eso = Rectangle(
            width=0.6, height=3.0, color=ORANGE,
            fill_opacity=0.4, stroke_width=2.5,
        ).shift(LEFT * 4 + DOWN * 0.2)
        eso_label = Text("Хранопровод", font_size=22, color=ORANGE)
        eso_label.next_to(eso, DOWN, buff=0.2)

        # stomach = blob
        stomach = Ellipse(
            width=2.2, height=2.6, color=RED,
            fill_opacity=0.4, stroke_width=2.5,
        ).shift(LEFT * 1 + DOWN * 0.2)
        stomach_label = Text("Желудник", font_size=22, color=RED)
        stomach_label.next_to(stomach, DOWN, buff=0.2)

        self.play(Create(eso), FadeIn(eso_label), run_time=0.7)

        # peristalsis = ball moving down esophagus
        bolus = Circle(radius=0.18, color=YELLOW, fill_opacity=1)
        bolus.move_to(eso.get_top())
        self.play(FadeIn(bolus), run_time=0.3)
        self.play(bolus.animate.move_to(eso.get_bottom()),
                  run_time=1.3, rate_func=linear)
        self.play(FadeOut(bolus), run_time=0.2)

        self.play(Create(stomach), FadeIn(stomach_label), run_time=0.7)

        # churning motion (small dots)
        dots = VGroup(*[
            Dot(point=stomach.get_center() + np.array([
                np.cos(a) * 0.6, np.sin(a) * 0.7, 0
            ]), color=YELLOW, radius=0.08)
            for a in np.linspace(0, 2 * np.pi, 6, endpoint=False)
        ])
        self.play(FadeIn(dots), run_time=0.4)
        for _ in range(2):
            self.play(Rotate(dots, angle=PI, about_point=stomach.get_center()),
                      run_time=0.8, rate_func=linear)
        self.play(FadeOut(dots), run_time=0.3)

        tasks_s = VGroup(
            Text("• Перисталтика — бранови.", font_size=24, color=WHITE2),
            Text("• Желудочна киселина.", font_size=24, color=WHITE2),
            Text("• Пепсин разградува белки.", font_size=24, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        tasks_s.shift(RIGHT * 3 + DOWN * 0.2)

        for t in tasks_s:
            self.play(FadeIn(t, shift=LEFT * 0.2), run_time=0.5)

        self.wait(0.8)
        self.play(FadeOut(VGroup(t4, eso, eso_label, stomach,
                                 stomach_label, tasks_s)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ТЕНКО ЦРЕВО — главното место                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("small_intestine")

        t5 = section_title("3. Тенко црево", color=GREEN)
        self.play(Write(t5), run_time=0.7)

        # coiled intestine path
        path = VMobject(color=GREEN, stroke_width=4)
        pts = []
        for i in range(120):
            x = -3 + i * 0.05
            y = 0.4 * np.sin(i * 0.6)
            pts.append([x, y, 0])
        path.set_points_as_corners(pts)
        path.shift(DOWN * 0.5)
        self.play(Create(path), run_time=1.6)

        len_lbl = Text("≈ 6 метри",
                       font_size=28, color=YELLOW, weight=BOLD)
        len_lbl.next_to(path, DOWN, buff=0.5)
        self.play(Write(len_lbl), run_time=0.7)
        self.wait(0.3)

        tasks_si = VGroup(
            Text("• Главно место за варење.",
                 font_size=26, color=WHITE2),
            Text("• Главно место за апсорпција.",
                 font_size=26, color=WHITE2),
            Text("• Винчести цревни ресички.",
                 font_size=26, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        tasks_si.next_to(len_lbl, DOWN, buff=0.4)

        for t in tasks_si:
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.55)

        self.wait(0.8)
        self.play(FadeOut(VGroup(t5, path, len_lbl, tasks_si)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ДЕБЕЛО ЦРЕВО → ИЗЛЕЗ                             ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("large_intestine")

        t6 = section_title("4. Дебело црево → излез", color=PURPLE)
        self.play(Write(t6), run_time=0.7)

        # large intestine — thicker tube
        large = VMobject(color=PURPLE, stroke_width=10)
        large.set_points_as_corners([
            [-4, -1, 0],
            [-4, 1.5, 0],
            [-1, 1.5, 0],
            [-1, -1, 0],
            [1, -1, 0],
        ])
        self.play(Create(large), run_time=1.4)

        rectum = Line([1, -1, 0], [1, -2, 0], color=YELLOW, stroke_width=10)
        anus = Dot([1, -2.2, 0], color=GREY, radius=0.18)

        rectum_lbl = Text("Ректум", font_size=22, color=YELLOW)
        rectum_lbl.next_to(rectum, RIGHT, buff=0.25)
        anus_lbl = Text("Анус", font_size=22, color=GREY)
        anus_lbl.next_to(anus, RIGHT, buff=0.25)

        large_lbl = Text("Дебело црево ≈ 1.5 м",
                         font_size=24, color=PURPLE)
        large_lbl.next_to(large, UP, buff=0.3)

        self.play(Create(rectum), FadeIn(rectum_lbl), run_time=0.6)
        self.play(FadeIn(anus), FadeIn(anus_lbl), run_time=0.5)
        self.play(Write(large_lbl), run_time=0.6)

        tasks_li = VGroup(
            Text("• Апсорпција на вода.",
                 font_size=24, color=WHITE2),
            Text("• Бактерии — витамин К.",
                 font_size=24, color=WHITE2),
            Text("• Формирање измет.",
                 font_size=24, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        tasks_li.shift(RIGHT * 3.5 + DOWN * 0.5)

        for t in tasks_li:
            self.play(FadeIn(t, shift=LEFT * 0.15), run_time=0.5)

        self.wait(0.7)
        self.play(FadeOut(VGroup(t6, large, rectum, anus,
                                 rectum_lbl, anus_lbl, large_lbl,
                                 tasks_li)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conclusion")

        t7 = section_title("Заклучок", color=GREEN)
        self.play(Write(t7), run_time=0.7)

        final = VGroup(
            Text("Уста почнува.",
                 font_size=32, color=BLUE),
            Text("Желудник меша.",
                 font_size=32, color=RED),
            Text("Тенко црево апсорбира.",
                 font_size=32, color=GREEN, weight=BOLD),
            Text("Дебело црево заштедува.",
                 font_size=32, color=PURPLE),
            Text("Патување.",
                 font_size=44, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(t7, DOWN, buff=0.6)

        for line in final:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.75)
            self.wait(0.2)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t7, final)), run_time=0.8)
        self.wait(0.4)
