"""
bio8-2-7  —  Држечка положба, повреди и здравје на мускули
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
posture as silent damage, body as listening organism.
Render:  manim -ql bio8-2-7.py Bio827Scene
Output:  media/videos/bio8-2-7/480p15/Bio827Scene.mp4
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


def stick_figure_good(pos):
    # Vertical spine
    head = Circle(radius=0.3, color=WHITE2, fill_opacity=0.3, stroke_width=2)
    head.move_to(pos + UP * 2.0)
    # Straight spine
    spine = Line(pos + UP * 1.7, pos + DOWN * 0.5, color=GREEN, stroke_width=5)
    # Shoulders
    sh = Line(pos + UP * 1.5 + LEFT * 0.6, pos + UP * 1.5 + RIGHT * 0.6,
              color=WHITE2, stroke_width=3)
    # Hips
    hip = Line(pos + DOWN * 0.4 + LEFT * 0.5, pos + DOWN * 0.4 + RIGHT * 0.5,
               color=WHITE2, stroke_width=3)
    # Legs
    l_leg = Line(pos + DOWN * 0.4 + LEFT * 0.5, pos + DOWN * 2.3 + LEFT * 0.5,
                 color=WHITE2, stroke_width=3)
    r_leg = Line(pos + DOWN * 0.4 + RIGHT * 0.5, pos + DOWN * 2.3 + RIGHT * 0.5,
                 color=WHITE2, stroke_width=3)
    return VGroup(head, spine, sh, hip, l_leg, r_leg)


def stick_figure_bad(pos):
    # Forward head
    head = Circle(radius=0.3, color=WHITE2, fill_opacity=0.3, stroke_width=2)
    head.move_to(pos + UP * 1.9 + RIGHT * 0.7)
    # Curved spine (hunched)
    spine = CubicBezier(
        pos + UP * 1.7 + RIGHT * 0.5,
        pos + UP * 1.0 + RIGHT * 0.8,
        pos + UP * 0.3 + LEFT * 0.1,
        pos + DOWN * 0.5,
    ).set_color(RED).set_stroke(width=5)
    sh = Line(pos + UP * 1.4 + LEFT * 0.3, pos + UP * 1.4 + RIGHT * 0.9,
              color=WHITE2, stroke_width=3)
    hip = Line(pos + DOWN * 0.4 + LEFT * 0.5, pos + DOWN * 0.4 + RIGHT * 0.5,
               color=WHITE2, stroke_width=3)
    l_leg = Line(pos + DOWN * 0.4 + LEFT * 0.5, pos + DOWN * 2.3 + LEFT * 0.5,
                 color=WHITE2, stroke_width=3)
    r_leg = Line(pos + DOWN * 0.4 + RIGHT * 0.5, pos + DOWN * 2.3 + RIGHT * 0.5,
                 color=WHITE2, stroke_width=3)
    return VGroup(head, spine, sh, hip, l_leg, r_leg)


class Bio827Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — ДРЖИШ ТЕЛЕФОН                            ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Држиш телефон.", font_size=42, color=WHITE2)
        h1.to_edge(UP, buff=0.8)
        self.play(Write(h1), run_time=1.0)
        self.wait(0.25)

        h2 = Text("Свиткана глава.", font_size=40, color=ORANGE)
        h2.next_to(h1, DOWN, buff=0.35)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.25)

        h3 = Text("Цел ден.", font_size=40, color=GREY)
        h3.next_to(h2, DOWN, buff=0.35)
        self.play(Write(h3), run_time=1.0)
        self.wait(0.25)

        h4 = Text("Грбот плаче.", font_size=42, color=RED, weight=BOLD)
        h4.next_to(h3, DOWN, buff=0.35)
        self.play(Write(h4), run_time=1.0)
        self.wait(0.4)

        beats = VGroup(
            Text("Не веднаш.", font_size=32, color=GREY),
            Text("Со години.", font_size=34, color=ORANGE, weight=BOLD),
            Text("Поправи го држењето.", font_size=34, color=GREEN),
            Text("Денеска.", font_size=38, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.25).next_to(h4, DOWN, buff=0.4)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.55)
            self.wait(0.18)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, h2, h3, h4, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ДОБРА vs ЛОША ПОЛОЖБА                           ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("posture")
        title = section_title("Држечка положба")
        self.play(Write(title), run_time=0.8)

        good = stick_figure_good(LEFT * 3.5 + DOWN * 0.2)
        bad = stick_figure_bad(RIGHT * 3.5 + DOWN * 0.2)

        good_lbl = Text("Добра", font_size=28, color=GREEN, weight=BOLD)
        good_lbl.next_to(good, DOWN, buff=0.3)
        bad_lbl = Text("Лоша", font_size=28, color=RED, weight=BOLD)
        bad_lbl.next_to(bad, DOWN, buff=0.3)

        self.play(Create(good), Create(bad), run_time=1.5)
        self.play(Write(good_lbl), Write(bad_lbl), run_time=0.6)
        self.wait(0.4)

        # Tick / cross
        tick = Text("✓", font_size=48, color=GREEN, weight=BOLD)
        tick.next_to(good_lbl, DOWN, buff=0.2)
        cross = Text("✗", font_size=48, color=RED, weight=BOLD)
        cross.next_to(bad_lbl, DOWN, buff=0.2)
        self.play(Write(tick), Write(cross), run_time=0.7)
        self.wait(0.5)

        # Spine alignment text
        info = VGroup(
            Text("Кичма во природна линија.", font_size=22, color=GREEN),
            Text("Глава над рамо. Рамо над колк.", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)

        for line in info:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, good, bad, good_lbl, bad_lbl,
                                 tick, cross, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  ТРИ ВИДА ПОВРЕДИ                                ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("injuries")
        title = section_title("Три видови повреди")
        self.play(Write(title), run_time=0.8)

        # Sprain — ligament
        sp = RoundedRectangle(width=4.0, height=3.2, corner_radius=0.25,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=BLUE, stroke_width=3)
        sp.move_to(LEFT * 4.3)
        sp_t = Text("Истегнување", font_size=24, color=BLUE, weight=BOLD)
        sp_t.move_to(sp.get_top() + DOWN * 0.4)
        sp_what = Text("Лигамент", font_size=20, color=YELLOW)
        sp_what.move_to(sp.get_center() + UP * 0.4)
        sp_desc = VGroup(
            Text("• Натргнат врзивен", font_size=14, color=WHITE2),
            Text("  ткиво помеѓу коски", font_size=14, color=WHITE2),
            Text("• Чест: глужд, колено", font_size=14, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        sp_desc.move_to(sp.get_center() + DOWN * 0.4)

        # Strain — muscle
        st = RoundedRectangle(width=4.0, height=3.2, corner_radius=0.25,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=ORANGE, stroke_width=3)
        st.move_to(ORIGIN)
        st_t = Text("Натегнување", font_size=24, color=ORANGE, weight=BOLD)
        st_t.move_to(st.get_top() + DOWN * 0.4)
        st_what = Text("Мускул / тетива", font_size=20, color=YELLOW)
        st_what.move_to(st.get_center() + UP * 0.4)
        st_desc = VGroup(
            Text("• Растегнати или", font_size=14, color=WHITE2),
            Text("  скинати влакна", font_size=14, color=WHITE2),
            Text("• Чест: грб, нога", font_size=14, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        st_desc.move_to(st.get_center() + DOWN * 0.4)

        # Fracture — bone
        fr = RoundedRectangle(width=4.0, height=3.2, corner_radius=0.25,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=RED, stroke_width=3)
        fr.move_to(RIGHT * 4.3)
        fr_t = Text("Прелом", font_size=24, color=RED, weight=BOLD)
        fr_t.move_to(fr.get_top() + DOWN * 0.4)
        fr_what = Text("Коска", font_size=20, color=YELLOW)
        fr_what.move_to(fr.get_center() + UP * 0.4)
        fr_desc = VGroup(
            Text("• Скршена или", font_size=14, color=WHITE2),
            Text("  напукната", font_size=14, color=WHITE2),
            Text("• Чест: рака, нога", font_size=14, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        fr_desc.move_to(fr.get_center() + DOWN * 0.4)

        for box, t, w, d in [(sp, sp_t, sp_what, sp_desc),
                             (st, st_t, st_what, st_desc),
                             (fr, fr_t, fr_what, fr_desc)]:
            self.play(FadeIn(box, shift=UP * 0.2), run_time=0.55)
            self.play(Write(t), run_time=0.5)
            self.play(FadeIn(w), run_time=0.4)
            self.play(FadeIn(d), run_time=0.5)
            self.wait(0.2)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, sp, st, fr, sp_t, st_t, fr_t,
                                 sp_what, st_what, fr_what,
                                 sp_desc, st_desc, fr_desc)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  RICE МЕТОДОТ                                    ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rice")
        title = section_title("RICE — прва помош")
        self.play(Write(title), run_time=0.8)

        sub = Text("Кога ќе се повредиш — четири чекори.",
                   font_size=22, color=GREY)
        sub.next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(sub), run_time=0.5)

        # R card
        def rice_card(letter, name_mk, desc, color, pos):
            box = RoundedRectangle(width=4.8, height=1.5, corner_radius=0.2,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=color, stroke_width=2)
            box.move_to(pos)
            big = Text(letter, font_size=40, color=color, weight=BOLD)
            big.move_to(box.get_left() + RIGHT * 0.6)
            nm = Text(name_mk, font_size=20, color=YELLOW, weight=BOLD)
            nm.move_to(box.get_center() + UP * 0.2 + RIGHT * 0.6)
            ds = Text(desc, font_size=16, color=WHITE2)
            ds.move_to(box.get_center() + DOWN * 0.25 + RIGHT * 0.6)
            return VGroup(box, big, nm, ds)

        r1 = rice_card("R", "Rest — Одмор",
                       "престани да движиш, дај време", BLUE,
                       LEFT * 2.5 + UP * 1.5)
        r2 = rice_card("I", "Ice — Лед",
                       "20 мин на повредата, намалува оток", PURPLE,
                       RIGHT * 2.5 + UP * 1.5)
        r3 = rice_card("C", "Compression — Притисок",
                       "завој — спречува отекување", ORANGE,
                       LEFT * 2.5 + DOWN * 0.5)
        r4 = rice_card("E", "Elevation — Подигнување",
                       "над срцето — намалува крвоток", GREEN,
                       RIGHT * 2.5 + DOWN * 0.5)

        for card in (r1, r2, r3, r4):
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.55)
            self.wait(0.15)

        self.wait(0.8)

        punch = callout("Прв час — RICE. Потоа — лекар.",
                        width=9.5, bg="#1a3552", border=YELLOW, font_size=26)
        punch.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(punch, shift=UP * 0.2), run_time=0.7)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, sub, r1, r2, r3, r4, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ВЕЖБАЊЕТО ПОМАГА                                ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("exercise")
        title = section_title("Зошто да вежбаш?")
        self.play(Write(title), run_time=0.8)

        def benefit_card(icon, name, desc, color, pos):
            box = RoundedRectangle(width=3.4, height=2.4, corner_radius=0.2,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=color, stroke_width=2)
            box.move_to(pos)
            ic = Text(icon, font_size=36, color=color, weight=BOLD)
            ic.move_to(box.get_center() + UP * 0.6)
            nm = Text(name, font_size=22, color=color, weight=BOLD)
            nm.move_to(box.get_center() + UP * 0.0)
            ds = Text(desc, font_size=14, color=WHITE2)
            ds.move_to(box.get_center() + DOWN * 0.6)
            return VGroup(box, ic, nm, ds)

        b1 = benefit_card("С", "Сила", "мускули растат", RED,
                          LEFT * 4.2 + UP * 0.5)
        b2 = benefit_card("Г", "Гипкост", "зглобови работат", BLUE,
                          ORIGIN + UP * 0.5)
        b3 = benefit_card("К", "Коски",
                          "поцврсти и подебели", GREEN,
                          RIGHT * 4.2 + UP * 0.5)

        # Second row
        b4 = benefit_card("Р", "Рамнотежа", "помалку паѓања", ORANGE,
                          LEFT * 2.5 + DOWN * 2.0)
        b5 = benefit_card("Е", "Енергија", "будно тело и ум", PURPLE,
                          RIGHT * 2.5 + DOWN * 2.0)

        for c in (b1, b2, b3, b4, b5):
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.5)
            self.wait(0.12)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, b1, b2, b3, b4, b5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  СОВЕТИ ЗА ЗДРАВЈЕ                               ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("tips")
        title = section_title("Совети за здрав скелет")
        self.play(Write(title), run_time=0.8)

        tips = VGroup(
            callout("Седи исправено — грбот да биде во природна линија",
                    width=11.0, bg="#1a3552", border=BLUE, font_size=22),
            callout("Користи и двете рамена за ранец",
                    width=11.0, bg="#1a3552", border=GREEN, font_size=22),
            callout("Раздвижи се на секои 30 минути од седење",
                    width=11.0, bg="#1a3552", border=ORANGE, font_size=22),
            callout("Спиј 8–10 часа — коските растат во сон",
                    width=11.0, bg="#1a3552", border=PURPLE, font_size=22),
            callout("Јади калциум — млеко, сирење, риба",
                    width=11.0, bg="#1a3552", border=YELLOW, font_size=22),
            callout("Сонце — за витамин Д",
                    width=11.0, bg="#1a3552", border=RED, font_size=22),
        ).arrange(DOWN, buff=0.18).move_to(ORIGIN)

        for t in tips:
            self.play(FadeIn(t, shift=UP * 0.1), run_time=0.45)
            self.wait(0.1)

        self.wait(2.0)
        self.play(FadeOut(VGroup(title, tips)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Држи се исправено.", font_size=42, color=BLUE, weight=BOLD),
            Text("Движи се секој ден.", font_size=42, color=GREEN, weight=BOLD),
            Text("Слушај го телото.", font_size=42, color=ORANGE, weight=BOLD),
            Text("Тоа е твој дом.", font_size=46, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
