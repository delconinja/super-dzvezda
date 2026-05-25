"""
bio8-3-7  —  Физичко и хемиско варење
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
teeth as crushers, enzymes as scissors, physics and chemistry
working together.
Render:  manim -ql bio8-3-7.py Bio837Scene
Output:  media/videos/bio8-3-7/480p15/Bio837Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE    = "#4fc3f7"
YELLOW  = "#ffd54f"
GREEN   = "#81c784"
RED     = "#e57373"
GREY    = "#90a4ae"
ORANGE  = "#ffb74d"
PURPLE  = "#ce93d8"
WHITE2  = "#e8eaf0"
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


def molecule_chain(n, color, scale=0.4):
    chain = VGroup()
    for i in range(n):
        c = Circle(radius=scale * 0.5, color=color,
                   fill_opacity=0.8, stroke_width=2)
        chain.add(c)
    chain.arrange(RIGHT, buff=0.05)
    return chain


class Bio837Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Забите кршат.",
                 font_size=42, color=BLUE, weight=BOLD),
            Text("Желудникот мие.",
                 font_size=42, color=RED, weight=BOLD),
            Text("Ензимите сечкаат.",
                 font_size=42, color=GREEN, weight=BOLD),
            Text("Физика и хемија работат заедно.",
                 font_size=34, color=ORANGE),
            Text("Без нив — не би имало хранење.",
                 font_size=36, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).to_edge(UP, buff=0.8)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.9)
            self.wait(0.2)
        self.wait(0.9)
        self.play(FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ДВЕ ВИДОВИ ВАРЕЊЕ                                ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("two_types")

        t2 = section_title("Две вида варење")
        self.play(Write(t2), run_time=0.7)

        # left box: physical
        left_box = RoundedRectangle(
            width=5.5, height=3.8, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2.5,
        ).shift(LEFT * 3.2 + DOWN * 0.3)
        left_title = Text("Физичко", font_size=32, color=BLUE, weight=BOLD)
        left_title.move_to(left_box.get_top() + DOWN * 0.5)
        left_def = Text("Менува облик.\nНе менува состав.",
                        font_size=22, color=WHITE2)
        left_def.next_to(left_title, DOWN, buff=0.4)

        right_box = RoundedRectangle(
            width=5.5, height=3.8, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2.5,
        ).shift(RIGHT * 3.2 + DOWN * 0.3)
        right_title = Text("Хемиско", font_size=32, color=GREEN, weight=BOLD)
        right_title.move_to(right_box.get_top() + DOWN * 0.5)
        right_def = Text("Менува состав.\nГолеми → мали молекули.",
                         font_size=22, color=WHITE2)
        right_def.next_to(right_title, DOWN, buff=0.4)

        self.play(Create(left_box), FadeIn(left_title), run_time=0.8)
        self.play(FadeIn(left_def, shift=UP * 0.2), run_time=0.7)
        self.wait(0.3)
        self.play(Create(right_box), FadeIn(right_title), run_time=0.8)
        self.play(FadeIn(right_def, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)

        # examples
        left_ex = Text("• Џвакање\n• Меткање\n• Сегментација",
                       font_size=22, color=BLUE)
        left_ex.next_to(left_def, DOWN, buff=0.3)

        right_ex = Text("• Амилаза\n• Пепсин\n• Липаза",
                        font_size=22, color=GREEN)
        right_ex.next_to(right_def, DOWN, buff=0.3)

        self.play(FadeIn(left_ex, shift=UP * 0.15),
                  FadeIn(right_ex, shift=UP * 0.15),
                  run_time=0.8)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t2, left_box, left_title, left_def, left_ex,
                                 right_box, right_title, right_def, right_ex)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  ФИЗИЧКО — ЏВАКАЊЕ                                ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("physical_chewing")

        t3 = section_title("Физичко варење", color=BLUE)
        self.play(Write(t3), run_time=0.7)

        big_food = RoundedRectangle(
            width=2.0, height=1.2, corner_radius=0.2,
            fill_color=ORANGE, fill_opacity=0.85, stroke_color=YELLOW,
            stroke_width=2,
        ).shift(LEFT * 4 + DOWN * 0.5)
        big_lbl = Text("залак", font_size=22, color=WHITE2).move_to(big_food)
        big = VGroup(big_food, big_lbl)

        arrow1 = Arrow(LEFT * 2.5, LEFT * 0.5, color=WHITE2, buff=0.15)
        arrow1.shift(DOWN * 0.5)

        pieces = VGroup()
        for i in range(6):
            p = RoundedRectangle(
                width=0.5, height=0.5, corner_radius=0.1,
                fill_color=ORANGE, fill_opacity=0.85,
                stroke_color=YELLOW, stroke_width=1.5,
            )
            pieces.add(p)
        pieces.arrange_in_grid(rows=2, cols=3, buff=0.15)
        pieces.shift(RIGHT * 1.5 + DOWN * 0.5)

        arrow2 = Arrow(RIGHT * 3, RIGHT * 4.5, color=WHITE2, buff=0.15)
        arrow2.shift(DOWN * 0.5)

        tiny = VGroup(*[
            Dot(radius=0.1, color=ORANGE)
            for _ in range(12)
        ])
        tiny.arrange_in_grid(rows=3, cols=4, buff=0.12)
        tiny.shift(RIGHT * 5.3 + DOWN * 0.5)

        self.play(FadeIn(big), run_time=0.6)
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(FadeIn(pieces, shift=LEFT * 0.2), run_time=0.7)
        self.play(GrowArrow(arrow2), run_time=0.4)
        self.play(FadeIn(tiny, shift=LEFT * 0.2), run_time=0.7)

        labels = VGroup(
            Text("залак", font_size=18, color=WHITE2),
            Text("парчиња", font_size=18, color=WHITE2),
            Text("ситни делови", font_size=18, color=WHITE2),
        )
        labels[0].next_to(big, DOWN, buff=0.3)
        labels[1].next_to(pieces, DOWN, buff=0.3)
        labels[2].next_to(tiny, DOWN, buff=0.3)
        self.play(FadeIn(labels), run_time=0.6)
        self.wait(0.5)

        explain = callout(
            "Целта: поголема површина за ензимите.",
            width=10.5, font_size=26, border=BLUE,
        )
        explain.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t3, big, arrow1, pieces, arrow2, tiny,
                                 labels, explain)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ХЕМИСКО — ЕНЗИМИ ГИ СЕЧАТ                       ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chemical_enzymes")

        t4 = section_title("Хемиско варење", color=GREEN)
        self.play(Write(t4), run_time=0.7)

        intro4 = Text("Ензимите сечат големи молекули на мали.",
                      font_size=26, color=WHITE2)
        intro4.next_to(t4, DOWN, buff=0.3)
        self.play(FadeIn(intro4), run_time=0.7)
        self.wait(0.3)

        # long chain → cut into pieces
        chain = molecule_chain(8, GREEN, scale=0.6)
        chain.shift(UP * 0.3)
        self.play(Create(chain), run_time=1.0)

        # enzyme = small scissor circle
        enzyme = VGroup(
            Circle(radius=0.3, color=YELLOW, fill_opacity=0.85, stroke_width=2),
            Text("Е", font_size=22, color=DARK_CARD, weight=BOLD),
        )
        enzyme.move_to(chain.get_center() + DOWN * 1.0)
        enzyme_lbl = Text("ензим", font_size=20, color=YELLOW)
        enzyme_lbl.next_to(enzyme, DOWN, buff=0.2)

        self.play(FadeIn(enzyme, shift=UP * 0.3), FadeIn(enzyme_lbl), run_time=0.7)

        # show cutting motion
        for i in [2, 4, 6]:
            cut_x = chain[i].get_left()[0]
            cut_line = Line(
                [cut_x, chain.get_top()[1] + 0.2, 0],
                [cut_x, chain.get_bottom()[1] - 0.2, 0],
                color=RED, stroke_width=3,
            )
            self.play(Create(cut_line), run_time=0.3)
            self.play(FadeOut(cut_line), run_time=0.2)

        # split chain visually
        new_pieces = VGroup()
        for i in range(0, 8, 2):
            pair = VGroup(chain[i].copy(), chain[i + 1].copy())
            new_pieces.add(pair)

        target = VGroup()
        for i in range(4):
            p = VGroup(
                Circle(radius=0.3, color=GREEN, fill_opacity=0.8, stroke_width=2),
                Circle(radius=0.3, color=GREEN, fill_opacity=0.8, stroke_width=2),
            ).arrange(RIGHT, buff=0.05)
            target.add(p)
        target.arrange(RIGHT, buff=0.45)
        target.move_to(chain.get_center())

        self.play(Transform(chain, target), run_time=1.0)
        self.wait(0.6)

        result_lbl = callout(
            "Големи → мали → апсорпција.",
            width=9.5, font_size=26, border=GREEN,
        )
        result_lbl.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(result_lbl, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t4, intro4, chain, enzyme,
                                 enzyme_lbl, result_lbl)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  ТАБЕЛА НА ЕНЗИМИ                                 ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("enzyme_table")

        t5 = section_title("Главни ензими", color=YELLOW)
        self.play(Write(t5), run_time=0.7)

        # build a simple table
        headers = VGroup(
            Text("Ензим", font_size=24, color=YELLOW, weight=BOLD),
            Text("Каде", font_size=24, color=YELLOW, weight=BOLD),
            Text("Што разградува", font_size=24, color=YELLOW, weight=BOLD),
        )
        headers.arrange(RIGHT, buff=1.6).next_to(t5, DOWN, buff=0.5)

        rows_data = [
            ("Амилаза",   "уста",          "скроб → шеќер",  BLUE),
            ("Пепсин",    "желудник",      "белковини",      RED),
            ("Липаза",    "тенко црево",   "масти",          ORANGE),
            ("Трипсин",   "тенко црево",   "белковини",      PURPLE),
        ]

        row_groups = VGroup()
        for name, place, target, color in rows_data:
            r = VGroup(
                Text(name, font_size=22, color=color, weight=BOLD),
                Text(place, font_size=22, color=WHITE2),
                Text(target, font_size=22, color=GREEN),
            )
            r.arrange(RIGHT, buff=0.6)
            # align widths
            r[0].move_to([headers[0].get_x(), 0, 0])
            r[1].move_to([headers[1].get_x(), 0, 0])
            r[2].move_to([headers[2].get_x(), 0, 0])
            row_groups.add(r)

        row_groups.arrange(DOWN, buff=0.4)
        row_groups.next_to(headers, DOWN, buff=0.5)
        # re-align x positions
        for r in row_groups:
            r[0].move_to([headers[0].get_x(), r[0].get_y(), 0])
            r[1].move_to([headers[1].get_x(), r[1].get_y(), 0])
            r[2].move_to([headers[2].get_x(), r[2].get_y(), 0])

        self.play(FadeIn(headers, shift=UP * 0.2), run_time=0.7)
        self.wait(0.3)
        for r in row_groups:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(VGroup(t5, headers, row_groups)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ЖОЛЧКА — ЕМУЛЗИЈА                                ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("bile")

        t6 = section_title("Жолчка и масти", color=ORANGE)
        self.play(Write(t6), run_time=0.7)

        intro6 = Text("Жолчката не е ензим. Туку помошник.",
                      font_size=28, color=WHITE2)
        intro6.next_to(t6, DOWN, buff=0.35)
        self.play(FadeIn(intro6), run_time=0.7)
        self.wait(0.3)

        # big fat blob → small droplets
        big_fat = Circle(radius=0.9, color=YELLOW,
                         fill_opacity=0.7, stroke_width=2)
        big_fat.shift(LEFT * 3 + DOWN * 0.3)
        big_lbl = Text("маст", font_size=22, color=WHITE2)
        big_lbl.move_to(big_fat)

        arr = Arrow(LEFT * 1.5, RIGHT * 1.5, color=ORANGE, buff=0.15)
        arr.shift(DOWN * 0.3)
        arr_lbl = Text("жолчка", font_size=22, color=ORANGE)
        arr_lbl.next_to(arr, UP, buff=0.2)

        drops = VGroup(*[
            Circle(radius=0.18, color=YELLOW,
                   fill_opacity=0.7, stroke_width=1.5)
            for _ in range(10)
        ])
        drops.arrange_in_grid(rows=3, cols=4, buff=0.1)
        drops.shift(RIGHT * 3 + DOWN * 0.3)

        self.play(FadeIn(big_fat), FadeIn(big_lbl), run_time=0.6)
        self.play(GrowArrow(arr), FadeIn(arr_lbl), run_time=0.6)
        self.play(FadeIn(drops, shift=LEFT * 0.2), run_time=0.7)
        self.wait(0.4)

        explain6 = callout(
            "Емулзија — голема површина за липаза.",
            width=10.5, font_size=26, border=ORANGE,
        )
        explain6.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(explain6, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t6, intro6, big_fat, big_lbl, arr,
                                 arr_lbl, drops, explain6)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conclusion")

        t7 = section_title("Заклучок", color=GREEN)
        self.play(Write(t7), run_time=0.7)

        final = VGroup(
            Text("Физичко — кршење.",
                 font_size=34, color=BLUE, weight=BOLD),
            Text("Хемиско — сечење.",
                 font_size=34, color=GREEN, weight=BOLD),
            Text("Двајцата — еден тим.",
                 font_size=34, color=ORANGE),
            Text("Заедно.",
                 font_size=44, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(t7, DOWN, buff=0.7)

        for line in final:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.85)
            self.wait(0.25)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t7, final)), run_time=0.8)
        self.wait(0.4)
