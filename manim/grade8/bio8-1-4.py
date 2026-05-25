"""
bio8-1-4  —  Рецептори за светлина — окото
Биологија 8, Единица 1: Сетила и нервна координација

Teaching narrative — Andonovski-style: three-beat punches,
eye as camera, retina as canvas, brain as the final painter.
Render:  manim -ql bio8-1-4.py Bio814Scene
Output:  media/videos/bio8-1-4/480p15/Bio814Scene.mp4
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


class Bio814Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Окото гледа наопаку.",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.5)
        self.wait(0.4)

        beats = VGroup(
            Text("Мозокот ја превртува сликата.",
                 font_size=36, color=WHITE2),
            Text("Никогаш не знаеш.",
                 font_size=36, color=GREY),
            Text("Тоа е магија.",
                 font_size=36, color=PURPLE),
            Text("Тоа е биологија.",
                 font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — eye anatomy                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Делови на окото")
        self.play(Write(title), run_time=0.8)

        # eye cross-section
        # main eyeball
        eyeball = Circle(radius=2.0, fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=2.5)
        eyeball.shift(LEFT * 1.5 + DOWN * 0.3)

        # cornea (front bump on left)
        cornea = Arc(radius=0.7, start_angle=-PI / 2.5, angle=PI * 0.8,
                     color=BLUE, stroke_width=4)
        cornea.move_to(eyeball.get_left() + RIGHT * 0.1)

        # iris (ring) — vertical line at front
        iris_top = Line(eyeball.get_left() + RIGHT * 0.65 + UP * 0.25,
                        eyeball.get_left() + RIGHT * 0.65 + UP * 0.75,
                        color=ORANGE, stroke_width=5)
        iris_bot = Line(eyeball.get_left() + RIGHT * 0.65 + DOWN * 0.25,
                        eyeball.get_left() + RIGHT * 0.65 + DOWN * 0.75,
                        color=ORANGE, stroke_width=5)
        pupil_gap = Line(iris_top.get_bottom(), iris_bot.get_top(),
                         color=DARK_CARD, stroke_width=5)

        # lens (yellow ellipse just behind iris)
        lens = Ellipse(width=0.5, height=1.0,
                       fill_color=YELLOW, fill_opacity=0.7,
                       stroke_color=YELLOW, stroke_width=2)
        lens.move_to(eyeball.get_left() + RIGHT * 0.95)

        # retina (back inside curve)
        retina = Arc(radius=1.95, start_angle=-PI / 2, angle=PI,
                     color=RED, stroke_width=4)
        retina.move_to(eyeball.get_center())
        # rotate so it covers the right (back) half
        retina.rotate(PI, about_point=eyeball.get_center())

        # optic nerve (line from back)
        optic = Line(eyeball.get_right() + DOWN * 0.4,
                     eyeball.get_right() + RIGHT * 1.2 + DOWN * 0.6,
                     color=PURPLE, stroke_width=6)

        self.play(Create(eyeball), run_time=0.8)
        self.play(Create(cornea), run_time=0.6)
        self.play(Create(iris_top), Create(iris_bot), run_time=0.6)
        self.play(FadeIn(lens), run_time=0.6)
        self.play(Create(retina), run_time=0.7)
        self.play(Create(optic), run_time=0.6)

        # labels on right
        labels_data = [
            ("Рожница",    BLUE,   cornea.get_left() + LEFT * 0.3 + UP * 0.5),
            ("Ирис",       ORANGE, iris_top.get_left() + LEFT * 0.2 + UP * 0.3),
            ("Леќа",       YELLOW, lens.get_top() + UP * 0.3),
            ("Мрежница",   RED,    retina.get_right() + RIGHT * 0.2 + UP * 0.5),
            ("Оптички нерв", PURPLE, optic.get_right() + RIGHT * 0.4),
        ]
        labels = VGroup()
        for txt, col, pos in labels_data:
            l = Text(txt, font_size=20, color=col)
            l.move_to(pos)
            labels.add(l)

        # place labels in legible area (right column)
        legend = VGroup()
        legend_items = [
            ("Рожница",    BLUE),
            ("Ирис",       ORANGE),
            ("Леќа",       YELLOW),
            ("Мрежница",   RED),
            ("Оптички нерв", PURPLE),
        ]
        for txt, col in legend_items:
            box = RoundedRectangle(
                width=3.2, height=0.55, corner_radius=0.1,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            t = Text(txt, font_size=20, color=col, weight=BOLD).move_to(box)
            legend.add(VGroup(box, t))
        legend.arrange(DOWN, buff=0.15).move_to(RIGHT * 4.5 + DOWN * 0.3)

        for item in legend:
            self.play(FadeIn(item, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, eyeball, cornea, iris_top, iris_bot, lens, retina, optic, legend,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — rods vs cones                       ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Два типа рецептори")
        self.play(Write(title), run_time=0.8)

        # Left card — rods
        rods_card = RoundedRectangle(
            width=5.8, height=4.5, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREY, stroke_width=2.5,
        ).shift(LEFT * 3.3 + DOWN * 0.3)
        rods_title = Text("Стапчиња", font_size=30, color=GREY, weight=BOLD)
        rods_title.move_to(rods_card.get_top() + DOWN * 0.4)

        rods_lines = VGroup(
            Text("120 милиони", font_size=24, color=WHITE2),
            Text("Слаба светлина", font_size=24, color=WHITE2),
            Text("Без бои", font_size=24, color=WHITE2),
            Text("Ноќно гледање", font_size=24, color=WHITE2),
        ).arrange(DOWN, buff=0.3)
        rods_lines.move_to(rods_card.get_center() + DOWN * 0.1)

        # tiny rod shape
        rod_shape = Rectangle(width=0.2, height=0.8,
                              fill_color=GREY, fill_opacity=1,
                              stroke_width=0)
        rod_shape.move_to(rods_card.get_bottom() + UP * 0.5)

        # Right card — cones
        cones_card = RoundedRectangle(
            width=5.8, height=4.5, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2.5,
        ).shift(RIGHT * 3.3 + DOWN * 0.3)
        cones_title = Text("Чунки", font_size=30, color=YELLOW, weight=BOLD)
        cones_title.move_to(cones_card.get_top() + DOWN * 0.4)

        cones_lines = VGroup(
            Text("6-7 милиони", font_size=24, color=WHITE2),
            Text("Силна светлина", font_size=24, color=WHITE2),
            Text("Разликуваат бои", font_size=24, color=WHITE2),
            Text("Дневно гледање", font_size=24, color=WHITE2),
        ).arrange(DOWN, buff=0.3)
        cones_lines.move_to(cones_card.get_center() + DOWN * 0.1)

        # three colored cone shapes
        cone_shapes = VGroup()
        for i, col in enumerate([RED, GREEN, BLUE]):
            c = Polygon(
                [-0.1, 0.0, 0], [0.1, 0.0, 0], [0.0, 0.6, 0],
                fill_color=col, fill_opacity=1, stroke_width=0,
            )
            c.shift(RIGHT * (i * 0.4 - 0.4))
            cone_shapes.add(c)
        cone_shapes.move_to(cones_card.get_bottom() + UP * 0.5)

        self.play(Create(rods_card), Write(rods_title), run_time=0.8)
        for line in rods_lines:
            self.play(FadeIn(line, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(rod_shape), run_time=0.4)
        self.wait(0.5)

        self.play(Create(cones_card), Write(cones_title), run_time=0.8)
        for line in cones_lines:
            self.play(FadeIn(line, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(cone_shapes), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, rods_card, rods_title, rods_lines, rod_shape,
            cones_card, cones_title, cones_lines, cone_shapes,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — inverted image                        ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Сликата паѓа наопаку")
        self.play(Write(title), run_time=0.8)

        # arrow object on left (the tree)
        tree_trunk = Rectangle(width=0.25, height=1.2,
                               fill_color="#5d4037", fill_opacity=1,
                               stroke_width=0)
        tree_top = Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0)
        tree_top.scale(0.7)
        tree_top.next_to(tree_trunk, UP, buff=-0.15)
        tree = VGroup(tree_trunk, tree_top)
        tree.shift(LEFT * 5.0)
        tree_label = Text("Предмет", font_size=22, color=GREEN)
        tree_label.next_to(tree, DOWN, buff=0.2)

        # simplified eye
        eye2 = Circle(radius=1.2, color=WHITE2, stroke_width=2.5)
        lens2 = Ellipse(width=0.35, height=0.8, fill_color=YELLOW, fill_opacity=0.7,
                        stroke_color=YELLOW, stroke_width=2)
        lens2.move_to(eye2.get_left() + RIGHT * 0.4)
        retina2 = Arc(radius=1.18, start_angle=PI / 2, angle=PI,
                      color=RED, stroke_width=3)
        retina2.move_to(eye2.get_center())

        eye_group = VGroup(eye2, lens2, retina2).shift(DOWN * 0.0)

        # inverted image on retina (small upside-down tree)
        inv_trunk = Rectangle(width=0.12, height=0.4,
                              fill_color="#5d4037", fill_opacity=1,
                              stroke_width=0)
        inv_top = Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0)
        inv_top.scale(0.25)
        inv_top.next_to(inv_trunk, DOWN, buff=-0.05)  # upside down
        inv_tree = VGroup(inv_trunk, inv_top)
        inv_tree.move_to(eye2.get_right() + LEFT * 0.4)

        # light rays
        ray_top = Line(tree.get_top(), inv_tree.get_bottom(),
                       color=YELLOW, stroke_width=2)
        ray_bot = Line(tree.get_bottom(), inv_tree.get_top(),
                       color=YELLOW, stroke_width=2)

        self.play(FadeIn(tree), FadeIn(tree_label), run_time=0.7)
        self.play(Create(eye_group), run_time=0.9)
        self.play(Create(ray_top), Create(ray_bot), run_time=1.0)
        self.play(FadeIn(inv_tree), run_time=0.5)
        self.wait(0.6)

        # arrow to brain
        brain_box = callout("Мозок: ја превртува!",
                            width=4.5, border=PURPLE, font_size=24)
        brain_box.move_to(RIGHT * 4.7 + UP * 0.2)
        arr_brain = Arrow(eye2.get_right(), brain_box.get_left(),
                          buff=0.15, color=PURPLE, stroke_width=4)
        self.play(GrowArrow(arr_brain), FadeIn(brain_box), run_time=0.9)
        self.wait(0.4)

        # final upright tree (what we see)
        right_tree = tree.copy()
        right_tree.scale(0.7)
        right_tree.move_to(brain_box.get_center() + DOWN * 1.7)
        rt_label = Text("Што гледаш", font_size=20, color=GREEN)
        rt_label.next_to(right_tree, DOWN, buff=0.2)
        self.play(FadeIn(right_tree), FadeIn(rt_label), run_time=0.7)
        self.wait(1.3)

        self.play(FadeOut(VGroup(
            title, tree, tree_label, eye_group, ray_top, ray_bot, inv_tree,
            brain_box, arr_brain, right_tree, rt_label,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — pupil reflex                       ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("Зеницата се прилагодува")
        self.play(Write(title), run_time=0.8)

        # bright light eye (small pupil)
        bright_eye = Circle(radius=1.0, color=ORANGE, stroke_width=3,
                            fill_color=WHITE2, fill_opacity=0.15)
        bright_pupil = Dot(point=bright_eye.get_center(), radius=0.2,
                           color="#0d1b2e")
        bright_label = Text("Силна светлина", font_size=22, color=ORANGE)
        bright_label.next_to(bright_eye, DOWN, buff=0.4)
        bright_subl = Text("Зеница мала", font_size=20, color=WHITE2)
        bright_subl.next_to(bright_label, DOWN, buff=0.15)
        bright_grp = VGroup(bright_eye, bright_pupil, bright_label, bright_subl)
        bright_grp.shift(LEFT * 3.5 + DOWN * 0.2)

        # dark eye (large pupil)
        dark_eye = Circle(radius=1.0, color=BLUE, stroke_width=3,
                          fill_color=DARK_CARD, fill_opacity=0.5)
        dark_pupil = Dot(point=dark_eye.get_center(), radius=0.6,
                         color="#0d1b2e")
        dark_label = Text("Слаба светлина", font_size=22, color=BLUE)
        dark_label.next_to(dark_eye, DOWN, buff=0.4)
        dark_subl = Text("Зеница голема", font_size=20, color=WHITE2)
        dark_subl.next_to(dark_label, DOWN, buff=0.15)
        dark_grp = VGroup(dark_eye, dark_pupil, dark_label, dark_subl)
        dark_grp.shift(RIGHT * 3.5 + DOWN * 0.2)

        self.play(FadeIn(bright_grp, shift=RIGHT * 0.2), run_time=0.9)
        self.play(FadeIn(dark_grp, shift=LEFT * 0.2), run_time=0.9)
        self.wait(0.6)

        # animate transition
        self.play(
            bright_pupil.animate.scale(3.0),
            dark_pupil.animate.scale(1 / 3),
            run_time=1.0,
        )
        self.wait(0.4)
        self.play(
            bright_pupil.animate.scale(1 / 3),
            dark_pupil.animate.scale(3.0),
            run_time=1.0,
        )

        concl = Text("Автоматски. Никогаш не размислуваш.",
                     font_size=28, color=GREEN, weight=BOLD)
        concl.to_edge(DOWN, buff=0.5)
        self.play(Write(concl), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, bright_grp, dark_grp, concl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Леќа фокусира. Мрежница прима.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Стапчиња: ноќ. Чунки: бои.",
                 font_size=30, color=BLUE, weight=BOLD),
            Text("Сликата паѓа наопаку.",
                 font_size=28, color=ORANGE),
            Text("Мозокот ја превртува. Секогаш.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
