"""
bio8-2-2  —  Градба на коски
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
bone as living architecture, marrow as factory.
Render:  manim -ql bio8-2-2.py Bio822Scene
Output:  media/videos/bio8-2-2/480p15/Bio822Scene.mp4
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


def layer_label(name, value, color, pos):
    line = Line(LEFT * 0.3, RIGHT * 0.3, color=color, stroke_width=3).move_to(pos)
    nm = Text(name, font_size=18, color=WHITE2, weight=BOLD)
    val = Text(value, font_size=14, color=GREY)
    grp = VGroup(nm, val).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
    grp.next_to(line, RIGHT, buff=0.2)
    return VGroup(line, grp)


class Bio822Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Коската не е камен.", font_size=50, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.8)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.4)

        beats = VGroup(
            Text("Коската живее.", font_size=40, color=GREEN, weight=BOLD),
            Text("Се менува.", font_size=36, color=BLUE),
            Text("Се поправа.", font_size=36, color=ORANGE),
            Text("Низ цел живот.", font_size=36, color=WHITE2),
        ).arrange(DOWN, buff=0.35).next_to(h1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ПОПРЕЧЕН ПРЕСЕК                                  ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cross_section")
        title = section_title("Пресек на коска")
        self.play(Write(title), run_time=0.8)

        # Cross-section as nested ellipses (concentric layers)
        # Outer layer: periosteum
        periosteum = Ellipse(width=4.5, height=2.6, color=GREEN,
                             fill_opacity=0.6, stroke_color=GREEN, stroke_width=2)
        periosteum.shift(LEFT * 2.5)

        # Compact bone
        compact = Ellipse(width=4.3, height=2.4, color=WHITE2,
                          fill_opacity=0.7, stroke_color=WHITE2, stroke_width=1.5)
        compact.shift(LEFT * 2.5)

        # Spongy bone — porous look (smaller ellipse with cells)
        spongy = Ellipse(width=3.3, height=1.7, color=ORANGE,
                         fill_opacity=0.4, stroke_color=ORANGE, stroke_width=1.5)
        spongy.shift(LEFT * 2.5)

        # Pores in spongy
        pores = VGroup()
        np.random.seed(2)
        for _ in range(14):
            x = -2.5 + np.random.uniform(-1.3, 1.3)
            y = np.random.uniform(-0.6, 0.6)
            r = np.random.uniform(0.06, 0.13)
            p = Circle(radius=r, color="#0d1b2e", fill_opacity=1, stroke_width=0)
            p.move_to([x, y, 0])
            pores.add(p)

        # Marrow cavity (center)
        marrow = Ellipse(width=2.0, height=0.9, color=RED,
                         fill_opacity=0.7, stroke_color=RED, stroke_width=1.5)
        marrow.shift(LEFT * 2.5)

        self.play(GrowFromCenter(periosteum), run_time=0.8)
        self.wait(0.2)
        self.play(GrowFromCenter(compact), run_time=0.8)
        self.wait(0.2)
        self.play(GrowFromCenter(spongy), FadeIn(pores), run_time=0.9)
        self.wait(0.2)
        self.play(GrowFromCenter(marrow), run_time=0.7)
        self.wait(0.4)

        # Labels on the right side
        labels = VGroup(
            layer_label("Периост", "надворешна обвивка", GREEN, ORIGIN),
            layer_label("Компактна", "цврст надворешен дел", WHITE2, ORIGIN),
            layer_label("Сунѓераста", "лесна и порозна", ORANGE, ORIGIN),
            layer_label("Срцевина", "црвена и жолта", RED, ORIGIN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        labels.to_edge(RIGHT, buff=0.6).shift(UP * 0.2)

        for lbl in labels:
            self.play(FadeIn(lbl, shift=LEFT * 0.2), run_time=0.5)
            self.wait(0.15)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, periosteum, compact, spongy,
                                 pores, marrow, labels)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  СРЦЕВИНА — ЦРВЕНА vs ЖОЛТА                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("marrow")
        title = section_title("Коскена срцевина — две бои")
        self.play(Write(title), run_time=0.8)

        # Red marrow card
        red_card = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.3,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=RED, stroke_width=3)
        red_card.move_to(LEFT * 3.3)
        red_title = Text("Црвена срцевина", font_size=28, color=RED, weight=BOLD)
        red_title.move_to(red_card.get_top() + DOWN * 0.4)
        red_desc = VGroup(
            Text("• Прави крвни клетки", font_size=20, color=WHITE2),
            Text("• Црвени крвни зрнца", font_size=18, color=GREY),
            Text("• Бели крвни зрнца", font_size=18, color=GREY),
            Text("• Тромбоцити", font_size=18, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        red_desc.next_to(red_title, DOWN, buff=0.4)

        # Yellow marrow card
        yel_card = RoundedRectangle(width=5.5, height=3.5, corner_radius=0.3,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=YELLOW, stroke_width=3)
        yel_card.move_to(RIGHT * 3.3)
        yel_title = Text("Жолта срцевина", font_size=28, color=YELLOW, weight=BOLD)
        yel_title.move_to(yel_card.get_top() + DOWN * 0.4)
        yel_desc = VGroup(
            Text("• Чува масти", font_size=20, color=WHITE2),
            Text("• Резерва на енергија", font_size=18, color=GREY),
            Text("• Во подолгите коски", font_size=18, color=GREY),
            Text("• Се претвора во црвена", font_size=18, color=GREY),
            Text("  кога е потребно", font_size=18, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        yel_desc.next_to(yel_title, DOWN, buff=0.4)

        self.play(FadeIn(red_card), FadeIn(yel_card), run_time=0.7)
        self.play(Write(red_title), Write(yel_title), run_time=0.8)
        self.wait(0.3)
        for r, y in zip(red_desc, yel_desc):
            self.play(FadeIn(r, shift=RIGHT * 0.15),
                      FadeIn(y, shift=LEFT * 0.15), run_time=0.4)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, red_card, yel_card, red_title,
                                 yel_title, red_desc, yel_desc)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  МИНЕРАЛИ                                        ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("minerals")
        title = section_title("Минерали — за цврстина")
        self.play(Write(title), run_time=0.8)

        # Calcium card
        ca = RoundedRectangle(width=4.5, height=2.8, corner_radius=0.3,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=BLUE, stroke_width=3)
        ca.move_to(LEFT * 2.8 + UP * 0.2)
        ca_sym = Text("Ca", font_size=56, color=BLUE, weight=BOLD)
        ca_sym.move_to(ca.get_center() + UP * 0.4)
        ca_name = Text("Калциум", font_size=24, color=WHITE2)
        ca_name.move_to(ca.get_center() + DOWN * 0.3)
        ca_pct = Text("~65% од минералите", font_size=16, color=GREY)
        ca_pct.move_to(ca.get_center() + DOWN * 0.75)

        # Phosphorus card
        ph = RoundedRectangle(width=4.5, height=2.8, corner_radius=0.3,
                              fill_color=DARK_CARD, fill_opacity=1,
                              stroke_color=ORANGE, stroke_width=3)
        ph.move_to(RIGHT * 2.8 + UP * 0.2)
        ph_sym = Text("P", font_size=56, color=ORANGE, weight=BOLD)
        ph_sym.move_to(ph.get_center() + UP * 0.4)
        ph_name = Text("Фосфор", font_size=24, color=WHITE2)
        ph_name.move_to(ph.get_center() + DOWN * 0.3)
        ph_pct = Text("~25% од минералите", font_size=16, color=GREY)
        ph_pct.move_to(ph.get_center() + DOWN * 0.75)

        self.play(FadeIn(ca, shift=UP * 0.2), FadeIn(ph, shift=UP * 0.2), run_time=0.7)
        self.play(Write(ca_sym), Write(ph_sym), run_time=0.8)
        self.play(FadeIn(ca_name), FadeIn(ph_name), run_time=0.5)
        self.play(FadeIn(ca_pct), FadeIn(ph_pct), run_time=0.5)
        self.wait(0.6)

        punch = callout("Калциум + фосфор = цврстина",
                        width=8.5, bg="#1a3552", border=YELLOW, font_size=30)
        punch.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(punch, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, ca, ph, ca_sym, ph_sym, ca_name,
                                 ph_name, ca_pct, ph_pct, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  РЕМОДЕЛИРАЊЕ                                    ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("remodeling")
        title = section_title("Обновување на коската")
        self.play(Write(title), run_time=0.8)

        # Two characters: builder vs destroyer
        # Osteoblast (builder)
        ob_circle = Circle(radius=0.6, color=GREEN, fill_opacity=0.7, stroke_width=2)
        ob_circle.move_to(LEFT * 4.0 + UP * 1.0)
        ob_label = Text("Остеобласт", font_size=22, color=GREEN, weight=BOLD)
        ob_label.next_to(ob_circle, DOWN, buff=0.2)
        ob_role = Text("гради нова коска", font_size=18, color=WHITE2)
        ob_role.next_to(ob_label, DOWN, buff=0.15)

        # Osteoclast (destroyer)
        oc_circle = Circle(radius=0.6, color=RED, fill_opacity=0.7, stroke_width=2)
        oc_circle.move_to(RIGHT * 4.0 + UP * 1.0)
        oc_label = Text("Остеокласт", font_size=22, color=RED, weight=BOLD)
        oc_label.next_to(oc_circle, DOWN, buff=0.2)
        oc_role = Text("ја разградува старата", font_size=18, color=WHITE2)
        oc_role.next_to(oc_label, DOWN, buff=0.15)

        # Bone block in middle
        bone_block = RoundedRectangle(width=2.5, height=0.7, corner_radius=0.15,
                                      fill_color=WHITE2, fill_opacity=0.3,
                                      stroke_color=WHITE2, stroke_width=2)
        bone_block.move_to(UP * 1.0)

        self.play(FadeIn(ob_circle), FadeIn(oc_circle), run_time=0.6)
        self.play(Write(ob_label), Write(oc_label), run_time=0.7)
        self.play(FadeIn(ob_role), FadeIn(oc_role), run_time=0.5)
        self.play(FadeIn(bone_block), run_time=0.5)
        self.wait(0.4)

        # Arrows + animation
        arr_build = Arrow(ob_circle.get_right(), bone_block.get_left(),
                          color=GREEN, buff=0.15, stroke_width=4)
        arr_destroy = Arrow(oc_circle.get_left(), bone_block.get_right(),
                            color=RED, buff=0.15, stroke_width=4)
        self.play(GrowArrow(arr_build), GrowArrow(arr_destroy), run_time=0.8)
        self.wait(0.6)

        balance = Text("Рамнотежа — секој ден",
                       font_size=30, color=YELLOW, weight=BOLD)
        balance.move_to(DOWN * 0.7)
        self.play(Write(balance), run_time=0.9)
        self.wait(0.4)

        # Renewal time
        time_text = VGroup(
            Text("Целиот скелет се обновува", font_size=24, color=WHITE2),
            Text("на секои 10 години.", font_size=28, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(time_text, shift=UP * 0.2), run_time=1.0)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, ob_circle, oc_circle, ob_label, oc_label,
                                 ob_role, oc_role, bone_block, arr_build,
                                 arr_destroy, balance, time_text)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ЗДРАВА КОСКА                                    ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("healthy")
        title = section_title("Здрава коска — три услови")
        self.play(Write(title), run_time=0.8)

        tips = VGroup(
            callout("Калциум — млеко, сирење, зелка",
                    width=10.0, bg="#1a3552", border=BLUE, font_size=26),
            callout("Витамин Д — сонце, риба",
                    width=10.0, bg="#1a3552", border=YELLOW, font_size=26),
            callout("Движење — коската јакне со напор",
                    width=10.0, bg="#1a3552", border=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for t in tips:
            self.play(FadeIn(t, shift=UP * 0.2), run_time=0.7)
            self.wait(0.3)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, tips)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Коската не спие.", font_size=42, color=BLUE, weight=BOLD),
            Text("Коската работи.", font_size=42, color=GREEN, weight=BOLD),
            Text("Коската живее.", font_size=46, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
