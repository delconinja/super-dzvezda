"""
chem8-1-4  —  Дифузија
Хемија 8, Единица 1: Агрегатни состојби на материјата

Teaching narrative — Andonovski-style: three-beat punches,
parfumes/molecules as travellers, не...туку contrast.
Render:  manim -ql chem8-1-4.py Chem814Scene
Output:  media/videos/chem8-1-4/480p15/Chem814Scene.mp4
"""
from manim import *
import numpy as np
import random

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


class Chem814Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        # Room outline
        room = Rectangle(width=10.0, height=4.5,
                         fill_color=DARK_CARD, fill_opacity=0.5,
                         stroke_color=GREY, stroke_width=2).move_to(DOWN * 0.5)
        self.play(Create(room), run_time=0.8)

        # Perfume bottle in one corner
        bottle = RoundedRectangle(width=0.4, height=0.7, corner_radius=0.05,
                                  fill_color=PURPLE, fill_opacity=1,
                                  stroke_color=WHITE2, stroke_width=1.5)
        bottle.move_to(room.get_corner(DL) + UP * 0.55 + RIGHT * 0.5)
        bottle_lbl = Text("парфем", font_size=18, color=WHITE2).next_to(bottle, UP, buff=0.1)
        self.play(FadeIn(bottle), Write(bottle_lbl), run_time=0.7)

        hook1 = Text("Парфем во еден агол.",
                     font_size=38, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.5)
        self.play(Write(hook1), run_time=1.0)
        self.wait(0.4)

        # Molecules spreading from bottle
        random.seed(21)
        molecules = VGroup()
        for _ in range(35):
            m = Circle(radius=0.07, fill_color=PURPLE, fill_opacity=0.9,
                       stroke_width=0)
            m.move_to(bottle.get_top() + np.array([
                random.uniform(-0.1, 0.1),
                random.uniform(-0.05, 0.05), 0]))
            molecules.add(m)

        # Animate molecules dispersing into room
        target_positions = []
        for _ in molecules:
            target_positions.append(np.array([
                random.uniform(room.get_left()[0] + 0.3, room.get_right()[0] - 0.3),
                random.uniform(room.get_bottom()[1] + 0.3, room.get_top()[1] - 0.3),
                0,
            ]))

        self.play(FadeIn(molecules), run_time=0.5)
        self.play(*[m.animate.move_to(target_positions[i])
                    for i, m in enumerate(molecules)], run_time=2.2)
        self.wait(0.5)

        hook2 = Text("За момент — во цела соба.",
                     font_size=32, color=WHITE2)
        hook2.next_to(hook1, DOWN, buff=0.25)
        self.play(Write(hook2), run_time=1.0)

        hook3 = Text("Сам патува. Тоа е дифузија.",
                     font_size=34, color=GREEN, weight=BOLD)
        hook3.to_edge(DOWN, buff=0.3)
        self.play(Write(hook3), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(VGroup(room, bottle, bottle_lbl, molecules, hook1, hook2, hook3)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                       ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е дифузија?")
        self.play(Write(t2), run_time=0.9)

        defn = callout("Спонтано мешање на честици — од високо кон ниско.",
                       width=11.5, font_size=26)
        defn.next_to(t2, DOWN, buff=0.6)
        self.play(FadeIn(defn), run_time=0.8)
        self.wait(0.4)

        rhetq = Text("Кој ги носи? Никој.",
                     font_size=34, color=YELLOW)
        rhetq.next_to(defn, DOWN, buff=0.5)
        self.play(Write(rhetq), run_time=1.2)

        answer = Text("Топлинското движење ги тера.",
                      font_size=30, color=GREEN, weight=BOLD)
        answer.next_to(rhetq, DOWN, buff=0.35)
        self.play(Write(answer), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t2, defn, rhetq, answer)))

        # ══════════════════════════════════════════════════════════
        # 3.  БОЈА ВО ВОДА — ДЕМОНСТРАЦИЈА                     ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dye_in_water")

        t3 = section_title("Боја во вода")
        self.play(Write(t3), run_time=0.9)

        # Beaker
        beaker = VGroup(
            Line(LEFT * 2, LEFT * 2 + DOWN * 3, color=WHITE2, stroke_width=3),
            Line(LEFT * 2 + DOWN * 3, RIGHT * 2 + DOWN * 3, color=WHITE2, stroke_width=3),
            Line(RIGHT * 2 + DOWN * 3, RIGHT * 2, color=WHITE2, stroke_width=3),
        )
        beaker.move_to(DOWN * 0.4)
        # Water area
        water = Rectangle(width=3.9, height=2.9,
                          fill_color=BLUE, fill_opacity=0.2,
                          stroke_width=0).move_to(beaker.get_center() + DOWN * 0.05)
        self.play(FadeIn(water), Create(beaker), run_time=0.8)

        # Dye drop in center top
        dye_particles = VGroup()
        random.seed(31)
        for _ in range(28):
            p = Circle(radius=0.08, fill_color=RED, fill_opacity=0.9,
                       stroke_width=0)
            p.move_to(np.array([
                random.uniform(-0.2, 0.2),
                random.uniform(0.4, 0.7), 0]))
            dye_particles.add(p)

        self.play(FadeIn(dye_particles), run_time=0.5)

        # Spread the dye
        targets = []
        for _ in dye_particles:
            targets.append(np.array([
                random.uniform(-1.7, 1.7),
                random.uniform(-1.7, 0.8), 0]))
        self.play(*[p.animate.move_to(targets[i]).set_opacity(0.6)
                    for i, p in enumerate(dye_particles)], run_time=3.0)
        self.wait(0.5)

        cap = Text("Од концентрирано — кон разредено.",
                   font_size=26, color=YELLOW)
        cap.to_edge(DOWN, buff=0.3)
        self.play(Write(cap), run_time=1.3)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, beaker, water, dye_particles, cap)))

        # ══════════════════════════════════════════════════════════
        # 4.  СОСТОЈБИ — БРЗИНА НА ДИФУЗИЈА                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("speed_by_state")

        t4 = section_title("Колку брзо? Зависи од состојбата.")
        self.play(Write(t4), run_time=0.9)

        # Three cards
        def speed_card(state_name, speed_text, color, pos):
            card = RoundedRectangle(width=4.0, height=3.4, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=3).move_to(pos)
            title = Text(state_name, font_size=26, color=color, weight=BOLD)
            title.move_to(card.get_top() + DOWN * 0.5)
            speed = Text(speed_text, font_size=22, color=YELLOW, weight=BOLD)
            speed.move_to(card.get_center() + UP * 0.3)
            return VGroup(card, title, speed)

        c1 = speed_card("Гас", "НАЈБРЗО", ORANGE, LEFT * 4.6 + DOWN * 0.4)
        c2 = speed_card("Течно", "СРЕДНО", GREEN, DOWN * 0.4)
        c3 = speed_card("Цврсто", "НАЈБАВНО", BLUE, RIGHT * 4.6 + DOWN * 0.4)

        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.play(FadeIn(c3), run_time=0.6)

        # Small icon under each: speed examples
        ex1 = Text("секунди", font_size=20, color=WHITE2).move_to(c1[0].get_bottom() + UP * 0.4)
        ex2 = Text("минути", font_size=20, color=WHITE2).move_to(c2[0].get_bottom() + UP * 0.4)
        ex3 = Text("години", font_size=20, color=WHITE2).move_to(c3[0].get_bottom() + UP * 0.4)
        self.play(Write(ex1), Write(ex2), Write(ex3), run_time=0.9)
        self.wait(1.4)

        why = Text("Зошто? Простор + брзина.",
                   font_size=26, color=YELLOW)
        why.to_edge(DOWN, buff=0.35)
        self.play(Write(why), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t4, c1, c2, c3, ex1, ex2, ex3, why)))

        # ══════════════════════════════════════════════════════════
        # 5.  ГРАХАМОВ ЕКСПЕРИМЕНТ                             ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("graham")

        t5 = section_title("Грахамов експеримент")
        self.play(Write(t5), run_time=0.9)

        # Tube
        tube = Rectangle(width=9.0, height=0.9,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=2.5)
        tube.move_to(DOWN * 0.3)
        self.play(Create(tube), run_time=0.8)

        # NH3 (left, lighter)
        nh3_lbl = MathTex(r"\text{NH}_3", font_size=36, color=BLUE)
        nh3_lbl.move_to(tube.get_left() + LEFT * 0.6)
        nh3_sub = Text("полесен", font_size=18, color=BLUE).next_to(nh3_lbl, DOWN, buff=0.15)
        # HCl (right, heavier)
        hcl_lbl = MathTex(r"\text{HCl}", font_size=36, color=RED)
        hcl_lbl.move_to(tube.get_right() + RIGHT * 0.6)
        hcl_sub = Text("потежок", font_size=18, color=RED).next_to(hcl_lbl, DOWN, buff=0.15)

        self.play(Write(nh3_lbl), Write(nh3_sub), Write(hcl_lbl), Write(hcl_sub), run_time=0.9)

        # Particles spreading from each end
        nh3_p = VGroup()
        for _ in range(8):
            p = Circle(radius=0.1, fill_color=BLUE, fill_opacity=0.9, stroke_width=0)
            p.move_to(tube.get_left() + RIGHT * 0.3 + np.array([
                random.uniform(-0.1, 0.2),
                random.uniform(-0.3, 0.3), 0]))
            nh3_p.add(p)

        hcl_p = VGroup()
        for _ in range(8):
            p = Circle(radius=0.1, fill_color=RED, fill_opacity=0.9, stroke_width=0)
            p.move_to(tube.get_right() + LEFT * 0.3 + np.array([
                random.uniform(-0.2, 0.1),
                random.uniform(-0.3, 0.3), 0]))
            hcl_p.add(p)

        self.play(FadeIn(nh3_p), FadeIn(hcl_p), run_time=0.5)

        # NH3 moves further (lighter), HCl less
        # Meeting point is at ~1/3 from HCl side (closer to HCl since HCl is slower)
        meet_x = 1.2  # right of center, closer to HCl
        nh3_targets = [np.array([
            random.uniform(meet_x - 0.6, meet_x + 0.2),
            random.uniform(-0.3, 0.3), 0]) for _ in nh3_p]
        hcl_targets = [np.array([
            random.uniform(meet_x - 0.2, meet_x + 0.5),
            random.uniform(-0.3, 0.3), 0]) for _ in hcl_p]

        self.play(
            *[p.animate.move_to(nh3_targets[i]) for i, p in enumerate(nh3_p)],
            *[p.animate.move_to(hcl_targets[i]) for i, p in enumerate(hcl_p)],
            run_time=2.5,
        )

        # White ring (NH4Cl)
        ring = Circle(radius=0.5, fill_color=WHITE2, fill_opacity=0.6,
                      stroke_color=YELLOW, stroke_width=2).move_to(np.array([meet_x, -0.3, 0]))
        ring_lbl = MathTex(r"\text{NH}_4\text{Cl}", font_size=28, color=YELLOW)
        ring_lbl.next_to(ring, UP, buff=0.15)
        self.play(FadeIn(ring), Write(ring_lbl), run_time=0.9)
        self.wait(0.8)

        explain = Text("Полесните одат побрзо. Затоа се сретнуваат поблиску до HCl.",
                       font_size=22, color=YELLOW)
        explain.to_edge(DOWN, buff=0.35)
        self.play(Write(explain), run_time=1.6)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t5, tube, nh3_lbl, nh3_sub, hcl_lbl, hcl_sub,
                                  nh3_p, hcl_p, ring, ring_lbl, explain)))

        # ══════════════════════════════════════════════════════════
        # 6.  ВО ЖИВОТОТ                                       ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("life")

        t6 = section_title("Без дифузија — нема живот.", color=GREEN)
        self.play(Write(t6), run_time=1.0)

        items = VGroup(
            Text("Дишење:  O₂ од дробови во крв", font_size=24, color=BLUE),
            Text("Варење:  хранливи материи во крв", font_size=24, color=ORANGE),
            Text("Бубрези:  отпадоци во урината", font_size=24, color=YELLOW),
            Text("Растенија:  вода од почва во корени", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.move_to(ORIGIN)

        for it in items:
            self.play(Write(it), run_time=0.6)
        self.wait(1.5)

        line = Text("Невидлив транспорт. Постојан. Бесплатен.",
                    font_size=26, color=YELLOW, weight=BOLD)
        line.to_edge(DOWN, buff=0.35)
        self.play(Write(line), run_time=1.4)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t6, items, line)))

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни", color=GREEN)
        self.play(Write(t7), run_time=0.8)

        bullets = [
            (PURPLE, "Дифузија = спонтано мешање"),
            (YELLOW, "Од високо кон ниско концентрација"),
            (ORANGE, "Најбрза во гас, најбавна во цврсто"),
            (BLUE,   "Повисока T → побрза дифузија"),
            (GREEN,  "Полесни молекули → побрзо"),
            (RED,    "Дишење, варење, живот — сè дифузија"),
        ]
        bg = VGroup()
        for i, (c, txt) in enumerate(bullets):
            dot = Dot(color=c, radius=0.12)
            t = Text(txt, font_size=22, color=WHITE2)
            row = VGroup(dot, t).arrange(RIGHT, buff=0.3)
            row.move_to(np.array([0, 1.6 - i * 0.65, 0]))
            bg.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(1.6)

        final = Text("Никој не ги носи. Сами патуваат.",
                     font_size=32, color=YELLOW, weight=BOLD)
        final.to_edge(DOWN, buff=0.35)
        self.play(Write(final), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, bg, final)))
        self.wait(0.4)
