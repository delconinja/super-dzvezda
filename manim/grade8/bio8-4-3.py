"""
bio8-4-3  —  Крвни садови
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
artery pushes, vein pulls, capillary passes the message.
Render:  manim -ql bio8-4-3.py Bio843Scene
Output:  media/videos/bio8-4-3/480p15/Bio843Scene.mp4
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


class Bio843Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Три типа цевки.",
                     font_size=46, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)

        beats = VGroup(
            Text("Артеријата турка.",
                 font_size=36, color=RED, weight=BOLD),
            Text("Вената влече.",
                 font_size=36, color=BLUE, weight=BOLD),
            Text("Капиларот ја пренесува пораката.",
                 font_size=30, color=GREEN),
            Text("Една цел: животот.",
                 font_size=38, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ARTERY — thick walls, high pressure              ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("artery")

        title = section_title("Артерија — турка", color=RED)
        self.play(Write(title), run_time=0.8)

        # cross-section — concentric circles
        outer_a = Circle(radius=1.8, color=RED,
                         fill_color=RED, fill_opacity=0.25,
                         stroke_color=RED, stroke_width=4)
        inner_a = Circle(radius=0.7, color=DARK_CARD,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=1.5)
        outer_a.move_to(LEFT * 4.0 + UP * 0.3)
        inner_a.move_to(LEFT * 4.0 + UP * 0.3)

        # blood dots inside
        a_dots = VGroup()
        for _ in range(6):
            r = np.random.uniform(0, 0.5)
            ang = np.random.uniform(0, TAU)
            d = Dot(LEFT * 4.0 + UP * 0.3 +
                    np.array([r * np.cos(ang), r * np.sin(ang), 0]),
                    radius=0.07, color=RED)
            a_dots.add(d)

        wall_brace = Brace(outer_a, RIGHT, color=YELLOW, buff=0.1).scale(0.5)
        wall_brace.move_to(LEFT * 1.9 + UP * 0.3)
        wall_lbl = Text("дебел ѕид", font_size=20, color=YELLOW)
        wall_lbl.next_to(wall_brace, RIGHT, buff=0.2)

        # right side — feature cards
        feats = [
            ("Дебели мускулни ѕидови", RED),
            ("Висок притисок",         ORANGE),
            ("Отстранува од срцето",   YELLOW),
            ("Пулсира со срцето",      PURPLE),
            ("Носи богата со кислород", GREEN),
        ]
        cards = VGroup()
        for name, col in feats:
            box = RoundedRectangle(
                width=6.0, height=0.6, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            t = Text(name, font_size=22, color=col)
            t.move_to(box)
            cards.add(VGroup(box, t))
        cards.arrange(DOWN, buff=0.18)
        cards.move_to(RIGHT * 3.0 + UP * 0.3)

        self.play(Create(outer_a), Create(inner_a), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in a_dots],
                              lag_ratio=0.08), run_time=0.8)
        self.play(GrowFromCenter(wall_brace), FadeIn(wall_lbl), run_time=0.6)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, outer_a, inner_a, a_dots,
                                 wall_brace, wall_lbl, cards)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  VEIN — thin walls, valves                        ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vein")

        title = section_title("Вена — влече", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # cross-section — thinner wall
        outer_v = Circle(radius=1.7, color=BLUE,
                         fill_color=BLUE, fill_opacity=0.18,
                         stroke_color=BLUE, stroke_width=2)
        inner_v = Circle(radius=1.3, color=DARK_CARD,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=1.5)
        outer_v.move_to(LEFT * 4.0 + UP * 1.2)
        inner_v.move_to(LEFT * 4.0 + UP * 1.2)

        v_dots = VGroup()
        for _ in range(8):
            r = np.random.uniform(0, 1.1)
            ang = np.random.uniform(0, TAU)
            d = Dot(LEFT * 4.0 + UP * 1.2 +
                    np.array([r * np.cos(ang), r * np.sin(ang), 0]),
                    radius=0.07, color=BLUE)
            v_dots.add(d)

        v_wall_lbl = Text("тенок ѕид", font_size=20, color=YELLOW)
        v_wall_lbl.next_to(outer_v, RIGHT, buff=0.4)

        # below — longitudinal view with valves
        long_top = Line(LEFT * 6.0 + DOWN * 1.5,
                        LEFT * 1.5 + DOWN * 1.5,
                        color=BLUE, stroke_width=3)
        long_bot = Line(LEFT * 6.0 + DOWN * 2.5,
                        LEFT * 1.5 + DOWN * 2.5,
                        color=BLUE, stroke_width=3)

        # valves — two pairs of triangles
        valve_xs = [LEFT * 4.7, LEFT * 2.7]
        valves = VGroup()
        for vx in valve_xs:
            t1 = Polygon(vx + DOWN * 1.5,
                         vx + RIGHT * 0.4 + DOWN * 2.0,
                         vx + LEFT * 0.4 + DOWN * 2.0,
                         color=GREEN, fill_color=GREEN, fill_opacity=0.7,
                         stroke_width=1.5)
            t2 = Polygon(vx + DOWN * 2.5,
                         vx + RIGHT * 0.4 + DOWN * 2.0,
                         vx + LEFT * 0.4 + DOWN * 2.0,
                         color=GREEN, fill_color=GREEN, fill_opacity=0.7,
                         stroke_width=1.5)
            valves.add(t1, t2)

        # arrow showing direction
        flow_arrow = Arrow(LEFT * 5.8 + DOWN * 2.0,
                           LEFT * 1.8 + DOWN * 2.0,
                           color=YELLOW, buff=0.1, stroke_width=4)

        valves_lbl = Text("залистоци — спречуваат враќање",
                          font_size=20, color=GREEN)
        valves_lbl.move_to(LEFT * 3.7 + DOWN * 3.2)

        # right side — features
        feats = [
            ("Тенки ѕидови",            BLUE),
            ("Низок притисок",          GREY),
            ("Враќа кон срцето",        ORANGE),
            ("Има залистоци",           GREEN),
            ("Носи сиромашна со O₂",    PURPLE),
        ]
        cards = VGroup()
        for name, col in feats:
            box = RoundedRectangle(
                width=5.5, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            t = Text(name, font_size=20, color=col)
            t.move_to(box)
            cards.add(VGroup(box, t))
        cards.arrange(DOWN, buff=0.15)
        cards.move_to(RIGHT * 3.2 + DOWN * 0.5)

        self.play(Create(outer_v), Create(inner_v), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in v_dots],
                              lag_ratio=0.07), run_time=0.8)
        self.play(FadeIn(v_wall_lbl), run_time=0.4)
        self.play(Create(long_top), Create(long_bot), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(v) for v in valves],
                              lag_ratio=0.15), run_time=0.8)
        self.play(GrowArrow(flow_arrow), FadeIn(valves_lbl), run_time=0.7)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, outer_v, inner_v, v_dots, v_wall_lbl,
                                 long_top, long_bot, valves, flow_arrow,
                                 valves_lbl, cards)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  CAPILLARY — exchange                             ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("capillary")

        title = section_title("Капилар — пренесува", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # very narrow tube
        cap_top = Line(LEFT * 6.0, RIGHT * 6.0, color=GREEN, stroke_width=2)
        cap_bot = Line(LEFT * 6.0 + DOWN * 0.4, RIGHT * 6.0 + DOWN * 0.4,
                       color=GREEN, stroke_width=2)
        cap_top.shift(UP * 1.5)
        cap_bot.shift(UP * 1.5)

        cap_lbl = Text("еден ред клетки — ѕидот", font_size=20, color=GREEN)
        cap_lbl.next_to(cap_top, UP, buff=0.2)

        # cells around the capillary
        cells = VGroup()
        for x in [-4, -2, 0, 2, 4]:
            for y in [0.4, -0.7]:
                c = RoundedRectangle(width=0.9, height=0.5,
                                     corner_radius=0.15,
                                     fill_color=PURPLE, fill_opacity=0.5,
                                     stroke_color=WHITE2, stroke_width=1)
                c.move_to(RIGHT * x + UP * y)
                cells.add(c)

        # O2 entering cells (orange dots from capillary down/up)
        o2_arrows = VGroup()
        for x in [-4, -2, 0, 2, 4]:
            a = Arrow(RIGHT * x + UP * 1.5, RIGHT * x + UP * 0.5,
                      color=ORANGE, buff=0.1, stroke_width=3)
            o2_arrows.add(a)
        o2_lbl = Text("O₂ → клетка", font_size=20, color=ORANGE)
        o2_lbl.move_to(LEFT * 5.0 + UP * 0.4)

        # CO2 going back (blue arrows up)
        co2_arrows = VGroup()
        for x in [-4, -2, 0, 2, 4]:
            a = Arrow(RIGHT * x + DOWN * 0.7,
                      RIGHT * x + UP * 1.0,
                      color=BLUE, buff=0.1, stroke_width=3)
            co2_arrows.add(a)
        co2_lbl = Text("CO₂ ← клетка", font_size=20, color=BLUE)
        co2_lbl.move_to(RIGHT * 5.5 + DOWN * 1.0)

        self.play(Create(cap_top), Create(cap_bot), FadeIn(cap_lbl),
                  run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c) for c in cells],
                              lag_ratio=0.05), run_time=1.0)
        self.play(LaggedStart(*[GrowArrow(a) for a in o2_arrows],
                              lag_ratio=0.15),
                  FadeIn(o2_lbl), run_time=1.0)
        self.play(LaggedStart(*[GrowArrow(a) for a in co2_arrows],
                              lag_ratio=0.15),
                  FadeIn(co2_lbl), run_time=1.0)

        note = callout("Капиларот е каде размена се случува",
                       width=10.0, border=GREEN, font_size=24)
        note.move_to(DOWN * 2.8)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, cap_top, cap_bot, cap_lbl,
                                 cells, o2_arrows, co2_arrows,
                                 o2_lbl, co2_lbl, note)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  COMPARISON TABLE                                 ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        title = section_title("Споредба")
        self.play(Write(title), run_time=0.8)

        head_y = UP * 1.8
        col_x = [-4.5, -1.0, 2.5]
        h0 = Text("Особина", font_size=22, color=YELLOW, weight=BOLD).move_to(RIGHT * col_x[0] + head_y)
        h1 = Text("Артерија", font_size=22, color=RED, weight=BOLD).move_to(RIGHT * col_x[1] + head_y)
        h2 = Text("Вена", font_size=22, color=BLUE, weight=BOLD).move_to(RIGHT * col_x[2] + head_y)
        h3 = Text("Капилар", font_size=22, color=GREEN, weight=BOLD).move_to(RIGHT * 5.5 + head_y)

        rows = [
            ("Ѕид",       "дебел",      "тенок",      "1 клетка"),
            ("Притисок",  "висок",      "низок",      "многу низок"),
            ("Насока",    "од срце",    "кон срце",   "размена"),
            ("Залистоци", "не",         "да",         "не"),
            ("Дијаметар", "среден",     "голем",      "микро"),
        ]

        all_cells = VGroup(h0, h1, h2, h3)
        for i, (a, b, c, d) in enumerate(rows):
            y = head_y + DOWN * (0.6 + i * 0.5)
            ta = Text(a, font_size=20, color=WHITE2).move_to(RIGHT * col_x[0] + y)
            tb = Text(b, font_size=20, color=RED).move_to(RIGHT * col_x[1] + y)
            tc = Text(c, font_size=20, color=BLUE).move_to(RIGHT * col_x[2] + y)
            td = Text(d, font_size=20, color=GREEN).move_to(RIGHT * 5.5 + y)
            all_cells.add(ta, tb, tc, td)

        self.play(FadeIn(h0), FadeIn(h1), FadeIn(h2), FadeIn(h3),
                  run_time=0.6)
        for i in range(len(rows)):
            row_objs = all_cells[4 + i * 4:8 + i * 4]
            self.play(FadeIn(row_objs, shift=UP * 0.15), run_time=0.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, all_cells)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  REAL — total length                              ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("real")

        title = section_title("Цевки — повеќе од замислуваш")
        self.play(Write(title), run_time=0.8)

        stat = Text("100.000 km крвни садови во едно тело",
                    font_size=32, color=YELLOW, weight=BOLD)
        stat.move_to(UP * 1.4)

        cmp1 = Text("Доволно да го обиколи екваторот 2.5 пати.",
                    font_size=26, color=BLUE)
        cmp2 = Text("Капиларите се 80% од сè.",
                    font_size=26, color=GREEN)
        cmp3 = Text("Невидливи. Но без нив — нема живот.",
                    font_size=28, color=ORANGE, weight=BOLD)
        cmps = VGroup(cmp1, cmp2, cmp3).arrange(DOWN, buff=0.5)
        cmps.next_to(stat, DOWN, buff=0.7)

        self.play(Write(stat), run_time=1.0)
        for c in cmps:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.6)
            self.wait(0.25)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, stat, cmps)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Артеријата турка — дебели ѕидови, висок притисок.",
                 font_size=26, color=RED),
            Text("Вената влече — тенки ѕидови, залистоци.",
                 font_size=26, color=BLUE),
            Text("Капиларот пренесува — еден ред клетки.",
                 font_size=26, color=GREEN),
            Text("Три типа. Една цел: животот.",
                 font_size=32, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
