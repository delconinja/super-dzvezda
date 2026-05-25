"""
bio8-3-5  —  Неухранетост и ефекти
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
malnutrition as imbalance, hunger and abundance as two faces of
the same disease, one-word finishers.
Render:  manim -ql bio8-3-5.py Bio835Scene
Output:  media/videos/bio8-3-5/480p15/Bio835Scene.mp4
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


def disease_card(name, symptom, color):
    box = RoundedRectangle(
        width=3.2, height=2.0, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2.5,
    )
    title = Text(name, font_size=26, color=color, weight=BOLD)
    title.move_to(box.get_top() + DOWN * 0.45)
    body = Text(symptom, font_size=20, color=WHITE2)
    body.move_to(box.get_center() + DOWN * 0.15)
    return VGroup(box, title, body)


class Bio835Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Многу храна — болни.",
                     font_size=42, color=ORANGE, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.1)
        self.wait(0.3)

        hook2 = Text("Малку храна — болни.",
                     font_size=42, color=RED, weight=BOLD)
        hook2.next_to(hook1, DOWN, buff=0.45)
        self.play(Write(hook2), run_time=1.1)
        self.wait(0.4)

        beats = VGroup(
            Text("Не количество.",
                 font_size=36, color=YELLOW),
            Text("Туку рамнотежа.",
                 font_size=38, color=GREEN, weight=BOLD),
            Text("Хармонија прави здравје.",
                 font_size=40, color=BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook2, DOWN, buff=0.65)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.9)
            self.wait(0.25)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                       ~24 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е неухранетост?")
        self.play(Write(t2), run_time=0.8)

        defn = callout(
            "Состојба кога телото добива премалку, премногу\n"
            "или погрешен вид хранливи материи.",
            width=11.5, font_size=26, border=YELLOW,
        )
        defn.next_to(t2, DOWN, buff=0.6)
        self.play(FadeIn(defn, shift=UP * 0.2), run_time=0.9)
        self.wait(0.6)

        scale = VGroup(
            Line(LEFT * 3, RIGHT * 3, color=GREY, stroke_width=3),
            Triangle(color=YELLOW, fill_opacity=1).scale(0.25).shift(DOWN * 0.25),
        )
        scale.next_to(defn, DOWN, buff=0.8)

        left_label = Text("Премалку", font_size=24, color=RED).next_to(scale, LEFT, buff=0.4)
        right_label = Text("Премногу", font_size=24, color=ORANGE).next_to(scale, RIGHT, buff=0.4)

        self.play(Create(scale), FadeIn(left_label), FadeIn(right_label), run_time=1.0)
        self.wait(0.5)

        # tilt scale to left
        self.play(scale.animate.rotate(0.3), run_time=0.6)
        self.wait(0.3)
        # tilt to right
        self.play(scale.animate.rotate(-0.6), run_time=0.6)
        self.wait(0.3)
        # balance
        self.play(scale.animate.rotate(0.3), run_time=0.6)

        balance = Text("Рамнотежа = здравје.",
                       font_size=30, color=GREEN, weight=BOLD)
        balance.next_to(scale, DOWN, buff=0.6)
        self.play(Write(balance), run_time=0.9)
        self.wait(0.8)

        self.play(FadeOut(VGroup(t2, defn, scale, left_label,
                                 right_label, balance)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  ПОДХРАНЕТОСТ — KWASHIORKOR & MARASMUS           ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("undernutrition")

        t3 = section_title("Подхранетост", color=RED)
        self.play(Write(t3), run_time=0.8)

        intro3 = Text("Кога телото не добива доволно енергија или белковини.",
                      font_size=26, color=WHITE2)
        intro3.next_to(t3, DOWN, buff=0.4)
        self.play(FadeIn(intro3), run_time=0.7)
        self.wait(0.4)

        kwash = disease_card(
            "Квашиоркор",
            "Недостаток на\nбелковини.\nОтечен стомак.",
            ORANGE,
        )
        kwash.shift(LEFT * 3.3 + DOWN * 0.7)

        maras = disease_card(
            "Маразам",
            "Недостаток на\nкалории.\nИзнемоштеност.",
            RED,
        )
        maras.shift(RIGHT * 3.3 + DOWN * 0.7)

        self.play(FadeIn(kwash, shift=UP * 0.2), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(maras, shift=UP * 0.2), run_time=0.9)
        self.wait(0.6)

        finisher3 = Text("Глад. Тивок. Смртоносен.",
                         font_size=32, color=YELLOW, weight=BOLD)
        finisher3.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher3), run_time=1.0)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t3, intro3, kwash, maras, finisher3)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ПРЕХРАНЕТОСТ — ГОЈАЗНОСТ                         ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("overnutrition")

        t4 = section_title("Прехранетост", color=ORANGE)
        self.play(Write(t4), run_time=0.8)

        intro4 = Text("Кога телото добива повеќе енергија отколку што троши.",
                      font_size=26, color=WHITE2)
        intro4.next_to(t4, DOWN, buff=0.4)
        self.play(FadeIn(intro4), run_time=0.7)
        self.wait(0.4)

        # plate getting bigger
        plate = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3, stroke_width=3)
        plate.move_to(LEFT * 3 + DOWN * 0.5)
        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color=WHITE2, buff=0.2)
        arrow.move_to(DOWN * 0.5)
        plate2 = Circle(radius=1.6, color=ORANGE, fill_opacity=0.5, stroke_width=3)
        plate2.move_to(RIGHT * 3 + DOWN * 0.5)

        label1 = Text("здраво", font_size=22, color=GREEN).next_to(plate, DOWN, buff=0.2)
        label2 = Text("гојазност", font_size=22, color=RED).next_to(plate2, DOWN, buff=0.2)

        self.play(Create(plate), FadeIn(label1), run_time=0.7)
        self.play(Create(arrow), run_time=0.5)
        self.play(Create(plate2), FadeIn(label2), run_time=0.7)
        self.wait(0.4)

        consequences = VGroup(
            Text("• Дијабетес тип 2", font_size=24, color=WHITE2),
            Text("• Срцеви заболувања", font_size=24, color=WHITE2),
            Text("• Висок крвен притисок", font_size=24, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        consequences.to_edge(DOWN, buff=0.5).shift(LEFT * 0.5)

        for c in consequences:
            self.play(FadeIn(c, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(t4, intro4, plate, arrow, plate2,
                                 label1, label2, consequences)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  МИКРОНУТРИЕНТИ — ДЕФИЦИТИ                        ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("micronutrients")

        t5 = section_title("Дефицити на микронутриенти", color=PURPLE)
        self.play(Write(t5), run_time=0.8)

        intro5 = Text("Малку количество — голема последица.",
                      font_size=28, color=WHITE2)
        intro5.next_to(t5, DOWN, buff=0.4)
        self.play(FadeIn(intro5), run_time=0.7)
        self.wait(0.4)

        rows = [
            ("Витамин А", "→", "слепило", YELLOW, RED),
            ("Железо", "→", "анемија", ORANGE, RED),
            ("Јод", "→", "гушавост", BLUE, RED),
        ]

        deficit_group = VGroup()
        for nutrient, arrow_str, effect, ncol, ecol in rows:
            n = Text(nutrient, font_size=28, color=ncol, weight=BOLD)
            a = Text(arrow_str, font_size=28, color=WHITE2)
            e = Text(effect, font_size=28, color=ecol, weight=BOLD)
            row = VGroup(n, a, e).arrange(RIGHT, buff=0.5)
            deficit_group.add(row)

        deficit_group.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        deficit_group.next_to(intro5, DOWN, buff=0.6)

        for row in deficit_group:
            self.play(FadeIn(row[0], shift=RIGHT * 0.2), run_time=0.4)
            self.play(FadeIn(row[1]), run_time=0.2)
            self.play(FadeIn(row[2], shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.3)

        self.wait(0.5)

        warning = callout(
            "Невидлив глад. Скриен. Опасен.",
            width=8.5, font_size=28, border=PURPLE, bg="#2a1a3a",
        )
        warning.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(warning, shift=UP * 0.2), run_time=0.9)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t5, intro5, deficit_group, warning)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ГЛОБАЛНА СЛИКА                                   ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("global")

        t6 = section_title("Светска слика", color=BLUE)
        self.play(Write(t6), run_time=0.8)

        intro6 = Text("Двата света — една иста криза.",
                      font_size=28, color=WHITE2)
        intro6.next_to(t6, DOWN, buff=0.4)
        self.play(FadeIn(intro6), run_time=0.7)
        self.wait(0.4)

        # two stat boxes
        left_box = RoundedRectangle(
            width=5.5, height=2.6, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=RED, stroke_width=2.5,
        ).shift(LEFT * 3.2 + DOWN * 0.5)
        left_num = Text("≈ 800 милиони", font_size=30, color=RED, weight=BOLD)
        left_num.move_to(left_box.get_top() + DOWN * 0.55)
        left_txt = Text("луѓе — гладни.", font_size=24, color=WHITE2)
        left_txt.next_to(left_num, DOWN, buff=0.2)

        right_box = RoundedRectangle(
            width=5.5, height=2.6, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2.5,
        ).shift(RIGHT * 3.2 + DOWN * 0.5)
        right_num = Text("≈ 2 милијарди", font_size=30, color=ORANGE, weight=BOLD)
        right_num.move_to(right_box.get_top() + DOWN * 0.55)
        right_txt = Text("луѓе — со прекумерна тежина.", font_size=22, color=WHITE2)
        right_txt.next_to(right_num, DOWN, buff=0.2)

        self.play(Create(left_box), FadeIn(left_num), FadeIn(left_txt),
                  run_time=0.9)
        self.wait(0.4)
        self.play(Create(right_box), FadeIn(right_num), FadeIn(right_txt),
                  run_time=0.9)
        self.wait(0.7)

        contrast = Text("Иста планета. Различен болест.",
                        font_size=28, color=YELLOW, weight=BOLD)
        contrast.to_edge(DOWN, buff=0.5)
        self.play(Write(contrast), run_time=1.0)
        self.wait(0.9)

        self.play(FadeOut(VGroup(t6, intro6, left_box, left_num, left_txt,
                                 right_box, right_num, right_txt, contrast)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conclusion")

        t7 = section_title("Заклучок", color=GREEN)
        self.play(Write(t7), run_time=0.8)

        final = VGroup(
            Text("Премалку — болест.",
                 font_size=34, color=RED, weight=BOLD),
            Text("Премногу — болест.",
                 font_size=34, color=ORANGE, weight=BOLD),
            Text("Балансот — лек.",
                 font_size=36, color=GREEN, weight=BOLD),
            Text("Хармонија.",
                 font_size=44, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(t7, DOWN, buff=0.7)

        for line in final:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.9)
            self.wait(0.3)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t7, final)), run_time=0.8)
        self.wait(0.4)
