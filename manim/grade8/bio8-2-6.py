"""
bio8-2-6  —  Движење — координација на скелет и мускули
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
movement as collaboration, levers as engineering of body.
Render:  manim -ql bio8-2-6.py Bio826Scene
Output:  media/videos/bio8-2-6/480p15/Bio826Scene.mp4
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


class Bio826Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Скелетот држи.", font_size=44, color=BLUE, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.0)
        self.wait(0.25)

        h2 = Text("Мускулот влече.", font_size=44, color=RED, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.35)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.25)

        h3 = Text("Нервот командува.", font_size=44, color=PURPLE, weight=BOLD)
        h3.next_to(h2, DOWN, buff=0.35)
        self.play(Write(h3), run_time=1.0)
        self.wait(0.3)

        beats = VGroup(
            Text("Тројката се движи.", font_size=36, color=WHITE2),
            Text("Заедно.", font_size=36, color=GREEN, weight=BOLD),
            Text("Никогаш сами.", font_size=38, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.25).next_to(h3, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.65)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, h2, h3, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ТРОЈНА СОРАБОТКА                                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("trio")
        title = section_title("Тројката на движењето")
        self.play(Write(title), run_time=0.8)

        # Three role cards
        bone_card = RoundedRectangle(width=3.4, height=2.5, corner_radius=0.25,
                                     fill_color=DARK_CARD, fill_opacity=1,
                                     stroke_color=BLUE, stroke_width=3)
        bone_card.move_to(LEFT * 4.2)
        bone_t = Text("Коска", font_size=28, color=BLUE, weight=BOLD)
        bone_t.move_to(bone_card.get_top() + DOWN * 0.4)
        bone_role = Text("Полуга", font_size=22, color=YELLOW)
        bone_role.move_to(bone_card.get_center() + UP * 0.1)
        bone_desc = Text("(пренесува сила)", font_size=16, color=GREY)
        bone_desc.move_to(bone_card.get_center() + DOWN * 0.4)

        joint_card = RoundedRectangle(width=3.4, height=2.5, corner_radius=0.25,
                                      fill_color=DARK_CARD, fill_opacity=1,
                                      stroke_color=ORANGE, stroke_width=3)
        joint_card.move_to(ORIGIN)
        joint_t = Text("Зглоб", font_size=28, color=ORANGE, weight=BOLD)
        joint_t.move_to(joint_card.get_top() + DOWN * 0.4)
        joint_role = Text("Потпорна точка", font_size=22, color=YELLOW)
        joint_role.move_to(joint_card.get_center() + UP * 0.1)
        joint_desc = Text("(околу која се ротира)", font_size=16, color=GREY)
        joint_desc.move_to(joint_card.get_center() + DOWN * 0.4)

        muscle_card = RoundedRectangle(width=3.4, height=2.5, corner_radius=0.25,
                                       fill_color=DARK_CARD, fill_opacity=1,
                                       stroke_color=RED, stroke_width=3)
        muscle_card.move_to(RIGHT * 4.2)
        muscle_t = Text("Мускул", font_size=28, color=RED, weight=BOLD)
        muscle_t.move_to(muscle_card.get_top() + DOWN * 0.4)
        muscle_role = Text("Сила", font_size=22, color=YELLOW)
        muscle_role.move_to(muscle_card.get_center() + UP * 0.1)
        muscle_desc = Text("(влече коска)", font_size=16, color=GREY)
        muscle_desc.move_to(muscle_card.get_center() + DOWN * 0.4)

        for card, t, r, d in [(bone_card, bone_t, bone_role, bone_desc),
                              (joint_card, joint_t, joint_role, joint_desc),
                              (muscle_card, muscle_t, muscle_role, muscle_desc)]:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.55)
            self.play(Write(t), run_time=0.45)
            self.play(FadeIn(r), FadeIn(d), run_time=0.5)
            self.wait(0.2)

        # Plus signs between
        plus1 = Text("+", font_size=44, color=YELLOW, weight=BOLD)
        plus1.move_to(LEFT * 2.1)
        plus2 = Text("+", font_size=44, color=YELLOW, weight=BOLD)
        plus2.move_to(RIGHT * 2.1)

        self.play(Write(plus1), Write(plus2), run_time=0.6)

        result = Text("= Движење", font_size=34, color=GREEN, weight=BOLD)
        result.to_edge(DOWN, buff=0.7)
        self.play(Write(result), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, bone_card, joint_card, muscle_card,
                                 bone_t, joint_t, muscle_t,
                                 bone_role, joint_role, muscle_role,
                                 bone_desc, joint_desc, muscle_desc,
                                 plus1, plus2, result)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ШТО Е ПОЛУГА                                    ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("lever_basics")
        title = section_title("Што е полуга?")
        self.play(Write(title), run_time=0.8)

        # Triangle pivot + bar
        pivot = Polygon([-0.4, -0.5, 0], [0.4, -0.5, 0], [0, 0.05, 0],
                        color=ORANGE, fill_opacity=0.7, stroke_color=ORANGE,
                        stroke_width=2)
        bar = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE2, stroke_width=6)
        bar.shift(UP * 0.05)

        # Force arrow (down on right side)
        force_arr = Arrow(RIGHT * 2.5 + UP * 1.2, RIGHT * 2.5 + UP * 0.15,
                          color=RED, stroke_width=4, buff=0.05)
        force_lbl = Text("Сила (F)", font_size=20, color=RED, weight=BOLD)
        force_lbl.next_to(force_arr, UP, buff=0.1)

        # Load arrow (down on left side)
        load_arr = Arrow(LEFT * 2.5 + UP * 1.2, LEFT * 2.5 + UP * 0.15,
                         color=BLUE, stroke_width=4, buff=0.05)
        load_lbl = Text("Тежина (W)", font_size=20, color=BLUE, weight=BOLD)
        load_lbl.next_to(load_arr, UP, buff=0.1)

        # Fulcrum label
        ful_lbl = Text("Потпорна точка", font_size=18, color=ORANGE)
        ful_lbl.next_to(pivot, DOWN, buff=0.15)

        self.play(Create(bar), GrowFromCenter(pivot), run_time=0.8)
        self.play(GrowArrow(force_arr), Write(force_lbl),
                  GrowArrow(load_arr), Write(load_lbl), run_time=0.9)
        self.play(Write(ful_lbl), run_time=0.5)
        self.wait(0.5)

        # Three elements summary
        elements = VGroup(
            Text("Полугата има три точки:", font_size=24, color=WHITE2),
            Text("сила, потпора, товар.", font_size=26, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.7)

        for line in elements:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, bar, pivot, force_arr, force_lbl,
                                 load_arr, load_lbl, ful_lbl, elements)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ПОЛУГА ПРВ РОД — ВРАТ                           ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("first_class")
        title = section_title("Прв род — климнување глава")
        self.play(Write(title), run_time=0.8)

        sub = Text("Потпора во средина — сила и товар на страните",
                   font_size=22, color=GREY)
        sub.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(sub), run_time=0.6)

        # Schema
        bar1 = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE2, stroke_width=6)
        bar1.shift(UP * 0.2)
        pivot1 = Polygon([-0.3, -0.4, 0], [0.3, -0.4, 0], [0, 0.15, 0],
                         color=ORANGE, fill_opacity=0.7, stroke_color=ORANGE,
                         stroke_width=2)
        pivot1.shift(UP * 0.0)

        f_arr1 = Arrow(RIGHT * 2.5 + UP * 1.3, RIGHT * 2.5 + UP * 0.3,
                       color=RED, stroke_width=4, buff=0.05)
        f_lbl1 = Text("F", font_size=24, color=RED, weight=BOLD)
        f_lbl1.next_to(f_arr1, UP, buff=0.1)

        w_arr1 = Arrow(LEFT * 2.5 + UP * 1.3, LEFT * 2.5 + UP * 0.3,
                       color=BLUE, stroke_width=4, buff=0.05)
        w_lbl1 = Text("W", font_size=24, color=BLUE, weight=BOLD)
        w_lbl1.next_to(w_arr1, UP, buff=0.1)

        # Body example — head on neck
        body_lbl = Text("Пример во телото:", font_size=22, color=YELLOW)
        body_lbl.move_to(DOWN * 1.5 + LEFT * 4.0)

        info = VGroup(
            Text("• Глава (W) — тежина напред",
                 font_size=20, color=BLUE),
            Text("• Атлас-аксис (потпора) — врат",
                 font_size=20, color=ORANGE),
            Text("• Мускули зад вратот (F) — влечат назад",
                 font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        info.next_to(body_lbl, DOWN, buff=0.2)
        info.align_to(body_lbl, LEFT)

        self.play(Create(bar1), GrowFromCenter(pivot1), run_time=0.7)
        self.play(GrowArrow(f_arr1), Write(f_lbl1),
                  GrowArrow(w_arr1), Write(w_lbl1), run_time=0.7)
        self.wait(0.3)
        self.play(Write(body_lbl), run_time=0.6)
        for line in info:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, sub, bar1, pivot1, f_arr1, f_lbl1,
                                 w_arr1, w_lbl1, body_lbl, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ПОЛУГА ВТОР РОД — СТОИШ НА ПРСТИ                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("second_class")
        title = section_title("Втор род — на прсти")
        self.play(Write(title), run_time=0.8)

        sub = Text("Потпора на крај, товар во средина",
                   font_size=22, color=GREY)
        sub.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(sub), run_time=0.6)

        # Schema
        bar2 = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE2, stroke_width=6)
        bar2.shift(UP * 0.2)
        # Pivot at left end
        pivot2 = Polygon([-3.3, -0.2, 0], [-2.7, -0.2, 0], [-3.0, 0.35, 0],
                         color=ORANGE, fill_opacity=0.7, stroke_color=ORANGE,
                         stroke_width=2)

        # Load in middle
        w_arr2 = Arrow(UP * 1.3, UP * 0.3, color=BLUE, stroke_width=4, buff=0.05)
        w_lbl2 = Text("W", font_size=24, color=BLUE, weight=BOLD)
        w_lbl2.next_to(w_arr2, UP, buff=0.1)

        # Force at right end
        f_arr2 = Arrow(RIGHT * 2.8 + UP * 1.3, RIGHT * 2.8 + UP * 0.3,
                       color=RED, stroke_width=4, buff=0.05)
        f_lbl2 = Text("F", font_size=24, color=RED, weight=BOLD)
        f_lbl2.next_to(f_arr2, UP, buff=0.1)

        body_lbl = Text("Пример во телото:", font_size=22, color=YELLOW)
        body_lbl.move_to(DOWN * 1.5 + LEFT * 4.0)

        info = VGroup(
            Text("• Прсти на нога (потпора)", font_size=20, color=ORANGE),
            Text("• Телесна тежина (W) — во средина", font_size=20, color=BLUE),
            Text("• Лист (F) — мускул влече петата нагоре",
                 font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        info.next_to(body_lbl, DOWN, buff=0.2)
        info.align_to(body_lbl, LEFT)

        self.play(Create(bar2), GrowFromCenter(pivot2), run_time=0.7)
        self.play(GrowArrow(w_arr2), Write(w_lbl2),
                  GrowArrow(f_arr2), Write(f_lbl2), run_time=0.7)
        self.wait(0.3)
        self.play(Write(body_lbl), run_time=0.6)
        for line in info:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, sub, bar2, pivot2, w_arr2, w_lbl2,
                                 f_arr2, f_lbl2, body_lbl, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ПОЛУГА ТРЕТ РОД — БИЦЕПС                        ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("third_class")
        title = section_title("Трет род — биципс свива рака")
        self.play(Write(title), run_time=0.8)

        sub = Text("Потпора на крај, сила во средина, товар на другиот крај",
                   font_size=20, color=GREY)
        sub.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(sub), run_time=0.6)

        # Schema
        bar3 = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE2, stroke_width=6)
        bar3.shift(UP * 0.2)
        # Pivot at left
        pivot3 = Polygon([-3.3, -0.2, 0], [-2.7, -0.2, 0], [-3.0, 0.35, 0],
                         color=ORANGE, fill_opacity=0.7, stroke_color=ORANGE,
                         stroke_width=2)

        # Force in middle (slightly left of center)
        f_arr3 = Arrow(LEFT * 1.5 + UP * 1.3, LEFT * 1.5 + UP * 0.3,
                       color=RED, stroke_width=4, buff=0.05)
        f_lbl3 = Text("F", font_size=24, color=RED, weight=BOLD)
        f_lbl3.next_to(f_arr3, UP, buff=0.1)

        # Load at right end
        w_arr3 = Arrow(RIGHT * 2.8 + UP * 1.3, RIGHT * 2.8 + UP * 0.3,
                       color=BLUE, stroke_width=4, buff=0.05)
        w_lbl3 = Text("W", font_size=24, color=BLUE, weight=BOLD)
        w_lbl3.next_to(w_arr3, UP, buff=0.1)

        body_lbl = Text("Пример во телото:", font_size=22, color=YELLOW)
        body_lbl.move_to(DOWN * 1.5 + LEFT * 4.0)

        info = VGroup(
            Text("• Лакт (потпора)", font_size=20, color=ORANGE),
            Text("• Бицепс (F) — се прикачи близу лактот",
                 font_size=20, color=RED),
            Text("• Тежина во дланка (W) — на крај",
                 font_size=20, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        info.next_to(body_lbl, DOWN, buff=0.2)
        info.align_to(body_lbl, LEFT)

        self.play(Create(bar3), GrowFromCenter(pivot3), run_time=0.7)
        self.play(GrowArrow(f_arr3), Write(f_lbl3),
                  GrowArrow(w_arr3), Write(w_lbl3), run_time=0.7)
        self.wait(0.3)
        self.play(Write(body_lbl), run_time=0.6)
        for line in info:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.5)

        punch = Text("Најчестиот тип во телото.",
                     font_size=22, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.4)
        self.play(Write(punch), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, sub, bar3, pivot3, f_arr3, f_lbl3,
                                 w_arr3, w_lbl3, body_lbl, info, punch)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Прв род — климнување.", font_size=36, color=BLUE, weight=BOLD),
            Text("Втор род — на прсти.", font_size=36, color=GREEN, weight=BOLD),
            Text("Трет род — биципс.", font_size=36, color=RED, weight=BOLD),
            Text("Едно тело. Сите полуги.",
                 font_size=40, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
