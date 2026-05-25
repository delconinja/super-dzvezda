"""
Phys845Scene — Месечина: единствен природен сателит
Grade 8 Physics, Unit 4, Lesson 5
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


class Phys845Scene(Scene):
    def construct(self):
        # ── INTRO ──────────────────────────────────────────────────────────
        title = Text("Месечина", font_size=56, color=YELLOW, weight=BOLD)
        sub   = Text("Физика 8 · Единица 4 · Лекција 5", font_size=26, color=GREY)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ── SECTION 1 : Основни факти ──────────────────────────────────────
        sec1 = section_title("Основни факти за Месечината")
        self.play(Write(sec1))

        moon_icon = Circle(radius=1.0, fill_color="#808080", fill_opacity=0.9,
                            stroke_color=GREY, stroke_width=2)
        moon_icon.shift(LEFT*4.2 + DOWN*0.5)
        # Craters
        for cx, cy, cr in [(-4.5, -0.2, 0.18), (-3.8, -0.8, 0.12), (-4.0, 0.1, 0.1)]:
            crater = Circle(radius=cr, fill_color="#606060", fill_opacity=0.8, stroke_width=0)
            crater.move_to([cx, cy, 0])
            moon_icon = VGroup(moon_icon, crater) if not isinstance(moon_icon, VGroup) else VGroup(*moon_icon, crater)

        facts = [
            ("Пречник:",       "3 474 km  (¼ Земјата)",     WHITE2),
            ("Гравитација:",   "1.6 m/s²  (⅙ Земјата)",    WHITE2),
            ("Далечина:",      "384 400 km",                 WHITE2),
            ("Возраст:",       "4.5 милијарди години",       GREY),
            ("Атмосфера:",     "Нема",                        RED),
            ("Температура:",   "−173°C до +127°C",           ORANGE),
        ]
        fact_rows = VGroup()
        for label, val, col in facts:
            lb = Text(label, font_size=23, color=GREY).set_width(2.4)
            vl = Text(val,   font_size=23, color=col)
            fact_rows.add(VGroup(lb, vl).arrange(RIGHT, buff=0.45))
        fact_rows.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fact_rows.next_to(sec1, DOWN, buff=0.55).shift(RIGHT*0.5)

        self.play(FadeIn(moon_icon))
        for row in fact_rows:
            self.play(FadeIn(row, shift=RIGHT*0.2), run_time=0.38)
        self.wait(2)
        self.play(FadeOut(VGroup(sec1, moon_icon, fact_rows)))

        # ── SECTION 2 : Настанување — Теја ────────────────────────────────
        sec2 = section_title("Настанување — Хипотезата 'Теја'")
        self.play(Write(sec2))

        impact_box = callout(
            "Пред 4.5 милијарди години →\nПланетата 'Теја' удри во протоЗемјата →\nОтфрлените остатоци формираа Месечина.",
            width=9.5, font_size=24, border=ORANGE
        )
        impact_box.next_to(sec2, DOWN, buff=0.55)
        impact_box[0].height = 2.0
        impact_box[1].move_to(impact_box[0])

        self.play(FadeIn(impact_box))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec2, impact_box)))

        # ── SECTION 3 : Фази на Месечината ─────────────────────────────────
        sec3 = section_title("8 фази на Месечината — 29.5 дена")
        self.play(Write(sec3))

        phase_names = [
            "Млада",
            "Расечна\nсрп",
            "Прва\nчетвртина",
            "Растечка\nгиб.",
            "Полна",
            "Намалечка\nгиб.",
            "Последна\nчетвртина",
            "Намалечки\nsрп",
        ]
        # Moon phase as circles with varying lit portions
        phase_fracs = [0.0, 0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25]
        phase_dir   = [1,   1,    1,   1,    1,   -1,   -1,  -1]  # right=waxing, left=waning

        phase_group = VGroup()
        center_y    = DOWN * 0.8
        for i in range(8):
            angle = i * PI / 4
            pos   = 3.2 * np.array([np.cos(angle - PI/2), np.sin(angle - PI/2), 0])
            dark  = Circle(radius=0.42, fill_color="#1a1a2e", fill_opacity=1,
                            stroke_color=GREY, stroke_width=1.5)
            dark.move_to(pos + center_y)
            # Lit portion: ellipse overlay
            frac = phase_fracs[i]
            if frac > 0:
                lit_w  = 0.84 * frac if phase_dir[i] > 0 else 0.84 * frac
                lit    = Ellipse(width=lit_w if frac < 1 else 0.84,
                                  height=0.84,
                                  fill_color=GREY, fill_opacity=0.85, stroke_width=0)
                if phase_dir[i] > 0:
                    lit.move_to(pos + center_y + RIGHT*(0.42 - lit_w/2) if frac < 1 else pos + center_y)
                else:
                    lit.move_to(pos + center_y + LEFT*(0.42 - lit_w/2) if frac < 1 else pos + center_y)
                phase_group.add(VGroup(dark, lit))
            else:
                phase_group.add(dark)

            nm = Text(phase_names[i], font_size=14, color=WHITE2, line_spacing=0.7)
            nm.scale(0.85)
            nm.move_to(pos + center_y + normalize(pos)*1.05)
            phase_group.add(nm)

        cycle_lbl = Text("Еден циклус = 29.5 дена", font_size=24, color=YELLOW)
        cycle_lbl.to_edge(DOWN, buff=0.45)

        self.play(LaggedStart(*[FadeIn(obj) for obj in phase_group],
                               lag_ratio=0.1), run_time=2.5)
        self.play(FadeIn(cycle_lbl))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec3, phase_group, cycle_lbl)))

        # ── SECTION 4 : Плими и осеки ──────────────────────────────────────
        sec4 = section_title("Плими и осеки — гравитација на Месечина")
        self.play(Write(sec4))

        # Earth in center
        tide_earth = Circle(radius=0.7, fill_color="#1a3a5c", fill_opacity=1,
                             stroke_color=BLUE, stroke_width=2)
        tide_earth.shift(ORIGIN + DOWN*0.5)

        # Moon on right
        tide_moon = Circle(radius=0.3, fill_color="#808080", fill_opacity=0.9,
                            stroke_color=GREY, stroke_width=1.5)
        tide_moon.shift(RIGHT*3.8 + DOWN*0.5)
        moon_lbl = Text("Месечина", font_size=18, color=GREY)
        moon_lbl.next_to(tide_moon, DOWN, buff=0.15)

        # Two water bulges
        bulge_near = Ellipse(width=1.9, height=1.25,
                              fill_color="#1565c0", fill_opacity=0.5, stroke_width=0)
        bulge_near.move_to(tide_earth)
        bulge_near.shift(RIGHT*0.28)

        # Gravity arrows from moon to earth
        for dy in [-0.3, 0.0, 0.3]:
            ga = Arrow(RIGHT*3.5 + DOWN*0.5 + UP*dy,
                       RIGHT*0.75 + DOWN*0.5 + UP*dy,
                       color=RED, buff=0.05, stroke_width=1.5,
                       max_tip_length_to_length_ratio=0.15)
            self.play(GrowArrow(ga), run_time=0.3)

        tide_lbl1 = Text("Висока плима", font_size=20, color=BLUE).shift(RIGHT*0.9 + DOWN*0.5)
        tide_lbl2 = Text("(и зад Земјата)", font_size=18, color=BLUE).shift(LEFT*1.1 + DOWN*0.5)

        tide_note = callout(
            "Две високи плими на ден (~6h циклус).\nМесечината ги влече водите — Земјата се врти под нив.",
            width=9.5, font_size=23, border=BLUE
        )
        tide_note.to_edge(DOWN, buff=0.35)

        self.play(Create(tide_earth))
        self.play(FadeIn(bulge_near))
        self.play(FadeIn(tide_moon), FadeIn(moon_lbl))
        self.play(FadeIn(tide_lbl1), FadeIn(tide_lbl2))
        self.play(FadeIn(tide_note))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec4, tide_earth, bulge_near, tide_moon,
                                  moon_lbl, tide_lbl1, tide_lbl2, tide_note)))

        # ── SECTION 5 : Помрачувања ────────────────────────────────────────
        sec5 = section_title("Сончево и лунарно помрачување")
        self.play(Write(sec5))

        def eclipse_diagram(shift_pos, sun_col, earth_col, moon_col,
                             order, title_text, title_col):
            objs = []
            positions = [LEFT*2.5, ORIGIN, RIGHT*2.5]
            names     = order  # list of 3: e.g. ["Сонце", "Месечина", "Земја"]
            colors    = [sun_col, moon_col, earth_col] if names[1] != "Земја" else [sun_col, earth_col, moon_col]
            for i, (nm, col) in enumerate(zip(names, [sun_col, moon_col if "Месечина" in names[1] else earth_col,
                                                        earth_col if "Земја" in names[2] else moon_col])):
                r = 0.55 if nm == "Сонце" else (0.4 if nm == "Земја" else 0.22)
                c = Circle(radius=r, fill_color=col, fill_opacity=0.9, stroke_width=0)
                c.move_to(positions[i] + shift_pos)
                lb = Text(nm, font_size=16, color=WHITE2).next_to(c, DOWN, buff=0.1)
                objs.extend([c, lb])
            t = Text(title_text, font_size=22, color=title_col, weight=BOLD)
            t.move_to(shift_pos + UP*1.4)
            objs.append(t)
            return VGroup(*objs)

        solar_ecl = eclipse_diagram(
            LEFT*2.5 + DOWN*0.8,
            YELLOW, BLUE, GREY,
            ["Сонце", "Месечина", "Земја"],
            "Сончево помрачување", YELLOW
        )
        lunar_ecl = eclipse_diagram(
            RIGHT*2.5 + DOWN*0.8,
            YELLOW, BLUE, RED,
            ["Сонце", "Земја", "Месечина"],
            "Лунарно помрачување", RED
        )

        solar_note = Text("Сенката на Месечина → на Земјата",
                           font_size=18, color=GREY)
        solar_note.next_to(solar_ecl, DOWN, buff=0.1)
        lunar_note = Text("Сенката на Земјата → Месечина изгледа ЧЕРВЕНА",
                           font_size=18, color=RED)
        lunar_note.next_to(lunar_ecl, DOWN, buff=0.1)

        divider2 = DashedLine(UP*2.5, DOWN*3.2, color=GREY, stroke_width=1)

        self.play(FadeIn(solar_ecl), FadeIn(lunar_ecl))
        self.play(FadeIn(solar_note), FadeIn(lunar_note))
        self.play(Create(divider2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(sec5, solar_ecl, lunar_ecl,
                                  solar_note, lunar_note, divider2)))

        # ── SECTION 6 : Аполо 11 ──────────────────────────────────────────
        sec6 = section_title("Аполо 11 — 20 јули 1969")
        self.play(Write(sec6))

        apollo_box = callout(
            "Нил Армстронг — прв човек на Месечина\n\"One small step for man, one giant leap for mankind.\"",
            width=10.0, font_size=24, border=YELLOW
        )
        apollo_box.next_to(sec6, DOWN, buff=0.55)

        timeline = VGroup(
            Text("1957 → Спутник 1 (СССР) — прв сателит",   font_size=23, color=WHITE2),
            Text("1961 → Јуриј Гагарин — прв човек во свемир", font_size=23, color=WHITE2),
            Text("1969 → Аполо 11 → Армстронг на Месечина",  font_size=23, color=YELLOW),
            Text("2024 → НАСА Артемис — враќање на Месечина",  font_size=23, color=BLUE),
        )
        timeline.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        timeline.next_to(apollo_box, DOWN, buff=0.5)
        timeline.shift(LEFT*0.5)

        self.play(FadeIn(apollo_box))
        for item in timeline:
            self.play(FadeIn(item, shift=RIGHT*0.2), run_time=0.45)
        self.wait(2)
        self.play(FadeOut(VGroup(sec6, apollo_box, timeline)))

        # ── ANDONOVSKI MOMENT ──────────────────────────────────────────────
        quote_lines = VGroup(
            Text("Нил Армстронг чекна на Месечина во 1969.", font_size=30, color=YELLOW, weight=BOLD),
            Text("Прв чекор.", font_size=40, color=WHITE2, weight=BOLD),
            Text("Еден чекор.", font_size=40, color=WHITE2, weight=BOLD),
            Text("Цела историја.", font_size=38, color=ORANGE, weight=BOLD),
            Text("Потоа тишина. 50 години — никој друг.", font_size=28, color=GREY),
        )
        quote_lines.arrange(DOWN, buff=0.38)
        quote_lines.move_to(ORIGIN)
        for line in quote_lines:
            self.play(Write(line), run_time=0.75)
        self.wait(3)
        self.play(*[FadeOut(l) for l in quote_lines])

        # ── OUTRO ─────────────────────────────────────────────────────────
        outro = Text("Фази · Плими · Помрачувања · Аполо 11",
                     font_size=30, color=GREY)
        outro.move_to(ORIGIN)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
