"""
geo8-4-2  —  Франција и Бенелукс
Географија 8, Единица 4: Западна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as personalities — France stylish, Holland rational,
Belgium multilingual, Luxembourg rich. Four states. One philosophy.
Render:  manim -ql geo8-4-2.py Geo842Scene
Output:  media/videos/geo8-4-2/480p15/Geo842Scene.mp4
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


def country_card(name, capital, trait, color, pos, width=3.0):
    box = RoundedRectangle(
        width=width, height=2.2, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=22, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.65)
    cap = Text(capital, font_size=16, color=WHITE2)
    cap.move_to(box.get_center() + UP * 0.1)
    tr = Text(trait, font_size=14, color=GREY)
    tr.move_to(box.get_center() + DOWN * 0.5)
    return VGroup(box, nm, cap, tr)


def sector_chip(name, color, pos):
    box = RoundedRectangle(
        width=2.6, height=0.7, corner_radius=0.35,
        fill_color=color, fill_opacity=0.85,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=18, color="#0d1b2e", weight=BOLD)
    nm.move_to(box)
    return VGroup(box, nm)


class Geo842Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Франција има стил.", font_size=38, color=PURPLE, weight=BOLD)
        h2 = Text("Холандија — рационалност.", font_size=34, color=ORANGE, weight=BOLD)
        h3 = Text("Белгија — јазици.", font_size=34, color=YELLOW, weight=BOLD)
        h4 = Text("Луксембург — пари.", font_size=34, color=GREEN, weight=BOLD)
        h5 = Text("Четири држави. Една филозофија: соработка.",
                  font_size=28, color=WHITE2)

        hook = VGroup(h1, h2, h3, h4, h5).arrange(DOWN, buff=0.35)

        self.play(Write(h1), run_time=1.0)
        self.play(Write(h2), run_time=0.9)
        self.play(Write(h3), run_time=0.9)
        self.play(Write(h4), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(h5, shift=UP * 0.3), run_time=1.0)
        self.wait(2.2)
        self.play(FadeOut(hook), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  FRANCE — THE STYLISH GIANT                      ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("france")

        t2 = section_title("Франција — најголема во Западна Европа", color=PURPLE)
        self.play(Write(t2), run_time=1.0)

        # Hexagon France (l'hexagone)
        hex_france = RegularPolygon(n=6, radius=2.0, color=PURPLE,
                                    stroke_width=4,
                                    fill_color=PURPLE, fill_opacity=0.22)
        hex_france.move_to(LEFT * 3.5 + DOWN * 0.2)
        hex_lbl = Text("Шестаголник", font_size=18, color=PURPLE)
        hex_lbl.move_to(hex_france.get_center() + DOWN * 0.0)
        paris = Dot(hex_france.get_center() + UP * 0.6, radius=0.14, color=YELLOW)
        paris_lbl = Text("Париз", font_size=18, color=YELLOW, weight=BOLD)
        paris_lbl.next_to(paris, RIGHT, buff=0.15)

        self.play(Create(hex_france), Write(hex_lbl), run_time=1.2)
        self.play(FadeIn(paris), Write(paris_lbl), run_time=0.7)

        # Eiffel tower stylized
        tower_base = Polygon(
            np.array([1.5, -1.5, 0]), np.array([2.5, -1.5, 0]),
            np.array([2.3, -0.8, 0]), np.array([1.7, -0.8, 0]),
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.6
        )
        tower_mid = Polygon(
            np.array([1.7, -0.8, 0]), np.array([2.3, -0.8, 0]),
            np.array([2.15, 0.2, 0]), np.array([1.85, 0.2, 0]),
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.6
        )
        tower_top = Polygon(
            np.array([1.85, 0.2, 0]), np.array([2.15, 0.2, 0]),
            np.array([2.0, 1.2, 0]),
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.7
        )
        tower = VGroup(tower_base, tower_mid, tower_top)
        tower_lbl = Text("Ајфелова кула", font_size=18, color=YELLOW)
        tower_lbl.next_to(tower, DOWN, buff=0.2)

        self.play(FadeIn(tower), Write(tower_lbl), run_time=1.2)

        sectors_fr = VGroup(
            sector_chip("Вино",         RED,    RIGHT * 4.5 + UP * 1.5),
            sector_chip("Мода",         PURPLE, RIGHT * 4.5 + UP * 0.6),
            sector_chip("Земјоделство", GREEN,  RIGHT * 4.5 + DOWN * 0.3),
            sector_chip("Аеробус",      BLUE,   RIGHT * 4.5 + DOWN * 1.2),
        )
        self.play(LaggedStart(*[FadeIn(s, shift=LEFT * 0.3) for s in sectors_fr],
                              lag_ratio=0.2), run_time=1.4)
        self.wait(1.0)

        co2 = callout("68 мил. жители. Најпосетувана земја во светот.",
                      width=11.0, bg="#2a1230", border=PURPLE, font_size=26)
        co2.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(co2, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t2), FadeOut(hex_france), FadeOut(hex_lbl), FadeOut(paris),
                  FadeOut(paris_lbl), FadeOut(tower), FadeOut(tower_lbl),
                  FadeOut(sectors_fr), FadeOut(co2), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  BENELUX — THREE FOUNDERS                        ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("benelux")

        t3 = section_title("Бенелукс — три држави, едно име", color=ORANGE)
        self.play(Write(t3), run_time=1.0)

        be = country_card("Белгија", "Брисел", "11 мил. жители", YELLOW,
                          LEFT * 4.0 + UP * 0.3, width=3.4)
        ne = country_card("Холандија", "Амстердам", "17 мил. жители", ORANGE,
                          UP * 0.3, width=3.4)
        lu = country_card("Луксембург", "Луксембург", "660 илј. жители", GREEN,
                          RIGHT * 4.0 + UP * 0.3, width=3.4)

        self.play(FadeIn(be, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(ne, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(lu, shift=UP * 0.3), run_time=0.7)
        self.wait(0.5)

        # union arrows
        a1 = Arrow(be.get_right(), ne.get_left(), color=WHITE2,
                   buff=0.1, stroke_width=4)
        a2 = Arrow(ne.get_right(), lu.get_left(), color=WHITE2,
                   buff=0.1, stroke_width=4)
        self.play(Create(a1), Create(a2), run_time=1.0)

        bnx_lbl = Text("Be + Ne + Lux = Бенелукс", font_size=28,
                       color=YELLOW, weight=BOLD)
        bnx_lbl.to_edge(DOWN, buff=1.2)
        self.play(Write(bnx_lbl), run_time=1.2)

        co3 = callout("Основачи на Европската Унија — 1957.",
                      width=10.5, bg="#2a1810", border=ORANGE, font_size=26)
        co3.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co3, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t3), FadeOut(be), FadeOut(ne), FadeOut(lu),
                  FadeOut(a1), FadeOut(a2), FadeOut(bnx_lbl), FadeOut(co3),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  BRUSSELS — EU CAPITAL                           ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("brussels")

        t4 = section_title("Брисел — главен град на Европа", color=BLUE)
        self.play(Write(t4), run_time=1.0)

        # EU stars circle
        center = ORIGIN + UP * 0.3
        stars = VGroup()
        for i in range(12):
            angle = i * TAU / 12 + PI / 2
            pos = center + 2.0 * np.array([np.cos(angle), np.sin(angle), 0])
            star = Star(n=5, outer_radius=0.2, inner_radius=0.08,
                        color=YELLOW, fill_color=YELLOW, fill_opacity=1)
            star.move_to(pos)
            stars.add(star)

        eu_circle = Circle(radius=2.0, color=BLUE, stroke_width=3)
        eu_circle.move_to(center)
        eu_txt = Text("ЕУ", font_size=44, color=BLUE, weight=BOLD).move_to(center)

        self.play(Create(eu_circle), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(s, scale=0.3) for s in stars],
                              lag_ratio=0.07), run_time=1.4)
        self.play(Write(eu_txt), run_time=0.8)
        self.wait(0.5)

        hq = VGroup(
            Text("• Европска комисија", font_size=22, color=WHITE2),
            Text("• НАТО штаб", font_size=22, color=WHITE2),
            Text("• Европски парламент", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        hq.to_edge(DOWN, buff=0.6)
        self.play(Write(hq), run_time=1.6)
        self.wait(2.0)
        self.play(FadeOut(t4), FadeOut(stars), FadeOut(eu_circle), FadeOut(eu_txt),
                  FadeOut(hq), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ROTTERDAM & ANTWERP — PORTS                     ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ports")

        t5 = section_title("Ротердам и Антверпен — врати на Европа", color=BLUE)
        self.play(Write(t5), run_time=1.0)

        # Sea (bottom band)
        sea = Rectangle(width=14, height=2.5, color=BLUE,
                        fill_color=BLUE, fill_opacity=0.3, stroke_width=0)
        sea.to_edge(DOWN, buff=0.0)
        self.play(FadeIn(sea), run_time=0.6)

        # Cargo ships
        ship1 = VGroup(
            Polygon(np.array([-1, 0, 0]), np.array([1, 0, 0]),
                    np.array([0.8, -0.4, 0]), np.array([-0.8, -0.4, 0]),
                    color=GREY, fill_color=GREY, fill_opacity=1),
            Rectangle(width=0.6, height=0.4, color=RED,
                      fill_color=RED, fill_opacity=1).shift(UP * 0.2 + LEFT * 0.2),
            Rectangle(width=0.6, height=0.4, color=YELLOW,
                      fill_color=YELLOW, fill_opacity=1).shift(UP * 0.2 + RIGHT * 0.4),
        ).move_to(LEFT * 4 + DOWN * 0.9)
        ship2 = ship1.copy().move_to(RIGHT * 2 + DOWN * 1.1).scale(0.85)

        self.play(FadeIn(ship1), FadeIn(ship2), run_time=0.9)
        self.play(ship1.animate.shift(RIGHT * 1.5),
                  ship2.animate.shift(RIGHT * 1.5), run_time=2.0)

        port_facts = VGroup(
            Text("Ротердам — најголемо пристаниште во Европа", font_size=22, color=ORANGE),
            Text("Антверпен — дијаманти и хемија", font_size=20, color=YELLOW),
            Text("Стоки за цела Европа поминуваат тука.", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.18).to_edge(UP, buff=1.5)
        self.play(Write(port_facts), run_time=1.6)
        self.wait(2.0)
        self.play(FadeOut(t5), FadeOut(sea), FadeOut(ship1), FadeOut(ship2),
                  FadeOut(port_facts), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  POLDERS — LAND BELOW THE SEA                    ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("polders")

        t6 = section_title("Полдери — земја под морето", color=ORANGE)
        self.play(Write(t6), run_time=1.0)

        # Cross section
        sea_lvl = Line(LEFT * 6 + UP * 1.0, RIGHT * 6 + UP * 1.0,
                       color=BLUE, stroke_width=3)
        sea_lbl = Text("Морско ниво", font_size=18, color=BLUE)
        sea_lbl.next_to(sea_lvl, UP, buff=0.05).align_to(sea_lvl, LEFT).shift(RIGHT * 0.5)

        # water on left (sea)
        sea_water = Polygon(
            np.array([-6, 1.0, 0]), np.array([-1.5, 1.0, 0]),
            np.array([-1.5, -2.5, 0]), np.array([-6, -2.5, 0]),
            color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=0,
        )
        # dike
        dike = Polygon(
            np.array([-1.5, 1.3, 0]), np.array([-1.0, 1.3, 0]),
            np.array([-0.8, -2.5, 0]), np.array([-1.7, -2.5, 0]),
            color=GREY, fill_color=GREY, fill_opacity=1, stroke_color=GREY,
        )
        # polder land (below sea level)
        polder = Polygon(
            np.array([-1.0, 0.2, 0]), np.array([6, 0.2, 0]),
            np.array([6, -2.5, 0]), np.array([-0.8, -2.5, 0]),
            color=GREEN, fill_color=GREEN, fill_opacity=0.4, stroke_width=0,
        )

        self.play(Create(sea_lvl), Write(sea_lbl), run_time=0.9)
        self.play(FadeIn(sea_water), run_time=0.8)
        self.play(FadeIn(dike), run_time=0.7)
        self.play(FadeIn(polder), run_time=0.8)

        dike_lbl = Text("Брана", font_size=18, color=GREY, weight=BOLD)
        dike_lbl.move_to(dike).rotate(-PI / 2)
        polder_lbl = Text("Полдер — −2 м", font_size=22, color=GREEN, weight=BOLD)
        polder_lbl.move_to(polder.get_center() + UP * 0.4)

        # windmill
        windmill_pole = Line(RIGHT * 3 + DOWN * 0.5, RIGHT * 3 + DOWN * 2.0,
                             color=YELLOW, stroke_width=4)
        blade1 = Line(ORIGIN, RIGHT * 0.7, color=YELLOW, stroke_width=3)
        blade2 = Line(ORIGIN, UP * 0.7, color=YELLOW, stroke_width=3)
        blade3 = Line(ORIGIN, LEFT * 0.7, color=YELLOW, stroke_width=3)
        blade4 = Line(ORIGIN, DOWN * 0.7, color=YELLOW, stroke_width=3)
        blades = VGroup(blade1, blade2, blade3, blade4).move_to(RIGHT * 3 + DOWN * 0.5)

        self.play(Write(dike_lbl), Write(polder_lbl), run_time=1.0)
        self.play(Create(windmill_pole), Create(blades), run_time=0.8)
        self.play(Rotate(blades, angle=2 * PI,
                         about_point=RIGHT * 3 + DOWN * 0.5), run_time=2.0)

        co6 = callout("Холандија: 1/4 од земјата — под морско ниво.",
                      width=11.0, bg="#2a1810", border=ORANGE, font_size=26)
        co6.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(co6, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t6), FadeOut(sea_lvl), FadeOut(sea_lbl), FadeOut(sea_water),
                  FadeOut(dike), FadeOut(polder), FadeOut(dike_lbl),
                  FadeOut(polder_lbl), FadeOut(windmill_pole), FadeOut(blades),
                  FadeOut(co6), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        f1 = Text("Франција.", font_size=44, color=PURPLE, weight=BOLD)
        f2 = Text("Холандија. Белгија. Луксембург.", font_size=34, color=ORANGE)
        f3 = Text("Срцето на Западна Европа.", font_size=32, color=YELLOW)
        f4 = Text("Соработка.", font_size=46, color=GREEN, weight=BOLD)

        finale = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.45)
        self.play(Write(f1), run_time=1.0)
        self.play(FadeIn(f2, shift=UP * 0.3), run_time=1.0)
        self.play(Write(f3), run_time=1.0)
        self.wait(0.4)
        self.play(Write(f4), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(finale), run_time=1.0)
