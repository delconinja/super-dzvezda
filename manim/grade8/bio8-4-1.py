"""
bio8-4-1  —  Видови на циркулација
Биологија 8, Единица 4: Циркулаторниот систем

Teaching narrative — Andonovski-style: three-beat punches,
fish vs mammal heart, single vs double loop as story.
Render:  manim -ql bio8-4-1.py Bio841Scene
Output:  media/videos/bio8-4-1/480p15/Bio841Scene.mp4
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


class Bio841Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Крвта патува.",
                     font_size=46, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)
        self.wait(0.3)

        beats = VGroup(
            Text("Кај рибата — еден круг.",
                 font_size=34, color=BLUE),
            Text("Кај нас — два.",
                 font_size=36, color=ORANGE, weight=BOLD),
            Text("Пулмонарен. Системски.",
                 font_size=32, color=PURPLE),
            Text("Поделба за повисока ефикасност.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  OPEN VS CLOSED CIRCULATION                       ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("open_closed")

        title = section_title("Отворена и затворена")
        self.play(Write(title), run_time=0.8)

        # LEFT — open circulation (insect)
        open_header = Text("Отворена", font_size=28,
                           color=ORANGE, weight=BOLD)
        open_header.move_to(LEFT * 3.6 + UP * 2.0)

        # body outline
        open_body = RoundedRectangle(
            width=4.0, height=2.6, corner_radius=0.4,
            fill_color=DARK_CARD, fill_opacity=0.7,
            stroke_color=ORANGE, stroke_width=2,
        ).move_to(LEFT * 3.6 + DOWN * 0.3)

        # tiny tube heart
        open_heart = RoundedRectangle(
            width=1.2, height=0.3, corner_radius=0.1,
            fill_color=RED, fill_opacity=1,
            stroke_color=WHITE2, stroke_width=1.5,
        ).move_to(LEFT * 3.6 + UP * 0.5)

        # blood dots inside body cavity
        open_dots = VGroup()
        np.random.seed(7)
        for _ in range(14):
            x = LEFT * 3.6 + RIGHT * (np.random.uniform(-1.6, 1.6))
            y = UP * (np.random.uniform(-1.3, 0.2))
            d = Dot(point=x + y, radius=0.08, color=RED)
            open_dots.add(d)

        open_label = Text("инсекти, школки",
                          font_size=20, color=WHITE2)
        open_label.next_to(open_body, DOWN, buff=0.25)

        # RIGHT — closed circulation (mammal)
        closed_header = Text("Затворена", font_size=28,
                             color=GREEN, weight=BOLD)
        closed_header.move_to(RIGHT * 3.6 + UP * 2.0)

        closed_body = RoundedRectangle(
            width=4.0, height=2.6, corner_radius=0.4,
            fill_color=DARK_CARD, fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=2,
        ).move_to(RIGHT * 3.6 + DOWN * 0.3)

        closed_heart = Circle(radius=0.32, color=RED,
                              fill_color=RED, fill_opacity=1,
                              stroke_color=WHITE2, stroke_width=1.5)
        closed_heart.move_to(RIGHT * 3.6 + UP * 0.5)

        # vessels — loops
        vessels = VGroup()
        for r in [0.6, 0.95, 1.3]:
            e = Ellipse(width=r * 2.4, height=r * 1.8,
                        color=BLUE, stroke_width=2)
            e.move_to(RIGHT * 3.6 + DOWN * 0.3)
            vessels.add(e)

        closed_label = Text("'рбетници, луѓе",
                            font_size=20, color=WHITE2)
        closed_label.next_to(closed_body, DOWN, buff=0.25)

        self.play(FadeIn(open_header), FadeIn(closed_header),
                  run_time=0.6)
        self.play(Create(open_body), Create(closed_body),
                  run_time=0.8)
        self.play(FadeIn(open_heart), FadeIn(closed_heart),
                  run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in open_dots],
                              lag_ratio=0.05), run_time=1.2)
        self.play(LaggedStart(*[Create(v) for v in vessels],
                              lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(open_label), FadeIn(closed_label),
                  run_time=0.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(
            title, open_header, closed_header,
            open_body, closed_body, open_heart, closed_heart,
            open_dots, vessels, open_label, closed_label)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  SINGLE CIRCULATION — FISH                        ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("single_fish")

        title = section_title("Еден круг — рибата")
        self.play(Write(title), run_time=0.8)

        # fish heart (2 chambers) — left side
        atrium_f = RoundedRectangle(width=1.0, height=0.8, corner_radius=0.15,
                                    fill_color=BLUE, fill_opacity=0.85,
                                    stroke_color=WHITE2, stroke_width=2)
        atrium_f.move_to(LEFT * 4.5 + UP * 0.7)
        atrium_lbl = Text("преткомора", font_size=18, color=WHITE2)
        atrium_lbl.next_to(atrium_f, UP, buff=0.15)

        ventricle_f = RoundedRectangle(width=1.0, height=0.8, corner_radius=0.15,
                                       fill_color=RED, fill_opacity=0.85,
                                       stroke_color=WHITE2, stroke_width=2)
        ventricle_f.move_to(LEFT * 4.5 + DOWN * 0.3)
        vent_lbl = Text("комора", font_size=18, color=WHITE2)
        vent_lbl.next_to(ventricle_f, DOWN, buff=0.15)

        heart_brace = Brace(VGroup(atrium_f, ventricle_f), LEFT, color=YELLOW)
        heart_lbl = heart_brace.get_text("2 простории")
        heart_lbl.set_color(YELLOW).scale(0.7)

        # gills
        gills = VGroup()
        for i in range(4):
            arc = Arc(radius=0.25, angle=PI,
                      color=GREEN, stroke_width=3)
            arc.rotate(PI / 2)
            arc.move_to(LEFT * 1.5 + UP * (1.2 - i * 0.4))
            gills.add(arc)
        gills_lbl = Text("шкрги", font_size=22, color=GREEN, weight=BOLD)
        gills_lbl.next_to(gills, UP, buff=0.2)

        # body block
        body_f = RoundedRectangle(width=2.0, height=2.4, corner_radius=0.3,
                                  fill_color=DARK_CARD, fill_opacity=0.8,
                                  stroke_color=GREY, stroke_width=2)
        body_f.move_to(RIGHT * 3.5)
        body_lbl = Text("тело", font_size=22, color=WHITE2)
        body_lbl.move_to(body_f)

        # arrows — single loop
        arrow1 = Arrow(ventricle_f.get_right(), gills[0].get_left(),
                       color=RED, buff=0.15, stroke_width=4)
        arrow2 = Arrow(gills[-1].get_right(), body_f.get_left(),
                       color=ORANGE, buff=0.15, stroke_width=4)
        arrow3 = CurvedArrow(body_f.get_bottom(),
                             atrium_f.get_bottom() + DOWN * 0.5,
                             color=BLUE, angle=PI / 2, stroke_width=4)

        self.play(Create(atrium_f), Create(ventricle_f),
                  FadeIn(atrium_lbl), FadeIn(vent_lbl),
                  GrowFromCenter(heart_brace), FadeIn(heart_lbl),
                  run_time=1.0)
        self.play(LaggedStart(*[Create(g) for g in gills], lag_ratio=0.1),
                  FadeIn(gills_lbl), run_time=0.9)
        self.play(Create(body_f), FadeIn(body_lbl), run_time=0.6)
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(GrowArrow(arrow2), run_time=0.5)
        self.play(Create(arrow3), run_time=0.7)

        beat_single = Text("Срце → шкрги → тело → срце.",
                           font_size=26, color=YELLOW)
        beat_single.move_to(DOWN * 2.8)
        self.play(Write(beat_single), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, atrium_f, ventricle_f, atrium_lbl, vent_lbl,
            heart_brace, heart_lbl, gills, gills_lbl,
            body_f, body_lbl, arrow1, arrow2, arrow3, beat_single)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  DOUBLE CIRCULATION — MAMMAL                      ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("double_mammal")

        title = section_title("Два круга — цицачите")
        self.play(Write(title), run_time=0.8)

        # central heart — 4 chambers
        h_la = RoundedRectangle(width=0.9, height=0.7, corner_radius=0.12,
                                fill_color=BLUE, fill_opacity=0.85,
                                stroke_color=WHITE2, stroke_width=2)
        h_ra = RoundedRectangle(width=0.9, height=0.7, corner_radius=0.12,
                                fill_color=RED, fill_opacity=0.85,
                                stroke_color=WHITE2, stroke_width=2)
        h_lv = RoundedRectangle(width=0.9, height=0.9, corner_radius=0.12,
                                fill_color=BLUE, fill_opacity=0.85,
                                stroke_color=WHITE2, stroke_width=2)
        h_rv = RoundedRectangle(width=0.9, height=0.9, corner_radius=0.12,
                                fill_color=RED, fill_opacity=0.85,
                                stroke_color=WHITE2, stroke_width=2)

        h_ra.move_to(LEFT * 0.5 + UP * 0.5)
        h_la.move_to(RIGHT * 0.5 + UP * 0.5)
        h_rv.move_to(LEFT * 0.5 + DOWN * 0.4)
        h_lv.move_to(RIGHT * 0.5 + DOWN * 0.4)

        heart_grp = VGroup(h_ra, h_la, h_rv, h_lv)

        # lungs — top
        lung_l = Ellipse(width=1.3, height=1.6, color=PURPLE,
                        fill_color=PURPLE, fill_opacity=0.4,
                        stroke_width=2)
        lung_r = Ellipse(width=1.3, height=1.6, color=PURPLE,
                        fill_color=PURPLE, fill_opacity=0.4,
                        stroke_width=2)
        lung_l.move_to(LEFT * 3.5 + UP * 2.0)
        lung_r.move_to(RIGHT * 3.5 + UP * 2.0)
        lungs_lbl = Text("бели дробови", font_size=20, color=PURPLE)
        lungs_lbl.next_to(VGroup(lung_l, lung_r), UP, buff=0.15)

        # body — bottom
        body = RoundedRectangle(width=4.0, height=1.0, corner_radius=0.25,
                                fill_color=DARK_CARD, fill_opacity=0.8,
                                stroke_color=GREEN, stroke_width=2)
        body.move_to(DOWN * 2.5)
        body_lbl = Text("тело", font_size=22, color=GREEN, weight=BOLD)
        body_lbl.move_to(body)

        # arrows — pulmonary loop (right side of heart -> lungs -> left atrium)
        pul1 = Arrow(h_rv.get_top(), lung_l.get_bottom() + RIGHT * 0.2,
                     color=RED, buff=0.15, stroke_width=3)
        pul2 = Arrow(lung_r.get_bottom() + LEFT * 0.2, h_la.get_top(),
                     color=BLUE, buff=0.15, stroke_width=3)

        # arrows — systemic loop (left ventricle -> body -> right atrium)
        sys1 = CurvedArrow(h_lv.get_bottom(), body.get_right() + UP * 0.1,
                           color=ORANGE, angle=-PI / 4, stroke_width=3)
        sys2 = CurvedArrow(body.get_left() + UP * 0.1,
                           h_ra.get_bottom(),
                           color=BLUE, angle=-PI / 4, stroke_width=3)

        # labels
        pul_lbl = Text("Пулмонарен", font_size=22, color=RED, weight=BOLD)
        pul_lbl.move_to(UP * 3.4)
        sys_lbl = Text("Системски", font_size=22, color=ORANGE, weight=BOLD)
        sys_lbl.move_to(DOWN * 3.5)

        self.play(LaggedStart(*[Create(m) for m in heart_grp],
                              lag_ratio=0.1), run_time=1.0)
        self.play(Create(lung_l), Create(lung_r),
                  FadeIn(lungs_lbl), run_time=0.8)
        self.play(Create(body), FadeIn(body_lbl), run_time=0.6)

        self.play(GrowArrow(pul1), run_time=0.5)
        self.play(GrowArrow(pul2), run_time=0.5)
        self.play(FadeIn(pul_lbl), run_time=0.4)

        self.play(Create(sys1), run_time=0.6)
        self.play(Create(sys2), run_time=0.6)
        self.play(FadeIn(sys_lbl), run_time=0.4)

        self.wait(1.8)

        self.play(FadeOut(VGroup(
            title, heart_grp, lung_l, lung_r, lungs_lbl,
            body, body_lbl, pul1, pul2, sys1, sys2,
            pul_lbl, sys_lbl)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ADVANTAGES OF DOUBLE CIRCULATION                 ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("advantages")

        title = section_title("Зошто два круга се подобри")
        self.play(Write(title), run_time=0.8)

        adv = [
            ("Притисок", "Висок во системскиот круг.",        RED),
            ("Брзина",   "Крвта стасува побрзо до клетките.", ORANGE),
            ("Чистота",  "Кислородната и венската крв не се мешаат.", BLUE),
            ("Енергија", "Цицачите се топлокрвни — треба повеќе кислород.", GREEN),
        ]

        cards = VGroup()
        for name, role, col in adv:
            box = RoundedRectangle(
                width=12.0, height=0.7, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=26, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.6)
            r = Text(role, font_size=22, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 6.5)
            cards.add(VGroup(box, n, r))
        cards.arrange(DOWN, buff=0.2)
        cards.next_to(title, DOWN, buff=0.7)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  COMPARISON TABLE                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        title = section_title("Споредба")
        self.play(Write(title), run_time=0.8)

        # Header row
        col_w = 4.0
        head_y = UP * 1.6
        h1 = Text("Особина", font_size=24, color=YELLOW, weight=BOLD).move_to(LEFT * col_w + head_y)
        h2 = Text("Риба", font_size=24, color=BLUE, weight=BOLD).move_to(head_y)
        h3 = Text("Цицач", font_size=24, color=GREEN, weight=BOLD).move_to(RIGHT * col_w + head_y)

        rows = [
            ("Простории",    "2",            "4"),
            ("Кругови",      "1",            "2"),
            ("Притисок",     "Низок",        "Висок"),
            ("Мешање крв",   "Не — едноставно", "Не — одделено"),
        ]

        cells = VGroup(h1, h2, h3)
        for i, (a, b, c) in enumerate(rows):
            y = head_y + DOWN * (0.7 + i * 0.6)
            ta = Text(a, font_size=22, color=WHITE2).move_to(LEFT * col_w + y)
            tb = Text(b, font_size=22, color=BLUE).move_to(y)
            tc = Text(c, font_size=22, color=GREEN).move_to(RIGHT * col_w + y)
            cells.add(ta, tb, tc)

        self.play(FadeIn(h1), FadeIn(h2), FadeIn(h3), run_time=0.6)
        for i in range(len(rows)):
            self.play(FadeIn(cells[3 + i * 3:6 + i * 3], shift=UP * 0.15),
                      run_time=0.45)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title, cells)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Отворена — инсекти. Затворена — 'рбетници.",
                 font_size=28, color=BLUE),
            Text("Риба — еден круг. Цицач — два.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Пулмонарен. Системски.",
                 font_size=28, color=ORANGE),
            Text("Два круга — повеќе живот.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
