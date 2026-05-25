"""
geo8-7-2  —  Украина, Белорусија и Молдавија
Географија 8, Единица 7: Источна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as siblings of one fallen empire.
Render:  manim -ql geo8-7-2.py Geo872Scene
Output:  media/videos/geo8-7-2/480p15/Geo872Scene.mp4
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


def country_panel(name, capital, color, pos, w=3.6, h=3.4):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=3,
    ).move_to(pos)
    nm = Text(name, font_size=28, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * (h / 2 - 0.4))
    cap = Text(capital, font_size=20, color=WHITE2)
    cap.next_to(nm, DOWN, buff=0.15)
    return VGroup(box, nm, cap)


def stat_line(label, value, color, fs=20):
    lbl = Text(label, font_size=fs, color=GREY)
    val = Text(value, font_size=fs, color=color, weight=BOLD)
    return VGroup(lbl, val).arrange(RIGHT, buff=0.3)


class Geo872Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — три бивши Советски                     ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Три држави.", font_size=56, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.6)
        self.play(Write(h1), run_time=1.0)
        self.wait(0.2)

        beats = VGroup(
            Text("Сите бивши Советски.", font_size=42, color=ORANGE, weight=BOLD),
            Text("Сите се борат —", font_size=36, color=BLUE),
            Text("со историја, со соседи, со иднина.", font_size=32, color=PURPLE),
            Text("Молдавија молчи.", font_size=36, color=GREEN, weight=BOLD),
            Text("Белорусија чека.", font_size=36, color=GREY, weight=BOLD),
            Text("Украина се брани.", font_size=40, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.28).next_to(h1, DOWN, buff=0.4)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(1.0)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  МАПА — каде се наоѓаат                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mapa")

        title = section_title("Каде се наоѓаат", color=BLUE)
        self.play(FadeIn(title), run_time=0.6)

        # Russia big mass right
        russia = RoundedRectangle(width=4.5, height=4.5, corner_radius=0.2,
                                  fill_color="#3a2030", fill_opacity=0.7,
                                  stroke_color=RED, stroke_width=2).shift(RIGHT * 3.8 + DOWN * 0.3)
        russia_lbl = Text("Русија", font_size=26, color=WHITE2, weight=BOLD).move_to(russia)

        # Belarus
        belarus = RoundedRectangle(width=2.4, height=2.0, corner_radius=0.2,
                                   fill_color=GREEN, fill_opacity=0.5,
                                   stroke_color=GREEN, stroke_width=2).shift(LEFT * 0.5 + UP * 1.6)
        belarus_lbl = Text("Белорусија", font_size=18, color=WHITE2, weight=BOLD).move_to(belarus)

        # Ukraine
        ukraine = RoundedRectangle(width=4.0, height=2.5, corner_radius=0.2,
                                   fill_color=BLUE, fill_opacity=0.5,
                                   stroke_color=YELLOW, stroke_width=2).shift(LEFT * 1.0 + DOWN * 0.6)
        ukraine_lbl = Text("Украина", font_size=22, color=WHITE2, weight=BOLD).move_to(ukraine)

        # Moldova (small)
        moldova = RoundedRectangle(width=1.0, height=1.4, corner_radius=0.15,
                                   fill_color=PURPLE, fill_opacity=0.5,
                                   stroke_color=PURPLE, stroke_width=2).shift(LEFT * 2.8 + DOWN * 1.6)
        moldova_lbl = Text("Молд.", font_size=14, color=WHITE2, weight=BOLD).move_to(moldova)

        # EU border left
        eu = DashedLine(LEFT * 5.5 + UP * 2.5, LEFT * 5.5 + DOWN * 2.5,
                        stroke_color=BLUE, stroke_width=3).shift(LEFT * 0.3)
        eu_lbl = Text("ЕУ", font_size=22, color=BLUE, weight=BOLD).next_to(eu, UP, buff=0.2)

        self.play(FadeIn(russia), Write(russia_lbl), run_time=0.7)
        self.play(FadeIn(belarus), Write(belarus_lbl), run_time=0.6)
        self.play(FadeIn(ukraine), Write(ukraine_lbl), run_time=0.6)
        self.play(FadeIn(moldova), Write(moldova_lbl), run_time=0.6)
        self.play(Create(eu), Write(eu_lbl), run_time=0.7)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title, russia, russia_lbl, belarus, belarus_lbl,
                                  ukraine, ukraine_lbl, moldova, moldova_lbl, eu, eu_lbl)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  УКРАИНА — житница на Европа                   ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ukraina")

        title2 = section_title("Украина", color=YELLOW)
        self.play(FadeIn(title2), run_time=0.6)

        # Flag
        flag = VGroup(
            Rectangle(width=3.0, height=0.9, fill_color=BLUE, fill_opacity=1, stroke_width=0),
            Rectangle(width=3.0, height=0.9, fill_color=YELLOW, fill_opacity=1, stroke_width=0),
        ).arrange(DOWN, buff=0).shift(LEFT * 4.0 + UP * 1.5)
        self.play(FadeIn(flag), run_time=0.7)

        # Data
        data = VGroup(
            stat_line("Главен град:", "Киев", YELLOW),
            stat_line("Население:", "41 мил.", BLUE),
            stat_line("Површина:", "603.000 км²", GREEN),
            stat_line("Јазик:", "украински", ORANGE),
            stat_line("Симбол:", "жито и сонце", YELLOW),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT * 3.5 + DOWN * 1.0)

        for d in data:
            self.play(FadeIn(d, shift=RIGHT * 0.2), run_time=0.4)

        # Right side — "житница"
        zh = Text("Житница на Европа.", font_size=34, color=YELLOW, weight=BOLD).shift(RIGHT * 3.0 + UP * 1.8)
        zh2 = Text("Црна земја (чернозем).", font_size=24, color=ORANGE).next_to(zh, DOWN, buff=0.3)
        zh3 = Text("Пченица, пченка, сончоглед.", font_size=24, color=WHITE2).next_to(zh2, DOWN, buff=0.2)
        zh4 = Text("Храни милиони во светот.", font_size=24, color=GREEN).next_to(zh3, DOWN, buff=0.2)

        self.play(Write(zh), run_time=0.9)
        self.play(Write(zh2), Write(zh3), Write(zh4), run_time=1.4)

        # War 2022
        war = Text("2022 — војна со Русија.",
                   font_size=30, color=RED, weight=BOLD).next_to(zh4, DOWN, buff=0.5)
        war2 = Text("Украина се брани. Светот гледа.",
                    font_size=24, color=WHITE2).next_to(war, DOWN, buff=0.2)

        self.play(Write(war), run_time=0.9)
        self.play(Write(war2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, flag, data, zh, zh2, zh3, zh4, war, war2)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  БЕЛОРУСИЈА — соколот што чека                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("belorusija")

        title3 = section_title("Белорусија", color=GREEN)
        self.play(FadeIn(title3), run_time=0.6)

        # Flag (red/green with white pattern simplified)
        flag_b = VGroup(
            Rectangle(width=3.0, height=1.2, fill_color=RED, fill_opacity=1, stroke_width=0),
            Rectangle(width=3.0, height=0.6, fill_color=GREEN, fill_opacity=1, stroke_width=0),
        ).arrange(DOWN, buff=0).shift(LEFT * 4.0 + UP * 1.5)
        self.play(FadeIn(flag_b), run_time=0.7)

        data_b = VGroup(
            stat_line("Главен град:", "Минск", YELLOW),
            stat_line("Население:", "9.3 мил.", BLUE),
            stat_line("Површина:", "207.000 км²", GREEN),
            stat_line("Јазици:", "белоруски, руски", ORANGE),
            stat_line("Релјеф:", "рамнини, мочуришта", PURPLE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT * 3.5 + DOWN * 1.0)

        for d in data_b:
            self.play(FadeIn(d, shift=RIGHT * 0.2), run_time=0.4)

        # Right side — political
        pol = Text("Сојузник на Русија.", font_size=32, color=RED, weight=BOLD).shift(RIGHT * 3.0 + UP * 1.8)
        pol2 = Text("Авторитарна влада.", font_size=24, color=ORANGE).next_to(pol, DOWN, buff=0.3)
        pol3 = Text("Еден претседател —", font_size=24, color=WHITE2).next_to(pol2, DOWN, buff=0.2)
        pol4 = Text("повеќе од 30 години.", font_size=24, color=YELLOW).next_to(pol3, DOWN, buff=0.1)

        self.play(Write(pol), run_time=0.9)
        self.play(Write(pol2), Write(pol3), Write(pol4), run_time=1.4)

        # Economy
        econ = Text("Тешка индустрија. Трактори. Калиум.",
                    font_size=22, color=GREEN).next_to(pol4, DOWN, buff=0.4)
        self.play(Write(econ), run_time=1.0)

        wait_msg = Text("Белорусија чека — друго време.",
                        font_size=26, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(wait_msg), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, flag_b, data_b, pol, pol2, pol3, pol4, econ, wait_msg)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  МОЛДАВИЈА — најмала од трите                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("moldavija")

        title4 = section_title("Молдавија", color=PURPLE)
        self.play(FadeIn(title4), run_time=0.6)

        # Flag (blue/yellow/red)
        flag_m = VGroup(
            Rectangle(width=1.0, height=1.6, fill_color=BLUE, fill_opacity=1, stroke_width=0),
            Rectangle(width=1.0, height=1.6, fill_color=YELLOW, fill_opacity=1, stroke_width=0),
            Rectangle(width=1.0, height=1.6, fill_color=RED, fill_opacity=1, stroke_width=0),
        ).arrange(RIGHT, buff=0).shift(LEFT * 4.0 + UP * 1.5)
        self.play(FadeIn(flag_m), run_time=0.7)

        data_m = VGroup(
            stat_line("Главен град:", "Кишинев", YELLOW),
            stat_line("Население:", "2.5 мил.", BLUE),
            stat_line("Површина:", "33.846 км²", GREEN),
            stat_line("Јазик:", "молдавски (романски)", ORANGE),
            stat_line("Соседи:", "Романија, Украина", PURPLE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT * 3.5 + DOWN * 1.0)

        for d in data_m:
            self.play(FadeIn(d, shift=RIGHT * 0.2), run_time=0.4)

        # Right — agriculture + wine
        ag = Text("Земјоделска земја.", font_size=30, color=GREEN, weight=BOLD).shift(RIGHT * 3.0 + UP * 1.8)
        ag2 = Text("Овошје. Зеленчук.", font_size=24, color=ORANGE).next_to(ag, DOWN, buff=0.3)
        ag3 = Text("Лозја. Вино — светско име.", font_size=24, color=PURPLE).next_to(ag2, DOWN, buff=0.2)
        ag4 = Text("Помеѓу Романија и Украина —", font_size=22, color=WHITE2).next_to(ag3, DOWN, buff=0.3)
        ag5 = Text("мала земја со голема приказна.", font_size=22, color=YELLOW).next_to(ag4, DOWN, buff=0.1)

        self.play(Write(ag), run_time=0.9)
        self.play(Write(ag2), Write(ag3), run_time=1.0)
        self.play(Write(ag4), Write(ag5), run_time=1.0)

        sil = Text("Молдавија молчи — но рача дома и во Европа.",
                   font_size=24, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(sil), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title4, flag_m, data_m, ag, ag2, ag3, ag4, ag5, sil)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  СПОРЕДБА — табела                             ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sporedba")

        title5 = section_title("Споредба на трите", color=ORANGE)
        self.play(FadeIn(title5), run_time=0.6)

        headers = VGroup(
            Text("", font_size=22, color=WHITE2),
            Text("Украина", font_size=24, color=YELLOW, weight=BOLD),
            Text("Белорусија", font_size=24, color=GREEN, weight=BOLD),
            Text("Молдавија", font_size=24, color=PURPLE, weight=BOLD),
        ).arrange(RIGHT, buff=0.9).next_to(title5, DOWN, buff=0.6)
        self.play(Write(headers), run_time=0.8)

        rows_data = [
            ("Главен град", "Киев", "Минск", "Кишинев"),
            ("Население", "41 мил.", "9.3 мил.", "2.5 мил."),
            ("Површина", "603.000", "207.000", "33.846"),
            ("Симбол", "жито", "трактор", "вино"),
            ("Со Русија", "војна", "сојуз", "тензија"),
        ]

        rows = VGroup()
        for label, va, vs, vm in rows_data:
            r = VGroup(
                Text(label, font_size=20, color=GREY),
                Text(va, font_size=20, color=YELLOW),
                Text(vs, font_size=20, color=GREEN),
                Text(vm, font_size=20, color=PURPLE),
            ).arrange(RIGHT, buff=0.9)
            rows.add(r)

        rows.arrange(DOWN, buff=0.25).next_to(headers, DOWN, buff=0.4)

        for r in rows:
            self.play(FadeIn(r, shift=LEFT * 0.2), run_time=0.4)

        self.wait(1.4)
        self.play(FadeOut(VGroup(title5, headers, rows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        title6 = section_title("Што да запомниме", color=YELLOW)
        self.play(FadeIn(title6), run_time=0.6)

        bullets = VGroup(
            callout("Украина — Киев, житница, војна од 2022", width=11, border=YELLOW),
            callout("Белорусија — Минск, сојузник на Русија", width=11, border=GREEN),
            callout("Молдавија — Кишинев, најмала, винарска", width=11, border=PURPLE),
            callout("Сите три — бивши Советски Републики", width=11, border=RED),
            callout("Сите се борат за свое место во Европа", width=11, border=BLUE),
        ).arrange(DOWN, buff=0.25).next_to(title6, DOWN, buff=0.4)

        for b in bullets:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.45)

        self.wait(0.6)

        final = Text("Три сестри. Една историја. Различни патишта.",
                     font_size=30, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(final), run_time=1.2)
        self.wait(2.2)

        self.play(FadeOut(VGroup(title6, bullets, final)), run_time=0.8)
        self.wait(0.5)
