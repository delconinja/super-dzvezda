"""
geo8-1-1  —  Географска положба и брегова разгранетост
Географија 8, Единица 1: Природно-географски карактеристики на Европа

Teaching narrative — Andonovski-style: three-beat punches,
continents as characters, seas as friends, coast as embrace.
Render:  manim -ql geo8-1-1.py Geo811Scene
Output:  media/videos/geo8-1-1/480p15/Geo811Scene.mp4
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


def fact_card(label, value, color, pos):
    box = RoundedRectangle(
        width=2.6, height=1.6, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    val = Text(value, font_size=30, color=color, weight=BOLD)
    val.move_to(box.get_center() + UP * 0.25)
    lab = Text(label, font_size=18, color=WHITE2)
    lab.move_to(box.get_center() + DOWN * 0.4)
    return VGroup(box, val, lab)


class Geo811Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Европа е мала.",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.4)
        self.wait(0.4)

        beats = VGroup(
            Text("Но има најдолг брег во светот.", font_size=34, color=WHITE2),
            Text("Море ѝ ја сака компанијата.", font_size=34, color=BLUE),
            Text("Поинди отколку Африка.", font_size=32, color=ORANGE),
            Text("Отворена кон сите страни.", font_size=36, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.2)
        self.play(FadeOut(hook1), FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ПОЛОЖБА — координати                            ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("polozhba")

        t2 = section_title("Каде лежи Европа?")
        self.play(Write(t2), run_time=0.9)

        # Simple globe with latitude markers
        globe = Circle(radius=2.0, color=BLUE, stroke_width=3).shift(LEFT * 3.5 + DOWN * 0.5)
        equator = Line(globe.get_left(), globe.get_right(), color=YELLOW, stroke_width=2)
        equator.move_to(globe.get_center())
        eq_lab = Text("Екватор 0°", font_size=18, color=YELLOW)
        eq_lab.next_to(equator, RIGHT, buff=0.15)

        self.play(Create(globe), run_time=0.8)
        self.play(Create(equator), FadeIn(eq_lab), run_time=0.6)

        # Latitudes 35° and 71°
        lat35 = Line(
            globe.get_center() + LEFT * 1.85 + UP * 0.7,
            globe.get_center() + RIGHT * 1.85 + UP * 0.7,
            color=GREEN, stroke_width=2,
        )
        lat71 = Line(
            globe.get_center() + LEFT * 0.7 + UP * 1.85,
            globe.get_center() + RIGHT * 0.7 + UP * 1.85,
            color=RED, stroke_width=2,
        )
        lat35_lab = Text("35° СГШ", font_size=18, color=GREEN).next_to(lat35, RIGHT, buff=0.15)
        lat71_lab = Text("71° СГШ", font_size=18, color=RED).next_to(lat71, RIGHT, buff=0.15)

        self.play(Create(lat35), FadeIn(lat35_lab), run_time=0.6)
        self.play(Create(lat71), FadeIn(lat71_lab), run_time=0.6)

        # Europe band highlight
        band = Polygon(
            globe.get_center() + LEFT * 1.85 + UP * 0.7,
            globe.get_center() + RIGHT * 1.85 + UP * 0.7,
            globe.get_center() + RIGHT * 0.7 + UP * 1.85,
            globe.get_center() + LEFT * 0.7 + UP * 1.85,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.3, stroke_width=1,
        )
        self.play(FadeIn(band), run_time=0.8)
        eu_label = Text("Европа", font_size=22, color=YELLOW, weight=BOLD)
        eu_label.move_to(band.get_center())
        self.play(Write(eu_label), run_time=0.6)

        # Right column facts
        facts = VGroup(
            callout("Од 35° до 71° северна ширина", width=5.5, bg=DARK_CARD, border=GREEN, font_size=22),
            callout("Од 10° западна до 60° источна должина", width=5.5, bg=DARK_CARD, border=BLUE, font_size=22),
            callout("Целата на северната хемисфера", width=5.5, bg=DARK_CARD, border=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.3).shift(RIGHT * 3.2 + DOWN * 0.4)

        for f in facts:
            self.play(FadeIn(f, shift=LEFT * 0.2), run_time=0.6)
            self.wait(0.2)

        self.wait(1.0)
        self.play(
            FadeOut(VGroup(globe, equator, eq_lab, lat35, lat71,
                           lat35_lab, lat71_lab, band, eu_label, facts, t2)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 3.  ГРАНИЦИ — четири страни                          ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("granici")

        t3 = section_title("Четири граници")
        self.play(Write(t3), run_time=0.8)

        # Central Europe shape
        eu_shape = RoundedRectangle(
            width=4.0, height=3.0, corner_radius=0.4,
            fill_color="#1a3a5a", fill_opacity=0.8,
            stroke_color=YELLOW, stroke_width=3,
        ).shift(DOWN * 0.3)
        eu_text = Text("ЕВРОПА", font_size=28, color=YELLOW, weight=BOLD)
        eu_text.move_to(eu_shape)
        self.play(FadeIn(eu_shape), Write(eu_text), run_time=0.8)

        # North — Arctic
        north = callout("Север: Северен Леден Океан", width=4.6, bg="#0a2a4a",
                        border=BLUE, font_size=20)
        north.next_to(eu_shape, UP, buff=0.3)
        n_arrow = Arrow(north.get_bottom(), eu_shape.get_top(), color=BLUE, buff=0.05)

        # South — Mediterranean
        south = callout("Југ: Средоземно Море", width=4.6, bg="#3a2a0a",
                        border=ORANGE, font_size=20)
        south.next_to(eu_shape, DOWN, buff=0.3)
        s_arrow = Arrow(south.get_top(), eu_shape.get_bottom(), color=ORANGE, buff=0.05)

        # West — Atlantic
        west = callout("Запад: Атлантски Океан", width=3.8, bg="#0a2a4a",
                        border=BLUE, font_size=18)
        west.next_to(eu_shape, LEFT, buff=0.4)
        w_arrow = Arrow(west.get_right(), eu_shape.get_left(), color=BLUE, buff=0.05)

        # East — Asia / Urals
        east = callout("Исток: Урал → Азија", width=3.8, bg="#2a1a3a",
                        border=PURPLE, font_size=18)
        east.next_to(eu_shape, RIGHT, buff=0.4)
        e_arrow = Arrow(east.get_left(), eu_shape.get_right(), color=PURPLE, buff=0.05)

        self.play(FadeIn(north, shift=DOWN * 0.2), GrowArrow(n_arrow), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(south, shift=UP * 0.2), GrowArrow(s_arrow), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(west, shift=RIGHT * 0.2), GrowArrow(w_arrow), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(east, shift=LEFT * 0.2), GrowArrow(e_arrow), run_time=0.7)
        self.wait(0.6)

        punch = Text("Граница на исток — единствено копнена.",
                     font_size=24, color=YELLOW, slant=ITALIC)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=0.9)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(eu_shape, eu_text, north, south, west, east,
                           n_arrow, s_arrow, w_arrow, e_arrow, punch, t3)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 4.  ПОВРШИНА                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("povrshina")

        t4 = section_title("Колку е голема?", color=GREEN)
        self.play(Write(t4), run_time=0.8)

        area_num = Text("10.500.000", font_size=72, color=YELLOW, weight=BOLD)
        area_unit = Text("км²", font_size=44, color=WHITE2)
        area_grp = VGroup(area_num, area_unit).arrange(RIGHT, buff=0.3).shift(UP * 0.5)
        self.play(Write(area_num), run_time=1.2)
        self.play(FadeIn(area_unit, shift=LEFT * 0.2), run_time=0.5)

        sub = Text("≈ 7% од копното на Земјата",
                   font_size=26, color=BLUE).next_to(area_grp, DOWN, buff=0.6)
        self.play(FadeIn(sub), run_time=0.6)

        # Continent ranking
        rank_title = Text("Континентите по големина:",
                          font_size=22, color=WHITE2).next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(rank_title), run_time=0.5)

        ranks = VGroup(
            Text("1. Азија    2. Африка    3. Северна Америка",
                 font_size=20, color=GREY),
            Text("4. Јужна Америка    5. Антарктик    6. ЕВРОПА",
                 font_size=20, color=YELLOW),
            Text("7. Австралија",
                 font_size=20, color=GREY),
        ).arrange(DOWN, buff=0.25).next_to(rank_title, DOWN, buff=0.3)

        for r in ranks:
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.5)

        self.wait(0.6)
        small = Text("Втор најмал. Прв по влијание.",
                     font_size=24, color=ORANGE, slant=ITALIC)
        small.to_edge(DOWN, buff=0.3)
        self.play(Write(small), run_time=0.9)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(area_grp, sub, rank_title, ranks, small, t4)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 5.  БРЕГ — разгранетост                              ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("breg")

        t5 = section_title("Брег без крај", color=BLUE)
        self.play(Write(t5), run_time=0.8)

        # Compare two continents' coastline visually
        # Africa — smooth oval
        africa = Ellipse(width=2.6, height=3.4, color=ORANGE,
                         fill_color="#3a2a0a", fill_opacity=0.7, stroke_width=2)
        africa.shift(LEFT * 3.5 + DOWN * 0.4)
        af_lab = Text("Африка", font_size=22, color=ORANGE).next_to(africa, DOWN, buff=0.2)
        af_km = Text("30.500 км брег", font_size=18, color=WHITE2).next_to(af_lab, DOWN, buff=0.1)

        # Europe — jagged
        eu_points = []
        np.random.seed(7)
        for i in range(24):
            angle = i * (2 * np.pi / 24)
            r = 1.6 + 0.45 * np.sin(3 * angle) + 0.3 * np.cos(5 * angle)
            eu_points.append(np.array([r * np.cos(angle), r * np.sin(angle), 0]))
        europe = Polygon(*eu_points, color=BLUE,
                         fill_color="#0a2a4a", fill_opacity=0.7, stroke_width=2)
        europe.shift(RIGHT * 3.5 + DOWN * 0.4)
        eu_lab = Text("Европа", font_size=22, color=BLUE).next_to(europe, DOWN, buff=0.2)
        eu_km = Text("≈ 38.000 км брег", font_size=18, color=YELLOW).next_to(eu_lab, DOWN, buff=0.1)

        self.play(FadeIn(africa), FadeIn(europe), run_time=0.9)
        self.play(Write(af_lab), Write(eu_lab), run_time=0.6)
        self.play(FadeIn(af_km), FadeIn(eu_km), run_time=0.6)

        vs = Text("VS", font_size=36, color=YELLOW, weight=BOLD).shift(DOWN * 0.4)
        self.play(FadeIn(vs), run_time=0.4)

        self.wait(0.8)

        verdict = Text("Помала по површина — поголема по брег.",
                       font_size=26, color=YELLOW, slant=ITALIC).to_edge(UP, buff=1.4)
        # remove title to make room
        self.play(FadeOut(t5), run_time=0.3)
        self.play(Write(verdict), run_time=1.0)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(africa, europe, af_lab, eu_lab,
                           af_km, eu_km, vs, verdict)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 6.  ПОЛУОСТРОВИ                                      ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("poluostrovi")

        t6 = section_title("Четири големи полуострови", color=GREEN)
        self.play(Write(t6), run_time=0.8)

        peninsulas = [
            ("Скандинавски", "Север",  "800.000 км²", GREEN,  LEFT * 4.5 + UP * 1.0),
            ("Пиринејски",  "Запад",   "583.000 км²", BLUE,   LEFT * 1.5 + UP * 1.0),
            ("Апенински",   "Центар",  "131.000 км²", ORANGE, RIGHT * 1.5 + UP * 1.0),
            ("Балкански",   "Југоисток","505.000 км²", RED,    RIGHT * 4.5 + UP * 1.0),
        ]

        cards = []
        for name, pos_lab, area, color, pos in peninsulas:
            box = RoundedRectangle(
                width=2.6, height=2.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=2,
            ).move_to(pos)
            n = Text(name, font_size=20, color=color, weight=BOLD)
            n.move_to(box.get_center() + UP * 0.55)
            p = Text(pos_lab, font_size=16, color=WHITE2)
            p.move_to(box.get_center())
            a = Text(area, font_size=15, color=YELLOW)
            a.move_to(box.get_center() + DOWN * 0.55)
            grp = VGroup(box, n, p, a)
            cards.append(grp)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.55)
            self.wait(0.15)

        bottom_punch = VGroup(
            Text("Морето влегува длабоко.", font_size=26, color=BLUE),
            Text("Копното се простира кон морето.", font_size=26, color=GREEN),
            Text("Прегратка.", font_size=32, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.4)

        for line in bottom_punch:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(*cards, bottom_punch, t6)),
            run_time=0.7,
        )

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        final_title = Text("Положба = судбина.",
                           font_size=46, color=YELLOW, weight=BOLD)
        final_title.to_edge(UP, buff=0.8)
        self.play(Write(final_title), run_time=1.1)

        summary = VGroup(
            Text("35°–71° СГШ. Северна хемисфера.",
                 font_size=26, color=WHITE2),
            Text("Три океани. Едно копно. Илјадници километри брег.",
                 font_size=24, color=BLUE),
            Text("Полуострови — прсти што бараат сонце.",
                 font_size=24, color=GREEN, slant=ITALIC),
            Text("Европа не седи.",
                 font_size=30, color=ORANGE, weight=BOLD),
            Text("Се отвора.",
                 font_size=36, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(final_title, DOWN, buff=0.6)

        for line in summary:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(2.0)
        self.play(FadeOut(VGroup(final_title, summary)), run_time=0.8)
        self.wait(0.4)
