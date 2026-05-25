"""
bio8-2-5  —  Дејство на мускулите — парови антагонисти
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
muscles as dance partners, only pulling never pushing.
Render:  manim -ql bio8-2-5.py Bio825Scene
Output:  media/videos/bio8-2-5/480p15/Bio825Scene.mp4
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


class Bio825Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Мускулот само влече.",
                  font_size=48, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.3)
        self.wait(0.3)

        h2 = Text("Никогаш не турка.",
                  font_size=44, color=RED, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.5)
        self.play(Write(h2), run_time=1.3)
        self.wait(0.3)

        beats = VGroup(
            Text("Затоа доаѓаат во пар.", font_size=36, color=WHITE2),
            Text("Бицепс свива.", font_size=34, color=BLUE),
            Text("Трицепс исправа.", font_size=34, color=GREEN),
            Text("Совршен балет.", font_size=38, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(h2, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, h2, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ПРАВИЛОТО                                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("rule")
        title = section_title("Правилото на мускулите")
        self.play(Write(title), run_time=0.8)

        rule = RoundedRectangle(width=10.5, height=2.2, corner_radius=0.3,
                                fill_color="#1a3552", fill_opacity=1,
                                stroke_color=YELLOW, stroke_width=3)
        rule.move_to(UP * 1.0)
        rule_txt = VGroup(
            Text("Мускулот се скуса.", font_size=32, color=WHITE2),
            Text("Влече коска кон себе.", font_size=32, color=WHITE2),
            Text("Не може да турка назад.", font_size=32, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        rule_txt.move_to(rule.get_center())

        self.play(FadeIn(rule), run_time=0.6)
        for line in rule_txt:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)
        self.wait(0.5)

        # Question and answer
        q = Text("Како тогаш се враќа коската?",
                 font_size=28, color=BLUE)
        q.move_to(DOWN * 0.8)
        a = Text("Друг мускул на спротивна страна влече!",
                 font_size=28, color=GREEN, weight=BOLD)
        a.next_to(q, DOWN, buff=0.3)

        self.play(Write(q), run_time=0.9)
        self.wait(0.5)
        self.play(Write(a), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, rule, rule_txt, q, a)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  АНТАГОНИСТИ — ДЕФИНИЦИЈА                        ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("antagonist")
        title = section_title("Парови антагонисти")
        self.play(Write(title), run_time=0.8)

        defn = VGroup(
            Text("Антагонисти —", font_size=40, color=YELLOW, weight=BOLD),
            Text("мускули кои работат спротивно.", font_size=30, color=WHITE2),
            Text("Кога едниот се свива,", font_size=26, color=BLUE),
            Text("другиот се опушта.", font_size=26, color=GREEN),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in defn:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, defn)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  БИЦЕПС vs ТРИЦЕПС — АНИМАЦИЈА                   ~80 s
        # ══════════════════════════════════════════════════════════
        self.next_section("biceps_triceps")
        title = section_title("Бицепс vs трицепс")
        self.play(Write(title), run_time=0.8)

        # Shoulder pivot
        shoulder = Dot(UP * 1.8 + LEFT * 0.5, radius=0.15, color=GREY)
        # Upper arm (fixed)
        upper = Line(shoulder.get_center(), shoulder.get_center() + DOWN * 1.8,
                     color=WHITE2, stroke_width=10)
        elbow_pt = shoulder.get_center() + DOWN * 1.8
        elbow = Dot(elbow_pt, radius=0.13, color=BLUE)

        # Forearm — will rotate
        forearm = Line(elbow_pt, elbow_pt + DOWN * 1.8, color=WHITE2,
                       stroke_width=10)

        # Biceps muscle (front of upper arm)
        biceps = Ellipse(width=0.5, height=1.4, color=RED,
                         fill_opacity=0.7, stroke_color=RED, stroke_width=2)
        biceps.move_to(shoulder.get_center() + DOWN * 0.9 + LEFT * 0.4)
        biceps_lbl = Text("бицепс", font_size=20, color=RED, weight=BOLD)
        biceps_lbl.next_to(biceps, LEFT, buff=0.2)

        # Triceps muscle (back of upper arm)
        triceps = Ellipse(width=0.5, height=1.4, color=BLUE,
                          fill_opacity=0.7, stroke_color=BLUE, stroke_width=2)
        triceps.move_to(shoulder.get_center() + DOWN * 0.9 + RIGHT * 0.4)
        triceps_lbl = Text("трицепс", font_size=20, color=BLUE, weight=BOLD)
        triceps_lbl.next_to(triceps, RIGHT, buff=0.2)

        # Status indicators on the side
        status_box = RoundedRectangle(width=4.0, height=2.6, corner_radius=0.2,
                                      fill_color=DARK_CARD, fill_opacity=1,
                                      stroke_color=GREY, stroke_width=2)
        status_box.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        status_title = Text("Состојба", font_size=20, color=YELLOW, weight=BOLD)
        status_title.move_to(status_box.get_top() + DOWN * 0.3)

        bi_status_lbl = Text("Бицепс:", font_size=18, color=RED)
        bi_status_lbl.move_to(status_box.get_center() + UP * 0.4 + LEFT * 0.8)
        bi_status = Text("опуштен", font_size=18, color=GREEN, weight=BOLD)
        bi_status.next_to(bi_status_lbl, RIGHT, buff=0.2)

        tr_status_lbl = Text("Трицепс:", font_size=18, color=BLUE)
        tr_status_lbl.move_to(status_box.get_center() + DOWN * 0.3 + LEFT * 0.8)
        tr_status = Text("опуштен", font_size=18, color=GREEN, weight=BOLD)
        tr_status.next_to(tr_status_lbl, RIGHT, buff=0.2)

        self.play(FadeIn(shoulder), Create(upper), FadeIn(elbow),
                  Create(forearm), run_time=1.0)
        self.play(GrowFromCenter(biceps), GrowFromCenter(triceps),
                  Write(biceps_lbl), Write(triceps_lbl), run_time=0.8)
        self.play(FadeIn(status_box), Write(status_title), run_time=0.5)
        self.play(FadeIn(bi_status_lbl), FadeIn(bi_status),
                  FadeIn(tr_status_lbl), FadeIn(tr_status), run_time=0.6)
        self.wait(0.5)

        # Phase 1: biceps contracts — forearm bends up
        phase1 = Text("Фаза 1 — Свивање", font_size=26, color=RED, weight=BOLD)
        phase1.to_edge(DOWN, buff=0.6)
        self.play(Write(phase1), run_time=0.6)

        biceps_thick = Ellipse(width=0.85, height=1.0, color=RED,
                               fill_opacity=0.9, stroke_color=RED, stroke_width=2)
        biceps_thick.move_to(biceps.get_center())

        new_bi_status = Text("свиен", font_size=18, color=RED, weight=BOLD)
        new_bi_status.move_to(bi_status.get_center())
        new_tr_status = Text("опуштен", font_size=18, color=GREEN, weight=BOLD)
        new_tr_status.move_to(tr_status.get_center())

        self.play(Transform(biceps, biceps_thick),
                  Rotate(forearm, angle=PI * 0.6, about_point=elbow_pt),
                  Transform(bi_status, new_bi_status),
                  Transform(tr_status, new_tr_status), run_time=1.3)
        self.wait(1.0)

        # Phase 2: triceps contracts — forearm straightens
        phase2 = Text("Фаза 2 — Исправање", font_size=26, color=BLUE, weight=BOLD)
        phase2.move_to(phase1.get_center())
        self.play(FadeOut(phase1), Write(phase2), run_time=0.6)

        triceps_thick = Ellipse(width=0.85, height=1.0, color=BLUE,
                                fill_opacity=0.9, stroke_color=BLUE, stroke_width=2)
        triceps_thick.move_to(triceps.get_center())

        biceps_thin = Ellipse(width=0.5, height=1.4, color=RED,
                              fill_opacity=0.7, stroke_color=RED, stroke_width=2)
        biceps_thin.move_to(biceps.get_center())

        bi_status2 = Text("опуштен", font_size=18, color=GREEN, weight=BOLD)
        bi_status2.move_to(bi_status.get_center())
        tr_status2 = Text("свиен", font_size=18, color=RED, weight=BOLD)
        tr_status2.move_to(tr_status.get_center())

        self.play(Transform(triceps, triceps_thick),
                  Transform(biceps, biceps_thin),
                  Rotate(forearm, angle=-PI * 0.6, about_point=elbow_pt),
                  Transform(bi_status, bi_status2),
                  Transform(tr_status, tr_status2), run_time=1.3)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, shoulder, upper, elbow, forearm,
                                 biceps, triceps, biceps_lbl, triceps_lbl,
                                 status_box, status_title, bi_status_lbl,
                                 bi_status, tr_status_lbl, tr_status, phase2)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ДРУГИ ПАРОВИ                                    ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("other_pairs")
        title = section_title("Други антагонистички парови")
        self.play(Write(title), run_time=0.8)

        # Three pair cards
        def pair_card(loc, m1, m2, pos):
            box = RoundedRectangle(width=4.5, height=2.0, corner_radius=0.2,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=YELLOW, stroke_width=2)
            box.move_to(pos)
            loc_t = Text(loc, font_size=24, color=YELLOW, weight=BOLD)
            loc_t.move_to(box.get_top() + DOWN * 0.4)
            m1_t = Text(m1, font_size=18, color=BLUE)
            m1_t.move_to(box.get_center() + DOWN * 0.05)
            vs = Text("⇄", font_size=24, color=WHITE2)
            vs.next_to(m1_t, DOWN, buff=0.1)
            m2_t = Text(m2, font_size=18, color=GREEN)
            m2_t.move_to(box.get_bottom() + UP * 0.3)
            return VGroup(box, loc_t, m1_t, vs, m2_t)

        p1 = pair_card("Натколеница", "Квадрицепс (исправа)",
                       "Хамстринг (свива)", LEFT * 4.0 + UP * 0.5)
        p2 = pair_card("Глутеуси", "Глутеус (исправа колк)",
                       "Илиопсоас (свива колк)", UP * 0.5)
        p3 = pair_card("Прсти", "Флексори (стисни)",
                       "Екстензори (отвори)", RIGHT * 4.0 + UP * 0.5)

        for p in (p1, p2, p3):
            self.play(FadeIn(p, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)
        self.wait(1.0)

        punch = callout("Секаде во телото — секогаш во пар.",
                        width=9.5, bg="#1a3552", border=YELLOW, font_size=28)
        punch.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(punch, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, p1, p2, p3, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ТЕТИВИ — ВРСКАТА                                ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("tendons")
        title = section_title("Тетиви — врска со коска")
        self.play(Write(title), run_time=0.8)

        # Bone
        bone = RoundedRectangle(width=4.0, height=0.8, corner_radius=0.4,
                                color=WHITE2, fill_opacity=0.3, stroke_width=2)
        bone.move_to(UP * 0.5 + RIGHT * 1.5)
        bone_lbl = Text("Коска", font_size=18, color=WHITE2)
        bone_lbl.next_to(bone, UP, buff=0.15)

        # Muscle
        muscle = Ellipse(width=2.5, height=1.2, color=RED,
                         fill_opacity=0.7, stroke_color=RED, stroke_width=2)
        muscle.move_to(DOWN * 0.8 + LEFT * 2.5)
        muscle_lbl = Text("Мускул", font_size=18, color=RED)
        muscle_lbl.next_to(muscle, DOWN, buff=0.15)

        # Tendon — thick connecting line
        tendon = Line(muscle.get_right() + RIGHT * 0.05,
                      bone.get_left() + LEFT * 0.05,
                      color=ORANGE, stroke_width=10)
        tendon_lbl = Text("Тетива", font_size=22, color=ORANGE, weight=BOLD)
        tendon_lbl.next_to(tendon, UP, buff=0.3)

        self.play(Create(bone), Write(bone_lbl), run_time=0.7)
        self.play(GrowFromCenter(muscle), Write(muscle_lbl), run_time=0.7)
        self.play(Create(tendon), Write(tendon_lbl), run_time=0.8)
        self.wait(0.4)

        info = VGroup(
            Text("Тетивите се цврсти и неподвижни.",
                 font_size=22, color=WHITE2),
            Text("Пренесуваат сила од мускул на коска.",
                 font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)

        for line in info:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.7)
            self.wait(0.2)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, bone, bone_lbl, muscle, muscle_lbl,
                                 tendon, tendon_lbl, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Еден влече.", font_size=44, color=BLUE, weight=BOLD),
            Text("Другиот пушта.", font_size=44, color=GREEN, weight=BOLD),
            Text("Се менуваат улогите.", font_size=38, color=ORANGE),
            Text("Балет на сила.", font_size=46, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
