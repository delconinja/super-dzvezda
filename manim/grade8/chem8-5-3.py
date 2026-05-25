"""
chem8-5-3  —  Фосилни и алтернативни горива
Хемија 8, Единица 5: Органска хемија

Teaching narrative — Andonovski-style: three-beat punches,
fuels as ancient sunlight, personification, one-word finishers.
Render:  manim -ql chem8-5-3.py Chem853Scene
Output:  media/videos/chem8-5-3/480p15/Chem853Scene.mp4
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


class Chem853Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — bensinot e stara svetlina               ~26 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Бензинот е стара светлина.",
                  font_size=46, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.4)
        self.wait(0.4)

        beats = VGroup(
            Text("Растенијата го собрале Сонцето.",
                 font_size=32, color=GREEN),
            Text("Пред милиони години.", font_size=30, color=GREY),
            Text("Сега го гориме.", font_size=32, color=ORANGE),
            Text("За еден возен.", font_size=30, color=RED),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
            self.wait(0.2)

        self.wait(0.5)

        question = Text("Дојде ли ред да штедиме?",
                        font_size=36, color=PURPLE, weight=BOLD)
        question.to_edge(DOWN, buff=0.7)
        self.play(Write(question), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(h1, beats, question)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  FORMATION — sun→plants→buried→fuel              ~36 s
        # ══════════════════════════════════════════════════════════
        self.next_section("formation")

        title = section_title("Како настанале", color=ORANGE)
        self.play(Write(title), run_time=0.8)

        # 4 stages across the screen
        positions = [LEFT*5.5, LEFT*1.8, RIGHT*1.8, RIGHT*5.5]

        # stage 1: sun + plant
        sun = Circle(radius=0.35, fill_color=YELLOW, fill_opacity=1,
                     stroke_color=ORANGE, stroke_width=2)
        sun.move_to(positions[0] + UP*0.8)
        rays = VGroup(*[
            Line(positions[0] + UP*0.8,
                 positions[0] + UP*0.8 + np.array([np.cos(a)*0.6,
                                                   np.sin(a)*0.6, 0]),
                 color=YELLOW, stroke_width=2)
            for a in np.linspace(0, 2*PI, 9)[:-1]
        ])
        plant = VGroup(
            Triangle(color=GREEN, fill_opacity=1).scale(0.4)
                .move_to(positions[0] + DOWN*0.4),
            Line(positions[0] + DOWN*0.6, positions[0] + DOWN*1.0,
                 color="#5d4037", stroke_width=4),
        )
        s1_lbl = Text("Живот", font_size=22, color=GREEN)
        s1_lbl.next_to(plant, DOWN, buff=0.3)
        stage1 = VGroup(sun, rays, plant, s1_lbl)

        # stage 2: dead organisms buried
        ground = Rectangle(width=2.2, height=0.4, color="#5d4037",
                           fill_opacity=0.7, stroke_width=1)
        ground.move_to(positions[1] + DOWN*0.5)
        layers = VGroup(*[
            Rectangle(width=2.2, height=0.15,
                      fill_color=c, fill_opacity=0.7, stroke_width=0)
                .move_to(positions[1] + DOWN*(0.7 + i*0.18))
            for i, c in enumerate(["#6d4c41", "#4e342e", "#3e2723", "#212121"])
        ])
        bones = VGroup(
            Dot(positions[1] + DOWN*0.55 + LEFT*0.3, color=WHITE2, radius=0.06),
            Dot(positions[1] + DOWN*0.55 + RIGHT*0.2, color=WHITE2, radius=0.06),
            Dot(positions[1] + DOWN*0.5, color=WHITE2, radius=0.06),
        )
        s2_lbl = Text("Закопано", font_size=22, color=GREY)
        s2_lbl.next_to(layers, DOWN, buff=0.3)
        stage2 = VGroup(ground, layers, bones, s2_lbl)

        # stage 3: millions of years (clock + pressure arrows)
        clock = Circle(radius=0.5, color=YELLOW, stroke_width=3)
        clock.move_to(positions[2] + UP*0.3)
        hand1 = Line(positions[2] + UP*0.3,
                     positions[2] + UP*0.3 + UP*0.35,
                     color=YELLOW, stroke_width=3)
        hand2 = Line(positions[2] + UP*0.3,
                     positions[2] + UP*0.3 + RIGHT*0.3,
                     color=YELLOW, stroke_width=2)
        millions = Text("Милиони\nгодини", font_size=20,
                        color=WHITE2).next_to(clock, DOWN, buff=0.3)
        stage3 = VGroup(clock, hand1, hand2, millions)

        # stage 4: oil drum / fuel (2D representation)
        drum = VGroup(
            Rectangle(width=0.9, height=1.0,
                      fill_color="#37474f", fill_opacity=1,
                      stroke_color=WHITE2, stroke_width=2),
            Ellipse(width=0.9, height=0.2,
                    fill_color="#546e7a", fill_opacity=1,
                    stroke_color=WHITE2, stroke_width=1.5)
                .shift(UP*0.5),
        )
        drum.move_to(positions[3] + UP*0.1)
        fuel_lbl = Text("Гориво", font_size=22, color=ORANGE)
        fuel_lbl.next_to(drum, DOWN, buff=0.3)
        stage4 = VGroup(drum, fuel_lbl)

        # arrows between stages
        arrow_y = UP*0.1
        arrows = VGroup(
            Arrow(positions[0] + RIGHT*1.0 + arrow_y,
                  positions[1] + LEFT*1.0 + arrow_y,
                  color=WHITE2, stroke_width=3, buff=0.1),
            Arrow(positions[1] + RIGHT*1.0 + arrow_y,
                  positions[2] + LEFT*0.8 + arrow_y,
                  color=WHITE2, stroke_width=3, buff=0.1),
            Arrow(positions[2] + RIGHT*0.8 + arrow_y,
                  positions[3] + LEFT*1.0 + arrow_y,
                  color=WHITE2, stroke_width=3, buff=0.1),
        )

        self.play(FadeIn(stage1), run_time=0.8)
        self.play(Create(arrows[0]), run_time=0.4)
        self.play(FadeIn(stage2), run_time=0.8)
        self.play(Create(arrows[1]), run_time=0.4)
        self.play(FadeIn(stage3), run_time=0.8)
        self.play(Create(arrows[2]), run_time=0.4)
        self.play(FadeIn(stage4), run_time=0.8)
        self.wait(1.0)

        finite = callout("Конечно. Не се обновува.",
                         width=9, bg=DARK_CARD, border=RED, font_size=28)
        finite.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(finite, shift=UP*0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, stage1, stage2, stage3, stage4,
                                 arrows, finite)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  THREE FOSSIL FUELS                              ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_fuels")

        title2 = section_title("Три фосилни горива", color=YELLOW)
        self.play(Write(title2), run_time=0.7)

        def fuel_card(pos, name, state, sketch_color, icon_text, col):
            box = RoundedRectangle(
                width=3.6, height=3.4, corner_radius=0.3,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            icon = Text(icon_text, font_size=48, color=sketch_color, weight=BOLD)
            icon.move_to(pos + UP*0.6)
            name_t = Text(name, font_size=26, color=col, weight=BOLD)
            name_t.move_to(pos + DOWN*0.2)
            state_t = Text(state, font_size=20, color=WHITE2)
            state_t.move_to(pos + DOWN*0.7)
            return VGroup(box, icon, name_t, state_t)

        coal = fuel_card(LEFT*4.2, "Јаглен", "Цврст",
                         GREY, "■", GREY)
        oil = fuel_card(ORIGIN, "Нафта", "Течна",
                        "#5d4037", "≈", "#5d4037")
        gas = fuel_card(RIGHT*4.2, "Природен гас", "Гасовит",
                        BLUE, "～", BLUE)

        for c in [coal, oil, gas]:
            self.play(FadeIn(c, shift=UP*0.3), run_time=0.6)

        self.wait(0.5)

        all_carbon = Text("Сите се ланци од јаглерод и водород.",
                          font_size=26, color=YELLOW)
        all_carbon.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(all_carbon), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title2, coal, oil, gas, all_carbon)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  ALTERNATIVE FUELS                               ~36 s
        # ══════════════════════════════════════════════════════════
        self.next_section("alternatives")

        title3 = section_title("Алтернативни горива", color=GREEN)
        self.play(Write(title3), run_time=0.8)

        def alt_card(pos, name, desc, col):
            box = RoundedRectangle(
                width=3.0, height=2.4, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            n = Text(name, font_size=24, color=col, weight=BOLD)
            d = Text(desc, font_size=18, color=WHITE2)
            VGroup(n, d).arrange(DOWN, buff=0.25).move_to(box)
            return VGroup(box, n, d)

        biofuel = alt_card(LEFT*4.5 + UP*0.3, "Биогориво",
                           "од растенија\n(биоетанол)", GREEN)
        hydrogen = alt_card(LEFT*1.5 + UP*0.3, "Водород",
                            "H₂ — само вода\nкако продукт", BLUE)
        solar = alt_card(RIGHT*1.5 + UP*0.3, "Сонце",
                         "соларни\nпанели", YELLOW)
        wind = alt_card(RIGHT*4.5 + UP*0.3, "Ветер\nи вода",
                        "турбини,\nхидро-централи", PURPLE)

        for c in [biofuel, hydrogen, solar, wind]:
            self.play(FadeIn(c, shift=UP*0.2), run_time=0.55)

        self.wait(0.6)

        renew = callout("Обновливи. Не свршуваат.",
                        width=9, bg=DARK_CARD, border=GREEN, font_size=28)
        renew.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(renew, shift=UP*0.2), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(title3, biofuel, hydrogen, solar, wind, renew)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  PROS & CONS                                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pros_cons")

        title4 = section_title("Што добиваме. Што губиме.",
                               color=ORANGE)
        self.play(Write(title4), run_time=0.9)

        # two columns
        left_box = RoundedRectangle(
            width=5.5, height=4.2, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=RED, stroke_width=2,
        ).move_to(LEFT*3.2 + DOWN*0.2)
        left_title = Text("Фосилни", font_size=28, color=RED, weight=BOLD)
        left_title.move_to(left_box.get_top() + DOWN*0.4)
        left_items = VGroup(
            Text("+ Моќни. Концентрирани.", font_size=20, color=GREEN),
            Text("+ Лесна инфраструктура.", font_size=20, color=GREEN),
            Text("− Загадуваат.", font_size=20, color=RED),
            Text("− Свршуваат.", font_size=20, color=RED),
            Text("− Климатска криза.", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        left_items.next_to(left_title, DOWN, buff=0.3)

        right_box = RoundedRectangle(
            width=5.5, height=4.2, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).move_to(RIGHT*3.2 + DOWN*0.2)
        right_title = Text("Алтернативни",
                           font_size=28, color=GREEN, weight=BOLD)
        right_title.move_to(right_box.get_top() + DOWN*0.4)
        right_items = VGroup(
            Text("+ Чисти. Обновливи.", font_size=20, color=GREEN),
            Text("+ Помал отпечаток.", font_size=20, color=GREEN),
            Text("− Скапа технологија.", font_size=20, color=RED),
            Text("− Зависат од време.", font_size=20, color=RED),
            Text("− Помалку густи.", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        right_items.next_to(right_title, DOWN, buff=0.3)

        self.play(Create(left_box), Create(right_box), run_time=0.8)
        self.play(Write(left_title), Write(right_title), run_time=0.7)

        for i in range(5):
            self.play(FadeIn(left_items[i]), FadeIn(right_items[i]),
                      run_time=0.4)

        self.wait(1.4)

        self.play(FadeOut(VGroup(title4, left_box, left_title, left_items,
                                 right_box, right_title, right_items)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  FINISHER                                        ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("finisher")

        final = VGroup(
            Text("Сонцето уште свети.", font_size=38, color=YELLOW),
            Text("Ветерот уште дува.", font_size=38, color=BLUE),
            Text("Водата уште тече.", font_size=38, color=GREEN),
            Text("Сè уште избираме.",
                 font_size=42, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for f in final:
            self.play(FadeIn(f, shift=UP*0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(1.0)

        finisher = Text("Избор.", font_size=50, color=PURPLE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.6)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(final, finisher)), run_time=0.9)
        self.wait(0.4)
