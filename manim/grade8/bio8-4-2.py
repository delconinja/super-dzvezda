"""
bio8-4-2  —  Срце — анатомија и функција
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
heart as relentless protagonist, 100,000 beats per day.
Render:  manim -ql bio8-4-2.py Bio842Scene
Output:  media/videos/bio8-4-2/480p15/Bio842Scene.mp4
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


class Bio842Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — heartbeat                                ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Срцето куца.",
                     font_size=48, color=RED, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)

        # pulsing dot heart
        heart_dot = Circle(radius=0.8, color=RED,
                           fill_color=RED, fill_opacity=0.9,
                           stroke_color=WHITE2, stroke_width=2)
        heart_dot.move_to(ORIGIN + UP * 0.3)

        self.play(Write(hook1), FadeIn(heart_dot), run_time=1.0)
        # three pulses
        for _ in range(3):
            self.play(heart_dot.animate.scale(1.2), run_time=0.25)
            self.play(heart_dot.animate.scale(1 / 1.2), run_time=0.25)

        beats = VGroup(
            Text("100.000 пати на ден.",
                 font_size=34, color=YELLOW, weight=BOLD),
            Text("Без пауза. Без замор. Без награда.",
                 font_size=30, color=ORANGE),
            Text("Сè за тебе.",
                 font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(heart_dot, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, heart_dot, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ANATOMY — 4 CHAMBERS                             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chambers")

        title = section_title("Четири простории")
        self.play(Write(title), run_time=0.8)

        # 4 chambers — atria on top, ventricles below
        ra = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.18,
                              fill_color=BLUE, fill_opacity=0.7,
                              stroke_color=WHITE2, stroke_width=2)
        la = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.18,
                              fill_color=RED, fill_opacity=0.7,
                              stroke_color=WHITE2, stroke_width=2)
        rv = RoundedRectangle(width=1.6, height=1.5, corner_radius=0.18,
                              fill_color=BLUE, fill_opacity=0.85,
                              stroke_color=WHITE2, stroke_width=2)
        lv = RoundedRectangle(width=1.6, height=1.5, corner_radius=0.18,
                              fill_color=RED, fill_opacity=0.85,
                              stroke_color=WHITE2, stroke_width=2)

        ra.move_to(LEFT * 1.0 + UP * 1.0)
        la.move_to(RIGHT * 1.0 + UP * 1.0)
        rv.move_to(LEFT * 1.0 + DOWN * 0.7)
        lv.move_to(RIGHT * 1.0 + DOWN * 0.7)

        # labels inside
        ra_t = Text("ДП", font_size=28, color=WHITE2, weight=BOLD).move_to(ra)
        la_t = Text("ЛП", font_size=28, color=WHITE2, weight=BOLD).move_to(la)
        rv_t = Text("ДК", font_size=30, color=WHITE2, weight=BOLD).move_to(rv)
        lv_t = Text("ЛК", font_size=30, color=WHITE2, weight=BOLD).move_to(lv)

        # outer labels
        ra_l = Text("десна преткомора", font_size=18, color=BLUE).next_to(ra, LEFT, buff=0.2)
        la_l = Text("лева преткомора", font_size=18, color=RED).next_to(la, RIGHT, buff=0.2)
        rv_l = Text("десна комора", font_size=18, color=BLUE).next_to(rv, LEFT, buff=0.2)
        lv_l = Text("лева комора", font_size=18, color=RED).next_to(lv, RIGHT, buff=0.2)

        self.play(Create(ra), Create(la), FadeIn(ra_t), FadeIn(la_t),
                  FadeIn(ra_l), FadeIn(la_l), run_time=0.9)
        self.play(Create(rv), Create(lv), FadeIn(rv_t), FadeIn(lv_t),
                  FadeIn(rv_l), FadeIn(lv_l), run_time=0.9)

        # septum
        septum = Line(UP * 1.6, DOWN * 1.5, color=YELLOW, stroke_width=3)
        sept_lbl = Text("преграда", font_size=18, color=YELLOW).next_to(septum, DOWN, buff=0.15)
        self.play(Create(septum), FadeIn(sept_lbl), run_time=0.6)

        # callout — 2+2
        note = callout("2 преткомори + 2 комори = 4 простории",
                       width=10.0, border=YELLOW, font_size=26)
        note.move_to(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            title, ra, la, rv, lv, ra_t, la_t, rv_t, lv_t,
            ra_l, la_l, rv_l, lv_l, septum, sept_lbl, note)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  VALVES                                           ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("valves")

        title = section_title("Четири залистоци")
        self.play(Write(title), run_time=0.8)

        # simplified heart with valves shown as triangles
        outline = RoundedRectangle(
            width=4.5, height=4.5, corner_radius=0.5,
            fill_color=DARK_CARD, fill_opacity=0.6,
            stroke_color=RED, stroke_width=2)
        outline.move_to(LEFT * 3.5)

        # 4 valve triangles inside
        tri_pos = [
            (LEFT * 4.3 + UP * 0.2, "трикуспидален"),
            (LEFT * 2.7 + UP * 0.2, "бикуспидален"),
            (LEFT * 4.3 + UP * 1.4, "пулмонален"),
            (LEFT * 2.7 + UP * 1.4, "аортен"),
        ]
        valve_colors = [BLUE, RED, PURPLE, ORANGE]
        valves = VGroup()
        for (pos, _), col in zip(tri_pos, valve_colors):
            tri = Triangle(color=col, fill_color=col, fill_opacity=0.85,
                           stroke_color=WHITE2, stroke_width=1.5)
            tri.scale(0.25).move_to(pos)
            valves.add(tri)

        self.play(Create(outline), run_time=0.7)
        self.play(LaggedStart(*[GrowFromCenter(v) for v in valves],
                              lag_ratio=0.15), run_time=1.2)

        # right side — explanation cards
        valve_info = [
            ("Трикуспидален", "ДП → ДК",       BLUE),
            ("Бикуспидален",  "ЛП → ЛК (митрален)", RED),
            ("Пулмонален",    "ДК → бели дробови", PURPLE),
            ("Аортен",        "ЛК → аорта",    ORANGE),
        ]
        cards = VGroup()
        for name, role, col in valve_info:
            box = RoundedRectangle(
                width=6.0, height=0.7, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=22, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.4)
            r = Text(role, font_size=20, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 4.2)
            cards.add(VGroup(box, n, r))
        cards.arrange(DOWN, buff=0.2)
        cards.move_to(RIGHT * 3.0)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.2), run_time=0.4)

        beat = Text("Една насока. Никогаш назад.",
                    font_size=24, color=YELLOW, weight=BOLD)
        beat.move_to(DOWN * 3.0)
        self.play(Write(beat), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, outline, valves, cards, beat)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  CARDIAC CYCLE — SYSTOLE/DIASTOLE                 ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cycle")

        title = section_title("Циклус — систола и дијастола")
        self.play(Write(title), run_time=0.8)

        # animated heart that contracts/relaxes
        heart_shape = Circle(radius=1.2, color=RED,
                             fill_color=RED, fill_opacity=0.7,
                             stroke_color=WHITE2, stroke_width=3)
        heart_shape.move_to(LEFT * 3.5 + UP * 0.3)

        sys_lbl = Text("СИСТОЛА", font_size=28, color=RED, weight=BOLD)
        sys_desc = Text("стискање — крвта излегува",
                        font_size=20, color=WHITE2)
        dia_lbl = Text("ДИЈАСТОЛА", font_size=28, color=BLUE, weight=BOLD)
        dia_desc = Text("опуштање — крвта влегува",
                        font_size=20, color=WHITE2)

        sys_grp = VGroup(sys_lbl, sys_desc).arrange(DOWN, buff=0.2)
        dia_grp = VGroup(dia_lbl, dia_desc).arrange(DOWN, buff=0.2)
        sys_grp.move_to(RIGHT * 3.0 + UP * 1.5)
        dia_grp.move_to(RIGHT * 3.0 + DOWN * 1.0)

        self.play(Create(heart_shape), run_time=0.6)
        self.play(FadeIn(sys_grp), FadeIn(dia_grp), run_time=0.7)

        # cycle 3 times
        for _ in range(3):
            self.play(heart_shape.animate.scale(0.7).set_fill(RED),
                      sys_grp.animate.set_opacity(1.0),
                      dia_grp.animate.set_opacity(0.35),
                      run_time=0.5)
            self.wait(0.2)
            self.play(heart_shape.animate.scale(1 / 0.7).set_fill(BLUE),
                      sys_grp.animate.set_opacity(0.35),
                      dia_grp.animate.set_opacity(1.0),
                      run_time=0.5)
            self.wait(0.2)

        # restore
        self.play(heart_shape.animate.set_fill(RED),
                  sys_grp.animate.set_opacity(1.0),
                  dia_grp.animate.set_opacity(1.0),
                  run_time=0.4)

        cycle_note = callout("Еден циклус ≈ 0.8 секунди",
                             width=8.0, border=YELLOW, font_size=24)
        cycle_note.move_to(DOWN * 3.0)
        self.play(FadeIn(cycle_note), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, heart_shape, sys_grp, dia_grp, cycle_note)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  NUMBERS — beats per day, pumping                 ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("numbers")

        title = section_title("Бројките се неверојатни")
        self.play(Write(title), run_time=0.8)

        stats = [
            ("70 удари / минута",  "Во мирување.",                BLUE),
            ("100.000 удари / ден", "Без пауза. Без замор.",      RED),
            ("5 L крв / минута",    "Толку пумпа во мир.",        ORANGE),
            ("20 L / минута",       "При вежба — четири пати повеќе.", GREEN),
            ("2.500 милиони удари", "Просечен човек, цел живот.", PURPLE),
        ]

        cards = VGroup()
        for big, sub, col in stats:
            box = RoundedRectangle(
                width=11.0, height=0.85, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            b = Text(big, font_size=24, color=col, weight=BOLD)
            b.move_to(box.get_left() + RIGHT * 2.5)
            s = Text(sub, font_size=22, color=WHITE2)
            s.move_to(box.get_left() + RIGHT * 7.5)
            cards.add(VGroup(box, b, s))
        cards.arrange(DOWN, buff=0.18)
        cards.next_to(title, DOWN, buff=0.6)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.45)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  HEART MUSCLE — special                           ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("muscle")

        title = section_title("Срцев мускул — посебен")
        self.play(Write(title), run_time=0.8)

        feats = [
            ("Миокард",      "Мускул што никогаш не се мори.", RED),
            ("Автоматизам",  "Се контрахира сам, без мозок.",  YELLOW),
            ("СА јазол",     "Природен пејсмејкер во десната преткомора.", GREEN),
            ("Сопствена крв","Коронарни артерии го хранат.",   ORANGE),
        ]

        cards = VGroup()
        for name, role, col in feats:
            box = RoundedRectangle(
                width=12.0, height=0.75, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=24, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.7)
            r = Text(role, font_size=22, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 7.0)
            cards.add(VGroup(box, n, r))
        cards.arrange(DOWN, buff=0.2)
        cards.next_to(title, DOWN, buff=0.7)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("4 простории. 4 залистоци.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Систола — стиска. Дијастола — се опушта.",
                 font_size=26, color=BLUE),
            Text("100.000 удари на ден. 5 L во минута.",
                 font_size=28, color=ORANGE),
            Text("Срцето куца. Без награда. Сè за тебе.",
                 font_size=30, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
