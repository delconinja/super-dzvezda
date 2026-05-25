"""
bio8-6-3  —  Подредување на безрбетници
Биологија 8, Единица 6: Класификација

Teaching narrative — Andonovski-style: 97% of animals, less spine,
more variety. Invertebrates as the silent majority.
Render:  manim -ql bio8-6-3.py Bio863Scene
Output:  media/videos/bio8-6-3/480p15/Bio863Scene.mp4
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


class Bio863Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — 97% are invertebrates                    ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("97% од животните —",
                     font_size=48, color=YELLOW, weight=BOLD)
        hook2 = Text("без 'рбет.",
                     font_size=60, color=ORANGE, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.3).to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.0)
        self.play(Write(hook2), run_time=1.0)
        self.wait(0.4)

        beats = VGroup(
            Text("Не помалку важни.",        font_size=38, color=GREEN, weight=BOLD),
            Text("Само поразновидни.",        font_size=38, color=BLUE, weight=BOLD),
            Text("Океаните, копното, воздухот —", font_size=32, color=WHITE2),
            Text("преполни.",                 font_size=42, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook_group, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(hook_group, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  PIE — 97/3                                       ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pie")

        title = section_title("Удел во животинскиот свет")
        self.play(Write(title), run_time=0.8)

        # Pie chart
        big = Sector(radius=2.0, start_angle=PI/2,
                     angle=-2 * PI * 0.97,
                     color=PURPLE, fill_color=PURPLE, fill_opacity=0.85,
                     stroke_color=WHITE2, stroke_width=2)
        small = Sector(radius=2.0, start_angle=PI/2 - 2 * PI * 0.97,
                       angle=-2 * PI * 0.03,
                       color=YELLOW, fill_color=YELLOW, fill_opacity=0.95,
                       stroke_color=WHITE2, stroke_width=2)
        pie = VGroup(big, small).shift(LEFT * 2.5 + DOWN * 0.3)

        self.play(Create(big), run_time=1.0)
        self.play(Create(small), run_time=0.6)
        self.wait(0.4)

        legend = VGroup(
            VGroup(
                Square(side_length=0.35, fill_color=PURPLE, fill_opacity=0.9,
                       stroke_width=1),
                Text("97% — Безрбетници", font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Square(side_length=0.35, fill_color=YELLOW, fill_opacity=0.95,
                       stroke_width=1),
                Text("3% — Рбетници", font_size=26, color=WHITE2),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        legend.next_to(pie, RIGHT, buff=1.2)

        for item in legend:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, pie, legend)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  SPONGES & CNIDARIANS                             ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sponges_cnidarians")

        title2 = section_title("Сунѓери и жаркари", color=BLUE)
        self.play(Write(title2), run_time=0.8)

        # Sponge shape (vase)
        sponge = VGroup(
            Polygon(
                np.array([-0.7, -1.0, 0]),
                np.array([0.7, -1.0, 0]),
                np.array([1.0, 0.9, 0]),
                np.array([-1.0, 0.9, 0]),
                color=ORANGE, fill_color=ORANGE, fill_opacity=0.7, stroke_width=3,
            ),
            Ellipse(width=1.6, height=0.4, color=ORANGE,
                    fill_color="#0d1b2e", fill_opacity=1, stroke_width=3).shift(UP * 0.9),
        ).shift(LEFT * 4 + DOWN * 0.5)
        sponge_lbl = Text("Сунѓери", font_size=22, color=ORANGE, weight=BOLD)
        sponge_lbl.next_to(sponge, DOWN, buff=0.3)

        # Jellyfish
        jelly_dome = Arc(radius=1.0, start_angle=0, angle=PI,
                         color=PURPLE, fill_color=PURPLE, fill_opacity=0.7,
                         stroke_width=3)
        tentacles = VGroup()
        for x in np.linspace(-0.8, 0.8, 5):
            t = Line(np.array([x, 0, 0]), np.array([x + 0.2 * np.sin(x * 3), -1.2, 0]),
                     color=PURPLE, stroke_width=3)
            tentacles.add(t)
        jelly = VGroup(jelly_dome, tentacles).shift(LEFT * 1 + DOWN * 0.3)
        jelly_lbl = Text("Жаркари (медузи)", font_size=22, color=PURPLE, weight=BOLD)
        jelly_lbl.next_to(jelly, DOWN, buff=0.3)

        self.play(Create(sponge), Create(jelly), run_time=1.4)
        self.play(FadeIn(sponge_lbl), FadeIn(jelly_lbl), run_time=0.6)
        self.wait(0.4)

        notes = VGroup(
            Text("• Сунѓери — без органи, филтрираат вода", font_size=22, color=ORANGE),
            Text("• Жаркари — желатинесто тело, пипала", font_size=22, color=PURPLE),
            Text("• Прибираат храна со жаречки клетки", font_size=22, color=RED),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        notes.next_to(jelly, RIGHT, buff=0.6)

        for n in notes:
            self.play(FadeIn(n, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, sponge, jelly, sponge_lbl,
                                  jelly_lbl, notes)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  WORMS — three kinds                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("worms")

        title3 = section_title("Црви", color=GREEN)
        self.play(Write(title3), run_time=0.8)

        # Three worm types
        worm_groups = [
            ("Плоснати црви",    "тенки, плосни", RED),
            ("Облени црви",      "цилиндрични",   YELLOW),
            ("Прстенести црви",  "сегменти — пр. дождовник", GREEN),
        ]

        cards = VGroup()
        for name, desc, color in worm_groups:
            card = RoundedRectangle(
                width=4.0, height=2.0, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            # Small worm icon
            if "Плоснати" in name:
                icon = Ellipse(width=1.4, height=0.25, color=color,
                               fill_color=color, fill_opacity=0.7)
            elif "Облени" in name:
                icon = Ellipse(width=1.4, height=0.5, color=color,
                               fill_color=color, fill_opacity=0.7)
            else:
                icon = VGroup(*[
                    Circle(radius=0.18, color=color, fill_color=color,
                           fill_opacity=0.7, stroke_width=2).shift(RIGHT * (i * 0.35 - 0.7))
                    for i in range(5)
                ])
            n = Text(name, font_size=22, color=color, weight=BOLD)
            d = Text(desc, font_size=18, color=WHITE2)
            content = VGroup(icon, n, d).arrange(DOWN, buff=0.18)
            content.move_to(card)
            cards.add(VGroup(card, content))

        cards.arrange(RIGHT, buff=0.3).next_to(title3, DOWN, buff=0.8)

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title3, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  MOLLUSCS                                          ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("molluscs")

        title4 = section_title("Мекотели", color=PURPLE)
        self.play(Write(title4), run_time=0.8)

        # Snail
        shell = Annulus(inner_radius=0.3, outer_radius=1.0,
                        color=ORANGE, fill_color=ORANGE, fill_opacity=0.75,
                        stroke_width=3)
        snail_body = Ellipse(width=2.0, height=0.7, color=YELLOW,
                             fill_color=YELLOW, fill_opacity=0.7, stroke_width=3)
        snail_body.next_to(shell, DOWN, buff=-0.5)
        antenna_l = Line(np.array([-0.7, -0.2, 0]), np.array([-1.0, 0.4, 0]),
                         color=YELLOW, stroke_width=3)
        antenna_r = Line(np.array([-0.4, -0.2, 0]), np.array([-0.7, 0.4, 0]),
                         color=YELLOW, stroke_width=3)
        snail = VGroup(snail_body, shell, antenna_l, antenna_r).shift(LEFT * 3.5)
        snail_lbl = Text("Полжав", font_size=22, color=YELLOW, weight=BOLD)
        snail_lbl.next_to(snail, DOWN, buff=0.3)

        # Octopus
        oct_head = Ellipse(width=1.6, height=1.4, color=PURPLE,
                           fill_color=PURPLE, fill_opacity=0.7, stroke_width=3)
        oct_arms = VGroup()
        for i in range(6):
            angle = -PI/2 - 0.5 + i * 0.2
            start = np.array([np.cos(angle) * 0.7, np.sin(angle) * 0.6, 0])
            end = np.array([np.cos(angle) * 1.6, np.sin(angle) * 1.6 - 0.4, 0])
            mid = (start + end) / 2 + np.array([0.1 * np.sin(i), -0.1, 0])
            arm = ArcBetweenPoints(start, end, angle=0.5,
                                   color=PURPLE, stroke_width=4)
            oct_arms.add(arm)
        oct_eye_l = Dot(point=np.array([-0.3, 0.2, 0]), radius=0.1, color=WHITE2)
        oct_eye_r = Dot(point=np.array([0.3, 0.2, 0]), radius=0.1, color=WHITE2)
        octopus = VGroup(oct_head, oct_arms, oct_eye_l, oct_eye_r).shift(RIGHT * 0.5 + DOWN * 0.2)
        oct_lbl = Text("Октопод", font_size=22, color=PURPLE, weight=BOLD)
        oct_lbl.next_to(octopus, DOWN, buff=0.3)

        self.play(Create(snail), Create(octopus), run_time=1.4)
        self.play(FadeIn(snail_lbl), FadeIn(oct_lbl), run_time=0.6)
        self.wait(0.4)

        notes4 = VGroup(
            Text("• Меко тело", font_size=22, color=PURPLE),
            Text("• Често со школка", font_size=22, color=ORANGE),
            Text("• Полжави, школки, октоподи", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        notes4.to_edge(RIGHT, buff=0.6).shift(UP * 0.3)

        for n in notes4:
            self.play(FadeIn(n, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, snail, octopus, snail_lbl,
                                  oct_lbl, notes4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ARTHROPODS — biggest group                       ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("arthropods")

        title5 = section_title("Зглавкари", color=ORANGE)
        self.play(Write(title5), run_time=0.8)

        sub5 = Text("Најбројна група животни на Земјата",
                    font_size=26, color=WHITE2)
        sub5.next_to(title5, DOWN, buff=0.25)
        self.play(FadeIn(sub5), run_time=0.6)

        groups5 = [
            ("Инсекти",   "пр. пчела, мравка", "6 нозе",       YELLOW),
            ("Пајакови",  "пр. пајак, штипалка", "8 нозе",     RED),
            ("Ракови",    "пр. рак, скакулец", "повеќе нозе",  BLUE),
        ]

        cards5 = VGroup()
        for name, ex, legs, color in groups5:
            card = RoundedRectangle(
                width=4.0, height=2.4, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=3,
            )
            n = Text(name, font_size=26, color=color, weight=BOLD)
            l = Text(legs, font_size=20, color=ORANGE, weight=BOLD)
            e = Text(ex, font_size=18, color=WHITE2)
            content = VGroup(n, l, e).arrange(DOWN, buff=0.22)
            content.move_to(card)
            cards5.add(VGroup(card, content))

        cards5.arrange(RIGHT, buff=0.3).next_to(sub5, DOWN, buff=0.5)

        for c in cards5:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)
        self.wait(1.0)

        punch5 = Text("Зглавкари — со надворешен скелет (хитин) и сегментирано тело.",
                      font_size=22, color=GREEN)
        punch5.next_to(cards5, DOWN, buff=0.5)
        self.play(Write(punch5), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title5, sub5, cards5, punch5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ECHINODERMS + CLOSE                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("echinoderms")

        title6 = section_title("Боднокожи", color=RED)
        self.play(Write(title6), run_time=0.8)

        # Starfish (5-armed star)
        star = Star(n=5, outer_radius=1.4, inner_radius=0.6,
                    color=RED, fill_color=RED, fill_opacity=0.75,
                    stroke_width=3)
        star.shift(LEFT * 3.5 + DOWN * 0.2)
        star_lbl = Text("Морска ѕвезда", font_size=22, color=RED, weight=BOLD)
        star_lbl.next_to(star, DOWN, buff=0.3)

        self.play(Create(star), run_time=1.0)
        self.play(FadeIn(star_lbl), run_time=0.5)
        self.wait(0.3)

        notes6 = VGroup(
            Text("• Радијална симетрија (петоделна)", font_size=23, color=RED),
            Text("• Боди и боцки по кожата", font_size=23, color=ORANGE),
            Text("• Само во море", font_size=23, color=BLUE),
            Text("Пр.: морска ѕвезда, морски еж", font_size=22, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        notes6.next_to(star, RIGHT, buff=0.8)

        for n in notes6:
            self.play(FadeIn(n, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title6, star, star_lbl, notes6)),
                  run_time=0.7)

        # CLOSE
        close1 = Text("Без 'рбет.",
                      font_size=46, color=PURPLE, weight=BOLD)
        close2 = Text("Со разновидност.",
                      font_size=42, color=GREEN, weight=BOLD)
        close3 = Text("Без нив —",
                      font_size=38, color=ORANGE)
        close4 = Text("тишина.",
                      font_size=72, color=YELLOW, weight=BOLD)
        cg = VGroup(close1, close2, close3, close4).arrange(DOWN, buff=0.5)

        for line in cg:
            self.play(Write(line), run_time=0.9)
            self.wait(0.35)
        self.wait(2.0)

        self.play(FadeOut(cg), run_time=1.0)
        self.wait(0.5)
