"""
bio8-1-2  —  Нервен систем — вовед
Биологија 8, Единица 1: Сетила и нервна координација

Teaching narrative — Andonovski-style: three-beat punches,
nerves as messengers, brain as commander, signals as drama.
Render:  manim -ql bio8-1-2.py Bio812Scene
Output:  media/videos/bio8-1-2/480p15/Bio812Scene.mp4
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


class Bio812Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Една мисла.",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.4)
        self.wait(0.3)

        beats = VGroup(
            Text("Стигнува за милисекунда.", font_size=36, color=WHITE2),
            Text("Преку нервите.",            font_size=36, color=BLUE),
            Text("Брзо колку светлина?",      font_size=34, color=ORANGE),
            Text("Не. Но доволно.",           font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — CNS vs PNS                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Два дела")
        self.play(Write(title), run_time=0.8)

        # body silhouette (simplified)
        body = VGroup()
        head = Circle(radius=0.55, color=WHITE2, stroke_width=2).shift(UP * 2.0)
        torso = RoundedRectangle(
            width=1.6, height=2.2, corner_radius=0.3,
            stroke_color=WHITE2, stroke_width=2, fill_opacity=0,
        ).shift(UP * 0.2)
        body.add(head, torso)
        body.shift(LEFT * 4.0)

        # brain (inside head)
        brain = Ellipse(width=0.7, height=0.5,
                        fill_color=PURPLE, fill_opacity=0.9,
                        stroke_color=WHITE2, stroke_width=1.5)
        brain.move_to(head.get_center())

        # spinal cord
        spine = Line(
            head.get_bottom() + DOWN * 0.05,
            torso.get_bottom() + UP * 0.1,
            color=PURPLE, stroke_width=8,
        )

        # peripheral nerves (branching out from spine)
        nerves = VGroup()
        for y in [1.3, 0.5, -0.3, -0.8]:
            n_l = Line(
                spine.get_center() + UP * (y - spine.get_center()[1]),
                spine.get_center() + UP * (y - spine.get_center()[1]) + LEFT * 1.2 + DOWN * 0.2,
                color=YELLOW, stroke_width=3,
            )
            n_r = Line(
                spine.get_center() + UP * (y - spine.get_center()[1]),
                spine.get_center() + UP * (y - spine.get_center()[1]) + RIGHT * 1.2 + DOWN * 0.2,
                color=YELLOW, stroke_width=3,
            )
            nerves.add(n_l, n_r)

        self.play(Create(body), run_time=1.0)
        self.play(FadeIn(brain), Create(spine), run_time=0.9)
        self.play(*[Create(n) for n in nerves], run_time=1.2)

        # CNS callout
        cns_box = callout("ЦНС: мозок + рбетен мозок",
                          width=5.2, border=PURPLE, font_size=24)
        cns_box.move_to(RIGHT * 2.2 + UP * 1.6)
        cns_arrow = Arrow(cns_box.get_left(), brain.get_right(),
                          buff=0.1, color=PURPLE, stroke_width=3)

        # PNS callout
        pns_box = callout("ПНС: нерви низ телото",
                          width=5.2, border=YELLOW, font_size=24)
        pns_box.move_to(RIGHT * 2.2 + DOWN * 0.4)
        pns_arrow = Arrow(pns_box.get_left(), nerves[3].get_right(),
                          buff=0.1, color=YELLOW, stroke_width=3)

        self.play(FadeIn(cns_box, shift=LEFT * 0.3), GrowArrow(cns_arrow), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(pns_box, shift=LEFT * 0.3), GrowArrow(pns_arrow), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, body, brain, spine, nerves,
                                  cns_box, cns_arrow, pns_box, pns_arrow)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — neuron close-up                     ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Невронот — една клетка")
        self.play(Write(title), run_time=0.8)

        # cell body
        soma = Circle(radius=0.7, fill_color=PURPLE, fill_opacity=0.85,
                      stroke_color=WHITE2, stroke_width=2)
        soma.move_to(LEFT * 1.5)
        nucleus = Circle(radius=0.25, fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=1.5)
        nucleus.move_to(soma.get_center())

        # dendrites (branching left)
        dendrites = VGroup()
        for angle_deg in [120, 150, 180, 210, 240]:
            ang = angle_deg * DEGREES
            start = soma.get_center() + 0.7 * np.array([np.cos(ang), np.sin(ang), 0])
            end = soma.get_center() + 1.7 * np.array([np.cos(ang), np.sin(ang), 0])
            d = Line(start, end, color=BLUE, stroke_width=4)
            dendrites.add(d)

        # axon (long line right)
        axon_start = soma.get_right()
        axon_end = RIGHT * 4.2
        axon = Line(axon_start, axon_end, color=YELLOW, stroke_width=5)

        # terminals
        terminals = VGroup()
        for dy in [-0.3, 0, 0.3]:
            t = Line(axon_end, axon_end + RIGHT * 0.5 + UP * dy,
                     color=GREEN, stroke_width=4)
            terminals.add(t)

        self.play(Create(dendrites), run_time=1.0)
        self.play(FadeIn(soma), FadeIn(nucleus), run_time=0.7)
        self.play(Create(axon), run_time=1.1)
        self.play(Create(terminals), run_time=0.6)

        # labels
        lbl_d = Text("Дендрити", font_size=22, color=BLUE).move_to(LEFT * 4.5 + UP * 1.5)
        arr_d = Arrow(lbl_d.get_right(), dendrites[2].get_left(),
                      buff=0.1, color=BLUE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.2)

        lbl_s = Text("Тело", font_size=22, color=PURPLE).move_to(LEFT * 1.5 + DOWN * 1.6)
        arr_s = Arrow(lbl_s.get_top(), soma.get_bottom(),
                      buff=0.1, color=PURPLE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.2)

        lbl_a = Text("Аксон", font_size=22, color=YELLOW).move_to(RIGHT * 1.5 + UP * 1.3)
        arr_a = Arrow(lbl_a.get_bottom(), axon.get_center() + UP * 0.05,
                      buff=0.1, color=YELLOW, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(lbl_d), GrowArrow(arr_d), run_time=0.7)
        self.play(FadeIn(lbl_s), GrowArrow(arr_s), run_time=0.7)
        self.play(FadeIn(lbl_a), GrowArrow(arr_a), run_time=0.7)
        self.wait(0.6)

        # electrical pulse traveling along axon
        pulse = Dot(point=axon_start, color=WHITE2, radius=0.15)
        glow = Circle(radius=0.25, color=YELLOW, stroke_width=3, fill_opacity=0)
        glow.move_to(pulse.get_center())
        self.play(FadeIn(pulse), FadeIn(glow), run_time=0.3)
        self.play(
            pulse.animate.move_to(axon_end),
            glow.animate.move_to(axon_end),
            run_time=1.2, rate_func=linear,
        )
        self.play(FadeOut(pulse), FadeOut(glow), run_time=0.3)

        self.wait(0.8)
        self.play(FadeOut(VGroup(
            title, soma, nucleus, dendrites, axon, terminals,
            lbl_d, arr_d, lbl_s, arr_s, lbl_a, arr_a,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — hot stove reflex                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Допираш нешто жешко")
        self.play(Write(title), run_time=0.8)

        steps = [
            ("Стимул",       "Топлина допира кожа.",          RED),
            ("Рецептор",     "Прима сигнал.",                 ORANGE),
            ("Сензорен нерв","Носи кон рбетен мозок.",        YELLOW),
            ("ЦНС",          "Одлучува: повлечи!",            PURPLE),
            ("Моторен нерв", "Носи команда до мускул.",       BLUE),
            ("Ефектор",      "Раката се повлекува.",          GREEN),
        ]

        step_group = VGroup()
        for label, action, col in steps:
            box = RoundedRectangle(
                width=11.0, height=0.7, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            l = Text(label, font_size=22, color=col, weight=BOLD)
            l.move_to(box.get_left() + RIGHT * 1.5)
            a = Text(action, font_size=22, color=WHITE2)
            a.move_to(box.get_left() + RIGHT * 5.8)
            step_group.add(VGroup(box, l, a))
        step_group.arrange(DOWN, buff=0.18).next_to(title, DOWN, buff=0.5)

        for s in step_group:
            self.play(FadeIn(s, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, step_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — signal speed                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("Колку брзо?")
        self.play(Write(title), run_time=0.8)

        speed_box = callout(
            "Нервен импулс: до 120 m/s",
            width=8.5, border=YELLOW, font_size=34,
        ).shift(UP * 1.3)
        self.play(FadeIn(speed_box, shift=UP * 0.2), run_time=0.8)

        # speed bar comparison
        items = [
            ("Молња",        300_000_000, BLUE),
            ("Звук",         343,         ORANGE),
            ("Нервен импулс", 120,        YELLOW),
            ("Тркало во град", 14,        GREEN),
        ]
        bars = VGroup()
        for i, (name, speed, col) in enumerate(items):
            row = VGroup()
            n = Text(name, font_size=22, color=col)
            n.move_to(LEFT * 4.7)
            v = Text(f"{speed:,} m/s".replace(",", " "),
                     font_size=22, color=WHITE2)
            v.move_to(RIGHT * 3.5)
            row.add(n, v)
            row.shift(DOWN * (i * 0.6))
            bars.add(row)
        bars.next_to(speed_box, DOWN, buff=0.5)

        for r in bars:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.8)

        concl = Text("Не светлина. Но реакција за миг.",
                     font_size=28, color=GREEN, weight=BOLD)
        concl.to_edge(DOWN, buff=0.5)
        self.play(Write(concl), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, speed_box, bars, concl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("ЦНС: мозок + рбетен мозок.",
                 font_size=30, color=PURPLE, weight=BOLD),
            Text("ПНС: нерви до секој дел.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Неврон: дендрити → тело → аксон.",
                 font_size=28, color=BLUE),
            Text("Брзо. Точно. Електрично.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
