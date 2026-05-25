"""
chem8-2-1  —  Секојдневни материјали и нивните својства
Хемија 8, Единица 2: Материјали околу нас

Teaching narrative — Andonovski-style: three-beat punches,
materials as characters, не...туку contrast, one-word finishers.
Render:  manim -ql chem8-2-1.py Chem821Scene
Output:  media/videos/chem8-2-1/480p15/Chem821Scene.mp4
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


def material_card(name, color, pos, icon_builder=None, width=3.6, height=2.4):
    card = RoundedRectangle(
        width=width, height=height, corner_radius=0.22,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=3,
    ).move_to(pos)
    label = Text(name, font_size=26, color=color, weight=BOLD)
    label.next_to(card.get_top(), DOWN, buff=0.18)
    g = VGroup(card, label)
    if icon_builder is not None:
        icon = icon_builder()
        icon.move_to(card.get_center() + DOWN * 0.2)
        g.add(icon)
    return g


class Chem821Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Стакло пука.", font_size=48, color=BLUE, weight=BOLD)
        h2 = Text("Метал свиткува.", font_size=48, color=ORANGE, weight=BOLD)
        h3 = Text("Дрво гори.", font_size=48, color=RED, weight=BOLD)
        h1.move_to(UP * 2.0)
        h2.next_to(h1, DOWN, buff=0.35)
        h3.next_to(h2, DOWN, buff=0.35)

        self.play(Write(h1), run_time=0.9)
        self.wait(0.3)
        self.play(Write(h2), run_time=0.9)
        self.wait(0.3)
        self.play(Write(h3), run_time=0.9)
        self.wait(0.6)

        line2 = Text("Секој материјал има карактер.",
                     font_size=34, color=WHITE2)
        line2.next_to(h3, DOWN, buff=0.55)
        self.play(Write(line2), run_time=1.2)
        self.wait(0.5)

        line3 = Text("Дури и тивкиот пластика.",
                     font_size=34, color=PURPLE, weight=BOLD)
        line3.next_to(line2, DOWN, buff=0.30)
        self.play(Write(line3), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(h1, h2, h3, line2, line3)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                       ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е материјал?")
        self.play(Write(t2), run_time=0.9)

        defn = callout(
            "Материјал = супстанца од која правиме предмети.",
            width=11.5, font_size=28,
        )
        defn.next_to(t2, DOWN, buff=0.7)
        self.play(FadeIn(defn), run_time=0.8)
        self.wait(0.6)

        sub = Text("Секој има својства. Секое својство — намена.",
                   font_size=30, color=WHITE2)
        sub.next_to(defn, DOWN, buff=0.55)
        self.play(Write(sub), run_time=1.3)
        self.wait(1.0)

        finish = Text("Намена.", font_size=44, color=YELLOW, weight=BOLD)
        finish.next_to(sub, DOWN, buff=0.55)
        self.play(Write(finish), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(t2, defn, sub, finish)))

        # ══════════════════════════════════════════════════════════
        # 3.  ШЕСТ-КАРТИЧНА ГРИДА — материјали                 ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("grid")

        t3 = section_title("Шест материјали. Шест карактери.")
        self.play(Write(t3), run_time=0.9)

        # icon builders
        def metal_icon():
            return VGroup(
                Rectangle(width=1.6, height=0.5,
                          fill_color=GREY, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=2),
                Text("Fe", font_size=22, color=YELLOW, weight=BOLD).shift(DOWN*0.0),
            ).arrange(DOWN, buff=0.18)

        def plastic_icon():
            return RoundedRectangle(width=1.6, height=0.6, corner_radius=0.15,
                                    fill_color=PURPLE, fill_opacity=0.9,
                                    stroke_color=WHITE2, stroke_width=2)

        def glass_icon():
            return RoundedRectangle(width=1.6, height=0.7, corner_radius=0.1,
                                    fill_color=BLUE, fill_opacity=0.3,
                                    stroke_color=BLUE, stroke_width=3)

        def wood_icon():
            return VGroup(
                Rectangle(width=1.7, height=0.5,
                          fill_color="#8b5a2b", fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1.5),
                Line(LEFT*0.7, RIGHT*0.7, color="#5b3a1b", stroke_width=2),
            )

        def ceramic_icon():
            return VGroup(
                Arc(radius=0.5, angle=PI, color=ORANGE, stroke_width=4,
                    fill_color=ORANGE, fill_opacity=0.7),
                Line(LEFT*0.5, RIGHT*0.5, color=WHITE2, stroke_width=2).shift(DOWN*0.0),
            )

        def fabric_icon():
            grp = VGroup()
            for i in range(3):
                grp.add(Line(LEFT*0.7, RIGHT*0.7, color=GREEN, stroke_width=3)
                        .shift(UP*(0.2 - i*0.2)))
            return grp

        # 6 cards in 2x3 grid
        positions = [
            LEFT*4.2 + UP*1.0,  LEFT*0.0 + UP*1.0,  RIGHT*4.2 + UP*1.0,
            LEFT*4.2 + DOWN*1.9, LEFT*0.0 + DOWN*1.9, RIGHT*4.2 + DOWN*1.9,
        ]
        names_colors_icons = [
            ("Метали", GREY, metal_icon),
            ("Пластика", PURPLE, plastic_icon),
            ("Стакло", BLUE, glass_icon),
            ("Дрво", ORANGE, wood_icon),
            ("Керамика", RED, ceramic_icon),
            ("Текстил", GREEN, fabric_icon),
        ]
        cards = VGroup()
        for pos, (n, c, ic) in zip(positions, names_colors_icons):
            cards.add(material_card(n, c, pos, icon_builder=ic,
                                    width=3.6, height=2.3))

        for c in cards:
            self.play(FadeIn(c), run_time=0.35)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, cards)))

        # ══════════════════════════════════════════════════════════
        # 4.  СВОЈСТВА — споредна табела                       ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("properties_table")

        t4 = section_title("Својства. Секое — карактер.")
        self.play(Write(t4), run_time=0.9)

        # Build a compact 5-property table for 4 materials
        headers = ["Материјал", "Тврдост", "Сјај", "Спроводник", "Гори?"]
        rows = [
            ("Бакар",    "средна",  "има",   "ДА",   "не"),
            ("Стакло",   "висока",  "нема",  "не",   "не"),
            ("Дрво",     "ниска",   "нема",  "не",   "ДА"),
            ("Пластика", "ниска",   "нема",  "не",   "ДА"),
        ]

        col_widths = [2.2, 1.9, 1.4, 2.2, 1.4]
        col_x = [-5.0, -2.7, -0.7, 0.9, 3.0]
        row_y_start = 1.7

        # header background
        header_bg = Rectangle(
            width=sum(col_widths) + 0.4, height=0.7,
            fill_color="#15324d", fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2,
        ).move_to([(col_x[0] + col_x[-1])/2 + 0.4, row_y_start, 0])
        self.play(FadeIn(header_bg), run_time=0.4)

        header_texts = VGroup()
        for h, x in zip(headers, col_x):
            t = Text(h, font_size=22, color=YELLOW, weight=BOLD)
            t.move_to([x + 0.4, row_y_start, 0])
            header_texts.add(t)
        self.play(Write(header_texts), run_time=0.9)
        self.wait(0.3)

        # data rows
        for i, row in enumerate(rows):
            y = row_y_start - 0.65 * (i + 1)
            row_group = VGroup()
            for val, x in zip(row, col_x):
                col = WHITE2
                if val == "ДА":
                    col = GREEN
                elif val == "не":
                    col = GREY
                t = Text(val, font_size=22, color=col)
                t.move_to([x + 0.4, y, 0])
                row_group.add(t)
            self.play(FadeIn(row_group), run_time=0.55)

        self.wait(1.6)

        verdict = Text("Никој не е најдобар. Сите се најдобри — некаде.",
                       font_size=28, color=YELLOW, weight=BOLD)
        verdict.next_to(header_bg, DOWN, buff=3.2)
        self.play(Write(verdict), run_time=1.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, header_bg, header_texts, *self.mobjects)))

        # ══════════════════════════════════════════════════════════
        # 5.  ПРИМЕР — жица за струја                          ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example_cable")

        t5 = section_title("Жица. Два материјали. Една задача.")
        self.play(Write(t5), run_time=0.9)

        # Cable cross-section: copper core + plastic insulation
        insulation = Circle(radius=1.5,
                            fill_color=PURPLE, fill_opacity=0.85,
                            stroke_color=WHITE2, stroke_width=2)
        copper = Circle(radius=0.7,
                        fill_color="#c87533", fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=2)
        cu_label = Text("Cu", font_size=30, color=WHITE2, weight=BOLD)
        cu_label.move_to(copper)
        cable = VGroup(insulation, copper, cu_label)
        cable.move_to(LEFT * 3.5 + DOWN * 0.4)

        self.play(FadeIn(insulation), run_time=0.6)
        self.play(FadeIn(copper), FadeIn(cu_label), run_time=0.7)
        self.wait(0.3)

        # Labels with arrows
        ar1 = Arrow(start=RIGHT*1.0, end=LEFT*0.5,
                    color=ORANGE, buff=0.1)
        ar1.next_to(copper, RIGHT, buff=1.4)
        lab1 = Text("бакар — спроводник", font_size=26, color=ORANGE)
        lab1.next_to(ar1, RIGHT, buff=0.1)

        ar2 = Arrow(start=RIGHT*1.0, end=LEFT*0.5,
                    color=PURPLE, buff=0.1)
        ar2.next_to(insulation, RIGHT, buff=0.2)
        ar2.shift(UP*0.9)
        lab2 = Text("пластика — изолатор", font_size=26, color=PURPLE)
        lab2.next_to(ar2, RIGHT, buff=0.1)

        self.play(GrowArrow(ar1), Write(lab1), run_time=0.9)
        self.play(GrowArrow(ar2), Write(lab2), run_time=0.9)
        self.wait(0.7)

        verdict5 = Text("Не случајност. Дизајн.",
                        font_size=34, color=YELLOW, weight=BOLD)
        verdict5.to_edge(DOWN, buff=0.7)
        self.play(Write(verdict5), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, cable, ar1, ar2, lab1, lab2, verdict5)))

        # ══════════════════════════════════════════════════════════
        # 6.  ВО ЖИВОТОТ — три картички                        ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("real_world")

        t6 = section_title("Каде материјалот одлучува сè.")
        self.play(Write(t6), run_time=0.9)

        def use_card(title, body, color, pos):
            box = RoundedRectangle(
                width=4.0, height=2.8, corner_radius=0.22,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            ).move_to(pos)
            tt = Text(title, font_size=24, color=color, weight=BOLD)
            tt.next_to(box.get_top(), DOWN, buff=0.2)
            bb = Text(body, font_size=20, color=WHITE2)
            bb.move_to(box.get_center() + DOWN*0.2)
            return VGroup(box, tt, bb)

        c1 = use_card("Шише за вода", "Пластика. Лесна. Не се крши.",
                      BLUE, LEFT*4.4 + DOWN*0.4)
        c2 = use_card("Тенџера", "Челик внатре. Пластика на дршка.",
                      ORANGE, DOWN*0.4)
        c3 = use_card("Прозорец", "Стакло. Пушта светлина — држи зима.",
                      YELLOW, RIGHT*4.4 + DOWN*0.4)

        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.play(FadeIn(c3), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t6, c1, c2, c3)))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни.")
        self.play(Write(t7), run_time=0.8)

        b1 = callout("Материјал = супстанца со карактер.",
                     width=11.0, border=BLUE, font_size=28)
        b1.move_to(UP*1.6)
        b2 = callout("Својства одлучуваат за намената.",
                     width=11.0, border=GREEN, font_size=28)
        b2.next_to(b1, DOWN, buff=0.35)
        b3 = callout("Метал, дрво, стакло, пластика — секој со улога.",
                     width=11.0, border=YELLOW, font_size=28)
        b3.next_to(b2, DOWN, buff=0.35)

        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.0)

        finisher = Text("Карактер.",
                        font_size=54, color=YELLOW, weight=BOLD)
        finisher.next_to(b3, DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, b1, b2, b3, finisher)))
        self.wait(0.5)
