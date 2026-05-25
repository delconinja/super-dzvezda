"""
Phys834Scene — Рефракција (прелом) на светлина
Grade 8 Physics, Unit 3, Lesson 4
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


class Phys834Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Рефракција на светлина", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 3 · Лекција 4", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Što е рефракција ───────────────────────────────────
        sec1 = section_title("Рефракција = промена на насока")
        defn = callout(
            "Светлината ја менува насоката кога минува\nод една средина во друга со поинаква оптичка густина.",
            width=10.0, font_size=24
        )
        defn.next_to(sec1, DOWN, buff=0.55)
        self.play(Write(sec1))
        self.play(FadeIn(defn, shift=UP*0.15))
        self.wait(1.5)

        # Ray bending diagram
        # Medium boundary: horizontal line
        boundary = Line(LEFT*5, RIGHT*5, color=GREY, stroke_width=1.5).shift(DOWN*0.2)
        air_lbl  = Text("Воздух", font_size=22, color=BLUE).move_to(LEFT*3.8 + UP*0.8)
        water_lbl= Text("Вода", font_size=22, color=BLUE).move_to(LEFT*3.8 + DOWN*1.0)

        # Incident ray: coming from top-left toward boundary point
        hit_pt = boundary.get_center()
        inc_ray = Arrow(hit_pt + UP*1.8 + LEFT*1.3, hit_pt, color=YELLOW,
                        buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        # Refracted ray: bends toward normal (steeper) in water
        ref_ray = Arrow(hit_pt, hit_pt + DOWN*1.8 + RIGHT*0.7, color=ORANGE,
                        buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        # Normal line
        normal = DashedLine(hit_pt + UP*2.0, hit_pt + DOWN*2.0,
                            color=GREY, stroke_width=1.5)

        angle1_arc = Arc(radius=0.55, start_angle=PI/2, angle=-PI/4,
                         color=WHITE2, stroke_width=1.5).move_to(hit_pt)
        angle2_arc = Arc(radius=0.55, start_angle=-PI/2, angle=PI/6,
                         color=GREEN, stroke_width=1.5).move_to(hit_pt)
        a1_lbl = Text("θ₁", font_size=20, color=WHITE2).move_to(hit_pt + UP*0.75 + RIGHT*0.55)
        a2_lbl = Text("θ₂", font_size=20, color=GREEN).move_to(hit_pt + DOWN*0.75 + RIGHT*0.45)

        diagram = VGroup(boundary, air_lbl, water_lbl, normal,
                         inc_ray, ref_ray, angle1_arc, angle2_arc, a1_lbl, a2_lbl)
        diagram.shift(DOWN*0.9 + RIGHT*2.0)

        self.play(Create(boundary), FadeIn(air_lbl), FadeIn(water_lbl))
        self.play(Create(normal))
        self.play(GrowArrow(inc_ray))
        self.play(GrowArrow(ref_ray))
        self.play(Create(angle1_arc), FadeIn(a1_lbl), Create(angle2_arc), FadeIn(a2_lbl))
        self.wait(2)
        self.play(FadeOut(VGroup(sec1, defn, diagram)))

        # ── SECTION 2 : Брзини во различни средини ─────────────────────────
        sec2 = section_title("Светлината успорува во погуста средина")
        self.play(Write(sec2))

        media = [
            ("Вакуум",   "300 000 km/s", YELLOW,  1.0),
            ("Воздух",   "299 700 km/s", BLUE,    1.0),
            ("Вода",     "225 000 km/s", BLUE,    0.75),
            ("Стакло",   "200 000 km/s", GREEN,   0.67),
            ("Дијамант", "120 000 km/s", PURPLE,  0.40),
        ]
        rows = VGroup()
        for i, (name, speed, col, frac) in enumerate(media):
            name_t  = Text(name,  font_size=26, color=WHITE2).set_width(2.2)
            speed_t = Text(speed, font_size=26, color=col)
            bar     = Rectangle(width=4.0*frac, height=0.28,
                                 fill_color=col, fill_opacity=0.75, stroke_width=0)
            row = VGroup(name_t, speed_t, bar).arrange(RIGHT, buff=0.45)
            rows.add(row)
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        rows.next_to(sec2, DOWN, buff=0.6)
        rows.shift(LEFT*0.5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2)
        self.play(FadeOut(VGroup(sec2, rows)))

        # ── SECTION 3 : Закон на Снел ──────────────────────────────────────
        sec3 = section_title("Закон на Снел")
        snell_box = callout("n₁ × sin(θ₁) = n₂ × sin(θ₂)", width=7.0,
                             border=YELLOW, font_size=32)
        snell_box.next_to(sec3, DOWN, buff=0.55)

        idx_title = Text("Индекс на прекршување", font_size=28, color=GREY)
        idx_title.next_to(snell_box, DOWN, buff=0.6)
        idx_data = [
            ("Воздух",   "1.00", BLUE),
            ("Вода",     "1.33", BLUE),
            ("Стакло",   "1.50", GREEN),
            ("Дијамант", "2.42", PURPLE),
        ]
        idx_rows = VGroup()
        for name, val, col in idx_data:
            n_t = Text(name, font_size=25, color=WHITE2).set_width(2.4)
            v_t = Text(val,  font_size=25, color=col, weight=BOLD)
            r   = VGroup(n_t, v_t).arrange(RIGHT, buff=0.6)
            idx_rows.add(r)
        idx_rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        idx_rows.next_to(idx_title, DOWN, buff=0.3)
        idx_rows.shift(LEFT*0.5)

        self.play(Write(sec3))
        self.play(FadeIn(snell_box, shift=UP*0.15))
        self.play(FadeIn(idx_title))
        for r in idx_rows:
            self.play(FadeIn(r), run_time=0.4)
        self.wait(2)
        self.play(FadeOut(VGroup(sec3, snell_box, idx_title, idx_rows)))

        # ── SECTION 4 : Молив во вода / Базен ─────────────────────────────
        sec4 = section_title("Оптичка илузија — молив и базен")
        self.play(Write(sec4))

        # Pencil in water illusion sketch
        tank_rect = Rectangle(width=3.2, height=2.4, stroke_color=BLUE,
                               fill_color="#0a1a2e", fill_opacity=1, stroke_width=2)
        tank_rect.shift(LEFT*2.5 + DOWN*0.8)
        water_fill = Rectangle(width=3.2, height=1.4, stroke_width=0,
                                fill_color="#1a3a5c", fill_opacity=0.6)
        water_fill.align_to(tank_rect, DOWN).shift(LEFT*2.5)
        # pencil: above water straight, below bent
        pencil_above = Line(
            tank_rect.get_center() + UP*0.5 + LEFT*0.3,
            tank_rect.get_center() + UP*0.0 + LEFT*0.05,
            color=YELLOW, stroke_width=5
        )
        pencil_below = Line(
            tank_rect.get_center() + UP*0.0 + LEFT*0.05,
            tank_rect.get_center() + DOWN*0.9 + LEFT*0.5,
            color=YELLOW, stroke_width=5
        )
        water_surf = DashedLine(
            tank_rect.get_left() + UP*0.05,
            tank_rect.get_right() + UP*0.05,
            color=BLUE, stroke_width=1
        )

        pencil_lbl = Text("Молив изгледа скршен!", font_size=24, color=ORANGE)
        pencil_lbl.next_to(tank_rect, DOWN, buff=0.25)

        pool_txt = callout(
            "Базенот изгледа поплиток отколку што е.\nСветлината се прекршува кон очите.",
            width=5.5, font_size=22, border=GREEN
        )
        pool_txt.next_to(sec4, DOWN, buff=0.55).shift(RIGHT*1.8)

        self.play(Create(tank_rect), FadeIn(water_fill))
        self.play(Create(water_surf))
        self.play(Create(pencil_above), Create(pencil_below))
        self.play(FadeIn(pencil_lbl))
        self.play(FadeIn(pool_txt, shift=LEFT*0.2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec4, tank_rect, water_fill, water_surf,
                                  pencil_above, pencil_below, pencil_lbl, pool_txt)))

        # ── SECTION 5 : Виножито ──────────────────────────────────────────
        sec5 = section_title("Виножито — природна рефракција")
        self.play(Write(sec5))

        steps = VGroup(
            Text("1. Бела светлина влегува во капка вода → рефракција", font_size=25, color=WHITE2),
            Text("2. Внатрешна рефлексија во капката", font_size=25, color=WHITE2),
            Text("3. Излегување → втора рефракција → дисперзија на бои", font_size=25, color=WHITE2),
            Text("Различни бои излегуваат под различни агли.", font_size=25, color=YELLOW),
        )
        steps.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        steps.next_to(sec5, DOWN, buff=0.55)
        steps.shift(LEFT*0.5)

        # Simple rainbow arc
        rainbow_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        arcs = VGroup()
        for i, col in enumerate(rainbow_colors):
            r_val = 1.2 + i * 0.18
            a = Arc(radius=r_val, start_angle=0, angle=PI,
                    color=col, stroke_width=3)
            a.shift(RIGHT*4.5 + DOWN*0.5)
            arcs.add(a)

        self.play(Create(arcs), run_time=1.2)
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT*0.15), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(VGroup(sec5, steps, arcs)))

        # ── SECTION 6 : Леќи ──────────────────────────────────────────────
        sec6 = section_title("Леќи — збирна и расејувачка")
        self.play(Write(sec6))

        # Converging lens sketch (left)
        conv_label = Text("Збирна (+)", font_size=26, color=YELLOW, weight=BOLD)
        conv_label.shift(LEFT*3.5 + UP*0.8)

        # Lens shape using arc pair
        lens_l = Arc(radius=1.2, start_angle=-PI/3, angle=2*PI/3,
                     color=BLUE, stroke_width=3).shift(LEFT*3.5 + DOWN*0.2)
        lens_r = Arc(radius=1.2, start_angle=PI - PI/3, angle=2*PI/3,
                     color=BLUE, stroke_width=3).shift(LEFT*3.5 + DOWN*0.2)

        # Rays through converging lens
        focal_pt_c = LEFT*1.8 + DOWN*0.2
        r1c = Arrow(LEFT*5.2 + UP*0.55, focal_pt_c, color=YELLOW,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        r2c = Arrow(LEFT*5.2 + DOWN*0.2, focal_pt_c, color=YELLOW,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        r3c = Arrow(LEFT*5.2 + DOWN*0.95, focal_pt_c, color=YELLOW,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        f_dot_c = Dot(focal_pt_c, color=RED, radius=0.1)
        f_lbl_c = Text("F", font_size=20, color=RED).next_to(f_dot_c, DOWN, buff=0.1)

        # Diverging lens sketch (right)
        div_label = Text("Расејувачка (−)", font_size=26, color=ORANGE, weight=BOLD)
        div_label.shift(RIGHT*2.5 + UP*0.8)

        lens_dl = Arc(radius=1.5, start_angle=-PI/3+0.3, angle=2*PI/3-0.6,
                      color=ORANGE, stroke_width=3).shift(RIGHT*2.5 + DOWN*0.2)
        lens_dr = Arc(radius=1.5, start_angle=PI-PI/3+0.3, angle=2*PI/3-0.6,
                      color=ORANGE, stroke_width=3).shift(RIGHT*2.5 + DOWN*0.2)

        r1d_start = LEFT*0.2 + UP*0.55
        r1d_end   = RIGHT*4.5 + UP*1.4
        r2d_start = LEFT*0.2 + DOWN*0.2
        r2d_end   = RIGHT*4.5 + DOWN*0.2
        r3d_start = LEFT*0.2 + DOWN*0.95
        r3d_end   = RIGHT*4.5 + DOWN*1.7

        r1d = Arrow(r1d_start, r1d_end, color=ORANGE,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        r2d = Arrow(r2d_start, r2d_end, color=ORANGE,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        r3d = Arrow(r3d_start, r3d_end, color=ORANGE,
                    buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.1)

        uses_c = Text("Лупа · Проектор · Фотоапарат", font_size=20, color=GREEN)
        uses_c.shift(LEFT*3.5 + DOWN*2.3)
        uses_d = Text("Корекција на кратковидост", font_size=20, color=GREEN)
        uses_d.shift(RIGHT*2.5 + DOWN*2.3)

        self.play(Create(lens_l), Create(lens_r), FadeIn(conv_label))
        self.play(GrowArrow(r1c), GrowArrow(r2c), GrowArrow(r3c), run_time=0.9)
        self.play(FadeIn(f_dot_c), FadeIn(f_lbl_c), FadeIn(uses_c))
        self.play(Create(lens_dl), Create(lens_dr), FadeIn(div_label))
        self.play(GrowArrow(r1d), GrowArrow(r2d), GrowArrow(r3d), run_time=0.9)
        self.play(FadeIn(uses_d))
        self.wait(2)
        self.play(FadeOut(VGroup(sec6, conv_label, lens_l, lens_r,
                                  r1c, r2c, r3c, f_dot_c, f_lbl_c, uses_c,
                                  div_label, lens_dl, lens_dr, r1d, r2d, r3d, uses_d)))

        # ── SECTION 7 : Тотална внатрешна рефлексија ──────────────────────
        sec7 = section_title("Тотална внатрешна рефлексија")
        self.play(Write(sec7))

        fibre_box = callout(
            "Кога светлината удира под голем агол →\nне излегува — се одбива целосно внатре.",
            width=9.0, font_size=25, border=PURPLE
        )
        fibre_box.next_to(sec7, DOWN, buff=0.5)

        # Optical fibre sketch
        fibre_top = Line(LEFT*4, RIGHT*4, color=BLUE, stroke_width=3).shift(DOWN*1.6)
        fibre_bot = Line(LEFT*4, RIGHT*4, color=BLUE, stroke_width=3).shift(DOWN*2.8)

        bounce_pts = [
            LEFT*4    + DOWN*2.0,
            LEFT*2    + DOWN*1.7,
            ORIGIN    + DOWN*2.7,
            RIGHT*2   + DOWN*1.8,
            RIGHT*4   + DOWN*2.3,
        ]
        fibre_ray = VMobject(color=YELLOW, stroke_width=2.5)
        fibre_ray.set_points_as_corners(bounce_pts)

        fibre_lbl = Text("Оптичко влакно — интернет со светлина", font_size=24, color=GREEN)
        fibre_lbl.shift(DOWN*3.5)

        self.play(FadeIn(fibre_box, shift=UP*0.15))
        self.play(Create(fibre_top), Create(fibre_bot))
        self.play(Create(fibre_ray), run_time=1.2)
        self.play(FadeIn(fibre_lbl))
        self.wait(2)
        self.play(FadeOut(VGroup(sec7, fibre_box, fibre_top, fibre_bot, fibre_ray, fibre_lbl)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Светлината влегува во вода.", font_size=36, color=YELLOW, weight=BOLD),
            Text("Успорува.", font_size=36, color=ORANGE, weight=BOLD),
            Text("Свиткува.", font_size=36, color=GREEN, weight=BOLD),
            Text("Зошто? Затоа што водата е погуста.", font_size=32, color=WHITE2),
            Text("Физиката нема исклучоци.", font_size=38, color=RED, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.4)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.7)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Рефракција · Снел · Леќи · Виножито",
                     font_size=32, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
