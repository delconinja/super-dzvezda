"""
geo8-1-4  —  Хидрографија и природни ресурси
Географија 8, Единица 1: Природно-географски карактеристики на Европа

Teaching narrative — Andonovski-style: three-beat punches,
rivers as bloodstream, seas as friends, resources as inheritance.
Render:  manim -ql geo8-1-4.py Geo814Scene
Output:  media/videos/geo8-1-4/480p15/Geo814Scene.mp4
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


def river_card(name, length_km, countries, color, pos):
    box = RoundedRectangle(
        width=3.0, height=2.0, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    n = Text(name, font_size=22, color=color, weight=BOLD)
    n.move_to(box.get_center() + UP * 0.55)
    l = Text(length_km, font_size=20, color=YELLOW)
    l.move_to(box.get_center() + UP * 0.05)
    c = Text(countries, font_size=14, color=WHITE2)
    c.move_to(box.get_center() + DOWN * 0.45)
    return VGroup(box, n, l, c)


def resource_card(icon, name, where, color, pos):
    box = RoundedRectangle(
        width=2.8, height=2.0, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    i = Text(icon, font_size=34, color=color, weight=BOLD)
    i.move_to(box.get_center() + UP * 0.45)
    n = Text(name, font_size=18, color=WHITE2, weight=BOLD)
    n.move_to(box.get_center() + DOWN * 0.05)
    w = Text(where, font_size=14, color=color)
    w.move_to(box.get_center() + DOWN * 0.5)
    return VGroup(box, i, n, w)


class Geo814Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Реките се крвотокот на Европа.",
                     font_size=40, color=BLUE, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.3)
        self.wait(0.3)

        beats = VGroup(
            Text("Дунав тече низ 10 држави.", font_size=32, color=WHITE2),
            Text("Рајна носи стока.",         font_size=32, color=ORANGE),
            Text("Волга ja храни Русија.",    font_size=32, color=YELLOW),
            Text("Без нив — нема цивилизација.",
                 font_size=34, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.4)
        self.play(FadeOut(hook1), FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ГОЛЕМИТЕ РЕКИ                                    ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("reki")

        t2 = section_title("Пет големи реки", color=BLUE)
        self.play(Write(t2), run_time=0.9)

        r1 = river_card("Волга",  "3530 км",  "Русија", BLUE,
                        LEFT * 4.8 + UP * 0.6)
        r2 = river_card("Дунав",  "2860 км",  "10 држави", YELLOW,
                        LEFT * 1.6 + UP * 0.6)
        r3 = river_card("Дњепар", "2201 км",  "Русија, Белорусија, Украина", GREEN,
                        RIGHT * 1.6 + UP * 0.6)
        r4 = river_card("Рајна",  "1233 км",  "Швајцарија → Холандија", ORANGE,
                        RIGHT * 4.8 + UP * 0.6)
        r5 = river_card("Елба",   "1094 км",  "Чешка → Германија", PURPLE,
                        LEFT * 3.2 + DOWN * 1.8)

        # central note
        center_note = callout("Дунав не престанува. Тече од Шварцвалд. До Црно Море.",
                              width=6.0, bg=DARK_CARD, border=YELLOW, font_size=20)
        center_note.shift(RIGHT * 1.6 + DOWN * 1.8)

        for r in [r1, r2, r3, r4]:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.55)
            self.wait(0.12)

        self.play(FadeIn(r5, shift=UP * 0.2), FadeIn(center_note, shift=LEFT * 0.2),
                  run_time=0.7)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(r1, r2, r3, r4, r5, center_note, t2)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 3.  ДУНАВ — низ десет држави                         ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dunav")

        t3 = section_title("Дунав — реката што спојува", color=YELLOW)
        self.play(Write(t3), run_time=0.9)

        # Source label
        source = Text("Шварцвалд\n(Германија)", font_size=18, color=GREEN, weight=BOLD)
        source.shift(LEFT * 5.5 + UP * 1.5)
        # Mouth label
        mouth = Text("Црно Море\n(Романија)", font_size=18, color=BLUE, weight=BOLD)
        mouth.shift(RIGHT * 5.5 + DOWN * 1.0)

        self.play(Write(source), Write(mouth), run_time=0.8)

        # Wavy river path
        river_path = ParametricFunction(
            lambda t: np.array([
                -4.8 + 9.6 * t,
                1.0 - 1.6 * t + 0.6 * np.sin(t * PI * 3),
                0,
            ]),
            t_range=[0, 1],
            color=BLUE, stroke_width=6,
        )
        self.play(Create(river_path), run_time=2.2)

        end_pt = river_path.get_end()
        tail_pt = river_path.point_from_proportion(0.94)
        arr = Arrow(tail_pt, end_pt, color=BLUE, buff=0,
                    stroke_width=5, max_tip_length_to_length_ratio=0.4)
        self.play(GrowArrow(arr), run_time=0.4)

        # Ten countries
        countries = [
            "Германија", "Австрија", "Словачка", "Унгарија", "Хрватска",
            "Србија",    "Бугарија", "Романија", "Молдавија", "Украина",
        ]
        country_grp = VGroup(*[
            Text(c, font_size=14, color=WHITE2) for c in countries
        ]).arrange_in_grid(rows=2, cols=5, buff=(0.4, 0.2))
        country_grp.to_edge(DOWN, buff=0.5)

        for c in country_grp:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.25)

        km = Text("2860 километри. Без пауза.",
                  font_size=24, color=YELLOW, weight=BOLD)
        km.to_edge(DOWN, buff=0.15)
        # remove country grid to make room? keep — move km above
        self.play(country_grp.animate.shift(UP * 0.3), run_time=0.3)
        self.play(Write(km), run_time=0.8)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(river_path, arr, source, mouth, country_grp, km, t3)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 4.  МОРИЊА И ЕЗЕРА                                   ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("morinja")

        t4 = section_title("Мориња на Европа", color=BLUE)
        self.play(Write(t4), run_time=0.9)

        seas = [
            ("Средоземно", "≈ 2.5 мил. км²", "југ", YELLOW,  LEFT * 4.5 + UP * 0.3),
            ("Балтичко",   "≈ 415.000 км²",  "север", BLUE,   LEFT * 1.5 + UP * 0.3),
            ("Црно",       "≈ 436.000 км²",  "југоисток", RED,  RIGHT * 1.5 + UP * 0.3),
            ("Касписко",   "≈ 371.000 км²",  "исток (езеро)", PURPLE,
             RIGHT * 4.5 + UP * 0.3),
        ]

        cards = []
        for name, area, pos_lab, col, pos in seas:
            box = RoundedRectangle(
                width=2.7, height=2.2, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            n = Text(name, font_size=22, color=col, weight=BOLD)
            n.move_to(box.get_center() + UP * 0.65)
            a = Text(area, font_size=15, color=YELLOW)
            a.move_to(box.get_center() + UP * 0.1)
            p = Text(pos_lab, font_size=14, color=WHITE2)
            p.move_to(box.get_center() + DOWN * 0.4)
            cards.append(VGroup(box, n, a, p))

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.55)
            self.wait(0.12)

        note = Text("Касписко — најголемо езеро во светот.",
                    font_size=22, color=PURPLE, slant=ITALIC).to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=1.0)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(*cards, note, t4)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 5.  ПРИРОДНИ РЕСУРСИ                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("resursi")

        t5 = section_title("Природни ресурси — наследство", color=GREEN)
        self.play(Write(t5), run_time=0.9)

        r1 = resource_card("Ј", "Јаглен", "Германија, Полска", GREY,
                           LEFT * 4.5 + UP * 0.5)
        r2 = resource_card("Н", "Нафта", "Северно Море", ORANGE,
                           LEFT * 1.5 + UP * 0.5)
        r3 = resource_card("Ж", "Железо", "Шведска", BLUE,
                           RIGHT * 1.5 + UP * 0.5)
        r4 = resource_card("Б", "Боксит", "Грција, Унгарија", RED,
                           RIGHT * 4.5 + UP * 0.5)
        r5 = resource_card("Г", "Гас", "Норвешка, Русија", YELLOW,
                           LEFT * 3.0 + DOWN * 1.8)
        r6 = resource_card("У", "Уранум", "Чешка, Франција", PURPLE,
                           DOWN * 1.8)
        r7 = resource_card("Д", "Дрво", "Финска, Шведска", GREEN,
                           RIGHT * 3.0 + DOWN * 1.8)

        for r in [r1, r2, r3, r4]:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.45)
            self.wait(0.08)
        for r in [r5, r6, r7]:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.45)
            self.wait(0.08)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(r1, r2, r3, r4, r5, r6, r7, t5)),
            run_time=0.7,
        )

        # ══════════════════════════════════════════════════════════
        # 6.  ШУМИ И ТУРИЗАМ                                   ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("shumi")

        t6 = section_title("Шуми и туризам — живо богатство", color=GREEN)
        self.play(Write(t6), run_time=0.9)

        # Pie: forest coverage
        circ = Circle(radius=1.6, color=WHITE2, stroke_width=2)
        circ.shift(LEFT * 3.8 + DOWN * 0.3)
        forest_sec = Sector(
            outer_radius=1.6,
            angle=2 * PI * 0.43,
            start_angle=PI / 2,
            fill_color=GREEN, fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=2,
        ).move_arc_center_to(circ.get_center())
        other_sec = Sector(
            outer_radius=1.6,
            angle=2 * PI * 0.57,
            start_angle=PI / 2 + 2 * PI * 0.43,
            fill_color=GREY, fill_opacity=0.6,
            stroke_color=GREY, stroke_width=2,
        ).move_arc_center_to(circ.get_center())

        self.play(Create(circ), run_time=0.4)
        self.play(FadeIn(forest_sec), run_time=0.6)
        forest_lab = Text("43%\nшуми", font_size=22, color=WHITE2, weight=BOLD)
        forest_lab.move_to(forest_sec.get_center_of_mass())
        self.play(Write(forest_lab), run_time=0.5)
        self.play(FadeIn(other_sec), run_time=0.5)
        other_lab = Text("57%\nдруго", font_size=18, color=WHITE2)
        other_lab.move_to(other_sec.get_center_of_mass())
        self.play(Write(other_lab), run_time=0.4)

        # Tourism cards
        tour = VGroup(
            callout("Туризам — водечка индустрија",
                    width=5.4, bg=DARK_CARD, border=YELLOW, font_size=22),
            callout("Алпи, Медитеран, главни градови",
                    width=5.4, bg=DARK_CARD, border=ORANGE, font_size=20),
            callout("≈ 700 милиони посетители годишно",
                    width=5.4, bg=DARK_CARD, border=BLUE, font_size=20),
        ).arrange(DOWN, buff=0.25).shift(RIGHT * 3.0 + DOWN * 0.3)

        for c in tour:
            self.play(FadeIn(c, shift=LEFT * 0.2), run_time=0.55)
            self.wait(0.15)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(circ, forest_sec, other_sec, forest_lab,
                           other_lab, tour, t6)),
            run_time=0.7,
        )

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        final_title = Text("Вода и руда — основа на сè.",
                           font_size=42, color=YELLOW, weight=BOLD)
        final_title.to_edge(UP, buff=0.8)
        self.play(Write(final_title), run_time=1.1)

        summary = VGroup(
            Text("Реките се крвотокот на Европа.",
                 font_size=26, color=BLUE),
            Text("Морињата — четири врати кон светот.",
                 font_size=24, color=GREEN),
            Text("Јаглен, нафта, железо — наследство на векови.",
                 font_size=22, color=ORANGE, slant=ITALIC),
            Text("Шумите дишат. Туризмот плаќа.",
                 font_size=24, color=RED),
            Text("Природата дава.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Луѓето градат.",
                 font_size=36, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(final_title, DOWN, buff=0.5)

        for line in summary:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)

        self.wait(2.0)
        self.play(FadeOut(VGroup(final_title, summary)), run_time=0.8)
        self.wait(0.4)
