"""
chem8-2-2  —  Споредување материјали
Хемија 8, Единица 2: Материјали околу нас

Teaching narrative — Andonovski-style: three-beat punches,
materials as characters with roles, не...туку contrast, one-word finishers.
Render:  manim -ql chem8-2-2.py Chem822Scene
Output:  media/videos/chem8-2-2/480p15/Chem822Scene.mp4
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


class Chem822Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Тенџерето е метал.",
                  font_size=46, color=GREY, weight=BOLD)
        h2 = Text("Дршката е пластика.",
                  font_size=46, color=PURPLE, weight=BOLD)
        h1.move_to(UP * 1.8)
        h2.next_to(h1, DOWN, buff=0.35)

        self.play(Write(h1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.5)

        line2 = Text("Не случајност.", font_size=40, color=WHITE2, weight=BOLD)
        line2.next_to(h2, DOWN, buff=0.55)
        self.play(Write(line2), run_time=1.0)
        self.wait(0.4)

        line3 = Text("Топлината знае каде смее да оди.",
                     font_size=34, color=YELLOW)
        line3.next_to(line2, DOWN, buff=0.35)
        self.play(Write(line3), run_time=1.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(h1, h2, line2, line3)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА — зошто споредуваме                   ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Зошто споредуваме материјали?")
        self.play(Write(t2), run_time=1.0)

        d1 = callout(
            "За да изберам најсоодветен — за конкретна намена.",
            width=12.0, font_size=28,
        )
        d1.next_to(t2, DOWN, buff=0.7)
        self.play(FadeIn(d1), run_time=0.8)
        self.wait(0.6)

        d2 = Text("Не еден победник. Туку — прав човек на право место.",
                  font_size=30, color=WHITE2)
        d2.next_to(d1, DOWN, buff=0.55)
        self.play(Write(d2), run_time=1.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t2, d1, d2)))

        # ══════════════════════════════════════════════════════════
        # 3.  ТЕНЏЕРА — дијаграм                               ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pan_diagram")

        t3 = section_title("Топлинска спроводливост.")
        self.play(Write(t3), run_time=0.9)

        # Pan body — arc / U-shape
        pan_body_left = Line(LEFT*2.3 + UP*0.4, LEFT*2.3 + DOWN*1.2,
                             color=GREY, stroke_width=10)
        pan_body_bottom = Line(LEFT*2.3 + DOWN*1.2, RIGHT*2.3 + DOWN*1.2,
                               color=GREY, stroke_width=10)
        pan_body_right = Line(RIGHT*2.3 + UP*0.4, RIGHT*2.3 + DOWN*1.2,
                              color=GREY, stroke_width=10)
        pan_body = VGroup(pan_body_left, pan_body_bottom, pan_body_right)
        pan_body.shift(LEFT*1.5)

        # Handle - plastic
        handle = RoundedRectangle(
            width=3.0, height=0.5, corner_radius=0.15,
            fill_color=PURPLE, fill_opacity=1,
            stroke_color=WHITE2, stroke_width=2,
        )
        handle.next_to(pan_body, RIGHT, buff=-0.1).shift(UP*0.1)

        # Flame underneath
        flames = VGroup()
        for i, x in enumerate([-2.5, -1.8, -1.0, -0.2, 0.6]):
            f = Polygon(
                [x, -2.0, 0],
                [x - 0.2, -1.4, 0],
                [x + 0.0, -1.0, 0],
                [x + 0.2, -1.4, 0],
                fill_color=ORANGE, fill_opacity=1,
                stroke_color=YELLOW, stroke_width=2,
            )
            flames.add(f)
        flames.shift(LEFT*1.5)

        self.play(Create(pan_body), run_time=1.0)
        self.play(FadeIn(handle), run_time=0.6)
        self.play(FadeIn(flames), run_time=0.6)
        self.wait(0.4)

        # Heat arrows going through metal body
        heat_arrows = VGroup()
        for i in range(4):
            ar = Arrow(
                start=[-2.5 + i*0.5 - 1.5, -0.9, 0],
                end=[-2.5 + i*0.5 - 1.5, 0.3, 0],
                color=RED, buff=0.05, stroke_width=4,
            )
            heat_arrows.add(ar)
        self.play(*[GrowArrow(a) for a in heat_arrows], run_time=1.2)
        self.wait(0.4)

        # Block sign on handle — heat blocked
        block = Text("STOP", font_size=24, color=RED, weight=BOLD)
        block.move_to(handle.get_center() + UP*0.8)
        block_box = SurroundingRectangle(block, color=RED, stroke_width=3,
                                         corner_radius=0.1, buff=0.1)
        self.play(FadeIn(block), Create(block_box), run_time=0.9)
        self.wait(0.4)

        # Labels
        lab_metal = Text("метал → води топлина",
                         font_size=26, color=GREY, weight=BOLD)
        lab_metal.move_to(LEFT*4.5 + UP*2.4)
        lab_plastic = Text("пластика → блокира",
                           font_size=26, color=PURPLE, weight=BOLD)
        lab_plastic.move_to(RIGHT*3.3 + UP*2.4)
        self.play(Write(lab_metal), run_time=0.9)
        self.play(Write(lab_plastic), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t3, pan_body, handle, flames,
                                  heat_arrows, block, block_box,
                                  lab_metal, lab_plastic)))

        # ══════════════════════════════════════════════════════════
        # 4.  КАБЕЛ — пресек                                   ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cable_section")

        t4 = section_title("Електрична спроводливост.")
        self.play(Write(t4), run_time=0.9)

        # Cable - rectangular cross-section view
        cable_outer = RoundedRectangle(
            width=6.5, height=1.6, corner_radius=0.4,
            fill_color=PURPLE, fill_opacity=0.85,
            stroke_color=WHITE2, stroke_width=2,
        ).move_to(DOWN*0.4)
        cable_copper = RoundedRectangle(
            width=6.5, height=0.6, corner_radius=0.2,
            fill_color="#c87533", fill_opacity=1,
            stroke_color=WHITE2, stroke_width=2,
        ).move_to(DOWN*0.4)

        self.play(FadeIn(cable_outer), run_time=0.6)
        self.play(FadeIn(cable_copper), run_time=0.6)
        self.wait(0.3)

        # Electrons flowing through copper
        electrons = VGroup()
        for i in range(7):
            e = Circle(radius=0.12, fill_color=YELLOW, fill_opacity=1,
                      stroke_color=WHITE2, stroke_width=1)
            e.move_to([-2.8 + i*0.95, -0.4, 0])
            electrons.add(e)
        self.play(FadeIn(electrons), run_time=0.6)
        self.play(electrons.animate.shift(RIGHT*0.9), run_time=1.2)
        self.play(electrons.animate.shift(RIGHT*0.9), run_time=1.2)

        # Labels
        lab_cu = Text("Cu — пуша електрони",
                      font_size=26, color=ORANGE, weight=BOLD)
        lab_cu.next_to(cable_copper, UP, buff=0.4)
        lab_cu.shift(UP*0.3)
        lab_ins = Text("пластика — ги држи внатре",
                       font_size=26, color=PURPLE, weight=BOLD)
        lab_ins.next_to(cable_outer, DOWN, buff=0.4)
        self.play(Write(lab_cu), run_time=0.9)
        self.play(Write(lab_ins), run_time=0.9)
        self.wait(1.4)

        verdict = Text("Двајца. Една жица. Безбедност.",
                       font_size=32, color=YELLOW, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.4)
        self.play(Write(verdict), run_time=1.3)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, cable_outer, cable_copper, electrons,
                                  lab_cu, lab_ins, verdict)))

        # ══════════════════════════════════════════════════════════
        # 5.  СПОРЕДНА ТАБЕЛА — материјал → намена              ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("match_table")

        t5 = section_title("Материјал → намена.")
        self.play(Write(t5), run_time=0.9)

        rows = [
            ("Челик",     "мостови, тенџери",   GREY),
            ("Алуминиум", "авиони, конзерви",   BLUE),
            ("Бакар",     "жици за струја",     ORANGE),
            ("Пластика",  "изолација, шишиња",  PURPLE),
            ("Стакло",    "прозорци, садови",   YELLOW),
            ("Дрво",      "мебел, рамки",       GREEN),
        ]
        y_start = 1.9
        all_rows = VGroup()
        for i, (mat, use, col) in enumerate(rows):
            y = y_start - i*0.7
            box = RoundedRectangle(
                width=11.5, height=0.6, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to([0, y, 0])
            m = Text(mat, font_size=24, color=col, weight=BOLD)
            m.move_to([-4.2, y, 0])
            arrow = Arrow(start=LEFT*0.6, end=RIGHT*0.6, color=WHITE2,
                          buff=0.05, stroke_width=3)
            arrow.move_to([-1.5, y, 0])
            u = Text(use, font_size=24, color=WHITE2)
            u.move_to([1.8, y, 0])
            row_g = VGroup(box, m, arrow, u)
            all_rows.add(row_g)

        for r in all_rows:
            self.play(FadeIn(r), run_time=0.35)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t5, all_rows)))

        # ══════════════════════════════════════════════════════════
        # 6.  СЕЛЕКЦИЈА — научна метода                        ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("method")

        t6 = section_title("Како бираме? Чекор по чекор.")
        self.play(Write(t6), run_time=0.9)

        steps = [
            ("1.", "Дефинирај намена и услови.", BLUE),
            ("2.", "Идентификувај клучни својства.", GREEN),
            ("3.", "Спореди материјали.", YELLOW),
            ("4.", "Одбери најдобар компромис.", ORANGE),
            ("5.", "Тестирај и прилагоди.", RED),
        ]
        y_start = 1.7
        step_grp = VGroup()
        for i, (n, t, c) in enumerate(steps):
            y = y_start - i*0.75
            num = Text(n, font_size=30, color=c, weight=BOLD)
            num.move_to([-5.0, y, 0])
            tt = Text(t, font_size=26, color=WHITE2)
            tt.move_to([-0.5, y, 0])
            step_grp.add(VGroup(num, tt))

        for s in step_grp:
            self.play(FadeIn(s), run_time=0.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t6, step_grp)))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни.")
        self.play(Write(t7), run_time=0.8)

        b1 = callout("Споредба = метод, не наслућивање.",
                     width=11.0, border=BLUE, font_size=28)
        b1.move_to(UP*1.4)
        b2 = callout("Секој материјал има своја улога.",
                     width=11.0, border=GREEN, font_size=28)
        b2.next_to(b1, DOWN, buff=0.35)
        b3 = callout("Тенџерето те храни. Дршката те чува.",
                     width=11.0, border=YELLOW, font_size=28)
        b3.next_to(b2, DOWN, buff=0.35)

        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.0)

        finisher = Text("Дизајн.", font_size=54, color=YELLOW, weight=BOLD)
        finisher.next_to(b3, DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, b1, b2, b3, finisher)))
        self.wait(0.5)
