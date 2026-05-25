"""
bio8-1-6  —  Рецептори во кожата
Биологија 8, Единица 1: Нервен и сетилен систем

Teaching narrative — Andonovski-style: three-beat punches,
skin as drama, receptors as silent witnesses, one-word finishers.
Render:  manim -ql bio8-1-6.py Bio816Scene
Output:  media/videos/bio8-1-6/480p15/Bio816Scene.mp4
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


class Bio816Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — кожата не е обвивка                       ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Кожата не е обвивка.",
                  font_size=44, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.5)

        h2 = Text("Кожата е сетило.",
                  font_size=44, color=ORANGE, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.4)
        self.play(Write(h2), run_time=1.2)
        self.wait(0.5)

        senses = VGroup(
            Text("Чувствува допир.", font_size=32, color=BLUE),
            Text("Чувствува болка.", font_size=32, color=RED),
            Text("Чувствува топлина.", font_size=32, color=ORANGE),
            Text("Чувствува ладно.", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN*0.3)

        for s in senses:
            self.play(FadeIn(s, shift=UP*0.2), run_time=0.5)
            self.wait(0.15)

        finishers = VGroup(
            Text("Сè паралелно.", font_size=34, color=GREEN, weight=BOLD),
            Text("Сè во ист миг.", font_size=34, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)

        for f in finishers:
            self.play(FadeIn(f, shift=UP*0.2), run_time=0.6)
            self.wait(0.2)

        self.wait(1.0)
        self.play(FadeOut(VGroup(h1, h2, senses, finishers)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  НАЈГОЛЕМИОТ ОРГАН                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("largest")

        title = section_title("Најголемиот орган", color=YELLOW)
        self.play(Write(title), run_time=0.8)

        body = RoundedRectangle(
            width=2.6, height=4.5, corner_radius=0.8,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=WHITE2, stroke_width=2.5,
        ).move_to(LEFT*3.5)
        head = Circle(radius=0.7, color=WHITE2, fill_color=DARK_CARD, fill_opacity=1)
        head.next_to(body, UP, buff=-0.2)
        silhouette = VGroup(body, head)

        self.play(FadeIn(silhouette), run_time=0.8)

        area_label = Text("2 m²", font_size=72, color=ORANGE, weight=BOLD)
        area_label.move_to(RIGHT*2.5 + UP*1.2)
        area_sub = Text("површина на кожата", font_size=24, color=WHITE2)
        area_sub.next_to(area_label, DOWN, buff=0.25)

        self.play(Write(area_label), FadeIn(area_sub), run_time=1.2)
        self.wait(0.4)

        weight_label = Text("~ 4 kg", font_size=44, color=GREEN, weight=BOLD)
        weight_label.move_to(RIGHT*2.5 + DOWN*0.6)
        weight_sub = Text("маса кај возрасен", font_size=22, color=GREY)
        weight_sub.next_to(weight_label, DOWN, buff=0.2)

        self.play(Write(weight_label), FadeIn(weight_sub), run_time=1.0)
        self.wait(0.4)

        finisher = Text("Најголем. Најтежок. Најприсутен.",
                        font_size=30, color=PURPLE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, silhouette, area_label, area_sub,
                                 weight_label, weight_sub, finisher)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ТРИ СЛОЕВИ                                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("layers")

        title = section_title("Три слоеви на кожата", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # Epidermis (top)
        epi = Rectangle(width=10, height=0.6,
                        fill_color="#e8c7a0", fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=1)
        epi.move_to(UP*1.6)
        epi_lbl = Text("Епидермис", font_size=26, color=DARK_CARD, weight=BOLD)
        epi_lbl.move_to(epi)
        epi_note = Text("надворешен заштитен слој", font_size=20, color=GREY)
        epi_note.next_to(epi, RIGHT, buff=0).shift(LEFT*0).next_to(epi, DOWN, buff=0.05).align_to(epi, LEFT).shift(RIGHT*0.2)

        # Dermis (middle)
        derm = Rectangle(width=10, height=1.6,
                         fill_color="#c97c6a", fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=1)
        derm.next_to(epi, DOWN, buff=0)
        derm_lbl = Text("Дермис", font_size=28, color=WHITE2, weight=BOLD)
        derm_lbl.move_to(derm).shift(LEFT*3.5)

        # Hypodermis (bottom)
        hyp = Rectangle(width=10, height=1.4,
                        fill_color="#ffd54f", fill_opacity=0.7,
                        stroke_color=WHITE2, stroke_width=1)
        hyp.next_to(derm, DOWN, buff=0)
        hyp_lbl = Text("Хиподермис", font_size=26, color=DARK_CARD, weight=BOLD)
        hyp_lbl.move_to(hyp).shift(LEFT*3.3)

        self.play(FadeIn(epi), Write(epi_lbl), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(derm), Write(derm_lbl), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hyp), Write(hyp_lbl), run_time=0.8)
        self.wait(0.4)

        # Right-side descriptions
        descs = VGroup(
            Text("• мртви клетки + меланин", font_size=20, color=WHITE2),
            Text("• крвни садови + рецептори", font_size=20, color=WHITE2),
            Text("• масно ткиво + изолација", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        descs[0].move_to(epi.get_right() + RIGHT*0.0).shift(DOWN*0.0)
        descs.move_to(RIGHT*3.8 + DOWN*0.3)

        # Manually align each description to its layer
        descs[0].next_to(epi, RIGHT, buff=0.3).set_color("#e8c7a0")
        descs[1].next_to(derm, RIGHT, buff=0.3).set_color(YELLOW)
        descs[2].next_to(hyp, RIGHT, buff=0.3).set_color(ORANGE)

        # Shrink to fit
        for d in descs:
            d.scale(0.95)

        for d in descs:
            self.play(FadeIn(d, shift=LEFT*0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(1.2)

        layer_group = VGroup(epi, derm, hyp, epi_lbl, derm_lbl, hyp_lbl,
                             descs)
        self.play(FadeOut(VGroup(title, layer_group)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 4.  РЕЦЕПТОРИ ВО ДЕРМИС                              ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("receptors")

        title = section_title("Рецептори во кожата", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # Cross-section background
        skin_bg = Rectangle(width=12, height=4.5,
                            fill_color="#c97c6a", fill_opacity=0.4,
                            stroke_color=WHITE2, stroke_width=1)
        skin_bg.move_to(DOWN*0.4)
        surface = Line(skin_bg.get_corner(UL), skin_bg.get_corner(UR),
                       color=YELLOW, stroke_width=3)

        self.play(FadeIn(skin_bg), Create(surface), run_time=0.8)

        # Meissner — light touch (near surface)
        meissner = Ellipse(width=0.55, height=0.35,
                           fill_color=BLUE, fill_opacity=1,
                           stroke_color=WHITE2, stroke_width=1.5)
        meissner.move_to(LEFT*4 + UP*0.6)
        m_lbl = Text("Меиснерови", font_size=18, color=BLUE, weight=BOLD)
        m_lbl_2 = Text("телца — лесен допир", font_size=16, color=WHITE2)
        m_grp = VGroup(m_lbl, m_lbl_2).arrange(DOWN, buff=0.05)
        m_grp.next_to(meissner, UP, buff=0.2)

        # Pacinian — deep pressure (bottom)
        pacinian = Circle(radius=0.35, color=PURPLE,
                          fill_color=PURPLE, fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1.5)
        pacinian.move_to(LEFT*1.5 + DOWN*1.4)
        # onion-skin rings around it
        for r in [0.5, 0.65, 0.8]:
            pacinian = VGroup(pacinian,
                              Circle(radius=r, color=PURPLE,
                                     stroke_width=1.2, fill_opacity=0)
                              .move_to(LEFT*1.5 + DOWN*1.4))
        p_lbl = Text("Паќиниеви", font_size=18, color=PURPLE, weight=BOLD)
        p_lbl_2 = Text("телца — силен притисок", font_size=16, color=WHITE2)
        p_grp = VGroup(p_lbl, p_lbl_2).arrange(DOWN, buff=0.05)
        p_grp.next_to(pacinian, DOWN, buff=0.2)

        # Hot
        hot = Triangle(color=RED, fill_color=RED, fill_opacity=1).scale(0.25)
        hot.move_to(RIGHT*1 + UP*0.3)
        h_lbl = Text("Топлина", font_size=18, color=RED, weight=BOLD)
        h_lbl.next_to(hot, UP, buff=0.15)

        # Cold
        cold = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.25)
        cold.rotate(PI)
        cold.move_to(RIGHT*2.8 + UP*0.3)
        c_lbl = Text("Ладно", font_size=18, color=BLUE, weight=BOLD)
        c_lbl.next_to(cold, UP, buff=0.15)

        # Pain — free nerve endings (lines)
        pain_lines = VGroup(*[
            Line(RIGHT*4.5 + DOWN*0.5,
                 RIGHT*4.5 + DOWN*0.5 + np.array([np.cos(a)*0.4, np.sin(a)*0.4, 0]),
                 color=ORANGE, stroke_width=2.5)
            for a in np.linspace(0, 2*PI, 9)[:-1]
        ])
        pain_dot = Dot(RIGHT*4.5 + DOWN*0.5, color=ORANGE, radius=0.08)
        pain_grp = VGroup(pain_lines, pain_dot)
        pn_lbl = Text("Болка", font_size=18, color=ORANGE, weight=BOLD)
        pn_lbl_2 = Text("слободни нервни", font_size=14, color=WHITE2)
        pn_lbl_3 = Text("завршетоци", font_size=14, color=WHITE2)
        pn_grp = VGroup(pn_lbl, pn_lbl_2, pn_lbl_3).arrange(DOWN, buff=0.05)
        pn_grp.next_to(pain_grp, DOWN, buff=0.2)

        self.play(FadeIn(meissner), Write(m_grp), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(pacinian), Write(p_grp), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hot), Write(h_lbl),
                  FadeIn(cold), Write(c_lbl), run_time=0.8)
        self.wait(0.3)
        self.play(Create(pain_grp), Write(pn_grp), run_time=0.9)
        self.wait(1.2)

        line_finish = Text("Секој вид — свој рецептор.",
                           font_size=26, color=YELLOW, weight=BOLD)
        line_finish.to_edge(DOWN, buff=0.3)
        self.play(Write(line_finish), run_time=1.0)
        self.wait(1.5)

        recep_group = VGroup(skin_bg, surface, meissner, m_grp,
                             pacinian, p_grp, hot, h_lbl, cold, c_lbl,
                             pain_grp, pn_grp, line_finish)
        self.play(FadeOut(VGroup(title, recep_group)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 5.  ДЕМОНСТРАЦИЈА — допир                            ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("demo")

        title = section_title("Од допир до мозок", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        # finger
        finger = RoundedRectangle(width=0.6, height=1.4, corner_radius=0.3,
                                  fill_color="#e8c7a0", fill_opacity=1,
                                  stroke_color=WHITE2, stroke_width=2)
        finger.move_to(LEFT*5 + UP*1.5)

        # skin surface
        skin_line = Line(LEFT*5 + UP*0.3, LEFT*5 + DOWN*0.3,
                         color=YELLOW, stroke_width=3)
        receptor = Dot(LEFT*5 + UP*0, color=BLUE, radius=0.12)

        self.play(FadeIn(finger), Create(skin_line), FadeIn(receptor), run_time=0.8)

        # neuron path
        neuron_path = VMobject(color=GREEN, stroke_width=3)
        neuron_path.set_points_as_corners([
            LEFT*5,
            LEFT*3 + UP*0.5,
            LEFT*1 + UP*1,
            RIGHT*1 + UP*1.2,
            RIGHT*3.5 + UP*1.5,
        ])
        brain = Ellipse(width=1.6, height=1.2,
                        fill_color=PURPLE, fill_opacity=0.7,
                        stroke_color=WHITE2, stroke_width=2)
        brain.move_to(RIGHT*4.5 + UP*1.5)
        brain_lbl = Text("Мозок", font_size=22, color=WHITE2, weight=BOLD)
        brain_lbl.move_to(brain)

        self.play(Create(neuron_path), run_time=1.2)
        self.play(FadeIn(brain), Write(brain_lbl), run_time=0.7)

        # signal travels
        signal = Dot(LEFT*5, color=YELLOW, radius=0.15)
        self.play(MoveAlongPath(signal, neuron_path), run_time=1.5, rate_func=linear)
        self.play(Flash(brain.get_center(), color=YELLOW,
                        flash_radius=0.9, num_lines=14), run_time=0.6)
        self.wait(0.3)

        steps = VGroup(
            Text("1. Рецепторот регистрира.", font_size=22, color=BLUE),
            Text("2. Нервот пренесува.", font_size=22, color=GREEN),
            Text("3. Мозокот препознава.", font_size=22, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.to_edge(DOWN, buff=0.5).shift(LEFT*2)

        for s in steps:
            self.play(FadeIn(s, shift=RIGHT*0.2), run_time=0.5)
            self.wait(0.2)

        self.wait(1.5)
        demo_grp = VGroup(finger, skin_line, receptor, neuron_path,
                          brain, brain_lbl, signal, steps)
        self.play(FadeOut(VGroup(title, demo_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 6.  ЗАШТО Е ВАЖНО                                    ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        title = section_title("Зошто е важно?", color=ORANGE)
        self.play(Write(title), run_time=0.8)

        c1 = callout("Без болка — нема предупредување.",
                     border=RED, bg="#3a1010", font_size=28)
        c2 = callout("Без топлина — нема свест за оган.",
                     border=ORANGE, bg="#3a2510", font_size=28)
        c3 = callout("Без допир — нема прегратка.",
                     border=PURPLE, bg="#2a1a3a", font_size=28)

        callouts = VGroup(c1, c2, c3).arrange(DOWN, buff=0.35)
        callouts.move_to(ORIGIN + UP*0.1)

        for c in callouts:
            self.play(FadeIn(c, shift=UP*0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.0)
        self.play(FadeOut(VGroup(title, callouts)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  FINISHER                                         ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        f1 = Text("Кожата чувствува.",
                  font_size=44, color=YELLOW, weight=BOLD)
        f2 = Text("Кожата штити.",
                  font_size=44, color=GREEN, weight=BOLD)
        f3 = Text("Кожата зборува.",
                  font_size=44, color=PURPLE, weight=BOLD)
        f4 = Text("Слушај ја.",
                  font_size=54, color=ORANGE, weight=BOLD)

        block = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN)

        for line in [f1, f2, f3]:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)

        self.play(Write(f4), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(block), run_time=1.0)
        self.wait(0.5)
