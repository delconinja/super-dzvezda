"""
bio8-7-3  —  Записи од фосили и староста на Земјата
Биологија 8, Единица 7: Запис во карпите

Teaching narrative — Andonovski-style: three-beat punches,
deep time as epic, geological eras as chapters.
Render:  manim -ql bio8-7-3.py Bio873Scene
Output:  media/videos/bio8-7-3/480p15/Bio873Scene.mp4
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


def stratum(width, height, color, y, label_txt=None, label_color=WHITE2):
    band = Rectangle(
        width=width, height=height,
        fill_color=color, fill_opacity=0.9,
        stroke_color=BLACK, stroke_width=1,
    ).move_to([0, y, 0])
    if label_txt:
        lbl = Text(label_txt, font_size=20, color=label_color, weight=BOLD)
        lbl.next_to(band, RIGHT, buff=0.3)
        return VGroup(band, lbl)
    return band


class Bio873Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — deep time                                 ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Земјата е стара 4.6 милијарди години.",
                     font_size=42, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.4)
        self.wait(0.5)

        beats = VGroup(
            Text("Динозаурите живееле 165 милиони.",   font_size=36, color=GREEN),
            Text("Луѓето — 300.000.",                   font_size=36, color=BLUE),
            Text("Тивка приказна.",                     font_size=40, color=ORANGE, weight=BOLD),
            Text("Запишана во камен.",                  font_size=44, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.15), run_time=0.6)
            self.wait(0.3)
        self.wait(1.4)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  EARTH AGE — 4.6 billion                          ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("earth-age")

        t2 = section_title("Колку е стара Земјата?", color=BLUE)
        self.play(Write(t2), run_time=0.7)

        age_text = MathTex(r"4{,}6 \times 10^{9}", r"\ \text{години}",
                           font_size=72, color=YELLOW)
        age_text.move_to(UP * 0.5)
        self.play(Write(age_text), run_time=1.4)
        self.wait(0.8)

        explain = VGroup(
            Text("4.600.000.000 години.", font_size=36, color=ORANGE),
            Text("Тоа е број што не се замислува.", font_size=30, color=WHITE2),
        ).arrange(DOWN, buff=0.3).next_to(age_text, DOWN, buff=0.7)

        self.play(FadeIn(explain[0], shift=UP * 0.15), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(explain[1], shift=UP * 0.15), run_time=0.7)
        self.wait(1.0)

        analogy = callout(
            "Ако Земјата живеела 24 часа — човекот доаѓа во последните 2 секунди.",
            width=12, border=PURPLE, font_size=24,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(analogy, shift=UP * 0.2), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t2, age_text, explain, analogy)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  STRATIGRAPHY — rock layers                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("strata")

        t3 = section_title("Слоеви — книгата на Земјата", color=ORANGE)
        self.play(Write(t3), run_time=0.7)

        intro = Text("Карпите се редат во слоеви. Како страници.",
                     font_size=28, color=WHITE2)
        intro.next_to(t3, DOWN, buff=0.3)
        self.play(FadeIn(intro), run_time=0.7)
        self.wait(0.5)

        # шест слоеви, најдолниот најстар
        layer_data = [
            ("#5d4037", "најстар",   -2.2),
            ("#6d4c41", "",           -1.6),
            ("#8d6e63", "",           -1.0),
            ("#a1887f", "",           -0.4),
            ("#bcaaa4", "",            0.2),
            ("#d7ccc8", "најмлад",     0.8),
        ]
        layers = VGroup()
        layer_labels = VGroup()
        for c, lbl, y in layer_data:
            band = Rectangle(width=8, height=0.55, fill_color=c, fill_opacity=0.95,
                             stroke_color=BLACK, stroke_width=1).move_to([0, y, 0])
            layers.add(band)
            if lbl:
                l = Text(lbl, font_size=22, color=YELLOW, weight=BOLD)
                l.next_to(band, RIGHT, buff=0.3)
                layer_labels.add(l)

        self.play(LaggedStart(*[FadeIn(l, shift=DOWN * 0.2) for l in layers], lag_ratio=0.18), run_time=1.8)
        self.play(FadeIn(layer_labels), run_time=0.6)

        # стрелка покажува време
        arrow_time = Arrow(
            layers[5].get_left() + LEFT * 1.0 + UP * 0.2,
            layers[0].get_left() + LEFT * 1.0 + DOWN * 0.2,
            color=BLUE, buff=0,
        )
        arrow_lbl = Text("време наназад", font_size=22, color=BLUE).next_to(arrow_time, LEFT, buff=0.15)
        self.play(GrowArrow(arrow_time), FadeIn(arrow_lbl), run_time=1.0)

        rule = Text("Подолу = постаро. Погоре = помладо.",
                    font_size=28, color=GREEN, weight=BOLD)
        rule.to_edge(DOWN, buff=0.4)
        self.play(Write(rule), run_time=1.0)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t3, intro, layers, layer_labels, arrow_time, arrow_lbl, rule)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  GEOLOGICAL TIME SCALE — 4 eras                   ~70 s
        # ══════════════════════════════════════════════════════════
        self.next_section("eras")

        t4 = section_title("Геолошки ери", color=PURPLE)
        self.play(Write(t4), run_time=0.7)

        # вертикална трака — горе најстар, долу најмлад
        era_data = [
            ("Прекамбриум",  "4.6 милијарди — 540 милиони",  "Микроби. Прв живот.",          "#3e2723",  YELLOW),
            ("Палеозоик",    "540 — 250 милиони",            "Трилобити. Риби. Растенија.",  "#5d4037",  GREEN),
            ("Мезозоик",     "250 — 66 милиони",             "Динозаури. Господари.",        "#8d6e63",  ORANGE),
            ("Кенозоик",     "66 милиони — денес",           "Цицачи. Птици. Луѓе.",         "#bcaaa4",  BLUE),
        ]

        era_height = 1.2
        era_groups = VGroup()
        start_y = 1.8
        for i, (name, span, life, c, accent) in enumerate(era_data):
            y = start_y - i * (era_height + 0.15)
            band = Rectangle(
                width=12, height=era_height,
                fill_color=c, fill_opacity=0.95,
                stroke_color=accent, stroke_width=2,
            ).move_to([0, y, 0])
            name_t = Text(name, font_size=28, color=accent, weight=BOLD)
            name_t.move_to(band.get_left() + RIGHT * 1.7)
            span_t = Text(span, font_size=20, color=WHITE2)
            span_t.move_to(band.get_center() + LEFT * 0.5)
            life_t = Text(life, font_size=20, color=YELLOW)
            life_t.move_to(band.get_right() + LEFT * 2.0)
            era_groups.add(VGroup(band, name_t, span_t, life_t))

        for eg in era_groups:
            self.play(FadeIn(eg, shift=LEFT * 0.3), run_time=0.7)
            self.wait(0.4)
        self.wait(1.6)

        # punch line
        punch = Text("Секоја ера — поглавје во книгата на животот.",
                     font_size=26, color=YELLOW)
        punch.to_edge(DOWN, buff=0.4)
        self.play(Write(punch), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t4, era_groups, punch)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  INDEX FOSSILS                                    ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("index-fossils")

        t5 = section_title("Водечки фосили", color=GREEN)
        self.play(Write(t5), run_time=0.7)

        intro5 = Text("Некои фосили живееле кратко — но насекаде.",
                      font_size=28, color=WHITE2)
        intro5.next_to(t5, DOWN, buff=0.3)
        self.play(FadeIn(intro5), run_time=0.7)
        self.wait(0.5)

        rule5 = callout(
            "Ако го најдеш — знаеш точно колку е стар слојот.",
            width=11, border=YELLOW, font_size=26,
        ).next_to(intro5, DOWN, buff=0.4)
        self.play(FadeIn(rule5, shift=UP * 0.15), run_time=0.8)
        self.wait(1.0)

        # examples
        ex_data = [
            ("Трилобит", "Палеозоик", BLUE),
            ("Амонит", "Мезозоик", ORANGE),
            ("Нумулит", "Кенозоик", PURPLE),
        ]
        ex_group = VGroup()
        for i, (name, era, c) in enumerate(ex_data):
            x = -4.4 + i * 4.4
            box = RoundedRectangle(
                width=3.8, height=1.5, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=c, stroke_width=2,
            ).move_to([x, -1.7, 0])
            name_t = Text(name, font_size=26, color=c, weight=BOLD).move_to(box.get_top() + DOWN * 0.4)
            era_t = Text(era, font_size=20, color=WHITE2).move_to(box.get_bottom() + UP * 0.4)
            ex_group.add(VGroup(box, name_t, era_t))

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in ex_group], lag_ratio=0.2), run_time=1.5)
        self.wait(2.4)

        self.play(FadeOut(VGroup(t5, intro5, rule5, ex_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  RELATIVE vs ABSOLUTE DATING                      ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dating")

        t6 = section_title("Како мериме старост?", color=BLUE)
        self.play(Write(t6), run_time=0.7)

        # left — relative
        rel_box = RoundedRectangle(
            width=5.8, height=3.6, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).move_to([-3.3, -0.3, 0])
        rel_ttl = Text("Релативна старост", font_size=26, color=GREEN, weight=BOLD)
        rel_ttl.move_to(rel_box.get_top() + DOWN * 0.4)
        rel_body = VGroup(
            Text("Кој е постар?", font_size=22, color=YELLOW),
            Text("Без точна година.", font_size=20, color=WHITE2),
            Text("Со слоеви и водечки", font_size=20, color=WHITE2),
            Text("фосили.", font_size=20, color=WHITE2),
            Text("\"Постар од...\" \"Помлад од...\"", font_size=18, color=ORANGE),
        ).arrange(DOWN, buff=0.18).move_to(rel_box).shift(DOWN * 0.2)

        # right — absolute
        abs_box = RoundedRectangle(
            width=5.8, height=3.6, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).move_to([3.3, -0.3, 0])
        abs_ttl = Text("Апсолутна старост", font_size=26, color=ORANGE, weight=BOLD)
        abs_ttl.move_to(abs_box.get_top() + DOWN * 0.4)
        abs_body = VGroup(
            Text("Колку точно години?", font_size=22, color=YELLOW),
            Text("Со радиоактивни", font_size=20, color=WHITE2),
            Text("изотопи. C-14, U-238.", font_size=20, color=WHITE2),
            MathTex(r"t = \frac{\ln(N_0/N)}{\lambda}", font_size=30, color=BLUE),
            Text("\"Стар е 65 милиони години.\"", font_size=18, color=ORANGE),
        ).arrange(DOWN, buff=0.18).move_to(abs_box).shift(DOWN * 0.15)

        self.play(FadeIn(VGroup(rel_box, rel_ttl)), FadeIn(VGroup(abs_box, abs_ttl)), run_time=1.0)
        self.play(Write(rel_body), Write(abs_body), run_time=2.0)
        self.wait(2.4)

        compare = Text("Една ни кажува редослед. Другата — година.",
                       font_size=26, color=YELLOW)
        compare.to_edge(DOWN, buff=0.4)
        self.play(Write(compare), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t6, rel_box, rel_ttl, rel_body, abs_box, abs_ttl, abs_body, compare)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  OUTRO — story written in stone                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        outro = VGroup(
            Text("4.6 милијарди години.",       font_size=46, color=YELLOW, weight=BOLD),
            Text("Четири ери.",                  font_size=42, color=ORANGE, weight=BOLD),
            Text("Илјади слоеви.",               font_size=42, color=BLUE,   weight=BOLD),
            Text("Милиони фосили.",              font_size=42, color=GREEN,  weight=BOLD),
            Text("Една приказна — за животот.",  font_size=38, color=WHITE2),
            Text("Запис.",                       font_size=58, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.32)

        for o in outro:
            self.play(FadeIn(o, shift=UP * 0.15), run_time=0.55)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(outro), run_time=0.8)
