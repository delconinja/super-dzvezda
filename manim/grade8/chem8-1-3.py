"""
chem8-1-3  —  Гасен притисок
Хемија 8, Единица 1: Агрегатни состојби на материјата

Teaching narrative — Andonovski-style: three-beat punches,
particles bombarding walls as drama, не...туку contrast.
Render:  manim -ql chem8-1-3.py Chem813Scene
Output:  media/videos/chem8-1-3/480p15/Chem813Scene.mp4
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


def gas_box(center, w=4.0, h=3.0):
    return Rectangle(width=w, height=h,
                     fill_color=DARK_CARD, fill_opacity=1,
                     stroke_color=WHITE2, stroke_width=2.5).move_to(center)


class Chem813Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        l1 = Text("Гасот удира во ѕидот.",
                  font_size=44, color=YELLOW, weight=BOLD)
        l2 = Text("Милијарди удари во секунда.",
                  font_size=36, color=WHITE2)
        l3 = Text("Тоа е притисок.",
                  font_size=44, color=ORANGE, weight=BOLD)
        l4 = Text("Невидлива сила. Постојана.",
                  font_size=34, color=GREEN, weight=BOLD)

        stack = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.4)
        stack.move_to(ORIGIN)

        for ln in stack:
            self.play(Write(ln), run_time=0.8)
            self.wait(0.2)
        self.wait(1.4)

        self.play(FadeOut(stack))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА + БОКС СО ЧЕСТИЦИ                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition_visual")

        t2 = section_title("Што е гасен притисок?")
        self.play(Write(t2), run_time=0.9)

        defn = callout("Сила со која честиците удираат во ѕидовите на садот.",
                       width=11.5, font_size=26)
        defn.next_to(t2, DOWN, buff=0.5)
        self.play(FadeIn(defn), run_time=0.8)

        # Box with bouncing particles
        box = gas_box(DOWN * 0.6, w=6.0, h=3.4)
        self.play(Create(box), run_time=0.7)

        random.seed(13)
        particles = VGroup()
        velocities = []
        for _ in range(12):
            p = Circle(radius=0.14, fill_color=ORANGE, fill_opacity=1,
                       stroke_color=WHITE2, stroke_width=1)
            p.move_to(box.get_center() + np.array([
                random.uniform(-2.5, 2.5),
                random.uniform(-1.3, 1.3), 0]))
            particles.add(p)
            v = np.array([
                random.uniform(-2.5, 2.5),
                random.uniform(-2.0, 2.0), 0])
            velocities.append(v)

        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.05), run_time=0.9)

        # Simple bouncing animation using updaters
        box_center = box.get_center()
        half_w = 3.0 - 0.18
        half_h = 1.7 - 0.18

        def make_updater(idx):
            def upd(mob, dt):
                v = velocities[idx]
                mob.shift(v * dt)
                pos = mob.get_center() - box_center
                if abs(pos[0]) > half_w:
                    velocities[idx][0] *= -1
                    mob.shift(np.array([-pos[0] + np.sign(pos[0]) * half_w, 0, 0]))
                if abs(pos[1]) > half_h:
                    velocities[idx][1] *= -1
                    mob.shift(np.array([0, -pos[1] + np.sign(pos[1]) * half_h, 0]))
            return upd

        for i, p in enumerate(particles):
            p.add_updater(make_updater(i))

        self.wait(4.0)

        for p in particles:
            p.clear_updaters()

        # Pressure arrows on walls
        arr_left = Arrow(box.get_left() + LEFT * 0.6, box.get_left() + RIGHT * 0.1,
                         color=RED, stroke_width=4, buff=0)
        arr_right = Arrow(box.get_right() + RIGHT * 0.6, box.get_right() + LEFT * 0.1,
                          color=RED, stroke_width=4, buff=0)
        arr_top = Arrow(box.get_top() + UP * 0.6, box.get_top() + DOWN * 0.1,
                        color=RED, stroke_width=4, buff=0)
        arr_bot = Arrow(box.get_bottom() + DOWN * 0.6, box.get_bottom() + UP * 0.1,
                        color=RED, stroke_width=4, buff=0)

        self.play(GrowArrow(arr_left), GrowArrow(arr_right),
                  GrowArrow(arr_top), GrowArrow(arr_bot), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t2, defn, box, particles,
                                  arr_left, arr_right, arr_top, arr_bot)))

        # ══════════════════════════════════════════════════════════
        # 3.  ТРИ ФАКТОРИ                                      ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("factors")

        t3 = section_title("Три фактори. Три причини.")
        self.play(Write(t3), run_time=0.9)

        # Three columns
        def factor_card(num, title_text, body_text, color, pos):
            card = RoundedRectangle(width=4.0, height=3.6, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=3).move_to(pos)
            n = Text(num, font_size=36, color=color, weight=BOLD)
            n.move_to(card.get_top() + DOWN * 0.5)
            title = Text(title_text, font_size=22, color=YELLOW, weight=BOLD)
            title.move_to(card.get_top() + DOWN * 1.1)
            body = Text(body_text, font_size=18, color=WHITE2)
            body.move_to(card.get_center() + DOWN * 0.4)
            return VGroup(card, n, title, body)

        f1 = factor_card("1", "Број на честици", "Повеќе честици\nповеќе удари",
                         BLUE, LEFT * 4.6 + DOWN * 0.4)
        f2 = factor_card("2", "Температура", "Побрзи честици\nпосилни удари",
                         ORANGE, DOWN * 0.4)
        f3 = factor_card("3", "Обем", "Помал сад\nпочести удари",
                         GREEN, RIGHT * 4.6 + DOWN * 0.4)

        self.play(FadeIn(f1), run_time=0.7)
        self.play(FadeIn(f2), run_time=0.7)
        self.play(FadeIn(f3), run_time=0.7)
        self.wait(2.5)

        warn = Text("На жега — гумата на велосипед експлодира.",
                    font_size=24, color=RED)
        warn.to_edge(DOWN, buff=0.35)
        self.play(Write(warn), run_time=1.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, f1, f2, f3, warn)))

        # ══════════════════════════════════════════════════════════
        # 4.  БОУЛЕВ ЗАКОН                                     ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("boyle")

        t4 = section_title("Боулев закон")
        self.play(Write(t4), run_time=0.9)

        formula = MathTex(r"P \times V = \text{константа}",
                          font_size=56, color=YELLOW)
        formula.move_to(UP * 1.8)
        self.play(Write(formula), run_time=1.2)

        sub = Text("Притисок и обем — обратно пропорционални.",
                   font_size=24, color=WHITE2)
        sub.next_to(formula, DOWN, buff=0.4)
        self.play(Write(sub), run_time=1.0)

        # Syringe example: three stages
        stages = VGroup()
        for i, (V, P, color) in enumerate([(100, 1, BLUE), (50, 2, GREEN), (25, 4, RED)]):
            card = RoundedRectangle(width=3.4, height=2.0, corner_radius=0.2,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            card.move_to(np.array([-4.5 + i * 4.5, -1.7, 0]))
            v_txt = Text(f"V = {V} ml", font_size=22, color=WHITE2)
            p_txt = Text(f"P = {P} bar", font_size=22, color=color, weight=BOLD)
            stack = VGroup(v_txt, p_txt).arrange(DOWN, buff=0.2)
            stack.move_to(card)
            stages.add(VGroup(card, stack))

        for s in stages:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.6)

        self.wait(2.0)

        punch = Text("Половина обем. Двоен притисок.",
                     font_size=26, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.25)
        self.play(Write(punch), run_time=1.3)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t4, formula, sub, stages, punch)))

        # ══════════════════════════════════════════════════════════
        # 5.  ГАЈ-ЛУСАКОВ ЗАКОН                                ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("gay_lussac")

        t5 = section_title("Гај-Лусаков закон")
        self.play(Write(t5), run_time=0.9)

        formula2 = MathTex(r"\frac{P}{T} = \text{константа}",
                           font_size=56, color=ORANGE)
        formula2.move_to(UP * 1.5)
        self.play(Write(formula2), run_time=1.2)

        sub2 = Text("Притисок и температура — директно пропорционални.",
                    font_size=24, color=WHITE2)
        sub2.next_to(formula2, DOWN, buff=0.4)
        self.play(Write(sub2), run_time=1.0)

        example = VGroup(
            Text("Шише на 0°C (273 K)  →  P = 1 bar", font_size=24, color=BLUE),
            Text("Шише на 273°C (546 K)  →  P = 2 bar", font_size=24, color=RED),
        ).arrange(DOWN, buff=0.3)
        example.move_to(DOWN * 1.2)
        self.play(Write(example[0]), run_time=0.8)
        self.play(Write(example[1]), run_time=0.8)
        self.wait(1.2)

        warn = Text("Никогаш не загревај затворено шише!",
                    font_size=28, color=RED, weight=BOLD)
        warn.to_edge(DOWN, buff=0.3)
        self.play(Write(warn), run_time=1.3)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t5, formula2, sub2, example, warn)))

        # ══════════════════════════════════════════════════════════
        # 6.  АТМОСФЕРСКИ ПРИТИСОК                             ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("atmosphere")

        t6 = section_title("Атмосферскиот притисок", color=BLUE)
        self.play(Write(t6), run_time=0.9)

        defn = Text("Тежината на воздухот над нас.",
                    font_size=30, color=WHITE2)
        defn.move_to(UP * 1.5)
        self.play(Write(defn), run_time=1.0)

        rows = VGroup(
            Text("Ниво на море:     ~ 1 bar (101 325 Pa)", font_size=24, color=BLUE),
            Text("Височина 5000 m:  ~ 0.5 bar", font_size=24, color=YELLOW),
            Text("Врв на Еверест:   ~ 0.3 bar", font_size=24, color=RED),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rows.move_to(ORIGIN)
        for r in rows:
            self.play(Write(r), run_time=0.7)
        self.wait(1.0)

        ear = Text("Зато ушите ни „пукаат\" во авион.",
                   font_size=26, color=YELLOW)
        ear.to_edge(DOWN, buff=0.35)
        self.play(Write(ear), run_time=1.3)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t6, defn, rows, ear)))

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни", color=GREEN)
        self.play(Write(t7), run_time=0.8)

        bullets = [
            (BLUE,   "Притисок = удари по ѕид"),
            (ORANGE, "Повеќе честици → повеќе притисок"),
            (RED,    "Повисока T → повеќе притисок"),
            (GREEN,  "Помал обем → повеќе притисок"),
            (YELLOW, "P × V = константа (Боул)"),
            (PURPLE, "P / T = константа (Гај-Лусак)"),
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

        final = Text("Невидливо. Но мерливо.",
                     font_size=34, color=YELLOW, weight=BOLD)
        final.to_edge(DOWN, buff=0.35)
        self.play(Write(final), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, bg, final)))
        self.wait(0.4)
