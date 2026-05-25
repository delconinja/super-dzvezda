"""
geo8-3-3  —  Пиринејски Полуостров (Шпанија и Португалија)
Географија 8, Единица 3: Јужна Европа

Teaching narrative — Andonovski-style: three-beat punches,
neighbours as characters, peninsulas as branches of land.
Render:  manim -ql geo8-3-3.py Geo833Scene
Output:  media/videos/geo8-3-3/480p15/Geo833Scene.mp4
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


class Geo833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — "Шпанија и Португалија"                ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Шпанија и Португалија.", font_size=54, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Соседи.", font_size=40, color=WHITE2),
            Text("Раздвоени со граница.", font_size=34, color=GREY),
            Text("Споени со историја.", font_size=34, color=ORANGE),
            Text("Откривале нови светови.", font_size=34, color=BLUE),
            Text("Кога Европа уште не знаела за нив.", font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  THE PENINSULA — quadrilateral shape             ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("peninsula")

        t2 = section_title("Пиринејски Полуостров")
        self.play(Write(t2), run_time=0.8)

        # Rough quadrilateral
        iberia = Polygon(
            [-3.0,  1.8, 0],
            [ 2.5,  2.0, 0],
            [ 2.8,  0.8, 0],
            [ 2.4, -0.5, 0],
            [ 1.6, -1.5, 0],
            [-0.5, -2.0, 0],
            [-2.5, -1.5, 0],
            [-3.2,  0.0, 0],
            fill_color="#a87850", fill_opacity=0.6,
            stroke_color=ORANGE, stroke_width=3,
        )

        # Portugal — western strip
        portugal = Polygon(
            [-3.2,  1.8, 0],
            [-2.0,  1.9, 0],
            [-1.8,  0.5, 0],
            [-2.0, -1.2, 0],
            [-2.5, -1.5, 0],
            [-3.2,  0.0, 0],
            fill_color="#5a8a4a", fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=3,
        )

        self.play(FadeIn(iberia), run_time=1.0)
        self.play(FadeIn(portugal), run_time=0.8)

        sp_lab = Text("Шпанија", font_size=26, color=RED, weight=BOLD).move_to([0.5, 0.5, 0])
        pt_lab = Text("Португалија", font_size=20, color=GREEN, weight=BOLD).move_to([-2.5, 0.3, 0])
        and_lab = Text("Андора", font_size=14, color=PURPLE)
        and_lab.move_to([1.5, 1.7, 0])
        gib_lab = Text("Гибралтар", font_size=14, color=YELLOW)
        gib_lab.move_to([-0.5, -2.3, 0])

        self.play(Write(sp_lab), Write(pt_lab), run_time=0.6)
        self.play(Write(and_lab), Write(gib_lab), run_time=0.5)

        # Pyrenees mountain barrier — top
        pyr = VMobject(color=GREY, stroke_width=5)
        pyr.set_points_as_corners([
            [-1.0, 2.4, 0], [-0.5, 2.7, 0], [0.0, 2.4, 0],
            [0.5, 2.8, 0], [1.0, 2.4, 0], [1.5, 2.7, 0], [2.0, 2.3, 0]
        ])
        pyr_lab = Text("Пиринеи", font_size=20, color=GREY, weight=BOLD)
        pyr_lab.next_to(pyr, UP, buff=0.1)
        self.play(Create(pyr), Write(pyr_lab), run_time=1.0)

        # Seas
        atl = Text("Атлантски\nокеан", font_size=18, color=BLUE, weight=BOLD)
        atl.move_to([-5.0, 0.5, 0])
        med = Text("Средоземно\nморе", font_size=18, color=BLUE, weight=BOLD)
        med.move_to([4.5, 0.0, 0])
        gib_str = Text("Гибралтарски\nтеснец", font_size=14, color=BLUE)
        gib_str.move_to([-3.0, -2.5, 0])

        self.play(FadeIn(atl), FadeIn(med), FadeIn(gib_str), run_time=0.7)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t2, iberia, portugal, sp_lab, pt_lab, and_lab,
                                  gib_lab, pyr, pyr_lab, atl, med, gib_str)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  PYRENEES BARRIER                                ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pyrenees")

        t3 = section_title("Пиринеите — ѕид кон Европа")
        self.play(Write(t3), run_time=0.8)

        # Wall of mountains
        wall = VGroup()
        for i, x in enumerate(np.linspace(-5, 5, 11)):
            h = 2.0 + 0.4 * np.sin(i * 1.3)
            tri = Polygon(
                [x-0.6, -1.0, 0], [x, h-1.0, 0], [x+0.6, -1.0, 0],
                fill_color="#5a6470", fill_opacity=0.9,
                stroke_color=GREY, stroke_width=2,
            )
            wall.add(tri)
        self.play(LaggedStartMap(FadeIn, wall, shift=UP*0.2, lag_ratio=0.08), run_time=2.0)

        # France above
        fr_lab = Text("Франција (Европа)", font_size=22, color=BLUE, weight=BOLD)
        fr_lab.move_to([0, 2.5, 0])
        ar1 = Arrow([0, 2.2, 0], [0, 1.5, 0], color=BLUE, buff=0.05, stroke_width=3)
        self.play(Write(fr_lab), GrowArrow(ar1), run_time=0.7)

        # Iberian peninsula below
        ib_lab = Text("Пиринејски Полуостров", font_size=22, color=ORANGE, weight=BOLD)
        ib_lab.move_to([0, -1.8, 0])
        ar2 = Arrow([0, -1.4, 0], [0, -0.7, 0], color=ORANGE, buff=0.05, stroke_width=3)
        self.play(Write(ib_lab), GrowArrow(ar2), run_time=0.7)

        # Side note
        note = VGroup(
            Text("430 km во должина.", font_size=20, color=WHITE2),
            Text("3000 m висина.", font_size=20, color=WHITE2),
            Text("Природна граница.", font_size=22, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.3)

        for n in note:
            self.play(FadeIn(n, shift=UP*0.15), run_time=0.5)
            self.wait(0.15)

        self.wait(1.0)
        self.play(FadeOut(VGroup(t3, wall, fr_lab, ar1, ib_lab, ar2, note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  TWO COASTS                                      ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("coasts")

        t4 = section_title("Две мориња. Две лица.")
        self.play(Write(t4), run_time=0.8)

        # Left: Atlantic coast
        atl_box = RoundedRectangle(
            width=5.5, height=4.2, corner_radius=0.2,
            fill_color="#0a2a4a", fill_opacity=0.6,
            stroke_color=BLUE, stroke_width=2,
        ).move_to([-3.2, -0.3, 0])
        atl_h = Text("Атлантик", font_size=28, color=BLUE, weight=BOLD)
        atl_h.move_to(atl_box.get_top()+DOWN*0.35)
        atl_l = VGroup(
            Text("• Силни бранови", font_size=18, color=WHITE2),
            Text("• Дожд и магла", font_size=18, color=WHITE2),
            Text("• Сурфање", font_size=18, color=WHITE2),
            Text("• Бакалар, сардина", font_size=18, color=WHITE2),
            Text("• Лисабон, Порто", font_size=18, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        atl_l.next_to(atl_h, DOWN, buff=0.3).align_to(atl_h, LEFT).shift(LEFT*0.5)

        self.play(FadeIn(atl_box), Write(atl_h), run_time=0.6)
        for L in atl_l:
            self.play(FadeIn(L, shift=RIGHT*0.15), run_time=0.3)

        # Right: Mediterranean coast
        med_box = RoundedRectangle(
            width=5.5, height=4.2, corner_radius=0.2,
            fill_color="#0a3a2a", fill_opacity=0.6,
            stroke_color=GREEN, stroke_width=2,
        ).move_to([3.2, -0.3, 0])
        med_h = Text("Средоземје", font_size=28, color=GREEN, weight=BOLD)
        med_h.move_to(med_box.get_top()+DOWN*0.35)
        med_l = VGroup(
            Text("• Мирно и топло", font_size=18, color=WHITE2),
            Text("• Сонце и плажи", font_size=18, color=WHITE2),
            Text("• Туризам", font_size=18, color=WHITE2),
            Text("• Маслинки, портокали", font_size=18, color=WHITE2),
            Text("• Барселона, Валенсија", font_size=18, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        med_l.next_to(med_h, DOWN, buff=0.3).align_to(med_h, LEFT).shift(LEFT*0.5)

        self.play(FadeIn(med_box), Write(med_h), run_time=0.6)
        for L in med_l:
            self.play(FadeIn(L, shift=RIGHT*0.15), run_time=0.3)

        self.wait(1.0)
        self.play(FadeOut(VGroup(t4, atl_box, atl_h, atl_l, med_box, med_h, med_l)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  AGRICULTURE                                     ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("agriculture")

        t5 = section_title("Што раѓа Иберија?")
        self.play(Write(t5), run_time=0.8)

        # 4 products
        prods = [
            ("Маслинки",     "Шпанија — #1 во светот",          GREEN,  [-4.5, 1.0, 0]),
            ("Портокали",    "Валенсија ги полни Европа",       ORANGE, [-1.5, 1.0, 0]),
            ("Вино",         "Риоха • Порто • Дору",            PURPLE, [ 1.5, 1.0, 0]),
            ("Пробиотик",    "Пршут • Серано • Хамон",          RED,    [ 4.5, 1.0, 0]),
        ]
        cards = VGroup()
        for nm, det, col, pos in prods:
            box = RoundedRectangle(
                width=2.8, height=2.4, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            h = Text(nm, font_size=22, color=col, weight=BOLD).move_to(box.get_top()+DOWN*0.35)
            d = Text(det, font_size=13, color=WHITE2).move_to(box.get_center()+DOWN*0.2)
            cards.add(VGroup(box, h, d))

        for c in cards:
            self.play(FadeIn(c, scale=0.9), run_time=0.5)

        self.wait(0.6)

        msg = callout("Сонцето и морето даваат богатство.", width=8.5, border=YELLOW)
        msg.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg, shift=UP*0.2), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, cards, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CONQUISTADORES                                  ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conquistadores")

        t6 = section_title("Освојувачи на нови светови")
        self.play(Write(t6), run_time=0.8)

        # Ship sailing line
        ib = Dot([-4.5, 0.5, 0], radius=0.15, color=ORANGE)
        ib_l = Text("Иберија\n1492", font_size=18, color=ORANGE, weight=BOLD)
        ib_l.next_to(ib, UP, buff=0.2)

        am = Dot([4.5, -0.5, 0], radius=0.15, color=YELLOW)
        am_l = Text("Америка", font_size=18, color=YELLOW, weight=BOLD)
        am_l.next_to(am, DOWN, buff=0.2)

        self.play(FadeIn(ib), Write(ib_l), run_time=0.6)
        self.play(FadeIn(am), Write(am_l), run_time=0.6)

        path = ArcBetweenPoints(ib.get_center(), am.get_center(),
                                angle=-PI/3, color=BLUE, stroke_width=3)
        self.play(Create(path), run_time=2.0)

        # ship
        ship = Triangle(color=WHITE2, fill_color=WHITE2, fill_opacity=1).scale(0.2)
        ship.move_to(ib.get_center())
        self.play(MoveAlongPath(ship, path), run_time=2.5)

        facts = VGroup(
            Text("Колумбо. Магелан. Васко да Гама.", font_size=22, color=WHITE2),
            Text("Шпански и португалски говорат денес 600 милиони.", font_size=20, color=GREEN),
            Text("Двете империи. Едно море.", font_size=22, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.3)

        for f in facts:
            self.play(FadeIn(f, shift=UP*0.15), run_time=0.55)
            self.wait(0.15)

        self.wait(1.0)
        self.play(FadeOut(VGroup(t6, ib, ib_l, am, am_l, path, ship, facts)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        end1 = Text("Иберија.", font_size=64, color=YELLOW, weight=BOLD)
        end1.move_to(UP * 1.6)
        self.play(Write(end1), run_time=1.0)

        end_lines = VGroup(
            Text("Две земји. Едно сонце.", font_size=32, color=WHITE2),
            Text("Освоиле далечини.", font_size=32, color=ORANGE),
            Text("Сега ги привлекуваат.", font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(end1, DOWN, buff=0.5)

        for L in end_lines:
            self.play(FadeIn(L, shift=UP*0.15), run_time=0.7)
            self.wait(0.2)

        self.wait(2.0)
