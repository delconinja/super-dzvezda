"""
Phys836Scene — Леќи и окото: оптика во медицина
Grade 8 Physics, Unit 3, Lesson 6
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


class Phys836Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Леќи и окото", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 3 · Лекција 6", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Збирна леќа ────────────────────────────────────────
        sec1 = section_title("Збирна леќа (+) — го фокусира светлото")
        self.play(Write(sec1))

        # Lens as ellipse
        conv_lens = Ellipse(width=0.55, height=2.2, fill_color=BLUE,
                             fill_opacity=0.35, stroke_color=BLUE, stroke_width=2.5)
        conv_lens.shift(LEFT*0.5 + DOWN*0.6)

        # Optical axis
        axis = DashedLine(LEFT*5.5, RIGHT*3.5, color=GREY, stroke_width=1).shift(DOWN*0.6)

        # Three parallel rays converging to focal point
        f_pt = RIGHT*1.8 + DOWN*0.6
        ray_offsets = [-0.8, 0.0, 0.8]
        rays_in = VGroup()
        rays_out = VGroup()
        for dy in ray_offsets:
            r_in = Arrow(LEFT*4.5 + DOWN*0.6 + UP*dy,
                         conv_lens.get_left() + UP*dy*0.6,
                         color=YELLOW, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.1)
            r_out = Arrow(conv_lens.get_right() + UP*dy*0.6,
                          f_pt,
                          color=YELLOW, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.1)
            rays_in.add(r_in)
            rays_out.add(r_out)

        f_dot = Dot(f_pt, color=RED, radius=0.1)
        f_lbl = Text("F", font_size=22, color=RED, weight=BOLD)
        f_lbl.next_to(f_dot, DOWN, buff=0.12)

        # Focal length label
        f_len_line = DoubleArrow(LEFT*0.5 + DOWN*1.8, RIGHT*1.8 + DOWN*1.8,
                                  color=GREEN, buff=0, stroke_width=1.5,
                                  max_tip_length_to_length_ratio=0.08)
        f_len_lbl = Text("f (фокусна должина)", font_size=20, color=GREEN)
        f_len_lbl.next_to(f_len_line, DOWN, buff=0.1)

        uses_conv = callout("Употреба: лупа · проектор · фотоапарат · телескоп",
                             width=7.5, font_size=22, border=GREEN)
        uses_conv.to_edge(DOWN, buff=0.45)

        self.play(Create(axis))
        self.play(FadeIn(conv_lens))
        self.play(LaggedStart(*[GrowArrow(r) for r in rays_in], lag_ratio=0.15))
        self.play(LaggedStart(*[GrowArrow(r) for r in rays_out], lag_ratio=0.15))
        self.play(FadeIn(f_dot), FadeIn(f_lbl))
        self.play(Create(f_len_line), FadeIn(f_len_lbl))
        self.play(FadeIn(uses_conv))
        self.wait(2)
        self.play(FadeOut(VGroup(sec1, conv_lens, axis, rays_in, rays_out,
                                  f_dot, f_lbl, f_len_line, f_len_lbl, uses_conv)))

        # ── SECTION 2 : Расејувачка леќа ──────────────────────────────────
        sec2 = section_title("Расејувачка леќа (−) — го расејува светлото")
        self.play(Write(sec2))

        div_lens = VGroup(
            Arc(radius=2.5, start_angle=-PI/6, angle=PI/3, color=ORANGE, stroke_width=2.5),
            Arc(radius=2.5, start_angle=PI - PI/3 + PI/6, angle=PI/3, color=ORANGE, stroke_width=2.5),
        )
        div_lens.shift(LEFT*0.5 + DOWN*0.6)

        axis2 = DashedLine(LEFT*5.5, RIGHT*4.0, color=GREY, stroke_width=1).shift(DOWN*0.6)

        # Virtual focal point (left side)
        vf_pt = LEFT*2.2 + DOWN*0.6
        vf_dot = Dot(vf_pt, color=ORANGE, radius=0.08)
        vf_lbl = Text("F (виртуелна)", font_size=20, color=ORANGE)
        vf_lbl.next_to(vf_dot, DOWN, buff=0.12)

        # Diverging rays
        div_ray_data = [(-0.8, -1.5), (0.0, -0.2), (0.8, 1.1)]
        div_rays_in  = VGroup()
        div_rays_out = VGroup()
        for dy, dy_out in div_ray_data:
            r_in = Arrow(LEFT*4.5 + DOWN*0.6 + UP*dy,
                         LEFT*0.7 + DOWN*0.6 + UP*dy*0.7,
                         color=ORANGE, buff=0, stroke_width=2,
                         max_tip_length_to_length_ratio=0.1)
            r_out = Arrow(LEFT*0.7 + DOWN*0.6 + UP*dy*0.7,
                          RIGHT*3.2 + DOWN*0.6 + UP*dy_out,
                          color=ORANGE, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.1)
            div_rays_in.add(r_in)
            div_rays_out.add(r_out)

        uses_div = callout("Употреба: корекција на кратковидост (мопија)",
                            width=7.0, font_size=22, border=ORANGE)
        uses_div.to_edge(DOWN, buff=0.45)

        self.play(Create(axis2))
        self.play(FadeIn(div_lens))
        self.play(LaggedStart(*[GrowArrow(r) for r in div_rays_in], lag_ratio=0.15))
        self.play(LaggedStart(*[GrowArrow(r) for r in div_rays_out], lag_ratio=0.15))
        self.play(FadeIn(vf_dot), FadeIn(vf_lbl))
        self.play(FadeIn(uses_div))
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, div_lens, axis2, div_rays_in, div_rays_out,
                                  vf_dot, vf_lbl, uses_div)))

        # ── SECTION 3 : Диоптри ────────────────────────────────────────────
        sec3 = section_title("Диоптри — јачина на леќата")
        self.play(Write(sec3))

        diopt_box = callout("D = 1 / f     (f во метри)", width=5.5,
                             border=YELLOW, font_size=34)
        diopt_box.next_to(sec3, DOWN, buff=0.55)

        examples = VGroup(
            Text("f = 0.5 m  →  D = +2 диоптри  (збирна)", font_size=26, color=GREEN),
            Text("f = 0.25 m →  D = +4 диоптри  (лупа)",   font_size=26, color=GREEN),
            Text("f = −1.0 m →  D = −1 диоптар  (расејувачка)", font_size=26, color=ORANGE),
        )
        examples.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        examples.next_to(diopt_box, DOWN, buff=0.5)
        examples.shift(LEFT*0.3)

        self.play(FadeIn(diopt_box, shift=UP*0.15))
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT*0.2), run_time=0.55)
        self.wait(2)
        self.play(FadeOut(VGroup(sec3, diopt_box, examples)))

        # ── SECTION 4 : Окото ──────────────────────────────────────────────
        sec4 = section_title("Окото — природна камера")
        self.play(Write(sec4))

        # Eye outline
        eye_outer = Ellipse(width=3.0, height=2.0,
                             fill_color="#0a1e33", fill_opacity=1,
                             stroke_color=WHITE2, stroke_width=2)
        eye_outer.shift(LEFT*3.0 + DOWN*0.5)

        cornea   = Arc(radius=1.5, start_angle=-PI/4, angle=PI/2,
                       color=BLUE, stroke_width=2).shift(LEFT*3.0 + DOWN*0.5).shift(LEFT*0.9)
        pupil    = Circle(radius=0.3, fill_color="#000000", fill_opacity=1,
                          stroke_color=GREY, stroke_width=1).shift(LEFT*3.0 + DOWN*0.5 + LEFT*0.05)
        lens_eye = Ellipse(width=0.25, height=0.65, fill_color=BLUE,
                            fill_opacity=0.5, stroke_color=BLUE, stroke_width=1.5)
        lens_eye.shift(LEFT*3.0 + DOWN*0.5 + RIGHT*0.35)
        retina   = Arc(radius=1.45, start_angle=PI*0.6, angle=-PI*1.2,
                       color=RED, stroke_width=2.5).shift(LEFT*3.0 + DOWN*0.5)

        eye_labels = VGroup(
            Text("Рожница", font_size=18, color=BLUE).shift(LEFT*5.0 + UP*0.1),
            Text("Леќа",    font_size=18, color=BLUE).shift(LEFT*2.4 + UP*0.75),
            Text("Ретина",  font_size=18, color=RED).shift(LEFT*1.4 + DOWN*0.5),
        )

        eye_group = VGroup(eye_outer, cornea, pupil, lens_eye, retina)

        desc = VGroup(
            Text("Рожница + леќа → фокусираат светлото на ретина", font_size=23, color=WHITE2),
            Text("Акомодација = леќата ја менува формата за блиско/далечно", font_size=23, color=YELLOW),
            Text("Мозокот ја обработува сликата — тоа е видот", font_size=23, color=WHITE2),
        )
        desc.arrange(DOWN, buff=0.33, aligned_edge=LEFT)
        desc.next_to(sec4, DOWN, buff=0.5).shift(RIGHT*0.8)

        self.play(Create(eye_outer))
        self.play(Create(cornea), Create(pupil), FadeIn(lens_eye), Create(retina))
        self.play(*[FadeIn(l) for l in eye_labels])
        self.play(FadeIn(desc, shift=UP*0.1))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec4, eye_group, eye_labels, desc)))

        # ── SECTION 5 : Миопија и хиперопија ──────────────────────────────
        sec5 = section_title("Мопија и хиперопија — корекција со леќи")
        self.play(Write(sec5))

        def mini_eye(shift_pos, ray_color, focus_offset, label_text, label_color, fix_text):
            eye = Ellipse(width=2.2, height=1.5,
                          fill_color="#0a1e33", fill_opacity=1,
                          stroke_color=WHITE2, stroke_width=1.5)
            eye.shift(shift_pos)
            ret = Arc(radius=1.07, start_angle=PI*0.6, angle=-PI*1.2,
                      color=GREY, stroke_width=2).shift(shift_pos)
            focus_pt = shift_pos + RIGHT*focus_offset
            focus_d  = Dot(focus_pt, color=ray_color, radius=0.08)
            # incoming ray
            ray_a = Arrow(shift_pos + LEFT*2.5 + UP*0.4,
                          focus_pt, color=ray_color,
                          buff=0, stroke_width=1.5,
                          max_tip_length_to_length_ratio=0.1)
            ray_b = Arrow(shift_pos + LEFT*2.5 + DOWN*0.4,
                          focus_pt, color=ray_color,
                          buff=0, stroke_width=1.5,
                          max_tip_length_to_length_ratio=0.1)
            lbl = Text(label_text, font_size=20, color=label_color)
            lbl.next_to(eye, DOWN, buff=0.18)
            fix = Text(fix_text, font_size=18, color=GREEN)
            fix.next_to(lbl, DOWN, buff=0.1)
            return VGroup(eye, ret, ray_a, ray_b, focus_d, lbl, fix)

        myopia = mini_eye(LEFT*3.2 + DOWN*0.7, RED, 0.35,
                          "Мопија (кратковидост)", RED,
                          "→ Расејувачка (−D)")
        hyperopia = mini_eye(RIGHT*2.8 + DOWN*0.7, GREEN, 1.45,
                              "Хиперопија (далековидост)", ORANGE,
                              "→ Збирна (+D)")

        self.play(FadeIn(myopia), FadeIn(hyperopia))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec5, myopia, hyperopia)))

        # ── SECTION 6 : Оптички инструменти ───────────────────────────────
        sec6 = section_title("Оптички инструменти")
        self.play(Write(sec6))

        instruments = [
            ("Лупа",          "× 2–10",   YELLOW),
            ("Микроскоп",     "× до 1000", GREEN),
            ("Телескоп",      "× до 1000+", BLUE),
            ("Фотоапарат",    "× ~1",      ORANGE),
            ("Проектор",      "увеличување", PURPLE),
        ]
        rows = VGroup()
        for name, mag, col in instruments:
            nm = Text(name, font_size=26, color=WHITE2).set_width(2.8)
            mg = Text(mag,  font_size=26, color=col)
            row = VGroup(nm, mg).arrange(RIGHT, buff=0.7)
            rows.add(row)
        rows.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        rows.next_to(sec6, DOWN, buff=0.6)
        rows.shift(LEFT*1.0)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec6, rows)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Окото е леќа.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Ретината е сензор.", font_size=38, color=BLUE, weight=BOLD),
            Text("Мозокот е екран.", font_size=38, color=GREEN, weight=BOLD),
            Text("Камерата е измислена по нас.", font_size=32, color=WHITE2),
            Text("Не обратно.", font_size=44, color=RED, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.7)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Леќи · Диоптри · Окото · Мопија · Инструменти",
                     font_size=28, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
