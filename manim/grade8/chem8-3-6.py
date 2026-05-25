"""
chem8-3-6  —  Разделување смеси — практични примери
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — Andonovski-style: chemistry as patient, not violent,
separation methods as choices, one-word finishers.
Render:  manim -ql chem8-3-6.py Chem836Scene
Output:  media/videos/chem8-3-6/480p15/Chem836Scene.mp4
"""
from manim import *
import numpy as np
import random

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
    t = Text(text, font_size=40, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


class Chem836Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Сол во вода.", font_size=42, color=BLUE, weight=BOLD).move_to(UP*1.6)
        h2 = Text("Како да ja вратиш солта?",
                  font_size=36, color=WHITE2).next_to(h1, DOWN, buff=0.4)
        self.play(Write(h1), run_time=0.9)
        self.play(Write(h2), run_time=1.0)
        self.wait(0.5)

        beats = VGroup(
            Text("Не повлекуваш.", font_size=34, color=RED),
            Text("Не цедиш.", font_size=34, color=RED),
            Text("Испаруваш.", font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.25).move_to(DOWN*0.7)

        for b in beats:
            self.play(Write(b), run_time=0.6)
            self.wait(0.15)
        self.wait(0.4)

        f1 = Text("Хемијата не насилува.", font_size=28, color=YELLOW).move_to(DOWN*2.6)
        f2 = Text("Хемијата трпи.", font_size=32, color=ORANGE, weight=BOLD).next_to(f1, DOWN, buff=0.25)
        self.play(Write(f1), run_time=0.9)
        self.play(Write(f2), run_time=0.9)
        self.wait(1.3)

        self.play(FadeOut(VGroup(h1, h2, beats, f1, f2)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ЗОШТО РАЗДЕЛУВАМЕ                              ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        t2 = section_title("Зошто разделуваме смеси?")
        self.play(Write(t2), run_time=0.8)

        reasons = VGroup(
            Text("Да добиеме чисти материи.", font_size=28, color=WHITE2),
            Text("Да отстраниме нечистотии.", font_size=28, color=WHITE2),
            Text("Да искористиме секој дел.", font_size=28, color=WHITE2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(ORIGIN)

        for r in reasons:
            self.play(Write(r), run_time=0.7)
        self.wait(0.4)

        end_line = Text("Од суровина → различни производи.",
                        font_size=28, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(end_line), run_time=1.1)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, reasons, end_line)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  МЕТОД 1 — ФИЛТРИРАЊЕ                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("filtration")

        t3 = section_title("Филтрирање — цврсто + течно")
        self.play(Write(t3), run_time=0.8)

        # Funnel + paper + flask
        funnel = Polygon(
            [-1.2, 1.0, 0], [1.2, 1.0, 0], [0.3, -0.2, 0], [-0.3, -0.2, 0],
            stroke_color=WHITE2, stroke_width=3, fill_color=DARK_CARD, fill_opacity=0.4,
        ).shift(UP*0.8)
        # Sand particles caught
        sand = VGroup()
        for i in range(10):
            x = random.uniform(-0.9, 0.9); y = random.uniform(0.6, 1.0)
            sand.add(Circle(radius=0.08, fill_color=ORANGE, fill_opacity=1,
                             stroke_width=0).move_to(funnel.get_center()+np.array([x,y,0])+DOWN*0.3))

        # Flask below
        flask = Polygon(
            [-1.5, -2.5, 0], [1.5, -2.5, 0], [0.5, -1.5, 0], [-0.5, -1.5, 0],
            stroke_color=WHITE2, stroke_width=3, fill_color=BLUE, fill_opacity=0.3,
        )
        # Drops
        drops = VGroup(*[
            Circle(radius=0.08, fill_color=BLUE, fill_opacity=0.8,
                    stroke_width=0).move_to([0, -0.7-i*0.4, 0])
            for i in range(3)
        ])

        self.play(Create(funnel), run_time=0.7)
        self.play(FadeIn(sand), run_time=0.5)
        self.play(Create(flask), run_time=0.7)
        self.play(LaggedStartMap(FadeIn, drops, lag_ratio=0.2), run_time=0.8)

        sand_lbl = Text("песок — на филтер", font_size=22, color=ORANGE).next_to(funnel, RIGHT, buff=0.8)
        water_lbl = Text("вода — низ", font_size=22, color=BLUE).next_to(flask, RIGHT, buff=0.8)
        self.play(Write(sand_lbl), Write(water_lbl), run_time=0.8)

        msg = Text("Цврстото останува. Течното поминува.",
                   font_size=24, color=GREEN).to_edge(DOWN, buff=0.3)
        self.play(Write(msg), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, funnel, sand, flask, drops,
                                  sand_lbl, water_lbl, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  МЕТОД 2 — ИСПАРУВАЊЕ                          ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("evaporation")

        t4 = section_title("Испарување — растворена сол")
        self.play(Write(t4), run_time=0.8)

        # Dish with salt water
        dish = Ellipse(width=4.5, height=1.0, color=WHITE2, stroke_width=3).shift(DOWN*0.5)
        dish_fill = Ellipse(width=4.3, height=0.85, color=BLUE, fill_opacity=0.5,
                             stroke_width=0).shift(DOWN*0.5)

        # heat source
        flame = Text("△△△", font_size=40, color=ORANGE).next_to(dish, DOWN, buff=0.4)
        heat_lbl = Text("топлина", font_size=20, color=ORANGE).next_to(flame, DOWN, buff=0.1)

        # vapor arrows
        vapors = VGroup(*[
            Arrow(start=dish.get_top()+RIGHT*(-1.5+i*0.7), end=dish.get_top()+RIGHT*(-1.5+i*0.7)+UP*1.2,
                   stroke_width=2, color=GREY, buff=0.05)
            for i in range(5)
        ])
        vapor_lbl = Text("водена пара одлета", font_size=22, color=GREY).next_to(vapors, UP, buff=0.2)

        self.play(Create(dish), FadeIn(dish_fill), run_time=0.7)
        self.play(Write(flame), Write(heat_lbl), run_time=0.7)
        self.play(LaggedStartMap(GrowArrow, vapors, lag_ratio=0.15), run_time=1.0)
        self.play(Write(vapor_lbl), run_time=0.6)

        # show salt crystals remain
        self.play(FadeOut(dish_fill), run_time=1.0)
        salt = VGroup(*[
            Square(side_length=0.18, fill_color=YELLOW, fill_opacity=1,
                    stroke_color=WHITE2, stroke_width=0.5).move_to(
                        dish.get_center() + np.array([random.uniform(-1.8,1.8), random.uniform(-0.2,0.1), 0]))
            for _ in range(12)
        ])
        self.play(FadeIn(salt), run_time=0.7)
        salt_lbl = Text("остаје сол.", font_size=26, color=YELLOW).next_to(dish, RIGHT, buff=0.6)
        self.play(Write(salt_lbl), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, dish, flame, heat_lbl, vapors, vapor_lbl, salt, salt_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  МЕТОД 3 — ДЕСТИЛАЦИЈА И МАГНЕТ                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("distill_magnet")

        t5 = section_title("Дестилација и магнет")
        self.play(Write(t5), run_time=0.8)

        # Left: distillation - boil flask + condenser + receiver
        boil = Circle(radius=0.6, fill_color=BLUE, fill_opacity=0.5,
                       stroke_color=WHITE2, stroke_width=2).shift(LEFT*4.7 + DOWN*0.5)
        boil_lbl = Text("грееш", font_size=18, color=ORANGE).next_to(boil, DOWN, buff=0.2)
        tube = Line(boil.get_top()+UP*0.05, [-1.8, 0.5, 0], stroke_color=WHITE2, stroke_width=3)
        cond = Line([-1.8, 0.5, 0], [-1.0, -0.8, 0], stroke_color=BLUE, stroke_width=3)
        recv = Circle(radius=0.5, fill_color=GREEN, fill_opacity=0.4,
                       stroke_color=WHITE2, stroke_width=2).move_to([-1.0, -1.2, 0])
        recv_lbl = Text("чиста вода", font_size=18, color=GREEN).next_to(recv, DOWN, buff=0.2)

        title_left = Text("Дестилација", font_size=24, color=BLUE, weight=BOLD).move_to(LEFT*3.5 + UP*2.0)

        self.play(Write(title_left), run_time=0.6)
        self.play(FadeIn(boil), Write(boil_lbl), run_time=0.6)
        self.play(Create(tube), Create(cond), run_time=0.8)
        self.play(FadeIn(recv), Write(recv_lbl), run_time=0.7)

        d_msg = Text("Различни точки на врење.", font_size=20, color=WHITE2)
        d_msg.move_to(LEFT*3.5 + DOWN*2.6)
        self.play(Write(d_msg), run_time=0.8)

        # Right: magnet attracting iron from sand
        title_right = Text("Магнет", font_size=24, color=ORANGE, weight=BOLD).move_to(RIGHT*3.5 + UP*2.0)
        self.play(Write(title_right), run_time=0.6)

        # Pile of sand+iron
        pile = VGroup()
        iron_bits = VGroup()
        for i in range(20):
            x = random.uniform(-1.5, 1.5); y = random.uniform(-1.6, -0.8)
            is_iron = random.random() < 0.5
            color = GREY if is_iron else ORANGE
            r = 0.10 if is_iron else 0.12
            c = Circle(radius=r, fill_color=color, fill_opacity=1,
                       stroke_width=0).move_to(RIGHT*3.5 + np.array([x,y,0]))
            if is_iron:
                iron_bits.add(c)
            else:
                pile.add(c)
        # Magnet U-shape
        mag_left = Rectangle(width=0.35, height=1.2, fill_color=RED, fill_opacity=1,
                              stroke_color=WHITE2, stroke_width=1).move_to(RIGHT*3.0 + UP*0.9)
        mag_right = Rectangle(width=0.35, height=1.2, fill_color=RED, fill_opacity=1,
                               stroke_color=WHITE2, stroke_width=1).move_to(RIGHT*4.0 + UP*0.9)
        mag_top = Rectangle(width=1.3, height=0.35, fill_color=RED, fill_opacity=1,
                             stroke_color=WHITE2, stroke_width=1).move_to(RIGHT*3.5 + UP*1.45)
        magnet = VGroup(mag_left, mag_right, mag_top)

        self.play(FadeIn(pile), FadeIn(iron_bits), run_time=0.6)
        self.play(FadeIn(magnet, shift=DOWN*0.3), run_time=0.6)
        # iron jumps to magnet
        self.play(iron_bits.animate.move_to(RIGHT*3.5 + UP*0.35), run_time=0.9)

        m_msg = Text("Железо лета. Песок останува.",
                     font_size=20, color=WHITE2).move_to(RIGHT*3.5 + DOWN*2.6)
        self.play(Write(m_msg), run_time=0.9)
        self.wait(1.4)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ХРОМАТОГРАФИЈА И КАТАЛОГ                      ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("chromato_catalog")

        t6 = section_title("Сите методи во каталог")
        self.play(Write(t6), run_time=0.8)

        def row(method, target, color, y):
            m = Text(method, font_size=24, color=color, weight=BOLD).move_to(LEFT*4.5 + UP*y)
            arr = Arrow(start=LEFT*2.6+UP*y, end=LEFT*0.8+UP*y, stroke_width=2, color=GREY, buff=0.1)
            tgt = Text(target, font_size=22, color=WHITE2).move_to(RIGHT*2.3 + UP*y)
            return VGroup(m, arr, tgt)

        r1 = row("Филтрирање", "цврсто + течно", BLUE, 2.0)
        r2 = row("Испарување", "растворена сол", YELLOW, 1.2)
        r3 = row("Дестилација", "различни точки врење", GREEN, 0.4)
        r4 = row("Хроматографија", "бои, пигменти", PURPLE, -0.4)
        r5 = row("Магнет", "железо", ORANGE, -1.2)
        r6 = row("Декантирање", "масло + вода", RED, -2.0)

        for r in (r1, r2, r3, r4, r5, r6):
            self.play(FadeIn(r, shift=RIGHT*0.2), run_time=0.45)
        self.wait(1.4)

        msg = Text("Прав метод за прав проблем.",
                   font_size=26, color=GREEN).to_edge(DOWN, buff=0.3)
        self.play(Write(msg), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t6, r1, r2, r3, r4, r5, r6, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ПРИМЕНА И CLOSER                              ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("applications")

        t7 = section_title("Зошто е важно?")
        self.play(Write(t7), run_time=0.8)

        apps = VGroup(
            Text("Чиста пиење вода.", font_size=28, color=BLUE),
            Text("Сол од море.", font_size=28, color=YELLOW),
            Text("Бензин од нафта.", font_size=28, color=ORANGE),
            Text("Кислород за болница.", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(ORIGIN+UP*0.2)

        for a in apps:
            self.play(Write(a), run_time=0.6)
        self.wait(0.5)

        last = Text("Без разделување — нема современ живот.",
                    font_size=26, color=RED).to_edge(DOWN, buff=0.6)
        self.play(Write(last), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t7, apps, last)), run_time=0.7)

        # Final 3-beat
        c1f = Text("Не повлекувај.", font_size=44, color=GREY, weight=BOLD).move_to(UP*1.0)
        c2f = Text("Не цеди.", font_size=44, color=GREY, weight=BOLD).move_to(ORIGIN)
        c3f = Text("Трпи.", font_size=58, color=GREEN, weight=BOLD).move_to(DOWN*1.2)

        self.play(Write(c1f), run_time=0.7)
        self.play(Write(c2f), run_time=0.7)
        self.play(Write(c3f), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(c1f, c2f, c3f)), run_time=0.7)
        self.wait(0.3)
