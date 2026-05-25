"""
bio8-1-3  —  Хемиски рецептори — вкус и мирис
Биологија 8, Единица 1: Сетила и нервна координација

Teaching narrative — Andonovski-style: three-beat punches,
taste as story, smell as silent boss, molecules as keys.
Render:  manim -ql bio8-1-3.py Bio813Scene
Output:  media/videos/bio8-1-3/480p15/Bio813Scene.mp4
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
PINK    = "#f48fb1"


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


class Bio813Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Без мирис — нема вкус.",
                     font_size=46, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.5)
        self.wait(0.4)

        beats = VGroup(
            Text("Затвори нос.",                  font_size=38, color=WHITE2),
            Text("Изеди јаболко.",                font_size=38, color=GREEN),
            Text("Како картон.",                  font_size=38, color=GREY),
            Text("Мирисот е тивкиот шеф на вкусот.",
                 font_size=32, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — chemical receptors                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е хемиски рецептор?")
        self.play(Write(title), run_time=0.8)

        defn = callout(
            "Клетка што препознава одредена хемикалија.",
            width=11.5, font_size=28, border=YELLOW,
        )
        defn.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.9)
        self.wait(0.6)

        # lock and key analogy
        lock = RoundedRectangle(
            width=2.0, height=2.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=3,
        ).shift(LEFT * 2.5 + DOWN * 1.4)
        # carve out a "keyhole" - decorative
        keyhole = VGroup(
            Circle(radius=0.2, color=BLUE, stroke_width=3),
            Rectangle(width=0.15, height=0.5, color=BLUE, stroke_width=3,
                      fill_opacity=0).next_to(Circle(radius=0.2), DOWN, buff=0),
        ).move_to(lock.get_center())

        key = VGroup(
            Circle(radius=0.3, color=YELLOW, stroke_width=3, fill_color=YELLOW, fill_opacity=0.4),
            Rectangle(width=0.9, height=0.18, color=YELLOW, stroke_width=3,
                      fill_color=YELLOW, fill_opacity=0.4),
        )
        key[1].next_to(key[0], RIGHT, buff=-0.05)
        key.move_to(RIGHT * 3.0 + DOWN * 1.4)

        lbl_lock = Text("Рецептор", font_size=22, color=BLUE).next_to(lock, DOWN, buff=0.3)
        lbl_key = Text("Молекула (вкус/мирис)", font_size=22, color=YELLOW).next_to(key, DOWN, buff=0.3)

        self.play(Create(lock), Create(keyhole), FadeIn(lbl_lock), run_time=0.9)
        self.play(FadeIn(key, shift=LEFT * 0.3), FadeIn(lbl_key), run_time=0.9)
        self.wait(0.5)

        # key moves into lock
        self.play(key.animate.move_to(lock.get_center() + RIGHT * 0.4),
                  run_time=1.0)
        self.play(Indicate(lock, color=GREEN, scale_factor=1.1),
                  Indicate(key, color=GREEN, scale_factor=1.1),
                  run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, defn, lock, keyhole, key, lbl_lock, lbl_key)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — 5 tastes                            ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Пет основни вкуси")
        self.play(Write(title), run_time=0.8)

        # tongue shape (oval)
        tongue = Ellipse(width=5.0, height=3.2,
                         fill_color=PINK, fill_opacity=0.5,
                         stroke_color=PINK, stroke_width=3)
        tongue.shift(LEFT * 3.2 + DOWN * 0.4)

        # taste buds (small dots scattered)
        buds = VGroup()
        np.random.seed(7)
        for _ in range(40):
            x = (np.random.random() - 0.5) * 4.2
            y = (np.random.random() - 0.5) * 2.4
            if (x * x) / (2.5 ** 2) + (y * y) / (1.6 ** 2) < 0.85:
                d = Dot(point=tongue.get_center() + np.array([x, y, 0]),
                        color=RED, radius=0.05)
                buds.add(d)

        self.play(Create(tongue), run_time=0.9)
        self.play(FadeIn(buds), run_time=0.6)

        # 5 taste cards on the right
        tastes = [
            ("Слатко",   "шеќер, овошје",   GREEN),
            ("Кисело",   "лимон, оцет",     YELLOW),
            ("Солено",   "сол, маслинки",   BLUE),
            ("Горчливо", "кафе, лек",       PURPLE),
            ("Умами",    "месо, сирење",    ORANGE),
        ]
        cards = VGroup()
        for name, ex, col in tastes:
            box = RoundedRectangle(
                width=4.5, height=0.75, corner_radius=0.15,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=22, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.0)
            e = Text(ex, font_size=20, color=WHITE2)
            e.move_to(box.get_left() + RIGHT * 3.0)
            cards.add(VGroup(box, n, e))
        cards.arrange(DOWN, buff=0.18).shift(RIGHT * 3.3 + DOWN * 0.2)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.7)

        # myth-busting note
        myth = callout(
            "Мит: мапа на јазикот. Сите пупки примаат сè.",
            width=10.5, border=RED, font_size=24,
        )
        myth.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(myth, shift=UP * 0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, tongue, buds, cards, myth)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — smell pathway                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Како мирисаш?")
        self.play(Write(title), run_time=0.8)

        # cross-section nose
        # outer outline
        nose = VMobject(stroke_color=WHITE2, stroke_width=2.5)
        pts = [
            LEFT * 3.5 + DOWN * 0.5,
            LEFT * 3.0 + UP * 0.3,
            LEFT * 1.5 + UP * 1.2,
            RIGHT * 0.5 + UP * 1.0,
            RIGHT * 0.8 + DOWN * 0.2,
            RIGHT * 0.0 + DOWN * 1.2,
            LEFT * 1.5 + DOWN * 1.5,
            LEFT * 3.0 + DOWN * 1.2,
            LEFT * 3.5 + DOWN * 0.5,
        ]
        nose.set_points_smoothly(pts)
        nose.shift(LEFT * 1.0)

        # olfactory bulb (top inside)
        bulb = Ellipse(width=1.6, height=0.5,
                       fill_color=PURPLE, fill_opacity=0.85,
                       stroke_color=WHITE2, stroke_width=2)
        bulb.shift(LEFT * 1.5 + UP * 0.75)

        # hairs (olfactory receptors)
        hairs = VGroup()
        for x in np.linspace(-2.2, -0.7, 8):
            h = Line([x, 0.5, 0], [x, 0.7, 0], color=YELLOW, stroke_width=2)
            hairs.add(h)

        # molecules entering
        molecules = VGroup()
        for i in range(5):
            m = Circle(radius=0.12, color=GREEN, fill_color=GREEN, fill_opacity=0.7,
                       stroke_width=1)
            m.move_to(LEFT * 2.5 + DOWN * 1.0 + RIGHT * (i * 0.3))
            molecules.add(m)

        self.play(Create(nose), run_time=1.0)
        self.play(FadeIn(bulb), Create(hairs), run_time=0.8)
        self.play(FadeIn(molecules), run_time=0.5)

        # molecules drift up
        self.play(
            *[m.animate.move_to(hairs[i % 8].get_top()) for i, m in enumerate(molecules)],
            run_time=1.4
        )
        self.play(Indicate(bulb, color=YELLOW, scale_factor=1.2), run_time=0.8)

        # bulb -> brain arrow
        brain_box = callout("Мозок", width=2.0, border=PURPLE, font_size=24)
        brain_box.move_to(RIGHT * 4.0 + UP * 0.7)
        bulb_arrow = Arrow(bulb.get_right(), brain_box.get_left(),
                           buff=0.15, color=PURPLE, stroke_width=4)
        self.play(GrowArrow(bulb_arrow), FadeIn(brain_box), run_time=0.9)

        # labels
        lbl_b = Text("Олфакторна луковица", font_size=20, color=PURPLE)
        lbl_b.next_to(bulb, UP, buff=0.3)
        lbl_h = Text("Рецепторни клетки", font_size=20, color=YELLOW)
        lbl_h.move_to(DOWN * 2.3 + LEFT * 1.5)
        arr_h = Arrow(lbl_h.get_top(), hairs[3].get_bottom(),
                      buff=0.1, color=YELLOW, stroke_width=2,
                      max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(lbl_b), run_time=0.5)
        self.play(FadeIn(lbl_h), GrowArrow(arr_h), run_time=0.7)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, nose, bulb, hairs, molecules,
            brain_box, bulb_arrow, lbl_b, lbl_h, arr_h,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — taste-smell connection             ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("80% од вкусот е мирис")
        self.play(Write(title), run_time=0.8)

        # bar showing breakdown
        bar_bg = Rectangle(width=9.0, height=0.9,
                           fill_color=DARK_CARD, fill_opacity=1,
                           stroke_color=WHITE2, stroke_width=2)
        bar_bg.shift(UP * 0.5)

        smell_part = Rectangle(width=7.2, height=0.9,
                               fill_color=ORANGE, fill_opacity=1,
                               stroke_width=0)
        smell_part.align_to(bar_bg, LEFT)
        smell_part.shift(UP * 0.5)

        taste_part = Rectangle(width=1.8, height=0.9,
                               fill_color=PINK, fill_opacity=1,
                               stroke_width=0)
        taste_part.next_to(smell_part, RIGHT, buff=0)
        taste_part.shift(UP * 0 - UP * 0)  # align

        lbl_smell = Text("Мирис 80%", font_size=24, color="#0d1b2e", weight=BOLD)
        lbl_smell.move_to(smell_part)
        lbl_taste = Text("Вкус 20%", font_size=18, color="#0d1b2e", weight=BOLD)
        lbl_taste.move_to(taste_part)

        self.play(Create(bar_bg), run_time=0.6)
        self.play(FadeIn(smell_part), Write(lbl_smell), run_time=0.8)
        self.play(FadeIn(taste_part), Write(lbl_taste), run_time=0.6)
        self.wait(0.6)

        why = callout(
            "Затоа храна нема вкус кога си настинат.",
            width=10.5, border=BLUE, font_size=26,
        )
        why.next_to(bar_bg, DOWN, buff=0.7)
        self.play(FadeIn(why, shift=UP * 0.2), run_time=0.9)
        self.wait(0.5)

        experiment = callout(
            "Експеримент: затвори нос, изеди јаболко и круша.",
            width=10.5, border=GREEN, font_size=24,
        )
        experiment.next_to(why, DOWN, buff=0.3)
        self.play(FadeIn(experiment, shift=UP * 0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            title, bar_bg, smell_part, taste_part, lbl_smell, lbl_taste,
            why, experiment,
        )), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                         ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("Пет вкуси. Не четири.",
                 font_size=32, color=YELLOW, weight=BOLD),
            Text("Молекула + рецептор = клуч и брава.",
                 font_size=28, color=BLUE),
            Text("Мирисот командува со вкус.",
                 font_size=28, color=ORANGE),
            Text("Тивко. Но секогаш.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
