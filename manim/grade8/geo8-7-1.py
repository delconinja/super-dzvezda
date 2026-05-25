"""
geo8-7-1  —  Русија — најголема земја во светот
Географија 8, Единица 7: Источна Европа

Teaching narrative — Andonovski-style: three-beat punches,
space as a character, time zones as voices.
Render:  manim -ql geo8-7-1.py Geo871Scene
Output:  media/videos/geo8-7-1/480p15/Geo871Scene.mp4
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


def stat_card(value, label, color, pos, w=2.6, h=1.5):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    v = Text(value, font_size=30, color=color, weight=BOLD)
    l = Text(label, font_size=18, color=WHITE2)
    v.move_to(box.get_center() + UP * 0.2)
    l.next_to(v, DOWN, buff=0.15)
    return VGroup(box, v, l)


class Geo871Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — 11 часовни зони                        ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Русија е огромна.", font_size=56, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.6)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("11 часовни зони.", font_size=44, color=ORANGE, weight=BOLD),
            Text("Кога утро во Москва —", font_size=34, color=BLUE),
            Text("вечер во Владивосток.", font_size=34, color=PURPLE),
            Text("Иста држава.", font_size=38, color=YELLOW, weight=BOLD),
            Text("Различни денови.", font_size=40, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.9)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  ГОЛЕМИНА — 17 милиони км²                     ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("golemina")

        title = section_title("Најголемата земја во светот")
        self.play(FadeIn(title), run_time=0.6)

        # Russia silhouette (very stylized — wide horizontal band)
        russia = Polygon(
            [-6.0, 1.2, 0], [-5.5, 1.8, 0], [-3.0, 2.0, 0], [-1.5, 1.6, 0],
            [0.5, 1.8, 0], [2.5, 2.0, 0], [4.5, 1.6, 0], [6.0, 1.8, 0],
            [6.2, 1.0, 0], [5.5, 0.4, 0], [4.0, 0.2, 0], [2.0, -0.2, 0],
            [0.0, 0.0, 0], [-2.0, -0.3, 0], [-3.5, 0.2, 0], [-5.0, 0.6, 0],
            [-6.2, 0.8, 0],
            fill_color="#1a3a5c", fill_opacity=0.85,
            stroke_color=YELLOW, stroke_width=2,
        ).shift(UP * 0.3)
        self.play(DrawBorderThenFill(russia), run_time=2.0)

        # Add cities
        moscow = Dot(point=russia.get_left() + RIGHT * 1.4 + UP * 0.4, color=RED, radius=0.13)
        moscow_lbl = Text("Москва", font_size=22, color=WHITE2, weight=BOLD).next_to(moscow, UP, buff=0.12)
        vlad = Dot(point=russia.get_right() + LEFT * 0.6, color=RED, radius=0.13)
        vlad_lbl = Text("Владивосток", font_size=22, color=WHITE2, weight=BOLD).next_to(vlad, UP, buff=0.12)

        self.play(GrowFromCenter(moscow), Write(moscow_lbl),
                  GrowFromCenter(vlad), Write(vlad_lbl), run_time=0.9)

        # Stats below
        stats = VGroup(
            stat_card("17 мил.", "км²", BLUE, ORIGIN),
            stat_card("146 мил.", "жители", GREEN, ORIGIN),
            stat_card("11", "часовни зони", ORANGE, ORIGIN),
            stat_card("№1", "по површина", YELLOW, ORIGIN),
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.5)

        for s in stats:
            self.play(FadeIn(s, shift=UP * 0.2), run_time=0.45)

        self.wait(1.4)
        self.play(FadeOut(VGroup(title, russia, moscow, moscow_lbl,
                                  vlad, vlad_lbl, stats)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  ДВА КОНТИНЕНТИ — Урал                         ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ural")

        title2 = section_title("Урал — границата", color=GREEN)
        self.play(FadeIn(title2), run_time=0.6)

        # Europe (left) and Asia (right) with Ural between
        europe = RoundedRectangle(width=4.5, height=3.0, corner_radius=0.2,
                                  fill_color=BLUE, fill_opacity=0.5,
                                  stroke_color=WHITE2, stroke_width=2).shift(LEFT * 3.0 + DOWN * 0.3)
        europe_lbl = Text("ЕВРОПА", font_size=32, color=WHITE2, weight=BOLD).move_to(europe.get_center() + UP * 0.8)
        europe_sub = Text("западен дел\n25%", font_size=22, color=YELLOW).move_to(europe.get_center() + DOWN * 0.4)

        asia = RoundedRectangle(width=5.5, height=3.0, corner_radius=0.2,
                                fill_color=ORANGE, fill_opacity=0.4,
                                stroke_color=WHITE2, stroke_width=2).shift(RIGHT * 2.6 + DOWN * 0.3)
        asia_lbl = Text("АЗИЈА", font_size=32, color=WHITE2, weight=BOLD).move_to(asia.get_center() + UP * 0.8)
        asia_sub = Text("источен дел\n75%", font_size=22, color=YELLOW).move_to(asia.get_center() + DOWN * 0.4)

        # Ural — wavy vertical line
        ural = VMobject(stroke_color=GREY, stroke_width=6)
        ural.set_points_smoothly([
            np.array([-0.2, 1.5, 0]),
            np.array([0.1, 0.5, 0]),
            np.array([-0.1, -0.5, 0]),
            np.array([0.1, -1.5, 0]),
        ])

        self.play(FadeIn(europe), Write(europe_lbl), Write(europe_sub), run_time=0.9)
        self.play(FadeIn(asia), Write(asia_lbl), Write(asia_sub), run_time=0.9)
        self.play(Create(ural), run_time=1.0)

        ural_lbl = Text("Урал", font_size=24, color=YELLOW, weight=BOLD).next_to(ural, UP, buff=0.2)
        self.play(Write(ural_lbl), run_time=0.6)

        fact = Text("Една земја — два континенти.",
                    font_size=30, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(fact), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, europe, europe_lbl, europe_sub,
                                  asia, asia_lbl, asia_sub, ural, ural_lbl, fact)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  КЛИМА И ПРИРОДА — Сибир                       ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("klima")

        title3 = section_title("Сибир — кралство на студ", color=BLUE)
        self.play(FadeIn(title3), run_time=0.6)

        # Three zones — vertical bands
        tundra = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                  fill_color="#a8c8e8", fill_opacity=0.6,
                                  stroke_color=WHITE2, stroke_width=2).shift(LEFT * 4.0 + DOWN * 0.3)
        tundra_lbl = Text("ТУНДРА", font_size=28, color="#0d1b2e", weight=BOLD).move_to(tundra.get_center() + UP * 1.4)
        tundra_d = VGroup(
            Text("Мраз", font_size=20, color="#0d1b2e"),
            Text("Мов и лишај", font_size=20, color="#0d1b2e"),
            Text("Северни елени", font_size=20, color="#0d1b2e"),
        ).arrange(DOWN, buff=0.18).move_to(tundra.get_center() + DOWN * 0.4)

        taiga = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                 fill_color="#2d5d3a", fill_opacity=0.7,
                                 stroke_color=WHITE2, stroke_width=2).shift(DOWN * 0.3)
        taiga_lbl = Text("ТАЈГА", font_size=28, color=WHITE2, weight=BOLD).move_to(taiga.get_center() + UP * 1.4)
        taiga_d = VGroup(
            Text("Иглолисни шуми", font_size=20, color=WHITE2),
            Text("Бор, ела, смрча", font_size=20, color=WHITE2),
            Text("Мечки, волци", font_size=20, color=WHITE2),
        ).arrange(DOWN, buff=0.18).move_to(taiga.get_center() + DOWN * 0.4)

        step = RoundedRectangle(width=3.5, height=4.0, corner_radius=0.2,
                                fill_color="#c2a468", fill_opacity=0.7,
                                stroke_color=WHITE2, stroke_width=2).shift(RIGHT * 4.0 + DOWN * 0.3)
        step_lbl = Text("СТЕПА", font_size=28, color="#0d1b2e", weight=BOLD).move_to(step.get_center() + UP * 1.4)
        step_d = VGroup(
            Text("Тревни рамнини", font_size=20, color="#0d1b2e"),
            Text("Жито и пченица", font_size=20, color="#0d1b2e"),
            Text("Топли лета", font_size=20, color="#0d1b2e"),
        ).arrange(DOWN, buff=0.18).move_to(step.get_center() + DOWN * 0.4)

        self.play(FadeIn(tundra), Write(tundra_lbl), run_time=0.7)
        self.play(Write(tundra_d), run_time=0.6)
        self.play(FadeIn(taiga), Write(taiga_lbl), run_time=0.7)
        self.play(Write(taiga_d), run_time=0.6)
        self.play(FadeIn(step), Write(step_lbl), run_time=0.7)
        self.play(Write(step_d), run_time=0.6)

        cold = Text("Во Сибир — до −60°C. Реки замрзнуваат. Земјата замолчува.",
                    font_size=24, color=BLUE).to_edge(DOWN, buff=0.4)
        self.play(Write(cold), run_time=1.2)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title3, tundra, tundra_lbl, tundra_d,
                                  taiga, taiga_lbl, taiga_d,
                                  step, step_lbl, step_d, cold)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  БОГАТСТВА — нафта, гас, минерали              ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("bogatstva")

        title4 = section_title("Богатства под земјата", color=ORANGE)
        self.play(FadeIn(title4), run_time=0.6)

        intro = Text("Русија — еден од најбогатите со суровини.",
                     font_size=28, color=WHITE2).next_to(title4, DOWN, buff=0.3)
        self.play(Write(intro), run_time=0.9)

        resources = VGroup(
            stat_card("Нафта", "№3 во светот", "#3d2820", ORIGIN),
            stat_card("Гас", "№2 во светот", BLUE, ORIGIN),
            stat_card("Јаглен", "огромни залихи", GREY, ORIGIN),
            stat_card("Дрво", "тајга = шума", GREEN, ORIGIN),
            stat_card("Метали", "никел, злато", YELLOW, ORIGIN),
            stat_card("Дијаманти", "Јакутија", PURPLE, ORIGIN),
        ).arrange_in_grid(rows=2, cols=3, buff=0.3).shift(DOWN * 0.3)

        for r in resources:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.35)

        export = Text("Гасот од Сибир грее половина Европа.",
                      font_size=26, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(export), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title4, intro, resources, export)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  ИСТОРИЈА — Царство, СССР, Федерација          ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("istorija")

        title5 = section_title("Историја — три лица", color=RED)
        self.play(FadeIn(title5), run_time=0.6)

        # Timeline
        line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=WHITE2, stroke_width=3).shift(DOWN * 0.5)
        self.play(Create(line), run_time=0.8)

        markers = [
            (LEFT * 4.5, "1547", "Царство", "Иван Грозни", BLUE),
            (LEFT * 0.5, "1917", "Револуција", "Совети", RED),
            (RIGHT * 2.0, "1922", "СССР", "15 републики", YELLOW),
            (RIGHT * 4.8, "1991", "Федерација", "денешна Русија", GREEN),
        ]

        for pos, year, label, sub, col in markers:
            d = Dot(point=line.get_center() + pos - line.get_center() + DOWN * 0.0, color=col, radius=0.15)
            d.move_to(line.point_from_proportion((pos[0] + 5.5) / 11.0))
            yr = Text(year, font_size=22, color=col, weight=BOLD).next_to(d, UP, buff=0.2)
            lb = Text(label, font_size=20, color=WHITE2, weight=BOLD).next_to(d, DOWN, buff=0.2)
            sb = Text(sub, font_size=16, color=GREY).next_to(lb, DOWN, buff=0.1)
            self.play(GrowFromCenter(d), Write(yr), Write(lb), Write(sb), run_time=0.7)

        self.wait(0.5)

        msg = Text("Од царови до претседатели — иста огромна земја.",
                   font_size=24, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(msg), run_time=1.1)
        self.wait(1.4)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        title6 = section_title("Што да запомниме", color=YELLOW)
        self.play(FadeIn(title6), run_time=0.6)

        bullets = VGroup(
            callout("17 мил. км² — најголема земја во светот", width=11, border=BLUE),
            callout("11 часовни зони — од Москва до Владивосток", width=11, border=ORANGE),
            callout("Урал — граница помеѓу Европа и Азија", width=11, border=GREEN),
            callout("Сибир — тундра, тајга, степи; до −60°C", width=11, border=PURPLE),
            callout("Богата со нафта, гас, дрво и метали", width=11, border=YELLOW),
        ).arrange(DOWN, buff=0.25).next_to(title6, DOWN, buff=0.4)

        for b in bullets:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.45)

        self.wait(0.6)

        final = Text("Русија. Огромна. Студена. Богата.",
                     font_size=34, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(final), run_time=1.2)
        self.wait(2.2)

        self.play(FadeOut(VGroup(title6, bullets, final)), run_time=0.8)
        self.wait(0.5)
