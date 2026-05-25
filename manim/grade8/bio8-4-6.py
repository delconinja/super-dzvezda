"""
bio8-4-6  —  Вилијам Харви и откривање на циркулација
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
1500 years of wrong, then one man saw, calculated, proved.
Render:  manim -ql bio8-4-6.py Bio846Scene
Output:  media/videos/bio8-4-6/480p15/Bio846Scene.mp4
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


class Bio846Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("1500 години — Гален.",
                     font_size=42, color=RED, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)

        beats = VGroup(
            Text("Грешно.",
                 font_size=42, color=RED, weight=BOLD),
            Text("Но никој не сомневаше.",
                 font_size=32, color=ORANGE),
            Text("Харви виде.",
                 font_size=34, color=GREEN, weight=BOLD),
            Text("Харви пресмета.",
                 font_size=34, color=BLUE, weight=BOLD),
            Text("Харви докажа.",
                 font_size=38, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  GALEN'S WRONG THEORY                             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("galen")

        title = section_title("Пред Харви — Гален грешеше", color=RED)
        self.play(Write(title), run_time=0.8)

        # Galen profile box
        galen_box = RoundedRectangle(
            width=3.5, height=4.0, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=RED, stroke_width=2,
        )
        galen_box.move_to(LEFT * 4.0 + DOWN * 0.2)

        g_name = Text("Гален", font_size=30, color=RED, weight=BOLD)
        g_year = Text("129–216 н.е.", font_size=20, color=GREY)
        g_origin = Text("Грчки лекар", font_size=20, color=WHITE2)
        g_grp = VGroup(g_name, g_year, g_origin).arrange(DOWN, buff=0.2)
        g_grp.move_to(galen_box.get_top() + DOWN * 0.8)

        # silhouette circle
        silh = Circle(radius=0.5, color=RED,
                      fill_color=DARK_CARD, fill_opacity=1,
                      stroke_color=RED, stroke_width=3)
        silh.move_to(galen_box.get_center() + DOWN * 0.5)

        # wrong claims on right
        claims_hdr = Text("Што тврдеше Гален:", font_size=24,
                          color=RED, weight=BOLD)
        claims_hdr.move_to(RIGHT * 2.5 + UP * 1.9)

        claims = [
            "Црниот дроб прави крв постојано.",
            "Крвта се потроши во клетките.",
            "Не циркулира — само патува нанадвор.",
            "Срцето е извор на топлина, не пумпа.",
        ]
        cl_group = VGroup()
        for c in claims:
            box = RoundedRectangle(
                width=7.5, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=RED, stroke_width=1.5,
            )
            t = Text(c, font_size=20, color=WHITE2)
            t.move_to(box)
            cl_group.add(VGroup(box, t))
        cl_group.arrange(DOWN, buff=0.15)
        cl_group.move_to(RIGHT * 2.5 + UP * 0.3)

        # X mark
        x_mark = Text("X", font_size=80, color=RED, weight=BOLD)
        x_mark.move_to(RIGHT * 2.5 + UP * 0.3)
        x_mark.set_opacity(0)

        self.play(Create(galen_box), run_time=0.7)
        self.play(FadeIn(g_grp), Create(silh), run_time=0.8)
        self.play(FadeIn(claims_hdr), run_time=0.5)
        for c in cl_group:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.45)

        # show X over all of it
        self.play(x_mark.animate.set_opacity(0.7), run_time=0.5)

        legacy = Text("1500 години никој не сомневаше.",
                      font_size=24, color=ORANGE, weight=BOLD)
        legacy.move_to(DOWN * 3.0)
        self.play(Write(legacy), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, galen_box, g_grp, silh,
                                 claims_hdr, cl_group, x_mark, legacy)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  HARVEY APPEARS                                   ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("harvey")

        title = section_title("Влегува Вилијам Харви", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # profile card
        h_box = RoundedRectangle(
            width=8.0, height=4.0, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        )
        h_box.move_to(DOWN * 0.2)

        h_silh = Circle(radius=0.6, color=GREEN,
                        fill_color=DARK_CARD, fill_opacity=1,
                        stroke_color=GREEN, stroke_width=3)
        h_silh.move_to(h_box.get_left() + RIGHT * 1.4)

        h_name = Text("Вилијам Харви", font_size=30, color=GREEN, weight=BOLD)
        h_dates = Text("1578–1657", font_size=22, color=GREY)
        h_role = Text("Англиски лекар на крал Чарлс I", font_size=20, color=WHITE2)
        h_grp = VGroup(h_name, h_dates, h_role).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        h_grp.next_to(h_silh, RIGHT, buff=0.6)

        self.play(Create(h_box), run_time=0.7)
        self.play(Create(h_silh), FadeIn(h_grp), run_time=0.9)

        # 1628 banner
        banner = RoundedRectangle(
            width=9.5, height=0.9, corner_radius=0.2,
            fill_color=YELLOW, fill_opacity=0.9,
            stroke_color=YELLOW, stroke_width=2,
        )
        banner.move_to(DOWN * 2.6)
        banner_t = Text('1628 — објавува "De Motu Cordis"',
                        font_size=28, color=DARK_CARD, weight=BOLD)
        banner_t.move_to(banner)

        sub = Text('"За движењето на срцето"',
                   font_size=22, color=YELLOW)
        sub.move_to(DOWN * 3.4)

        self.play(GrowFromCenter(banner), Write(banner_t), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, h_box, h_silh, h_grp,
                                 banner, banner_t, sub)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  HARVEY'S CALCULATION                             ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("calc")

        title = section_title("Пресметката што промени сè")
        self.play(Write(title), run_time=0.8)

        intro = Text("Харви размислуваше:", font_size=26, color=YELLOW)
        intro.move_to(UP * 2.4)

        # Steps as math
        s1 = MathTex(r"\text{1 удар} \approx 70 \text{ ml крв}",
                     font_size=32, color=WHITE2)
        s2 = MathTex(r"70 \text{ удари/мин} \times 70 \text{ ml} = 4900 \text{ ml/мин}",
                     font_size=32, color=BLUE)
        s3 = MathTex(r"4900 \times 60 = 294\,000 \text{ ml/ч}",
                     font_size=32, color=ORANGE)
        s4 = MathTex(r"\approx 294 \text{ литри / час}",
                     font_size=34, color=RED)
        steps = VGroup(s1, s2, s3, s4).arrange(DOWN, buff=0.35)
        steps.next_to(intro, DOWN, buff=0.5)

        self.play(Write(intro), run_time=0.6)
        for s in steps:
            self.play(Write(s), run_time=0.9)
            self.wait(0.3)

        concl = callout("Не може секој час да правиме 294 L нова крв!",
                        width=11.5, border=RED, font_size=24)
        concl.move_to(DOWN * 3.0)
        self.play(FadeIn(concl), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, intro, steps, concl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  EXPERIMENTS                                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("experiments")

        title = section_title("Експериментите на Харви")
        self.play(Write(title), run_time=0.8)

        # arm with ligature
        arm = RoundedRectangle(width=4.5, height=1.0, corner_radius=0.3,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=WHITE2, stroke_width=2)
        arm.move_to(LEFT * 3.0 + UP * 1.5)

        # tied band — vertical line
        band = Rectangle(width=0.2, height=1.4,
                         fill_color=PURPLE, fill_opacity=0.9,
                         stroke_width=0)
        band.move_to(LEFT * 4.0 + UP * 1.5)

        # bulging veins below band (left)
        bulge = VGroup()
        for i, y in enumerate([1.7, 1.5, 1.3]):
            d = Dot(LEFT * 4.5 + UP * y, radius=0.1, color=BLUE)
            bulge.add(d)

        arm_lbl = Text("1. Врзи рака — вените набабруваат",
                       font_size=22, color=BLUE, weight=BOLD)
        arm_lbl.move_to(LEFT * 3.0 + UP * 2.6)

        # valves experiment — press finger on vein
        finger_lbl = Text("2. Притисни вена — крвта оди само нагоре",
                          font_size=22, color=GREEN, weight=BOLD)
        finger_lbl.move_to(RIGHT * 0.0 + DOWN * 0.0)

        vein_h = Line(RIGHT * 1.0 + DOWN * 0.6,
                      RIGHT * 5.0 + DOWN * 0.6,
                      color=BLUE, stroke_width=4)
        finger = Triangle(color=ORANGE, fill_color=ORANGE,
                          fill_opacity=0.9, stroke_color=WHITE2,
                          stroke_width=1.5).scale(0.25)
        finger.move_to(RIGHT * 3.0 + DOWN * 0.3).rotate(PI)

        # arrows
        arr_up = Arrow(RIGHT * 3.0 + DOWN * 0.6, RIGHT * 5.0 + DOWN * 0.6,
                       color=GREEN, buff=0.05, stroke_width=3)
        arr_no = Arrow(RIGHT * 3.0 + DOWN * 0.6, RIGHT * 1.5 + DOWN * 0.6,
                       color=RED, buff=0.05, stroke_width=3)
        arr_no_x = Cross(arr_no, color=RED, stroke_width=4).scale(0.3)
        arr_no_x.move_to(arr_no.get_center())

        self.play(Create(arm), run_time=0.5)
        self.play(FadeIn(band), FadeIn(arm_lbl), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in bulge],
                              lag_ratio=0.15), run_time=0.7)

        self.play(Create(vein_h), FadeIn(finger), FadeIn(finger_lbl),
                  run_time=0.8)
        self.play(GrowArrow(arr_up), run_time=0.5)
        self.play(GrowArrow(arr_no), FadeIn(arr_no_x), run_time=0.5)

        # vivisection note
        viv = Text("3. Виде живо срце како пумпа — не само топли се полнат",
                   font_size=20, color=PURPLE, weight=BOLD)
        viv.move_to(DOWN * 2.5)
        self.play(Write(viv), run_time=0.9)

        concl2 = callout("Крвта циркулира — се враќа во срцето!",
                         width=11.0, border=GREEN, font_size=24)
        concl2.move_to(DOWN * 3.4)
        self.play(FadeIn(concl2), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, arm, band, bulge, arm_lbl,
                                 vein_h, finger, finger_lbl,
                                 arr_up, arr_no, arr_no_x, viv, concl2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  PARADIGM SHIFT                                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("shift")

        title = section_title("Промена на парадигма", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        before_box = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.25,
                                      fill_color=DARK_CARD, fill_opacity=1,
                                      stroke_color=RED, stroke_width=2)
        before_box.move_to(LEFT * 3.3 + DOWN * 0.2)
        b_h = Text("Пред Харви", font_size=26, color=RED, weight=BOLD)
        b_h.move_to(before_box.get_top() + DOWN * 0.4)
        b_lines = VGroup(
            Text("• Крвта се потроши", font_size=20, color=WHITE2),
            Text("• Срцето = печка",  font_size=20, color=WHITE2),
            Text("• Гален непогрешлив", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        b_lines.next_to(b_h, DOWN, buff=0.4)

        after_box = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.25,
                                     fill_color=DARK_CARD, fill_opacity=1,
                                     stroke_color=GREEN, stroke_width=2)
        after_box.move_to(RIGHT * 3.3 + DOWN * 0.2)
        a_h = Text("По Харви", font_size=26, color=GREEN, weight=BOLD)
        a_h.move_to(after_box.get_top() + DOWN * 0.4)
        a_lines = VGroup(
            Text("• Крвта циркулира", font_size=20, color=WHITE2),
            Text("• Срцето = пумпа",  font_size=20, color=WHITE2),
            Text("• Експериментот победи", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        a_lines.next_to(a_h, DOWN, buff=0.4)

        # big arrow between
        big_arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW,
                          buff=0, stroke_width=8)
        big_arrow.move_to(DOWN * 0.2)

        self.play(Create(before_box), FadeIn(b_h), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l) for l in b_lines],
                              lag_ratio=0.1), run_time=0.8)
        self.play(GrowArrow(big_arrow), run_time=0.5)
        self.play(Create(after_box), FadeIn(a_h), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l) for l in a_lines],
                              lag_ratio=0.1), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, before_box, b_h, b_lines,
                                 after_box, a_h, a_lines, big_arrow)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("1500 години Гален грешеше — никој не сомневаше.",
                 font_size=26, color=RED),
            Text("Харви — 1628 — De Motu Cordis.",
                 font_size=28, color=YELLOW, weight=BOLD),
            Text("Пресмета: 294 L/час — невозможно ново.",
                 font_size=26, color=BLUE),
            Text("Виде. Пресмета. Докажа.",
                 font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
