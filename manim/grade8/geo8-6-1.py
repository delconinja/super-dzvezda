"""
geo8-6-1  —  Германија — водечка држава на Европа
Географија 8, Единица 6: Средна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as characters, history as drama, rivers as elders.
Render:  manim -ql geo8-6-1.py Geo861Scene
Output:  media/videos/geo8-6-1/480p15/Geo861Scene.mp4
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


def city_dot(name, pos, color=YELLOW, fs=22):
    dot = Dot(point=pos, color=color, radius=0.12)
    lbl = Text(name, font_size=fs, color=WHITE2, weight=BOLD)
    lbl.next_to(dot, UP, buff=0.12)
    return VGroup(dot, lbl)


def stat_card(value, label, color, pos, w=2.6, h=1.6):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    v = Text(value, font_size=34, color=color, weight=BOLD)
    l = Text(label, font_size=18, color=WHITE2)
    v.move_to(box.get_center() + UP * 0.25)
    l.next_to(v, DOWN, buff=0.15)
    return VGroup(box, v, l)


class Geo861Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — "Германија беше поделена"              ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Германија беше поделена.", font_size=54, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.6)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Запад и Исток.", font_size=42, color=ORANGE, weight=BOLD),
            Text("Ѕид помеѓу.", font_size=42, color=RED, weight=BOLD),
            Text("1989 — паднал.", font_size=38, color=BLUE),
            Text("1990 — обединување.", font_size=38, color=GREEN, weight=BOLD),
            Text("Денес — мотор на Европа.", font_size=40, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.9)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ПОЛОЖБА И ОСНОВНИ ПОДАТОЦИ                    ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("polozba")

        title = section_title("Германија — основни податоци")
        self.play(FadeIn(title), run_time=0.6)

        # silhouette of Germany (stylized polygon)
        germany_shape = Polygon(
            [-1.6, 2.4, 0], [-0.6, 2.6, 0], [0.4, 2.2, 0], [1.4, 2.4, 0],
            [1.8, 1.4, 0], [1.6, 0.4, 0], [1.9, -0.6, 0], [1.2, -1.6, 0],
            [0.6, -2.4, 0], [-0.4, -2.2, 0], [-1.0, -1.4, 0], [-1.6, -0.8, 0],
            [-2.0, 0.2, 0], [-1.8, 1.4, 0],
            fill_color="#1a3a5c", fill_opacity=0.8,
            stroke_color=YELLOW, stroke_width=2,
        ).scale(0.9).shift(LEFT * 3.5 + DOWN * 0.2)
        self.play(DrawBorderThenFill(germany_shape), run_time=1.5)

        # Berlin marker
        berlin = city_dot("Берлин", germany_shape.get_center() + RIGHT * 0.6 + UP * 0.5, color=RED)
        self.play(GrowFromCenter(berlin[0]), Write(berlin[1]), run_time=0.7)

        # Data cards on the right
        cards = VGroup(
            stat_card("83 мил.", "жители", BLUE, ORIGIN),
            stat_card("357.000", "км²", GREEN, ORIGIN),
            stat_card("16", "сојузни единици", ORANGE, ORIGIN),
            stat_card("EU + НАТО", "членка", PURPLE, ORIGIN),
        ).arrange_in_grid(rows=2, cols=2, buff=0.3).shift(RIGHT * 3.0 + DOWN * 0.2)

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.5)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title, germany_shape, berlin, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  СОСЕДИ — Германија во срце на Европа          ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sosedi")

        title2 = section_title("Срце на Европа", color=GREEN)
        self.play(FadeIn(title2), run_time=0.6)

        center_box = RoundedRectangle(
            width=2.4, height=1.4, corner_radius=0.2,
            fill_color=YELLOW, fill_opacity=0.9, stroke_color=WHITE2,
        ).move_to(ORIGIN + DOWN * 0.2)
        center_lbl = Text("ГЕРМАНИЈА", font_size=24, color="#0d1b2e", weight=BOLD).move_to(center_box)

        self.play(GrowFromCenter(center_box), Write(center_lbl), run_time=0.8)

        neighbours = [
            ("Данска", UP * 2.4, BLUE),
            ("Полска", UP * 1.2 + RIGHT * 3.5, RED),
            ("Чешка", DOWN * 0.6 + RIGHT * 3.5, ORANGE),
            ("Австрија", DOWN * 2.0 + RIGHT * 2.0, GREEN),
            ("Швајцарија", DOWN * 2.4, PURPLE),
            ("Франција", DOWN * 1.0 + LEFT * 3.5, BLUE),
            ("Холандија", UP * 0.8 + LEFT * 3.5, ORANGE),
            ("Белгија/Лук.", UP * 2.0 + LEFT * 2.5, GREEN),
        ]

        nbox_group = VGroup()
        line_group = VGroup()
        for name, pos, col in neighbours:
            b = RoundedRectangle(width=1.8, height=0.6, corner_radius=0.1,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=col, stroke_width=2).move_to(pos + DOWN * 0.2)
            lab = Text(name, font_size=18, color=col).move_to(b)
            nbox_group.add(VGroup(b, lab))
            line_group.add(Line(center_box.get_center(), b.get_center(),
                                stroke_color=col, stroke_width=1).set_opacity(0.5))

        for ln, nb in zip(line_group, nbox_group):
            self.play(Create(ln), FadeIn(nb), run_time=0.3)

        self.wait(0.4)
        nine = Text("9 соседи. Никој не е сам со толку соседи.",
                    font_size=28, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(nine), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, center_box, center_lbl, nbox_group, line_group, nine)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ИСТОРИЈА — Ѕидот од Берлин                    ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zid")

        title3 = section_title("Берлинскиот ѕид", color=RED)
        self.play(FadeIn(title3), run_time=0.6)

        # Wall visual
        west = RoundedRectangle(width=4.5, height=2.0, corner_radius=0.2,
                                fill_color=BLUE, fill_opacity=0.6,
                                stroke_color=WHITE2, stroke_width=2).shift(LEFT * 2.6)
        west_lbl = Text("ЗАПАД\n(СРГ)", font_size=26, color=WHITE2, weight=BOLD).move_to(west)

        east = RoundedRectangle(width=4.5, height=2.0, corner_radius=0.2,
                                fill_color=RED, fill_opacity=0.6,
                                stroke_color=WHITE2, stroke_width=2).shift(RIGHT * 2.6)
        east_lbl = Text("ИСТОК\n(ДДР)", font_size=26, color=WHITE2, weight=BOLD).move_to(east)

        wall = Rectangle(width=0.25, height=2.4,
                         fill_color=GREY, fill_opacity=1,
                         stroke_color=YELLOW, stroke_width=2)

        self.play(FadeIn(west), Write(west_lbl), FadeIn(east), Write(east_lbl), run_time=1.0)
        self.play(GrowFromCenter(wall), run_time=0.7)

        year1 = Text("1961 — ѕидот ѕида.", font_size=30, color=WHITE2).to_edge(DOWN, buff=1.6)
        year2 = Text("28 години — фамилии раздвоени.", font_size=26, color=ORANGE).next_to(year1, DOWN, buff=0.15)
        year3 = Text("1989 — народот тргна.", font_size=30, color=YELLOW, weight=BOLD).next_to(year2, DOWN, buff=0.15)

        self.play(Write(year1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(year2), run_time=0.8)
        self.wait(0.3)
        self.play(Write(year3), run_time=0.9)
        self.wait(0.6)

        # Wall falls
        self.play(wall.animate.shift(DOWN * 4).set_opacity(0), run_time=1.2)
        self.play(west.animate.set_fill(GREEN, opacity=0.6),
                  east.animate.set_fill(GREEN, opacity=0.6),
                  FadeOut(west_lbl), FadeOut(east_lbl), run_time=1.0)

        united = Text("3 октомври 1990 — една Германија.",
                      font_size=34, color=GREEN, weight=BOLD).move_to(ORIGIN)
        self.play(Write(united), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, west, east, year1, year2, year3, united)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ЕКОНОМИЈА — мотор на Европа                   ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ekonomija")

        title4 = section_title("Мотор на Европа", color=ORANGE)
        self.play(FadeIn(title4), run_time=0.6)

        intro = Text("Германија = најголема економија во ЕУ.",
                     font_size=30, color=WHITE2).next_to(title4, DOWN, buff=0.4)
        self.play(Write(intro), run_time=1.0)
        self.wait(0.5)

        brands = VGroup(
            stat_card("BMW", "Минхен", BLUE, ORIGIN),
            stat_card("Mercedes", "Штутгарт", YELLOW, ORIGIN),
            stat_card("VW", "Волфсбург", GREEN, ORIGIN),
            stat_card("Audi", "Инголштат", RED, ORIGIN),
        ).arrange(RIGHT, buff=0.3).next_to(intro, DOWN, buff=0.5)

        for b in brands:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.4)

        below = Text("Автомобили. Машини. Хемија.",
                     font_size=30, color=YELLOW, weight=BOLD).next_to(brands, DOWN, buff=0.5)
        below2 = Text("Светот купува „Made in Germany“.",
                      font_size=26, color=WHITE2).next_to(below, DOWN, buff=0.2)

        self.play(Write(below), run_time=0.9)
        self.play(Write(below2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title4, intro, brands, below, below2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЛЈЕФ И РЕКА РАЈНА                           ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("relief")

        title5 = section_title("Рајна — реката-старец", color=BLUE)
        self.play(FadeIn(title5), run_time=0.6)

        # Rhine winding line
        rhine = VMobject(stroke_color=BLUE, stroke_width=8)
        rhine.set_points_smoothly([
            np.array([-5.0, -2.5, 0]),
            np.array([-4.2, -1.5, 0]),
            np.array([-3.8, -0.4, 0]),
            np.array([-3.2, 0.6, 0]),
            np.array([-2.4, 1.4, 0]),
            np.array([-1.8, 2.0, 0]),
            np.array([-1.0, 2.4, 0]),
            np.array([0.0, 2.8, 0]),
        ])
        self.play(Create(rhine), run_time=2.0)

        cities = VGroup(
            city_dot("Базел", np.array([-5.0, -2.5, 0]), color=YELLOW),
            city_dot("Келн", np.array([-2.4, 1.4, 0]), color=ORANGE),
            city_dot("Северно море", np.array([0.0, 2.8, 0]), color=BLUE),
        )
        for c in cities:
            self.play(GrowFromCenter(c[0]), Write(c[1]), run_time=0.5)

        # Bavaria, Black Forest cards
        bav = stat_card("Баварија", "најголема покраина", GREEN, RIGHT * 3.2 + UP * 1.5)
        bf = stat_card("Шварцвалд", "црна шума", PURPLE, RIGHT * 3.2 + DOWN * 0.4)
        alps = stat_card("Алпи", "јужна граница", ORANGE, RIGHT * 3.2 + DOWN * 2.2)

        self.play(FadeIn(bav, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(bf, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(alps, shift=LEFT * 0.2), run_time=0.5)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title5, rhine, cities, bav, bf, alps)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК — Што да запомниме                   ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        title6 = section_title("Што да запомниме", color=YELLOW)
        self.play(FadeIn(title6), run_time=0.6)

        bullets = VGroup(
            callout("83 милиони жители — најмногунаселена во ЕУ", width=11, border=BLUE),
            callout("16 сојузни единици — федеративна држава", width=11, border=GREEN),
            callout("Берлин — главен град, симбол на обединувањето", width=11, border=RED),
            callout("Рајна — најважна река, длабока артерија", width=11, border=ORANGE),
            callout("Автомобилска индустрија — водечка во светот", width=11, border=YELLOW),
        ).arrange(DOWN, buff=0.25).next_to(title6, DOWN, buff=0.4)

        for b in bullets:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.45)

        self.wait(0.6)

        final = Text("Германија. Поделена. Обединета. Силна.",
                     font_size=34, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(final), run_time=1.2)
        self.wait(2.2)

        self.play(FadeOut(VGroup(title6, bullets, final)), run_time=0.8)
        self.wait(0.5)
