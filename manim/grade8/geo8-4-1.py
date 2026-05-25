"""
geo8-4-1  —  Велика Британија и Ирска
Географија 8, Единица 4: Западна Европа

Teaching narrative — Andonovski-style: three-beat punches,
Britain as fallen empire still proud, Ireland as freed sister,
British Isles as two siblings on the Atlantic.
Render:  manim -ql geo8-4-1.py Geo841Scene
Output:  media/videos/geo8-4-1/480p15/Geo841Scene.mp4
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


def region_card(name, capital, fact, color, pos):
    box = RoundedRectangle(
        width=3.4, height=2.4, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    nm = Text(name, font_size=24, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.75)
    cap = Text(capital, font_size=18, color=WHITE2)
    cap.move_to(box.get_center() + UP * 0.15)
    fc = Text(fact, font_size=14, color=GREY)
    fc.move_to(box.get_center() + DOWN * 0.55)
    return VGroup(box, nm, cap, fc)


def timeline_dot(year, label, color, pos):
    dot = Dot(point=pos, radius=0.16, color=color)
    yr = Text(year, font_size=20, color=color, weight=BOLD)
    yr.next_to(dot, UP, buff=0.18)
    lb = Text(label, font_size=16, color=WHITE2)
    lb.next_to(dot, DOWN, buff=0.18)
    return VGroup(dot, yr, lb)


class Geo841Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Британија беше империја.", font_size=40, color=RED, weight=BOLD)
        h2 = Text("Над која сонцето никогаш не заоѓало.", font_size=32, color=YELLOW)
        h3 = Text("Денес — острово.", font_size=36, color=BLUE, weight=BOLD)
        h4 = Text("Но сè уште силна. Сè уште важна.", font_size=30, color=WHITE2)

        hook = VGroup(h1, h2, h3, h4).arrange(DOWN, buff=0.45)

        self.play(Write(h1), run_time=1.4)
        self.play(FadeIn(h2, shift=UP * 0.3), run_time=1.2)
        self.wait(0.5)
        self.play(Write(h3), run_time=1.2)
        self.play(FadeIn(h4), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(hook), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  UK = 4 KINGDOMS                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("kingdoms")

        t2 = section_title("Обединето Кралство — четири нации", color=YELLOW)
        self.play(Write(t2), run_time=1.0)

        eng = region_card("Англија", "Лондон", "55 мил. жители", RED,    LEFT * 4.5 + UP * 0.4)
        sco = region_card("Шкотска", "Единбург", "Хајленди, виски", BLUE,   LEFT * 1.5 + UP * 0.4)
        wal = region_card("Велс",    "Кардиф",   "Келтски јазик",   GREEN,  RIGHT * 1.5 + UP * 0.4)
        nir = region_card("С. Ирска","Белфаст",  "Дел од Британија", ORANGE, RIGHT * 4.5 + UP * 0.4)

        self.play(FadeIn(eng, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(sco, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(wal, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(nir, shift=UP * 0.3), run_time=0.7)
        self.wait(1.0)

        co2 = callout("Една држава. Четири народи. Едно знаме.",
                      width=10.0, bg="#1a1230", border=YELLOW, font_size=28)
        co2.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(co2, shift=UP * 0.3), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(t2), FadeOut(eng), FadeOut(sco), FadeOut(wal),
                  FadeOut(nir), FadeOut(co2), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  LONDON & THE THAMES                             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("london")

        t3 = section_title("Лондон — срцето на островот", color=YELLOW)
        self.play(Write(t3), run_time=1.0)

        # river thames + city silhouette
        river = ParametricFunction(
            lambda t: np.array([t, 0.4 * np.sin(t * 1.2) - 1.5, 0]),
            t_range=[-5.5, 5.5], color=BLUE, stroke_width=6,
        )
        rlabel = Text("Темза", font_size=22, color=BLUE, weight=BOLD)
        rlabel.next_to(river, DOWN, buff=0.2).shift(LEFT * 4.0)

        # Big Ben + parliament block
        bigben = Rectangle(width=0.5, height=2.2, fill_color=YELLOW,
                           fill_opacity=0.9, stroke_color=YELLOW)
        bigben.move_to(LEFT * 1.5 + UP * 0.4)
        bb_top = Triangle(fill_color=YELLOW, fill_opacity=0.9, stroke_color=YELLOW)
        bb_top.scale(0.35).next_to(bigben, UP, buff=0.0)
        bb_lbl = Text("Биг Бен", font_size=16, color=YELLOW).next_to(bigben, UP, buff=0.5)

        parl = Rectangle(width=2.6, height=1.2, fill_color=DARK_CARD,
                         fill_opacity=1, stroke_color=GREY, stroke_width=2)
        parl.next_to(bigben, RIGHT, buff=0.1).align_to(bigben, DOWN)
        parl_lbl = Text("Парламент", font_size=16, color=GREY).next_to(parl, DOWN, buff=0.1)

        # Eye (London Eye)
        eye = Circle(radius=0.7, color=WHITE2, stroke_width=3)
        eye.move_to(RIGHT * 3.5 + UP * 0.0)
        eye_lbl = Text("Лондонско око", font_size=16, color=WHITE2).next_to(eye, UP, buff=0.2)

        self.play(Create(river), Write(rlabel), run_time=1.5)
        self.play(FadeIn(parl), Write(parl_lbl), run_time=0.9)
        self.play(FadeIn(bigben), FadeIn(bb_top), Write(bb_lbl), run_time=0.9)
        self.play(Create(eye), Write(eye_lbl), run_time=1.0)

        facts = VGroup(
            Text("9 мил. жители", font_size=22, color=WHITE2),
            Text("Финансиски центар на светот", font_size=20, color=GREEN),
            Text("Кралица. Метро. Магла.", font_size=20, color=GREY),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)
        self.play(Write(facts), run_time=1.4)
        self.wait(2.0)
        self.play(FadeOut(t3), FadeOut(river), FadeOut(rlabel), FadeOut(parl),
                  FadeOut(parl_lbl), FadeOut(bigben), FadeOut(bb_top), FadeOut(bb_lbl),
                  FadeOut(eye), FadeOut(eye_lbl), FadeOut(facts), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  INDUSTRIAL REVOLUTION                           ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("industry")

        t4 = section_title("Колевка на индустриската револуција", color=ORANGE)
        self.play(Write(t4), run_time=1.0)

        line = Line(LEFT * 5.5 + DOWN * 0.5, RIGHT * 5.5 + DOWN * 0.5,
                    color=GREY, stroke_width=3)
        self.play(Create(line), run_time=0.8)

        d1 = timeline_dot("1769", "Парна машина — Ват",  ORANGE, LEFT * 4.5 + DOWN * 0.5)
        d2 = timeline_dot("1825", "Прва железница",      YELLOW, LEFT * 1.5 + DOWN * 0.5)
        d3 = timeline_dot("1850", "Светска фабрика",     RED,    RIGHT * 1.5 + DOWN * 0.5)
        d4 = timeline_dot("Денес","Постиндустриска",     BLUE,   RIGHT * 4.5 + DOWN * 0.5)

        self.play(FadeIn(d1), run_time=0.6)
        self.play(FadeIn(d2), run_time=0.6)
        self.play(FadeIn(d3), run_time=0.6)
        self.play(FadeIn(d4), run_time=0.6)
        self.wait(0.6)

        co4 = callout("Британија ја научи Европа да работи со пареа.",
                      width=11.0, bg="#2a1810", border=ORANGE, font_size=26)
        co4.to_edge(UP, buff=1.5)
        self.play(FadeIn(co4, shift=DOWN * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t4), FadeOut(line), FadeOut(d1), FadeOut(d2),
                  FadeOut(d3), FadeOut(d4), FadeOut(co4), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  BREXIT 2020                                     ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("brexit")

        t5 = section_title("Брегзит — 2020 година", color=RED)
        self.play(Write(t5), run_time=1.0)

        # EU circle with UK breaking off
        eu = Circle(radius=2.2, color=BLUE, stroke_width=5,
                    fill_color=BLUE, fill_opacity=0.18)
        eu.move_to(LEFT * 2.5)
        eu_lbl = Text("ЕУ", font_size=32, color=BLUE, weight=BOLD).move_to(eu)

        uk = Circle(radius=1.0, color=RED, stroke_width=4,
                    fill_color=RED, fill_opacity=0.25)
        uk.move_to(eu.get_center())
        uk_lbl = Text("ОК", font_size=22, color=RED, weight=BOLD).move_to(uk)

        self.play(Create(eu), Write(eu_lbl), run_time=1.0)
        self.play(FadeIn(uk), Write(uk_lbl), run_time=0.8)
        self.wait(0.5)

        # break-off arrow
        arrow = Arrow(eu.get_right() + LEFT * 0.5, RIGHT * 3.0,
                      color=RED, buff=0.0, stroke_width=6)
        self.play(uk.animate.move_to(RIGHT * 3.5),
                  uk_lbl.animate.move_to(RIGHT * 3.5),
                  Create(arrow), run_time=1.6)
        self.wait(0.6)

        yr = Text("31 јануари 2020", font_size=30, color=YELLOW, weight=BOLD)
        yr.to_edge(DOWN, buff=1.6)
        reason = Text("52% — за излез. 48% — против.", font_size=24, color=WHITE2)
        reason.next_to(yr, DOWN, buff=0.25)
        self.play(Write(yr), Write(reason), run_time=1.4)
        self.wait(2.0)
        self.play(FadeOut(t5), FadeOut(eu), FadeOut(eu_lbl), FadeOut(uk),
                  FadeOut(uk_lbl), FadeOut(arrow), FadeOut(yr), FadeOut(reason),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  IRELAND — THE FREED SISTER                      ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ireland")

        t6 = section_title("Ирска — посебна држава", color=GREEN)
        self.play(Write(t6), run_time=1.0)

        # Two islands schematic
        gb_isle = Ellipse(width=2.8, height=4.0, color=RED,
                          stroke_width=3, fill_color=RED, fill_opacity=0.25)
        gb_isle.move_to(RIGHT * 1.5 + DOWN * 0.2)
        gb_lbl = Text("Велика Британија", font_size=20, color=RED, weight=BOLD)
        gb_lbl.next_to(gb_isle, UP, buff=0.2)

        ire_isle = Ellipse(width=2.2, height=3.0, color=GREEN,
                           stroke_width=3, fill_color=GREEN, fill_opacity=0.25)
        ire_isle.move_to(LEFT * 2.5 + DOWN * 0.2)
        ire_lbl = Text("Ирска", font_size=22, color=GREEN, weight=BOLD)
        ire_lbl.next_to(ire_isle, UP, buff=0.2)

        nir_part = Ellipse(width=0.9, height=0.8, color=ORANGE,
                           stroke_width=2, fill_color=ORANGE, fill_opacity=0.4)
        nir_part.move_to(ire_isle.get_center() + UP * 0.9 + RIGHT * 0.6)
        nir_lbl = Text("С. Ирска", font_size=12, color=ORANGE).next_to(nir_part, UP, buff=0.05)

        self.play(FadeIn(gb_isle), Write(gb_lbl), run_time=0.9)
        self.play(FadeIn(ire_isle), Write(ire_lbl), run_time=0.9)
        self.play(FadeIn(nir_part), Write(nir_lbl), run_time=0.7)
        self.wait(0.5)

        ire_facts = VGroup(
            Text("Главен град: Даблин", font_size=22, color=WHITE2),
            Text("Независност 1922", font_size=20, color=YELLOW),
            Text("Член на ЕУ — останува", font_size=20, color=BLUE),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)
        self.play(Write(ire_facts), run_time=1.4)
        self.wait(2.0)
        self.play(FadeOut(t6), FadeOut(gb_isle), FadeOut(gb_lbl), FadeOut(ire_isle),
                  FadeOut(ire_lbl), FadeOut(nir_part), FadeOut(nir_lbl),
                  FadeOut(ire_facts), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ATLANTIC CLIMATE — CLOSING                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        t7 = section_title("Атлантска клима — мека и влажна", color=BLUE)
        self.play(Write(t7), run_time=1.0)

        # raindrops over islands
        cloud = Ellipse(width=4.5, height=1.4, color=GREY,
                        stroke_width=3, fill_color=GREY, fill_opacity=0.4)
        cloud.move_to(UP * 1.5)
        self.play(FadeIn(cloud), run_time=0.7)

        drops = VGroup(*[
            Line(UP * 0.3, DOWN * 0.3, color=BLUE, stroke_width=3)
            .move_to(cloud.get_center() + DOWN * 0.9 + RIGHT * (-2.0 + 0.5 * i))
            for i in range(9)
        ])
        self.play(*[FadeIn(d) for d in drops], run_time=0.8)
        self.play(drops.animate.shift(DOWN * 1.5), run_time=1.0)

        climate_facts = VGroup(
            Text("Голфска струја — топла вода", font_size=24, color=ORANGE),
            Text("Зима блага. Лето свежо.", font_size=22, color=WHITE2),
            Text("Дожд — секој ден. Магла — секое утро.", font_size=20, color=GREY),
        ).arrange(DOWN, buff=0.2).next_to(drops, DOWN, buff=0.4)
        self.play(Write(climate_facts), run_time=1.6)
        self.wait(2.0)

        self.play(FadeOut(t7), FadeOut(cloud), FadeOut(drops),
                  FadeOut(climate_facts), run_time=0.8)

        # Final punch
        f1 = Text("Британски острови.", font_size=42, color=YELLOW, weight=BOLD)
        f2 = Text("Две сестри. Еден океан.", font_size=34, color=BLUE)
        f3 = Text("Историја.", font_size=44, color=RED, weight=BOLD)
        finale = VGroup(f1, f2, f3).arrange(DOWN, buff=0.5)
        self.play(Write(f1), run_time=1.0)
        self.play(FadeIn(f2, shift=UP * 0.3), run_time=1.0)
        self.play(Write(f3), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(finale), run_time=1.0)
