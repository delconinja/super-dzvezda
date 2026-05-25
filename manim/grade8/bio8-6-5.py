"""
bio8-6-5  —  Биодиверзитет и зачувување
Биологија 8, Единица 6: Класификација

Teaching narrative — Andonovski-style: biodiversity as insurance,
extinction as silent collapse, conservation as duty.
Render:  manim -ql bio8-6-5.py Bio865Scene
Output:  media/videos/bio8-6-5/480p15/Bio865Scene.mp4
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


class Bio865Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — biodiversity = insurance                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Биодиверзитет не е луксуз.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook2 = Text("Биодиверзитет е осигурување.",
                     font_size=42, color=GREEN, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.4)
        hook_group.to_edge(UP, buff=0.7)

        for h in hook_group:
            self.play(Write(h), run_time=1.2)
            self.wait(0.3)
        self.wait(0.5)

        beats = VGroup(
            Text("Без него — еден вирус ја брише цела жетва.",
                 font_size=30, color=RED, weight=BOLD),
            Text("Со него — природата има резерва.",
                 font_size=30, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(hook_group, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.9)
            self.wait(0.3)
        self.wait(1.5)

        self.play(FadeOut(VGroup(hook_group, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  WHAT IS BIODIVERSITY                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е биодиверзитет?")
        self.play(Write(title), run_time=0.8)

        defn = callout("Разновидноста на сите живи организми на Земјата.",
                       width=12.0, border=GREEN, font_size=28)
        defn.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(defn), run_time=0.9)
        self.wait(0.7)

        levels = [
            ("Генетски",  "разлики во гените", BLUE),
            ("Видов",     "број на различни видови", GREEN),
            ("Екосистемски", "разни средини и врски", ORANGE),
        ]

        cards = VGroup()
        for name, desc, color in levels:
            card = RoundedRectangle(
                width=4.0, height=2.2, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            n = Text(name, font_size=26, color=color, weight=BOLD)
            d = Text(desc, font_size=18, color=WHITE2)
            txt = VGroup(n, d).arrange(DOWN, buff=0.3)
            txt.move_to(card)
            cards.add(VGroup(card, txt))

        cards.arrange(RIGHT, buff=0.3).next_to(defn, DOWN, buff=0.6)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, defn, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  THREATS — five dangers                          ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("threats")

        title2 = section_title("Закани", color=RED)
        self.play(Write(title2), run_time=0.8)

        threats = [
            ("Губење на живеалиштата",  "сечење шуми, градби",          RED),
            ("Климатски промени",        "затоплување, суши",            ORANGE),
            ("Загадување",               "вода, воздух, почва",          GREY),
            ("Инвазивни видови",         "странци кои нарушуваат",      PURPLE),
            ("Прекумерно искористување", "лов, риболов без мера",        YELLOW),
        ]

        rows = VGroup()
        for name, desc, color in threats:
            row = RoundedRectangle(
                width=11.0, height=0.9, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            warn = Text("!", font_size=32, color=color, weight=BOLD)
            n = Text(name, font_size=24, color=color, weight=BOLD)
            d = Text(desc, font_size=20, color=WHITE2)
            content = VGroup(warn, n, Text(" — ", font_size=20, color=WHITE2), d).arrange(RIGHT, buff=0.3)
            content.move_to(row)
            rows.add(VGroup(row, content))

        rows.arrange(DOWN, buff=0.18).next_to(title2, DOWN, buff=0.5)

        for r in rows:
            self.play(FadeIn(r, shift=LEFT * 0.3), run_time=0.55)
            self.wait(0.15)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, rows)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  EXTINCTION CURVE                                ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("extinction")

        title3 = section_title("Стапка на изумирање", color=ORANGE)
        self.play(Write(title3), run_time=0.8)

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"color": GREY, "stroke_width": 2},
        )
        ax.shift(DOWN * 0.4)
        x_lbl = Text("време", font_size=22, color=WHITE2)
        x_lbl.next_to(ax.x_axis, RIGHT, buff=0.2)
        y_lbl = Text("видови што изумираат", font_size=20, color=WHITE2)
        y_lbl.next_to(ax.y_axis, UP, buff=0.2).shift(LEFT * 0.5)

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.0)

        # Slow rise, then sharp upturn
        curve = ax.plot(
            lambda x: 0.2 + 0.15 * x + 0.05 * x ** 3,
            x_range=[0, 4.5],
            color=RED, stroke_width=5,
        )
        self.play(Create(curve), run_time=1.5)
        self.wait(0.4)

        marker = Dot(ax.c2p(4.3, 0.2 + 0.15 * 4.3 + 0.05 * 4.3 ** 3),
                     color=YELLOW, radius=0.13)
        now_lbl = Text("денес", font_size=24, color=YELLOW, weight=BOLD)
        now_lbl.next_to(marker, UP, buff=0.2)

        self.play(FadeIn(marker, scale=0.5), Write(now_lbl), run_time=0.8)
        self.wait(0.5)

        warn = Text("100 — 1000 пати побрзо од природно.",
                    font_size=26, color=RED, weight=BOLD)
        warn.next_to(ax, DOWN, buff=0.5)
        self.play(Write(warn), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, ax, x_lbl, y_lbl, curve,
                                  marker, now_lbl, warn)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  CONSERVATION MEASURES                            ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conservation")

        title4 = section_title("Зачувување", color=GREEN)
        self.play(Write(title4), run_time=0.8)

        measures = [
            ("Заштитени подрачја",      "национални паркови, резервати", GREEN),
            ("Програми за размножување", "зоо-градини, банки на семе",    BLUE),
            ("IUCN — Црвена листа",      "регистар на загрозени видови",  RED),
            ("Закони и образование",     "правила и свест",               YELLOW),
        ]

        cards4 = VGroup()
        for name, desc, color in measures:
            card = RoundedRectangle(
                width=5.4, height=1.5, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            n = Text(name, font_size=22, color=color, weight=BOLD)
            d = Text(desc, font_size=18, color=WHITE2)
            content = VGroup(n, d).arrange(DOWN, buff=0.2)
            content.move_to(card)
            cards4.add(VGroup(card, content))

        # 2x2 grid
        cards4[0].next_to(title4, DOWN, buff=0.6).shift(LEFT * 2.9)
        cards4[1].next_to(cards4[0], RIGHT, buff=0.3)
        cards4[2].next_to(cards4[0], DOWN, buff=0.3)
        cards4[3].next_to(cards4[2], RIGHT, buff=0.3)

        for c in cards4:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.6)
            self.wait(0.18)
        self.wait(1.0)

        # Red List colour key
        key_title = Text("Категории на IUCN", font_size=24,
                         color=ORANGE, weight=BOLD)
        key_title.next_to(cards4, DOWN, buff=0.5)
        self.play(FadeIn(key_title), run_time=0.5)

        cats = VGroup()
        cat_data = [
            ("EX",  "изумрен",       "#000000"),
            ("CR",  "критично",      RED),
            ("EN",  "загрозен",      ORANGE),
            ("VU",  "ранлив",        YELLOW),
            ("LC",  "стабилен",      GREEN),
        ]
        for code, mk, color in cat_data:
            chip = RoundedRectangle(
                width=1.5, height=0.55, corner_radius=0.1,
                fill_color=color if color != "#000000" else "#222222",
                fill_opacity=0.95,
                stroke_color=WHITE2, stroke_width=1,
            )
            c_txt = Text(code, font_size=18, color=WHITE2, weight=BOLD)
            chip_grp = VGroup(chip, c_txt)
            c_txt.move_to(chip)
            mk_txt = Text(mk, font_size=16, color=WHITE2)
            full = VGroup(chip_grp, mk_txt).arrange(DOWN, buff=0.15)
            cats.add(full)

        cats.arrange(RIGHT, buff=0.3).next_to(key_title, DOWN, buff=0.25)

        for c in cats:
            self.play(FadeIn(c, shift=DOWN * 0.15), run_time=0.4)
            self.wait(0.08)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title4, cards4, key_title, cats)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  MACEDONIA'S BIODIVERSITY                         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("macedonia")

        title5 = section_title("Македонија — мала, но богата", color=PURPLE)
        self.play(Write(title5), run_time=0.9)

        # Simplified Macedonia outline (rough)
        mk_outline = Polygon(
            np.array([-2.5, 1.0, 0]),
            np.array([2.5, 1.2, 0]),
            np.array([3.0, -0.5, 0]),
            np.array([1.5, -1.5, 0]),
            np.array([-2.0, -1.3, 0]),
            np.array([-2.8, 0.0, 0]),
            color=PURPLE, fill_color="#1a3a5a", fill_opacity=0.6,
            stroke_width=3,
        )
        mk_outline.shift(LEFT * 2.5 + DOWN * 0.3)

        # Dots for protected areas
        dots = VGroup(
            Dot(mk_outline.get_center() + np.array([-1.3, 0.3, 0]),
                color=GREEN, radius=0.12),
            Dot(mk_outline.get_center() + np.array([0.2, 0.5, 0]),
                color=GREEN, radius=0.12),
            Dot(mk_outline.get_center() + np.array([1.5, -0.3, 0]),
                color=GREEN, radius=0.12),
            Dot(mk_outline.get_center() + np.array([0.5, -0.8, 0]),
                color=GREEN, radius=0.12),
        )

        self.play(Create(mk_outline), run_time=1.0)
        for d in dots:
            self.play(FadeIn(d, scale=0.5), run_time=0.25)
        self.wait(0.4)

        stats = VGroup(
            Text("• Преку 200 риби, птици, цицачи", font_size=22, color=BLUE),
            Text("• 3 национални парка", font_size=22, color=GREEN, weight=BOLD),
            Text("  Маврово, Пелистер, Галичица", font_size=18, color=WHITE2),
            Text("• Ендемични видови — пр. охридска пастрмка",
                 font_size=22, color=YELLOW),
            Text("• Охридско Езеро — жив музеј",
                 font_size=22, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        stats.next_to(mk_outline, RIGHT, buff=0.6)

        for s in stats:
            self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title5, mk_outline, dots, stats)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE — call to action                           ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        close1 = Text("Секој вид —",
                      font_size=40, color=BLUE, weight=BOLD)
        close2 = Text("една нишка во мрежата.",
                      font_size=36, color=GREEN, weight=BOLD)
        close3 = Text("Кога нишка пука —",
                      font_size=34, color=ORANGE)
        close4 = Text("мрежата ослабнува.",
                      font_size=34, color=RED, weight=BOLD)
        close5 = Text("Зачувај ја.",
                      font_size=64, color=YELLOW, weight=BOLD)
        cg = VGroup(close1, close2, close3, close4, close5).arrange(DOWN, buff=0.4)

        for line in cg:
            self.play(Write(line), run_time=0.85)
            self.wait(0.3)
        self.wait(2.0)

        self.play(FadeOut(cg), run_time=1.0)
        self.wait(0.5)
