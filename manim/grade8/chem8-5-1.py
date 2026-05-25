"""
chem8-5-1  —  Вовед во хемијата на јаглеродни соединенија
Хемија 8, Единица 5: Органска хемија

Teaching narrative — Andonovski-style: three-beat punches,
carbon as protagonist of organic chemistry, personification,
one-word finishers.
Render:  manim -ql chem8-5-1.py Chem851Scene
Output:  media/videos/chem8-5-1/480p15/Chem851Scene.mp4
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


def carbon_atom(pos, label="C", r=0.42, color=YELLOW):
    c = Circle(radius=r, fill_color=color, fill_opacity=1,
               stroke_color=WHITE2, stroke_width=2).move_to(pos)
    t = Text(label, font_size=28, color="#0d1b2e", weight=BOLD).move_to(pos)
    return VGroup(c, t)


def hydrogen_atom(pos, r=0.26):
    c = Circle(radius=r, fill_color=BLUE, fill_opacity=1,
               stroke_color=WHITE2, stroke_width=2).move_to(pos)
    t = Text("H", font_size=22, color="#0d1b2e", weight=BOLD).move_to(pos)
    return VGroup(c, t)


def bond(p1, p2, color=WHITE2, width=4):
    return Line(p1, p2, color=color, stroke_width=width)


class Chem851Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Јаглеродот има 4 раце.",
                     font_size=46, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.6)
        self.wait(0.5)

        beats = VGroup(
            Text("Држи се за себе.", font_size=34, color=WHITE2),
            Text("Држи се за други.", font_size=34, color=WHITE2),
            Text("Создава ланци.", font_size=34, color=GREEN),
            Text("Создава прстени.", font_size=34, color=ORANGE),
            Text("Создава живот.", font_size=38, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.28).move_to(ORIGIN + DOWN*0.3)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
            self.wait(0.25)

        self.wait(1.0)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  CARBON — 4 BONDS                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("four_bonds")

        title = section_title("Четири врски")
        self.play(Write(title), run_time=0.8)

        # central carbon with 4 bonds in tetrahedral-ish 2D
        C = carbon_atom(ORIGIN, "C")
        self.play(GrowFromCenter(C), run_time=0.7)

        # 4 bond stubs
        directions = [UP*1.2, DOWN*1.2, LEFT*1.6, RIGHT*1.6]
        stubs = VGroup(*[bond(ORIGIN, d, color=WHITE2) for d in directions])
        self.play(LaggedStart(*[Create(s) for s in stubs],
                              lag_ratio=0.2), run_time=1.4)

        hands_label = Text("4 валентни електрони → 4 врски",
                           font_size=28, color=YELLOW)
        hands_label.next_to(C, DOWN*3.2)
        self.play(FadeIn(hands_label), run_time=0.8)
        self.wait(1.0)

        # attach 4 hydrogens → methane
        Hs = VGroup(
            hydrogen_atom(UP*1.5),
            hydrogen_atom(DOWN*1.5),
            hydrogen_atom(LEFT*1.9),
            hydrogen_atom(RIGHT*1.9),
        )
        self.play(*[FadeIn(h, scale=0.5) for h in Hs], run_time=1.0)

        ch4 = MathTex(r"\mathrm{CH_4}", font_size=46, color=GREEN)
        ch4.to_edge(DOWN, buff=0.7)
        self.play(Write(ch4), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(C, stubs, Hs, hands_label, ch4, title)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  CHAINS & RINGS                                  ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chains_rings")

        title2 = section_title("Ланци. Прстени.")
        self.play(Write(title2), run_time=0.8)

        # chain on left
        chain_pts = [LEFT*4 + RIGHT*i*1.0 for i in range(5)]
        chain_C = VGroup(*[carbon_atom(p + UP*1.0, "C", r=0.32) for p in chain_pts])
        chain_bonds = VGroup(*[
            bond(chain_pts[i] + UP*1.0, chain_pts[i+1] + UP*1.0)
            for i in range(4)
        ])
        self.play(LaggedStart(*[GrowFromCenter(a) for a in chain_C],
                              lag_ratio=0.15), run_time=1.6)
        self.play(LaggedStart(*[Create(b) for b in chain_bonds],
                              lag_ratio=0.15), run_time=1.2)

        chain_lbl = Text("ланец", font_size=28, color=GREEN)
        chain_lbl.next_to(chain_C, UP, buff=0.3)
        self.play(FadeIn(chain_lbl), run_time=0.5)

        # ring on right (hexagon)
        ring_center = RIGHT*3.5 + DOWN*0.5
        ring_pts = [ring_center + np.array([np.cos(a)*1.0, np.sin(a)*1.0, 0])
                    for a in np.linspace(0, 2*PI, 7)[:-1]]
        ring_C = VGroup(*[carbon_atom(p, "C", r=0.28) for p in ring_pts])
        ring_bonds = VGroup(*[
            bond(ring_pts[i], ring_pts[(i+1) % 6])
            for i in range(6)
        ])
        self.play(LaggedStart(*[GrowFromCenter(a) for a in ring_C],
                              lag_ratio=0.12), run_time=1.4)
        self.play(LaggedStart(*[Create(b) for b in ring_bonds],
                              lag_ratio=0.12), run_time=1.0)

        ring_lbl = Text("прстен", font_size=28, color=ORANGE)
        ring_lbl.next_to(ring_C, UP, buff=0.3)
        self.play(FadeIn(ring_lbl), run_time=0.5)
        self.wait(1.2)

        punch = callout("Само јаглеродот го прави ова.", width=10,
                        bg=DARK_CARD, border=YELLOW, font_size=30)
        punch.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(punch, shift=UP*0.3), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, chain_C, chain_bonds, chain_lbl,
                                 ring_C, ring_bonds, ring_lbl, punch)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ORGANIC CHEMISTRY DEFINITION                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title3 = section_title("Органска хемија")
        self.play(Write(title3), run_time=0.8)

        defn_box = RoundedRectangle(
            width=11, height=2.2, corner_radius=0.4,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=3,
        ).move_to(ORIGIN + UP*0.6)
        defn = VGroup(
            Text("Хемија на јаглеродните соединенија.",
                 font_size=32, color=WHITE2),
            Text("Освен карбонати и оксиди — сите се органски.",
                 font_size=24, color=GREY),
        ).arrange(DOWN, buff=0.2).move_to(defn_box)

        self.play(Create(defn_box), run_time=0.7)
        self.play(Write(defn), run_time=1.4)
        self.wait(1.0)

        examples = VGroup(
            Text("Бензин. Шеќер. ДНК.", font_size=30, color=YELLOW),
            Text("Пластика. Лек. Витамин.", font_size=30, color=ORANGE),
            Text("Сè живо.", font_size=34, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.22).next_to(defn_box, DOWN, buff=0.5)

        for e in examples:
            self.play(FadeIn(e, shift=UP*0.15), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, defn_box, defn, examples)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ALLOTROPES OF CARBON                            ~36 s
        # ══════════════════════════════════════════════════════════
        self.next_section("allotropes")

        title4 = section_title("Истиот атом. Различни лица.", color=PURPLE)
        self.play(Write(title4), run_time=0.9)
        self.wait(0.4)

        # 4 cards: diamond, graphite, graphene, fullerene
        def allotrope_card(pos, name, sketch_func, color):
            box = RoundedRectangle(
                width=2.8, height=2.6, corner_radius=0.3,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=2,
            ).move_to(pos)
            sk = sketch_func().scale(0.55).move_to(pos + UP*0.25)
            lbl = Text(name, font_size=22, color=color, weight=BOLD)
            lbl.next_to(box, DOWN, buff=-0.6).align_to(box, DOWN).shift(UP*0.25)
            return VGroup(box, sk, lbl)

        def diamond_sketch():
            # tetrahedral
            top = UP*0.8
            base = [LEFT*0.7 + DOWN*0.4, RIGHT*0.7 + DOWN*0.4, DOWN*0.8]
            pts = [top] + base
            dots = VGroup(*[Dot(p, color=BLUE, radius=0.08) for p in pts])
            lines = VGroup(
                Line(pts[0], pts[1], color=BLUE),
                Line(pts[0], pts[2], color=BLUE),
                Line(pts[0], pts[3], color=BLUE),
                Line(pts[1], pts[2], color=BLUE),
                Line(pts[1], pts[3], color=BLUE),
                Line(pts[2], pts[3], color=BLUE),
            )
            return VGroup(lines, dots)

        def graphite_sketch():
            # stacked hex sheets — show 2 hexagons stacked
            def hex_at(center, color):
                pts = [center + np.array([np.cos(a)*0.5, np.sin(a)*0.5, 0])
                       for a in np.linspace(0, 2*PI, 7)[:-1]]
                hex_lines = VGroup(*[Line(pts[i], pts[(i+1) % 6], color=color)
                                     for i in range(6)])
                hex_dots = VGroup(*[Dot(p, color=color, radius=0.06)
                                    for p in pts])
                return VGroup(hex_lines, hex_dots)
            return VGroup(hex_at(UP*0.35, GREY),
                          hex_at(DOWN*0.35 + RIGHT*0.2, ORANGE))

        def graphene_sketch():
            # single hex sheet — multiple hexagons in row
            g = VGroup()
            for i, c in enumerate([LEFT*0.5, RIGHT*0.5]):
                pts = [c + np.array([np.cos(a)*0.4, np.sin(a)*0.4, 0])
                       for a in np.linspace(0, 2*PI, 7)[:-1]]
                lines = VGroup(*[Line(pts[i], pts[(i+1) % 6], color=GREEN)
                                 for i in range(6)])
                dots = VGroup(*[Dot(p, color=GREEN, radius=0.05) for p in pts])
                g.add(lines, dots)
            return g

        def fullerene_sketch():
            # sphere of dots
            g = VGroup()
            for r, n, col in [(0.5, 8, YELLOW), (0.8, 12, ORANGE)]:
                for k in range(n):
                    a = 2*PI*k/n
                    p = np.array([np.cos(a)*r, np.sin(a)*r*0.6, 0])
                    g.add(Dot(p, color=col, radius=0.06))
            outer = Circle(radius=0.85, color=YELLOW, stroke_width=1.5)
            return VGroup(outer, g)

        positions = [LEFT*4.5, LEFT*1.5, RIGHT*1.5, RIGHT*4.5]
        names = ["Дијамант", "Графит", "Графен", "Фулерен"]
        sketches = [diamond_sketch, graphite_sketch,
                    graphene_sketch, fullerene_sketch]
        colors = [BLUE, GREY, GREEN, YELLOW]

        cards = VGroup()
        for p, n, s, c in zip(positions, names, sketches, colors):
            cards.add(allotrope_card(p + DOWN*0.5, n, s, c))

        for card in cards:
            self.play(FadeIn(card, shift=UP*0.3), run_time=0.6)
        self.wait(1.0)

        all_lbl = Text("Алотропи: ист елемент, различна структура.",
                       font_size=26, color=WHITE2)
        all_lbl.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(all_lbl), run_time=0.6)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title4, cards, all_lbl)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  CARBON = LIFE                                   ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("life")

        final_title = Text("Јаглеродот.",
                           font_size=56, color=YELLOW, weight=BOLD)
        final_title.to_edge(UP, buff=0.7)
        self.play(Write(final_title), run_time=0.9)

        punches = VGroup(
            Text("Скромен атом.", font_size=34, color=WHITE2),
            Text("Шест протони. Шест електрони.", font_size=30, color=GREY),
            Text("Но четири раце.", font_size=34, color=GREEN),
            Text("И целиот живот зависи од него.",
                 font_size=36, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN + DOWN*0.3)

        for p in punches:
            self.play(FadeIn(p, shift=UP*0.2), run_time=0.6)
            self.wait(0.3)

        self.wait(1.0)

        finisher = Text("Протагонист.", font_size=44, color=ORANGE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.7)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(final_title, punches, finisher)),
                  run_time=1.0)
        self.wait(0.5)
