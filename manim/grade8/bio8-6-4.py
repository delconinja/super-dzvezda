"""
bio8-6-4  —  Растенија — главни групи
Биологија 8, Единица 6: Класификација

Teaching narrative — Andonovski-style: from moss to flower,
the plant kingdom climbs through complexity.
Render:  manim -ql bio8-6-4.py Bio864Scene
Output:  media/videos/bio8-6-4/480p15/Bio864Scene.mp4
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


class Bio864Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — four stages                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Мовот тивко покрива камења.",
                     font_size=34, color=GREEN, weight=BOLD)
        hook2 = Text("Папратот собира спори.",
                     font_size=34, color=BLUE, weight=BOLD)
        hook3 = Text("Борот крие семе.",
                     font_size=34, color=ORANGE, weight=BOLD)
        hook4 = Text("Цветот ја прави целата приказна видлива.",
                     font_size=32, color=PURPLE, weight=BOLD)

        beats = VGroup(hook1, hook2, hook3, hook4).arrange(DOWN, buff=0.5)
        beats.to_edge(UP, buff=0.8)

        for line in beats:
            self.play(Write(line), run_time=1.0)
            self.wait(0.3)
        self.wait(1.5)

        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  KINGDOM PLANTAE — overview                      ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("overview")

        title = section_title("Царство — Растенија")
        self.play(Write(title), run_time=0.8)

        big_num = Text("≈ 400.000", font_size=70, color=YELLOW, weight=BOLD)
        big_num.shift(UP * 0.5)
        species_lbl = Text("познати видови",
                           font_size=30, color=WHITE2)
        species_lbl.next_to(big_num, DOWN, buff=0.3)

        self.play(Write(big_num), run_time=1.2)
        self.play(FadeIn(species_lbl), run_time=0.6)
        self.wait(0.8)

        info = callout("Сите вршат фотосинтеза. Сите имаат клеточен ѕид од целулоза.",
                       width=12.0, border=GREEN, font_size=24)
        info.next_to(species_lbl, DOWN, buff=0.6)
        self.play(FadeIn(info), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, big_num, species_lbl, info)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MOSSES — simplest                                ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mosses")

        title2 = section_title("Мовови", color=GREEN)
        self.play(Write(title2), run_time=0.8)

        # Moss illustration — small tufts
        rock = Polygon(
            np.array([-2.2, -0.7, 0]),
            np.array([2.2, -0.7, 0]),
            np.array([1.8, 0.1, 0]),
            np.array([-1.8, 0.1, 0]),
            color=GREY, fill_color=GREY, fill_opacity=0.6, stroke_width=2,
        )
        tufts = VGroup()
        for x in np.linspace(-1.6, 1.6, 7):
            tuft = VGroup()
            for j in range(4):
                stem = Line(
                    np.array([x + (j - 1.5) * 0.08, 0.1, 0]),
                    np.array([x + (j - 1.5) * 0.08 + 0.04, 0.55 + j * 0.05, 0]),
                    color=GREEN, stroke_width=3,
                )
                tuft.add(stem)
            tufts.add(tuft)
        moss = VGroup(rock, tufts).shift(LEFT * 3.5 + DOWN * 0.6)

        self.play(Create(rock), run_time=0.7)
        self.play(Create(tufts), run_time=1.2)
        self.wait(0.3)

        features = VGroup(
            Text("• Без спроводни садови", font_size=23, color=RED),
            Text("• Без семе — се множат со спори", font_size=23, color=ORANGE),
            Text("• Многу мали (1–10 см)", font_size=23, color=YELLOW),
            Text("• Живеат во влажни места", font_size=23, color=BLUE),
            Text("Најпримитивни копнени растенија.",
                 font_size=22, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features.next_to(moss, RIGHT, buff=0.7)

        for f in features:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, moss, features)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  FERNS                                            ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ferns")

        title3 = section_title("Папрати", color=BLUE)
        self.play(Write(title3), run_time=0.8)

        # Fern frond — central stem with side leaflets
        stem = Line(np.array([0, -1.5, 0]), np.array([0, 1.5, 0]),
                    color=GREEN, stroke_width=5)
        leaflets = VGroup()
        for y in np.linspace(-1.3, 1.3, 9):
            length = 1.2 - abs(y) * 0.4
            l_left = Line(np.array([0, y, 0]),
                          np.array([-length, y + 0.1, 0]),
                          color=GREEN, stroke_width=4)
            l_right = Line(np.array([0, y, 0]),
                           np.array([length, y + 0.1, 0]),
                           color=GREEN, stroke_width=4)
            leaflets.add(l_left, l_right)
        fern = VGroup(stem, leaflets).shift(LEFT * 3.5)

        self.play(Create(stem), run_time=0.7)
        self.play(Create(leaflets), run_time=1.4)
        self.wait(0.3)

        features3 = VGroup(
            Text("• Имаат спроводни садови", font_size=23, color=GREEN),
            Text("• Сè уште без семе — со спори", font_size=23, color=ORANGE),
            Text("• Може да достигнат поголеми висини", font_size=23, color=YELLOW),
            Text("• Сакаат сенка и влага", font_size=23, color=BLUE),
            Text("Чекор напред од мововите.",
                 font_size=22, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features3.next_to(fern, RIGHT, buff=0.7)

        for f in features3:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, fern, features3)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  GYMNOSPERMS — naked seeds                        ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("gymnosperms")

        title4 = section_title("Голосемени", color=ORANGE)
        self.play(Write(title4), run_time=0.8)

        # Pine tree silhouette
        trunk = Rectangle(width=0.35, height=1.2, color=ORANGE,
                          fill_color=ORANGE, fill_opacity=0.85, stroke_width=2)
        trunk.shift(DOWN * 1.3)
        triangles = VGroup()
        for i in range(3):
            tri = Polygon(
                np.array([-1.0 + i * 0.1, -0.5 + i * 0.6, 0]),
                np.array([1.0 - i * 0.1, -0.5 + i * 0.6, 0]),
                np.array([0, 0.5 + i * 0.6, 0]),
                color=GREEN, fill_color=GREEN, fill_opacity=0.75, stroke_width=2,
            )
            triangles.add(tri)
        pine_cone = Ellipse(width=0.35, height=0.5, color=ORANGE,
                            fill_color=ORANGE, fill_opacity=0.9, stroke_width=2)
        pine_cone.shift(RIGHT * 0.6 + DOWN * 0.3)
        pine = VGroup(trunk, triangles, pine_cone).shift(LEFT * 3.5)

        self.play(Create(trunk), run_time=0.5)
        self.play(Create(triangles), run_time=1.0)
        self.play(FadeIn(pine_cone), run_time=0.5)
        self.wait(0.3)

        features4 = VGroup(
            Text("• Имаат семе — но не во плод", font_size=23, color=ORANGE, weight=BOLD),
            Text("• Семето е во шишарка ('голо')", font_size=23, color=YELLOW),
            Text("• Без цветови", font_size=23, color=RED),
            Text("• Зимзелени, тивки, силни", font_size=23, color=GREEN),
            Text("Пр.: бор, ела, смрча, кедар",
                 font_size=22, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features4.next_to(pine, RIGHT, buff=0.7)

        for f in features4:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, pine, features4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ANGIOSPERMS — flowering plants                   ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("angiosperms")

        title5 = section_title("Скриеносемени", color=PURPLE)
        self.play(Write(title5), run_time=0.8)

        sub5 = Text("Растенија со цветови и плодови",
                    font_size=26, color=WHITE2)
        sub5.next_to(title5, DOWN, buff=0.25)
        self.play(FadeIn(sub5), run_time=0.6)

        # Flower
        petals = VGroup()
        for k in range(6):
            angle = k * PI / 3
            petal = Ellipse(width=0.5, height=1.1, color=PURPLE,
                            fill_color=PURPLE, fill_opacity=0.75, stroke_width=2)
            petal.rotate(angle)
            petal.shift(np.array([np.cos(angle + PI/2) * 0.55,
                                   np.sin(angle + PI/2) * 0.55, 0]))
            petals.add(petal)
        center_flower = Circle(radius=0.35, color=YELLOW,
                               fill_color=YELLOW, fill_opacity=1, stroke_width=2)
        flower_stem = Line(np.array([0, -0.5, 0]), np.array([0, -2.0, 0]),
                           color=GREEN, stroke_width=4)
        leaf_l = Ellipse(width=0.8, height=0.35, color=GREEN,
                         fill_color=GREEN, fill_opacity=0.7)
        leaf_l.rotate(0.4).shift(np.array([-0.4, -1.3, 0]))
        leaf_r = Ellipse(width=0.8, height=0.35, color=GREEN,
                         fill_color=GREEN, fill_opacity=0.7)
        leaf_r.rotate(-0.4).shift(np.array([0.4, -1.5, 0]))
        flower = VGroup(flower_stem, leaf_l, leaf_r, petals, center_flower)
        flower.shift(LEFT * 3.5 + UP * 0.3)

        self.play(Create(flower_stem), run_time=0.5)
        self.play(Create(leaf_l), Create(leaf_r), run_time=0.5)
        self.play(FadeIn(petals, scale=0.5), run_time=1.0)
        self.play(FadeIn(center_flower), run_time=0.4)
        self.wait(0.3)

        features5 = VGroup(
            Text("• Цветовите — фабрика за семе", font_size=22, color=PURPLE),
            Text("• Семето во плод — заштитено", font_size=22, color=ORANGE, weight=BOLD),
            Text("• Привлекуваат опрашувачи", font_size=22, color=YELLOW),
            Text("• Најбројна група — ~90% од растенијата", font_size=22, color=GREEN, weight=BOLD),
            Text("Пр.: јаболко, пченица, роза, даб", font_size=22, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        features5.next_to(flower, RIGHT, buff=0.6)

        for f in features5:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title5, sub5, flower, features5)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY LADDER + CLOSE                           ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ladder")

        title6 = section_title("Од едноставно — до сложено", color=YELLOW)
        self.play(Write(title6), run_time=0.8)

        ladder = [
            ("Мовови",        "без садови, спори",       GREEN),
            ("Папрати",       "садови, спори",            BLUE),
            ("Голосемени",    "семе во шишарка",          ORANGE),
            ("Скриеносемени", "цвет, плод, семе",         PURPLE),
        ]

        steps = VGroup()
        for i, (name, desc, color) in enumerate(ladder):
            step = RoundedRectangle(
                width=9.0, height=0.85, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            n = Text(name, font_size=26, color=color, weight=BOLD)
            arrow = Text("→", font_size=26, color=WHITE2)
            d = Text(desc, font_size=22, color=WHITE2)
            content = VGroup(n, arrow, d).arrange(RIGHT, buff=0.4)
            content.move_to(step)
            steps.add(VGroup(step, content))

        steps.arrange(DOWN, buff=0.25).next_to(title6, DOWN, buff=0.5)

        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.55)
            self.wait(0.18)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title6, steps)), run_time=0.7)

        # CLOSE
        close1 = Text("Од спора —",
                      font_size=42, color=GREEN, weight=BOLD)
        close2 = Text("до цвет.",
                      font_size=46, color=PURPLE, weight=BOLD)
        close3 = Text("Растението не молчи —",
                      font_size=36, color=YELLOW)
        close4 = Text("расте.",
                      font_size=72, color=ORANGE, weight=BOLD)
        cg = VGroup(close1, close2, close3, close4).arrange(DOWN, buff=0.5)

        for line in cg:
            self.play(Write(line), run_time=0.9)
            self.wait(0.35)
        self.wait(2.0)

        self.play(FadeOut(cg), run_time=1.0)
        self.wait(0.5)
