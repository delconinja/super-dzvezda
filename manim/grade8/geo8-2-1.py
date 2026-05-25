"""
geo8-2-1  —  Население на Европа
Географија 8, Единица 2: Европа како општествена целина

Teaching narrative — Andonovski-style: three-beat punches,
nations as characters, populations as flowing rivers,
languages as colours weaving one tapestry.
Render:  manim -ql geo8-2-1.py Geo821Scene
Output:  media/videos/geo8-2-1/480p15/Geo821Scene.mp4
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


def lang_card(name, family, color, pos):
    box = RoundedRectangle(
        width=3.0, height=1.7, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=22, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.35)
    fm = Text(family, font_size=15, color=GREY)
    fm.move_to(box.get_center() + DOWN * 0.35)
    return VGroup(box, nm, fm)


class Geo821Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("750 милиони луѓе.", font_size=54, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Стотина јазици.", font_size=38, color=WHITE2),
            Text("Една мала континента.", font_size=38, color=GREY),
            Text("Богата ја прави разноликоста.", font_size=36, color=GREEN),
            Text("Не уништува.", font_size=36, color=RED),
            Text("Гради.", font_size=44, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.18)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  POPULATION SCALE                                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("scale")

        st2 = section_title("Колку сме?")
        self.play(Write(st2), run_time=0.8)

        # Big number
        big = Text("≈ 750 000 000", font_size=68, color=YELLOW, weight=BOLD)
        big.move_to(UP * 1.3)
        self.play(Write(big), run_time=1.0)
        self.wait(0.4)

        sub = Text("седум стотини и педесет милиони жители", font_size=26, color=WHITE2)
        sub.next_to(big, DOWN, buff=0.35)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.7)
        self.wait(0.5)

        # Visual: 75 dots = 10 million each
        dots = VGroup()
        for i in range(75):
            row = i // 15
            col = i % 15
            d = Dot(point=np.array([-3.5 + col * 0.5, -1.0 - row * 0.5, 0]),
                    radius=0.12, color=BLUE)
            dots.add(d)
        legend = Text("● = 10 милиони луѓе", font_size=18, color=GREY)
        legend.next_to(dots, DOWN, buff=0.3)

        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots],
                              lag_ratio=0.03), run_time=2.5)
        self.play(FadeIn(legend), run_time=0.4)
        self.wait(1.0)

        rank = Text("Трет по бројност — по Азија и Африка.", font_size=24, color=ORANGE)
        rank.to_edge(DOWN, buff=0.4)
        self.play(Write(rank), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st2, big, sub, dots, legend, rank)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  LANGUAGE FAMILIES                               ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("languages")

        st3 = section_title("Јазиците на Европа")
        self.play(Write(st3), run_time=0.8)

        intro3 = Text("Не еден говор. Туку семејства.", font_size=28, color=WHITE2)
        intro3.next_to(st3, DOWN, buff=0.4)
        self.play(FadeIn(intro3, shift=UP * 0.2), run_time=0.7)
        self.wait(0.4)

        slav = lang_card("Словенски", "македонски, руски,\nпол. српски", GREEN,
                         np.array([-4.5, -0.5, 0]))
        germ = lang_card("Германски", "англиски, германски,\nшведски", BLUE,
                         np.array([-1.5, -0.5, 0]))
        rom = lang_card("Романски", "италијански, шпански,\nфранцуски", ORANGE,
                        np.array([1.5, -0.5, 0]))
        gr = lang_card("Грчки", "грчки јазик —\nсам своја гранка", YELLOW,
                       np.array([4.5, -0.5, 0]))
        fu = lang_card("Фино-угрски", "фински, унгарски,\nестонски", PURPLE,
                       np.array([0, -2.6, 0]))

        for card in (slav, germ, rom, gr, fu):
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.5)
            self.wait(0.15)

        self.wait(0.6)

        # Andonovski close
        close3 = Text("Различни корени. Иста почва.", font_size=26, color=YELLOW)
        close3.to_edge(DOWN, buff=0.35)
        self.play(Write(close3), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(st3, intro3, slav, germ, rom, gr, fu, close3)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  RELIGIONS                                       ~65 s
        # ══════════════════════════════════════════════════════════
        self.next_section("religions")

        st4 = section_title("Религиите")
        self.play(Write(st4), run_time=0.8)

        # Christianity tree
        chr_root = Text("Христијанство", font_size=32, color=BLUE, weight=BOLD)
        chr_root.move_to(UP * 1.6)
        self.play(Write(chr_root), run_time=0.7)
        self.wait(0.3)

        orth = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.15,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=YELLOW, stroke_width=2)
        orth.move_to(LEFT * 4 + UP * 0.1)
        orth_t = Text("Православие", font_size=20, color=YELLOW).move_to(orth)

        cath = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.15,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=GREEN, stroke_width=2)
        cath.move_to(UP * 0.1)
        cath_t = Text("Католицизам", font_size=20, color=GREEN).move_to(cath)

        prot = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.15,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=ORANGE, stroke_width=2)
        prot.move_to(RIGHT * 4 + UP * 0.1)
        prot_t = Text("Протестантизам", font_size=18, color=ORANGE).move_to(prot)

        line1 = Line(chr_root.get_bottom(), orth.get_top(), color=GREY, stroke_width=2)
        line2 = Line(chr_root.get_bottom(), cath.get_top(), color=GREY, stroke_width=2)
        line3 = Line(chr_root.get_bottom(), prot.get_top(), color=GREY, stroke_width=2)

        self.play(Create(line1), Create(line2), Create(line3), run_time=0.6)
        self.play(FadeIn(orth), FadeIn(orth_t),
                  FadeIn(cath), FadeIn(cath_t),
                  FadeIn(prot), FadeIn(prot_t), run_time=0.8)
        self.wait(0.6)

        # Other religions
        other_row = VGroup(
            Text("Ислам", font_size=22, color=GREEN, weight=BOLD),
            Text("Јудаизам", font_size=22, color=PURPLE, weight=BOLD),
            Text("Атеизам — расте", font_size=22, color=GREY),
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 1.5)

        self.play(LaggedStart(*[FadeIn(o, shift=UP * 0.2) for o in other_row],
                              lag_ratio=0.25), run_time=1.2)
        self.wait(0.6)

        close4 = Text("Една земја. Многу вери. Заедничка стреа.", font_size=24, color=YELLOW)
        close4.to_edge(DOWN, buff=0.35)
        self.play(Write(close4), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st4, chr_root, orth, orth_t, cath, cath_t,
                                  prot, prot_t, line1, line2, line3,
                                  other_row, close4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  URBANIZATION 74%                                ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("urban")

        st5 = section_title("Урбанизација")
        self.play(Write(st5), run_time=0.8)

        intro5 = Text("Каде живееме?", font_size=28, color=WHITE2)
        intro5.next_to(st5, DOWN, buff=0.4)
        self.play(FadeIn(intro5), run_time=0.6)
        self.wait(0.3)

        # Pie-like bar
        bar_bg = Rectangle(width=8.0, height=0.8, fill_color=DARK_CARD,
                          fill_opacity=1, stroke_color=GREY, stroke_width=1)
        bar_bg.move_to(UP * 0.2)
        urban_fill = Rectangle(width=8.0 * 0.74, height=0.8,
                               fill_color=BLUE, fill_opacity=1,
                               stroke_width=0)
        urban_fill.align_to(bar_bg, LEFT)
        urban_fill.move_to(bar_bg.get_left() + RIGHT * (8.0 * 0.74 / 2))

        self.play(FadeIn(bar_bg), run_time=0.4)
        self.play(GrowFromEdge(urban_fill, LEFT), run_time=1.5)
        self.wait(0.3)

        urban_lbl = Text("74% — градови", font_size=26, color=BLUE, weight=BOLD)
        urban_lbl.next_to(bar_bg, UP, buff=0.3)
        rural_lbl = Text("26% — села", font_size=22, color=GREEN)
        rural_lbl.next_to(bar_bg, DOWN, buff=0.3)
        self.play(Write(urban_lbl), Write(rural_lbl), run_time=0.8)
        self.wait(0.6)

        beats5 = VGroup(
            Text("Селото испразнето.", font_size=26, color=GREY),
            Text("Градот преполн.", font_size=26, color=ORANGE),
            Text("Така тече реката на луѓето.", font_size=26, color=BLUE),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1.8)

        for b in beats5:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)

        self.wait(1.0)
        self.play(FadeOut(VGroup(st5, intro5, bar_bg, urban_fill,
                                  urban_lbl, rural_lbl, beats5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  AGING POPULATION                                ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("aging")

        st6 = section_title("Старее Европа", color=ORANGE)
        self.play(Write(st6), run_time=0.8)

        # Pyramid shape - inverted
        intro6 = Text("Помалку деца. Повеќе старци.", font_size=28, color=WHITE2)
        intro6.next_to(st6, DOWN, buff=0.4)
        self.play(FadeIn(intro6, shift=UP * 0.2), run_time=0.7)
        self.wait(0.4)

        # Simple age pyramid (rectangles)
        ages = [
            ("65+",   3.5, ORANGE),
            ("40–64", 3.0, YELLOW),
            ("15–39", 2.5, GREEN),
            ("0–14",  1.8, BLUE),
        ]
        bars = VGroup()
        for i, (label, w, c) in enumerate(ages):
            r = Rectangle(width=w, height=0.6,
                          fill_color=c, fill_opacity=0.85,
                          stroke_color=c, stroke_width=1)
            r.move_to(UP * (0.9 - i * 0.7))
            lbl = Text(label, font_size=20, color=WHITE2, weight=BOLD)
            lbl.next_to(r, LEFT, buff=0.3)
            bars.add(VGroup(r, lbl))

        for bar in bars:
            self.play(FadeIn(bar, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.1)

        warn = Text("Превртена пирамида — врвот тежок.", font_size=22, color=RED)
        warn.move_to(DOWN * 2.5)
        self.play(Write(warn), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(st6, intro6, bars, warn)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final_lines = VGroup(
            Text("750 милиони гласови.", font_size=40, color=YELLOW, weight=BOLD),
            Text("Стотина јазици.", font_size=34, color=BLUE),
            Text("Три големи вери.", font_size=34, color=GREEN),
            Text("Една континента.", font_size=34, color=WHITE2),
            Text("Една приказна.", font_size=46, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for ln in final_lines:
            self.play(Write(ln), run_time=0.7)
            self.wait(0.2)

        self.wait(2.5)
        self.play(FadeOut(final_lines), run_time=1.2)
        self.wait(0.4)
