"""
bio8-4-4  —  Состав на крвта
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
four ingredients, one story — that is blood.
Render:  manim -ql bio8-4-4.py Bio844Scene
Output:  media/videos/bio8-4-4/480p15/Bio844Scene.mp4
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


class Bio844Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Крвта не е една течност.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)

        beats = VGroup(
            Text("Плазма.",       font_size=36, color=ORANGE, weight=BOLD),
            Text("Црвенки.",      font_size=36, color=RED, weight=BOLD),
            Text("Беленки.",      font_size=36, color=BLUE, weight=BOLD),
            Text("Тромбоцити.",   font_size=36, color=PURPLE, weight=BOLD),
            Text("Четири состојки. Една приказна.",
                 font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  CENTRIFUGE — separation                          ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("centrifuge")

        title = section_title("Што гледаме во епрувета")
        self.play(Write(title), run_time=0.8)

        # tube — vertical rectangle, separated into 3 layers
        tube = RoundedRectangle(width=1.6, height=5.0,
                                corner_radius=0.4,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=WHITE2, stroke_width=2)
        tube.move_to(LEFT * 4.0 + DOWN * 0.2)

        plasma_layer = Rectangle(width=1.55, height=2.6,
                                 fill_color=YELLOW, fill_opacity=0.7,
                                 stroke_width=0)
        plasma_layer.move_to(LEFT * 4.0 + UP * 1.0)

        buffy = Rectangle(width=1.55, height=0.25,
                          fill_color=WHITE2, fill_opacity=0.9,
                          stroke_width=0)
        buffy.move_to(LEFT * 4.0 + DOWN * 0.4)

        rbc_layer = Rectangle(width=1.55, height=2.0,
                              fill_color=RED, fill_opacity=0.85,
                              stroke_width=0)
        rbc_layer.move_to(LEFT * 4.0 + DOWN * 1.6)

        # labels
        plasma_lbl = Text("Плазма ~55%", font_size=22, color=YELLOW, weight=BOLD)
        plasma_lbl.move_to(LEFT * 1.0 + UP * 1.5)
        plasma_arrow = Arrow(plasma_lbl.get_left(), LEFT * 3.2 + UP * 1.0,
                             color=YELLOW, buff=0.1, stroke_width=3)

        buffy_lbl = Text("Беленки + тромбоцити <1%",
                         font_size=20, color=BLUE)
        buffy_lbl.move_to(LEFT * 0.5 + DOWN * 0.4)
        buffy_arrow = Arrow(buffy_lbl.get_left(), LEFT * 3.2 + DOWN * 0.4,
                            color=BLUE, buff=0.1, stroke_width=3)

        rbc_lbl = Text("Црвенки ~44%", font_size=22, color=RED, weight=BOLD)
        rbc_lbl.move_to(LEFT * 1.0 + DOWN * 1.6)
        rbc_arrow = Arrow(rbc_lbl.get_left(), LEFT * 3.2 + DOWN * 1.6,
                          color=RED, buff=0.1, stroke_width=3)

        self.play(Create(tube), run_time=0.6)
        self.play(FadeIn(plasma_layer), FadeIn(buffy), FadeIn(rbc_layer),
                  run_time=0.9)
        self.play(GrowArrow(plasma_arrow), FadeIn(plasma_lbl), run_time=0.5)
        self.play(GrowArrow(buffy_arrow), FadeIn(buffy_lbl), run_time=0.5)
        self.play(GrowArrow(rbc_arrow), FadeIn(rbc_lbl), run_time=0.5)

        # right side — total volume
        total = callout("Вкупно ~5 L крв во возрасен човек",
                        width=7.5, border=GREEN, font_size=24)
        total.move_to(RIGHT * 3.5 + DOWN * 2.4)
        self.play(FadeIn(total), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, tube, plasma_layer, buffy, rbc_layer,
                                 plasma_lbl, plasma_arrow,
                                 buffy_lbl, buffy_arrow,
                                 rbc_lbl, rbc_arrow, total)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  PLASMA                                           ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("plasma")

        title = section_title("Плазма — реката", color=ORANGE)
        self.play(Write(title), run_time=0.8)

        # big drop shape
        drop = Ellipse(width=2.8, height=3.0,
                       color=YELLOW, fill_color=YELLOW, fill_opacity=0.5,
                       stroke_color=YELLOW, stroke_width=2)
        drop.move_to(LEFT * 3.5 + DOWN * 0.2)

        # composition list inside
        comp = VGroup(
            Text("90% вода", font_size=22, color=BLUE, weight=BOLD),
            Text("протеини", font_size=20, color=WHITE2),
            Text("соли",     font_size=20, color=WHITE2),
            Text("гликоза",  font_size=20, color=WHITE2),
            Text("хормони",  font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.18)
        comp.move_to(LEFT * 3.5 + DOWN * 0.2)

        # right side — roles
        roles = [
            ("Транспорт", "Носи храна, отпад, хормони.", BLUE),
            ("Топлина",   "Распределува топлина низ телото.", RED),
            ("Притисок",  "Држи волуменот на крвта.", ORANGE),
            ("Имунитет",  "Носи антитела.",             GREEN),
        ]
        cards = VGroup()
        for n, r, col in roles:
            box = RoundedRectangle(
                width=6.0, height=0.7, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            nt = Text(n, font_size=22, color=col, weight=BOLD)
            nt.move_to(box.get_left() + RIGHT * 1.2)
            rt = Text(r, font_size=18, color=WHITE2)
            rt.move_to(box.get_left() + RIGHT * 4.0)
            cards.add(VGroup(box, nt, rt))
        cards.arrange(DOWN, buff=0.18)
        cards.move_to(RIGHT * 3.0 + DOWN * 0.2)

        self.play(Create(drop), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c) for c in comp],
                              lag_ratio=0.15), run_time=1.0)
        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, drop, comp, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  RED BLOOD CELLS                                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rbc")

        title = section_title("Црвенки — носачите на кислород", color=RED)
        self.play(Write(title), run_time=0.8)

        # donut shape — RBC is biconcave
        rbcs = VGroup()
        for x, y in [(-4, 1.0), (-3.5, -0.5), (-4.2, -1.7),
                     (-2.5, 0.5), (-2.8, -1.0)]:
            outer = Circle(radius=0.45, color=RED,
                           fill_color=RED, fill_opacity=0.85,
                           stroke_color=WHITE2, stroke_width=1.5)
            inner = Circle(radius=0.18, color=DARK_CARD,
                           fill_color=DARK_CARD, fill_opacity=1,
                           stroke_width=0)
            outer.move_to(RIGHT * x + UP * y)
            inner.move_to(RIGHT * x + UP * y)
            rbcs.add(VGroup(outer, inner))

        rbcs_lbl = Text("биконкавни — поголема површина",
                        font_size=20, color=YELLOW)
        rbcs_lbl.move_to(LEFT * 3.5 + DOWN * 2.8)

        # facts
        facts = [
            ("Содржат хемоглобин",       "Сврзува кислород.",        RED),
            ("Без јадро",                "Повеќе место за O₂.",      ORANGE),
            ("Живеат ~120 дена",         "Се обновуваат во коски.",  PURPLE),
            ("25 милијарди / литар",     "Огромен број во малку крв.", GREEN),
            ("Хем + железо",             "Без железо — анемија.",    BLUE),
        ]
        cards = VGroup()
        for n, r, col in facts:
            box = RoundedRectangle(
                width=7.0, height=0.6, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            nt = Text(n, font_size=20, color=col, weight=BOLD)
            nt.move_to(box.get_left() + RIGHT * 1.7)
            rt = Text(r, font_size=18, color=WHITE2)
            rt.move_to(box.get_left() + RIGHT * 5.0)
            cards.add(VGroup(box, nt, rt))
        cards.arrange(DOWN, buff=0.15)
        cards.move_to(RIGHT * 2.5 + UP * 0.1)

        self.play(LaggedStart(*[FadeIn(r, scale=0.5) for r in rbcs],
                              lag_ratio=0.1), run_time=1.0)
        self.play(FadeIn(rbcs_lbl), run_time=0.5)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, rbcs, rbcs_lbl, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  WHITE BLOOD CELLS                                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("wbc")

        title = section_title("Беленки — браниците", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # WBC shapes — irregular
        wbcs = VGroup()
        for x, y in [(-3.8, 1.0), (-3.2, -0.7), (-4.4, -1.2)]:
            blob = Circle(radius=0.55, color=BLUE,
                          fill_color=BLUE, fill_opacity=0.4,
                          stroke_color=WHITE2, stroke_width=2)
            nucleus = Circle(radius=0.25, color=PURPLE,
                             fill_color=PURPLE, fill_opacity=0.9,
                             stroke_width=0)
            blob.move_to(RIGHT * x + UP * y)
            nucleus.move_to(RIGHT * x + UP * y)
            wbcs.add(VGroup(blob, nucleus))

        # bacterium being attacked
        bact = Circle(radius=0.25, color=GREEN,
                      fill_color=GREEN, fill_opacity=0.9,
                      stroke_width=1.5)
        bact.move_to(LEFT * 2.0 + DOWN * 0.5)
        bact_lbl = Text("бактерија", font_size=18, color=GREEN)
        bact_lbl.next_to(bact, DOWN, buff=0.15)

        # arrow showing engulfment
        attack = Arrow(LEFT * 3.0 + DOWN * 0.3, LEFT * 2.2 + DOWN * 0.5,
                       color=RED, buff=0.05, stroke_width=3)

        types = [
            ("Фагоцити",   "Голтаат микроби.",                BLUE),
            ("Лимфоцити",  "Произведуваат антитела.",         PURPLE),
            ("Без нив",    "Секоја инфекција би била смртна.", RED),
        ]
        cards = VGroup()
        for n, r, col in types:
            box = RoundedRectangle(
                width=6.5, height=0.7, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            nt = Text(n, font_size=22, color=col, weight=BOLD)
            nt.move_to(box.get_left() + RIGHT * 1.4)
            rt = Text(r, font_size=20, color=WHITE2)
            rt.move_to(box.get_left() + RIGHT * 4.4)
            cards.add(VGroup(box, nt, rt))
        cards.arrange(DOWN, buff=0.2)
        cards.move_to(RIGHT * 3.0 + DOWN * 0.2)

        self.play(LaggedStart(*[FadeIn(w, scale=0.5) for w in wbcs],
                              lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(bact), FadeIn(bact_lbl), run_time=0.5)
        self.play(GrowArrow(attack), run_time=0.5)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.45)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, wbcs, bact, bact_lbl, attack, cards)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  PLATELETS + CLOTTING                             ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("platelets")

        title = section_title("Тромбоцити — лепачи", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        # small purple irregular shapes
        plats = VGroup()
        for x, y in [(-4.2, 1.5), (-3.5, 1.0), (-4.5, 0.4),
                     (-3.0, 0.7), (-3.8, -0.0)]:
            p = RegularPolygon(n=5, color=PURPLE,
                               fill_color=PURPLE, fill_opacity=0.8,
                               stroke_color=WHITE2, stroke_width=1)
            p.scale(0.22).move_to(RIGHT * x + UP * y)
            plats.add(p)

        # wound — red line
        wound = Line(LEFT * 5.5 + DOWN * 1.5,
                     LEFT * 1.5 + DOWN * 1.5,
                     color=RED, stroke_width=5)
        wound_lbl = Text("повреда", font_size=20, color=RED)
        wound_lbl.next_to(wound, DOWN, buff=0.2)

        # clot forming — animate platelets moving to wound
        target_positions = [LEFT * (5.0 - i * 0.7) + DOWN * 1.5
                            for i in range(5)]
        clot_lbl = Text("згрутчување — затвора рана",
                        font_size=22, color=PURPLE, weight=BOLD)
        clot_lbl.move_to(DOWN * 2.5)

        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in plats],
                              lag_ratio=0.1), run_time=0.8)
        self.play(Create(wound), FadeIn(wound_lbl), run_time=0.7)
        self.play(*[p.animate.move_to(t)
                    for p, t in zip(plats, target_positions)],
                  run_time=1.2)
        self.play(FadeIn(clot_lbl), run_time=0.6)

        # right side info
        info = VGroup(
            Text("Не се вистински клетки.",       font_size=22, color=WHITE2),
            Text("Фрагменти од големи клетки.",   font_size=22, color=WHITE2),
            Text("Прв одговор на повреда.",       font_size=22, color=YELLOW, weight=BOLD),
            Text("Без нив — крвавиш до смрт.",    font_size=22, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        info.move_to(RIGHT * 3.0 + UP * 0.5)

        for line in info:
            self.play(FadeIn(line, shift=LEFT * 0.2), run_time=0.45)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, plats, wound, wound_lbl,
                                 clot_lbl, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Плазма — реката што носи сè.",
                 font_size=28, color=ORANGE),
            Text("Црвенки — носат O₂ преку хемоглобин.",
                 font_size=28, color=RED),
            Text("Беленки — го бранат телото од микроби.",
                 font_size=28, color=BLUE),
            Text("Тромбоцити — затвораат рани.",
                 font_size=28, color=PURPLE),
            Text("5 L. Четири состојки. Една приказна.",
                 font_size=30, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(title, DOWN, buff=0.6)

        for b in bullets:
            self.play(Write(b), run_time=0.6)
            self.wait(0.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
