"""
Phys835Scene — Бои и дисперзија
Grade 8 Physics, Unit 3, Lesson 5
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


class Phys835Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Бои и дисперзија", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 3 · Лекција 5", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Бела светлина ──────────────────────────────────────
        sec1 = section_title("Белата светлина не е 'чиста'")
        myth = callout(
            "Белата светлина е МЕШАВИНА од сите бои.\nПризмата ги разложува — не ги создава.",
            width=9.5, font_size=25, border=YELLOW
        )
        myth.next_to(sec1, DOWN, buff=0.55)
        self.play(Write(sec1))
        self.play(FadeIn(myth, shift=UP*0.15))
        self.wait(1.8)
        self.play(FadeOut(VGroup(sec1, myth)))

        # ── SECTION 2 : Прима и спектар ────────────────────────────────────
        sec2 = section_title("Дисперзија — прима го разложува светлото")
        self.play(Write(sec2))

        # Prism: triangle
        prism = Triangle(color=BLUE, fill_color="#0a2040", fill_opacity=0.8,
                         stroke_width=2.5)
        prism.scale(1.2).shift(LEFT*1.5 + DOWN*0.5)

        # White ray going in
        white_in = Arrow(LEFT*4.8 + DOWN*0.5, prism.get_left() + RIGHT*0.15,
                         color=WHITE2, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.1)

        # Dispersed rays coming out right side of prism
        spectrum_colors = [
            ("#7b00ff", "Виолетова ~400nm"),
            ("#4400ff", "Индиго"),
            (BLUE,      "Сина"),
            (GREEN,     "Зелена"),
            (YELLOW,    "Жолта"),
            (ORANGE,    "Портокалова"),
            (RED,       "Црвена ~700nm"),
        ]
        out_start = prism.get_right() + LEFT*0.1 + DOWN*0.1
        disp_rays = VGroup()
        for i, (col, _) in enumerate(spectrum_colors):
            angle_offset = (i - 3) * 0.22
            end_pt = out_start + RIGHT*2.5 + UP*(-angle_offset*1.8) + DOWN*0.1
            ray = Arrow(out_start, end_pt, color=col, buff=0, stroke_width=2.5,
                        max_tip_length_to_length_ratio=0.1)
            disp_rays.add(ray)

        # Spectrum bar below
        spec_bar = VGroup()
        spec_bar_colors = ["#7b00ff","#4400ff", BLUE, GREEN, YELLOW, ORANGE, RED]
        for i, col in enumerate(spec_bar_colors):
            seg = Rectangle(width=0.9, height=0.45,
                            fill_color=col, fill_opacity=1, stroke_width=0)
            seg.shift(LEFT*2.7 + RIGHT*i*0.9 + DOWN*2.8)
            spec_bar.add(seg)
        spec_lbl_l = Text("400nm", font_size=18, color=WHITE2).next_to(spec_bar, LEFT, buff=0.15)
        spec_lbl_r = Text("700nm", font_size=18, color=WHITE2).next_to(spec_bar, RIGHT, buff=0.15)

        self.play(Create(prism))
        self.play(GrowArrow(white_in))
        self.play(LaggedStart(*[GrowArrow(r) for r in disp_rays], lag_ratio=0.15), run_time=1.4)
        self.play(Create(spec_bar), FadeIn(spec_lbl_l), FadeIn(spec_lbl_r))
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, prism, white_in, disp_rays,
                                  spec_bar, spec_lbl_l, spec_lbl_r)))

        # ── SECTION 3 : Адитивно мешање (RGB) ─────────────────────────────
        sec3 = section_title("Адитивно мешање — светлина (RGB)")
        self.play(Write(sec3))

        # Three overlapping circles
        offset = 0.62
        c_r = Circle(radius=1.1, fill_color=RED,    fill_opacity=0.55, stroke_width=0)
        c_g = Circle(radius=1.1, fill_color=GREEN,  fill_opacity=0.55, stroke_width=0)
        c_b = Circle(radius=1.1, fill_color=BLUE,   fill_opacity=0.55, stroke_width=0)
        c_r.shift(UP*offset + LEFT*0.6)
        c_g.shift(UP*offset + RIGHT*0.6)
        c_b.shift(DOWN*offset*1.4)

        lbl_r = Text("R", font_size=26, color=RED,   weight=BOLD).move_to(c_r.get_center() + LEFT*0.55)
        lbl_g = Text("G", font_size=26, color=GREEN, weight=BOLD).move_to(c_g.get_center() + RIGHT*0.55)
        lbl_b = Text("B", font_size=26, color=BLUE,  weight=BOLD).move_to(c_b.get_center() + DOWN*0.5)

        center_group = VGroup(c_r, c_g, c_b, lbl_r, lbl_g, lbl_b).shift(LEFT*3.2 + DOWN*0.5)

        note_rgb = callout(
            "R + G + B = Бела светлина\nПоставено во: монитори, телевизори, проектори",
            width=6.0, font_size=23, border=WHITE2
        )
        note_rgb.next_to(sec3, DOWN, buff=0.5).shift(RIGHT*2.0)

        self.play(FadeIn(c_r), FadeIn(c_g), FadeIn(c_b))
        self.play(FadeIn(lbl_r), FadeIn(lbl_g), FadeIn(lbl_b))
        self.play(FadeIn(note_rgb, shift=LEFT*0.2))
        self.wait(2)
        self.play(FadeOut(VGroup(sec3, center_group, note_rgb)))

        # ── SECTION 4 : Субтрактивно мешање (CMY) ─────────────────────────
        sec4 = section_title("Субтрактивно мешање — пигменти (CMY)")
        self.play(Write(sec4))

        cyan_c    = "#00bcd4"
        magenta_c = "#e91e63"
        yellow_c  = YELLOW

        cc = Circle(radius=1.1, fill_color=cyan_c,    fill_opacity=0.55, stroke_width=0)
        cm = Circle(radius=1.1, fill_color=magenta_c, fill_opacity=0.55, stroke_width=0)
        cy = Circle(radius=1.1, fill_color=yellow_c,  fill_opacity=0.55, stroke_width=0)
        cc.shift(UP*offset + LEFT*0.6)
        cm.shift(UP*offset + RIGHT*0.6)
        cy.shift(DOWN*offset*1.4)

        lbl_c = Text("C", font_size=26, color=cyan_c,    weight=BOLD).move_to(cc.get_center() + LEFT*0.55)
        lbl_m = Text("M", font_size=26, color=magenta_c, weight=BOLD).move_to(cm.get_center() + RIGHT*0.55)
        lbl_y = Text("Y", font_size=26, color=yellow_c,  weight=BOLD).move_to(cy.get_center() + DOWN*0.5)

        cmy_group = VGroup(cc, cm, cy, lbl_c, lbl_m, lbl_y).shift(LEFT*3.2 + DOWN*0.5)

        note_cmy = callout(
            "C + M + Y = Черна боја (теоретски)\nПоставено во: печатачи, сликарство",
            width=6.0, font_size=23, border=ORANGE
        )
        note_cmy.next_to(sec4, DOWN, buff=0.5).shift(RIGHT*2.0)

        self.play(FadeIn(cc), FadeIn(cm), FadeIn(cy))
        self.play(FadeIn(lbl_c), FadeIn(lbl_m), FadeIn(lbl_y))
        self.play(FadeIn(note_cmy, shift=LEFT*0.2))
        self.wait(2)
        self.play(FadeOut(VGroup(sec4, cmy_group, note_cmy)))

        # ── SECTION 5 : Зошто ги гледаме боите ────────────────────────────
        sec5 = section_title("Зошто гледаме бои?")
        self.play(Write(sec5))

        apple_body = Circle(radius=0.9, fill_color="#c0392b", fill_opacity=1,
                            stroke_color=RED, stroke_width=2)
        apple_body.shift(LEFT*3.5 + DOWN*0.6)
        apple_stem = Line(apple_body.get_top(), apple_body.get_top() + UP*0.4 + RIGHT*0.15,
                          color=GREEN, stroke_width=3)
        apple_lbl  = Text("Јаболко", font_size=22, color=WHITE2).next_to(apple_body, DOWN, buff=0.2)

        arrows_abs = VGroup()
        for i, (col, ang) in enumerate([(BLUE, -0.6), (GREEN, -0.2), (PURPLE, 0.2), (YELLOW, 0.6)]):
            a = Arrow(apple_body.get_center() + normalize(LEFT+UP*ang)*1.8,
                      apple_body.get_center() + normalize(LEFT+UP*ang)*1.05,
                      color=col, buff=0, stroke_width=2,
                      max_tip_length_to_length_ratio=0.15)
            arrows_abs.add(a)

        arrow_reflect = Arrow(
            apple_body.get_right(),
            apple_body.get_right() + RIGHT*1.8,
            color=RED, buff=0, stroke_width=3,
            max_tip_length_to_length_ratio=0.12
        )
        reflect_lbl = Text("Рефлектира САМО ЦРВЕНА", font_size=22, color=RED)
        reflect_lbl.next_to(arrow_reflect, UP, buff=0.15)

        explain = VGroup(
            Text("• Предметот ги апсорбира сите бои ОСВЕН сопствената", font_size=24, color=WHITE2),
            Text("• Рефлектираната боја ја гледаме со окото", font_size=24, color=WHITE2),
            Text("• Црно = апсорбира сè.  Бело = рефлектира сè.", font_size=24, color=GREY),
        )
        explain.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        explain.next_to(sec5, DOWN, buff=0.5).shift(RIGHT*0.5)

        self.play(FadeIn(apple_body), FadeIn(apple_stem), FadeIn(apple_lbl))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_abs], lag_ratio=0.15))
        self.play(GrowArrow(arrow_reflect), FadeIn(reflect_lbl))
        self.play(FadeIn(explain, shift=UP*0.1))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec5, apple_body, apple_stem, apple_lbl,
                                  arrows_abs, arrow_reflect, reflect_lbl, explain)))

        # ── SECTION 6 : Бои на ѕвезди ────────────────────────────────────
        sec6 = section_title("Бои на ѕвезди — температура")
        self.play(Write(sec6))

        star_data = [
            (RED,    "Червена ѕвезда",   "~3 000°C"),
            (YELLOW, "Жолта ѕвезда",     "~6 000°C"),
            (WHITE2, "Бела ѕвезда",      "~10 000°C"),
            (BLUE,   "Сина ѕвезда",      "~30 000°C"),
        ]
        star_rows = VGroup()
        for col, name, temp in star_data:
            dot  = Dot(radius=0.25, color=col)
            dot.set_fill(color=col, opacity=1)
            nm_t = Text(name, font_size=26, color=WHITE2)
            tp_t = Text(temp, font_size=26, color=col, weight=BOLD)
            row  = VGroup(dot, nm_t, tp_t).arrange(RIGHT, buff=0.55)
            star_rows.add(row)
        star_rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        star_rows.next_to(sec6, DOWN, buff=0.6)
        star_rows.shift(LEFT*0.5)

        sun_note = callout("Нашето Сонце е жолта ѕвезда — ~5 500°C",
                            width=7.5, font_size=24, border=YELLOW)
        sun_note.to_edge(DOWN, buff=0.4)

        for row in star_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.play(FadeIn(sun_note))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec6, star_rows, sun_note)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Белата светлина е лага.", font_size=36, color=WHITE2, weight=BOLD),
            Text("Таа е сите бои заедно.", font_size=36, color=YELLOW, weight=BOLD),
            Text("Само призмата ја разоткрива.", font_size=32, color=BLUE),
            Text("Само истината ја разложува.", font_size=38, color=RED, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.42)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.75)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Спектар · Дисперзија · RGB · CMY · Бои на ѕвезди",
                     font_size=28, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
