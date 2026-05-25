"""
bio8-1-5  —  Рецептори за звук — увото
Биологија 8, Единица 1: Сетила и нервна координација

Teaching narrative — Andonovski-style: three-beat punches,
ear as theatre, ossicles as the smallest heroes, silence as enemy.
Render:  manim -ql bio8-1-5.py Bio815Scene
Output:  media/videos/bio8-1-5/480p15/Bio815Scene.mp4
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


class Bio815Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Три коски.",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.4)
        self.wait(0.3)

        beats = VGroup(
            Text("Како зрно ориз.",            font_size=38, color=WHITE2),
            Text("Најмалите во телото.",       font_size=36, color=BLUE),
            Text("Без нив — тишина.",          font_size=36, color=GREY),
            Text("Без тишина — нема звук.",    font_size=36, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — three parts of the ear             ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Три дела на увото")
        self.play(Write(title), run_time=0.8)

        # outer ear (curl on left)
        outer_ear = VMobject(stroke_color=WHITE2, stroke_width=3)
        outer_pts = [
            LEFT * 5.5 + UP * 1.2,
            LEFT * 5.0 + UP * 1.6,
            LEFT * 4.0 + UP * 1.7,
            LEFT * 3.3 + UP * 1.0,
            LEFT * 3.5 + DOWN * 0.0,
            LEFT * 4.5 + DOWN * 1.0,
            LEFT * 5.5 + DOWN * 0.8,
            LEFT * 5.7 + UP * 0.0,
            LEFT * 5.5 + UP * 1.2,
        ]
        outer_ear.set_points_smoothly(outer_pts)

        # ear canal (tube from outer to eardrum)
        canal = Rectangle(width=2.5, height=0.5,
                          stroke_color=WHITE2, stroke_width=2.5,
                          fill_opacity=0)
        canal.shift(LEFT * 1.8 + DOWN * 0.0)

        # eardrum (vertical line at right end of canal)
        eardrum = Line(canal.get_right() + UP * 0.25,
                       canal.get_right() + DOWN * 0.25,
                       color=ORANGE, stroke_width=5)

        # ossicles (3 small shapes)
        os1 = Polygon([0, 0, 0], [0.15, 0.4, 0], [-0.15, 0.4, 0],
                      fill_color=YELLOW, fill_opacity=1, stroke_width=1)
        os1.next_to(eardrum, RIGHT, buff=0.2)
        os2 = Polygon([0, 0, 0], [0.2, 0.3, 0], [0.0, 0.5, 0], [-0.2, 0.3, 0],
                      fill_color=YELLOW, fill_opacity=1, stroke_width=1)
        os2.next_to(os1, RIGHT, buff=0.1)
        os3 = RoundedRectangle(width=0.3, height=0.45, corner_radius=0.08,
                               fill_color=YELLOW, fill_opacity=1, stroke_width=1)
        os3.next_to(os2, RIGHT, buff=0.1)
        ossicles = VGroup(os1, os2, os3)
        ossicles.shift(DOWN * 0.2)

        # cochlea (spiral)
        cochlea = ParametricFunction(
            lambda t: np.array([
                0.5 * np.exp(-0.15 * t) * np.cos(t),
                0.5 * np.exp(-0.15 * t) * np.sin(t),
                0,
            ]),
            t_range=[0, 4 * PI],
            color=GREEN, stroke_width=4,
        )
        cochlea.move_to(RIGHT * 3.0 + DOWN * 0.0)

        # auditory nerve
        aud_nerve = Line(cochlea.get_right(),
                         cochlea.get_right() + RIGHT * 1.3,
                         color=PURPLE, stroke_width=5)

        self.play(Create(outer_ear), run_time=1.0)
        self.play(Create(canal), Create(eardrum), run_time=0.8)
        self.play(FadeIn(ossicles), run_time=0.7)
        self.play(Create(cochlea), run_time=1.0)
        self.play(Create(aud_nerve), run_time=0.4)

        # 3 zone brackets above
        z1 = Brace(VGroup(outer_ear, eardrum), UP, buff=0.3, color=BLUE)
        z1_lbl = z1.get_text("Надворешно").set_color(BLUE)
        z1_lbl.set_font_size(22)

        z2 = Brace(ossicles, UP, buff=0.3, color=YELLOW)
        z2_lbl = z2.get_text("Средно").set_color(YELLOW)
        z2_lbl.set_font_size(22)

        z3 = Brace(VGroup(cochlea, aud_nerve), UP, buff=0.3, color=GREEN)
        z3_lbl = z3.get_text("Внатрешно").set_color(GREEN)
        z3_lbl.set_font_size(22)

        self.play(GrowFromCenter(z1), FadeIn(z1_lbl), run_time=0.6)
        self.play(GrowFromCenter(z2), FadeIn(z2_lbl), run_time=0.6)
        self.play(GrowFromCenter(z3), FadeIn(z3_lbl), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, outer_ear, canal, eardrum, ossicles, cochlea, aud_nerve,
            z1, z1_lbl, z2, z2_lbl, z3, z3_lbl,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — ossicles close-up                   ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Три коски — три имиња")
        self.play(Write(title), run_time=0.8)

        # bigger ossicles for the close-up
        m1 = Polygon([-0.3, 0, 0], [0.3, 0, 0], [0, 1.4, 0],
                     fill_color=YELLOW, fill_opacity=1,
                     stroke_color=WHITE2, stroke_width=2)
        m1.shift(LEFT * 3.7 + DOWN * 0.3)
        m1_lbl = Text("Чеканче", font_size=24, color=YELLOW, weight=BOLD)
        m1_lbl.next_to(m1, DOWN, buff=0.5)
        m1_sub = Text("malleus", font_size=18, color=GREY)
        m1_sub.next_to(m1_lbl, DOWN, buff=0.1)

        m2 = Polygon([-0.4, 0, 0], [0.4, 0.2, 0], [0.2, 1.2, 0], [-0.2, 1.0, 0],
                     fill_color=ORANGE, fill_opacity=1,
                     stroke_color=WHITE2, stroke_width=2)
        m2.shift(DOWN * 0.3)
        m2_lbl = Text("Наковалче", font_size=24, color=ORANGE, weight=BOLD)
        m2_lbl.next_to(m2, DOWN, buff=0.5)
        m2_sub = Text("incus", font_size=18, color=GREY)
        m2_sub.next_to(m2_lbl, DOWN, buff=0.1)

        m3 = VGroup(
            RoundedRectangle(width=0.5, height=0.9, corner_radius=0.2,
                             fill_color=RED, fill_opacity=1,
                             stroke_color=WHITE2, stroke_width=2),
            Rectangle(width=0.2, height=0.3, fill_color=DARK_CARD,
                      fill_opacity=1, stroke_color=WHITE2, stroke_width=1.5),
        )
        m3.shift(RIGHT * 3.7 + DOWN * 0.3)
        m3_lbl = Text("Узенгија", font_size=24, color=RED, weight=BOLD)
        m3_lbl.next_to(m3, DOWN, buff=0.5)
        m3_sub = Text("stapes", font_size=18, color=GREY)
        m3_sub.next_to(m3_lbl, DOWN, buff=0.1)

        # rice grain for scale
        rice = Ellipse(width=0.45, height=0.2,
                       fill_color="#fff9c4", fill_opacity=1,
                       stroke_color=WHITE2, stroke_width=1.5)
        rice.shift(UP * 2.3)
        rice_lbl = Text("Зрно ориз — за споредба",
                        font_size=22, color=WHITE2)
        rice_lbl.next_to(rice, RIGHT, buff=0.3)

        self.play(FadeIn(m1, shift=UP * 0.2), FadeIn(m1_lbl), FadeIn(m1_sub), run_time=0.8)
        self.play(FadeIn(m2, shift=UP * 0.2), FadeIn(m2_lbl), FadeIn(m2_sub), run_time=0.8)
        self.play(FadeIn(m3, shift=UP * 0.2), FadeIn(m3_lbl), FadeIn(m3_sub), run_time=0.8)
        self.wait(0.5)

        self.play(FadeIn(rice, shift=DOWN * 0.2), FadeIn(rice_lbl), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, m1, m1_lbl, m1_sub, m2, m2_lbl, m2_sub,
            m3, m3_lbl, m3_sub, rice, rice_lbl,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — sound pathway                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Како слушаш — седум чекори")
        self.play(Write(title), run_time=0.8)

        steps = [
            ("1", "Звучен бран влегува во каналот.", BLUE),
            ("2", "Тапанчето вибрира.",              ORANGE),
            ("3", "Трите коски засилуваат.",         YELLOW),
            ("4", "Течноста во полжавот вибрира.",   GREEN),
            ("5", "Влакна-клетки се активираат.",    PURPLE),
            ("6", "Слухов нерв носи сигнал.",        RED),
            ("7", "Мозокот толкува звук.",           WHITE2),
        ]

        step_group = VGroup()
        for num, txt, col in steps:
            box = RoundedRectangle(
                width=10.5, height=0.62, corner_radius=0.13,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(num, font_size=24, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 0.5)
            t = Text(txt, font_size=22, color=WHITE2)
            t.move_to(box.get_left() + RIGHT * 5.0)
            step_group.add(VGroup(box, n, t))
        step_group.arrange(DOWN, buff=0.15).next_to(title, DOWN, buff=0.4)

        for s in step_group:
            self.play(FadeIn(s, shift=LEFT * 0.3), run_time=0.45)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, step_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — frequency range & protection       ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("20 Hz — 20 000 Hz")
        self.play(Write(title), run_time=0.8)

        # frequency bar
        bar_low = Rectangle(width=2.0, height=0.9,
                            fill_color=BLUE, fill_opacity=1, stroke_width=0)
        bar_mid = Rectangle(width=5.0, height=0.9,
                            fill_color=GREEN, fill_opacity=1, stroke_width=0)
        bar_high = Rectangle(width=2.5, height=0.9,
                             fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        bar_low.next_to(bar_mid, LEFT, buff=0)
        bar_high.next_to(bar_mid, RIGHT, buff=0)
        bar = VGroup(bar_low, bar_mid, bar_high)
        bar.move_to(UP * 1.5)

        low_lbl = Text("20 Hz", font_size=22, color=BLUE).next_to(bar_low, DOWN, buff=0.2)
        mid_lbl = Text("слушливо", font_size=22, color="#0d1b2e", weight=BOLD).move_to(bar_mid)
        high_lbl = Text("20 kHz", font_size=22, color=YELLOW).next_to(bar_high, DOWN, buff=0.2)

        self.play(Create(bar), run_time=0.9)
        self.play(FadeIn(low_lbl), FadeIn(mid_lbl), FadeIn(high_lbl), run_time=0.6)
        self.wait(0.6)

        # protection callouts
        warn1 = callout(
            "Над 85 dB долготрајно — уништува влакна-клетки.",
            width=11.5, border=RED, font_size=24,
        )
        warn1.shift(DOWN * 0.5)
        warn2 = callout(
            "Влакна-клетки НЕ растат повторно.",
            width=11.5, border=ORANGE, font_size=26,
        )
        warn2.next_to(warn1, DOWN, buff=0.3)
        warn3 = callout(
            "Заштити го слухот. Денес. Засекогаш.",
            width=11.5, border=GREEN, font_size=26,
        )
        warn3.next_to(warn2, DOWN, buff=0.3)

        self.play(FadeIn(warn1, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(warn2, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(warn3, shift=UP * 0.2), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, bar, low_lbl, mid_lbl, high_lbl, warn1, warn2, warn3,
        )), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Три дела: надворешно, средно, внатрешно.",
                 font_size=28, color=YELLOW, weight=BOLD),
            Text("Три коски — најмали во телото.",
                 font_size=28, color=ORANGE, weight=BOLD),
            Text("Полжав претвора вибрации во сигнал.",
                 font_size=26, color=GREEN),
            Text("Полукружни канали држат рамнотежа.",
                 font_size=26, color=BLUE),
            Text("Чувај го слухот. Молкум.",
                 font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.6)

        for b in bullets:
            self.play(Write(b), run_time=0.65)
            self.wait(0.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
