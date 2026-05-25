"""
Phys844Scene — Сончевиот систем
Grade 8 Physics, Unit 4, Lesson 4
Manim CE v0.20.1
"""
from manim import *

config.background_color = "#0d1b2e"
BLUE   = "#4fc3f7"
YELLOW = "#ffd54f"
GREEN  = "#81c784"
RED    = "#e57373"
GREY   = "#90a4ae"
ORANGE = "#ffb74d"
PURPLE = "#ce93d8"
WHITE2 = "#e8eaf0"
DARK_CARD = "#0f2233"


def callout(text, width=9.0, bg="#0d2b44", border=BLUE, font_size=28):
    box = RoundedRectangle(
        width=width, height=1.4, corner_radius=0.3,
        fill_color=bg, fill_opacity=1,
        stroke_color=border, stroke_width=2
    )
    label = Text(text, font_size=font_size, color=WHITE2)
    label.move_to(box)
    return VGroup(box, label)


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


class Phys844Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Сончевиот систем", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 4 · Лекција 4", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Дијаграм на Сончевиот систем ──────────────────────
        sec1 = section_title("8 планети — редоследот")
        self.play(Write(sec1))

        # Planet data: (name, color, relative size, orbit radius)
        planet_data = [
            ("Меркур",   "#b0b0b0", 0.18, 1.2),
            ("Венера",   ORANGE,    0.26, 1.9),
            ("Земја",    BLUE,      0.28, 2.6),
            ("Марс",     RED,       0.22, 3.3),
            ("Јупитер",  "#e8c49a", 0.6,  4.4),
            ("Сатурн",   "#d4b483", 0.52, 5.5),
            ("Уран",     "#80deea", 0.38, 6.5),
            ("Нептун",   "#3f51b5", 0.36, 7.4),
        ]

        # Sun
        solar_sun = Circle(radius=0.55, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        solar_sun.shift(LEFT*6.8 + DOWN*0.2)

        planets_group = VGroup(solar_sun)
        for name, col, size, orb_r in planet_data:
            orbit_line = DashedLine(
                solar_sun.get_center(),
                solar_sun.get_center() + RIGHT*orb_r,
                color=GREY, stroke_width=0.8, dash_length=0.12
            )
            planet_circle = Circle(radius=size*0.42,
                                    fill_color=col, fill_opacity=1, stroke_width=0)
            planet_circle.move_to(solar_sun.get_center() + RIGHT*orb_r)
            p_lbl = Text(name, font_size=14, color=WHITE2)
            p_lbl.next_to(planet_circle, DOWN, buff=0.08)
            planets_group.add(VGroup(orbit_line, planet_circle, p_lbl))

        planets_group.shift(RIGHT*0.5)

        # Saturn ring
        saturn_obj = planets_group[6][1]  # Saturn circle
        sat_ring = Ellipse(width=0.95, height=0.28,
                            fill_opacity=0, stroke_color="#d4b483", stroke_width=1.5)
        sat_ring.move_to(saturn_obj)

        inner_outer_lbl = VGroup(
            Text("← Каменести →", font_size=18, color=GREY).shift(LEFT*3.2 + DOWN*2.0),
            Text("← Гасовити/Ледени →", font_size=18, color=BLUE).shift(RIGHT*1.5 + DOWN*2.0),
        )
        belt_lbl = Text("Астероиден\nпојас", font_size=14, color=ORANGE)
        belt_lbl.move_to(solar_sun.get_center() + RIGHT*3.9 + DOWN*0.5 + RIGHT*0.5)

        self.play(FadeIn(solar_sun))
        for p_grp in planets_group[1:]:
            self.play(Create(p_grp[0]), FadeIn(p_grp[1]), FadeIn(p_grp[2]),
                      run_time=0.3)
        self.play(Create(sat_ring))
        self.play(FadeIn(inner_outer_lbl), FadeIn(belt_lbl))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec1, planets_group, sat_ring,
                                  inner_outer_lbl, belt_lbl)))

        # ── SECTION 2 : Клучни факти за планетите ─────────────────────────
        sec2 = section_title("Интересни факти")
        self.play(Write(sec2))

        facts = [
            ("Венера",   "Најтопла: 495°C (CO₂ стаклена градина)",  ORANGE),
            ("Јупитер",  "Најголема: 11× пречникот на Земјата",      "#e8c49a"),
            ("Сатурн",   "Прстени од мраз и камен",                  "#d4b483"),
            ("Уран",     "Накосен 98° — врти на страна",             "#80deea"),
            ("Плутон",   "Патуљаста планета (класифициран 2006)",    GREY),
        ]
        fact_rows = VGroup()
        for name, fact, col in facts:
            nm = Text(name, font_size=24, color=col, weight=BOLD).set_width(2.0)
            ft = Text(fact, font_size=22, color=WHITE2)
            row = VGroup(nm, ft).arrange(RIGHT, buff=0.45)
            fact_rows.add(row)
        fact_rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        fact_rows.next_to(sec2, DOWN, buff=0.55)
        fact_rows.shift(LEFT*0.5)

        for row in fact_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, fact_rows)))

        # ── SECTION 3 : Зошто планетите остануваат во орбита ──────────────
        sec3 = section_title("Зошто планетите не паѓаат во Сонцето?")
        self.play(Write(sec3))

        orbit_explain = callout(
            "Сонцето ги привлекува (гравитација) →\nСтрана брзина ги спречува да паднат → ОРБИТА",
            width=9.5, font_size=25, border=GREEN
        )
        orbit_explain.next_to(sec3, DOWN, buff=0.55)

        # Mini orbit diagram
        mini_sun = Circle(radius=0.3, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        mini_sun.shift(LEFT*2.5 + DOWN*1.5)
        mini_orbit = Circle(radius=1.2, stroke_color=GREY, stroke_width=1.5,
                             fill_opacity=0)
        mini_orbit.move_to(mini_sun)
        mini_planet = Dot(mini_sun.get_center() + RIGHT*1.2, color=BLUE, radius=0.12)

        grav_arrow = Arrow(mini_planet.get_center(),
                            mini_sun.get_center(),
                            color=RED, buff=0.05, stroke_width=2,
                            max_tip_length_to_length_ratio=0.15)
        vel_arrow  = Arrow(mini_planet.get_center(),
                            mini_planet.get_center() + UP*1.0,
                            color=GREEN, buff=0, stroke_width=2,
                            max_tip_length_to_length_ratio=0.15)
        grav_lbl = Text("гравитација", font_size=18, color=RED)
        grav_lbl.next_to(grav_arrow, DOWN, buff=0.1)
        vel_lbl  = Text("брзина", font_size=18, color=GREEN)
        vel_lbl.next_to(vel_arrow, RIGHT, buff=0.1)

        kepler_box = callout(
            "Кеплер: орбитите се ЕЛИПСИ.\nПоблиску до Сонцето → побрзо движење.",
            width=6.0, font_size=22, border=YELLOW
        )
        kepler_box.next_to(orbit_explain, DOWN, buff=0.4).shift(RIGHT*1.5)

        self.play(FadeIn(orbit_explain))
        self.play(FadeIn(mini_sun), Create(mini_orbit), FadeIn(mini_planet))
        self.play(GrowArrow(grav_arrow), FadeIn(grav_lbl))
        self.play(GrowArrow(vel_arrow),  FadeIn(vel_lbl))
        self.play(FadeIn(kepler_box))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec3, orbit_explain, mini_sun, mini_orbit,
                                  mini_planet, grav_arrow, grav_lbl,
                                  vel_arrow, vel_lbl, kepler_box)))

        # ── SECTION 4 : Мали тела ──────────────────────────────────────────
        sec4 = section_title("Мали тела: астероиди · комети · метеори")
        self.play(Write(sec4))

        small_data = [
            ("Астероиди", "Камења во орбита меѓу Марс и Јупитер", GREY),
            ("Комети",    "Ледени — развиваат опашка кај Сонцето", BLUE),
            ("Метеори",   "'Паѓачки ѕвезди' — парчиња кои горат во атмосферата", ORANGE),
            ("Метеорити", "Метеори кои допираат до Земјата",       RED),
        ]
        small_rows = VGroup()
        for name, desc, col in small_data:
            nm = Text(name, font_size=24, color=col, weight=BOLD).set_width(2.2)
            ds = Text(desc, font_size=21, color=WHITE2)
            row = VGroup(nm, ds).arrange(RIGHT, buff=0.45)
            small_rows.add(row)
        small_rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        small_rows.next_to(sec4, DOWN, buff=0.55)
        small_rows.shift(LEFT*0.5)

        for row in small_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2)
        self.play(FadeOut(VGroup(sec4, small_rows)))

        # ── SECTION 5 : Живот надвор од Земјата? ──────────────────────────
        sec5 = section_title("Живот надвор од Земјата?")
        self.play(Write(sec5))

        life_data = [
            ("Европа (Јупитер)",   "Течен океан под мраз — можни микроорганизми", GREEN),
            ("Енцелад (Сатурн)",   "Гејзири на вода — посетен од Касини",          BLUE),
            ("Марс",               "Минато → докази за течна вода",                RED),
        ]
        life_rows = VGroup()
        for name, desc, col in life_data:
            nm = Text(name, font_size=23, color=col, weight=BOLD).set_width(3.0)
            ds = Text(desc, font_size=21, color=WHITE2)
            row = VGroup(nm, ds).arrange(RIGHT, buff=0.4)
            life_rows.add(row)
        life_rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        life_rows.next_to(sec5, DOWN, buff=0.55)
        life_rows.shift(LEFT*0.3)

        math_note = callout(
            "Математиката вели: со 2 трилиони галаксии\nверојатноста за самотија е мала.",
            width=9.0, font_size=24, border=PURPLE
        )
        math_note.to_edge(DOWN, buff=0.4)

        for row in life_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.play(FadeIn(math_note))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec5, life_rows, math_note)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Осум планети.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Трилиони ѕвезди.", font_size=38, color=WHITE2, weight=BOLD),
            Text("Две трилиони галаксии.", font_size=34, color=BLUE),
            Text("А ти се прашуваш дали си сам?", font_size=30, color=GREY),
            Text("Математиката вели: не.", font_size=44, color=GREEN, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.72)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("8 Планети · Орбити · Кеплер · Мали тела · Живот",
                     font_size=27, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
