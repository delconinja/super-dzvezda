"""
bio8-4-5  —  Истражување — пулс и вежбање
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
pulse as the heart's honest report, exercise as the test.
Render:  manim -ql bio8-4-5.py Bio845Scene
Output:  media/videos/bio8-4-5/480p15/Bio845Scene.mp4
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


class Bio845Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Притисни врат.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=0.9)

        beats = VGroup(
            Text("Брои за 15 секунди.",
                 font_size=34, color=BLUE),
            Text("Помножи со 4.",
                 font_size=34, color=ORANGE),
            Text("Тоа е твојот пулс.",
                 font_size=36, color=GREEN, weight=BOLD),
            Text("Реалниот извештај на твоето срце.",
                 font_size=32, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHERE TO MEASURE PULSE                           ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("where")

        title = section_title("Каде се мери пулсот")
        self.play(Write(title), run_time=0.8)

        # body figure — simple silhouette
        head = Circle(radius=0.5, color=WHITE2,
                      fill_color=DARK_CARD, fill_opacity=1,
                      stroke_color=WHITE2, stroke_width=2)
        head.move_to(UP * 2.0)
        torso = RoundedRectangle(width=1.6, height=2.0, corner_radius=0.3,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=WHITE2, stroke_width=2)
        torso.move_to(UP * 0.4)
        arm_l = RoundedRectangle(width=0.35, height=1.8, corner_radius=0.15,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=WHITE2, stroke_width=2)
        arm_l.move_to(LEFT * 1.1 + UP * 0.4)
        arm_r = RoundedRectangle(width=0.35, height=1.8, corner_radius=0.15,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=WHITE2, stroke_width=2)
        arm_r.move_to(RIGHT * 1.1 + UP * 0.4)
        body_grp = VGroup(head, torso, arm_l, arm_r)

        # spots
        spot_neck = Dot(UP * 1.5, radius=0.18, color=RED)
        spot_wrist = Dot(RIGHT * 1.1 + DOWN * 0.6, radius=0.18, color=RED)
        spot_temple = Dot(LEFT * 0.4 + UP * 2.2, radius=0.15, color=ORANGE)

        # labels
        lbl_neck = Text("каротидна — врат", font_size=22, color=RED, weight=BOLD)
        lbl_neck.move_to(LEFT * 3.5 + UP * 1.8)
        arr_neck = Arrow(lbl_neck.get_right(), spot_neck.get_left(),
                         color=RED, buff=0.15, stroke_width=3)

        lbl_wrist = Text("радијална — китка", font_size=22, color=RED, weight=BOLD)
        lbl_wrist.move_to(RIGHT * 4.0 + DOWN * 0.6)
        arr_wrist = Arrow(lbl_wrist.get_left(), spot_wrist.get_right(),
                          color=RED, buff=0.15, stroke_width=3)

        lbl_temple = Text("темпорална — слепоочница",
                          font_size=20, color=ORANGE)
        lbl_temple.move_to(LEFT * 3.5 + UP * 3.0)
        arr_temple = Arrow(lbl_temple.get_right(), spot_temple.get_left(),
                           color=ORANGE, buff=0.15, stroke_width=3)

        self.play(LaggedStart(*[Create(p) for p in body_grp],
                              lag_ratio=0.1), run_time=1.0)
        self.play(FadeIn(spot_neck, scale=0.5),
                  GrowArrow(arr_neck), FadeIn(lbl_neck), run_time=0.8)
        self.play(FadeIn(spot_wrist, scale=0.5),
                  GrowArrow(arr_wrist), FadeIn(lbl_wrist), run_time=0.8)
        self.play(FadeIn(spot_temple, scale=0.5),
                  GrowArrow(arr_temple), FadeIn(lbl_temple), run_time=0.8)

        # pulse animation — make dots pulse
        for _ in range(3):
            self.play(spot_neck.animate.scale(1.5),
                      spot_wrist.animate.scale(1.5),
                      run_time=0.2)
            self.play(spot_neck.animate.scale(1 / 1.5),
                      spot_wrist.animate.scale(1 / 1.5),
                      run_time=0.2)

        instr = callout("Два прста, не палец — палецот има свој пулс",
                        width=11.0, border=YELLOW, font_size=22)
        instr.move_to(DOWN * 2.8)
        self.play(FadeIn(instr), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, body_grp, spot_neck, spot_wrist,
                                 spot_temple, lbl_neck, lbl_wrist, lbl_temple,
                                 arr_neck, arr_wrist, arr_temple, instr)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  FORMULA                                          ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("formula")

        title = section_title("Како се пресметува")
        self.play(Write(title), run_time=0.8)

        formula = MathTex(r"\text{пулс} = (\text{удари за 15 s}) \times 4",
                          font_size=42, color=YELLOW)
        formula.move_to(UP * 1.5)

        # worked example
        ex_title = Text("Пример", font_size=28, color=ORANGE, weight=BOLD)
        ex_title.move_to(UP * 0.4)

        ex1 = MathTex(r"18 \text{ удари за } 15\text{ s}",
                      font_size=34, color=WHITE2)
        ex2 = MathTex(r"18 \times 4 = 72 \text{ удари/мин}",
                      font_size=36, color=GREEN)
        ex_grp = VGroup(ex1, ex2).arrange(DOWN, buff=0.4).next_to(ex_title, DOWN, buff=0.4)

        self.play(Write(formula), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(ex_title), run_time=0.5)
        self.play(Write(ex1), run_time=0.8)
        self.play(Write(ex2), run_time=1.0)

        result = callout("72 / мин — нормално!",
                         width=6.0, border=GREEN, font_size=26)
        result.move_to(DOWN * 2.8)
        self.play(FadeIn(result), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, formula, ex_title, ex_grp, result)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  NORMAL RANGES                                    ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ranges")

        title = section_title("Нормални вредности")
        self.play(Write(title), run_time=0.8)

        # horizontal scale 30-200
        ax = NumberLine(x_range=[30, 200, 20], length=11,
                        color=GREY, include_numbers=True,
                        font_size=20)
        ax.move_to(UP * 0.5)

        # zones
        zone_low = Rectangle(width=2.8, height=0.45,
                             fill_color=BLUE, fill_opacity=0.4,
                             stroke_width=0)
        zone_norm = Rectangle(width=2.8, height=0.45,
                              fill_color=GREEN, fill_opacity=0.55,
                              stroke_width=0)
        zone_high = Rectangle(width=2.8, height=0.45,
                              fill_color=ORANGE, fill_opacity=0.45,
                              stroke_width=0)
        zone_danger = Rectangle(width=2.0, height=0.45,
                                fill_color=RED, fill_opacity=0.45,
                                stroke_width=0)
        # place along ax
        zone_low.move_to(ax.n2p(45) + UP * 0.55)
        zone_norm.move_to(ax.n2p(80) + UP * 0.55)
        zone_high.move_to(ax.n2p(115) + UP * 0.55)
        zone_danger.move_to(ax.n2p(165) + UP * 0.55)

        l_low = Text("< 60 брадикардија", font_size=18, color=BLUE).next_to(zone_low, UP, buff=0.1)
        l_norm = Text("60–100 нормално", font_size=18, color=GREEN, weight=BOLD).next_to(zone_norm, UP, buff=0.1)
        l_high = Text("100–140 вежбање", font_size=18, color=ORANGE).next_to(zone_high, UP, buff=0.1)
        l_dan = Text("> 150 интензивно", font_size=18, color=RED).next_to(zone_danger, UP, buff=0.1)

        self.play(Create(ax), run_time=0.8)
        self.play(FadeIn(zone_low), FadeIn(zone_norm),
                  FadeIn(zone_high), FadeIn(zone_danger), run_time=0.7)
        self.play(FadeIn(l_low), FadeIn(l_norm),
                  FadeIn(l_high), FadeIn(l_dan), run_time=0.7)

        # examples
        ex = [
            ("Новороденче", "120–160", BLUE),
            ("Дете 7-12",   "75–110",  ORANGE),
            ("Возрасен",    "60–100",  GREEN),
            ("Атлет",       "40–60",   PURPLE),
        ]
        cards = VGroup()
        for n, v, col in ex:
            box = RoundedRectangle(
                width=11.5, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            nt = Text(n, font_size=22, color=col, weight=BOLD)
            nt.move_to(box.get_left() + RIGHT * 2.0)
            vt = Text(v + " удари/мин", font_size=22, color=WHITE2)
            vt.move_to(box.get_left() + RIGHT * 7.5)
            cards.add(VGroup(box, nt, vt))
        cards.arrange(DOWN, buff=0.15)
        cards.move_to(DOWN * 2.0)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, ax, zone_low, zone_norm,
                                 zone_high, zone_danger,
                                 l_low, l_norm, l_high, l_dan, cards)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  EXERCISE EFFECT — graph                          ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("graph")

        title = section_title("Ефект на вежба — графикон")
        self.play(Write(title), run_time=0.8)

        # axes — time (min) vs pulse
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[50, 170, 20],
            x_length=9.0,
            y_length=4.5,
            axis_config={"color": GREY, "include_tip": True,
                         "include_numbers": True,
                         "font_size": 20},
        )
        axes.move_to(DOWN * 0.3)

        x_lbl = Text("време (мин)", font_size=20, color=WHITE2)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = Text("пулс", font_size=20, color=WHITE2)
        y_lbl.next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI / 2)

        # data points
        # 0-2 min rest (70), 2-5 exercise rising (70->150),
        # 5-7 sustained (150), 7-12 recovery (150->75)
        def curve_y(x):
            if x <= 2:
                return 70
            elif x <= 5:
                return 70 + (x - 2) / 3 * 80
            elif x <= 7:
                return 150
            elif x <= 12:
                return 150 - (x - 7) / 5 * 75
            return 75

        graph = axes.plot(curve_y, x_range=[0, 12], color=RED, stroke_width=4)

        # phase markers
        phases = [
            (1.0, 75, "мирување", BLUE),
            (3.5, 110, "вежба", ORANGE),
            (6.0, 155, "врв", RED),
            (9.5, 105, "опоравување", GREEN),
        ]
        ph_text = VGroup()
        for x, y, label, col in phases:
            t = Text(label, font_size=20, color=col, weight=BOLD)
            t.move_to(axes.c2p(x, y) + UP * 0.4)
            ph_text.add(t)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.0)
        self.play(Create(graph), run_time=2.5)
        for t in ph_text:
            self.play(FadeIn(t, shift=UP * 0.2), run_time=0.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, axes, x_lbl, y_lbl, graph, ph_text)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  RECOVERY = FITNESS                               ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("recovery")

        title = section_title("Опоравување — мерило за кондиција")
        self.play(Write(title), run_time=0.8)

        compare = [
            ("Атлет",      "Пулс паѓа за 1–2 мин.",         GREEN),
            ("Просечен",   "Пулс паѓа за 3–5 мин.",         ORANGE),
            ("Седечки живот","Пулс останува висок 5+ мин.",  RED),
        ]
        cards = VGroup()
        for n, r, col in compare:
            box = RoundedRectangle(
                width=11.5, height=0.85, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            nt = Text(n, font_size=26, color=col, weight=BOLD)
            nt.move_to(box.get_left() + RIGHT * 2.0)
            rt = Text(r, font_size=22, color=WHITE2)
            rt.move_to(box.get_left() + RIGHT * 7.0)
            cards.add(VGroup(box, nt, rt))
        cards.arrange(DOWN, buff=0.2)
        cards.next_to(title, DOWN, buff=0.7)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.5)

        note = callout("Побрз опоравок = посилно срце",
                       width=8.5, border=YELLOW, font_size=26)
        note.move_to(DOWN * 2.7)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, cards, note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Притисни врат или китка.",
                 font_size=28, color=BLUE),
            Text("15 секунди × 4 = пулс/мин.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("60–100 во мирување — нормално.",
                 font_size=28, color=GREEN),
            Text("Побрз опоравок — посилно срце.",
                 font_size=30, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
