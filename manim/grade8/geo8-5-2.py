"""
geo8-5-2  —  Балтички држави: Естонија, Латвија, Литванија
Географија 8, Единица 5: Северна Европа

Teaching narrative — Andonovski-style: three-beat punches,
three sisters — lost to USSR, returned with independence.
Today: European. Digital. Ambitious.
Render:  manim -ql geo8-5-2.py Geo852Scene
Output:  media/videos/geo8-5-2/480p15/Geo852Scene.mp4
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


def baltic_card(name, capital, pop, area, color, pos):
    box = RoundedRectangle(
        width=3.4, height=2.8, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=24, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 1.0)
    cap = Text(capital, font_size=18, color=WHITE2)
    cap.move_to(box.get_center() + UP * 0.4)
    p = Text(pop, font_size=15, color=YELLOW)
    p.move_to(box.get_center() + DOWN * 0.15)
    a = Text(area, font_size=14, color=GREY)
    a.move_to(box.get_center() + DOWN * 0.7)
    return VGroup(box, nm, cap, p, a)


def timeline_event(year, label, color, pos):
    dot = Dot(point=pos, radius=0.16, color=color)
    yr = Text(year, font_size=20, color=color, weight=BOLD)
    yr.next_to(dot, UP, buff=0.18)
    lb = Text(label, font_size=15, color=WHITE2)
    lb.next_to(dot, DOWN, buff=0.18)
    return VGroup(dot, yr, lb)


class Geo852Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Естонија.", font_size=44, color=BLUE,   weight=BOLD)
        h2 = Text("Латвија.",  font_size=44, color=RED,    weight=BOLD)
        h3 = Text("Литванија.",font_size=44, color=GREEN,  weight=BOLD)
        h4 = Text("Три сестри.", font_size=32, color=YELLOW)
        h5 = Text("Изгубени со СССР. Враќени со независност.",
                  font_size=24, color=WHITE2)
        h6 = Text("Денес — европски, дигитални, амбициозни.",
                  font_size=24, color=ORANGE)

        hook = VGroup(h1, h2, h3, h4, h5, h6).arrange(DOWN, buff=0.3)

        self.play(Write(h1), run_time=0.9)
        self.play(Write(h2), run_time=0.9)
        self.play(Write(h3), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(h4, shift=UP * 0.3), run_time=1.0)
        self.play(Write(h5), run_time=1.2)
        self.play(Write(h6), run_time=1.2)
        self.wait(2.2)
        self.play(FadeOut(hook), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ON THE BALTIC SEA                               ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("baltic_sea")

        t2 = section_title("На Балтичкото Море", color=BLUE)
        self.play(Write(t2), run_time=1.0)

        # baltic sea (left side)
        sea = Polygon(
            np.array([-6, 2.5, 0]), np.array([-2, 2.5, 0]),
            np.array([-2, -2.5, 0]), np.array([-6, -2.5, 0]),
            color=BLUE, fill_color=BLUE, fill_opacity=0.4, stroke_width=0,
        )
        sea_lbl = Text("Балтичко\nморе", font_size=24, color=BLUE, weight=BOLD)
        sea_lbl.move_to(sea.get_center())

        self.play(FadeIn(sea), Write(sea_lbl), run_time=1.0)

        # three country blobs stacked
        est = RoundedRectangle(width=2.6, height=1.2, corner_radius=0.2,
                               color=BLUE, fill_color=BLUE, fill_opacity=0.3,
                               stroke_width=3)
        est.move_to(RIGHT * 1.0 + UP * 1.4)
        est_lbl = Text("Естонија", font_size=22, color=BLUE, weight=BOLD).move_to(est)

        lat = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.2,
                               color=RED, fill_color=RED, fill_opacity=0.3,
                               stroke_width=3)
        lat.move_to(RIGHT * 1.0 + UP * 0.0)
        lat_lbl = Text("Латвија", font_size=22, color=RED, weight=BOLD).move_to(lat)

        lit = RoundedRectangle(width=3.4, height=1.2, corner_radius=0.2,
                               color=GREEN, fill_color=GREEN, fill_opacity=0.3,
                               stroke_width=3)
        lit.move_to(RIGHT * 1.0 + DOWN * 1.4)
        lit_lbl = Text("Литванија", font_size=22, color=GREEN, weight=BOLD).move_to(lit)

        self.play(FadeIn(est), Write(est_lbl), run_time=0.8)
        self.play(FadeIn(lat), Write(lat_lbl), run_time=0.8)
        self.play(FadeIn(lit), Write(lit_lbl), run_time=0.8)
        self.wait(0.5)

        # arrow from sea
        arrow_e = Arrow(sea.get_right() + UP * 1.4, est.get_left(),
                        color=BLUE, buff=0.1, stroke_width=3)
        arrow_l = Arrow(sea.get_right(), lat.get_left(),
                        color=BLUE, buff=0.1, stroke_width=3)
        arrow_li = Arrow(sea.get_right() + DOWN * 1.4, lit.get_left(),
                         color=BLUE, buff=0.1, stroke_width=3)

        self.play(Create(arrow_e), Create(arrow_l), Create(arrow_li), run_time=1.0)
        self.wait(0.5)

        co2 = callout("Три мали држави. Заеднички брег. Заедничка судбина.",
                      width=12.0, bg="#0d2b44", border=BLUE, font_size=24)
        co2.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co2, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t2), FadeOut(sea), FadeOut(sea_lbl),
                  FadeOut(est), FadeOut(est_lbl), FadeOut(lat), FadeOut(lat_lbl),
                  FadeOut(lit), FadeOut(lit_lbl), FadeOut(arrow_e),
                  FadeOut(arrow_l), FadeOut(arrow_li), FadeOut(co2), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  THREE SISTERS — CARDS                           ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cards")

        t3 = section_title("Три портрети", color=YELLOW)
        self.play(Write(t3), run_time=1.0)

        est_c = baltic_card("Естонија", "Талин",
                            "1.3 мил. жители", "45.000 км²",
                            BLUE, LEFT * 4.5)
        lat_c = baltic_card("Латвија", "Рига",
                            "1.9 мил. жители", "65.000 км²",
                            RED, ORIGIN)
        lit_c = baltic_card("Литванија", "Вилнус",
                            "2.8 мил. жители", "65.000 км²",
                            GREEN, RIGHT * 4.5)

        self.play(FadeIn(est_c, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(lat_c, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(lit_c, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)

        co3 = callout("Заедно: помалку од 6 милиони жители.",
                      width=10.5, bg="#1a1230", border=PURPLE, font_size=26)
        co3.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co3, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t3), FadeOut(est_c), FadeOut(lat_c),
                  FadeOut(lit_c), FadeOut(co3), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  SOVIET PAST — TIMELINE                          ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("soviet")

        t4 = section_title("Советска минатост — и враќањето", color=RED)
        self.play(Write(t4), run_time=1.0)

        line = Line(LEFT * 5.5, RIGHT * 5.5, color=GREY, stroke_width=3)
        self.play(Create(line), run_time=0.8)

        e1 = timeline_event("1918", "Независност",      YELLOW, LEFT * 4.5)
        e2 = timeline_event("1940", "Окупација",        RED,    LEFT * 1.5)
        e3 = timeline_event("1991", "Слобода!",          GREEN,  RIGHT * 1.5)
        e4 = timeline_event("2004", "Членки на ЕУ",      BLUE,   RIGHT * 4.5)

        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.play(FadeIn(e3), run_time=0.6)
        self.play(FadeIn(e4), run_time=0.6)
        self.wait(0.5)

        # Singing revolution
        chain = Text("Балтички пат: 600 км човечки синџир", font_size=24,
                     color=YELLOW)
        chain.to_edge(UP, buff=1.4)
        chain_yr = Text("23 август 1989", font_size=20, color=ORANGE)
        chain_yr.next_to(chain, DOWN, buff=0.2)

        self.play(Write(chain), run_time=1.2)
        self.play(Write(chain_yr), run_time=0.8)
        self.wait(0.5)

        co4 = callout("Без оружје. Со песна. Со рака за рака.",
                      width=11.0, bg="#2a1810", border=ORANGE, font_size=26)
        co4.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(co4, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t4), FadeOut(line), FadeOut(e1), FadeOut(e2),
                  FadeOut(e3), FadeOut(e4), FadeOut(chain), FadeOut(chain_yr),
                  FadeOut(co4), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ESTONIA — DIGITAL LEADER                        ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("digital")

        t5 = section_title("Естонија — дигитално општество", color=BLUE)
        self.play(Write(t5), run_time=1.0)

        # central circle
        center = ORIGIN + UP * 0.4
        core = Circle(radius=1.2, color=BLUE, stroke_width=4,
                      fill_color=BLUE, fill_opacity=0.25)
        core.move_to(center)
        core_lbl = Text("e-Естонија", font_size=24, color=BLUE, weight=BOLD)
        core_lbl.move_to(center)

        self.play(Create(core), Write(core_lbl), run_time=1.0)

        # Orbiting services
        services = [
            ("e-Резидентство", PURPLE,  UP * 2.5 + LEFT * 3.0),
            ("e-Гласање",      YELLOW,  UP * 2.5 + RIGHT * 3.0),
            ("e-Здравство",    GREEN,   DOWN * 1.5 + LEFT * 3.5),
            ("e-Училиште",     ORANGE,  DOWN * 1.5 + RIGHT * 3.5),
            ("e-Даноци",       RED,     UP * 2.5),
        ]
        chips = VGroup()
        lines = VGroup()
        for name, color, pos in services:
            chip_box = RoundedRectangle(width=2.2, height=0.7, corner_radius=0.35,
                                        fill_color=color, fill_opacity=0.85,
                                        stroke_color=color, stroke_width=2)
            chip_box.move_to(pos)
            chip_lbl = Text(name, font_size=18, color="#0d1b2e", weight=BOLD)
            chip_lbl.move_to(chip_box)
            chip = VGroup(chip_box, chip_lbl)
            connector = Line(center, chip_box.get_center(),
                             color=color, stroke_width=2, stroke_opacity=0.6)
            chips.add(chip)
            lines.add(connector)

        for i in range(len(services)):
            self.play(Create(lines[i]), FadeIn(chips[i], shift=UP * 0.2),
                      run_time=0.6)
        self.wait(0.5)

        co5 = callout("99% од јавните услуги — онлајн.",
                      width=10.0, bg="#0d2b44", border=BLUE, font_size=26)
        co5.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co5, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t5), FadeOut(core), FadeOut(core_lbl),
                  FadeOut(chips), FadeOut(lines), FadeOut(co5), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  LANGUAGES & CULTURE                             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("language")

        t6 = section_title("Јазици и култура", color=PURPLE)
        self.play(Write(t6), run_time=1.0)

        # Three columns
        est_h = Text("Естонски", font_size=26, color=BLUE, weight=BOLD)
        est_h.move_to(LEFT * 4.0 + UP * 1.8)
        est_fam = VGroup(
            Text("Угрофинско семејство", font_size=18, color=WHITE2),
            Text("Сродно со финскиот", font_size=18, color=YELLOW),
            Text("Tere! = Здраво!", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        est_fam.next_to(est_h, DOWN, buff=0.3).align_to(est_h, LEFT)

        lat_h = Text("Латвиски", font_size=26, color=RED, weight=BOLD)
        lat_h.move_to(UP * 1.8)
        lat_fam = VGroup(
            Text("Балтичко семејство", font_size=18, color=WHITE2),
            Text("Многу стар индоевропски", font_size=18, color=YELLOW),
            Text("Sveiki! = Здраво!", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        lat_fam.next_to(lat_h, DOWN, buff=0.3).align_to(lat_h, LEFT)

        lit_h = Text("Литвански", font_size=26, color=GREEN, weight=BOLD)
        lit_h.move_to(RIGHT * 4.0 + UP * 1.8)
        lit_fam = VGroup(
            Text("Балтичко семејство", font_size=18, color=WHITE2),
            Text("Најархаичен жив јазик", font_size=18, color=YELLOW),
            Text("Labas! = Здраво!", font_size=20, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        lit_fam.next_to(lit_h, DOWN, buff=0.3).align_to(lit_h, LEFT)

        self.play(Write(est_h), run_time=0.5)
        self.play(Write(est_fam), run_time=1.2)
        self.play(Write(lat_h), run_time=0.5)
        self.play(Write(lat_fam), run_time=1.2)
        self.play(Write(lit_h), run_time=0.5)
        self.play(Write(lit_fam), run_time=1.2)
        self.wait(0.5)

        co6 = callout("Различни корени. Иста приказна.",
                      width=10.0, bg="#1a1230", border=PURPLE, font_size=26)
        co6.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co6, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t6), FadeOut(est_h), FadeOut(est_fam),
                  FadeOut(lat_h), FadeOut(lat_fam),
                  FadeOut(lit_h), FadeOut(lit_fam), FadeOut(co6), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        f1 = Text("Естонија. Латвија. Литванија.",
                  font_size=36, color=YELLOW, weight=BOLD)
        f2 = Text("Мали. Млади. Будни.",
                  font_size=30, color=BLUE)
        f3 = Text("Минатото не ги скрши.",
                  font_size=28, color=WHITE2)
        f4 = Text("Иднина.",
                  font_size=48, color=GREEN, weight=BOLD)

        finale = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.45)
        self.play(Write(f1), run_time=1.2)
        self.play(FadeIn(f2, shift=UP * 0.3), run_time=1.0)
        self.play(Write(f3), run_time=1.0)
        self.wait(0.4)
        self.play(Write(f4), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(finale), run_time=1.0)
