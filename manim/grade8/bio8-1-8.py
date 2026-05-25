"""
bio8-1-8  —  Систем за излачување
Биологија 8, Единица 1: Нервен и сетилен систем

Teaching narrative — Andonovski-style: three-beat punches,
kidneys as Swiss precision, filtration as accounting,
one-word finishers.
Render:  manim -ql bio8-1-8.py Bio818Scene
Output:  media/videos/bio8-1-8/480p15/Bio818Scene.mp4
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


class Bio818Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — швајцарски часовник                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Бубрезите филтрираат 180 литри крв на ден.",
                  font_size=34, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.5)
        self.wait(0.5)

        h2 = Text("Издвојуваат само 1,5 литра.",
                  font_size=34, color=ORANGE, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.4)
        self.play(Write(h2), run_time=1.3)
        self.wait(0.4)

        # visual: big bar 180L on left, small bar 1.5L on right
        big = Rectangle(width=1.2, height=4.5,
                        fill_color=RED, fill_opacity=0.5,
                        stroke_color=RED, stroke_width=2)
        big.move_to(LEFT*3 + DOWN*0.7)
        big_lbl = Text("180 L\nкрв", font_size=22, color=WHITE2)
        big_lbl.next_to(big, DOWN, buff=0.25)

        small = Rectangle(width=1.2, height=0.5,
                          fill_color=YELLOW, fill_opacity=0.7,
                          stroke_color=YELLOW, stroke_width=2)
        small.move_to(RIGHT*3 + DOWN*2.7)
        small_lbl = Text("1,5 L\nурина", font_size=22, color=WHITE2)
        small_lbl.next_to(small, DOWN, buff=0.25)

        arrow = Arrow(big.get_right(), small.get_left(),
                      color=GREEN, stroke_width=4)
        a_lbl = Text("филтрирање", font_size=22, color=GREEN)
        a_lbl.next_to(arrow, UP, buff=0.15)

        self.play(FadeIn(big), Write(big_lbl), run_time=0.8)
        self.play(GrowArrow(arrow), Write(a_lbl), run_time=0.8)
        self.play(FadeIn(small), Write(small_lbl), run_time=0.7)
        self.wait(0.4)

        finisher = Text("Прецизни како швајцарски часовник.",
                        font_size=28, color=PURPLE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.3)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(h1, h2, big, big_lbl, small, small_lbl,
                                 arrow, a_lbl, finisher)),
                  run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 2.  АНАТОМИЈА — БУБРЕГ                               ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("anatomy")

        title = section_title("Бубрег — пресек", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # bean-shaped outline
        outer = Ellipse(width=4.5, height=6, color=WHITE2,
                        fill_color="#3a1a1a", fill_opacity=0.9,
                        stroke_width=2.5).scale(0.7)
        outer.move_to(LEFT*3)

        # inner medulla (lighter)
        inner = Ellipse(width=3.2, height=4.6, color=WHITE2,
                        fill_color="#5a2828", fill_opacity=0.95,
                        stroke_width=2).scale(0.7)
        inner.move_to(LEFT*3)

        # pelvis (light tube)
        pelvis = Ellipse(width=1.4, height=2.2,
                         fill_color=YELLOW, fill_opacity=0.6,
                         stroke_color=YELLOW, stroke_width=2).scale(0.7)
        pelvis.move_to(LEFT*3)

        self.play(FadeIn(outer), run_time=0.6)
        self.play(FadeIn(inner), run_time=0.6)
        self.play(FadeIn(pelvis), run_time=0.6)

        # ureter tube going down/right
        ureter = Line(LEFT*3 + DOWN*1.5, LEFT*3 + DOWN*2.5,
                      color=YELLOW, stroke_width=5)
        self.play(Create(ureter), run_time=0.5)

        # labels
        labels = VGroup(
            VGroup(Text("Кора", font_size=22, color=RED, weight=BOLD),
                   Text("(надворешен слој)", font_size=18, color=WHITE2)),
            VGroup(Text("Срцевина", font_size=22, color=ORANGE, weight=BOLD),
                   Text("(пирамиди)", font_size=18, color=WHITE2)),
            VGroup(Text("Бубрежно легенче", font_size=22, color=YELLOW, weight=BOLD),
                   Text("(собира урина)", font_size=18, color=WHITE2)),
            VGroup(Text("Уретер", font_size=22, color=GREEN, weight=BOLD),
                   Text("(води кон мочен меур)", font_size=18, color=WHITE2)),
        )
        for l in labels:
            l.arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        labels.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        labels.move_to(RIGHT*2.5 + UP*0.2)

        for l in labels:
            self.play(FadeIn(l, shift=LEFT*0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(1.3)

        kidney_grp = VGroup(outer, inner, pelvis, ureter, labels)
        self.play(FadeOut(VGroup(title, kidney_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 3.  НЕФРОН — ФИЛТРАЦИСКА ЕДИНИЦА                     ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("nephron")

        title = section_title("Нефрон — единицата што филтрира", color=GREEN)
        self.play(Write(title), run_time=0.8)

        sub = Text("Секој бубрег има ~1.000.000 нефрони.",
                   font_size=22, color=GREY)
        sub.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(0.3)

        # glomerulus — tangled circle on left
        glom = Circle(radius=0.6, color=RED,
                      fill_color=RED, fill_opacity=0.4,
                      stroke_color=RED, stroke_width=2.5)
        glom.move_to(LEFT*4 + UP*0.5)
        # add fake capillary squiggle
        squiggle = ParametricFunction(
            lambda t: glom.get_center() + np.array([
                0.4*np.cos(t*3), 0.4*np.sin(t*3) + 0.05*np.sin(t*9), 0
            ]),
            t_range=[0, 2*PI],
            color=RED, stroke_width=2,
        )
        glom_lbl = Text("Гломерул", font_size=20, color=RED, weight=BOLD)
        glom_lbl.next_to(glom, UP, buff=0.2)
        glom_sub = Text("капиларно клопче", font_size=16, color=WHITE2)
        glom_sub.next_to(glom_lbl, UP, buff=0.05)

        # capsule (Bowman's) — outer cup around glomerulus
        capsule = Circle(radius=0.95, color=YELLOW, stroke_width=2,
                         fill_opacity=0)
        capsule.move_to(glom.get_center())
        cap_lbl = Text("Боуманова капсула", font_size=18, color=YELLOW)
        cap_lbl.next_to(capsule, DOWN, buff=0.2)

        self.play(FadeIn(glom), Create(squiggle), Write(glom_lbl),
                  Write(glom_sub), run_time=1.1)
        self.play(Create(capsule), Write(cap_lbl), run_time=0.8)
        self.wait(0.4)

        # tubule — winding line going right
        tubule = VMobject(color=BLUE, stroke_width=4)
        tubule.set_points_smoothly([
            capsule.get_right(),
            LEFT*2.5 + UP*0.5,
            LEFT*1.5 + DOWN*0.5,
            LEFT*0.5 + UP*0.7,
            RIGHT*0.5 + DOWN*0.8,
            RIGHT*1.5 + UP*0.3,
            RIGHT*3 + DOWN*0.5,
        ])
        tub_lbl = Text("Тубул", font_size=20, color=BLUE, weight=BOLD)
        tub_lbl.move_to(RIGHT*0.5 + UP*1.5)
        tub_sub = Text("ресорпција + излачување", font_size=16, color=WHITE2)
        tub_sub.next_to(tub_lbl, DOWN, buff=0.1)

        self.play(Create(tubule), run_time=1.5)
        self.play(Write(tub_lbl), Write(tub_sub), run_time=0.7)

        # collecting duct
        duct = Line(RIGHT*3 + DOWN*0.5, RIGHT*3 + DOWN*2.5,
                    color=YELLOW, stroke_width=5)
        duct_lbl = Text("собирен канал", font_size=18, color=YELLOW)
        duct_lbl.next_to(duct, RIGHT, buff=0.2)
        self.play(Create(duct), Write(duct_lbl), run_time=0.7)
        self.wait(0.3)

        # animate flow: red dots = waste, blue = water/useful
        waste = VGroup(*[Dot(color=RED, radius=0.08)
                         for _ in range(6)])
        for i, d in enumerate(waste):
            d.move_to(glom.get_center() + np.array([np.cos(i)*0.2,
                                                     np.sin(i)*0.2, 0]))
        self.add(waste)

        # flow from glomerulus through tubule into duct
        self.play(*[d.animate.move_to(capsule.get_right() + RIGHT*0.2)
                    for d in waste], run_time=0.8)
        self.play(MoveAlongPath(waste, tubule), run_time=1.6, rate_func=linear)
        self.play(waste.animate.move_to(duct.get_end()), run_time=0.8)
        self.wait(0.4)

        flow_lbl = Text("отпад → урина", font_size=22, color=YELLOW, weight=BOLD)
        flow_lbl.to_edge(DOWN, buff=0.3)
        self.play(Write(flow_lbl), run_time=0.9)
        self.wait(1.5)

        neph_grp = VGroup(sub, glom, squiggle, glom_lbl, glom_sub,
                          capsule, cap_lbl, tubule, tub_lbl, tub_sub,
                          duct, duct_lbl, waste, flow_lbl)
        self.play(FadeOut(VGroup(title, neph_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 4.  ПАТ НА УРИНАТА                                   ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("path")

        title = section_title("Патот на урината", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # 4 boxes flow chart
        steps_data = [
            ("Бубрези", BLUE,    "филтрираат крв"),
            ("Уретери", GREEN,   "тенки цевки"),
            ("Мочен меур", ORANGE, "складиште"),
            ("Уретра", PURPLE,   "излез"),
        ]
        boxes = VGroup()
        for name, col, sub in steps_data:
            b = RoundedRectangle(width=2.3, height=1.4, corner_radius=0.25,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=col, stroke_width=2.5)
            n_lbl = Text(name, font_size=22, color=col, weight=BOLD)
            n_lbl.move_to(b.get_top() + DOWN*0.4)
            s_lbl = Text(sub, font_size=15, color=WHITE2)
            s_lbl.next_to(n_lbl, DOWN, buff=0.2)
            boxes.add(VGroup(b, n_lbl, s_lbl))
        boxes.arrange(RIGHT, buff=0.3)
        boxes.move_to(ORIGIN + UP*0.2)

        # arrows
        arrows = VGroup()
        for i in range(len(steps_data) - 1):
            ar = Arrow(boxes[i][0].get_right(), boxes[i+1][0].get_left(),
                       color=YELLOW, stroke_width=3,
                       buff=0.05, max_tip_length_to_length_ratio=0.18)
            arrows.add(ar)

        for b in boxes:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.35)
        self.wait(0.4)

        # animate drop traveling
        drop = Dot(boxes[0][0].get_center(), color=YELLOW, radius=0.14)
        self.play(FadeIn(drop), run_time=0.4)
        for b in boxes[1:]:
            self.play(drop.animate.move_to(b[0].get_center()),
                      run_time=0.7, rate_func=smooth)
        self.wait(0.4)

        finisher = Text("Влез — обработка — излез.",
                        font_size=28, color=YELLOW, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        path_grp = VGroup(boxes, arrows, drop, finisher)
        self.play(FadeOut(VGroup(title, path_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 5.  РАМНОТЕЖА НА ВОДА                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("water")

        title = section_title("Рамнотежа на вода", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # human body silhouette in middle, with water % label
        body = RoundedRectangle(width=1.8, height=4.0, corner_radius=0.4,
                                fill_color=BLUE, fill_opacity=0.3,
                                stroke_color=BLUE, stroke_width=2.5)
        body.move_to(ORIGIN + UP*0.1)
        head = Circle(radius=0.5, color=BLUE,
                      fill_color=BLUE, fill_opacity=0.3, stroke_width=2.5)
        head.next_to(body, UP, buff=0)

        pct = Text("~60%", font_size=44, color=BLUE, weight=BOLD)
        pct.move_to(body)
        pct_sub = Text("вода", font_size=22, color=WHITE2)
        pct_sub.next_to(pct, DOWN, buff=0.15)

        self.play(FadeIn(body), FadeIn(head), run_time=0.7)
        self.play(Write(pct), Write(pct_sub), run_time=0.9)
        self.wait(0.3)

        # left: intake
        intake = VGroup(
            Text("ВНЕС", font_size=24, color=GREEN, weight=BOLD),
            Text("вода + храна", font_size=20, color=WHITE2),
            Text("~2,5 L/ден", font_size=20, color=GREEN),
        ).arrange(DOWN, buff=0.15)
        intake.move_to(LEFT*4.5)
        in_arrow = Arrow(intake.get_right(), body.get_left(),
                         color=GREEN, stroke_width=3)

        outflow = VGroup(
            Text("ИЗЛЕЗ", font_size=24, color=ORANGE, weight=BOLD),
            Text("урина + пот + здив", font_size=18, color=WHITE2),
            Text("~2,5 L/ден", font_size=20, color=ORANGE),
        ).arrange(DOWN, buff=0.15)
        outflow.move_to(RIGHT*4.5)
        out_arrow = Arrow(body.get_right(), outflow.get_left(),
                          color=ORANGE, stroke_width=3)

        self.play(FadeIn(intake, shift=RIGHT*0.2),
                  GrowArrow(in_arrow), run_time=0.9)
        self.wait(0.2)
        self.play(GrowArrow(out_arrow),
                  FadeIn(outflow, shift=LEFT*0.2), run_time=0.9)
        self.wait(0.4)

        finisher = Text("Што влегува — мора да излезе.",
                        font_size=26, color=YELLOW, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.4)

        water_grp = VGroup(body, head, pct, pct_sub, intake, in_arrow,
                           out_arrow, outflow, finisher)
        self.play(FadeOut(VGroup(title, water_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 6.  ДИЈАЛИЗА                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dialysis")

        title = section_title("Кога бубрезите откажуваат — дијализа", color=RED)
        self.play(Write(title), run_time=0.8)

        # person on left
        pat = RoundedRectangle(width=1.3, height=2.4, corner_radius=0.3,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=WHITE2, stroke_width=2)
        pat.move_to(LEFT*4.5 + DOWN*0.2)
        p_head = Circle(radius=0.4, color=WHITE2,
                        fill_color=DARK_CARD, fill_opacity=1, stroke_width=2)
        p_head.next_to(pat, UP, buff=0)
        patient = VGroup(pat, p_head)
        pat_lbl = Text("пациент", font_size=18, color=GREY)
        pat_lbl.next_to(patient, DOWN, buff=0.2)

        # machine on right
        machine = RoundedRectangle(width=2.5, height=3.0, corner_radius=0.3,
                                   fill_color="#1a3a4a", fill_opacity=1,
                                   stroke_color=BLUE, stroke_width=2.5)
        machine.move_to(RIGHT*3.5 + DOWN*0.2)
        m_lbl = Text("дијализна\nмашина", font_size=22, color=BLUE, weight=BOLD,
                     line_spacing=0.8)
        m_lbl.move_to(machine)

        # two tubes connecting them
        tube_top = Line(patient.get_right() + UP*0.5,
                        machine.get_left() + UP*0.5,
                        color=RED, stroke_width=4)
        tube_bot = Line(machine.get_left() + DOWN*0.5,
                        patient.get_right() + DOWN*0.5,
                        color=BLUE, stroke_width=4)
        tube_top_lbl = Text("крв со отпад", font_size=16, color=RED)
        tube_top_lbl.next_to(tube_top, UP, buff=0.1)
        tube_bot_lbl = Text("исчистена крв", font_size=16, color=BLUE)
        tube_bot_lbl.next_to(tube_bot, DOWN, buff=0.1)

        self.play(FadeIn(patient), Write(pat_lbl), run_time=0.7)
        self.play(FadeIn(machine), Write(m_lbl), run_time=0.8)
        self.play(Create(tube_top), Write(tube_top_lbl), run_time=0.6)
        self.play(Create(tube_bot), Write(tube_bot_lbl), run_time=0.6)
        self.wait(0.3)

        # animate flow
        red_dot = Dot(patient.get_right() + UP*0.5, color=RED, radius=0.1)
        blue_dot = Dot(machine.get_left() + DOWN*0.5, color=BLUE, radius=0.1)
        self.add(red_dot, blue_dot)
        for _ in range(2):
            self.play(red_dot.animate.move_to(machine.get_left() + UP*0.5),
                      blue_dot.animate.move_to(patient.get_right() + DOWN*0.5),
                      run_time=1.0)
            red_dot.move_to(patient.get_right() + UP*0.5)
            blue_dot.move_to(machine.get_left() + DOWN*0.5)
        self.wait(0.3)

        finisher = Text("Машината прави што бубрегот веќе не може.",
                        font_size=24, color=PURPLE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.4)
        self.play(Write(finisher), run_time=1.1)
        self.wait(1.5)

        dial_grp = VGroup(patient, pat_lbl, machine, m_lbl,
                          tube_top, tube_top_lbl, tube_bot, tube_bot_lbl,
                          red_dot, blue_dot, finisher)
        self.play(FadeOut(VGroup(title, dial_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 7.  FINISHER                                         ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        f1 = Text("Бубрезите чистат.", font_size=44, color=BLUE, weight=BOLD)
        f2 = Text("Бубрезите делат.", font_size=44, color=GREEN, weight=BOLD)
        f3 = Text("Бубрезите никогаш не спијат.",
                  font_size=40, color=YELLOW, weight=BOLD)
        f4 = Text("Тивки.", font_size=54, color=PURPLE, weight=BOLD)

        block = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN)

        for line in [f1, f2, f3]:
            self.play(Write(line), run_time=0.7)
            self.wait(0.2)
        self.play(Write(f4), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(block), run_time=1.0)
        self.wait(0.5)
