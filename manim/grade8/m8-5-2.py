"""
m8-5-2  —  Обработка и претставување на податоци
Математика 8, Единица 5: Ракување со податоци

Andonovski-style: средната, медијаната, модата — три ликови со три карактери.
Render:  manim -ql m8-5-2.py M852Scene
Output:  media/videos/m8-5-2/480p15/M852Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE      = "#4fc3f7"
YELLOW    = "#ffd54f"
GREEN     = "#81c784"
RED       = "#e57373"
GREY      = "#90a4ae"
ORANGE    = "#ffb74d"
PURPLE    = "#ce93d8"
WHITE2    = "#e8eaf0"
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


def measure_card(name, formula, value, color=BLUE, w=3.0, h=2.6):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    nm = Text(name, font_size=24, color=color, weight=BOLD)
    fm = MathTex(formula, font_size=28, color=WHITE2)
    vl = Text(value, font_size=26, color=YELLOW, weight=BOLD)
    nm.move_to(box.get_top() + DOWN * 0.4)
    fm.move_to(box.get_center())
    vl.move_to(box.get_bottom() + UP * 0.4)
    return VGroup(box, nm, fm, vl)


class M852Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Средината ja сака рамнотежата.", font_size=34, color=BLUE, weight=BOLD)
        h2 = Text("Медијаната ja чува правдата.", font_size=34, color=GREEN, weight=BOLD)
        h3 = Text("Модата ja прати толпата.", font_size=34, color=ORANGE, weight=BOLD)
        h4 = Text("Различни прашања — различни одговори.", font_size=30, color=WHITE2)

        hooks = VGroup(h1, h2, h3, h4).arrange(DOWN, buff=0.35)
        hooks.move_to(ORIGIN)

        for h in hooks:
            self.play(Write(h), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(hooks), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ЧЕТИРИ МЕРКИ                                    ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("four_measures")

        title2 = section_title("Четири мерки за множество {2, 4, 6, 8}")
        self.play(Write(title2), run_time=1.0)

        dataset = MathTex(r"\{2,\;4,\;6,\;8\}", font_size=42, color=WHITE2)
        dataset.move_to(UP * 1.9)
        self.play(Write(dataset), run_time=0.8)

        mean = measure_card(
            "Средина",
            r"\frac{2+4+6+8}{4}",
            "= 5",
            color=BLUE,
        )
        median = measure_card(
            "Медијана",
            r"\frac{4+6}{2}",
            "= 5",
            color=GREEN,
        )
        mode = measure_card(
            "Мода",
            r"\text{нема}",
            "(сите ист)",
            color=ORANGE,
        )
        rng = measure_card(
            "Ранг",
            r"8 - 2",
            "= 6",
            color=PURPLE,
        )

        cards = VGroup(mean, median, mode, rng).arrange(RIGHT, buff=0.25)
        cards.scale(0.85)
        cards.move_to(DOWN * 0.6)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  КОГА КОЈА?                                      ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("when_which")

        title3 = section_title("Која мерка кога?")
        self.play(Write(title3), run_time=1.0)

        rules = [
            ("Средина", "кога нема екстремни вредности", BLUE),
            ("Медијана", "кога има екстремни (поробусна)", GREEN),
            ("Мода", "за категориски податоци", ORANGE),
            ("Ранг", "ja покажува разликата", PURPLE),
        ]

        rule_grp = VGroup()
        for name, desc, col in rules:
            n = Text(name, font_size=30, color=col, weight=BOLD)
            arrow = Text("→", font_size=30, color=YELLOW)
            d = Text(desc, font_size=26, color=WHITE2)
            row = VGroup(n, arrow, d).arrange(RIGHT, buff=0.3)
            rule_grp.add(row)
        rule_grp.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rule_grp.move_to(ORIGIN)

        for r in rule_grp:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # Outlier example
        self.play(FadeOut(rule_grp), run_time=0.5)

        out_title = Text("Пример со екстрем", font_size=30, color=ORANGE, weight=BOLD)
        out_title.move_to(UP * 1.6)
        self.play(Write(out_title), run_time=0.8)

        ds = MathTex(r"\{2,\;3,\;3,\;4,\;100\}", font_size=42, color=WHITE2)
        ds.move_to(UP * 0.7)
        self.play(Write(ds), run_time=0.8)

        mean_b = MathTex(r"\text{Средина} = 22{,}4 \;\;\text{(влече ja 100)}",
                         font_size=32, color=RED)
        med_b = MathTex(r"\text{Медијана} = 3 \;\;\text{(не реагира)}",
                        font_size=32, color=GREEN)
        mean_b.move_to(DOWN * 0.2)
        med_b.next_to(mean_b, DOWN, buff=0.4)

        self.play(Write(mean_b), run_time=1.0)
        self.play(Write(med_b), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ТИПОВИ ГРАФИЦИ                                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("graph_types")

        title4 = section_title("Типови графици")
        self.play(Write(title4), run_time=1.0)

        # Bar chart with gaps
        ax1 = Axes(
            x_range=[0, 5, 1], y_range=[0, 8, 2],
            x_length=4.5, y_length=2.5,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax1.move_to(LEFT * 3.5 + UP * 0.8)

        bar_heights = [3, 6, 4, 7]
        bars1 = VGroup()
        for i, h in enumerate(bar_heights):
            b = Rectangle(
                width=0.6, height=h * 0.31,
                fill_color=BLUE, fill_opacity=0.7,
                stroke_color=BLUE, stroke_width=2,
            )
            b.move_to(ax1.c2p(i + 0.7, h / 2))
            bars1.add(b)

        bar_lbl = Text("Столбест (со празнини)", font_size=22, color=BLUE)
        bar_lbl.next_to(ax1, DOWN, buff=0.2)

        # Histogram - no gaps
        ax2 = Axes(
            x_range=[0, 5, 1], y_range=[0, 8, 2],
            x_length=4.5, y_length=2.5,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax2.move_to(RIGHT * 3.5 + UP * 0.8)

        hist_heights = [2, 5, 6, 3]
        bars2 = VGroup()
        for i, h in enumerate(hist_heights):
            b = Rectangle(
                width=1.05, height=h * 0.31,
                fill_color=GREEN, fill_opacity=0.7,
                stroke_color=GREEN, stroke_width=2,
            )
            b.move_to(ax2.c2p(i + 0.5, h / 2))
            bars2.add(b)

        hist_lbl = Text("Хистограм (без празнини)", font_size=22, color=GREEN)
        hist_lbl.next_to(ax2, DOWN, buff=0.2)

        self.play(Create(ax1), Create(ax2), run_time=1.0)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars1],
                  *[GrowFromEdge(b, DOWN) for b in bars2],
                  run_time=1.0)
        self.play(Write(bar_lbl), Write(hist_lbl), run_time=0.8)
        self.wait(1.5)

        # Use case note
        note = Text("Столбест — дискретни.   Хистограм — континуирани.",
                    font_size=24, color=YELLOW)
        note.move_to(DOWN * 2.3)
        self.play(Write(note), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ПИТА И ЛИНИСКИ                                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pie_line")

        title5 = section_title("Пита и линиски")
        self.play(Write(title5), run_time=1.0)

        # Pie chart left
        center_pie = LEFT * 3.5 + DOWN * 0.2
        sectors_data = [
            (0.25, BLUE,   "25%"),
            (0.30, GREEN,  "30%"),
            (0.20, ORANGE, "20%"),
            (0.25, RED,    "25%"),
        ]
        radius = 1.6
        start_angle = 90 * DEGREES
        sectors = VGroup()
        labels = VGroup()
        cur = start_angle
        for frac, col, lbl in sectors_data:
            ang = frac * TAU
            sec = AnnularSector(
                inner_radius=0, outer_radius=radius,
                start_angle=cur, angle=ang,
                fill_color=col, fill_opacity=0.8,
                stroke_color=WHITE2, stroke_width=2,
            )
            sec.move_arc_center_to(center_pie)
            sectors.add(sec)
            # Label
            mid = cur + ang / 2
            lpos = center_pie + np.array([np.cos(mid) * (radius + 0.5),
                                           np.sin(mid) * (radius + 0.5), 0])
            t = Text(lbl, font_size=20, color=col, weight=BOLD)
            t.move_to(lpos)
            labels.add(t)
            cur += ang

        for s, l in zip(sectors, labels):
            self.play(Create(s), FadeIn(l), run_time=0.4)

        pie_note = Text(r"25% × 360° = 90°", font_size=22, color=YELLOW)
        pie_note.move_to(center_pie + DOWN * 2.4)
        self.play(Write(pie_note), run_time=0.8)

        # Line chart right
        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 10, 2],
            x_length=4.5, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax.move_to(RIGHT * 3.5 + UP * 0.0)

        pts = [(1, 3), (2, 5), (3, 4), (4, 7), (5, 6)]
        coords = [ax.c2p(x, y) for x, y in pts]
        line = VMobject(stroke_color=YELLOW, stroke_width=4)
        line.set_points_as_corners(coords)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.06) for p in coords])

        line_lbl = Text("Линиски — тренд во време", font_size=22, color=YELLOW)
        line_lbl.next_to(ax, DOWN, buff=0.2)

        self.play(Create(ax), run_time=0.8)
        self.play(Create(line), FadeIn(dots), run_time=1.2)
        self.play(Write(line_lbl), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  СТЕБЛО И ЛИСТ                                   ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("stem_leaf")

        title6 = section_title("Стебло и лист")
        self.play(Write(title6), run_time=1.0)

        sub = Text("Цифрите на десетки = стебло. Цифрите на единици = лист.",
                   font_size=24, color=WHITE2)
        sub.move_to(UP * 2.0)
        self.play(Write(sub), run_time=1.2)

        # Heights 145-168
        stems = ["14", "15", "16"]
        leaves = ["5 8 9", "0 2 5 5 7", "1 3 8"]

        header = VGroup(
            Text("Стебло", font_size=26, color=YELLOW, weight=BOLD),
            Text("|", font_size=26, color=GREY),
            Text("Лист", font_size=26, color=YELLOW, weight=BOLD),
        )
        header[0].move_to(LEFT * 2.0 + UP * 1.0)
        header[1].move_to(LEFT * 0.5 + UP * 1.0)
        header[2].move_to(RIGHT * 1.5 + UP * 1.0)
        self.play(Write(header), run_time=0.8)

        row_mobs = VGroup()
        for i, (s, l) in enumerate(zip(stems, leaves)):
            y = 0.3 - i * 0.6
            s_t = Text(s, font_size=28, color=BLUE, weight=BOLD).move_to(LEFT * 2.0 + UP * y)
            bar = Text("|", font_size=28, color=GREY).move_to(LEFT * 0.5 + UP * y)
            l_t = Text(l, font_size=28, color=GREEN).move_to(RIGHT * 1.5 + UP * y)
            row_mobs.add(s_t, bar, l_t)

        for i in range(0, len(row_mobs), 3):
            self.play(Write(row_mobs[i]), Write(row_mobs[i+1]), Write(row_mobs[i+2]),
                      run_time=0.6)

        note = Text("Пример: 14 | 5 значи 145.",
                    font_size=24, color=YELLOW)
        note.move_to(DOWN * 2.3)
        self.play(Write(note), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ПРИМЕР: 10 ВИСИНИ                               ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title7 = section_title("Десет висини (cm)")
        self.play(Write(title7), run_time=1.0)

        data = "145, 148, 149, 150, 152, 155, 155, 157, 161, 168"
        d = Text(data, font_size=26, color=WHITE2)
        d.move_to(UP * 1.7)
        self.play(Write(d), run_time=1.2)

        results = VGroup(
            MathTex(r"\text{Средина} = \frac{1570}{10} = 157",
                    font_size=34, color=BLUE),
            MathTex(r"\text{Медијана} = \frac{152 + 155}{2}",
                    font_size=34, color=GREEN),
            MathTex(r"= 153{,}5",
                    font_size=34, color=GREEN),
            MathTex(r"\text{Мода} = 155 \;\;\text{(се повторува)}",
                    font_size=32, color=ORANGE),
            MathTex(r"\text{Ранг} = 168 - 145 = 23",
                    font_size=32, color=PURPLE),
        )
        results[0].move_to(UP * 0.7)
        results[1].move_to(DOWN * 0.0)
        results[2].next_to(results[1], DOWN, buff=0.05)
        results[3].move_to(DOWN * 1.0)
        results[4].move_to(DOWN * 1.9)

        for r in results:
            self.play(Write(r), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  CLOSING                                         ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        close = Text("Бројки откако ќе ги подредиш — почнуваат да зборуваат.",
                     font_size=32, color=YELLOW, weight=BOLD)
        close.move_to(ORIGIN)
        self.play(Write(close), run_time=1.8)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
