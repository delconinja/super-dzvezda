"""
bio8-7-1  —  Што се фосили?
Биологија 8, Единица 7: Запис во карпите

Teaching narrative — Andonovski-style: three-beat punches,
fossils as time travelers, deep time as epic.
Render:  manim -ql bio8-7-1.py Bio871Scene
Output:  media/videos/bio8-7-1/480p15/Bio871Scene.mp4
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


def sediment_layer(width=10, height=0.55, color=ORANGE, y=0):
    """A single horizontal rock/sediment band."""
    band = Rectangle(
        width=width, height=height,
        fill_color=color, fill_opacity=0.85,
        stroke_color=BLACK, stroke_width=1,
    )
    band.move_to([0, y, 0])
    return band


def dino_silhouette(color=GREY, scale=1.0):
    """Tiny dinosaur silhouette — round body, neck, tail, legs."""
    body = Ellipse(width=1.2, height=0.55, color=color, fill_color=color, fill_opacity=1, stroke_width=0)
    neck = Line(body.get_left() + UP * 0.05, body.get_left() + LEFT * 0.45 + UP * 0.5,
                color=color, stroke_width=8)
    head = Circle(radius=0.13, color=color, fill_color=color, fill_opacity=1, stroke_width=0)
    head.move_to(neck.get_end())
    tail = Line(body.get_right() + UP * 0.02, body.get_right() + RIGHT * 0.7 + UP * 0.25,
                color=color, stroke_width=6)
    leg1 = Line(body.get_bottom() + LEFT * 0.25, body.get_bottom() + LEFT * 0.25 + DOWN * 0.35,
                color=color, stroke_width=5)
    leg2 = Line(body.get_bottom() + RIGHT * 0.25, body.get_bottom() + RIGHT * 0.25 + DOWN * 0.35,
                color=color, stroke_width=5)
    g = VGroup(body, neck, head, tail, leg1, leg2)
    g.scale(scale)
    return g


class Bio871Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — A dinosaur died.                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Динозаур умрел.",
                     font_size=54, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.4)

        beats = VGroup(
            Text("Пред 70 милиони години.",      font_size=44, color=BLUE),
            Text("Покрит со кал.",               font_size=42, color=ORANGE),
            Text("Со време — камен.",            font_size=42, color=GREY),
            Text("Денеска го гледаш.",           font_size=44, color=GREEN, weight=BOLD),
            Text("Тоа е фосил.",                 font_size=50, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(hook1, DOWN, buff=0.5)

        for b in beats:
            self.play(FadeIn(b, shift=UP * 0.15), run_time=0.55)
            self.wait(0.25)
        self.wait(1.0)
        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — what a fossil is                    ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е фосил?")
        self.play(Write(t2), run_time=0.8)

        def_card = RoundedRectangle(
            width=11, height=2.6, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2,
        ).next_to(t2, DOWN, buff=0.6)

        def_text = VGroup(
            Text("Фосил = зачуван остаток", font_size=34, color=WHITE2),
            Text("или трага од некогашно живо суштество.", font_size=30, color=WHITE2),
            Text("Од далечни времиња. Од друг свет.", font_size=28, color=ORANGE),
        ).arrange(DOWN, buff=0.18).move_to(def_card)

        self.play(FadeIn(def_card), Write(def_text), run_time=1.6)
        self.wait(1.6)

        # три collонки: коски, отпечатоци, ќилибар
        cols_y = -1.6
        col_titles = [
            ("Коски", BLUE),
            ("Отпечатоци", GREEN),
            ("Ќилибар", ORANGE),
        ]
        col_group = VGroup()
        for i, (txt, c) in enumerate(col_titles):
            x = -4.2 + i * 4.2
            box = RoundedRectangle(
                width=3.6, height=1.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=c, stroke_width=2,
            ).move_to([x, cols_y, 0])
            lbl = Text(txt, font_size=30, color=c, weight=BOLD).move_to(box)
            col_group.add(VGroup(box, lbl))

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in col_group], lag_ratio=0.2), run_time=1.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, def_card, def_text, col_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  HOW A FOSSIL FORMS — burial sequence             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("formation")

        t3 = section_title("Како настанува фосил?", color=ORANGE)
        self.play(Write(t3), run_time=0.7)

        # хоризонт
        ground = Line(LEFT * 6 + DOWN * 2.5, RIGHT * 6 + DOWN * 2.5, color=GREY, stroke_width=3)
        self.play(Create(ground), run_time=0.5)

        # 1. живиот динозаур
        dino = dino_silhouette(color=GREEN, scale=1.0)
        dino.move_to([-3, -1.7, 0])

        step1_lbl = Text("1. Животно умира", font_size=28, color=GREEN).to_edge(LEFT, buff=0.6).shift(UP * 1.5)
        self.play(FadeIn(dino), Write(step1_lbl), run_time=1.0)
        self.wait(0.8)

        # пад
        self.play(dino.animate.rotate(PI/2).move_to([-3, -2.2, 0]).set_color(GREY), run_time=1.0)
        self.wait(0.4)

        # 2. брзо заземјување — sediment falls
        step2_lbl = Text("2. Брзо заземјување", font_size=28, color=ORANGE).next_to(step1_lbl, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(step2_lbl), run_time=0.5)

        sed1 = sediment_layer(width=12, height=0.4, color="#8d6e63", y=-2.7)
        self.play(FadeIn(sed1, shift=DOWN * 0.3), run_time=0.7)
        sed2 = sediment_layer(width=12, height=0.4, color="#a1887f", y=-2.3)
        self.play(FadeIn(sed2, shift=DOWN * 0.3), run_time=0.7)
        sed3 = sediment_layer(width=12, height=0.4, color="#bcaaa4", y=-1.9)
        self.play(FadeIn(sed3, shift=DOWN * 0.3), dino.animate.set_opacity(0.5), run_time=0.7)

        self.wait(0.6)

        # 3. многу време
        step3_lbl = Text("3. Милиони години", font_size=28, color=YELLOW).next_to(step2_lbl, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(step3_lbl), run_time=0.5)

        # додатни слоеви
        extra_layers = VGroup(
            sediment_layer(width=12, height=0.35, color="#5d4037", y=-1.55),
            sediment_layer(width=12, height=0.35, color="#6d4c41", y=-1.2),
            sediment_layer(width=12, height=0.35, color="#795548", y=-0.85),
        )
        self.play(LaggedStart(*[FadeIn(l, shift=DOWN * 0.2) for l in extra_layers], lag_ratio=0.3), run_time=1.5)

        time_clock = Text("70 000 000 години", font_size=32, color=YELLOW, weight=BOLD)
        time_clock.to_edge(RIGHT, buff=0.6).shift(UP * 0.5)
        self.play(Write(time_clock), run_time=0.8)
        self.wait(1.0)

        # 4. камен!
        step4_lbl = Text("4. Коска → камен", font_size=28, color=BLUE, weight=BOLD).next_to(step3_lbl, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(step4_lbl), run_time=0.5)

        # dino mineralized
        self.play(dino.animate.set_color(BLUE).set_opacity(1.0), run_time=1.0)
        self.wait(0.8)

        # 5. изложен
        step5_lbl = Text("5. Ерозија — пронајден", font_size=28, color=RED).next_to(step4_lbl, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(step5_lbl), run_time=0.5)

        self.play(
            FadeOut(extra_layers),
            FadeOut(sed3),
            sed2.animate.set_opacity(0.4),
            run_time=1.0,
        )
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            t3, ground, dino, sed1, sed2, time_clock,
            step1_lbl, step2_lbl, step3_lbl, step4_lbl, step5_lbl,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  CONDITIONS — what's required                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conditions")

        t4 = section_title("Услови за фосилизација", color=BLUE)
        self.play(Write(t4), run_time=0.7)

        cond_intro = Text("Не секое суштество станува фосил.",
                          font_size=32, color=WHITE2)
        cond_intro.next_to(t4, DOWN, buff=0.4)
        self.play(FadeIn(cond_intro), run_time=0.7)
        self.wait(0.6)

        conds = [
            ("Брзо покривање",  "Пред да го изедат лешинари.", BLUE),
            ("Малку кислород",  "Без кислород — нема распаѓање.", GREEN),
            ("Седимент",        "Кал, песок, тиња — го запечатува.", ORANGE),
            ("Тврди делови",    "Коски, заби, школки. Мекото исчезнува.", PURPLE),
        ]
        cond_group = VGroup()
        for i, (title, sub, c) in enumerate(conds):
            row = i // 2
            col = i % 2
            x = -3.2 + col * 6.4
            y = -0.3 - row * 1.8
            box = RoundedRectangle(
                width=5.8, height=1.5, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=c, stroke_width=2,
            ).move_to([x, y, 0])
            ttl = Text(title, font_size=26, color=c, weight=BOLD).move_to(box.get_top() + DOWN * 0.4)
            sbt = Text(sub, font_size=20, color=WHITE2).move_to(box.get_bottom() + UP * 0.4)
            cond_group.add(VGroup(box, ttl, sbt))

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cond_group], lag_ratio=0.2), run_time=1.8)
        self.wait(2.2)

        self.play(FadeOut(VGroup(t4, cond_intro, cond_group)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  TYPES OF FOSSILS — gallery                       ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("types")

        t5 = section_title("Видови фосили", color=GREEN)
        self.play(Write(t5), run_time=0.7)

        # ред 1: вкаменети коски, отпечаток, калап
        # ред 2: ќилибар, замрзнат мамут, трага (стапалка)

        types_data = [
            ("Вкаменети коски", "Минерали го заменуваат коскениот ткиво.", BLUE),
            ("Отпечаток на лист", "Лист притиска во кал. Останува облик.", GREEN),
            ("Калап и одлеан", "Школка се распаѓа. Калап останува.", ORANGE),
            ("Ќилибар", "Инсект во смола. Зачуван 50 милиони години.", YELLOW),
            ("Замрзнат мамут", "Сибир. Леден. Со коса, со месо.", PURPLE),
            ("Стапалка", "Динозаур поминал. Калта се вкаменила.", RED),
        ]
        cells = VGroup()
        for i, (ttl, sub, c) in enumerate(types_data):
            row = i // 3
            col = i % 3
            x = -4.4 + col * 4.4
            y = 1.2 - row * 2.4
            box = RoundedRectangle(
                width=4.0, height=2.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=c, stroke_width=2,
            ).move_to([x, y, 0])
            t_ttl = Text(ttl, font_size=24, color=c, weight=BOLD).move_to(box.get_top() + DOWN * 0.35)
            t_sub = Text(sub, font_size=17, color=WHITE2).move_to(box).shift(DOWN * 0.15)
            cells.add(VGroup(box, t_ttl, t_sub))

        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cells], lag_ratio=0.15), run_time=2.4)
        self.wait(2.8)

        # one-word finisher
        finisher = Text("Шест начини. Една цел: да остане.",
                        font_size=30, color=YELLOW, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.4)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, cells, finisher)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  WHY IT MATTERS                                   ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        t6 = section_title("Зошто се важни?", color=PURPLE)
        self.play(Write(t6), run_time=0.7)

        whys = VGroup(
            callout("Не книги — туку камења. Тие ни кажуваат.", width=11, border=PURPLE, font_size=28),
            callout("Кој живеел. Каде. И кога.", width=11, border=BLUE, font_size=28),
            callout("Како се менувал животот на Земјата.", width=11, border=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.4).next_to(t6, DOWN, buff=0.6)

        for w in whys:
            self.play(FadeIn(w, shift=UP * 0.15), run_time=0.6)
            self.wait(0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t6, whys)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  OUTRO                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        outro1 = Text("Фосил не е само камен.",
                      font_size=44, color=WHITE2)
        outro2 = Text("Тоа е писмо.",
                      font_size=44, color=YELLOW, weight=BOLD)
        outro3 = Text("Од времиња пред нас.",
                      font_size=38, color=BLUE)
        outro4 = Text("Запис.",
                      font_size=56, color=ORANGE, weight=BOLD)

        outro_group = VGroup(outro1, outro2, outro3, outro4).arrange(DOWN, buff=0.45)
        for o in outro_group:
            self.play(Write(o), run_time=0.7)
            self.wait(0.3)
        self.wait(2.0)
        self.play(FadeOut(outro_group), run_time=0.8)
