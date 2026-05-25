"""
bio8-1-9  —  Рефлексен лак — брзи автоматски реакции
Биологија 8, Единица 1: Нервен и сетилен систем

Teaching narrative — Andonovski-style: three-beat punches,
reflex as protection, brain as latecomer,
one-word finishers.
Render:  manim -ql bio8-1-9.py Bio819Scene
Output:  media/videos/bio8-1-9/480p15/Bio819Scene.mp4
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


class Bio819Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — врело                                     ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Допреш врело.",
                  font_size=46, color=RED, weight=BOLD)
        h2 = Text("Рака се повлекува.",
                  font_size=46, color=ORANGE, weight=BOLD)
        h3 = Text("Пред да помислиш.",
                  font_size=42, color=YELLOW, weight=BOLD)

        block = VGroup(h1, h2, h3).arrange(DOWN, buff=0.4)
        block.move_to(ORIGIN + UP*0.3)

        for line in [h1, h2, h3]:
            self.play(Write(line), run_time=0.9)
            self.wait(0.3)

        bottom = VGroup(
            Text("Тоа не е глупост.", font_size=30, color=GREY),
            Text("Тоа е заштита.", font_size=30, color=GREEN, weight=BOLD),
            Text("Мозокот ја дознава потоа.",
                 font_size=30, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        bottom.to_edge(DOWN, buff=0.4)

        for line in bottom:
            self.play(FadeIn(line, shift=UP*0.2), run_time=0.55)
            self.wait(0.2)

        self.wait(1.2)
        self.play(FadeOut(VGroup(block, bottom)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е РЕФЛЕКС                                    ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("define")

        title = section_title("Што е рефлекс?", color=YELLOW)
        self.play(Write(title), run_time=0.8)

        defin = callout(
            "Брза, автоматска реакција — без свесна команда.",
            border=YELLOW, bg="#2a2010", font_size=26, width=10,
        )
        defin.move_to(ORIGIN + UP*1.0)
        self.play(FadeIn(defin, shift=DOWN*0.2), run_time=0.9)
        self.wait(0.5)

        traits = VGroup(
            Text("• Брз — милисекунди.", font_size=26, color=BLUE),
            Text("• Автоматски — без волја.", font_size=26, color=GREEN),
            Text("• Заштитен — го чува телото.", font_size=26, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        traits.move_to(ORIGIN + DOWN*1.0)

        for t in traits:
            self.play(FadeIn(t, shift=RIGHT*0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title, defin, traits)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 3.  РЕФЛЕКСЕН ЛАК — 5 ЧЕКОРИ                         ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("arc")

        title = section_title("Рефлексен лак — 5 чекори", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # 5 boxes arranged in arc-like layout
        positions = [
            LEFT*5.5 + DOWN*1.3,   # receptor
            LEFT*3   + UP*0.8,      # sensory neuron
            LEFT*0   + UP*1.6,      # spinal cord
            RIGHT*3  + UP*0.8,      # motor neuron
            RIGHT*5.5 + DOWN*1.3,   # effector
        ]
        steps_data = [
            ("1", "Рецептор", "(во кожа)", RED),
            ("2", "Сетилен неврон", "→ кон 'рбет", BLUE),
            ("3", "'Рбетен мозок", "(одлука!)", PURPLE),
            ("4", "Моторен неврон", "→ кон мускул", GREEN),
            ("5", "Извршител", "(мускул)", ORANGE),
        ]

        nodes = VGroup()
        for (num, name, sub, col), pos in zip(steps_data, positions):
            box = Circle(radius=0.55, color=col,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_width=3)
            box.move_to(pos)
            num_t = Text(num, font_size=30, color=col, weight=BOLD)
            num_t.move_to(box)
            name_t = Text(name, font_size=18, color=col, weight=BOLD)
            name_t.next_to(box, DOWN, buff=0.15)
            sub_t = Text(sub, font_size=14, color=WHITE2)
            sub_t.next_to(name_t, DOWN, buff=0.05)
            nodes.add(VGroup(box, num_t, name_t, sub_t))

        # Connect with arcs/arrows
        arrows = VGroup()
        for i in range(len(positions) - 1):
            a = Arrow(nodes[i][0].get_center(),
                      nodes[i+1][0].get_center(),
                      color=YELLOW, stroke_width=3,
                      buff=0.65, max_tip_length_to_length_ratio=0.12)
            arrows.add(a)

        for n in nodes:
            self.play(FadeIn(n, shift=UP*0.1), run_time=0.55)
            self.wait(0.1)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.4)
            self.wait(0.1)

        self.wait(0.4)

        # animate impulse traveling
        impulse = Dot(nodes[0][0].get_center(), color=YELLOW, radius=0.16)
        self.add(impulse)
        self.play(FadeIn(impulse), run_time=0.3)
        for i in range(1, len(nodes)):
            self.play(impulse.animate.move_to(nodes[i][0].get_center()),
                      Flash(nodes[i][0].get_center(), color=YELLOW,
                            flash_radius=0.7, num_lines=10),
                      run_time=0.6, rate_func=linear)
        self.wait(0.5)

        # callout: bypass brain
        bypass = Text("Сигналот НЕ оди до мозокот прво!",
                      font_size=26, color=RED, weight=BOLD)
        bypass.to_edge(DOWN, buff=0.4)
        self.play(Write(bypass), run_time=1.0)
        self.wait(1.4)

        arc_grp = VGroup(nodes, arrows, impulse, bypass)
        self.play(FadeOut(VGroup(title, arc_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 4.  ПРИМЕР — ВРЕЛА ШПОРЕТ                            ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hot")

        title = section_title("Пример — врело шпорет", color=RED)
        self.play(Write(title), run_time=0.8)

        # hand (left side)
        hand = RoundedRectangle(width=1.2, height=0.7, corner_radius=0.2,
                                fill_color="#e8c7a0", fill_opacity=1,
                                stroke_color=WHITE2, stroke_width=2)
        hand.move_to(LEFT*5 + UP*0.5)
        h_lbl = Text("рака", font_size=18, color=WHITE2)
        h_lbl.next_to(hand, UP, buff=0.15)

        # stove (red orange)
        stove = Square(side_length=1.2, color=RED,
                       fill_color=ORANGE, fill_opacity=0.8,
                       stroke_color=RED, stroke_width=3)
        stove.move_to(LEFT*5 + DOWN*1.2)
        s_lbl = Text("шпорет!", font_size=20, color=RED, weight=BOLD)
        s_lbl.next_to(stove, DOWN, buff=0.15)

        # heat waves
        waves = VGroup(*[
            Arc(radius=0.35 + 0.2*i, angle=PI,
                color=ORANGE, stroke_width=2)
            .rotate(-PI/2)
            .move_to(stove.get_top() + UP*0.2)
            for i in range(3)
        ])

        self.play(FadeIn(hand), Write(h_lbl),
                  FadeIn(stove), Write(s_lbl),
                  Create(waves), run_time=1.0)
        self.wait(0.3)

        # spinal cord representation (vertical bar on right)
        spine = RoundedRectangle(width=0.8, height=4.0, corner_radius=0.2,
                                 fill_color=PURPLE, fill_opacity=0.6,
                                 stroke_color=PURPLE, stroke_width=2)
        spine.move_to(RIGHT*4 + UP*0.2)
        sp_lbl = Text("'рбетен\nмозок", font_size=18, color=WHITE2,
                      line_spacing=0.8, weight=BOLD)
        sp_lbl.move_to(spine)

        self.play(FadeIn(spine), Write(sp_lbl), run_time=0.7)

        # sensory in
        in_arrow = Arrow(hand.get_right() + DOWN*0.3,
                         spine.get_left() + UP*0.5,
                         color=BLUE, stroke_width=3)
        in_lbl = Text("1. сетилен", font_size=16, color=BLUE)
        in_lbl.next_to(in_arrow, UP, buff=0.1)

        # motor out
        out_arrow = Arrow(spine.get_left() + DOWN*0.5,
                          hand.get_right() + DOWN*0.5,
                          color=GREEN, stroke_width=3)
        out_lbl = Text("2. моторен", font_size=16, color=GREEN)
        out_lbl.next_to(out_arrow, DOWN, buff=0.1)

        self.play(GrowArrow(in_arrow), Write(in_lbl), run_time=0.7)
        self.wait(0.2)
        self.play(GrowArrow(out_arrow), Write(out_lbl), run_time=0.7)
        self.wait(0.2)

        # hand pulls away
        self.play(hand.animate.shift(UP*1.2), run_time=0.4)
        self.play(Flash(hand.get_center(), color=GREEN,
                        flash_radius=0.8, num_lines=12), run_time=0.5)
        self.wait(0.3)

        finisher = Text("Без свесна одлука. Без чекање. Заштита.",
                        font_size=26, color=YELLOW, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.3)
        self.play(Write(finisher), run_time=1.1)
        self.wait(1.5)

        hot_grp = VGroup(hand, h_lbl, stove, s_lbl, waves, spine, sp_lbl,
                         in_arrow, in_lbl, out_arrow, out_lbl, finisher)
        self.play(FadeOut(VGroup(title, hot_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 5.  ПАТЕЛАРЕН РЕФЛЕКС                                ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("knee")

        title = section_title("Пателарен рефлекс — удар во колено",
                              color=BLUE)
        self.play(Write(title), run_time=0.8)

        # leg: thigh (rectangle) hinged at knee, with shin
        thigh = Rectangle(width=2.5, height=0.6,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=2)
        thigh.move_to(LEFT*3 + UP*0.3)
        knee = Circle(radius=0.35, color=YELLOW,
                      fill_color=YELLOW, fill_opacity=0.8,
                      stroke_color=WHITE2, stroke_width=2)
        knee.move_to(thigh.get_right() + RIGHT*0.05)
        knee_lbl = Text("колено", font_size=16, color=WHITE2)
        knee_lbl.next_to(knee, UP, buff=0.15)

        # shin hanging down
        shin = Rectangle(width=0.4, height=2.2,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=2)
        shin.next_to(knee, DOWN, buff=0).shift(DOWN*0.0)

        self.play(FadeIn(thigh), FadeIn(knee), Write(knee_lbl),
                  FadeIn(shin), run_time=0.9)
        self.wait(0.3)

        # hammer
        hammer_head = Rectangle(width=0.6, height=0.25,
                                fill_color=GREY, fill_opacity=1,
                                stroke_color=WHITE2, stroke_width=1.5)
        hammer_handle = Rectangle(width=0.15, height=1.0,
                                  fill_color="#8b4513", fill_opacity=1,
                                  stroke_color=WHITE2, stroke_width=1)
        hammer_handle.next_to(hammer_head, UP, buff=0)
        hammer = VGroup(hammer_head, hammer_handle)
        hammer.move_to(knee.get_center() + UP*2 + LEFT*0.4)

        self.play(FadeIn(hammer), run_time=0.5)

        # hammer strikes knee
        self.play(hammer.animate.move_to(knee.get_center() + UP*0.45 + LEFT*0.4),
                  run_time=0.4, rate_func=rush_into)
        self.play(Flash(knee.get_center(), color=YELLOW,
                        flash_radius=0.6, num_lines=10), run_time=0.3)

        # shin kicks up (rotate around knee)
        # We rotate shin about knee.get_center() by ~ -45°
        self.play(Rotate(shin, angle=-PI/3,
                         about_point=knee.get_center()),
                  run_time=0.45, rate_func=rush_out)
        self.wait(0.3)

        # timer with milliseconds
        timer = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.2,
                                 fill_color="#10293a", fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=2)
        timer.move_to(RIGHT*3 + UP*1.5)
        t_top = Text("Време на реакција:", font_size=18, color=WHITE2)
        t_val = Text("~50 ms", font_size=36, color=YELLOW, weight=BOLD)
        t_top.move_to(timer.get_top() + DOWN*0.25)
        t_val.move_to(timer.get_bottom() + UP*0.35)

        self.play(FadeIn(timer), Write(t_top), Write(t_val), run_time=0.9)
        self.wait(0.4)

        # comparison
        cmp_box = VGroup(
            Text("Свесна одлука: ~250 ms", font_size=22, color=GREY),
            Text("Рефлекс: ~50 ms", font_size=22, color=GREEN, weight=BOLD),
            Text("5× побрз!", font_size=26, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        cmp_box.move_to(RIGHT*3 + DOWN*1.5)

        for c in cmp_box:
            self.play(FadeIn(c, shift=UP*0.15), run_time=0.5)
            self.wait(0.15)

        self.wait(1.4)

        knee_grp = VGroup(thigh, knee, knee_lbl, shin, hammer, timer,
                          t_top, t_val, cmp_box)
        self.play(FadeOut(VGroup(title, knee_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 6.  УСЛОВНИ vs БЕЗУСЛОВНИ                            ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("kinds")

        title = section_title("Видови рефлекси", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        # two columns
        uncond = RoundedRectangle(width=5.5, height=4.5, corner_radius=0.3,
                                  fill_color="#10293a", fill_opacity=1,
                                  stroke_color=BLUE, stroke_width=2.5)
        uncond.move_to(LEFT*3.3 + DOWN*0.3)
        u_lbl = Text("Безусловни", font_size=28, color=BLUE, weight=BOLD)
        u_lbl.move_to(uncond.get_top() + DOWN*0.4)
        u_sub = Text("(вродени)", font_size=18, color=GREY)
        u_sub.next_to(u_lbl, DOWN, buff=0.05)

        u_items = VGroup(
            Text("• кашлање", font_size=22, color=WHITE2),
            Text("• кивање", font_size=22, color=WHITE2),
            Text("• трепкање", font_size=22, color=WHITE2),
            Text("• цицање (бебе)", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        u_items.move_to(uncond.get_center() + DOWN*0.2)

        cond = RoundedRectangle(width=5.5, height=4.5, corner_radius=0.3,
                                fill_color="#2a1a3a", fill_opacity=1,
                                stroke_color=PURPLE, stroke_width=2.5)
        cond.move_to(RIGHT*3.3 + DOWN*0.3)
        c_lbl = Text("Условни", font_size=28, color=PURPLE, weight=BOLD)
        c_lbl.move_to(cond.get_top() + DOWN*0.4)
        c_sub = Text("(научени)", font_size=18, color=GREY)
        c_sub.next_to(c_lbl, DOWN, buff=0.05)

        c_items = VGroup(
            Text("• возење велосипед", font_size=22, color=WHITE2),
            Text("• свирење инструмент", font_size=22, color=WHITE2),
            Text("• пишување", font_size=22, color=WHITE2),
            Text("• плукање при мирис", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        c_items.move_to(cond.get_center() + DOWN*0.2)

        self.play(FadeIn(uncond), Write(u_lbl), Write(u_sub), run_time=0.8)
        self.play(FadeIn(cond), Write(c_lbl), Write(c_sub), run_time=0.8)
        self.wait(0.3)

        for i in range(4):
            self.play(FadeIn(u_items[i], shift=RIGHT*0.15),
                      FadeIn(c_items[i], shift=LEFT*0.15), run_time=0.4)
            self.wait(0.1)

        self.wait(1.3)

        kinds_grp = VGroup(uncond, u_lbl, u_sub, u_items,
                           cond, c_lbl, c_sub, c_items)
        self.play(FadeOut(VGroup(title, kinds_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 7.  FINISHER                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        f1 = Text("Рефлексот не размислува.",
                  font_size=40, color=YELLOW, weight=BOLD)
        f2 = Text("Рефлексот не чека.",
                  font_size=40, color=ORANGE, weight=BOLD)
        f3 = Text("Рефлексот спасува.",
                  font_size=40, color=GREEN, weight=BOLD)
        f4 = Text("Брзо.", font_size=58, color=RED, weight=BOLD)

        block = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN)

        for line in [f1, f2, f3]:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.play(Write(f4), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(block), run_time=1.0)
        self.wait(0.5)
