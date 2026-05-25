"""
geo8-2-2  —  Економија на Европа
Географија 8, Единица 2: Европа како општествена целина

Teaching narrative — Andonovski-style: three-beat punches,
economy as living ecosystem, sectors as body parts,
EU single market as one heart with many veins.
Render:  manim -ql geo8-2-2.py Geo822Scene
Output:  media/videos/geo8-2-2/480p15/Geo822Scene.mp4
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


def sector_card(icon, name, desc, color, pos):
    box = RoundedRectangle(
        width=3.6, height=2.2, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    ic = Text(icon, font_size=34, color=color, weight=BOLD)
    ic.move_to(box.get_center() + UP * 0.65)
    nm = Text(name, font_size=22, color=WHITE2, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.05)
    dc = Text(desc, font_size=15, color=GREY)
    dc.move_to(box.get_center() + DOWN * 0.55)
    return VGroup(box, ic, nm, dc)


def country_bar(name, value, max_val, color, y):
    width = 8.0 * (value / max_val)
    bar = Rectangle(width=width, height=0.55,
                    fill_color=color, fill_opacity=0.9,
                    stroke_color=color, stroke_width=1)
    bar.move_to(np.array([-4.0 + width / 2, y, 0]))
    nm = Text(name, font_size=20, color=WHITE2, weight=BOLD)
    nm.next_to(bar, LEFT, buff=0.25).align_to(bar, LEFT).shift(LEFT * 2.4)
    vl = Text(f"{value}", font_size=18, color=color, weight=BOLD)
    vl.next_to(bar, RIGHT, buff=0.2)
    return VGroup(bar, nm, vl)


class Geo822Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Земјоделство — стара душа.", font_size=38, color=GREEN, weight=BOLD)
        h2 = Text("Индустрија — мускули.", font_size=38, color=ORANGE, weight=BOLD)
        h3 = Text("Услуги — мозок.", font_size=38, color=BLUE, weight=BOLD)
        h4 = Text("Економијата има тројство.", font_size=34, color=WHITE2)
        h5 = Text("Сите три неопходни.", font_size=44, color=YELLOW, weight=BOLD)

        beats = VGroup(h1, h2, h3, h4, h5).arrange(DOWN, buff=0.4)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)

        self.wait(1.0)
        self.play(FadeOut(beats), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  THREE SECTORS                                   ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sectors")

        st2 = section_title("Трите сектори")
        self.play(Write(st2), run_time=0.8)

        primary = sector_card("I",  "Примарен", "земјоделство,\nрударство, шумарство",
                              GREEN,  np.array([-4.5, -0.3, 0]))
        secondary = sector_card("II", "Секундарен", "индустрија,\nградежништво",
                                ORANGE, np.array([0.0, -0.3, 0]))
        tertiary = sector_card("III","Терцијарен", "услуги — банки,\nтрговија, туризам",
                               BLUE,   np.array([4.5, -0.3, 0]))

        self.play(FadeIn(primary, shift=UP * 0.3), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(secondary, shift=UP * 0.3), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(tertiary, shift=UP * 0.3), run_time=0.7)
        self.wait(0.5)

        # Dominance arrow
        dom = Text("Терцијарниот сектор владее.", font_size=26, color=BLUE, weight=BOLD)
        dom.move_to(DOWN * 2.3)
        arrow = Arrow(tertiary.get_bottom() + DOWN * 0.1, dom.get_top() + UP * 0.1,
                      color=BLUE, buff=0.1, stroke_width=4)
        self.play(GrowArrow(arrow), Write(dom), run_time=1.0)
        self.wait(0.8)

        share = Text("Повеќе од 70% од европскиот БДП.", font_size=22, color=YELLOW)
        share.move_to(DOWN * 3.1)
        self.play(FadeIn(share, shift=UP * 0.15), run_time=0.7)
        self.wait(1.2)

        self.play(FadeOut(VGroup(st2, primary, secondary, tertiary,
                                  dom, arrow, share)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  TOP ECONOMIES                                   ~65 s
        # ══════════════════════════════════════════════════════════
        self.next_section("top")

        st3 = section_title("Главните економии")
        self.play(Write(st3), run_time=0.8)

        intro3 = Text("Кој ја носи Европа?", font_size=26, color=WHITE2)
        intro3.next_to(st3, DOWN, buff=0.4)
        self.play(FadeIn(intro3), run_time=0.6)
        self.wait(0.3)

        # BDP in billions USD (illustrative)
        max_val = 4500
        b1 = country_bar("Германија",     4500, max_val, BLUE,   1.0)
        b2 = country_bar("В. Британија",  3300, max_val, ORANGE, 0.2)
        b3 = country_bar("Франција",      3000, max_val, GREEN,  -0.6)
        b4 = country_bar("Италија",       2200, max_val, YELLOW, -1.4)
        b5 = country_bar("Шпанија",       1600, max_val, PURPLE, -2.2)

        bars = VGroup(b1, b2, b3, b4, b5)
        for b in bars:
            self.play(GrowFromEdge(b[0], LEFT), FadeIn(b[1]), FadeIn(b[2]),
                      run_time=0.55)
            self.wait(0.1)

        unit = Text("БДП — милијарди американски долари", font_size=16, color=GREY)
        unit.move_to(DOWN * 3.1)
        self.play(FadeIn(unit), run_time=0.5)
        self.wait(1.0)

        close3 = Text("Германија — мотор на континентата.", font_size=24, color=BLUE)
        close3.move_to(DOWN * 3.5).shift(UP * 0.15)
        # Move unit up to avoid collision
        self.play(unit.animate.shift(UP * 0.15), run_time=0.2)
        close3.move_to(DOWN * 3.5)
        # Skip — just fade out cleanly
        self.wait(1.0)

        self.play(FadeOut(VGroup(st3, intro3, bars, unit)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  EU SINGLE MARKET                                ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("eu_market")

        st4 = section_title("Единствениот пазар на ЕУ", color=BLUE)
        self.play(Write(st4), run_time=0.8)

        intro4 = Text("Една зона. Без граници за стоки.", font_size=26, color=WHITE2)
        intro4.next_to(st4, DOWN, buff=0.4)
        self.play(FadeIn(intro4, shift=UP * 0.2), run_time=0.7)
        self.wait(0.4)

        # Central EU circle with 4 freedoms around it
        center = Circle(radius=1.3, color=BLUE, fill_color=DARK_CARD,
                        fill_opacity=1, stroke_width=3)
        center.move_to(DOWN * 0.3)
        eu_lbl = Text("ЕУ", font_size=44, color=YELLOW, weight=BOLD).move_to(center)
        self.play(Create(center), Write(eu_lbl), run_time=0.9)

        # 4 freedoms
        freedoms = [
            ("Стоки",    UP * 2.4 + LEFT * 3.0, GREEN),
            ("Услуги",   UP * 2.4 + RIGHT * 3.0, ORANGE),
            ("Капитал",  DOWN * 2.8 + LEFT * 3.0, PURPLE),
            ("Луѓе",     DOWN * 2.8 + RIGHT * 3.0, YELLOW),
        ]
        nodes = []
        lines = []
        for nm, pos, col in freedoms:
            box = RoundedRectangle(width=2.0, height=0.8, corner_radius=0.15,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=col, stroke_width=2)
            box.move_to(pos)
            lbl = Text(nm, font_size=20, color=col, weight=BOLD).move_to(box)
            line = Line(center.get_center(), box.get_center(),
                        color=col, stroke_width=2)
            nodes.append(VGroup(box, lbl))
            lines.append(line)

        for ln, nd in zip(lines, nodes):
            self.play(Create(ln), FadeIn(nd), run_time=0.55)
            self.wait(0.1)

        self.wait(0.6)

        close4 = Text("Четири слободи. Едно срце.", font_size=24, color=YELLOW)
        close4.to_edge(DOWN, buff=0.3)
        self.play(Write(close4), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st4, intro4, center, eu_lbl,
                                  *nodes, *lines, close4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  EAST vs WEST                                    ~65 s
        # ══════════════════════════════════════════════════════════
        self.next_section("east_west")

        st5 = section_title("Запад наспроти Исток")
        self.play(Write(st5), run_time=0.8)

        # Two columns
        west_box = RoundedRectangle(width=5.5, height=4.3, corner_radius=0.3,
                                    fill_color="#0d2b44", fill_opacity=1,
                                    stroke_color=BLUE, stroke_width=2)
        west_box.move_to(LEFT * 3.2 + DOWN * 0.4)
        west_t = Text("ЗАПАД", font_size=28, color=BLUE, weight=BOLD)
        west_t.move_to(west_box.get_top() + DOWN * 0.4)

        east_box = RoundedRectangle(width=5.5, height=4.3, corner_radius=0.3,
                                    fill_color="#0d2b44", fill_opacity=1,
                                    stroke_color=ORANGE, stroke_width=2)
        east_box.move_to(RIGHT * 3.2 + DOWN * 0.4)
        east_t = Text("ИСТОК", font_size=28, color=ORANGE, weight=BOLD)
        east_t.move_to(east_box.get_top() + DOWN * 0.4)

        self.play(Create(west_box), Create(east_box),
                  Write(west_t), Write(east_t), run_time=0.9)

        west_items = VGroup(
            Text("• висок БДП по жител", font_size=20, color=WHITE2),
            Text("• развиена индустрија", font_size=20, color=WHITE2),
            Text("• силен терцијарен", font_size=20, color=WHITE2),
            Text("• стабилни плати", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        west_items.next_to(west_t, DOWN, buff=0.4).shift(LEFT * 0.5)

        east_items = VGroup(
            Text("• низок БДП по жител", font_size=20, color=WHITE2),
            Text("• пост-социјалистичка", font_size=20, color=WHITE2),
            Text("• растечки услуги", font_size=20, color=WHITE2),
            Text("• миграција на млади", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        east_items.next_to(east_t, DOWN, buff=0.4).shift(LEFT * 0.5)

        for w, e in zip(west_items, east_items):
            self.play(FadeIn(w, shift=RIGHT * 0.2),
                      FadeIn(e, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.1)

        self.wait(0.8)

        bridge = Text("Разликата се намалува. Бавно.", font_size=24, color=YELLOW)
        bridge.to_edge(DOWN, buff=0.3)
        self.play(Write(bridge), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st5, west_box, east_box, west_t, east_t,
                                  west_items, east_items, bridge)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CLOSING                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final_lines = VGroup(
            Text("Душа. Мускули. Мозок.", font_size=42, color=YELLOW, weight=BOLD),
            Text("Трите сектори чинат тело.", font_size=30, color=WHITE2),
            Text("Заедничкиот пазар — крвоток.", font_size=30, color=BLUE),
            Text("Една економија. Многу пулсеви.", font_size=34, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for ln in final_lines:
            self.play(Write(ln), run_time=0.8)
            self.wait(0.25)

        self.wait(2.5)
        self.play(FadeOut(final_lines), run_time=1.2)
        self.wait(0.4)
