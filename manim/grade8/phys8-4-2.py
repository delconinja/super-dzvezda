"""
Phys842Scene — Годишни времиња
Grade 8 Physics, Unit 4, Lesson 2
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


class Phys842Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Годишни времиња", font_size=52, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 4 · Лекција 2", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Митот (погрешна идеја) ─────────────────────────────
        sec1 = section_title("МИТ: Лето = поблиску до Сонцето?")
        self.play(Write(sec1))

        myth_box = RoundedRectangle(width=9.5, height=1.5, corner_radius=0.3,
                                     fill_color="#2d0a0a", fill_opacity=1,
                                     stroke_color=RED, stroke_width=2)
        myth_box.next_to(sec1, DOWN, buff=0.5)
        myth_text = Text("ПОГРЕШНО! Земјата е поблиску до Сонцето во ЈАНУАРИ!",
                          font_size=26, color=RED, weight=BOLD)
        myth_text.move_to(myth_box)

        fact_box = callout(
            "Причина за сезоните: НАКОСЕНОСТА на оската за 23.5°\nНЕ далечината до Сонцето.",
            width=9.5, font_size=25, border=GREEN
        )
        fact_box.next_to(myth_box, DOWN, buff=0.4)

        self.play(FadeIn(myth_box), Write(myth_text))
        self.play(FadeIn(fact_box, shift=UP*0.15))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec1, myth_box, myth_text, fact_box)))

        # ── SECTION 2 : Орбита со 4 позиции ────────────────────────────────
        sec2 = section_title("Оската на Земјата е накосена 23.5°")
        self.play(Write(sec2))

        # Sun at center
        sun_c = Circle(radius=0.5, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        sun_c.move_to(ORIGIN + DOWN*0.3)

        # Orbit ellipse
        orbit = Ellipse(width=8.5, height=3.8, stroke_color=GREY,
                         stroke_width=1.5, fill_opacity=0)
        orbit.move_to(ORIGIN + DOWN*0.3)

        # 4 Earth positions
        positions = {
            "Лето (СХ)"    : (LEFT*4.0  + DOWN*0.3, YELLOW,  "21 јуни"),
            "Есен"         : (DOWN*1.7  + DOWN*0.3, BLUE,    "23 септ"),
            "Зима (СХ)"    : (RIGHT*4.0 + DOWN*0.3, BLUE,    "22 дек"),
            "Пролет"       : (UP*1.7   + DOWN*0.3, GREEN,   "21 март"),
        }

        earth_objs = VGroup()
        for label, (pos, col, date) in positions.items():
            e = Circle(radius=0.35, fill_color="#1a3a5c", fill_opacity=1,
                       stroke_color=col, stroke_width=2)
            e.move_to(pos)
            # Axis tilt (always same direction in space)
            ax = Line(pos + UP*0.5 + LEFT*0.12,
                      pos + DOWN*0.5 + RIGHT*0.12,
                      color=GREY, stroke_width=1.5)
            lbl = Text(label, font_size=16, color=col)
            lbl.next_to(e, DOWN if pos[1] <= 0 else UP, buff=0.12)
            dt_lbl = Text(date, font_size=14, color=GREY)
            dt_lbl.next_to(lbl, DOWN, buff=0.06)
            earth_objs.add(VGroup(e, ax, lbl, dt_lbl))

        self.play(Create(orbit), FadeIn(sun_c))
        for obj in earth_objs:
            self.play(FadeIn(obj), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec2, sun_c, orbit, earth_objs)))

        # ── SECTION 3 : Агол на зраците ────────────────────────────────────
        sec3 = section_title("Зошто е потопло лето? — Агол на зраците")
        self.play(Write(sec3))

        # Left: direct rays (summer)
        surface_s = Line(LEFT*2.0, RIGHT*0.5, color=GREEN, stroke_width=3).shift(LEFT*3.5 + DOWN*1.0)
        for i in range(3):
            r = Arrow(LEFT*3.5 + RIGHT*i*0.4 + UP*1.8,
                      LEFT*3.5 + RIGHT*i*0.4 + DOWN*1.0,
                      color=YELLOW, buff=0, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.12)
            self.play(GrowArrow(r), run_time=0.3)
        summer_lbl = Text("Лето — прав агол\nКонцентрирана енергија → топло",
                           font_size=22, color=YELLOW)
        summer_lbl.shift(LEFT*3.5 + DOWN*2.2)

        # Right: shallow rays (winter)
        surface_w = Line(LEFT*0.5, RIGHT*2.5, color=BLUE, stroke_width=3).shift(RIGHT*2.0 + DOWN*1.0)
        for i in range(4):
            angle = -PI/4
            dx = i * 0.55
            start = RIGHT*2.0 + LEFT*0.8 + RIGHT*dx + UP*1.5
            end   = start + normalize(np.array([np.cos(angle+PI/2)*0.6,
                                                 np.sin(angle+PI/2)*0.6, 0]))*(-2.2)
            ra = Arrow(start, end, color=BLUE, buff=0, stroke_width=2,
                       max_tip_length_to_length_ratio=0.12)
            self.play(GrowArrow(ra), run_time=0.3)
        winter_lbl = Text("Зима — косо (плиток агол)\nРазредена енергија → ладно",
                           font_size=22, color=BLUE)
        winter_lbl.shift(RIGHT*2.5 + DOWN*2.2)

        divider = DashedLine(UP*2.5, DOWN*2.8, color=GREY, stroke_width=1).shift(LEFT*0.5)

        self.play(Create(surface_s), Create(surface_w))
        self.play(FadeIn(summer_lbl), FadeIn(winter_lbl))
        self.play(Create(divider))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec3, surface_s, surface_w,
                                  summer_lbl, winter_lbl, divider)))

        # ── SECTION 4 : Двете полутопки ────────────────────────────────────
        sec4 = section_title("Две полутопки — спротивни сезони")
        self.play(Write(sec4))

        hemi_box = callout(
            "Кога е лето во северната полутопка →\nво јужната е ЗИМА и обратно.",
            width=9.0, font_size=26, border=ORANGE
        )
        hemi_box.next_to(sec4, DOWN, buff=0.55)

        hemi_table = VGroup(
            Text("Македонија (СП)     Австралија (ЈП)", font_size=26, color=WHITE2),
            Text("Јуни → ЛЕТО                   ЗИМА",  font_size=25, color=YELLOW),
            Text("Декември → ЗИМА               ЛЕТО",   font_size=25, color=BLUE),
        )
        hemi_table.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        hemi_table.next_to(hemi_box, DOWN, buff=0.5)
        hemi_table.shift(LEFT*0.5)

        self.play(FadeIn(hemi_box))
        for row in hemi_table:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(VGroup(sec4, hemi_box, hemi_table)))

        # ── SECTION 5 : Солстиции и рамнодневици ───────────────────────────
        sec5 = section_title("Солстиции и рамнодневици")
        self.play(Write(sec5))

        cal_data = [
            ("21 март",   "Пролетна рамнодневица",  "12h ден / 12h ноќ",  GREEN),
            ("21 јуни",   "Летна солстиција",        "Најдолг ден",        YELLOW),
            ("23 септ",   "Есенска рамнодневица",    "12h ден / 12h ноќ",  ORANGE),
            ("22 декември","Зимска солстиција",       "Најкраток ден",       BLUE),
        ]
        cal_rows = VGroup()
        for date, event, note, col in cal_data:
            dt = Text(date,  font_size=22, color=col, weight=BOLD).set_width(2.0)
            ev = Text(event, font_size=22, color=WHITE2).set_width(3.5)
            nt = Text(note,  font_size=20, color=GREY)
            row = VGroup(dt, ev, nt).arrange(RIGHT, buff=0.4)
            cal_rows.add(row)
        cal_rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        cal_rows.next_to(sec5, DOWN, buff=0.55)
        cal_rows.shift(LEFT*0.5)

        for row in cal_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec5, cal_rows)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Не сонцето е поблиску лето.", font_size=34, color=WHITE2, weight=BOLD),
            Text("Земјата е свртена.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Само 23.5°.", font_size=46, color=ORANGE, weight=BOLD),
            Text("Тоа е доволно за снег.", font_size=32, color=BLUE),
            Text("Или за плажа.", font_size=38, color=GREEN, weight=BOLD),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.72)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Сезони · Накосеност 23.5° · Солстиции · Рамнодневици",
                     font_size=27, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
