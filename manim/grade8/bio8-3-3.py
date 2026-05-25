"""
bio8-3-3  —  Тестирање на јаглехидрати и масти
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
chemistry as detective, color change as confession.
Render:  manim -ql bio8-3-3.py Bio833Scene
Output:  media/videos/bio8-3-3/480p15/Bio833Scene.mp4
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


def make_tube(fill_color, fill_opacity=0.7):
    """Returns a test tube VGroup (outline + liquid fill)."""
    body = RoundedRectangle(
        width=0.7, height=2.2, corner_radius=0.35,
        stroke_color=WHITE2, stroke_width=2.5,
        fill_color=DARK_CARD, fill_opacity=1,
    )
    liquid = RoundedRectangle(
        width=0.6, height=1.2, corner_radius=0.3,
        stroke_color=fill_color, stroke_width=0,
        fill_color=fill_color, fill_opacity=fill_opacity,
    )
    liquid.move_to(body.get_bottom() + UP * 0.7)
    return VGroup(body, liquid)


class Bio833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Капни јод на леб.",
                     font_size=44, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Стане синочерн.",                font_size=42, color=PURPLE, weight=BOLD),
            Text("Скроб.",                         font_size=46, color=BLUE, weight=BOLD),
            Text("Капни на јаболко.",              font_size=36, color=ORANGE),
            Text("Без промена. Без скроб.",        font_size=34, color=GREY),
            Text("Хемијата открива.",              font_size=36, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — three tests overview                ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Три теста")
        self.play(Write(title), run_time=0.8)

        tests = [
            ("Скроб",   "Јод",            "Синочерно",   PURPLE),
            ("Шеќер",   "Бенедиктов",     "Тула-црвено", RED),
            ("Маст",    "Хартија",        "Мрсна дамка", ORANGE),
        ]

        cards = VGroup()
        for what, reagent, result, col in tests:
            box = RoundedRectangle(
                width=11.5, height=1.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.5,
            )
            w = Text(what, font_size=26, color=col, weight=BOLD)
            w.move_to(box.get_left() + RIGHT * 1.3)
            r = Text(reagent, font_size=22, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 4.5)
            arrow = Text("→", font_size=28, color=WHITE2)
            arrow.move_to(box.get_left() + RIGHT * 6.6)
            res = Text(result, font_size=22, color=YELLOW, weight=BOLD)
            res.move_to(box.get_left() + RIGHT * 9.0)
            cards.add(VGroup(box, w, r, arrow, res))
        cards.arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=0.6)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — iodine test (starch)                 ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("iodine_test")

        title = section_title("Тест со јод — скроб")
        self.play(Write(title), run_time=0.8)

        # Before
        tube_before = make_tube(ORANGE, 0.75)
        tube_before.shift(LEFT * 4.0 + DOWN * 0.3)
        lbl_before = Text("Леб + јод", font_size=22, color=WHITE2)
        lbl_before.next_to(tube_before, DOWN, buff=0.3)
        time_before = Text("0 s", font_size=20, color=GREY)
        time_before.next_to(tube_before, UP, buff=0.3)

        # Arrow
        arrow = Arrow(LEFT * 2.4, RIGHT * 0.4, color=YELLOW, stroke_width=4,
                      buff=0.2).shift(DOWN * 0.3)
        arrow_lbl = Text("реакција", font_size=20, color=YELLOW)
        arrow_lbl.next_to(arrow, UP, buff=0.15)

        # After
        tube_after = make_tube(PURPLE, 0.95)
        # Make it darker - overlay a dark fill
        dark_overlay = RoundedRectangle(
            width=0.6, height=1.2, corner_radius=0.3,
            stroke_width=0, fill_color="#1a0a3a", fill_opacity=0.6,
        )
        dark_overlay.move_to(tube_after[1].get_center())
        tube_after.add(dark_overlay)
        tube_after.shift(RIGHT * 2.6 + DOWN * 0.3)
        lbl_after = Text("Синочерно", font_size=22, color=PURPLE, weight=BOLD)
        lbl_after.next_to(tube_after, DOWN, buff=0.3)
        time_after = Text("после", font_size=20, color=GREY)
        time_after.next_to(tube_after, UP, buff=0.3)

        self.play(FadeIn(tube_before), FadeIn(lbl_before), FadeIn(time_before),
                  run_time=0.8)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.6)
        self.play(FadeIn(tube_after), FadeIn(lbl_after), FadeIn(time_after),
                  run_time=0.8)

        # Result callout
        result = callout("ПОЗИТИВНО: содржи скроб",
                         width=8.0, border=GREEN, font_size=28)
        result.shift(RIGHT * 3.5 + DOWN * 2.4)
        # Actually center the result below
        result.move_to(DOWN * 2.4)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.8)
        self.wait(1.0)

        # Negative case (apple)
        neg = Text("Јаболко + јод → без промена → НЕМА скроб",
                   font_size=22, color=GREY)
        neg.move_to(DOWN * 3.4)
        self.play(FadeIn(neg), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, tube_before, lbl_before, time_before,
            arrow, arrow_lbl, tube_after, lbl_after, time_after,
            result, neg)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — Benedict's test (sugar)                ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("benedict_test")

        title = section_title("Бенедиктов тест — шеќер")
        self.play(Write(title), run_time=0.8)

        # Before — blue
        tube_b = make_tube(BLUE, 0.75)
        tube_b.shift(LEFT * 4.0 + DOWN * 0.3)
        lbl_b = Text("Грозје + Бенедиктов", font_size=20, color=WHITE2)
        lbl_b.next_to(tube_b, DOWN, buff=0.3)
        t_b = Text("сино", font_size=20, color=BLUE)
        t_b.next_to(tube_b, UP, buff=0.3)

        # Heat flame under tube
        flame = VGroup(
            Triangle(color=RED, fill_color=RED, fill_opacity=0.7),
            Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=0.9),
        )
        for f in flame:
            f.scale(0.35)
        flame.move_to(tube_b.get_bottom() + DOWN * 0.6)

        # Arrow
        arrow = Arrow(LEFT * 2.4, RIGHT * 0.4, color=YELLOW, stroke_width=4,
                      buff=0.2).shift(DOWN * 0.3)
        arrow_lbl = Text("загревање", font_size=20, color=YELLOW)
        arrow_lbl.next_to(arrow, UP, buff=0.15)

        # After — brick red
        tube_a = make_tube(RED, 0.9)
        tube_a.shift(RIGHT * 2.6 + DOWN * 0.3)
        lbl_a = Text("Тула-црвено", font_size=22, color=RED, weight=BOLD)
        lbl_a.next_to(tube_a, DOWN, buff=0.3)
        t_a = Text("после", font_size=20, color=GREY)
        t_a.next_to(tube_a, UP, buff=0.3)

        self.play(FadeIn(tube_b), FadeIn(lbl_b), FadeIn(t_b), run_time=0.7)
        self.play(FadeIn(flame), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.6)
        self.play(FadeIn(tube_a), FadeIn(lbl_a), FadeIn(t_a), run_time=0.7)

        result = callout("ПОЗИТИВНО: содржи шеќер",
                         width=8.0, border=GREEN, font_size=28)
        result.move_to(DOWN * 2.6)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.8)

        scale = Text("сино → зелено → жолто → тула-црвено",
                     font_size=22, color=WHITE2)
        scale.move_to(DOWN * 3.5)
        self.play(FadeIn(scale), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, tube_b, lbl_b, t_b, flame,
            arrow, arrow_lbl, tube_a, lbl_a, t_a,
            result, scale)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — grease spot test                    ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("grease_test")

        title = section_title("Тест за маст — мрсна дамка")
        self.play(Write(title), run_time=0.8)

        # Paper sheets
        paper1 = Rectangle(width=2.4, height=3.2,
                           fill_color=WHITE2, fill_opacity=0.95,
                           stroke_color=GREY, stroke_width=2)
        paper1.shift(LEFT * 3.5 + DOWN * 0.2)

        paper2 = Rectangle(width=2.4, height=3.2,
                           fill_color=WHITE2, fill_opacity=0.95,
                           stroke_color=GREY, stroke_width=2)
        paper2.shift(RIGHT * 3.5 + DOWN * 0.2)

        # Sample labels
        lbl1 = Text("Путер", font_size=24, color=ORANGE, weight=BOLD)
        lbl1.next_to(paper1, UP, buff=0.3)
        lbl2 = Text("Вода", font_size=24, color=BLUE, weight=BOLD)
        lbl2.next_to(paper2, UP, buff=0.3)

        self.play(FadeIn(paper1), FadeIn(paper2),
                  FadeIn(lbl1), FadeIn(lbl2), run_time=0.9)

        # Spots appear
        butter_spot = Circle(radius=0.5, fill_color=ORANGE, fill_opacity=0.6,
                             stroke_color=ORANGE, stroke_width=1)
        butter_spot.move_to(paper1.get_center())

        water_spot = Circle(radius=0.5, fill_color=BLUE, fill_opacity=0.5,
                            stroke_color=BLUE, stroke_width=1)
        water_spot.move_to(paper2.get_center())

        self.play(FadeIn(butter_spot), FadeIn(water_spot), run_time=0.7)
        self.wait(0.5)

        # Wait label
        wait_lbl = Text("чекај да се исуши...", font_size=22, color=YELLOW)
        wait_lbl.move_to(DOWN * 2.4)
        self.play(FadeIn(wait_lbl), run_time=0.5)
        self.wait(0.8)

        # Water evaporates, butter spot stays (now translucent)
        butter_perm = Circle(radius=0.5, fill_color=ORANGE, fill_opacity=0.35,
                             stroke_color=ORANGE, stroke_width=2)
        butter_perm.move_to(paper1.get_center())

        self.play(
            FadeOut(water_spot),
            Transform(butter_spot, butter_perm),
            run_time=1.2,
        )

        # Results
        res1 = Text("трајна дамка → МАСТ",
                    font_size=22, color=GREEN, weight=BOLD)
        res1.next_to(paper1, DOWN, buff=0.3)
        res2 = Text("без дамка → НЕМА",
                    font_size=22, color=GREY)
        res2.next_to(paper2, DOWN, buff=0.3)

        self.play(FadeOut(wait_lbl),
                  FadeIn(res1), FadeIn(res2), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, paper1, paper2, lbl1, lbl2,
            butter_spot, res1, res2)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Јод + скроб → синочерно.",
                 font_size=30, color=PURPLE, weight=BOLD),
            Text("Бенедиктов + шеќер → тула-црвено.",
                 font_size=28, color=RED),
            Text("Маст на хартија → трајна дамка.",
                 font_size=28, color=ORANGE),
            Text("Бојата открива составот.",
                 font_size=32, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
