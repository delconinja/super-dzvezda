"""
Phys841Scene — Ден и ноќ
Grade 8 Physics, Unit 4, Lesson 1
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


class Phys841Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Ден и ноќ", font_size=56, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 4 · Лекција 1", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Ротација на Земјата ────────────────────────────────
        sec1 = section_title("Земјата се врти — ден и ноќ")
        self.play(Write(sec1))

        # Sun (left)
        sun = Circle(radius=0.85, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sun.shift(LEFT*5.0)
        sun_rays = VGroup(*[
            Line(sun.get_center() + normalize(np.array([np.cos(a), np.sin(a), 0]))*0.95,
                 sun.get_center() + normalize(np.array([np.cos(a), np.sin(a), 0]))*1.35,
                 color=YELLOW, stroke_width=2)
            for a in np.linspace(0, 2*PI, 12, endpoint=False)
        ])
        sun_lbl = Text("Сонце", font_size=22, color=YELLOW).next_to(sun, DOWN, buff=0.2)

        # Earth (right)
        earth = Circle(radius=1.1, fill_color="#1a3a5c", fill_opacity=1,
                        stroke_color=BLUE, stroke_width=2)
        earth.shift(RIGHT*1.5 + DOWN*0.3)

        # Day / Night halves
        day_half = AnnularSector(inner_radius=0, outer_radius=1.1,
                                  angle=PI, start_angle=-PI/2,
                                  fill_color="#1565c0", fill_opacity=0.6, stroke_width=0)
        day_half.shift(RIGHT*1.5 + DOWN*0.3)

        # Axis line
        axis_line = DashedLine(earth.get_center() + UP*1.5,
                               earth.get_center() + DOWN*1.5,
                               color=GREY, stroke_width=1.5)

        # Sun rays hitting Earth
        for_ray1 = Arrow(LEFT*3.8, RIGHT*0.45 + UP*0.3 + DOWN*0.3,
                          color=YELLOW, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.1)
        for_ray2 = Arrow(LEFT*3.8 + DOWN*0.4, RIGHT*0.45 + DOWN*0.35 + DOWN*0.3,
                          color=YELLOW, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.1)

        day_lbl  = Text("Ден", font_size=22, color=YELLOW, weight=BOLD)
        day_lbl.shift(RIGHT*0.6 + DOWN*0.3)
        night_lbl = Text("Ноќ", font_size=22, color=GREY, weight=BOLD)
        night_lbl.shift(RIGHT*2.6 + DOWN*0.3)

        rot_txt = callout(
            "Земјата се врти 1× за 24 часа — запад→исток.\nСтрана кон Сонцето = ден. Наспроти = ноќ.",
            width=7.5, font_size=23
        )
        rot_txt.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(sun), Create(sun_rays), FadeIn(sun_lbl))
        self.play(Create(earth), FadeIn(day_half))
        self.play(Create(axis_line))
        self.play(GrowArrow(for_ray1), GrowArrow(for_ray2))
        self.play(FadeIn(day_lbl), FadeIn(night_lbl))
        self.play(FadeIn(rot_txt))
        self.wait(2)
        self.play(FadeOut(VGroup(sec1, sun, sun_rays, sun_lbl, earth, day_half,
                                  axis_line, for_ray1, for_ray2,
                                  day_lbl, night_lbl, rot_txt)))

        # ── SECTION 2 : Брзина на ротација ─────────────────────────────────
        sec2 = section_title("Брзина на ротација — 1 670 km/h")
        self.play(Write(sec2))

        speed_note = callout(
            "На екваторот: ~1 670 km/h\nНе ја чувствуваме — сè се движи заедно.",
            width=8.5, font_size=26, border=GREEN
        )
        speed_note.next_to(sec2, DOWN, buff=0.55)

        comparison = VGroup(
            Text("Автомобил:     ~120 km/h", font_size=27, color=WHITE2),
            Text("Авион:          ~900 km/h", font_size=27, color=WHITE2),
            Text("Земјата (екватор): ~1 670 km/h", font_size=27, color=YELLOW, weight=BOLD),
        )
        comparison.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        comparison.next_to(speed_note, DOWN, buff=0.5)
        comparison.shift(LEFT*0.5)

        self.play(FadeIn(speed_note, shift=UP*0.15))
        for c in comparison:
            self.play(FadeIn(c, shift=RIGHT*0.2), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, speed_note, comparison)))

        # ── SECTION 3 : Должина на ден / сезони ────────────────────────────
        sec3 = section_title("Должина на денот — екватор vs полови")
        self.play(Write(sec3))

        day_data = [
            ("Екватор",    "~12h",  "~12h",  BLUE),
            ("Македонија", "~16h",  "~8h",   GREEN),
            ("Арктик",     "~24h",  "~0h",   YELLOW),
        ]
        header = VGroup(
            Text("Место",     font_size=24, color=GREY, weight=BOLD).set_width(2.6),
            Text("Лето",      font_size=24, color=YELLOW, weight=BOLD),
            Text("Зима",      font_size=24, color=BLUE,   weight=BOLD),
        ).arrange(RIGHT, buff=0.6)
        header.next_to(sec3, DOWN, buff=0.55)
        header.shift(LEFT*0.4)

        rows = VGroup()
        for place, summer, winter, col in day_data:
            pl = Text(place,  font_size=24, color=WHITE2).set_width(2.6)
            su = Text(summer, font_size=24, color=YELLOW)
            wi = Text(winter, font_size=24, color=BLUE)
            row = VGroup(pl, su, wi).arrange(RIGHT, buff=0.6)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rows.next_to(header, DOWN, buff=0.3)
        rows.shift(LEFT*0.4)

        polar_note = callout(
            "Поларен ден: 24h сонце (арктичко лето)\nПоларна ноќ: 24h темница (арктичка зима)",
            width=9.0, font_size=23, border=PURPLE
        )
        polar_note.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(header))
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.play(FadeIn(polar_note))
        self.wait(2)
        self.play(FadeOut(VGroup(sec3, header, rows, polar_note)))

        # ── SECTION 4 : Зошто небото е сино ────────────────────────────────
        sec4 = section_title("Зошто небото е сино?")
        self.play(Write(sec4))

        scatter_box = callout(
            "Молекулите на воздухот ја расејуваат сината светлина повеќе\nод другите бои → небото изгледа сино.",
            width=10.0, font_size=24, border=BLUE
        )
        scatter_box.next_to(sec4, DOWN, buff=0.55)

        sunset_box = callout(
            "При зајдисонце/изгрејсонце: светлината минува низ\nповеќе атмосфера → синото се расејува → останува ЧЕРВЕНО.",
            width=10.0, font_size=24, border=ORANGE
        )
        sunset_box.next_to(scatter_box, DOWN, buff=0.4)

        self.play(FadeIn(scatter_box, shift=UP*0.15))
        self.play(FadeIn(sunset_box, shift=UP*0.1))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec4, scatter_box, sunset_box)))

        # ── SECTION 5 : Временски зони ────────────────────────────────────
        sec5 = section_title("Временски зони")
        self.play(Write(sec5))

        tz_box = callout(
            "24 зони · секоја е 15° должинска линија · разлика = 1 час",
            width=9.0, font_size=25, border=GREEN
        )
        tz_box.next_to(sec5, DOWN, buff=0.55)

        cities = [
            ("Скопје",    "12:00", YELLOW),
            ("Лондон",    "11:00", BLUE),
            ("Њу Јорк",   "06:00", ORANGE),
            ("Токио",     "19:00", GREEN),
        ]
        city_rows = VGroup()
        for city, time, col in cities:
            ct = Text(city, font_size=26, color=WHITE2).set_width(2.5)
            tm = Text(time, font_size=28, color=col, weight=BOLD)
            row = VGroup(ct, tm).arrange(RIGHT, buff=0.7)
            city_rows.add(row)
        city_rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        city_rows.next_to(tz_box, DOWN, buff=0.45)
        city_rows.shift(LEFT*0.5)

        self.play(FadeIn(tz_box))
        for row in city_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2)
        self.play(FadeOut(VGroup(sec5, tz_box, city_rows)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Земјата се врти.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Секогаш.", font_size=38, color=WHITE2, weight=BOLD),
            Text("Во овој миг — со 1 670 km/h.", font_size=32, color=ORANGE),
            Text("Не ја чувствуваш.", font_size=32, color=GREY),
            Text("Но таа не запира.", font_size=42, color=RED, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.7)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Ротација · Ден/Ноќ · Сино небо · Временски зони",
                     font_size=28, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
