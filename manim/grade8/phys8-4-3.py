"""
Phys843Scene — Ѕвезди и планети
Grade 8 Physics, Unit 4, Lesson 3
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


class Phys843Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Ѕвезди и планети", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 4 · Лекција 3", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Ѕвезда vs Планета ─────────────────────────────────
        sec1 = section_title("Ѕвезда vs Планета")
        self.play(Write(sec1))

        # Comparison table
        headers = VGroup(
            Text("",         font_size=24, color=GREY).set_width(2.5),
            Text("ЅВЕЗДА",   font_size=24, color=YELLOW, weight=BOLD).set_width(3.2),
            Text("ПЛАНЕТА",  font_size=24, color=BLUE,   weight=BOLD).set_width(3.2),
        ).arrange(RIGHT, buff=0.3).next_to(sec1, DOWN, buff=0.55).shift(LEFT*0.3)

        comp_data = [
            ("Светлина",   "Произведува сопствена", "Одразува од ѕвезда"),
            ("Состав",     "Топол гас (H + He)",    "Камен / гас / мраз"),
            ("Јадрени реакции", "ДА — фузија",      "НЕ"),
            ("Пример",     "Сонцето, Сириус",       "Земјата, Јупитер"),
        ]
        comp_rows = VGroup()
        for prop, star_v, planet_v in comp_data:
            pr = Text(prop,    font_size=21, color=GREY).set_width(2.5)
            st = Text(star_v,  font_size=21, color=YELLOW).set_width(3.2)
            pl = Text(planet_v,font_size=21, color=BLUE).set_width(3.2)
            comp_rows.add(VGroup(pr, st, pl).arrange(RIGHT, buff=0.3))
        comp_rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        comp_rows.next_to(headers, DOWN, buff=0.25).shift(LEFT*0.3)

        self.play(FadeIn(headers))
        for row in comp_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec1, headers, comp_rows)))

        # ── SECTION 2 : Нашето Сонце ───────────────────────────────────────
        sec2 = section_title("Нашето Сонце — обична ѕвезда")
        self.play(Write(sec2))

        sun_icon = Circle(radius=1.0, fill_color=YELLOW, fill_opacity=0.9,
                           stroke_width=0)
        sun_icon.shift(LEFT*4.0 + DOWN*0.5)
        sun_rays2 = VGroup(*[
            Line(sun_icon.get_center() + normalize(np.array([np.cos(a), np.sin(a), 0]))*1.1,
                 sun_icon.get_center() + normalize(np.array([np.cos(a), np.sin(a), 0]))*1.55,
                 color=YELLOW, stroke_width=2)
            for a in np.linspace(0, 2*PI, 12, endpoint=False)
        ])

        sun_facts = VGroup(
            Text("Маса:         2 × 10³⁰ kg",        font_size=25, color=WHITE2),
            Text("Пречник:      1 400 000 km",        font_size=25, color=WHITE2),
            Text("Темп. површина: 5 500°C",            font_size=25, color=ORANGE),
            Text("Возраст:       4.6 милијарди год",  font_size=25, color=WHITE2),
            Text("Тип:          Жолта патуљаста ѕвезда", font_size=25, color=YELLOW),
        )
        sun_facts.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        sun_facts.next_to(sec2, DOWN, buff=0.55).shift(RIGHT*0.5)

        self.play(FadeIn(sun_icon), Create(sun_rays2))
        for fact in sun_facts:
            self.play(FadeIn(fact, shift=RIGHT*0.2), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, sun_icon, sun_rays2, sun_facts)))

        # ── SECTION 3 : Бои по температура ─────────────────────────────────
        sec3 = section_title("Бои на ѕвезди → температура")
        self.play(Write(sec3))

        star_data = [
            (RED,    "Червена",  "~3 000°C",  0.45),
            (ORANGE, "Портокал", "~4 500°C",  0.55),
            (YELLOW, "Жолта",    "~6 000°C",  0.65),
            (WHITE2, "Бела",     "~10 000°C", 0.8),
            (BLUE,   "Сина",     "~30 000°C", 1.0),
        ]
        star_rows = VGroup()
        for col, name, temp, size in star_data:
            dot = Circle(radius=size*0.28, fill_color=col, fill_opacity=1, stroke_width=0)
            nm  = Text(name, font_size=25, color=WHITE2).set_width(1.8)
            tp  = Text(temp, font_size=25, color=col, weight=BOLD)
            row = VGroup(dot, nm, tp).arrange(RIGHT, buff=0.5)
            star_rows.add(row)
        star_rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        star_rows.next_to(sec3, DOWN, buff=0.6)
        star_rows.shift(LEFT*0.5)

        for row in star_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec3, star_rows)))

        # ── SECTION 4 : Светлосна година ───────────────────────────────────
        sec4 = section_title("Светлосна година — колку е далечно?")
        self.play(Write(sec4))

        ly_box = callout(
            "1 светлосна година = 9.5 × 10¹² km\n(растојание изминато од светлина за 1 година)",
            width=9.5, font_size=25, border=YELLOW
        )
        ly_box.next_to(sec4, DOWN, buff=0.55)

        dist_data = [
            ("Месечина",      "1.3 секунди",   GREY),
            ("Сонцето",       "8 минути",       YELLOW),
            ("Алфа Кентавриус", "4.3 год.",      BLUE),
            ("Центар на Млечниот Пат", "~26 000 год.", PURPLE),
        ]
        dist_rows = VGroup()
        for name, time, col in dist_data:
            nm = Text(name, font_size=23, color=WHITE2).set_width(4.2)
            tm = Text(time, font_size=23, color=col, weight=BOLD)
            row = VGroup(nm, tm).arrange(RIGHT, buff=0.5)
            dist_rows.add(row)
        dist_rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        dist_rows.next_to(ly_box, DOWN, buff=0.45)
        dist_rows.shift(LEFT*0.3)

        past_note = callout(
            "Кога ја гледаш ѕвездата → ја гледаш каква БЕШЕ.\nМожеби веќе ја нема.",
            width=9.0, font_size=24, border=PURPLE
        )
        past_note.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(ly_box))
        for row in dist_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.4)
        self.play(FadeIn(past_note))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec4, ly_box, dist_rows, past_note)))

        # ── SECTION 5 : Животен циклус на ѕвезда ───────────────────────────
        sec5 = section_title("Животен циклус на ѕвезда")
        self.play(Write(sec5))

        lifecycle = [
            ("Маглина (небула)",      BLUE),
            ("Ѕвезда (главна низа)", YELLOW),
            ("Гигант / Супергигант", ORANGE),
            ("Мала ѕвезда → бела патуљица", WHITE2),
            ("Голема ѕвезда → СУПЕРНОВА", RED),
            ("Неутронска ѕвезда / Црна дупка", PURPLE),
        ]
        lc_objs = VGroup()
        for i, (name, col) in enumerate(lifecycle):
            circle = Circle(radius=0.22, fill_color=col, fill_opacity=0.8, stroke_width=0)
            lbl    = Text(name, font_size=22, color=col)
            lbl.next_to(circle, RIGHT, buff=0.3)
            item   = VGroup(circle, lbl)
            lc_objs.add(item)

        lc_objs.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        lc_objs.next_to(sec5, DOWN, buff=0.55)
        lc_objs.shift(LEFT*1.0)

        # Arrows between steps
        for i in range(len(lc_objs)-1):
            arrow = Arrow(lc_objs[i][0].get_bottom(),
                          lc_objs[i+1][0].get_top(),
                          color=GREY, buff=0.05, stroke_width=1.5,
                          max_tip_length_to_length_ratio=0.15)
            self.play(FadeIn(lc_objs[i], shift=RIGHT*0.15), run_time=0.4)
            self.play(GrowArrow(arrow), run_time=0.25)
        self.play(FadeIn(lc_objs[-1], shift=RIGHT*0.15), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec5, lc_objs)))

        # ── SECTION 6 : Млечниот Пат и вселената ──────────────────────────
        sec6 = section_title("Млечниот Пат и вселената")
        self.play(Write(sec6))

        scale_data = [
            ("Млечниот Пат:",   "100–400 милијарди ѕвезди", YELLOW),
            ("Вселената:",      "над 2 трилиони галаксии",   PURPLE),
        ]
        scale_rows = VGroup()
        for label, val, col in scale_data:
            lb = Text(label, font_size=26, color=GREY).set_width(3.0)
            vl = Text(val,   font_size=26, color=col, weight=BOLD)
            scale_rows.add(VGroup(lb, vl).arrange(RIGHT, buff=0.5))
        scale_rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        scale_rows.next_to(sec6, DOWN, buff=0.6)
        scale_rows.shift(LEFT*0.5)

        for row in scale_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(VGroup(sec6, scale_rows)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Гледаш ѕвезда.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Гледаш историја.", font_size=38, color=WHITE2, weight=BOLD),
            Text("Светлина стара 4 години.", font_size=32, color=BLUE),
            Text("Таа ѕвезда можеби веќе ја нема.", font_size=32, color=GREY),
            Text("Но ти ја гледаш. Сè уште.", font_size=40, color=PURPLE, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.72)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Ѕвезди · Планети · Светлосна год. · Животен циклус",
                     font_size=27, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
