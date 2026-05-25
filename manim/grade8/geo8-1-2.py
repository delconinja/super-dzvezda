"""
geo8-1-2  —  Релјеф на Европа
Географија 8, Единица 1: Природно-географски карактеристики на Европа

Teaching narrative — Andonovski-style: three-beat punches,
mountains as elders, plains as patience, peaks as ambition.
Render:  manim -ql geo8-1-2.py Geo812Scene
Output:  media/videos/geo8-1-2/480p15/Geo812Scene.mp4
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


def mountain_silhouette(width=4.0, height=1.8, color=GREY, jagged=True, seed=0):
    """Triangle / jagged mountain shape."""
    np.random.seed(seed)
    pts = [np.array([-width/2, 0, 0])]
    n = 12 if jagged else 3
    for i in range(1, n):
        x = -width/2 + (width * i / n)
        if jagged:
            y = height * (0.5 + 0.5 * np.sin(i * 0.9)) - 0.1 * np.random.random()
        else:
            y = height * (1 - abs(2*i/n - 1))
        pts.append(np.array([x, y, 0]))
    pts.append(np.array([width/2, 0, 0]))
    return Polygon(*pts, color=color, fill_color=color, fill_opacity=0.5, stroke_width=2)


class Geo812Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Север и исток — рамнини.",
                     font_size=44, color=GREEN, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Југ — планини.", font_size=40, color=ORANGE, weight=BOLD),
            Text("Алпите се млади.", font_size=34, color=WHITE2),
            Text("Стари 30 милиони години.", font_size=30, color=GREY),
            Text("Млади за планина.", font_size=36, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.4)
        self.play(FadeOut(hook1), FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  60% НИЗИНИ                                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("nizini")

        t2 = section_title("Половина и плус — рамнина", color=GREEN)
        self.play(Write(t2), run_time=0.9)

        # Pie-style proportion
        pie_radius = 1.8
        full_circle = Circle(radius=pie_radius, color=WHITE2, stroke_width=2)
        full_circle.shift(LEFT * 3.5 + DOWN * 0.3)
        # 60% sector (low) — start at top, sweep 216°
        low_sector = Sector(
            outer_radius=pie_radius,
            angle=2 * np.pi * 0.6,
            start_angle=PI / 2,
            fill_color=GREEN, fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=2,
        ).move_arc_center_to(full_circle.get_center())
        high_sector = Sector(
            outer_radius=pie_radius,
            angle=2 * np.pi * 0.4,
            start_angle=PI / 2 + 2 * np.pi * 0.6,
            fill_color=ORANGE, fill_opacity=0.7,
            stroke_color=ORANGE, stroke_width=2,
        ).move_arc_center_to(full_circle.get_center())

        self.play(Create(full_circle), run_time=0.5)
        self.play(FadeIn(low_sector), run_time=0.8)
        low_lab = Text("60%\nнизини", font_size=22, color=WHITE2, weight=BOLD)
        low_lab.move_to(low_sector.get_center_of_mass())
        self.play(Write(low_lab), run_time=0.6)
        self.play(FadeIn(high_sector), run_time=0.6)
        high_lab = Text("40%\nридести\n+ планини", font_size=18, color=WHITE2, weight=BOLD)
        high_lab.move_to(high_sector.get_center_of_mass())
        self.play(Write(high_lab), run_time=0.5)

        # Right side — East European Plain
        right = VGroup(
            callout("Источноевропска низина", width=5.4, bg=DARK_CARD,
                    border=GREEN, font_size=24),
            callout("Најголема рамнина во Европа", width=5.4, bg=DARK_CARD,
                    border=YELLOW, font_size=22),
            callout("Од Балтик до Касписко Море", width=5.4, bg=DARK_CARD,
                    border=BLUE, font_size=20),
            callout("≈ 4.000.000 км²", width=5.4, bg=DARK_CARD,
                    border=ORANGE, font_size=22),
        ).arrange(DOWN, buff=0.25).shift(RIGHT * 3.2 + DOWN * 0.3)

        for c in right:
            self.play(FadeIn(c, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(1.0)
        self.play(
            FadeOut(VGroup(full_circle, low_sector, high_sector,
                           low_lab, high_lab, right, t2)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 3.  МЛАДИ ПЛАНИНИ                                    ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mladi")

        t3 = section_title("Млади планини на југ", color=ORANGE)
        self.play(Write(t3), run_time=0.9)

        # Mountain silhouettes in a row
        alps     = mountain_silhouette(2.2, 1.7, ORANGE, seed=1)
        pyr      = mountain_silhouette(2.0, 1.4, RED,    seed=2)
        carp     = mountain_silhouette(2.4, 1.5, PURPLE, seed=3)
        balk     = mountain_silhouette(2.2, 1.3, YELLOW, seed=4)

        row = VGroup(alps, pyr, carp, balk).arrange(RIGHT, buff=0.4).shift(DOWN * 0.5)

        labels = []
        names = ["Алпи", "Пиринеи", "Карпати", "Балкан"]
        heights = ["4810 м", "3404 м", "2655 м", "2925 м"]
        colors = [ORANGE, RED, PURPLE, YELLOW]
        for m, name, h, col in zip(row, names, heights, colors):
            n = Text(name, font_size=22, color=col, weight=BOLD)
            n.next_to(m, DOWN, buff=0.15)
            ht = Text(h, font_size=16, color=WHITE2)
            ht.next_to(n, DOWN, buff=0.05)
            labels.append(VGroup(n, ht))

        for m, lab in zip(row, labels):
            self.play(FadeIn(m, shift=UP * 0.3), FadeIn(lab), run_time=0.55)
            self.wait(0.15)

        # Age note
        age = Text("Возраст: 30–60 милиони години — млади. Сè уште растат.",
                   font_size=22, color=BLUE, slant=ITALIC).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(age), run_time=0.8)
        self.wait(1.6)

        self.play(
            FadeOut(VGroup(row, *labels, age, t3)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 4.  СТАРИ ПЛАНИНИ                                    ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("stari")

        t4 = section_title("Стари планини — заоблени старци", color=GREY)
        self.play(Write(t4), run_time=0.9)

        # Two old, rounded mountains
        urals = mountain_silhouette(3.5, 1.2, GREY, jagged=False, seed=5)
        urals.shift(LEFT * 3.0 + DOWN * 0.5)
        scan  = mountain_silhouette(3.5, 1.4, GREY, jagged=False, seed=6)
        scan.shift(RIGHT * 3.0 + DOWN * 0.5)

        urals_lab = VGroup(
            Text("Урал", font_size=26, color=YELLOW, weight=BOLD),
            Text("1895 м (Народнаја)", font_size=18, color=WHITE2),
            Text("Граница со Азија", font_size=18, color=GREEN),
            Text("≈ 250 милиони год.", font_size=18, color=GREY),
        ).arrange(DOWN, buff=0.15).next_to(urals, DOWN, buff=0.3)

        scan_lab = VGroup(
            Text("Скандинавски планини", font_size=24, color=YELLOW, weight=BOLD),
            Text("2469 м (Галхопиген)", font_size=18, color=WHITE2),
            Text("Норвешка и Шведска", font_size=18, color=BLUE),
            Text("≈ 400 милиони год.", font_size=18, color=GREY),
        ).arrange(DOWN, buff=0.15).next_to(scan, DOWN, buff=0.3)

        self.play(FadeIn(urals, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(urals_lab), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(scan, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(scan_lab), run_time=0.5)

        punch = Text("Низок врв. Долга приказна.",
                     font_size=24, color=ORANGE, slant=ITALIC).to_edge(UP, buff=1.4)
        self.play(FadeOut(t4), run_time=0.3)
        self.play(Write(punch), run_time=0.9)

        self.wait(1.6)
        self.play(
            FadeOut(VGroup(urals, scan, urals_lab, scan_lab, punch)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 5.  МОН БЛАН — највисок врв                          ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("monblan")

        t5 = section_title("Мон Блан — крунисан врв", color=YELLOW)
        self.play(Write(t5), run_time=0.9)

        # Big mountain
        np.random.seed(11)
        big_pts = [LEFT * 4.0 + DOWN * 1.5]
        for i in range(1, 18):
            x = -4 + 8 * i / 18
            base_y = 3.2 * (1 - abs((i - 9)/9)**1.3)
            y = base_y + 0.15 * np.sin(i * 1.7)
            big_pts.append(np.array([x, y - 1.5, 0]))
        big_pts.append(RIGHT * 4.0 + DOWN * 1.5)
        mont = Polygon(*big_pts,
                       color=GREY, fill_color="#4a5a6a",
                       fill_opacity=0.7, stroke_width=2).shift(DOWN * 0.3)
        # Snow cap (top portion)
        peak_y = max(p[1] for p in big_pts)
        peak_x = [p[0] for p in big_pts if p[1] > peak_y - 0.5]
        snow_pts = [np.array([min(peak_x), peak_y - 0.5, 0])]
        for p in big_pts:
            if p[1] > peak_y - 0.5:
                snow_pts.append(p)
        snow_pts.append(np.array([max(peak_x), peak_y - 0.5, 0]))
        snow = Polygon(*snow_pts, color=WHITE2,
                       fill_color=WHITE2, fill_opacity=0.85, stroke_width=1).shift(DOWN * 0.3)

        self.play(FadeIn(mont, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(snow), run_time=0.6)

        # Height label with MathTex
        h_label = MathTex(r"4\,810 \text{ m}", font_size=56, color=YELLOW)
        h_arrow = Arrow(RIGHT * 2.5 + UP * 1.5, RIGHT * 0.8 + UP * 2.2,
                        color=YELLOW, buff=0.1)
        h_label.next_to(h_arrow.get_start(), RIGHT, buff=0.2)

        self.play(GrowArrow(h_arrow), run_time=0.6)
        self.play(Write(h_label), run_time=0.8)

        info = VGroup(
            Text("Највисок врв во Европа", font_size=22, color=WHITE2),
            Text("Алпи — Франција / Италија", font_size=20, color=ORANGE),
            Text("Покриен со снег цела година", font_size=20, color=BLUE),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.3)

        for ln in info:
            self.play(FadeIn(ln, shift=UP * 0.15), run_time=0.5)
            self.wait(0.15)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(mont, snow, h_arrow, h_label, info, t5)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 6.  ВЕРТИКАЛНО — попречен пресек                     ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("presek")

        t6 = section_title("Од запад на исток — попречен пресек", color=BLUE)
        self.play(Write(t6), run_time=0.9)

        # Cross section line
        base_y = -2.0
        base = Line(LEFT * 6.0 + UP * base_y, RIGHT * 6.0 + UP * base_y,
                    color=WHITE2, stroke_width=1.5)
        self.play(Create(base), run_time=0.5)

        # Profile points (west → east):
        profile_xy = [
            (-6.0, base_y),
            (-5.0, base_y + 0.2),   # coast
            (-4.0, base_y + 0.4),   # plains
            (-3.0, base_y + 0.6),
            (-2.0, base_y + 2.2),   # Alps
            (-0.8, base_y + 0.6),
            ( 0.5, base_y + 0.4),   # plain
            ( 2.0, base_y + 1.4),   # Carpathians
            ( 3.0, base_y + 0.4),
            ( 4.5, base_y + 0.6),   # East European Plain (low)
            ( 5.5, base_y + 1.6),   # Urals
            ( 6.0, base_y + 0.5),
        ]
        profile_pts = [np.array([x, y, 0]) for x, y in profile_xy]
        profile = VMobject(color=YELLOW, stroke_width=3)
        profile.set_points_as_corners(profile_pts)
        self.play(Create(profile), run_time=2.0)

        # Labels
        labs = [
            ("Атлантски брег", -5.0, base_y - 0.3, BLUE),
            ("Алпи", -2.0, base_y + 2.5, ORANGE),
            ("Источноевр. низина", 4.0, base_y - 0.3, GREEN),
            ("Урал", 5.5, base_y + 1.9, GREY),
        ]
        lab_objs = []
        for name, x, y, col in labs:
            t = Text(name, font_size=16, color=col)
            t.move_to(np.array([x, y, 0]))
            lab_objs.append(t)
            self.play(FadeIn(t), run_time=0.35)

        self.wait(0.8)
        verdict = Text("Запад мирен. Југ висок. Исток рамен. Урал — крај.",
                       font_size=22, color=YELLOW, slant=ITALIC).to_edge(DOWN, buff=0.3)
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(base, profile, *lab_objs, verdict, t6)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        final_title = Text("Релјеф = карактер.",
                           font_size=46, color=YELLOW, weight=BOLD)
        final_title.to_edge(UP, buff=0.8)
        self.play(Write(final_title), run_time=1.0)

        summary = VGroup(
            Text("Низини на исток. Планини на југ.",
                 font_size=26, color=GREEN),
            Text("Алпи млади и горди. Урал стар и низок.",
                 font_size=24, color=ORANGE),
            Text("Мон Блан — 4810 метри над сите.",
                 font_size=24, color=YELLOW, slant=ITALIC),
            Text("Земјата дише.",
                 font_size=30, color=BLUE, weight=BOLD),
            Text("Се крева.",
                 font_size=36, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(final_title, DOWN, buff=0.6)

        for line in summary:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(2.0)
        self.play(FadeOut(VGroup(final_title, summary)), run_time=0.8)
        self.wait(0.4)
