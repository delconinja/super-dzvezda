"""
bio8-5-5  —  Адаптации — преживување во средината
Биологија 8, Единица 5: Варијабилност

Teaching narrative — Andonovski-style: nothing by chance,
adaptation as the silent answer of the body to the world.
Render:  manim -ql bio8-5-5.py Bio855Scene
Output:  media/videos/bio8-5-5/480p15/Bio855Scene.mp4
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


class Bio855Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Камилата живее во пустина.",   font_size=40, color=YELLOW, weight=BOLD)
        hook2 = Text("Поларниот мечок во ладно.",     font_size=40, color=BLUE,   weight=BOLD)
        hook3 = Text("Жирафата на високо лиснато.",   font_size=40, color=ORANGE, weight=BOLD)
        hook4 = Text("Не случајно.",                   font_size=46, color=GREEN, weight=BOLD)
        hook5 = Text("Адаптација.",                    font_size=54, color=PURPLE, weight=BOLD)

        beats = VGroup(hook1, hook2, hook3, hook4, hook5).arrange(DOWN, buff=0.45)
        beats.move_to(ORIGIN)

        for b in beats:
            self.play(Write(b), run_time=0.9)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(beats), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                        ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е адаптација?")
        self.play(Write(t2), run_time=0.9)

        defn1 = callout("Адаптација = особина што помага преживување",
                        width=11.0, border=YELLOW, font_size=28)
        defn1.next_to(t2, DOWN, buff=0.5)
        defn2 = callout("во конкретна средина.",
                        width=11.0, border=YELLOW, font_size=28)
        defn2.next_to(defn1, DOWN, buff=0.2)

        self.play(FadeIn(defn1, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(defn2, shift=UP * 0.2), run_time=0.8)

        self.wait(0.4)

        # arrow connecting trait to survival
        trait = RoundedRectangle(
            width=3.2, height=1.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).shift(LEFT * 3.5 + DOWN * 1.3)
        trait_lab = Text("Особина", font_size=28, color=BLUE, weight=BOLD)
        trait_lab.move_to(trait)

        surv = RoundedRectangle(
            width=3.2, height=1.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).shift(RIGHT * 3.5 + DOWN * 1.3)
        surv_lab = Text("Преживување", font_size=28, color=GREEN, weight=BOLD)
        surv_lab.move_to(surv)

        arr = Arrow(trait.get_right(), surv.get_left(), color=YELLOW, buff=0.1, stroke_width=6)

        self.play(FadeIn(trait), Write(trait_lab),
                  FadeIn(surv), Write(surv_lab), run_time=0.9)
        self.play(GrowArrow(arr), run_time=0.7)

        self.wait(1.5)
        self.play(FadeOut(VGroup(t2, defn1, defn2, trait, trait_lab,
                                  surv, surv_lab, arr)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ПОЛАРЕН МЕЧОК                                    ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("polar_bear")

        t3 = section_title("Поларен мечок", color=BLUE)
        self.play(Write(t3), run_time=0.9)

        sub3 = Text("Живее на -40°C. Како преживува?",
                    font_size=28, color=WHITE2)
        sub3.next_to(t3, DOWN, buff=0.3)
        self.play(Write(sub3), run_time=1.0)

        # bear silhouette
        bear_body = Ellipse(width=2.4, height=1.6,
                            fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        bear_head = Circle(radius=0.6, fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        bear_head.move_to(bear_body.get_right() + RIGHT * 0.3 + UP * 0.3)
        ear1 = Circle(radius=0.15, fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        ear1.move_to(bear_head.get_top() + UP * 0.05 + LEFT * 0.2)
        ear2 = Circle(radius=0.15, fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        ear2.move_to(bear_head.get_top() + UP * 0.05 + RIGHT * 0.2)
        eye = Dot(point=bear_head.get_center() + RIGHT * 0.15 + UP * 0.05,
                  radius=0.05, color=BLACK)
        leg1 = RoundedRectangle(width=0.35, height=0.7, corner_radius=0.15,
                                fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        leg1.move_to(bear_body.get_bottom() + LEFT * 0.7 + DOWN * 0.2)
        leg2 = RoundedRectangle(width=0.35, height=0.7, corner_radius=0.15,
                                fill_color=WHITE2, fill_opacity=1, stroke_width=0)
        leg2.move_to(bear_body.get_bottom() + RIGHT * 0.7 + DOWN * 0.2)
        bear = VGroup(bear_body, bear_head, ear1, ear2, eye, leg1, leg2)
        bear.shift(LEFT * 3 + DOWN * 0.3)

        self.play(FadeIn(bear, shift=UP * 0.2), run_time=0.9)

        # adaptations list
        adapts = VGroup(
            Text("Дебело крзно", font_size=28, color=BLUE, weight=BOLD),
            Text("Слој маснотија", font_size=28, color=YELLOW, weight=BOLD),
            Text("Мали уши (помалку губење топлина)",
                 font_size=24, color=ORANGE),
            Text("Бела боја — маскирање", font_size=24, color=GREEN),
            Text("Широки шепи — газење по снег",
                 font_size=24, color=PURPLE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        adapts.shift(RIGHT * 2.5 + DOWN * 0.3)

        # arrows from bear to adaptations
        for a in adapts:
            self.play(Write(a), run_time=0.6)

        self.wait(0.5)

        punch3 = Text("Секоја особина — одговор на студот.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch3.to_edge(DOWN, buff=0.3)
        self.play(Write(punch3), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t3, sub3, bear, adapts, punch3)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  КАМИЛА                                            ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("camel")

        t4 = section_title("Камила", color=ORANGE)
        self.play(Write(t4), run_time=0.9)

        sub4 = Text("Живее на +45°C. Со малку вода.",
                    font_size=28, color=WHITE2)
        sub4.next_to(t4, DOWN, buff=0.3)
        self.play(Write(sub4), run_time=1.0)

        # simple camel
        camel_body = Ellipse(width=2.5, height=1.0,
                             fill_color="#c8a060", fill_opacity=1, stroke_width=0)
        hump = Arc(radius=0.7, angle=PI, start_angle=0,
                   fill_color="#c8a060", fill_opacity=1, stroke_width=0)
        hump.move_to(camel_body.get_top() + UP * 0.35)
        neck = Polygon(
            camel_body.get_right() + LEFT * 0.1,
            camel_body.get_right() + UP * 0.4,
            camel_body.get_right() + RIGHT * 0.5 + UP * 1.0,
            camel_body.get_right() + RIGHT * 0.8 + UP * 0.9,
            fill_color="#c8a060", fill_opacity=1, stroke_width=0,
        )
        head = Ellipse(width=0.6, height=0.4,
                       fill_color="#c8a060", fill_opacity=1, stroke_width=0)
        head.move_to(camel_body.get_right() + RIGHT * 0.9 + UP * 1.0)
        eye = Dot(head.get_center() + LEFT * 0.05, radius=0.05, color=BLACK)
        leg1 = Rectangle(width=0.2, height=0.9,
                         fill_color="#a08050", fill_opacity=1, stroke_width=0)
        leg1.move_to(camel_body.get_bottom() + LEFT * 0.7 + DOWN * 0.3)
        leg2 = Rectangle(width=0.2, height=0.9,
                         fill_color="#a08050", fill_opacity=1, stroke_width=0)
        leg2.move_to(camel_body.get_bottom() + RIGHT * 0.4 + DOWN * 0.3)

        camel = VGroup(camel_body, hump, neck, head, eye, leg1, leg2)
        camel.shift(LEFT * 3 + DOWN * 0.3)

        self.play(FadeIn(camel, shift=UP * 0.2), run_time=0.9)

        adapts4 = VGroup(
            Text("Грба — резерва маснотија",   font_size=26, color=ORANGE, weight=BOLD),
            Text("Долги нозе — далеку од песок",
                 font_size=24, color=YELLOW),
            Text("Широки стапала — не пропаѓа",
                 font_size=24, color=GREEN),
            Text("Издолжени трепки — против песок",
                 font_size=24, color=BLUE),
            Text("Концентрирана урина — штеди вода",
                 font_size=24, color=PURPLE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        adapts4.shift(RIGHT * 2.0 + DOWN * 0.3)

        for a in adapts4:
            self.play(Write(a), run_time=0.55)

        self.wait(0.4)

        punch4 = Text("Секоја особина — одговор на жегата.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch4.to_edge(DOWN, buff=0.3)
        self.play(Write(punch4), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t4, sub4, camel, adapts4, punch4)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ЖИРАФА                                            ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("giraffe")

        t5 = section_title("Жирафа", color=YELLOW)
        self.play(Write(t5), run_time=0.9)

        # giraffe stretched neck reaching tree
        body = Ellipse(width=1.6, height=1.0,
                       fill_color="#e8b04a", fill_opacity=1, stroke_width=0)
        body.shift(LEFT * 3 + DOWN * 1.5)
        neck = Rectangle(width=0.35, height=2.6,
                         fill_color="#e8b04a", fill_opacity=1, stroke_width=0)
        neck.next_to(body, UP, buff=-0.1).shift(RIGHT * 0.3)
        head = Ellipse(width=0.5, height=0.8,
                       fill_color="#e8b04a", fill_opacity=1, stroke_width=0)
        head.next_to(neck, UP, buff=-0.1)
        leg_l1 = Rectangle(width=0.18, height=1.4, fill_color="#c8904a",
                           fill_opacity=1, stroke_width=0).next_to(body, DOWN, buff=-0.1).shift(LEFT * 0.4)
        leg_l2 = Rectangle(width=0.18, height=1.4, fill_color="#c8904a",
                           fill_opacity=1, stroke_width=0).next_to(body, DOWN, buff=-0.1).shift(RIGHT * 0.4)
        # spots
        spots = VGroup(*[
            Dot(point=body.get_center() + np.array([0.4 * (i % 3 - 1),
                                                     0.3 * (i // 3 - 0.5), 0]),
                radius=0.12, color="#7a4a1a")
            for i in range(6)
        ])

        giraffe = VGroup(body, neck, head, leg_l1, leg_l2, spots)

        # tree
        trunk = Rectangle(width=0.4, height=2.8,
                          fill_color="#5a3a1f", fill_opacity=1, stroke_width=0)
        trunk.shift(RIGHT * 3 + DOWN * 0.6)
        crown = Circle(radius=1.2, fill_color=GREEN,
                       fill_opacity=0.85, stroke_width=0)
        crown.next_to(trunk, UP, buff=-0.1)
        tree = VGroup(trunk, crown)

        self.play(FadeIn(giraffe, shift=UP * 0.2), FadeIn(tree, shift=UP * 0.2),
                  run_time=1.0)

        adapt_label = callout("Долг врат → достапна храна од високи дрвја",
                              width=10.5, border=YELLOW, font_size=26)
        adapt_label.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(adapt_label, shift=UP * 0.2), run_time=0.9)
        self.wait(1.5)

        punch5 = Text("Структурна адаптација — на тело.",
                      font_size=28, color=GREEN, weight=BOLD)
        punch5.to_edge(DOWN, buff=0.2)
        self.play(FadeOut(adapt_label), Write(punch5), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5, giraffe, tree, punch5)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  ТРИ ТИПА АДАПТАЦИИ                                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_types")

        t6 = section_title("Три типа адаптации")
        self.play(Write(t6), run_time=0.9)

        panels = []
        types_data = [
            ("Структурни",   BLUE,   "облик на тело",  "грба, врат, крзно"),
            ("Однесувачки",  ORANGE, "однесување",     "миграции, спиење, ловење"),
            ("Физиолошки",   GREEN,  "функција внатре", "ладна крв, потење, штедење вода"),
        ]

        groups = VGroup()
        for name, col, sub, ex in types_data:
            panel = RoundedRectangle(
                width=4.0, height=3.5, corner_radius=0.3,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            lab = Text(name, font_size=30, color=col, weight=BOLD)
            lab.move_to(panel.get_top() + DOWN * 0.45)
            desc = Text(sub, font_size=24, color=WHITE2)
            desc.move_to(panel.get_center() + UP * 0.4)
            example = Text(ex, font_size=20, color=GREY)
            example.move_to(panel.get_bottom() + UP * 0.8)
            groups.add(VGroup(panel, lab, desc, example))

        groups.arrange(RIGHT, buff=0.3).next_to(t6, DOWN, buff=0.6)

        for g in groups:
            self.play(FadeIn(g, shift=UP * 0.2), run_time=0.7)

        self.wait(0.5)

        punch6 = Text("Тело. Однесување. Хемија. Сите три — преживување.",
                      font_size=28, color=YELLOW, weight=BOLD)
        punch6.to_edge(DOWN, buff=0.4)
        self.play(Write(punch6), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(VGroup(t6, groups, punch6)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                         ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        final1 = Text("Средината прашува.",         font_size=44, color=YELLOW, weight=BOLD)
        final2 = Text("Организмот одговара.",        font_size=42, color=BLUE,   weight=BOLD)
        final3 = Text("Со тело. Со однесување.",     font_size=36, color=ORANGE, weight=BOLD)
        final4 = Text("Со хемија.",                  font_size=40, color=GREEN,  weight=BOLD)
        final5 = Text("Адаптација.",                 font_size=50, color=PURPLE, weight=BOLD)

        finals = VGroup(final1, final2, final3, final4, final5).arrange(DOWN, buff=0.4)
        finals.move_to(ORIGIN)

        for f in finals:
            self.play(Write(f), run_time=0.8)
            self.wait(0.25)

        self.wait(2.0)
        self.play(FadeOut(finals), run_time=1.0)
        self.wait(0.5)
