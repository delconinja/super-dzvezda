"""
bio8-6-1  —  Зошто класифицираме?
Биологија 8, Единица 6: Класификација

Teaching narrative — Andonovski-style: three-beat punches,
classification as detective work, Linnaeus as the founding father.
Render:  manim -ql bio8-6-1.py Bio861Scene
Output:  media/videos/bio8-6-1/480p15/Bio861Scene.mp4
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


class Bio861Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — eight million species                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Осум милиони видови.",
                     font_size=50, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.4)

        beats = VGroup(
            Text("Без редослед — хаос.",         font_size=40, color=RED, weight=BOLD),
            Text("Линеј даде систем.",            font_size=42, color=GREEN, weight=BOLD),
            Text("Едно име на латински.",         font_size=38, color=WHITE2),
            Text("Целиот свет разбира.",          font_size=38, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.2)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHY CLASSIFY — three reasons                    ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        title = section_title("Зошто класифицираме?")
        self.play(Write(title), run_time=0.8)

        reasons = [
            ("Подредување",   "Од хаос — ред",                YELLOW),
            ("Споделување",   "Заеднички јазик на науката",   GREEN),
            ("Предвидување",  "Слични видови — слични својства", BLUE),
        ]

        cards = VGroup()
        for name, desc, color in reasons:
            card = RoundedRectangle(
                width=4.0, height=2.4, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            n = Text(name, font_size=30, color=color, weight=BOLD)
            d = Text(desc, font_size=20, color=WHITE2)
            txt = VGroup(n, d).arrange(DOWN, buff=0.3)
            txt.move_to(card)
            cards.add(VGroup(card, txt))

        cards.arrange(RIGHT, buff=0.4).next_to(title, DOWN, buff=0.7)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)
        self.wait(1.2)

        punch = Text("Класификацијата не е етикета — таа е алатка.",
                     font_size=28, color=ORANGE, weight=BOLD)
        punch.next_to(cards, DOWN, buff=0.6)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, cards, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  LINNAEUS — the founder                          ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("linnaeus")

        title2 = section_title("Карл Линеј", color=GREEN)
        self.play(Write(title2), run_time=0.8)

        # Portrait silhouette
        portrait = Circle(radius=1.1, color=YELLOW, fill_color="#1a3a5a",
                          fill_opacity=1, stroke_width=3)
        body = Polygon(
            np.array([-1.4, -1.1, 0]),
            np.array([1.4, -1.1, 0]),
            np.array([1.0, -2.6, 0]),
            np.array([-1.0, -2.6, 0]),
            color=YELLOW, fill_color="#1a3a5a", fill_opacity=1, stroke_width=3,
        )
        figure = VGroup(portrait, body)
        figure.next_to(title2, DOWN, buff=0.4).to_edge(LEFT, buff=1.2)

        self.play(Create(figure), run_time=1.0)

        info_lines = VGroup(
            Text("1707 — 1778", font_size=26, color=YELLOW),
            Text("Шведски ботаничар", font_size=24, color=WHITE2),
            Text("'Татко на таксономијата'", font_size=24, color=GREEN, weight=BOLD),
            Text("Systema Naturae, 1735", font_size=22, color=BLUE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        info_lines.next_to(figure, RIGHT, buff=0.8)

        for line in info_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        quote_box = callout("Едно име. Една наука. Цел свет.",
                            width=10.0, border=GREEN, font_size=30)
        quote_box.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(quote_box), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, figure, info_lines, quote_box)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  BINOMIAL NOMENCLATURE                            ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("binomial")

        title3 = section_title("Биномна номенклатура", color=BLUE)
        self.play(Write(title3), run_time=0.8)

        subtitle = Text("Две имиња. Латински. Засекогаш.",
                        font_size=28, color=WHITE2)
        subtitle.next_to(title3, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(0.5)

        # The formula
        formula = MathTex(
            r"\underbrace{Homo}_{\text{род}}\ \underbrace{sapiens}_{\text{вид}}",
            font_size=64, color=YELLOW,
        )
        formula.next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(formula), run_time=1.4)
        self.wait(1.0)

        rules = VGroup(
            Text("• Род — со голема буква", font_size=24, color=GREEN),
            Text("• Вид — со мала буква",   font_size=24, color=GREEN),
            Text("• Двете — закосени (italic)", font_size=24, color=GREEN),
            Text("• Латински — јазик кој не се менува", font_size=24, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rules.next_to(formula, DOWN, buff=0.7)

        for r in rules:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, subtitle, formula, rules)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  EXAMPLES of binomial names                       ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("examples")

        title4 = section_title("Примери", color=PURPLE)
        self.play(Write(title4), run_time=0.8)

        examples = [
            ("Canis lupus",         "Волк",         GREY),
            ("Felis catus",         "Домашна мачка", ORANGE),
            ("Quercus robur",       "Даб",          GREEN),
            ("Apis mellifera",      "Медоносна пчела", YELLOW),
            ("Tursiops truncatus",  "Делфин",       BLUE),
        ]

        rows = VGroup()
        for latin, mk, color in examples:
            row = RoundedRectangle(
                width=11.0, height=0.85, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=2,
            )
            lat = Text(latin, font_size=28, color=color, weight=BOLD, slant=ITALIC)
            arrow = Text("→", font_size=28, color=WHITE2)
            name = Text(mk, font_size=26, color=WHITE2)
            content = VGroup(lat, arrow, name).arrange(RIGHT, buff=0.5)
            content.move_to(row)
            rows.add(VGroup(row, content))

        rows.arrange(DOWN, buff=0.2).next_to(title4, DOWN, buff=0.6)

        for r in rows:
            self.play(FadeIn(r, shift=LEFT * 0.3), run_time=0.5)
            self.wait(0.15)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title4, rows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  TAXONOMIC HIERARCHY — 8 levels                   ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hierarchy")

        title5 = section_title("Таксономска хиерархија", color=ORANGE)
        self.play(Write(title5), run_time=0.8)

        subtitle5 = Text("Од најшироко — до најтесно",
                         font_size=26, color=WHITE2)
        subtitle5.next_to(title5, DOWN, buff=0.25)
        self.play(FadeIn(subtitle5), run_time=0.6)

        levels = [
            ("Домен",   "Eukarya",    "#ffd54f"),
            ("Царство", "Animalia",   "#ffb74d"),
            ("Тип",     "Chordata",   "#e57373"),
            ("Класа",   "Mammalia",   "#ce93d8"),
            ("Ред",     "Primates",   "#4fc3f7"),
            ("Фамилија","Hominidae",  "#81c784"),
            ("Род",     "Homo",       "#90a4ae"),
            ("Вид",     "sapiens",    "#ffd54f"),
        ]

        boxes = VGroup()
        max_w = 10.5
        for i, (mk, latin, color) in enumerate(levels):
            w = max_w - i * 0.7
            box = RoundedRectangle(
                width=w, height=0.55, corner_radius=0.1,
                fill_color=color, fill_opacity=0.85,
                stroke_color=WHITE2, stroke_width=1,
            )
            mk_t = Text(mk, font_size=22, color="#0d1b2e", weight=BOLD)
            la_t = Text(latin, font_size=20, color="#0d1b2e", slant=ITALIC)
            content = VGroup(mk_t, Text(" — ", font_size=20, color="#0d1b2e"), la_t).arrange(RIGHT, buff=0.15)
            content.move_to(box)
            boxes.add(VGroup(box, content))

        boxes.arrange(DOWN, buff=0.12).next_to(subtitle5, DOWN, buff=0.4)
        boxes.scale(0.85).next_to(subtitle5, DOWN, buff=0.3)

        for b in boxes:
            self.play(FadeIn(b, shift=DOWN * 0.15), run_time=0.4)
            self.wait(0.1)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title5, subtitle5, boxes)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE — one-word finisher                        ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        close1 = Text("Без класификација —",
                      font_size=42, color=GREY, weight=BOLD)
        close2 = Text("науката е метеж.",
                      font_size=42, color=RED, weight=BOLD)
        close3 = Text("Со неа —",
                      font_size=42, color=GREEN, weight=BOLD)
        close4 = Text("ред.",
                      font_size=72, color=YELLOW, weight=BOLD)
        close_group = VGroup(close1, close2, close3, close4).arrange(DOWN, buff=0.5)

        for line in close_group:
            self.play(Write(line), run_time=0.9)
            self.wait(0.35)
        self.wait(2.0)

        self.play(FadeOut(close_group), run_time=1.0)
        self.wait(0.5)
