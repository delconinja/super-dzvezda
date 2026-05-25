"""
m8-5-3  —  Толкување и дискутирање за резултатите
Математика 8, Единица 5: Ракување со податоци

Andonovski-style: бројките зборуваат, луѓето лажат. Биди скептичен.
Render:  manim -ql m8-5-3.py M853Scene
Output:  media/videos/m8-5-3/480p15/M853Scene.mp4
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


class M853Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Бројките не лажат.", font_size=38, color=GREEN, weight=BOLD)
        h2 = Text("Но луѓето кои ги читаат — можат.", font_size=34, color=RED, weight=BOLD)
        h3 = Text("Биди скептичен. Биди внимателен. Биди буден.",
                  font_size=30, color=YELLOW, weight=BOLD)

        hooks = VGroup(h1, h2, h3).arrange(DOWN, buff=0.45)
        hooks.move_to(ORIGIN)
        for h in hooks:
            self.play(Write(h), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(hooks), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ЧЕКОРИ НА ЧИТАЊЕ                                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("reading_steps")

        title2 = section_title("Како се чита график?")
        self.play(Write(title2), run_time=1.0)

        steps = [
            ("1. Наслов", BLUE),
            ("2. Оски", GREEN),
            ("3. Единици", YELLOW),
            ("4. Тренд", ORANGE),
            ("5. Екстреми", PURPLE),
            ("6. Споредба", RED),
        ]

        step_grp = VGroup()
        for txt, col in steps:
            t = Text(txt, font_size=30, color=col, weight=BOLD)
            step_grp.add(t)
        step_grp.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        step_grp.move_to(LEFT * 2.0)

        for s in step_grp:
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.4)

        side = callout(
            "Прво гледај — потоа верувај.",
            width=5.2, bg="#0d2b44", border=YELLOW, font_size=24,
        )
        side.move_to(RIGHT * 3.0)
        self.play(FadeIn(side, shift=LEFT * 0.3), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  ПРИМЕР: УЧЕНИЦИ 2020–2023                       ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("students_example")

        title3 = section_title("Ученици по година")
        self.play(Write(title3), run_time=1.0)

        ax = Axes(
            x_range=[2019.5, 2023.5, 1], y_range=[0, 600, 100],
            x_length=8, y_length=4,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax.shift(DOWN * 0.5)

        # x labels
        years = [2020, 2021, 2022, 2023]
        vals = [400, 480, 460, 520]
        x_labels = VGroup()
        for y in years:
            t = Text(str(y), font_size=20, color=WHITE2)
            t.move_to(ax.c2p(y, 0) + DOWN * 0.3)
            x_labels.add(t)

        y_labels = VGroup()
        for yv in [100, 200, 300, 400, 500, 600]:
            t = Text(str(yv), font_size=18, color=WHITE2)
            t.move_to(ax.c2p(2019.5, yv) + LEFT * 0.3)
            y_labels.add(t)

        self.play(Create(ax), Write(x_labels), Write(y_labels), run_time=1.5)

        coords = [ax.c2p(yr, v) for yr, v in zip(years, vals)]
        line = VMobject(stroke_color=YELLOW, stroke_width=4)
        line.set_points_as_corners(coords)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in coords])

        self.play(Create(line), FadeIn(dots), run_time=1.5)

        # Annotations
        arr1 = Arrow(ax.c2p(2021, 600), ax.c2p(2021, 490), color=GREEN,
                     stroke_width=4, buff=0.05)
        lbl1 = Text("раст", font_size=22, color=GREEN, weight=BOLD)
        lbl1.next_to(arr1, UP, buff=0.1)

        arr2 = Arrow(ax.c2p(2022, 600), ax.c2p(2022, 470), color=RED,
                     stroke_width=4, buff=0.05)
        lbl2 = Text("пад", font_size=22, color=RED, weight=BOLD)
        lbl2.next_to(arr2, UP, buff=0.1)

        self.play(GrowArrow(arr1), Write(lbl1), run_time=0.8)
        self.play(GrowArrow(arr2), Write(lbl2), run_time=0.8)

        conclusion = Text("Тренд: благ раст со мал пад во 2022.",
                          font_size=24, color=WHITE2)
        conclusion.move_to(DOWN * 3.2)
        self.play(Write(conclusion), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  КОРЕЛАЦИЈА vs ПРИЧИНА                           ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("correlation")

        title4 = section_title("Корелација не е причина")
        self.play(Write(title4), run_time=1.0)

        # Two columns - ice cream and drowning
        ice = Text("Сладолед ↑", font_size=32, color=BLUE, weight=BOLD)
        drown = Text("Удавувања ↑", font_size=32, color=RED, weight=BOLD)
        ice.move_to(LEFT * 3.5 + UP * 1.5)
        drown.move_to(RIGHT * 3.5 + UP * 1.5)

        self.play(Write(ice), Write(drown), run_time=1.0)

        # Wrong arrow
        wrong = Arrow(ice.get_right(), drown.get_left(),
                      color=RED, stroke_width=4, buff=0.2)
        wrong_x = Text("X", font_size=48, color=RED, weight=BOLD)
        wrong_x.move_to(wrong.get_center())

        self.play(GrowArrow(wrong), run_time=0.8)
        self.play(Write(wrong_x), run_time=0.5)

        wrong_lbl = Text("Не — сладоледот не дави!", font_size=22, color=RED)
        wrong_lbl.next_to(wrong, DOWN, buff=0.2)
        self.play(Write(wrong_lbl), run_time=1.0)
        self.wait(1.0)

        # The hidden cause
        hot = callout("Скриена причина: топло време!",
                      width=7.0, bg="#3d1818", border=YELLOW, font_size=28)
        hot.move_to(DOWN * 0.8)
        self.play(FadeIn(hot, shift=UP * 0.3), run_time=0.8)

        arr_l = Arrow(hot.get_top() + UP * 0.05, ice.get_bottom() + DOWN * 0.1,
                      color=YELLOW, stroke_width=4, buff=0.1)
        arr_r = Arrow(hot.get_top() + UP * 0.05, drown.get_bottom() + DOWN * 0.1,
                      color=YELLOW, stroke_width=4, buff=0.1)
        self.play(GrowArrow(arr_l), GrowArrow(arr_r), run_time=1.0)
        self.wait(1.5)

        bot = Text("Истовремено не значи поради.", font_size=26, color=GREEN, weight=BOLD)
        bot.move_to(DOWN * 2.5)
        self.play(Write(bot), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  СПОРЕДБА: ИСТА СРЕДИНА, РАЗЛИЧЕН РАНГ           ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        title5 = section_title("Иста средина, различна приказна")
        self.play(Write(title5), run_time=1.0)

        # Class A - narrow distribution
        ax_a = Axes(
            x_range=[0, 10, 2], y_range=[0, 6, 2],
            x_length=4.5, y_length=2.6,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax_a.move_to(LEFT * 3.5 + UP * 0.5)

        a_heights = [0, 1, 3, 5, 4, 2, 1, 0, 0, 0]
        bars_a = VGroup()
        for i, h in enumerate(a_heights):
            if h > 0:
                b = Rectangle(
                    width=0.4, height=h * 0.42,
                    fill_color=BLUE, fill_opacity=0.7,
                    stroke_color=BLUE, stroke_width=1,
                )
                b.move_to(ax_a.c2p(i + 0.5, h / 2))
                bars_a.add(b)

        lbl_a = Text("Клас А — ранг 15", font_size=24, color=BLUE, weight=BOLD)
        lbl_a.next_to(ax_a, DOWN, buff=0.2)

        # Class B - wide
        ax_b = Axes(
            x_range=[0, 10, 2], y_range=[0, 6, 2],
            x_length=4.5, y_length=2.6,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax_b.move_to(RIGHT * 3.5 + UP * 0.5)

        b_heights = [2, 2, 1, 2, 2, 2, 2, 1, 2, 2]
        bars_b = VGroup()
        for i, h in enumerate(b_heights):
            if h > 0:
                b = Rectangle(
                    width=0.4, height=h * 0.42,
                    fill_color=ORANGE, fill_opacity=0.7,
                    stroke_color=ORANGE, stroke_width=1,
                )
                b.move_to(ax_b.c2p(i + 0.5, h / 2))
                bars_b.add(b)

        lbl_b = Text("Клас Б — ранг 45", font_size=24, color=ORANGE, weight=BOLD)
        lbl_b.next_to(ax_b, DOWN, buff=0.2)

        self.play(Create(ax_a), Create(ax_b), run_time=1.0)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars_a],
                  *[GrowFromEdge(b, DOWN) for b in bars_b], run_time=1.0)
        self.play(Write(lbl_a), Write(lbl_b), run_time=0.8)

        mid = MathTex(r"\bar{x}_A = \bar{x}_B = 65", font_size=36, color=GREEN)
        mid.move_to(DOWN * 2.3)
        self.play(Write(mid), run_time=1.0)
        self.wait(1.5)

        note = Text("Иста средина — но А е стабилен, Б е променлив.",
                    font_size=24, color=YELLOW)
        note.move_to(DOWN * 3.1)
        self.play(Write(note), run_time=1.5)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ПИТА — АГЛИ                                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pie_angles")

        title6 = section_title("Пита: процент во агол")
        self.play(Write(title6), run_time=1.0)

        formula = MathTex(r"\text{агол} = \frac{\%}{100} \times 360^\circ",
                          font_size=44, color=YELLOW)
        formula.move_to(UP * 1.7)
        self.play(Write(formula), run_time=1.2)

        examples = VGroup(
            MathTex(r"25\% \;\to\; 0{,}25 \times 360 = 90^\circ",
                    font_size=32, color=WHITE2),
            MathTex(r"50\% \;\to\; 0{,}50 \times 360 = 180^\circ",
                    font_size=32, color=WHITE2),
            MathTex(r"10\% \;\to\; 0{,}10 \times 360 = 36^\circ",
                    font_size=32, color=WHITE2),
        )
        examples.arrange(DOWN, buff=0.35)
        examples.move_to(DOWN * 0.6)

        for e in examples:
            self.play(Write(e), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАМКИ                                           ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pitfalls")

        title7 = section_title("Четири замки", color=RED)
        self.play(Write(title7), run_time=1.0)

        pits = [
            ("1.", "Премал примерок", "3 другари ≠ сите млади", BLUE),
            ("2.", "Селективен примерок", "само математичари за математика", GREEN),
            ("3.", "Наведувачко прашање", "\"Зар не мислиш…?\"", ORANGE),
            ("4.", "Манипулиран график", "сечени оски, скриени делови", RED),
        ]

        pit_grp = VGroup()
        for num, t, ex, col in pits:
            n = Text(num, font_size=28, color=col, weight=BOLD)
            tt = Text(t, font_size=26, color=col, weight=BOLD)
            ee = Text(ex, font_size=22, color=WHITE2)
            row = VGroup(n, tt, ee).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
            pit_grp.add(row)
        pit_grp.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        pit_grp.scale(0.95)
        pit_grp.move_to(ORIGIN)

        for p in pit_grp:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(pit_grp), run_time=0.5)

        # Misleading graph demo
        demo_title = Text("Замка #4: исечени оски", font_size=30, color=RED, weight=BOLD)
        demo_title.move_to(UP * 2.1)
        self.play(Write(demo_title), run_time=0.8)

        # Truncated
        ax_t = Axes(
            x_range=[0, 4, 1], y_range=[95, 105, 2],
            x_length=4, y_length=2.5,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax_t.move_to(LEFT * 3.5 + DOWN * 0.4)

        vals_t = [98, 99, 100, 102]
        bars_t = VGroup()
        for i, v in enumerate(vals_t):
            h = (v - 95) * 0.25
            b = Rectangle(width=0.5, height=h,
                          fill_color=RED, fill_opacity=0.7,
                          stroke_color=RED, stroke_width=2)
            b.move_to(ax_t.c2p(i + 0.5, 95 + (v - 95) / 2))
            bars_t.add(b)

        lbl_t = Text("Изгледа како голем раст!", font_size=20, color=RED)
        lbl_t.next_to(ax_t, DOWN, buff=0.2)

        # Honest
        ax_h = Axes(
            x_range=[0, 4, 1], y_range=[0, 110, 25],
            x_length=4, y_length=2.5,
            axis_config={"include_numbers": False, "stroke_color": GREY},
            tips=False,
        )
        ax_h.move_to(RIGHT * 3.5 + DOWN * 0.4)

        bars_h = VGroup()
        for i, v in enumerate(vals_t):
            h = v * 0.0227
            b = Rectangle(width=0.5, height=h,
                          fill_color=GREEN, fill_opacity=0.7,
                          stroke_color=GREEN, stroke_width=2)
            b.move_to(ax_h.c2p(i + 0.5, v / 2))
            bars_h.add(b)

        lbl_h = Text("Всушност — мала разлика.", font_size=20, color=GREEN)
        lbl_h.next_to(ax_h, DOWN, buff=0.2)

        self.play(Create(ax_t), Create(ax_h), run_time=1.0)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars_t],
                  *[GrowFromEdge(b, DOWN) for b in bars_h], run_time=1.0)
        self.play(Write(lbl_t), Write(lbl_h), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  ЗАКЛУЧОЦИ + CLOSING                             ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        title8 = section_title("Како се пишува заклучок?")
        self.play(Write(title8), run_time=1.0)

        rules = VGroup(
            Text("• Бројки и споредби", font_size=28, color=BLUE),
            Text("• Внимателен јазик: \"можеби\", \"потребни се повеќе податоци\"",
                 font_size=24, color=GREEN),
            Text("• Признај ги ограничувањата", font_size=28, color=ORANGE),
        )
        rules.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rules.move_to(ORIGIN)

        for r in rules:
            self.play(Write(r), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(title8), FadeOut(rules), run_time=0.5)

        close = Text("Бројот без контекст — е лага со маска.",
                     font_size=34, color=YELLOW, weight=BOLD)
        close.move_to(ORIGIN)
        self.play(Write(close), run_time=1.8)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
