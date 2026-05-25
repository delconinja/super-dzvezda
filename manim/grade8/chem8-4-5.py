"""
chem8-4-5  —  Универзален индикатор и pH скала
Хемија 8, Единица 4: Киселини, бази и соли

Teaching narrative — Andonovski-style: three-beat punches,
indicator as truth-teller, personification, one-word finishers.
Render:  manim -ql chem8-4-5.py Chem845Scene
Output:  media/videos/chem8-4-5/480p15/Chem845Scene.mp4
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


class Chem845Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Универзалниот индикатор не лаже.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.6)
        self.wait(0.5)

        beats = VGroup(
            Text("Црвен — кисело.", font_size=34, color=RED, weight=BOLD),
            Text("Сино — базно.",   font_size=34, color=BLUE, weight=BOLD),
            Text("Зелено — неутрално.", font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
            self.wait(0.25)
        self.wait(0.5)

        drop = Text("Една капка.", font_size=32, color=WHITE2).to_edge(DOWN, buff=1.2)
        truth = Text("Цела вистина.", font_size=38, color=ORANGE, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(drop), run_time=0.9)
        self.play(FadeIn(truth, shift=UP*0.2), run_time=0.8)
        self.wait(0.9)

        self.play(FadeOut(VGroup(hook1, beats, drop, truth)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е ИНДИКАТОР                                 ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("indicator")

        t2 = section_title("Што е индикатор?")
        self.play(Write(t2), run_time=0.8)

        defn = callout("Индикатор — супстанца што менува боја според pH.",
                       width=12.0, font_size=28)
        defn.next_to(t2, DOWN, buff=0.4)
        self.play(FadeIn(defn, shift=UP*0.2), run_time=0.9)
        self.wait(0.5)

        # Three test tubes: red, green, blue
        def tube(color, label_text):
            body = RoundedRectangle(width=0.9, height=2.6, corner_radius=0.4,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=WHITE2, stroke_width=2)
            liquid = RoundedRectangle(width=0.78, height=1.8, corner_radius=0.35,
                                      fill_color=color, fill_opacity=0.85,
                                      stroke_opacity=0)
            liquid.move_to(body.get_bottom() + UP*1.0)
            lbl = Text(label_text, font_size=22, color=WHITE2)
            lbl.next_to(body, DOWN, buff=0.25)
            return VGroup(body, liquid, lbl)

        t_red   = tube(RED, "кисело")
        t_green = tube(GREEN, "неутрално")
        t_blue  = tube(BLUE, "базно")
        tubes = VGroup(t_red, t_green, t_blue).arrange(RIGHT, buff=1.2).shift(DOWN*0.5)

        for t in tubes:
            self.play(FadeIn(t, shift=UP*0.2), run_time=0.55)
        self.wait(1.0)

        small = Text("Бојата зборува.", font_size=26, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(small), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t2, defn, tubes, small)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  pH СКАЛА 0–14                                   ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ph_scale")

        t3 = section_title("pH скала: 0 до 14")
        self.play(Write(t3), run_time=0.8)

        # Build colored bar
        colors_ph = [
            "#d32f2f",  # 0  red
            "#e53935",  # 1
            "#ef5350",  # 2
            "#ff7043",  # 3  orange-red
            "#ff9800",  # 4
            "#ffb74d",  # 5  orange
            "#ffd54f",  # 6  yellow
            "#81c784",  # 7  green (neutral)
            "#4db6ac",  # 8
            "#26a69a",  # 9  teal
            "#42a5f5",  # 10
            "#1e88e5",  # 11 blue
            "#5e35b1",  # 12
            "#7b1fa2",  # 13 purple
            "#4a148c",  # 14 deep purple
        ]
        cells = VGroup()
        cell_w = 0.75
        for i, col in enumerate(colors_ph):
            sq = Square(side_length=cell_w, fill_color=col, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=1.0)
            sq.shift(RIGHT*(i - 7)*cell_w)
            num = Text(str(i), font_size=18, color=WHITE2 if i not in (7,) else "#0d1b2e", weight=BOLD)
            num.move_to(sq)
            cells.add(VGroup(sq, num))
        cells.shift(UP*0.3)

        self.play(LaggedStartMap(FadeIn, cells, lag_ratio=0.06), run_time=2.2)

        # Region labels
        acid_lbl = Text("кисело (0–6)", font_size=22, color=RED, weight=BOLD)
        acid_lbl.next_to(cells[0], DOWN, buff=0.35).shift(RIGHT*1.5)
        neutral_lbl = Text("неутрално (7)", font_size=22, color=GREEN, weight=BOLD)
        neutral_lbl.next_to(cells[7], DOWN, buff=0.35)
        base_lbl = Text("базно (8–14)", font_size=22, color=BLUE, weight=BOLD)
        base_lbl.next_to(cells[14], DOWN, buff=0.35).shift(LEFT*1.5)

        self.play(Write(acid_lbl), Write(neutral_lbl), Write(base_lbl), run_time=1.0)
        self.wait(0.6)

        # Arrow on 7
        arr = Arrow(cells[7].get_top()+UP*0.7, cells[7].get_top()+UP*0.05,
                    color=GREEN, stroke_width=4, buff=0.05)
        seven = Text("седум е граница", font_size=22, color=GREEN).next_to(arr, UP, buff=0.1)
        self.play(GrowArrow(arr), Write(seven), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(arr, seven)), run_time=0.5)

        beats3 = VGroup(
            Text("Помало од 7 — киселина.", font_size=26, color=RED),
            Text("Точно 7 — вода.",         font_size=26, color=GREEN),
            Text("Повеќе од 7 — база.",     font_size=26, color=BLUE),
        ).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=0.35)
        for b in beats3:
            self.play(FadeIn(b, shift=UP*0.15), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(t3, cells, acid_lbl, neutral_lbl, base_lbl, beats3)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ОБИЧНИ СУПСТАНЦИ НА СКАЛАТА                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("substances")

        t4 = section_title("Каде се секојдневните работи?")
        self.play(Write(t4), run_time=0.8)

        # Long horizontal bar
        bar = VGroup()
        bw = 0.65
        for i, col in enumerate(colors_ph):
            sq = Square(side_length=bw, fill_color=col, fill_opacity=1,
                        stroke_color=WHITE2, stroke_width=0.8)
            sq.shift(RIGHT*(i - 7)*bw)
            n = Text(str(i), font_size=14, color=WHITE2 if i != 7 else "#0d1b2e", weight=BOLD)
            n.move_to(sq)
            bar.add(VGroup(sq, n))
        bar.shift(UP*0.1)

        self.play(FadeIn(bar), run_time=0.8)

        # Markers
        def marker(idx, label, color=WHITE2, up=True):
            target = bar[idx][0]
            direction = UP if up else DOWN
            tick = Line(target.get_edge_center(direction),
                        target.get_edge_center(direction) + direction*0.35,
                        color=color, stroke_width=2.5)
            txt = Text(label, font_size=18, color=color, weight=BOLD)
            txt.next_to(tick, direction, buff=0.08)
            return VGroup(tick, txt)

        m_lemon = marker(2,  "лимон", RED, up=True)
        m_water = marker(7,  "вода", GREEN, up=True)
        m_soap  = marker(9,  "сапун", BLUE, up=True)
        m_bleach = marker(13, "белило", PURPLE, up=True)

        m_vinegar = marker(3, "сирче", ORANGE, up=False)
        m_milk    = marker(6, "млеко", YELLOW, up=False)
        m_blood   = marker(7, "крв ~7.4", "#4db6ac", up=False)
        m_soda    = marker(11, "сода", BLUE, up=False)

        for m in (m_lemon, m_water, m_soap, m_bleach):
            self.play(FadeIn(m, shift=DOWN*0.1), run_time=0.45)
        for m in (m_vinegar, m_milk, m_blood, m_soda):
            self.play(FadeIn(m, shift=UP*0.1), run_time=0.45)
        self.wait(1.2)

        c4 = callout("Кујна, бања, тело — секаде pH си игра.",
                     width=11.5, font_size=26, border=ORANGE)
        c4.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(c4, shift=UP*0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, bar, m_lemon, m_water, m_soap, m_bleach,
                                  m_vinegar, m_milk, m_blood, m_soda, c4)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ЛАКМУСОВА ХАРТИЈА                               ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("litmus")

        t5 = section_title("Лакмусова хартија")
        self.play(Write(t5), run_time=0.8)

        intro = callout("Едноставен тест: натопи — гледај боја.",
                        width=11.0, font_size=26)
        intro.next_to(t5, DOWN, buff=0.4)
        self.play(FadeIn(intro, shift=UP*0.2), run_time=0.8)

        # Two strips before/after
        def strip(color):
            s = RoundedRectangle(width=0.45, height=2.4, corner_radius=0.1,
                                 fill_color=color, fill_opacity=1,
                                 stroke_color=WHITE2, stroke_width=1.2)
            return s

        # Blue strip → red in acid
        s1_before = strip(BLUE).shift(LEFT*4.5 + DOWN*0.5)
        s1_after  = strip(RED).shift(LEFT*2.2 + DOWN*0.5)
        arr1 = Arrow(s1_before.get_right()+RIGHT*0.1,
                     s1_after.get_left()+LEFT*0.1,
                     color=YELLOW, buff=0.05, stroke_width=3)
        lbl1 = Text("кислина", font_size=22, color=RED).next_to(arr1, UP, buff=0.1)
        cap1 = Text("сино → црвено", font_size=20, color=WHITE2).next_to(
            VGroup(s1_before, s1_after), DOWN, buff=0.3)

        # Red strip → blue in base
        s2_before = strip(RED).shift(RIGHT*2.2 + DOWN*0.5)
        s2_after  = strip(BLUE).shift(RIGHT*4.5 + DOWN*0.5)
        arr2 = Arrow(s2_before.get_right()+RIGHT*0.1,
                     s2_after.get_left()+LEFT*0.1,
                     color=YELLOW, buff=0.05, stroke_width=3)
        lbl2 = Text("база", font_size=22, color=BLUE).next_to(arr2, UP, buff=0.1)
        cap2 = Text("црвено → сино", font_size=20, color=WHITE2).next_to(
            VGroup(s2_before, s2_after), DOWN, buff=0.3)

        self.play(FadeIn(s1_before), FadeIn(s2_before), run_time=0.7)
        self.play(GrowArrow(arr1), GrowArrow(arr2),
                  Write(lbl1), Write(lbl2), run_time=0.8)
        self.play(FadeIn(s1_after), FadeIn(s2_after), run_time=0.7)
        self.play(Write(cap1), Write(cap2), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, intro, s1_before, s1_after, arr1, lbl1, cap1,
                                  s2_before, s2_after, arr2, lbl2, cap2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  CLOSER                                          ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Бројки не лажат.", font_size=42,
                      color=YELLOW, weight=BOLD)
        close1.move_to(UP*0.7)
        self.play(Write(close1), run_time=1.0)
        self.wait(0.4)

        close2 = Text("Боите не лажат.", font_size=42,
                      color=BLUE, weight=BOLD)
        close2.move_to(ORIGIN)
        self.play(Write(close2), run_time=1.0)
        self.wait(0.4)

        close3 = Text("Хемијата зборува со светлина.", font_size=38,
                      color=GREEN, weight=BOLD)
        close3.move_to(DOWN*0.8)
        self.play(Write(close3), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(close1, close2, close3)), run_time=0.7)
        self.wait(0.3)
