"""
phys8-2-3  —  Енергијата во телото
Физика 8, Единица 2: Енергија

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-2-3.py Phys823Scene
Output:  media/videos/phys8-2-3/480p15/Phys823Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE      = "#4fc3f7"
YELLOW    = "#ffd54f"
GREEN     = "#81c784"
RED       = "#e57373"
GREY      = "#90a4ae"
ORANGE    = "#ffb74d"
PURPLE    = "#ce93d8"
WHITE2    = "#e8eaf0"
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


class Phys823Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Откаде добиваш енергија за да размислуваш?",
                    font_size=36, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)
        self.wait(0.8)

        chain_labels = ["Сонце", "Растение", "Јаболко", "Дигестија", "Глукоза", "АТП", "Движење"]
        chain_colors = [YELLOW, GREEN, GREEN, ORANGE, ORANGE, BLUE, RED]

        nodes = VGroup()
        for i, (lbl, col) in enumerate(zip(chain_labels, chain_colors)):
            circ = Circle(radius=0.36, fill_color=DARK_CARD, fill_opacity=1,
                          stroke_color=col, stroke_width=2.5)
            t = Text(lbl, font_size=16, color=col, weight=BOLD)
            t.move_to(circ)
            nodes.add(VGroup(circ, t))

        nodes.arrange(RIGHT, buff=0.55)
        nodes.shift(DOWN * 0.5)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            arr = Arrow(nodes[i].get_right(), nodes[i + 1].get_left(),
                        color=GREY, buff=0.05, stroke_width=2.5,
                        max_tip_length_to_length_ratio=0.25)
            arrows.add(arr)

        for node, arr in zip(nodes[:-1], arrows):
            self.play(FadeIn(node, shift=RIGHT * 0.2), GrowArrow(arr), run_time=0.4)
        self.play(FadeIn(nodes[-1], shift=RIGHT * 0.2), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(hook), FadeOut(nodes), FadeOut(arrows))

        # ══════════════════════════════════════════════════════════
        # 2.  КАЛОРИИ                                        ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("calories")

        hdr = section_title("Калории — мерка за хранлива енергија")
        self.play(Write(hdr), run_time=1.0)
        self.wait(0.5)

        kcal_box = callout(
            "1 kcal = 4 184 J   (=  1 Калорија / хранлива калорија)",
            width=10.5, bg="#0d2b44", border=YELLOW, font_size=26,
        )
        kcal_box.shift(UP * 1.5)
        self.play(FadeIn(kcal_box, shift=DOWN * 0.25))
        self.wait(0.8)

        daily_data = [
            ("Мажи",          "~2 500 kcal / ден", BLUE),
            ("Жени",          "~2 000 kcal / ден", PURPLE),
            ("Тинејџери",     "2 200–2 800 kcal / ден", GREEN),
        ]

        daily_cards = VGroup()
        for who, amount, col in daily_data:
            bg = RoundedRectangle(
                width=4.8, height=1.0, corner_radius=0.2,
                fill_color=f"{col}18", fill_opacity=1,
                stroke_color=col, stroke_width=1.5,
            )
            wt = Text(who, font_size=23, color=col, weight=BOLD)
            wt.next_to(bg.get_left(), RIGHT, buff=0.3)
            at = Text(amount, font_size=22, color=WHITE2)
            at.next_to(bg.get_right(), LEFT, buff=0.3)
            daily_cards.add(VGroup(bg, wt, at))

        daily_cards.arrange(DOWN, buff=0.28)
        daily_cards.shift(DOWN * 0.55)

        for card in daily_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.4)

        self.wait(1.5)
        self.play(FadeOut(hdr), FadeOut(kcal_box), FadeOut(daily_cards))

        # ══════════════════════════════════════════════════════════
        # 3.  МОЗОЧЕН ФАКТ                                   ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("brain")

        hdr2 = section_title("Мозокот — највредниот орган")
        self.play(Write(hdr2), run_time=0.9)

        brain_circle = Circle(radius=1.2, fill_color="#1f0b2b", fill_opacity=1,
                              stroke_color=PURPLE, stroke_width=3)
        brain_circle.shift(LEFT * 3.5 + DOWN * 0.5)

        pct_2 = Text("2%", font_size=54, color=PURPLE, weight=BOLD)
        pct_2.move_to(brain_circle).shift(UP * 0.25)
        lbl_mass = Text("маса", font_size=22, color=GREY)
        lbl_mass.next_to(pct_2, DOWN, buff=0.08)

        self.play(Create(brain_circle))
        self.play(Write(pct_2), Write(lbl_mass))
        self.wait(0.8)

        pct_20 = Text("20%", font_size=64, color=YELLOW, weight=BOLD)
        pct_20.shift(RIGHT * 1.5 + DOWN * 0.5)
        lbl_energy = Text("од сите калории", font_size=26, color=YELLOW)
        lbl_energy.next_to(pct_20, DOWN, buff=0.2)

        arrow_b = Arrow(brain_circle.get_right(), pct_20.get_left() + LEFT * 0.2,
                        color=GREY, buff=0.1, stroke_width=3)
        self.play(GrowArrow(arrow_b))
        self.play(Write(pct_20), Write(lbl_energy))
        self.play(Indicate(pct_20, scale_factor=1.2, color=YELLOW))
        self.wait(1.5)

        # Andonovski moment
        ando = Text(
            "Мозокот е 2% од тебе. Троши 20% од сè.\nУчењето е физичка работа.",
            font_size=26, color=WHITE2, weight=BOLD,
        )
        ando.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(ando, shift=UP * 0.2))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr2, brain_circle, pct_2, lbl_mass, pct_20, lbl_energy, arrow_b, ando,
        ]])

        # ══════════════════════════════════════════════════════════
        # 4.  ЕНЕРГЕТСКА РАМНОТЕЖА                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("balance")

        hdr3 = section_title("Енергетска рамнотежа")
        self.play(Write(hdr3), run_time=0.9)

        intake_box = callout("Внос > Потрошувачка → складирање (масти)",
                             width=10.0, bg="#0b2418", border=GREEN, font_size=25)
        intake_box.shift(UP * 1.2)
        self.play(FadeIn(intake_box, shift=DOWN * 0.2))
        self.wait(0.7)

        deficit_box = callout("Внос < Потрошувачка → губење на тежина",
                              width=10.0, bg="#2b0d0d", border=RED, font_size=25)
        deficit_box.next_to(intake_box, DOWN, buff=0.4)
        self.play(FadeIn(deficit_box, shift=DOWN * 0.2))
        self.wait(0.7)

        activity_data = [
            ("Спиење",  "60 kcal / час",  BLUE),
            ("Одење",   "250 kcal / час", GREEN),
            ("Трчање",  "500 kcal / час", RED),
        ]

        act_cards = VGroup()
        for act, cal, col in activity_data:
            bg = RoundedRectangle(
                width=4.6, height=0.9, corner_radius=0.18,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=1.5,
            )
            at = Text(act, font_size=22, color=col, weight=BOLD)
            at.next_to(bg.get_left(), RIGHT, buff=0.3)
            ct = Text(cal, font_size=21, color=WHITE2)
            ct.next_to(bg.get_right(), LEFT, buff=0.3)
            act_cards.add(VGroup(bg, at, ct))

        act_cards.arrange(RIGHT, buff=0.45)
        act_cards.next_to(deficit_box, DOWN, buff=0.5)

        for card in act_cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.45)
        self.wait(2.0)

        self.play(FadeOut(hdr3), FadeOut(intake_box), FadeOut(deficit_box),
                  FadeOut(act_cards))

        # ══════════════════════════════════════════════════════════
        # 5.  АНDONОВСКИ ФИНАЛЕ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Мозокот е 2% од тебе.",       WHITE2, 36),
            ("Троши 20% од сè.",            WHITE2, 36),
            ("Размислувај повеќе — трошиш повеќе.", WHITE2, 28),
            ("Учењето е физичка работа.",   YELLOW, 40),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.4)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.45)

        self.play(Indicate(grp[-1], scale_factor=1.2, color=YELLOW))
        self.wait(3.0)

        self.play(FadeOut(grp))

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЗИМЕ                                          ~8 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=44, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        bullets = [
            (YELLOW, "Сонце → растение → храна → глукоза → АТП → движење"),
            (ORANGE, "1 kcal = 4 184 J"),
            (PURPLE, "Мозок: 2% маса, 20% потрошувачка"),
            (GREEN,  "Внос = потрошувачка → стабилна тежина"),
            (RED,    "Трчање: ~500 kcal/h"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=23, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.shift(DOWN * 0.65 + RIGHT * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.5)
            self.wait(0.42)

        self.wait(3.0)
