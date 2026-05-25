"""
phys8-1-1  —  Што прават силите?
Физика 8, Единица 1: Сили и движење

Teaching narrative — Andonovski-style text: short punchy sentences,
contrast structure (не...туку), rhythmic build from concrete to concept.
Render:  manim -ql phys8-1-1.py Phys811Scene
Output:  media/videos/phys8-1-1/480p15/Phys811Scene.mp4
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


def obj_box(pos=ORIGIN, color=GREY):
    return RoundedRectangle(
        width=1.2, height=1.0, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)


class Phys811Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # Стил: Прашање → визуелен доказ → кратка моќна реченица
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook_q = Text(
            "Зошто топката секогаш паѓа наземи?",
            font_size=46, color=YELLOW, weight=BOLD,
        )
        hook_q.to_edge(UP, buff=0.55)
        self.play(Write(hook_q), run_time=1.5)
        self.wait(1.0)

        # Parabolic arc
        ball = Circle(radius=0.32, fill_color=ORANGE, fill_opacity=1,
                      stroke_color=WHITE, stroke_width=2)
        ball.move_to(LEFT * 5.5 + DOWN * 1.6)

        path = ParametricFunction(
            lambda t: np.array([
                -5.5 + 7.0 * t,
                -1.6 + 5.0 * t - 6.5 * t ** 2,
                0,
            ]),
            t_range=[0, 1],
            color=GREY, stroke_opacity=0.3, stroke_width=1.5,
        )
        self.play(FadeIn(ball), Create(path), run_time=0.4)
        self.play(MoveAlongPath(ball, path), run_time=2.2, rate_func=linear)
        self.wait(0.6)

        # Gravity arrow
        grav_arr = Arrow(
            ball.get_center(),
            ball.get_center() + DOWN * 2.0,
            color=RED, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.18,
        )
        grav_lbl = Text("Гравитација", font_size=30, color=RED, weight=BOLD)
        grav_lbl.next_to(grav_arr, RIGHT, buff=0.28)

        self.play(GrowArrow(grav_arr), run_time=0.8)
        self.play(Write(grav_lbl))
        self.wait(0.5)

        # Andonovski-style reveal: three short punches
        ans1 = Text("Невидлива.", font_size=36, color=WHITE2, weight=BOLD)
        ans2 = Text("Но постојана.", font_size=36, color=WHITE2, weight=BOLD)
        ans3 = Text("Тоа е сила.", font_size=40, color=YELLOW, weight=BOLD)
        ans1.to_edge(DOWN, buff=1.5)
        ans2.next_to(ans1, RIGHT, buff=0.5)
        ans3.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(ans1, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeIn(ans2, shift=UP * 0.2))
        self.wait(0.5)
        self.play(Write(ans3), run_time=0.8)
        self.play(Indicate(ans3, scale_factor=1.2, color=YELLOW))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [hook_q, ball, path, grav_arr, grav_lbl, ans1, ans2, ans3]])

        # ══════════════════════════════════════════════════════════
        # 2.  ШТО Е СИЛА?                                    ~15 s
        # Стил: Директна дефиниција + конкретен пример со движење
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        big = Text("СИЛА", font_size=100, color=YELLOW, weight=BOLD)
        self.play(Write(big), run_time=1.0)
        self.play(Wiggle(big, scale_value=1.15, n_wiggles=2))
        self.wait(0.3)
        self.play(big.animate.scale(0.42).to_corner(UL).shift(RIGHT * 0.2 + DOWN * 0.05))

        # Two-line definition — conversational, like speech
        defn1 = Text("Туркаш?  Тоа е сила.", font_size=34, color=WHITE2)
        defn2 = Text("Влечеш?  И тоа е сила.", font_size=34, color=WHITE2)
        defn1.shift(UP * 0.6)
        defn2.shift(UP * 0.0)
        self.play(FadeIn(defn1, shift=LEFT * 0.3))
        self.wait(0.7)
        self.play(FadeIn(defn2, shift=LEFT * 0.3))
        self.wait(0.8)

        box = RoundedRectangle(
            width=1.5, height=1.2, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        )
        box.shift(DOWN * 1.2)
        self.play(FadeIn(box))

        push = Arrow(box.get_left() + LEFT * 2.4, box.get_left(),
                     color=BLUE, buff=0.05, stroke_width=5,
                     max_tip_length_to_length_ratio=0.18)
        push_lbl = Text("туркање", font_size=26, color=BLUE, weight=BOLD)
        push_lbl.next_to(push, UP, buff=0.1)
        self.play(GrowArrow(push), Write(push_lbl))
        self.play(box.animate.shift(RIGHT * 0.9), run_time=0.5, rate_func=rush_into)
        self.play(box.animate.shift(LEFT * 0.9), run_time=0.3)
        self.wait(0.7)

        pull = Arrow(box.get_right(), box.get_right() + RIGHT * 2.4,
                     color=ORANGE, buff=0.05, stroke_width=5,
                     max_tip_length_to_length_ratio=0.18)
        pull_lbl = Text("повлекување", font_size=26, color=ORANGE, weight=BOLD)
        pull_lbl.next_to(pull, UP, buff=0.1)
        self.play(FadeOut(push), FadeOut(push_lbl))
        self.play(GrowArrow(pull), Write(pull_lbl))
        self.play(box.animate.shift(RIGHT * 0.9), run_time=0.5, rate_func=rush_into)
        self.play(box.animate.shift(LEFT * 0.9), run_time=0.3)
        self.wait(0.7)

        # Contrast structure: не...туку
        invis = Text(
            "Силата не ја виде никој.  Но нејзините ефекти — ги почувствуваше секој.",
            font_size=25, color=GREY,
        )
        invis.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(invis, shift=UP * 0.2))
        self.wait(2.8)

        self.play(*[FadeOut(m) for m in [big, defn1, defn2, box, pull, pull_lbl, invis]])

        # ══════════════════════════════════════════════════════════
        # 3.  ШТО МОЖЕ ДА НАПРАВИ СИЛАТА?                   ~15 s
        # Стил: броење + конкретен пример за секоја точка
        # ══════════════════════════════════════════════════════════
        self.next_section("effects")

        hdr = section_title("Силата прави само четири нешта.")
        sub_hdr = Text("Само четири — но сè е во нив.", font_size=28, color=GREY)
        sub_hdr.next_to(hdr, DOWN, buff=0.18)
        self.play(Write(hdr), run_time=1.0)
        self.play(FadeIn(sub_hdr))
        self.wait(0.8)

        data = [
            ("1", "Го менува обликот",       GREEN,  "стисни пружина → се деформира"),
            ("2", "Го менува движењето",      BLUE,   "удри топка → убрзува"),
            ("3", "Ја менува насоката",       ORANGE, "скрши, сврти, пренасочи"),
            ("4", "Го запира или почнува",    RED,    "запри кола, тргни камен"),
        ]

        cards = VGroup()
        for num, text, color, example in data:
            bg = RoundedRectangle(
                width=10.8, height=1.05, corner_radius=0.22,
                fill_color=f"{color}14", fill_opacity=1,
                stroke_color=color, stroke_width=1.8,
            )
            badge_c = Circle(radius=0.32, fill_color=color, fill_opacity=1, stroke_width=0)
            badge_t = Text(num, font_size=22, color="#0d1b2e", weight=BOLD)
            badge_t.move_to(badge_c)
            badge = VGroup(badge_c, badge_t)
            badge.next_to(bg.get_left(), RIGHT, buff=0.22)

            main_t = Text(text, font_size=26, color=WHITE2, weight=BOLD)
            main_t.next_to(badge, RIGHT, buff=0.3)

            ex_t = Text(example, font_size=20, color=color)
            ex_t.next_to(bg.get_right(), LEFT, buff=0.3)

            card = VGroup(bg, badge, main_t, ex_t)
            cards.add(card)

        cards.arrange(DOWN, buff=0.28)
        cards.shift(DOWN * 0.75)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.55)
            self.wait(0.6)

        self.wait(2.2)
        self.play(FadeOut(hdr), FadeOut(sub_hdr), FadeOut(cards))

        # ══════════════════════════════════════════════════════════
        # 4.  ВИДОВИ СИЛИ                                    ~15 s
        # Стил: две колони, нагласување на „без допир" — изненадување
        # ══════════════════════════════════════════════════════════
        self.next_section("types")

        hdr2 = section_title("Два вида сили")
        self.play(Write(hdr2), run_time=0.9)

        ct_panel = RoundedRectangle(
            width=6.0, height=5.2, corner_radius=0.4,
            fill_color="#0b2418", fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).shift(LEFT * 3.4 + DOWN * 0.8)

        ct_title = Text("Контактни сили", font_size=30, color=GREEN, weight=BOLD)
        ct_title.next_to(ct_panel.get_top(), DOWN, buff=0.35)
        ct_note = Text("потребен допир", font_size=22, color=GREEN)
        ct_note.next_to(ct_title, DOWN, buff=0.1)

        ct_items = VGroup(
            Text("⊙  Триење",          font_size=26, color=WHITE2),
            Text("⊙  Притисок",        font_size=26, color=WHITE2),
            Text("⊙  Затегнатост",     font_size=26, color=WHITE2),
            Text("⊙  Еластична сила",  font_size=26, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.36)
        ct_items.next_to(ct_note, DOWN, buff=0.4)

        self.play(Create(ct_panel))
        self.play(Write(ct_title), Write(ct_note))
        for item in ct_items:
            self.play(FadeIn(item, shift=RIGHT * 0.25), run_time=0.38)
        self.wait(0.5)

        dt_panel = RoundedRectangle(
            width=6.0, height=5.2, corner_radius=0.4,
            fill_color="#1f0b2b", fill_opacity=1,
            stroke_color=PURPLE, stroke_width=2,
        ).shift(RIGHT * 3.4 + DOWN * 0.8)

        dt_title = Text("Далечински сили", font_size=30, color=PURPLE, weight=BOLD)
        dt_title.next_to(dt_panel.get_top(), DOWN, buff=0.35)
        # Andonovski-style contrast: не...туку
        dt_note = Text("дејствуваат без допир — на далечина", font_size=21, color=PURPLE)
        dt_note.next_to(dt_title, DOWN, buff=0.1)

        dt_items = VGroup(
            Text("⊙  Гравитација",      font_size=26, color=WHITE2),
            Text("⊙  Магнетна сила",    font_size=26, color=WHITE2),
            Text("⊙  Електрична сила",  font_size=26, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.36)
        dt_items.next_to(dt_note, DOWN, buff=0.4)

        # Surprise note — the "никогаш" Andonovski punch
        surprise = Text(
            "Земјата те влече — а ти ја не допираш. Никогаш.",
            font_size=24, color=YELLOW,
        )
        surprise.to_edge(DOWN, buff=0.6)

        self.play(Create(dt_panel))
        self.play(Write(dt_title), Write(dt_note))
        for item in dt_items:
            self.play(FadeIn(item, shift=LEFT * 0.25), run_time=0.38)

        self.play(Circumscribe(dt_note, color=YELLOW, run_time=1.3))
        self.play(FadeIn(surprise, shift=UP * 0.2))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr2, ct_panel, ct_title, ct_note, ct_items,
            dt_panel, dt_title, dt_note, dt_items, surprise,
        ]])

        # ══════════════════════════════════════════════════════════
        # 5.  МЕРЕЊЕ                                          ~12 s
        # Стил: Пружината знае — антропоморфизација
        # ══════════════════════════════════════════════════════════
        self.next_section("measurement")

        hdr3 = section_title("Мериме со динамометар.  Во Њутни.")
        self.play(Write(hdr3), run_time=1.1)

        n_callout = callout(
            "1 Њутн  (N)  =  сила да го забрза 1 kg за 1 m/s²",
            width=9.2, bg="#0d2b44", border=BLUE, font_size=27,
        )
        n_callout.shift(UP * 1.7)
        self.play(FadeIn(n_callout, shift=DOWN * 0.3))
        self.wait(1.0)

        newton_note = Text("Именувана по Исак Њутн.", font_size=24, color=GREY)
        newton_note.next_to(n_callout, DOWN, buff=0.2)
        self.play(FadeIn(newton_note))
        self.wait(0.6)

        def make_spring(top_y, bottom_y, x=0.0, n=6, amp=0.22, col=GREEN):
            pts = []
            span = top_y - bottom_y
            step = span / (n * 2)
            for i in range(n * 2 + 1):
                y = top_y - step * i
                x_ = x + amp * (1 if i % 2 == 0 else -1)
                pts.append(np.array([x_, y, 0]))
            vm = VMobject(color=col, stroke_width=3)
            vm.set_points_as_corners(pts)
            return vm

        anchor = Line(RIGHT * 2.2 + DOWN * 0.1, RIGHT * 3.8 + DOWN * 0.1,
                      color=GREY, stroke_width=4)
        sp1 = make_spring(top_y=-0.1, bottom_y=-1.2, x=3.0)
        w1 = Circle(radius=0.3, fill_color=ORANGE, fill_opacity=1,
                    stroke_color=WHITE, stroke_width=1.5)
        w1.move_to(sp1.get_points()[-1] + DOWN * 0.3)
        w_lbl1 = Text("1 N", font_size=26, color=ORANGE, weight=BOLD)
        w_lbl1.next_to(w1, RIGHT, buff=0.2)

        self.play(FadeIn(anchor))
        self.play(Create(sp1))
        self.play(FadeIn(w1), Write(w_lbl1))
        self.wait(0.8)

        sp2 = make_spring(top_y=-0.1, bottom_y=-2.2, x=3.0)
        w2 = Circle(radius=0.38, fill_color=RED, fill_opacity=1,
                    stroke_color=WHITE, stroke_width=1.5)
        w2.move_to(sp2.get_points()[-1] + DOWN * 0.38)
        w_lbl2 = Text("3 N", font_size=26, color=RED, weight=BOLD)
        w_lbl2.next_to(w2, RIGHT, buff=0.2)

        # Andonovski: personification — "Пружината знае."
        spring_note = Text("Пружината знае.  Поголема сила — подолга пружина.",
                           font_size=25, color=YELLOW)
        spring_note.shift(LEFT * 1.2 + DOWN * 1.6)

        self.play(
            Transform(sp1, sp2),
            Transform(w1, w2),
            Transform(w_lbl1, w_lbl2),
            run_time=1.0,
        )
        self.play(Write(spring_note))
        self.wait(2.2)

        self.play(*[FadeOut(m) for m in [
            hdr3, n_callout, newton_note, anchor, sp1, w1, w_lbl1, spring_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 6.  РЕЗУЛТАНТНА СИЛА                               ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("resultant")

        hdr4 = section_title("Резултантна сила")
        sub4 = Text(
            "Кога повеќе сили делуваат на еден предмет — се собираат во една.",
            font_size=25, color=GREY,
        )
        sub4.next_to(hdr4, DOWN, buff=0.22)
        self.play(Write(hdr4), FadeIn(sub4))
        self.wait(1.2)

        def show_case(label, lbl_color, left_n, right_n, result_text, res_color):
            lbl = Text(label, font_size=27, color=lbl_color, weight=BOLD)
            lbl.shift(UP * 1.2)
            o = obj_box(DOWN * 0.4)
            self.play(Write(lbl), FadeIn(o))
            mobs = [lbl, o]

            if left_n > 0:
                a_l = Arrow(o.get_left(), o.get_left() + LEFT * (left_n * 0.38),
                            color=RED, buff=0, stroke_width=4,
                            max_tip_length_to_length_ratio=0.2)
                l_t = Text(f"{left_n} N ←", font_size=21, color=RED, weight=BOLD)
                l_t.next_to(a_l, UP, buff=0.07)
                self.play(GrowArrow(a_l), Write(l_t), run_time=0.55)
                mobs.extend([a_l, l_t])

            if right_n > 0:
                a_r = Arrow(o.get_right(), o.get_right() + RIGHT * (right_n * 0.38),
                            color=GREEN, buff=0, stroke_width=4,
                            max_tip_length_to_length_ratio=0.2)
                r_t = Text(f"{right_n} N →", font_size=21, color=GREEN, weight=BOLD)
                r_t.next_to(a_r, UP, buff=0.07)
                self.play(GrowArrow(a_r), Write(r_t), run_time=0.55)
                mobs.extend([a_r, r_t])

            res = Text(result_text, font_size=29, color=res_color, weight=BOLD)
            res.to_edge(DOWN, buff=0.9)
            self.play(Write(res))
            self.wait(2.4)
            self.play(*[FadeOut(m) for m in mobs + [res]])

        show_case(
            "1)  Исти насоки — се собираат",
            GREEN, 0, 8,
            "3 N + 5 N = 8 N  →  предметот убрзува",
            YELLOW,
        )

        show_case(
            "2)  Спротивни насоки — поголемата победува",
            ORANGE, 5, 3,
            "5 N − 3 N = 2 N  ←  поголемата страна победи",
            YELLOW,
        )

        # Equilibrium with Indicate
        eq_lbl = Text("3)  Еднакви и спротивни  →  ништо", font_size=27, color=BLUE, weight=BOLD)
        eq_lbl.shift(UP * 1.2)
        o3 = obj_box(DOWN * 0.4)
        self.play(Write(eq_lbl), FadeIn(o3))

        a_l3 = Arrow(o3.get_left(), o3.get_left() + LEFT * 1.9,
                     color=RED, buff=0, stroke_width=4,
                     max_tip_length_to_length_ratio=0.2)
        l_t3 = Text("5 N ←", font_size=21, color=RED, weight=BOLD)
        l_t3.next_to(a_l3, UP, buff=0.07)
        a_r3 = Arrow(o3.get_right(), o3.get_right() + RIGHT * 1.9,
                     color=GREEN, buff=0, stroke_width=4,
                     max_tip_length_to_length_ratio=0.2)
        r_t3 = Text("5 N →", font_size=21, color=GREEN, weight=BOLD)
        r_t3.next_to(a_r3, UP, buff=0.07)
        self.play(GrowArrow(a_l3), Write(l_t3), run_time=0.55)
        self.play(GrowArrow(a_r3), Write(r_t3), run_time=0.55)

        zero = Text(
            "5 N − 5 N = 0  →  Предметот мирува.  Тоа е Првиот Њутнов закон.",
            font_size=26, color=YELLOW, weight=BOLD,
        )
        zero.to_edge(DOWN, buff=0.9)
        self.play(Write(zero))
        self.play(Indicate(o3, scale_factor=1.3, color=YELLOW))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr4, sub4, eq_lbl, o3, a_l3, l_t3, a_r3, r_t3, zero,
        ]])

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                          ~9 s
        # Стил: кратки, ударни реченици — Анdonovski финале
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=46, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        rows_data = [
            (BLUE,   "Сила  =  туркање или повлекување"),
            (GREEN,  "Единица  =  Њутн  (N)"),
            (PURPLE, "Контактни сили  —  потребен допир"),
            (ORANGE, "Далечински сили  —  дејствуваат без допир"),
            (YELLOW, "Резултантна = 0  →  предметот мирува"),
            (WHITE2, "Резултантна ≠ 0  →  предметот убрзува"),
        ]

        rows = VGroup()
        for color, text in rows_data:
            dot = Circle(radius=0.14, fill_color=color,
                         fill_opacity=1, stroke_width=0)
            t = Text(text, font_size=26, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.24)
            row = VGroup(dot, t)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.shift(DOWN * 0.75 + RIGHT * 0.5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.5)

        self.wait(3.2)
