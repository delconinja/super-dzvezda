"""
bio8-3-1  —  Составни делови на избалансирана исхрана
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
food as story, nutrients as characters with roles.
Render:  manim -ql bio8-3-1.py Bio831Scene
Output:  media/videos/bio8-3-1/480p15/Bio831Scene.mp4
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


class Bio831Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Не една храна.",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Не два.",                         font_size=42, color=ORANGE, weight=BOLD),
            Text("Седум групи.",                    font_size=46, color=GREEN, weight=BOLD),
            Text("Сите неопходни.",                 font_size=34, color=WHITE2),
            Text("Сите за тебе.",                   font_size=36, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — 7 food groups                      ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Седум групи")
        self.play(Write(title), run_time=0.8)

        groups = [
            ("Јаглехидрати",  "Енергија",       YELLOW),
            ("Белковини",     "Градиво",        RED),
            ("Масти",         "Залиха, топлина", ORANGE),
            ("Витамини",      "Мали, но клучни", GREEN),
            ("Минерали",      "Ca, Fe",         BLUE),
            ("Вода",          "Носител",        PURPLE),
            ("Влакна",        "Чистач",         GREY),
        ]

        rows = VGroup()
        for name, role, col in groups:
            box = RoundedRectangle(
                width=11.0, height=0.65, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=24, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 2.0)
            r = Text(role, font_size=22, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 6.5)
            rows.add(VGroup(box, n, r))
        rows.arrange(DOWN, buff=0.15).next_to(title, DOWN, buff=0.5)

        for row in rows:
            self.play(FadeIn(row, shift=LEFT * 0.3), run_time=0.45)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, rows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — food pyramid                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Пирамида на исхрана")
        self.play(Write(title), run_time=0.8)

        # Build a 4-tier pyramid (bottom = most, top = least)
        tiers = [
            ("Жита, леб, ориз",      4.8, YELLOW),
            ("Овошје, зеленчук",     3.6, GREEN),
            ("Млеко, месо, риба",    2.4, RED),
            ("Шеќер, масти",         1.2, ORANGE),
        ]

        pyramid = VGroup()
        base_y = -2.4
        for i, (label, w, col) in enumerate(tiers):
            h = 0.85
            trap = Polygon(
                np.array([-w/2, base_y + i*h, 0]),
                np.array([ w/2, base_y + i*h, 0]),
                np.array([ (w - 0.6)/2, base_y + (i+1)*h, 0]),
                np.array([-(w - 0.6)/2, base_y + (i+1)*h, 0]),
                fill_color=col, fill_opacity=0.7,
                stroke_color=WHITE2, stroke_width=2,
            )
            txt = Text(label, font_size=20, color=DARK_CARD, weight=BOLD)
            txt.move_to(trap.get_center())
            pyramid.add(VGroup(trap, txt))

        pyramid.shift(LEFT * 2.5)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in pyramid],
                              lag_ratio=0.3), run_time=2.0)

        # Side annotations
        more = Text("Повеќе", font_size=26, color=GREEN, weight=BOLD)
        less = Text("Помалку", font_size=26, color=ORANGE, weight=BOLD)
        arrow = Arrow(
            start=LEFT * 0.4 + DOWN * 2.0,
            end=LEFT * 0.4 + UP * 2.2,
            color=WHITE2, stroke_width=3,
        )
        more.next_to(arrow, DOWN, buff=0.1)
        less.next_to(arrow, UP, buff=0.1)

        side_note = callout("Долу — повеќе. Горе — поретко.",
                            width=5.4, border=YELLOW, font_size=22)
        side_note.move_to(RIGHT * 3.8 + UP * 1.5)

        self.play(GrowArrow(arrow), FadeIn(more), FadeIn(less), run_time=0.9)
        self.play(FadeIn(side_note, shift=LEFT * 0.3), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, pyramid, arrow, more, less, side_note)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — balanced plate                        ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Чинија во рамнотежа")
        self.play(Write(title), run_time=0.8)

        # Circle plate divided into 4 sectors
        plate = Circle(radius=2.4, color=WHITE2, stroke_width=3)
        plate.shift(LEFT * 3.0)

        sectors = []
        sector_data = [
            (0,    120, GREEN,  "Зеленчук\nовошје"),
            (120,  210, YELLOW, "Жита"),
            (210,  300, RED,    "Белковини"),
            (300,  360, BLUE,   "Млечни"),
        ]
        for start, end, col, label in sector_data:
            arc = AnnularSector(
                inner_radius=0, outer_radius=2.4,
                angle=(end - start) * DEGREES,
                start_angle=start * DEGREES,
                fill_color=col, fill_opacity=0.65,
                stroke_color=WHITE2, stroke_width=2,
            )
            arc.move_arc_center_to(plate.get_center())
            mid_ang = ((start + end) / 2) * DEGREES
            lbl = Text(label, font_size=18, color=DARK_CARD, weight=BOLD)
            lbl.move_to(plate.get_center() + 1.3 * np.array(
                [np.cos(mid_ang), np.sin(mid_ang), 0]))
            sectors.append(VGroup(arc, lbl))

        self.play(Create(plate), run_time=0.8)
        for s in sectors:
            self.play(FadeIn(s, shift=UP * 0.15), run_time=0.6)
        self.wait(0.5)

        # Side legend
        legend = VGroup(
            Text("½ чинија: овошје + зеленчук", font_size=22, color=GREEN),
            Text("¼ чинија: жита",               font_size=22, color=YELLOW),
            Text("¼ чинија: белковини",          font_size=22, color=RED),
            Text("Странично: млеко",             font_size=22, color=BLUE),
            Text("Вода — секогаш.",              font_size=24, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.move_to(RIGHT * 3.2 + UP * 0.2)

        for line in legend:
            self.play(FadeIn(line, shift=LEFT * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, plate, *sectors, legend)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — roles of each nutrient             ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("Секој со улога")
        self.play(Write(title), run_time=0.8)

        roles = [
            ("Јаглехидрати",  "Тие се горивото.",            YELLOW),
            ("Белковини",     "Тие се ѕидари.",              RED),
            ("Масти",         "Тие се скривница за зима.",   ORANGE),
            ("Витамини",      "Тие се мали чувари.",         GREEN),
            ("Минерали",      "Тие се коски и крв.",         BLUE),
            ("Вода",          "Таа е реката низ телото.",    PURPLE),
            ("Влакна",        "Тие се метлата на цревото.",  GREY),
        ]

        cards = VGroup()
        for name, role, col in roles:
            box = RoundedRectangle(
                width=11.5, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=22, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.8)
            r = Text(role, font_size=21, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 6.5)
            cards.add(VGroup(box, n, r))
        cards.arrange(DOWN, buff=0.12).next_to(title, DOWN, buff=0.4)

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Седум групи. Сите важни.",
                 font_size=32, color=YELLOW, weight=BOLD),
            Text("Пирамидата кажува колку.",
                 font_size=28, color=BLUE),
            Text("Чинијата кажува како.",
                 font_size=28, color=ORANGE),
            Text("Не една храна. Седум.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
