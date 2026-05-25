"""
geo8-2-3  —  Македонија во европските интеграции
Географија 8, Единица 2: Европа како општествена целина

Teaching narrative — Andonovski-style: three-beat punches,
Macedonia as a patient traveller, EU as a long road,
NATO as an open door already crossed.
Render:  manim -ql geo8-2-3.py Geo823Scene
Output:  media/videos/geo8-2-3/480p15/Geo823Scene.mp4
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


def milestone(year, label, color, pos):
    dot = Dot(point=pos, radius=0.18, color=color)
    yr = Text(year, font_size=22, color=color, weight=BOLD)
    yr.next_to(dot, UP, buff=0.25)
    lb = Text(label, font_size=16, color=WHITE2)
    lb.next_to(dot, DOWN, buff=0.25)
    return VGroup(dot, yr, lb)


def chapter_card(num, name, color, pos):
    box = RoundedRectangle(width=2.6, height=1.1, corner_radius=0.2,
                           fill_color=DARK_CARD, fill_opacity=1,
                           stroke_color=color, stroke_width=2)
    box.move_to(pos)
    n = Text(num, font_size=22, color=color, weight=BOLD)
    n.move_to(box.get_center() + UP * 0.25)
    nm = Text(name, font_size=14, color=WHITE2)
    nm.move_to(box.get_center() + DOWN * 0.25)
    return VGroup(box, n, nm)


class Geo823Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Македонија чека.", font_size=50, color=YELLOW, weight=BOLD)
        h2 = Text("На вратата на Европа.", font_size=38, color=WHITE2)
        h3 = Text("Долго.", font_size=42, color=GREY, weight=BOLD)
        h4 = Text("Кандидат од 2005.", font_size=34, color=BLUE)
        h5 = Text("Патот не е лесен.", font_size=34, color=ORANGE)
        h6 = Text("Но не и невозможен.", font_size=42, color=GREEN, weight=BOLD)

        beats = VGroup(h1, h2, h3, h4, h5, h6).arrange(DOWN, buff=0.3)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.65)
            self.wait(0.18)

        self.wait(1.2)
        self.play(FadeOut(beats), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  TIMELINE                                        ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("timeline")

        st2 = section_title("Патот кон Европа")
        self.play(Write(st2), run_time=0.8)

        # Timeline arrow
        line = Arrow(LEFT * 5.5, RIGHT * 5.5, color=GREY, stroke_width=3, buff=0)
        line.move_to(DOWN * 0.3)
        self.play(GrowArrow(line), run_time=1.0)

        m1 = milestone("1991", "Независност",          GREEN,  np.array([-5.0, -0.3, 0]))
        m2 = milestone("2001", "Спогодба за\nстабилизација", BLUE,   np.array([-2.5, -0.3, 0]))
        m3 = milestone("2005", "Статус на\nкандидат",  YELLOW, np.array([0.0,  -0.3, 0]))
        m4 = milestone("2020", "НАТО — членка",        ORANGE, np.array([2.5,  -0.3, 0]))
        m5 = milestone("2022", "Старт на\nпреговори",  PURPLE, np.array([5.0,  -0.3, 0]))

        for m in (m1, m2, m3, m4, m5):
            self.play(FadeIn(m, scale=0.7), run_time=0.55)
            self.wait(0.15)

        self.wait(0.6)

        wait_note = Text("Помеѓу 2005 и 2022 — седумнаесет години чекање.",
                         font_size=22, color=GREY)
        wait_note.to_edge(DOWN, buff=0.4)
        self.play(Write(wait_note), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st2, line, m1, m2, m3, m4, m5, wait_note)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  CHAPTERS OF NEGOTIATION                         ~65 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chapters")

        st3 = section_title("Поглавјата за преговори")
        self.play(Write(st3), run_time=0.8)

        intro3 = Text("35 поглавја. 35 врати. Секоја се отвора посебно.",
                      font_size=24, color=WHITE2)
        intro3.next_to(st3, DOWN, buff=0.4)
        self.play(FadeIn(intro3, shift=UP * 0.2), run_time=0.8)
        self.wait(0.4)

        # Show 6 example chapters
        c1 = chapter_card("1", "Слободно движење\nна стоки", BLUE,
                          np.array([-4.5, 0.7, 0]))
        c2 = chapter_card("4", "Слободно движење\nна капитал", GREEN,
                          np.array([-1.5, 0.7, 0]))
        c3 = chapter_card("23", "Правосудство\nи права", YELLOW,
                          np.array([1.5, 0.7, 0]))
        c4 = chapter_card("24", "Слобода\nи безбедност", ORANGE,
                          np.array([4.5, 0.7, 0]))
        c5 = chapter_card("27", "Животна\nсредина", PURPLE,
                          np.array([-3.0, -0.9, 0]))
        c6 = chapter_card("32", "Финансиска\nконтрола", RED,
                          np.array([0.0, -0.9, 0]))
        c7 = chapter_card("...", "и уште 29\nпоглавја", GREY,
                          np.array([3.0, -0.9, 0]))

        cards = VGroup(c1, c2, c3, c4, c5, c6, c7)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.4)
            self.wait(0.08)

        self.wait(0.6)

        close3 = Text("Секое поглавје — реформа. Секоја реформа — чекор.",
                      font_size=22, color=YELLOW)
        close3.to_edge(DOWN, buff=0.35)
        self.play(Write(close3), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st3, intro3, cards, close3)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  BENEFITS vs CHALLENGES                          ~75 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pros_cons")

        st4 = section_title("Што добиваме, што даваме")
        self.play(Write(st4), run_time=0.8)

        # Left column — benefits
        pros_box = RoundedRectangle(width=5.7, height=4.3, corner_radius=0.3,
                                    fill_color="#0d2b44", fill_opacity=1,
                                    stroke_color=GREEN, stroke_width=2)
        pros_box.move_to(LEFT * 3.3 + DOWN * 0.4)
        pros_t = Text("Корист", font_size=28, color=GREEN, weight=BOLD)
        pros_t.move_to(pros_box.get_top() + DOWN * 0.4)

        cons_box = RoundedRectangle(width=5.7, height=4.3, corner_radius=0.3,
                                    fill_color="#2b1f0d", fill_opacity=1,
                                    stroke_color=ORANGE, stroke_width=2)
        cons_box.move_to(RIGHT * 3.3 + DOWN * 0.4)
        cons_t = Text("Предизвик", font_size=28, color=ORANGE, weight=BOLD)
        cons_t.move_to(cons_box.get_top() + DOWN * 0.4)

        self.play(Create(pros_box), Create(cons_box),
                  Write(pros_t), Write(cons_t), run_time=0.9)

        pros_items = VGroup(
            Text("• трговија без бариери", font_size=19, color=WHITE2),
            Text("• мобилност на луѓе", font_size=19, color=WHITE2),
            Text("• европски фондови", font_size=19, color=WHITE2),
            Text("• владеење на правото", font_size=19, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        pros_items.next_to(pros_t, DOWN, buff=0.4).shift(LEFT * 0.4)

        cons_items = VGroup(
            Text("• строги реформи", font_size=19, color=WHITE2),
            Text("• усогласување закони", font_size=19, color=WHITE2),
            Text("• политички спорови", font_size=19, color=WHITE2),
            Text("• бавен ритам", font_size=19, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        cons_items.next_to(cons_t, DOWN, buff=0.4).shift(LEFT * 0.4)

        for p, c in zip(pros_items, cons_items):
            self.play(FadeIn(p, shift=RIGHT * 0.2),
                      FadeIn(c, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.12)

        self.wait(0.8)

        close4 = Text("Не подарок. Туку договор.", font_size=24, color=YELLOW)
        close4.to_edge(DOWN, buff=0.3)
        self.play(Write(close4), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(st4, pros_box, cons_box, pros_t, cons_t,
                                  pros_items, cons_items, close4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  NATO MEMBERSHIP 2020                            ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("nato")

        st5 = section_title("НАТО — 2020", color=BLUE)
        self.play(Write(st5), run_time=0.8)

        intro5 = Text("Една врата веќе е минатата.", font_size=28, color=WHITE2)
        intro5.next_to(st5, DOWN, buff=0.5)
        self.play(FadeIn(intro5, shift=UP * 0.2), run_time=0.8)
        self.wait(0.4)

        # NATO shield
        shield = RegularPolygon(n=6, color=BLUE, fill_color="#0d2b44",
                                fill_opacity=1, stroke_width=3)
        shield.scale(1.6).move_to(LEFT * 3.5 + DOWN * 0.5)
        nato_t = Text("НАТО", font_size=32, color=YELLOW, weight=BOLD).move_to(shield)
        date_t = Text("27 март 2020", font_size=18, color=WHITE2)
        date_t.next_to(shield, DOWN, buff=0.3)

        self.play(Create(shield), Write(nato_t), run_time=0.9)
        self.play(FadeIn(date_t), run_time=0.5)

        info = VGroup(
            Text("30-та земја-членка", font_size=24, color=BLUE, weight=BOLD),
            Text("Колективна одбрана.", font_size=22, color=WHITE2),
            Text("Член 5 — еден за сите,", font_size=20, color=GREY),
            Text("сите за еден.", font_size=20, color=GREY),
            Text("Сигурност — гарантирана.", font_size=22, color=GREEN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        info.move_to(RIGHT * 2.2 + DOWN * 0.4)

        for ln in info:
            self.play(FadeIn(ln, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.12)

        self.wait(1.2)
        self.play(FadeOut(VGroup(st5, intro5, shield, nato_t, date_t, info)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CLOSING                                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final_lines = VGroup(
            Text("Една врата — отворена.", font_size=36, color=BLUE, weight=BOLD),
            Text("Друга — се отвора.", font_size=32, color=YELLOW),
            Text("Македонија — на патот.", font_size=32, color=WHITE2),
            Text("Не сама. Туку со Европа.", font_size=36, color=GREEN, weight=BOLD),
            Text("Чекор по чекор.", font_size=40, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for ln in final_lines:
            self.play(Write(ln), run_time=0.75)
            self.wait(0.22)

        self.wait(2.5)
        self.play(FadeOut(final_lines), run_time=1.2)
        self.wait(0.4)
