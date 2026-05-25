"""
geo8-3-4  —  Западен Балкан: Хрватска, Словенија, БиХ, Црна Гора
Географија 8, Единица 3: Јужна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as characters, peninsulas as branches of land.
Render:  manim -ql geo8-3-4.py Geo834Scene
Output:  media/videos/geo8-3-4/480p15/Geo834Scene.mp4
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


def country_panel(name, headline, bullets, color, pos, w=5.5, h=4.2):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=28, color=color, weight=BOLD)
    nm.move_to(box.get_top()+DOWN*0.4)
    hd = Text(headline, font_size=18, color=YELLOW)
    hd.move_to(box.get_top()+DOWN*0.95)
    bl = VGroup(*[Text("• " + b, font_size=16, color=WHITE2) for b in bullets])
    bl.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    bl.next_to(hd, DOWN, buff=0.35).align_to(box, LEFT).shift(RIGHT*0.4)
    return VGroup(box, nm, hd, bl)


class Geo834Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — "Четири приказни. Еден регион."        ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Западен Балкан.", font_size=54, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Хрватска прегрнала море.", font_size=32, color=BLUE),
            Text("Словенија ја чува планината.", font_size=32, color=GREEN),
            Text("БиХ е мозаик.", font_size=32, color=ORANGE),
            Text("Црна Гора — мала, но горда.", font_size=32, color=RED),
            Text("Четири приказни.", font_size=36, color=WHITE2, weight=BOLD),
            Text("Еден регион.", font_size=40, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.25).next_to(h1, DOWN, buff=0.4)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.5)
            self.wait(0.15)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  MAP OVERVIEW                                    ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("map")

        t2 = section_title("Каде се наоѓаат?")
        self.play(Write(t2), run_time=0.8)

        # Coastline curve (Adriatic)
        coast = ParametricFunction(
            lambda t: np.array([
                -3.0 + 2.5*np.sin(t*0.7),
                2.0 - t*0.9,
                0
            ]),
            t_range=[0, 5], color=BLUE, stroke_width=4,
        )
        self.play(Create(coast), run_time=1.5)

        adr_l = Text("Јадранско\nморе", font_size=18, color=BLUE, weight=BOLD)
        adr_l.move_to([-5.0, -0.5, 0])
        self.play(Write(adr_l), run_time=0.5)

        # Country blobs roughly placed
        sl = Polygon([-0.5, 2.5, 0], [1.5, 2.5, 0], [1.5, 1.5, 0], [-0.5, 1.5, 0],
                     fill_color="#5a8a4a", fill_opacity=0.7,
                     stroke_color=GREEN, stroke_width=2)
        sl_l = Text("Словенија", font_size=18, color=GREEN, weight=BOLD).move_to(sl)

        hr = Polygon([-1.5, 1.4, 0], [2.5, 1.4, 0], [2.5, 0.4, 0],
                     [1.0, 0.4, 0], [0.5, -0.6, 0], [-1.5, -0.6, 0],
                     fill_color="#4a7a8a", fill_opacity=0.7,
                     stroke_color=BLUE, stroke_width=2)
        hr_l = Text("Хрватска", font_size=18, color=BLUE, weight=BOLD).move_to([0.5, 0.4, 0])

        bh = Polygon([0.5, 0.3, 0], [3.0, 0.3, 0], [3.0, -1.5, 0], [0.0, -1.5, 0],
                     fill_color="#a87850", fill_opacity=0.7,
                     stroke_color=ORANGE, stroke_width=2)
        bh_l = Text("БиХ", font_size=20, color=ORANGE, weight=BOLD).move_to([1.5, -0.6, 0])

        mn = Polygon([0.2, -1.6, 0], [1.8, -1.6, 0], [2.0, -2.6, 0], [0.4, -2.6, 0],
                     fill_color="#8a4a5a", fill_opacity=0.7,
                     stroke_color=RED, stroke_width=2)
        mn_l = Text("Црна Гора", font_size=14, color=RED, weight=BOLD).move_to(mn)

        self.play(FadeIn(sl), Write(sl_l), run_time=0.5)
        self.play(FadeIn(hr), Write(hr_l), run_time=0.5)
        self.play(FadeIn(bh), Write(bh_l), run_time=0.5)
        self.play(FadeIn(mn), Write(mn_l), run_time=0.5)

        note = Text("Четири држави. Една обала.", font_size=24, color=YELLOW, weight=BOLD)
        note.to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t2, coast, adr_l, sl, sl_l, hr, hr_l, bh, bh_l, mn, mn_l, note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  CROATIA                                         ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("croatia")

        t3 = section_title("Хрватска — прегрнала море")
        self.play(Write(t3), run_time=0.8)

        hr_panel = country_panel(
            "Хрватска",
            "4 милиони луѓе",
            [
                "Загреб — главен град",
                "1800 km обала",
                "Над 1000 острови",
                "Туризам — Дубровник, Сплит",
                "Член на ЕУ од 2013",
                "Член на еврозона од 2023",
            ],
            BLUE,
            [-3.5, -0.3, 0]
        )

        # Coast illustration on right
        coast_d = ParametricFunction(
            lambda t: np.array([
                2.5 + 1.5*np.sin(t*1.5),
                2.0 - t*0.8,
                0
            ]),
            t_range=[0, 5], color=BLUE, stroke_width=4,
        )
        # Islands
        isles = VGroup(*[
            Circle(radius=0.15+0.05*i, color=GREEN, fill_color=GREEN, fill_opacity=0.7, stroke_width=1)
            .move_to([1.5+0.3*i, 1.8-0.7*i, 0])
            for i in range(6)
        ])

        self.play(FadeIn(hr_panel), run_time=1.0)
        self.play(Create(coast_d), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, isles, lag_ratio=0.15), run_time=1.2)

        punch = Text("Обала. Сонце. Гости.", font_size=24, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, hr_panel, coast_d, isles, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  SLOVENIA                                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("slovenia")

        t4 = section_title("Словенија — ја чува планината")
        self.play(Write(t4), run_time=0.8)

        sl_panel = country_panel(
            "Словенија",
            "2 милиони луѓе",
            [
                "Љубљана — главен град",
                "Јулиските Алпи — Триглав 2864 m",
                "Богато стопанство",
                "Член на ЕУ од 2004",
                "Член на еврозона од 2007",
                "Шуми покриваат 60% од земјата",
            ],
            GREEN,
            [-3.5, -0.3, 0]
        )

        # Mountain illustration
        mtn = Polygon(
            [1.5, -1.5, 0], [2.5, 1.5, 0], [3.5, -0.5, 0], [4.5, 1.8, 0], [5.5, -1.5, 0],
            fill_color="#5a6470", fill_opacity=0.9,
            stroke_color=GREY, stroke_width=2,
        )
        # Snow caps
        snow1 = Polygon([2.3, 1.0, 0], [2.5, 1.5, 0], [2.7, 1.0, 0],
                        fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        snow2 = Polygon([4.3, 1.3, 0], [4.5, 1.8, 0], [4.7, 1.3, 0],
                        fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        tri_l = Text("Триглав", font_size=16, color=WHITE2, weight=BOLD)
        tri_l.next_to(snow2, UP, buff=0.1)

        self.play(FadeIn(sl_panel), run_time=1.0)
        self.play(FadeIn(mtn), run_time=1.0)
        self.play(FadeIn(snow1), FadeIn(snow2), Write(tri_l), run_time=0.7)

        punch = Text("Мала земја. Голема врвица.", font_size=24, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t4, sl_panel, mtn, snow1, snow2, tri_l, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  BOSNIA AND HERZEGOVINA                          ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("bih")

        t5 = section_title("БиХ — мозаик од народи")
        self.play(Write(t5), run_time=0.8)

        bh_panel = country_panel(
            "Босна и Херцеговина",
            "3 милиони луѓе",
            [
                "Сараево — главен град",
                "Три народи: Бошњаци, Срби, Хрвати",
                "Три вери: ислам, православие, католицизам",
                "Војна 1992-1995",
                "Дејтонски мир 1995",
                "Сложен политички систем",
            ],
            ORANGE,
            [-3.5, -0.3, 0]
        )

        # Mosaic illustration — three circles overlapping
        c1 = Circle(radius=0.9, color=GREEN, fill_color=GREEN, fill_opacity=0.5, stroke_width=2)
        c1.move_to([3.0, 0.6, 0])
        c1_l = Text("Бошњаци", font_size=14, color=GREEN, weight=BOLD).next_to(c1, UP, buff=0.05)

        c2 = Circle(radius=0.9, color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=2)
        c2.move_to([2.2, -0.6, 0])
        c2_l = Text("Срби", font_size=14, color=BLUE, weight=BOLD).next_to(c2, LEFT, buff=0.1)

        c3 = Circle(radius=0.9, color=RED, fill_color=RED, fill_opacity=0.5, stroke_width=2)
        c3.move_to([3.8, -0.6, 0])
        c3_l = Text("Хрвати", font_size=14, color=RED, weight=BOLD).next_to(c3, RIGHT, buff=0.1)

        self.play(FadeIn(bh_panel), run_time=1.0)
        self.play(FadeIn(c1), Write(c1_l), run_time=0.5)
        self.play(FadeIn(c2), Write(c2_l), run_time=0.5)
        self.play(FadeIn(c3), Write(c3_l), run_time=0.5)

        punch = Text("Различни. Споени. БиХ.", font_size=24, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, bh_panel, c1, c1_l, c2, c2_l, c3, c3_l, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  MONTENEGRO                                      ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("montenegro")

        t6 = section_title("Црна Гора — мала, но горда")
        self.play(Write(t6), run_time=0.8)

        mn_panel = country_panel(
            "Црна Гора",
            "620 илјади луѓе",
            [
                "Подгорица — главен град",
                "Најмала на Балканот",
                "Боката Которска — фјорд во Медитеранот",
                "Користи евро од 2002",
                "Член на НАТО од 2017",
                "Цел туризам",
            ],
            RED,
            [-3.5, -0.3, 0]
        )

        # Bay illustration
        bay = ParametricFunction(
            lambda t: np.array([
                2.5 + 1.2*np.cos(t),
                0.2 + 0.8*np.sin(t),
                0
            ]),
            t_range=[0, 2*PI], color=BLUE, stroke_width=4,
        )
        bay_fill = Circle(radius=1.0, color=BLUE, fill_color="#1a4a6a", fill_opacity=0.6, stroke_width=0)
        bay_fill.move_to([2.5, 0.2, 0])
        bay_l = Text("Бока Которска", font_size=16, color=BLUE, weight=BOLD)
        bay_l.next_to(bay, DOWN, buff=0.2)

        # Mountains around
        mtn_l = Polygon([1.0, -0.5, 0], [1.5, 1.0, 0], [2.0, -0.5, 0],
                        fill_color="#5a6470", fill_opacity=0.8, stroke_color=GREY, stroke_width=1)
        mtn_r = Polygon([3.5, -0.5, 0], [4.0, 1.2, 0], [4.5, -0.5, 0],
                        fill_color="#5a6470", fill_opacity=0.8, stroke_color=GREY, stroke_width=1)

        self.play(FadeIn(mn_panel), run_time=1.0)
        self.play(FadeIn(bay_fill), Create(bay), Write(bay_l), run_time=1.0)
        self.play(FadeIn(mtn_l), FadeIn(mtn_r), run_time=0.6)

        punch = Text("Мала. Но горда.", font_size=24, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t6, mn_panel, bay_fill, bay, bay_l, mtn_l, mtn_r, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  TRANSITION ECONOMIES & CLOSING                  ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        t7 = section_title("Економии во транзиција")
        self.play(Write(t7), run_time=0.8)

        # Bar comparison of GDP per capita (rough relative)
        countries = [
            ("Словенија", 28000, GREEN),
            ("Хрватска",  19000, BLUE),
            ("Ц. Гора",   10000, RED),
            ("БиХ",        7500, ORANGE),
        ]
        max_v = 30000
        bars = VGroup()
        labels = VGroup()
        values = VGroup()
        for i, (nm, v, col) in enumerate(countries):
            x = -4.5 + i*3.0
            h = (v / max_v) * 3.0
            bar = Rectangle(width=1.5, height=h,
                fill_color=col, fill_opacity=0.8,
                stroke_color=col, stroke_width=2,
            )
            bar.move_to([x, -1.2 + h/2, 0])
            bars.add(bar)
            lab = Text(nm, font_size=16, color=col, weight=BOLD)
            lab.next_to(bar, DOWN, buff=0.15)
            labels.add(lab)
            val = Text(f"€{v//1000}k", font_size=14, color=WHITE2)
            val.next_to(bar, UP, buff=0.1)
            values.add(val)

        yax = Text("БДП по жител (евра)", font_size=16, color=GREY)
        yax.to_edge(UP, buff=1.3).shift(LEFT*4)

        self.play(Write(yax), run_time=0.5)
        for b, l, v in zip(bars, labels, values):
            self.play(GrowFromEdge(b, DOWN), Write(l), Write(v), run_time=0.5)

        self.wait(1.0)
        self.play(FadeOut(VGroup(t7, bars, labels, values, yax)), run_time=0.7)

        # Final beat
        end1 = Text("Западен Балкан.", font_size=58, color=YELLOW, weight=BOLD)
        end1.move_to(UP * 1.6)
        self.play(Write(end1), run_time=1.0)

        end_lines = VGroup(
            Text("Четири земји.", font_size=32, color=WHITE2),
            Text("Едно море. Едно небо.", font_size=32, color=BLUE),
            Text("Различни. Сите наши соседи.", font_size=36, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(end1, DOWN, buff=0.5)

        for L in end_lines:
            self.play(FadeIn(L, shift=UP*0.15), run_time=0.7)
            self.wait(0.2)

        self.wait(2.0)
