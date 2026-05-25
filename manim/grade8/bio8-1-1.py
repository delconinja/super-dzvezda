"""
bio8-1-1  —  Повторување за органски системи
Биологија 8, Единица 1: Сетила и нервна координација

Teaching narrative — Andonovski-style: three-beat punches,
body as story, organs as characters, life processes as drama.
Render:  manim -ql bio8-1-1.py Bio811Scene
Output:  media/videos/bio8-1-1/480p15/Bio811Scene.mp4
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


def system_card(icon_text, name, color, pos):
    box = RoundedRectangle(
        width=2.2, height=1.5, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    icon = Text(icon_text, font_size=36, color=color, weight=BOLD)
    icon.move_to(box.get_center() + UP * 0.3)
    label = Text(name, font_size=18, color=WHITE2)
    label.move_to(box.get_center() + DOWN * 0.35)
    return VGroup(box, icon, label)


class Bio811Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Не еден орган.",
                     font_size=46, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.4)
        self.wait(0.4)

        beats = VGroup(
            Text("Не два.", font_size=38, color=WHITE2),
            Text("Осум системи.", font_size=38, color=GREEN),
            Text("Сите работат истовремено.", font_size=34, color=ORANGE),
            Text("Сите за тебе.", font_size=36, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.0)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION                                      ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е органски систем?")
        self.play(Write(title), run_time=0.8)

        defn = callout(
            "Група органи кои заедно вршат една функција.",
            width=11.5, font_size=28, border=YELLOW,
        )
        defn.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.9)
        self.wait(0.8)

        # hierarchy chain
        chain_labels = ["Клетки", "Ткива", "Органи", "Системи", "Организам"]
        chain_colors = [BLUE, GREEN, YELLOW, ORANGE, RED]
        chain = VGroup()
        for i, (lbl, col) in enumerate(zip(chain_labels, chain_colors)):
            box = RoundedRectangle(
                width=1.9, height=0.9, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            t = Text(lbl, font_size=22, color=col, weight=BOLD).move_to(box)
            chain.add(VGroup(box, t))
        chain.arrange(RIGHT, buff=0.25).next_to(defn, DOWN, buff=0.8)

        arrows = VGroup()
        for i in range(len(chain) - 1):
            a = Arrow(
                chain[i].get_right(), chain[i + 1].get_left(),
                buff=0.05, color=WHITE2, stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            )
            arrows.add(a)

        for i, link in enumerate(chain):
            self.play(FadeIn(link, shift=RIGHT * 0.3), run_time=0.45)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.25)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, defn, chain, arrows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — 8 systems grid                      ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Осум главни системи")
        self.play(Write(title), run_time=0.8)

        # 4x2 grid of system cards
        systems = [
            ("CIRC", "Циркулаторен", RED),
            ("DIG",  "Дигестивен",   ORANGE),
            ("NRV",  "Нервен",       YELLOW),
            ("SKL",  "Скелетен",     WHITE2),
            ("MSC",  "Мускулен",     PURPLE),
            ("RSP",  "Респираторен", BLUE),
            ("EXC",  "Излачувачки",  GREEN),
            ("RPR",  "Репродуктивен", "#f48fb1"),
        ]

        cards = VGroup()
        for i, (icon, name, color) in enumerate(systems):
            row = i // 4
            col = i % 4
            x = -4.5 + col * 3.0
            y = 1.4 - row * 2.1
            cards.add(system_card(icon, name, color, [x, y, 0]))

        for c in cards:
            self.play(FadeIn(c, scale=0.9), run_time=0.28)
        self.wait(0.7)

        # highlight: all working simultaneously
        ring_anims = [
            Indicate(c, color=YELLOW, scale_factor=1.08) for c in cards
        ]
        self.play(*ring_anims, run_time=1.2)
        self.wait(0.5)

        all_label = Text("Сите истовремено. Сите за еден живот.",
                         font_size=28, color=YELLOW)
        all_label.to_edge(DOWN, buff=0.5)
        self.play(Write(all_label), run_time=0.9)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, cards, all_label)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — exercising body                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("При тркање")
        self.play(Write(title), run_time=0.8)

        steps = [
            ("Мускули", "Се движат коски.",            PURPLE),
            ("Дробови", "Внесуваат кислород.",         BLUE),
            ("Срце",    "Го носи до клетките.",        RED),
            ("Мозок",   "Координира сè.",              YELLOW),
        ]

        step_group = VGroup()
        for organ, action, col in steps:
            box = RoundedRectangle(
                width=10.5, height=0.85, corner_radius=0.18,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            o = Text(organ, font_size=26, color=col, weight=BOLD)
            o.move_to(box.get_left() + RIGHT * 1.4)
            a = Text(action, font_size=24, color=WHITE2)
            a.move_to(box.get_left() + RIGHT * 5.3)
            step_group.add(VGroup(box, o, a))
        step_group.arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.7)

        for s in step_group:
            self.play(FadeIn(s, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.8)

        concl = Text("Четири системи. Една акција.",
                     font_size=30, color=ORANGE, weight=BOLD)
        concl.to_edge(DOWN, buff=0.5)
        self.play(Write(concl), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, step_group, concl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — symptoms                           ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("Зошто учиш за системите?")
        self.play(Write(title), run_time=0.8)

        reasons = VGroup(
            callout("Препознаваш симптоми. Треска. Замор. Болка.",
                    width=11.5, border=RED, font_size=26),
            callout("Цениш зошто здраво јадеш и спиеш.",
                    width=11.5, border=GREEN, font_size=26),
            callout("Подготвен си за подлабоко учење.",
                    width=11.5, border=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.7)

        for r in reasons:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, reasons)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("8 системи. Никогаш сами.",
                 font_size=32, color=YELLOW, weight=BOLD),
            Text("Клетка → ткиво → орган → систем.",
                 font_size=28, color=WHITE2),
            Text("Заедно прават еден организам.",
                 font_size=28, color=BLUE),
            Text("Тебе.",
                 font_size=40, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.8)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
