"""
geo8-6-2  —  Алписки земји: Австрија и Швајцарија
Географија 8, Единица 6: Средна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as characters, mountains as elders.
Render:  manim -ql geo8-6-2.py Geo862Scene
Output:  media/videos/geo8-6-2/480p15/Geo862Scene.mp4
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


def country_card(name, color, pos, w=2.6, h=1.3, fs=24):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2.5,
    ).move_to(pos)
    nm = Text(name, font_size=fs, color=color, weight=BOLD)
    nm.move_to(box)
    return VGroup(box, nm)


def mountain(pos, base=2.0, height=2.0, color=GREY, snow_color=WHITE2):
    left = pos + LEFT * (base / 2)
    right = pos + RIGHT * (base / 2)
    top = pos + UP * height
    tri = Polygon(left, right, top, fill_color=color, fill_opacity=0.85,
                  stroke_color=WHITE2, stroke_width=1.5)
    # snow cap
    cap_l = top + DOWN * (height * 0.35) + LEFT * (base * 0.25)
    cap_r = top + DOWN * (height * 0.35) + RIGHT * (base * 0.25)
    cap = Polygon(cap_l, cap_r, top, fill_color=snow_color, fill_opacity=0.9,
                  stroke_color=snow_color, stroke_width=1)
    return VGroup(tri, cap)


class Geo862Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — Швајцарија — 4 јазици                  ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Швајцарија има 4 јазици.", font_size=52, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.6)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Една држава.", font_size=40, color=BLUE, weight=BOLD),
            Text("Без војна 500 години.", font_size=38, color=GREEN, weight=BOLD),
            Text("Не е магија.", font_size=36, color=ORANGE),
            Text("Договор.", font_size=36, color=PURPLE, weight=BOLD),
            Text("Со меч во еден и мир во друг збор.", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.3).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.9)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  АЛПИТЕ — кичма на Европа                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("alpi")

        title = section_title("Алпи — кичма на Европа", color=GREY)
        self.play(FadeIn(title), run_time=0.6)

        # Mountain range across the bottom
        peaks = VGroup(
            mountain(LEFT * 5 + DOWN * 1.5, base=2.0, height=1.5, color="#3a5068"),
            mountain(LEFT * 3 + DOWN * 1.5, base=2.4, height=2.4, color="#4a6078"),
            mountain(LEFT * 0.5 + DOWN * 1.5, base=2.8, height=2.8, color="#5a7088"),
            mountain(RIGHT * 2 + DOWN * 1.5, base=2.4, height=2.2, color="#4a6078"),
            mountain(RIGHT * 4.5 + DOWN * 1.5, base=2.0, height=1.6, color="#3a5068"),
        )

        for p in peaks:
            self.play(DrawBorderThenFill(p), run_time=0.5)

        # Highest peak label
        mb = Text("Монблан 4810 м", font_size=24, color=WHITE2, weight=BOLD)
        mb.next_to(peaks[2], UP, buff=0.2)
        self.play(Write(mb), run_time=0.8)

        fact = Text("Алпите делат — Север од Југ. Студ од топло.",
                    font_size=28, color=YELLOW).next_to(title, DOWN, buff=0.3)
        self.play(Write(fact), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, peaks, mb, fact)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  АВСТРИЈА — Виена и Моцарт                     ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("avstrija")

        title2 = section_title("Австрија", color=RED)
        self.play(FadeIn(title2), run_time=0.6)

        flag_a = VGroup(
            Rectangle(width=2.4, height=0.5, fill_color=RED, fill_opacity=1, stroke_width=0),
            Rectangle(width=2.4, height=0.5, fill_color=WHITE2, fill_opacity=1, stroke_width=0),
            Rectangle(width=2.4, height=0.5, fill_color=RED, fill_opacity=1, stroke_width=0),
        ).arrange(DOWN, buff=0).shift(LEFT * 4.5 + UP * 1.5)
        self.play(FadeIn(flag_a), run_time=0.7)

        data_a = VGroup(
            country_card("Виена", BLUE, ORIGIN),
            country_card("9 мил. жители", GREEN, ORIGIN),
            country_card("83.000 км²", ORANGE, ORIGIN),
            country_card("неутрална", YELLOW, ORIGIN),
        ).arrange_in_grid(rows=2, cols=2, buff=0.25).shift(LEFT * 3.5 + DOWN * 1.2)

        for d in data_a:
            self.play(FadeIn(d, shift=UP * 0.2), run_time=0.4)

        # Right column — culture
        culture = VGroup(
            Text("Моцарт", font_size=36, color=YELLOW, weight=BOLD),
            Text("Шуберт", font_size=30, color=ORANGE),
            Text("Штраус", font_size=30, color=PURPLE),
            Text("Виена — престолнина", font_size=24, color=WHITE2),
            Text("на класичната музика.", font_size=24, color=WHITE2),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.2 + UP * 0.5)

        for c in culture:
            self.play(Write(c), run_time=0.5)

        self.wait(0.5)

        neut = Text("Австрија — неутрална од 1955.",
                    font_size=28, color=GREEN, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(neut), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title2, flag_a, data_a, culture, neut)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ШВАЈЦАРИЈА — четири јазици                    ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("svajcarija")

        title3 = section_title("Швајцарија — 4 јазици", color=RED)
        self.play(FadeIn(title3), run_time=0.6)

        # Swiss flag
        flag_s_bg = Square(side_length=1.6, fill_color=RED, fill_opacity=1, stroke_color=WHITE2, stroke_width=1.5)
        flag_s_v = Rectangle(width=0.3, height=1.0, fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        flag_s_h = Rectangle(width=1.0, height=0.3, fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        flag_s = VGroup(flag_s_bg, flag_s_v, flag_s_h).shift(LEFT * 5.2 + UP * 2.0)
        self.play(FadeIn(flag_s), run_time=0.7)

        # 4 language regions
        langs = VGroup(
            country_card("Германски\n63%", BLUE, ORIGIN, h=1.4, fs=22),
            country_card("Француски\n23%", YELLOW, ORIGIN, h=1.4, fs=22),
            country_card("Италијански\n8%", GREEN, ORIGIN, h=1.4, fs=22),
            country_card("Романш\n0.5%", PURPLE, ORIGIN, h=1.4, fs=22),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 0.4)

        for l in langs:
            self.play(FadeIn(l, shift=UP * 0.2), run_time=0.45)

        # Capital + facts
        bern = country_card("Берн", RED, RIGHT * 3.5 + UP * 2.0, w=2.4, h=1.0)
        self.play(FadeIn(bern), run_time=0.5)

        facts = VGroup(
            Text("Чоколадо.", font_size=30, color=ORANGE, weight=BOLD),
            Text("Часовници.", font_size=30, color=YELLOW, weight=BOLD),
            Text("Банкарство.", font_size=30, color=GREEN, weight=BOLD),
            Text("Неутралност.", font_size=30, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.4)

        for f in facts:
            self.play(Write(f), run_time=0.4)

        self.wait(1.4)

        self.play(FadeOut(VGroup(title3, flag_s, langs, bern, facts)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ЗАЕДНИЧКО — без излез на море                 ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zaednichko")

        title4 = section_title("Заедничко — без море", color=BLUE)
        self.play(FadeIn(title4), run_time=0.6)

        intro = Text("И двете држави — без излез на море.",
                     font_size=30, color=WHITE2).next_to(title4, DOWN, buff=0.4)
        self.play(Write(intro), run_time=1.0)

        # Big lake illustration
        lake = Ellipse(width=4.5, height=2.2, fill_color=BLUE, fill_opacity=0.7,
                       stroke_color=WHITE2, stroke_width=2).shift(DOWN * 0.6)
        lake_lbl = Text("Боденско езеро", font_size=24, color=WHITE2, weight=BOLD).move_to(lake)
        self.play(DrawBorderThenFill(lake), Write(lake_lbl), run_time=1.0)

        shared = VGroup(
            callout("Алпите — заедничка кичма", width=10, border=GREY),
            callout("Високи планини, длабоки езера", width=10, border=BLUE),
            callout("Туризам — зимски спортови, скијање", width=10, border=YELLOW),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.4)

        for s in shared:
            self.play(FadeIn(s, shift=LEFT * 0.2), run_time=0.5)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title4, intro, lake, lake_lbl, shared)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  СПОРЕДБА — табела                             ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sporedba")

        title5 = section_title("Споредба", color=ORANGE)
        self.play(FadeIn(title5), run_time=0.6)

        # Headers
        headers = VGroup(
            Text("", font_size=22, color=WHITE2),
            Text("Австрија", font_size=26, color=RED, weight=BOLD),
            Text("Швајцарија", font_size=26, color=RED, weight=BOLD),
        ).arrange(RIGHT, buff=1.4).next_to(title5, DOWN, buff=0.6)
        self.play(Write(headers), run_time=0.7)

        rows_data = [
            ("Главен град", "Виена", "Берн"),
            ("Население", "9 мил.", "8.7 мил."),
            ("Површина", "83.000 км²", "41.000 км²"),
            ("Јазици", "1 (германски)", "4"),
            ("ЕУ", "Да", "Не"),
        ]

        rows = VGroup()
        for label, va, vs in rows_data:
            r = VGroup(
                Text(label, font_size=22, color=YELLOW),
                Text(va, font_size=22, color=WHITE2),
                Text(vs, font_size=22, color=WHITE2),
            ).arrange(RIGHT, buff=1.4)
            rows.add(r)

        rows.arrange(DOWN, buff=0.3).next_to(headers, DOWN, buff=0.4)

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
            callout("Австрија — Виена, Моцарт, неутралност", width=11, border=RED),
            callout("Швајцарија — 4 јазици, чоколадо, банки", width=11, border=YELLOW),
            callout("Алпите — кичма на двете држави", width=11, border=GREY),
            callout("Без излез на море — но богати со езера", width=11, border=BLUE),
            callout("Висок стандард, мир, ред — мала Европа", width=11, border=GREEN),
        ).arrange(DOWN, buff=0.25).next_to(title6, DOWN, buff=0.4)

        for b in bullets:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.45)

        self.wait(0.6)

        final = Text("Високи планини. Долги мирни години.",
                     font_size=32, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(final), run_time=1.2)
        self.wait(2.2)

        self.play(FadeOut(VGroup(title6, bullets, final)), run_time=0.8)
        self.wait(0.5)
