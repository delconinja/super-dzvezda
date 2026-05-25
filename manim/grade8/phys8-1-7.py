from manim import *
import numpy as np

config.background_color = "#0d1b2e"
BLUE   = "#4fc3f7"
YELLOW = "#ffd54f"
GREEN  = "#81c784"
RED    = "#e57373"
GREY   = "#90a4ae"
ORANGE = "#ffb74d"
PURPLE = "#ce93d8"
WHITE2 = "#e8eaf0"
DARK_CARD = "#0f2233"


def callout(text, width=9.0, bg="#0d2b44", border=BLUE, font_size=28):
    box = RoundedRectangle(width=width, height=1.4, corner_radius=0.3,
        fill_color=bg, fill_opacity=1, stroke_color=border, stroke_width=2)
    label = Text(text, font_size=font_size, color=WHITE2)
    label.move_to(box)
    return VGroup(box, label)


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


class Phys817Scene(Scene):
    def construct(self):
        self.hook()
        self.friction_definition()
        self.types_of_friction()
        self.factors()
        self.useful_harmful()
        self.reducing_friction()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        line1 = Text("Без триење не можеш да одиш.", font_size=40, color=YELLOW)
        line2 = Text("Без триење не можеш да спреш.", font_size=40, color=RED)
        line3 = Text("Триењето е непријател кој те спасува.", font_size=34, color=BLUE)
        grp = VGroup(line1, line2, line3).arrange(DOWN, buff=0.55)
        self.play(Write(line1))
        self.wait(0.4)
        self.play(Write(line2))
        self.wait(0.4)
        self.play(FadeIn(line3, shift=UP * 0.3))
        self.wait(1.8)
        self.play(FadeOut(grp))

    # ── 2. DEFINITION ─────────────────────────────────────────────────────────
    def friction_definition(self):
        title = section_title("Триење — дефиниција")
        self.play(Write(title))

        defn = Text(
            "Триењето е сила која се спротивставува на движењето\n"
            "помеѓу две површини во контакт.",
            font_size=28, color=WHITE2, line_spacing=1.4)
        defn.shift(UP * 1.0)
        self.play(FadeIn(defn))
        self.wait(0.5)

        # Block + arrows visual
        surface = Rectangle(width=8, height=0.3, fill_color="#1a2a3a",
                             fill_opacity=1, stroke_color=GREY, stroke_width=1.5)
        surface.shift(DOWN * 1.2)
        block = Square(side_length=1.0, fill_color=BLUE, fill_opacity=1,
                       stroke_color=WHITE2, stroke_width=2)
        block.move_to(surface.get_top() + UP * 0.5)

        push_arrow = Arrow(start=block.get_left() + LEFT * 1.4, end=block.get_left(),
                           buff=0, color=GREEN, stroke_width=3)
        frict_arrow = Arrow(start=block.get_right(), end=block.get_right() + RIGHT * 1.4,
                            buff=0, color=RED, stroke_width=3)
        frict_arrow.rotate(PI)  # reverse: friction opposes motion
        frict_arrow = Arrow(start=block.get_right() + RIGHT * 1.4, end=block.get_right(),
                            buff=0, color=RED, stroke_width=3)

        push_lbl  = Text("Туркање F", font_size=21, color=GREEN).next_to(push_arrow, UP, buff=0.15)
        frict_lbl = Text("Триење f", font_size=21, color=RED).next_to(frict_arrow, UP, buff=0.15)

        self.play(FadeIn(surface), FadeIn(block))
        self.play(GrowArrow(push_arrow), Write(push_lbl))
        self.play(GrowArrow(frict_arrow), Write(frict_lbl))
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, defn, surface, block,
                                  push_arrow, frict_arrow, push_lbl, frict_lbl)))

    # ── 3. TYPES ──────────────────────────────────────────────────────────────
    def types_of_friction(self):
        title = section_title("Видови триење", color=BLUE)
        self.play(Write(title))

        types = [
            ("Статичко",    BLUE,   "телото мирува,\nотпор кон почнување"),
            ("Кинетичко",   GREEN,  "клизење на\nповршините"),
            ("Тркалачко",   YELLOW, "тркалањето на\nтркала/топки"),
            ("Воздушен отпор", PURPLE, "триење со воздух\nпри движење"),
        ]
        cards = VGroup()
        for name, col, desc in types:
            card = RoundedRectangle(width=2.8, height=3.0, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.5)
            t_name = Text(name, font_size=24, color=col, weight=BOLD)
            t_name.next_to(card.get_top(), DOWN, buff=0.3)
            t_desc = Text(desc, font_size=19, color=WHITE2, line_spacing=1.35)
            t_desc.move_to(card.get_center() + DOWN * 0.1)
            cards.add(VGroup(card, t_name, t_desc))

        cards.arrange(RIGHT, buff=0.45)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c, scale=0.88) for c in cards], lag_ratio=0.22))
        self.wait(0.5)

        order_note = callout(
            "Статичко  >  Кинетичко  >  Тркалачко  (по јачина)",
            width=10.0, border=GREY, font_size=24)
        order_note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(order_note))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, cards, order_note)))

    # ── 4. FACTORS ────────────────────────────────────────────────────────────
    def factors(self):
        title = section_title("Од што зависи триењето?", color=ORANGE)
        self.play(Write(title))

        yes_factors = [
            (GREEN, "Грубост на површините"),
            (GREEN, "Силата на притисок (нормална сила)"),
        ]
        no_factors = [
            (RED, "НЕ зависи од контактната плоштина!"),
            (RED, "НЕ зависи од брзината (кинетичко)"),
        ]

        yes_lbl = Text("ЗАВИСИ:", font_size=28, color=GREEN, weight=BOLD)
        yes_lbl.shift(LEFT * 3.0 + UP * 1.2)
        no_lbl  = Text("НЕ ЗАВИСИ:", font_size=28, color=RED, weight=BOLD)
        no_lbl.shift(RIGHT * 1.5 + UP * 1.2)

        yes_rows = VGroup()
        for col, txt in yes_factors:
            r = VGroup(Dot(radius=0.12, color=col),
                       Text(txt, font_size=24, color=WHITE2)).arrange(RIGHT, buff=0.3)
            yes_rows.add(r)
        yes_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        yes_rows.next_to(yes_lbl, DOWN, aligned_edge=LEFT, buff=0.3)

        no_rows = VGroup()
        for col, txt in no_factors:
            r = VGroup(Dot(radius=0.12, color=col),
                       Text(txt, font_size=24, color=WHITE2)).arrange(RIGHT, buff=0.3)
            no_rows.add(r)
        no_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        no_rows.next_to(no_lbl, DOWN, aligned_edge=LEFT, buff=0.3)

        divider = DashedLine(UP * 2, DOWN * 2, stroke_color=GREY, stroke_width=1.5)
        divider.shift(RIGHT * 0.0)

        self.play(Write(yes_lbl), Write(no_lbl), Create(divider))
        self.play(LaggedStart(*[FadeIn(r) for r in yes_rows], lag_ratio=0.2))
        self.play(LaggedStart(*[FadeIn(r) for r in no_rows], lag_ratio=0.2))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, yes_lbl, no_lbl, yes_rows, no_rows, divider)))

    # ── 5. USEFUL / HARMFUL ───────────────────────────────────────────────────
    def useful_harmful(self):
        title = section_title("Корисно и штетно триење", color=GREEN)
        self.play(Write(title))

        useful_items = [
            "Ходање (без триење — паѓаш)",
            "Сопирање на автомобил",
            "Добивање оган (дрво-дрво)",
            "Пишување (молив-хартија)",
        ]
        harmful_items = [
            "Трошење на механизми",
            "Загревање на мотори",
            "Хабење на гуми",
        ]

        u_lbl = Text("Корисно:", font_size=28, color=GREEN, weight=BOLD)
        u_lbl.shift(LEFT * 3.5 + UP * 1.4)
        h_lbl = Text("Штетно:", font_size=28, color=RED, weight=BOLD)
        h_lbl.shift(RIGHT * 1.5 + UP * 1.4)

        u_rows = VGroup(*[
            VGroup(Dot(radius=0.11, color=GREEN),
                   Text(t, font_size=22, color=WHITE2)).arrange(RIGHT, buff=0.25)
            for t in useful_items])
        u_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        u_rows.next_to(u_lbl, DOWN, aligned_edge=LEFT, buff=0.28)

        h_rows = VGroup(*[
            VGroup(Dot(radius=0.11, color=RED),
                   Text(t, font_size=22, color=WHITE2)).arrange(RIGHT, buff=0.25)
            for t in harmful_items])
        h_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        h_rows.next_to(h_lbl, DOWN, aligned_edge=LEFT, buff=0.28)

        div = DashedLine(UP * 2.2, DOWN * 2.2, stroke_color=GREY, stroke_width=1.5)

        self.play(Write(u_lbl), Write(h_lbl), Create(div))
        self.play(LaggedStart(*[FadeIn(r) for r in u_rows], lag_ratio=0.15))
        self.play(LaggedStart(*[FadeIn(r) for r in h_rows], lag_ratio=0.15))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, u_lbl, h_lbl, u_rows, h_rows, div)))

    # ── 6. REDUCING FRICTION ──────────────────────────────────────────────────
    def reducing_friction(self):
        title = section_title("Намалување на триењето", color=PURPLE)
        self.play(Write(title))

        methods = [
            ("Подмачкување", YELLOW, "масло, мерфи, грес"),
            ("Мазни површини", GREEN, "полирање, лесирање"),
            ("Тркала / лежишта", BLUE, "претворање клизање → тркалање"),
            ("Аеродинамика", ORANGE, "стримлинувана форма"),
        ]
        cards = VGroup()
        for name, col, note in methods:
            card = RoundedRectangle(width=5.8, height=1.1, corner_radius=0.22,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2)
            t_name = Text(name, font_size=24, color=col, weight=BOLD)
            t_note = Text(note, font_size=20, color=GREY)
            t_name.move_to(card.get_center() + LEFT * 1.8)
            t_note.move_to(card.get_center() + RIGHT * 0.8)
            cards.add(VGroup(card, t_name, t_note))

        cards.arrange(DOWN, buff=0.32)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards], lag_ratio=0.2))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, cards)))

    # ── 7. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (BLUE,   "Триење = сила спротивна на движење"),
            (GREEN,  "Видови: статичко, кинетичко, тркалачко, воздушен отпор"),
            (YELLOW, "Зависи: грубост + притисок. НЕ зависи: плоштина"),
            (ORANGE, "Корисно: ходање, сопирање, оган"),
            (RED,    "Штетно: хабење, загревање"),
            (PURPLE, "Намалување: подмачкување, тркала, аеродинамика"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=25, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        rows.shift(DOWN * 0.2)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.18))
        self.wait(1.0)

        fin = Text("Непријател кој те спасува. Секојдневно.", font_size=28, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))
