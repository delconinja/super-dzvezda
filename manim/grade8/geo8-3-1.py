"""
geo8-3-1  —  Балкански Полуостров
Географија 8, Единица 3: Јужна Европа

Teaching narrative — Andonovski-style: three-beat punches,
countries as characters, peninsulas as branches of land.
Render:  manim -ql geo8-3-1.py Geo831Scene
Output:  media/videos/geo8-3-1/480p15/Geo831Scene.mp4
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


def country_card(name, color, pos, w=1.8, h=1.0, fs=20):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.15,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=fs, color=color, weight=BOLD)
    nm.move_to(box)
    return VGroup(box, nm)


class Geo831Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — "Балкан е мал, но густ"                ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Балкан е мал.", font_size=58, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Но густ.", font_size=44, color=ORANGE, weight=BOLD),
            Text("Десет држави во простор колку Франција.", font_size=32, color=WHITE2),
            Text("Различни јазици.", font_size=34, color=BLUE),
            Text("Различни вери.", font_size=34, color=PURPLE),
            Text("Едно исто соседство.", font_size=40, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.32).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHERE — peninsula shape                         ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("where")

        t2 = section_title("Каде се наоѓа?")
        self.play(Write(t2), run_time=0.8)

        # rough peninsula silhouette
        pen = Polygon(
            [-2.5,  2.3, 0],
            [ 2.3,  2.3, 0],
            [ 2.8,  1.0, 0],
            [ 2.2, -0.5, 0],
            [ 1.4, -1.8, 0],
            [ 0.2, -2.5, 0],
            [-1.0, -2.0, 0],
            [-1.8, -0.8, 0],
            [-2.6,  0.6, 0],
            fill_color="#2d5a4a", fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=3,
        ).shift(LEFT * 3)

        sea_l = Text("Јадранско\nморе", font_size=18, color=BLUE, weight=BOLD)
        sea_l.next_to(pen, LEFT, buff=0.2)
        sea_r = Text("Црно\nморе", font_size=18, color=BLUE, weight=BOLD)
        sea_r.next_to(pen, RIGHT, buff=0.2)
        sea_d = Text("Егејско\nморе", font_size=18, color=BLUE, weight=BOLD)
        sea_d.next_to(pen, DOWN, buff=0.15)

        self.play(FadeIn(pen), run_time=1.0)
        self.play(FadeIn(sea_l), FadeIn(sea_r), FadeIn(sea_d), run_time=0.8)

        info = VGroup(
            Text("Балканот гледа на три мориња.", font_size=26, color=WHITE2),
            Text("Север — Дунав го дели.", font_size=24, color=GREY),
            Text("Југ — Средоземјето го мие.", font_size=24, color=GREY),
            Text("Запад — Алпите го затвораат.", font_size=24, color=GREY),
            Text("Исток — Турција го продолжува.", font_size=24, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).shift(RIGHT * 2.8)

        for line in info:
            self.play(FadeIn(line, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.12)

        self.wait(0.8)
        self.play(FadeOut(VGroup(t2, pen, sea_l, sea_r, sea_d, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  TEN COUNTRIES                                   ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("countries")

        t3 = section_title("Десет држави. Едно соседство.")
        self.play(Write(t3), run_time=0.8)

        # positions roughly mirror Balkan geography
        countries = [
            ("Словенија",    PURPLE,  [-5.0,  2.0, 0]),
            ("Хрватска",     ORANGE,  [-3.5,  1.5, 0]),
            ("БиХ",          GREEN,   [-2.5,  0.3, 0]),
            ("Србија",       BLUE,    [-0.8,  1.0, 0]),
            ("Романија",     RED,     [ 1.5,  2.2, 0]),
            ("Бугарија",     YELLOW,  [ 2.0,  0.6, 0]),
            ("Црна Гора",    GREY,    [-2.0, -1.0, 0]),
            ("Косово",       PURPLE,  [-0.5, -0.3, 0]),
            ("Албанија",     RED,     [-1.5, -2.0, 0]),
            ("С. Македонија",GREEN,   [ 0.2, -1.8, 0]),
            ("Грција",       BLUE,    [ 1.5, -2.5, 0]),
            ("Турција (дел)",ORANGE,  [ 4.0, -1.0, 0]),
        ]

        cards = VGroup()
        for name, col, pos in countries:
            w = 2.0 if len(name) > 8 else 1.7
            c = country_card(name, col, pos, w=w, h=0.7, fs=16)
            cards.add(c)

        for c in cards:
            self.play(FadeIn(c, scale=0.8), run_time=0.25)

        self.wait(1.0)

        cnt = Text("12 држави. Една приказна.", font_size=28, color=YELLOW, weight=BOLD)
        cnt.to_edge(DOWN, buff=0.5)
        self.play(Write(cnt), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t3, cards, cnt)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  MOUNTAINS — relief                              ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mountains")

        t4 = section_title("Планини насекаде.")
        self.play(Write(t4), run_time=0.8)

        # zig-zag mountains
        mtns = VMobject(color=GREY, stroke_width=3)
        pts = [[-6,-1,0],[-5,1,0],[-4,-0.5,0],[-3,1.5,0],[-2,0,0],
               [-1,2,0],[0,0.5,0],[1,1.8,0],[2,-0.2,0],[3,1.6,0],
               [4,0.3,0],[5,1.2,0],[6,-1,0]]
        mtns.set_points_as_corners(pts)
        mtns.shift(UP * 0.3)
        self.play(Create(mtns), run_time=2.0)

        # peak labels
        peaks = [
            ("Динариди",  [-3.5, 2.0, 0], ORANGE),
            ("Шар",       [-0.8, 2.5, 0], YELLOW),
            ("Пинд",      [ 1.2, 2.3, 0], GREEN),
            ("Стара пл.", [ 3.5, 2.1, 0], BLUE),
        ]
        peak_labs = VGroup()
        for nm, pos, col in peaks:
            lab = Text(nm, font_size=18, color=col, weight=BOLD)
            lab.move_to(pos)
            peak_labs.add(lab)
            self.play(FadeIn(lab), run_time=0.4)

        self.wait(0.5)

        facts = VGroup(
            Text("Планините ги делат луѓето.", font_size=24, color=WHITE2),
            Text("Долините ги поврзуваат.", font_size=24, color=GREEN),
            Text("Реките течат меѓу.", font_size=24, color=BLUE),
            Text("Морето ги доловува.", font_size=24, color=PURPLE),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.6)

        for f in facts:
            self.play(FadeIn(f, shift=UP*0.15), run_time=0.5)
            self.wait(0.15)

        self.wait(0.8)
        self.play(FadeOut(VGroup(t4, mtns, peak_labs, facts)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  LANGUAGES & RELIGIONS                           ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("diversity")

        t5 = section_title("Многу јазици. Многу вери.")
        self.play(Write(t5), run_time=0.8)

        # Two columns: languages and religions
        lang_hdr = Text("Јазици", font_size=30, color=BLUE, weight=BOLD)
        lang_hdr.move_to([-3.5, 1.8, 0])
        self.play(Write(lang_hdr), run_time=0.5)

        langs = VGroup(
            Text("• Македонски", font_size=22, color=WHITE2),
            Text("• Српски", font_size=22, color=WHITE2),
            Text("• Хрватски", font_size=22, color=WHITE2),
            Text("• Бугарски", font_size=22, color=WHITE2),
            Text("• Грчки", font_size=22, color=WHITE2),
            Text("• Албански", font_size=22, color=WHITE2),
            Text("• Романски", font_size=22, color=WHITE2),
            Text("• Турски", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        langs.next_to(lang_hdr, DOWN, buff=0.3).align_to(lang_hdr, LEFT)

        for L in langs:
            self.play(FadeIn(L, shift=RIGHT*0.15), run_time=0.22)

        rel_hdr = Text("Вери", font_size=30, color=PURPLE, weight=BOLD)
        rel_hdr.move_to([2.5, 1.8, 0])
        self.play(Write(rel_hdr), run_time=0.5)

        rels = VGroup(
            Text("• Православие", font_size=22, color=WHITE2),
            Text("• Католицизам", font_size=22, color=WHITE2),
            Text("• Ислам", font_size=22, color=WHITE2),
            Text("• Јудаизам", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        rels.next_to(rel_hdr, DOWN, buff=0.3).align_to(rel_hdr, LEFT)

        for R in rels:
            self.play(FadeIn(R, shift=RIGHT*0.15), run_time=0.3)

        self.wait(1.0)

        msg = callout("Различни. Но сите свои.", width=8.0, border=YELLOW)
        msg.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg, shift=UP*0.2), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, lang_hdr, langs, rel_hdr, rels, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  HISTORY — конфликти и соработка                ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("history")

        t6 = section_title("Историја: рани и лекови.")
        self.play(Write(t6), run_time=0.8)

        # Timeline
        tl = Line([-5.5, 0, 0], [5.5, 0, 0], color=GREY, stroke_width=3)
        self.play(Create(tl), run_time=0.8)

        events = [
            (-4.5,  "Османлии",       "500 години", ORANGE, UP),
            (-2.0,  "Балкански\nвојни","1912-13",   RED,    DOWN),
            ( 0.0,  "I и II\nсв. војна","1914-1945", RED,    UP),
            ( 2.2,  "Југославија",    "1945-1991", BLUE,    DOWN),
            ( 4.5,  "ЕУ и НАТО",      "денес",     GREEN,   UP),
        ]
        for x, ev, dt, col, dr in events:
            dot = Dot([x, 0, 0], radius=0.12, color=col)
            ev_t = Text(ev, font_size=18, color=col, weight=BOLD)
            dt_t = Text(dt, font_size=14, color=GREY)
            if (dr == UP).all():
                ev_t.next_to(dot, UP, buff=0.3)
                dt_t.next_to(ev_t, UP, buff=0.1)
            else:
                ev_t.next_to(dot, DOWN, buff=0.3)
                dt_t.next_to(ev_t, DOWN, buff=0.1)
            self.play(FadeIn(dot), Write(ev_t), Write(dt_t), run_time=0.6)

        self.wait(0.8)

        closing = VGroup(
            Text("Војувале. Помируваат.", font_size=26, color=WHITE2),
            Text("Се делеле. Се поврзуваат.", font_size=26, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.5)

        for c in closing:
            self.play(FadeIn(c, shift=UP*0.15), run_time=0.6)
            self.wait(0.2)

        self.wait(1.2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        end1 = Text("Балканот.", font_size=64, color=YELLOW, weight=BOLD)
        end1.move_to(UP * 1.6)
        self.play(Write(end1), run_time=1.0)

        end_lines = VGroup(
            Text("Мал по површина.", font_size=32, color=WHITE2),
            Text("Голем по приказни.", font_size=32, color=ORANGE),
            Text("Сложен. Жив. Наш.", font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(end1, DOWN, buff=0.5)

        for L in end_lines:
            self.play(FadeIn(L, shift=UP*0.15), run_time=0.7)
            self.wait(0.2)

        self.wait(2.0)
