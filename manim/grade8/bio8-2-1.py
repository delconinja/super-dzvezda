"""
bio8-2-1  —  Скелетен систем
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
body as movement story, bones as living architecture.
Render:  manim -ql bio8-2-1.py Bio821Scene
Output:  media/videos/bio8-2-1/480p15/Bio821Scene.mp4
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


def function_card(icon, name, desc, color, pos):
    box = RoundedRectangle(
        width=3.0, height=1.7, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    ic = Text(icon, font_size=30, color=color, weight=BOLD)
    ic.move_to(box.get_center() + UP * 0.45)
    nm = Text(name, font_size=20, color=WHITE2, weight=BOLD)
    nm.move_to(box.get_center())
    dc = Text(desc, font_size=14, color=GREY)
    dc.move_to(box.get_center() + DOWN * 0.45)
    return VGroup(box, ic, nm, dc)


class Bio821Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("206 коски.", font_size=54, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Цврста архитектура.", font_size=38, color=WHITE2),
            Text("Не статуа.", font_size=38, color=GREY),
            Text("Жива градба.", font_size=38, color=GREEN),
            Text("Расте, се поправа, се менува.", font_size=34, color=BLUE),
        ).arrange(DOWN, buff=0.4).next_to(h1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  СКЕЛЕТНА СИЛУЕТА                                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("skeleton")
        title = section_title("Скелет — главните коски")
        self.play(Write(title), run_time=0.8)

        # Skull
        skull = Circle(radius=0.45, color=WHITE2, fill_opacity=0.15, stroke_width=2)
        skull.move_to(UP * 2.8 + LEFT * 0.3)

        # Spine — column of small rectangles
        spine = VGroup()
        for i in range(7):
            v = Rectangle(width=0.35, height=0.18, color=WHITE2,
                          fill_opacity=0.2, stroke_width=1.5)
            v.move_to(UP * (2.0 - i * 0.28) + LEFT * 0.3)
            spine.add(v)

        # Ribs — curved arcs around chest
        ribs = VGroup()
        for i in range(5):
            y = 1.6 - i * 0.22
            left = Arc(radius=1.0, start_angle=PI / 2, angle=PI / 2,
                       color=WHITE2, stroke_width=2)
            left.move_to(UP * y + LEFT * 0.95)
            right = Arc(radius=1.0, start_angle=0, angle=PI / 2,
                        color=WHITE2, stroke_width=2)
            right.move_to(UP * y + LEFT * 0.35 + RIGHT * 0.6)
            ribs.add(left, right)

        # Sternum
        sternum = Rectangle(width=0.18, height=1.1, color=WHITE2,
                            fill_opacity=0.3, stroke_width=1.5)
        sternum.move_to(UP * 1.15 + LEFT * 0.3)

        # Arms
        l_arm_upper = Line(LEFT * 1.3 + UP * 1.7, LEFT * 1.9 + UP * 0.2,
                           color=WHITE2, stroke_width=4)
        l_arm_lower = Line(LEFT * 1.9 + UP * 0.2, LEFT * 2.1 + DOWN * 1.2,
                           color=WHITE2, stroke_width=4)
        r_arm_upper = Line(RIGHT * 0.7 + UP * 1.7, RIGHT * 1.3 + UP * 0.2,
                           color=WHITE2, stroke_width=4)
        r_arm_lower = Line(RIGHT * 1.3 + UP * 0.2, RIGHT * 1.5 + DOWN * 1.2,
                           color=WHITE2, stroke_width=4)

        # Pelvis
        pelvis = Ellipse(width=1.8, height=0.7, color=WHITE2,
                         fill_opacity=0.2, stroke_width=2)
        pelvis.move_to(DOWN * 0.4 + LEFT * 0.3)

        # Legs
        l_femur = Line(DOWN * 0.6 + LEFT * 0.9, DOWN * 2.2 + LEFT * 0.9,
                       color=WHITE2, stroke_width=4)
        l_tibia = Line(DOWN * 2.2 + LEFT * 0.9, DOWN * 3.4 + LEFT * 1.0,
                       color=WHITE2, stroke_width=4)
        r_femur = Line(DOWN * 0.6 + RIGHT * 0.3, DOWN * 2.2 + RIGHT * 0.3,
                       color=WHITE2, stroke_width=4)
        r_tibia = Line(DOWN * 2.2 + RIGHT * 0.3, DOWN * 3.4 + RIGHT * 0.4,
                       color=WHITE2, stroke_width=4)

        skeleton = VGroup(skull, spine, ribs, sternum,
                          l_arm_upper, l_arm_lower, r_arm_upper, r_arm_lower,
                          pelvis, l_femur, l_tibia, r_femur, r_tibia)
        skeleton.scale(0.85).shift(LEFT * 2.5 + DOWN * 0.2)

        self.play(Create(skeleton), run_time=2.5)
        self.wait(0.4)

        # Labels
        labels = [
            ("Череп", skull, RIGHT * 0.6),
            ("Кичма", spine[3], RIGHT * 0.7),
            ("Ребра", ribs[2], RIGHT * 0.7),
            ("Граден кош", sternum, RIGHT * 0.5 + DOWN * 0.1),
            ("Карлица", pelvis, RIGHT * 0.7),
            ("Бутна коска", l_femur, LEFT * 0.6),
            ("Голен", l_tibia, LEFT * 0.5),
        ]
        label_group = VGroup()
        for txt, target, offset in labels:
            t = Text(txt, font_size=18, color=YELLOW)
            t.next_to(target, RIGHT, buff=0.3)
            t.shift(offset * 0.0)
            dot = Dot(target.get_center(), radius=0.05, color=YELLOW)
            label_group.add(dot, t)

        # Place labels manually on the right side
        right_labels = VGroup(
            Text("Череп", font_size=20, color=YELLOW),
            Text("Кичма", font_size=20, color=YELLOW),
            Text("Ребра", font_size=20, color=YELLOW),
            Text("Граден кош", font_size=20, color=YELLOW),
            Text("Раце", font_size=20, color=YELLOW),
            Text("Карлица", font_size=20, color=YELLOW),
            Text("Нозе", font_size=20, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        right_labels.to_edge(RIGHT, buff=1.5).shift(UP * 0.3)

        for lbl in right_labels:
            self.play(FadeIn(lbl, shift=LEFT * 0.2), run_time=0.35)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, skeleton, right_labels)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ФУНКЦИИ                                         ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("functions")
        title = section_title("Пет функции на скелетот")
        self.play(Write(title), run_time=0.8)

        f1 = function_card("П", "Потпора", "држи го телото", BLUE, UP * 1.5 + LEFT * 4.2)
        f2 = function_card("З", "Заштита", "мозок, срце, бели дробови", RED, UP * 1.5 + LEFT * 0.9)
        f3 = function_card("Д", "Движење", "место за мускули", GREEN, UP * 1.5 + RIGHT * 2.4)
        f4 = function_card("К", "Крвни клетки", "црвена коскена срцевина", ORANGE, DOWN * 0.7 + LEFT * 2.5)
        f5 = function_card("М", "Минерали", "калциум и фосфор", PURPLE, DOWN * 0.7 + RIGHT * 1.0)

        for card in (f1, f2, f3, f4, f5):
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.55)
            self.wait(0.2)

        self.wait(1.2)

        punch = callout("Една градба. Пет работи.", width=8.5,
                        bg="#1a3552", border=YELLOW, font_size=32)
        punch.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(punch, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, f1, f2, f3, f4, f5, punch)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  АКСИЈАЛЕН vs АПЕНДИКУЛАРЕН                      ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("axial_appendicular")
        title = section_title("Два дела на скелетот")
        self.play(Write(title), run_time=0.8)

        # Left: axial (skull + spine + ribs highlighted)
        axial_label = Text("Аксијален", font_size=32, color=BLUE, weight=BOLD)
        axial_label.move_to(UP * 2.2 + LEFT * 3.5)
        axial_count = Text("80 коски", font_size=22, color=WHITE2)
        axial_count.next_to(axial_label, DOWN, buff=0.15)

        axial_items = VGroup(
            Text("• Череп", font_size=20, color=WHITE2),
            Text("• Кичма", font_size=20, color=WHITE2),
            Text("• Ребра", font_size=20, color=WHITE2),
            Text("• Граден кош", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        axial_items.next_to(axial_count, DOWN, buff=0.5)
        axial_items.align_to(axial_label, LEFT)

        # Right: appendicular (arms + legs)
        app_label = Text("Апендикуларен", font_size=32, color=ORANGE, weight=BOLD)
        app_label.move_to(UP * 2.2 + RIGHT * 3.0)
        app_count = Text("126 коски", font_size=22, color=WHITE2)
        app_count.next_to(app_label, DOWN, buff=0.15)

        app_items = VGroup(
            Text("• Раце", font_size=20, color=WHITE2),
            Text("• Нозе", font_size=20, color=WHITE2),
            Text("• Рамен појас", font_size=20, color=WHITE2),
            Text("• Карличен појас", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        app_items.next_to(app_count, DOWN, buff=0.5)
        app_items.align_to(app_label, LEFT)

        # Divider
        div = DashedLine(UP * 2.5, DOWN * 2.5, color=GREY, stroke_width=2)

        self.play(Create(div), run_time=0.6)
        self.play(FadeIn(axial_label), FadeIn(app_label), run_time=0.6)
        self.play(FadeIn(axial_count), FadeIn(app_count), run_time=0.5)
        self.wait(0.3)

        for ai, app in zip(axial_items, app_items):
            self.play(FadeIn(ai, shift=RIGHT * 0.15),
                      FadeIn(app, shift=LEFT * 0.15), run_time=0.5)

        self.wait(0.4)

        total = Text("80 + 126 = 206", font_size=34, color=YELLOW, weight=BOLD)
        total.to_edge(DOWN, buff=0.8)
        self.play(Write(total), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, div, axial_label, app_label,
                                 axial_count, app_count, axial_items,
                                 app_items, total)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ЖИВА ГРАДБА                                     ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("living_bone")
        title = section_title("Коската е жива")
        self.play(Write(title), run_time=0.8)

        # Bone shape
        bone = RoundedRectangle(width=4.5, height=1.0, corner_radius=0.5,
                                fill_color=WHITE2, fill_opacity=0.25,
                                stroke_color=WHITE2, stroke_width=2)
        bone.move_to(UP * 0.5)
        end1 = Circle(radius=0.5, color=WHITE2, fill_opacity=0.25, stroke_width=2)
        end1.move_to(UP * 0.5 + LEFT * 2.0)
        end2 = Circle(radius=0.5, color=WHITE2, fill_opacity=0.25, stroke_width=2)
        end2.move_to(UP * 0.5 + RIGHT * 2.0)
        bone_full = VGroup(bone, end1, end2)
        self.play(Create(bone_full), run_time=1.0)
        self.wait(0.3)

        beats = VGroup(
            Text("Расте.", font_size=34, color=GREEN, weight=BOLD),
            Text("Се поправа кога ќе се скрши.", font_size=28, color=BLUE),
            Text("Се обновува секој ден.", font_size=28, color=ORANGE),
            Text("Складира калциум.", font_size=28, color=PURPLE),
            Text("Прави крвни клетки.", font_size=28, color=RED),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=0.8)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, bone_full, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ОБОБЕНИ КОСКИ                                   ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("special_bones")
        title = section_title("Интересно — три факти")
        self.play(Write(title), run_time=0.8)

        facts = VGroup(
            callout("Најмала коска: ушна коскичка — 3 мм",
                    width=10.5, bg="#1a3552", border=BLUE, font_size=26),
            callout("Најголема коска: бутна — 45 см",
                    width=10.5, bg="#1a3552", border=GREEN, font_size=26),
            callout("Бебе има 270 коски — некои се спојуваат",
                    width=10.5, bg="#1a3552", border=ORANGE, font_size=26),
        ).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        for f in facts:
            self.play(FadeIn(f, shift=UP * 0.2), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, facts)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Скелетот држи.", font_size=42, color=BLUE, weight=BOLD),
            Text("Скелетот штити.", font_size=42, color=RED, weight=BOLD),
            Text("Скелетот движи.", font_size=42, color=GREEN, weight=BOLD),
            Text("Скелетот живее.", font_size=46, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
