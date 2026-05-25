"""
chem8-1-2  —  Промени на агрегатната состојба
Хемија 8, Единица 1: Агрегатни состојби на материјата

Teaching narrative — Andonovski-style: three-beat punches,
не...туку contrast, phase transitions as drama, one-word finishers.
Render:  manim -ql chem8-1-2.py Chem812Scene
Output:  media/videos/chem8-1-2/480p15/Chem812Scene.mp4
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


class Chem812Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        l1 = Text("Лед се топи.", font_size=44, color=BLUE, weight=BOLD)
        l2 = Text("Вода ври.", font_size=44, color=GREEN, weight=BOLD)
        l3 = Text("Пареа кондензира.", font_size=44, color=ORANGE, weight=BOLD)
        l4 = Text("Иста супстанца — три приказни.",
                  font_size=34, color=WHITE2)
        l5 = Text("Само температурата ги распраќа.",
                  font_size=34, color=YELLOW, weight=BOLD)

        stack = VGroup(l1, l2, l3, l4, l5).arrange(DOWN, buff=0.32)
        stack.move_to(ORIGIN)

        for ln in stack:
            self.play(Write(ln), run_time=0.7)
            self.wait(0.15)
        self.wait(1.6)

        self.play(FadeOut(stack))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА — ФИЗИЧКА ПРОМЕНА                    ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е промена на состојба?")
        self.play(Write(t2), run_time=0.9)

        defn = callout("Премин од една состојба во друга — со загревање или ладење.",
                       width=12.0, font_size=26)
        defn.next_to(t2, DOWN, buff=0.6)
        self.play(FadeIn(defn), run_time=0.8)

        sub = Text("Не нова материја. Туку само ново лице.",
                   font_size=30, color=YELLOW)
        sub.next_to(defn, DOWN, buff=0.5)
        self.play(Write(sub), run_time=1.3)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t2, defn, sub)))

        # ══════════════════════════════════════════════════════════
        # 3.  ШЕСТТЕ ПРОМЕНИ — ДИЈАГРАМ                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("six_transitions")

        t3 = section_title("Шест промени")
        self.play(Write(t3), run_time=0.8)

        # Three state nodes: solid (left), liquid (center), gas (right)
        def state_node(label, color, pos):
            circ = Circle(radius=0.85, fill_color=DARK_CARD, fill_opacity=1,
                          stroke_color=color, stroke_width=3).move_to(pos)
            lbl = Text(label, font_size=24, color=color, weight=BOLD)
            lbl.move_to(circ)
            return VGroup(circ, lbl)

        solid_node = state_node("Цврсто", BLUE, LEFT * 4.8 + DOWN * 0.5)
        liq_node = state_node("Течно", GREEN, DOWN * 0.5)
        gas_node = state_node("Гас", ORANGE, RIGHT * 4.8 + DOWN * 0.5)

        self.play(FadeIn(solid_node), FadeIn(liq_node), FadeIn(gas_node), run_time=0.9)

        # Arrows solid <-> liquid
        s2l = CurvedArrow(solid_node.get_right() + UP * 0.25,
                          liq_node.get_left() + UP * 0.25,
                          color=RED, angle=-0.5, stroke_width=3)
        l2s = CurvedArrow(liq_node.get_left() + DOWN * 0.25,
                          solid_node.get_right() + DOWN * 0.25,
                          color=BLUE, angle=-0.5, stroke_width=3)
        # Arrows liquid <-> gas
        l2g = CurvedArrow(liq_node.get_right() + UP * 0.25,
                          gas_node.get_left() + UP * 0.25,
                          color=RED, angle=-0.5, stroke_width=3)
        g2l = CurvedArrow(gas_node.get_left() + DOWN * 0.25,
                          liq_node.get_right() + DOWN * 0.25,
                          color=BLUE, angle=-0.5, stroke_width=3)

        # Labels
        s2l_lbl = Text("топење", font_size=18, color=RED).next_to(s2l, UP, buff=0.05)
        l2s_lbl = Text("замрзнување", font_size=18, color=BLUE).next_to(l2s, DOWN, buff=0.05)
        l2g_lbl = Text("испарување", font_size=18, color=RED).next_to(l2g, UP, buff=0.05)
        g2l_lbl = Text("кондензација", font_size=18, color=BLUE).next_to(g2l, DOWN, buff=0.05)

        self.play(Create(s2l), Write(s2l_lbl), run_time=0.7)
        self.play(Create(l2s), Write(l2s_lbl), run_time=0.7)
        self.play(Create(l2g), Write(l2g_lbl), run_time=0.7)
        self.play(Create(g2l), Write(g2l_lbl), run_time=0.7)
        self.wait(0.5)

        # Sublimation arc (solid -> gas, bypass)
        sub_arc = CurvedArrow(solid_node.get_top() + UP * 0.1,
                              gas_node.get_top() + UP * 0.1,
                              color=PURPLE, angle=-1.2, stroke_width=3)
        sub_lbl = Text("сублимација", font_size=18, color=PURPLE)
        sub_lbl.move_to(UP * 2.2)
        self.play(Create(sub_arc), Write(sub_lbl), run_time=0.9)

        # Desublimation arc (gas -> solid, bypass)
        des_arc = CurvedArrow(gas_node.get_bottom() + DOWN * 0.1,
                              solid_node.get_bottom() + DOWN * 0.1,
                              color=YELLOW, angle=-1.2, stroke_width=3)
        des_lbl = Text("десублимација", font_size=18, color=YELLOW)
        des_lbl.move_to(DOWN * 3.0)
        self.play(Create(des_arc), Write(des_lbl), run_time=0.9)
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            t3, solid_node, liq_node, gas_node,
            s2l, l2s, l2g, g2l, sub_arc, des_arc,
            s2l_lbl, l2s_lbl, l2g_lbl, g2l_lbl, sub_lbl, des_lbl,
        )))

        # ══════════════════════════════════════════════════════════
        # 4.  ТОПЕЊЕ — ЛЕД ВО ВОДА                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("melting")

        t4 = section_title("Топење", color=BLUE)
        self.play(Write(t4), run_time=0.8)

        # Ice cube on left, water on right, arrow
        ice = RoundedRectangle(width=2.0, height=1.6, corner_radius=0.15,
                               fill_color=BLUE, fill_opacity=0.7,
                               stroke_color=WHITE2, stroke_width=2).move_to(LEFT * 4)
        ice_lbl = Text("лед", font_size=22, color=WHITE2).next_to(ice, DOWN, buff=0.2)
        ice_t = Text("0°C", font_size=22, color=YELLOW).next_to(ice, UP, buff=0.2)

        water = VGroup()
        for i in range(20):
            d = Circle(radius=0.18, fill_color=BLUE, fill_opacity=0.7,
                       stroke_color=WHITE2, stroke_width=1).move_to(
                RIGHT * 4 + np.array([
                    random.uniform(-0.9, 0.9),
                    random.uniform(-0.7, 0.4), 0]))
            water.add(d)
        water_lbl = Text("вода", font_size=22, color=WHITE2).move_to(RIGHT * 4 + DOWN * 1.3)
        water_t = Text("0°C", font_size=22, color=YELLOW).move_to(RIGHT * 4 + UP * 1.3)

        arrow = Arrow(LEFT * 1.7, RIGHT * 1.7, color=RED, stroke_width=4, buff=0.1)
        arrow_lbl = Text("+ топлина", font_size=22, color=RED).next_to(arrow, UP, buff=0.15)

        self.play(FadeIn(ice), Write(ice_lbl), Write(ice_t), run_time=0.7)
        self.play(GrowArrow(arrow), Write(arrow_lbl), run_time=0.6)
        self.play(LaggedStartMap(FadeIn, water, lag_ratio=0.04), Write(water_lbl), Write(water_t), run_time=1.2)
        self.wait(0.6)

        info = callout("Истата температура и за топење и за замрзнување.",
                       width=10.5, font_size=24)
        info.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(info), run_time=0.7)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t4, ice, ice_lbl, ice_t, water, water_lbl, water_t,
                                  arrow, arrow_lbl, info)))

        # ══════════════════════════════════════════════════════════
        # 5.  ГРАФИКОН НА ЗАГРЕВАЊЕ                           ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("heating_curve")

        t5 = section_title("Графикон на загревање на вода")
        self.play(Write(t5), run_time=0.9)

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-20, 140, 20],
            x_length=9, y_length=4.5,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        )
        axes.move_to(DOWN * 0.3)
        x_lbl = Text("време", font_size=22, color=WHITE2).next_to(axes, DOWN, buff=0.2)
        y_lbl = Text("T (°C)", font_size=22, color=WHITE2).next_to(axes, LEFT, buff=0.2)
        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=1.0)

        # Segments
        # 1) -10 -> 0 (ice heating)
        p1 = axes.c2p(0, -10)
        p2 = axes.c2p(2, 0)
        # 2) plateau at 0 (melting)
        p3 = axes.c2p(4, 0)
        # 3) 0 -> 100 (water heating)
        p4 = axes.c2p(6.5, 100)
        # 4) plateau at 100 (boiling)
        p5 = axes.c2p(8.5, 100)
        # 5) above 100 (steam heating)
        p6 = axes.c2p(10, 130)

        seg1 = Line(p1, p2, color=BLUE, stroke_width=4)
        seg2 = Line(p2, p3, color=YELLOW, stroke_width=4)
        seg3 = Line(p3, p4, color=GREEN, stroke_width=4)
        seg4 = Line(p4, p5, color=YELLOW, stroke_width=4)
        seg5 = Line(p5, p6, color=ORANGE, stroke_width=4)

        self.play(Create(seg1), run_time=0.7)
        cap1 = Text("лед се загрева", font_size=18, color=BLUE).next_to(seg1, UP, buff=0.1)
        self.play(FadeIn(cap1), run_time=0.4)

        self.play(Create(seg2), run_time=0.7)
        cap2 = Text("топење (0°C)", font_size=18, color=YELLOW).next_to(seg2, UP, buff=0.1)
        self.play(FadeIn(cap2), run_time=0.4)

        self.play(Create(seg3), run_time=0.7)
        cap3 = Text("вода се загрева", font_size=18, color=GREEN).next_to(seg3, UP, buff=0.1)
        self.play(FadeIn(cap3), run_time=0.4)

        self.play(Create(seg4), run_time=0.7)
        cap4 = Text("врење (100°C)", font_size=18, color=YELLOW).next_to(seg4, UP, buff=0.1)
        self.play(FadeIn(cap4), run_time=0.4)

        self.play(Create(seg5), run_time=0.6)
        cap5 = Text("пареа", font_size=18, color=ORANGE).next_to(seg5, UP, buff=0.1)
        self.play(FadeIn(cap5), run_time=0.4)

        self.wait(1.0)

        plateau_note = Text(
            "Плато = промена. Температурата не се менува.",
            font_size=24, color=YELLOW,
        )
        plateau_note.to_edge(DOWN, buff=0.3)
        self.play(Write(plateau_note), run_time=1.4)
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            t5, axes, x_lbl, y_lbl,
            seg1, seg2, seg3, seg4, seg5,
            cap1, cap2, cap3, cap4, cap5,
            plateau_note,
        )))

        # ══════════════════════════════════════════════════════════
        # 6.  СУБЛИМАЦИЈА — СУВ МРАЗ                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sublimation")

        t6 = section_title("Сублимација — без течно", color=PURPLE)
        self.play(Write(t6), run_time=0.8)

        formula = MathTex(r"\text{CO}_2 \,(\text{цврст}) \;\longrightarrow\; \text{CO}_2 \,(\text{гас})",
                          font_size=42, color=WHITE2)
        formula.move_to(UP * 0.8)
        self.play(Write(formula), run_time=1.2)

        info = callout("Сув мраз — премин директно во гас. Без минување низ течно.",
                       width=11.5, font_size=24, border=PURPLE)
        info.next_to(formula, DOWN, buff=0.6)
        self.play(FadeIn(info), run_time=0.8)

        examples = Text("Иње на прозорец. Снег во студен ден. Сув мраз.",
                        font_size=24, color=YELLOW)
        examples.next_to(info, DOWN, buff=0.4)
        self.play(Write(examples), run_time=1.3)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t6, formula, info, examples)))

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни", color=GREEN)
        self.play(Write(t7), run_time=0.8)

        bullets = [
            (BLUE,   "Топење: цврсто → течно"),
            (GREEN,  "Замрзнување: течно → цврсто"),
            (ORANGE, "Испарување: течно → гас"),
            (RED,    "Кондензација: гас → течно"),
            (PURPLE, "Сублимација: цврсто → гас (прескок)"),
            (YELLOW, "Платото = промена, не загревање"),
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

        final = Text("Иста супстанца. Само облик се менува.",
                     font_size=32, color=YELLOW, weight=BOLD)
        final.to_edge(DOWN, buff=0.35)
        self.play(Write(final), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, bg, final)))
        self.wait(0.4)
