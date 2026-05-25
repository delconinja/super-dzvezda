"""
bio8-2-4  —  Мускули и нивна градба
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
muscles as three characters with different jobs.
Render:  manim -ql bio8-2-4.py Bio824Scene
Output:  media/videos/bio8-2-4/480p15/Bio824Scene.mp4
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


def muscle_type_card(name, control, location, color, pos):
    box = RoundedRectangle(width=3.6, height=3.0, corner_radius=0.25,
                           fill_color=DARK_CARD, fill_opacity=1,
                           stroke_color=color, stroke_width=3)
    box.move_to(pos)
    nm = Text(name, font_size=24, color=color, weight=BOLD)
    nm.move_to(box.get_top() + DOWN * 0.4)
    line = Line(LEFT * 1.3, RIGHT * 1.3, color=color, stroke_width=1)
    line.move_to(box.get_top() + DOWN * 0.8)
    return VGroup(box, nm, line)


class Bio824Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Скелетните ги командуваш.",
                  font_size=38, color=BLUE, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        h2 = Text("Срцето куца самиот.",
                  font_size=38, color=RED, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.4)
        self.play(Write(h2), run_time=1.2)
        self.wait(0.3)

        h3 = Text("Глатките молчат.",
                  font_size=38, color=PURPLE, weight=BOLD)
        h3.next_to(h2, DOWN, buff=0.4)
        self.play(Write(h3), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Три различни.", font_size=34, color=WHITE2),
            Text("Сите неопходни.", font_size=36, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(h3, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, h2, h3, beats)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ТРИ ВИДОВИ МУСКУЛИ                              ~75 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_types")
        title = section_title("Три видови мускулно ткиво")
        self.play(Write(title), run_time=0.8)

        # Skeletal card
        sk = muscle_type_card("Скелетни", "доброволни", "коски",
                              BLUE, LEFT * 4.5 + DOWN * 0.3)
        # Skeletal tissue — long striated fibers
        sk_fibers = VGroup()
        for i in range(4):
            y = DOWN * 0.3 + UP * (0.3 - i * 0.18)
            f = Line(LEFT * 5.7 + y, LEFT * 3.3 + y, color=BLUE, stroke_width=4)
            sk_fibers.add(f)
            # striations
            for j in range(6):
                x_off = -5.5 + j * 0.4
                st = Line([x_off, y[1] - 0.06, 0], [x_off, y[1] + 0.06, 0],
                          color=WHITE2, stroke_width=1)
                sk_fibers.add(st)

        sk_desc = VGroup(
            Text("Доброволни", font_size=18, color=GREEN, weight=BOLD),
            Text("Ивичести (пругасти)", font_size=14, color=WHITE2),
            Text("Прикачени за коски", font_size=14, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        sk_desc.move_to(LEFT * 4.5 + DOWN * 1.5)

        # Smooth card
        sm = muscle_type_card("Глатки", "недоброволни", "органи",
                              PURPLE, UP * 0.0 + DOWN * 0.3)
        # Smooth tissue — spindle cells
        sm_cells = VGroup()
        np.random.seed(3)
        for i in range(5):
            for j in range(3):
                x = -1.1 + i * 0.55
                y = -0.1 + j * 0.22 - 0.2
                ell = Ellipse(width=0.45, height=0.15, color=PURPLE,
                              fill_opacity=0.6, stroke_color=PURPLE, stroke_width=1)
                ell.move_to([x, y, 0])
                sm_cells.add(ell)

        sm_desc = VGroup(
            Text("Недоброволни", font_size=18, color=ORANGE, weight=BOLD),
            Text("Без пруги", font_size=14, color=WHITE2),
            Text("Желудник, црева, крвни садови", font_size=12, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        sm_desc.move_to(DOWN * 1.5)

        # Cardiac card
        cd = muscle_type_card("Срцеви", "недоброволни", "само срце",
                              RED, RIGHT * 4.5 + DOWN * 0.3)
        # Cardiac tissue — branched striated cells
        cd_cells = VGroup()
        # Main branches
        for i in range(3):
            y = 0.0 - i * 0.25
            mn = Line(RIGHT * 3.3 + UP * y, RIGHT * 5.7 + UP * y,
                      color=RED, stroke_width=4)
            cd_cells.add(mn)
            # Y-branches
            br = Line(RIGHT * (4.0 + 0.4 * i) + UP * y, RIGHT * (4.0 + 0.4 * i) + UP * (y - 0.2),
                      color=RED, stroke_width=4)
            cd_cells.add(br)

        cd_desc = VGroup(
            Text("Недоброволни", font_size=18, color=ORANGE, weight=BOLD),
            Text("Ивичести и разгранети", font_size=14, color=WHITE2),
            Text("Само во срцето", font_size=14, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        cd_desc.move_to(RIGHT * 4.5 + DOWN * 1.5)

        # Animate cards
        for card, fibers, desc in [(sk, sk_fibers, sk_desc),
                                   (sm, sm_cells, sm_desc),
                                   (cd, cd_cells, cd_desc)]:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.6)
            self.play(Create(fibers), run_time=0.7)
            self.play(FadeIn(desc), run_time=0.5)
            self.wait(0.2)

        self.wait(1.8)
        self.play(FadeOut(VGroup(title, sk, sm, cd, sk_fibers, sm_cells,
                                 cd_cells, sk_desc, sm_desc, cd_desc)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  640 МУСКУЛИ                                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("count")
        title = section_title("Колку мускули имаме?")
        self.play(Write(title), run_time=0.8)

        big = Text("~640", font_size=140, color=YELLOW, weight=BOLD)
        big.move_to(UP * 0.5)
        self.play(Write(big), run_time=1.2)

        sub = Text("мускули во човечкото тело",
                   font_size=32, color=WHITE2)
        sub.next_to(big, DOWN, buff=0.4)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)

        pct = VGroup(
            Text("Околу 40% од телесната маса.", font_size=26, color=ORANGE),
            Text("Кај машките — повеќе. Кај женските — помалку.",
                 font_size=22, color=GREY),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.7)

        for line in pct:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, big, sub, pct)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ГРАДБА НА МУСКУЛ                                ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("structure")
        title = section_title("Од мускул до влакно")
        self.play(Write(title), run_time=0.8)

        # Whole muscle (oval, large)
        whole = Ellipse(width=4.0, height=1.0, color=RED,
                        fill_opacity=0.5, stroke_color=RED, stroke_width=2)
        whole.move_to(UP * 2.0 + LEFT * 4.0)
        whole_lbl = Text("Мускул", font_size=18, color=WHITE2)
        whole_lbl.next_to(whole, DOWN, buff=0.15)

        # Bundles (3 lines inside)
        bundles = VGroup()
        for i in range(3):
            b = Ellipse(width=3.5, height=0.18, color=ORANGE,
                        fill_opacity=0.7, stroke_color=ORANGE, stroke_width=1)
            b.move_to(UP * (2.0 + 0.25 - i * 0.25) + LEFT * 0.5)
            bundles.add(b)
        bundles_lbl = Text("Снопови", font_size=18, color=WHITE2)
        bundles_lbl.next_to(bundles, DOWN, buff=0.15)

        # Single fiber (zoom in)
        fiber = Rectangle(width=4.0, height=0.6, color=BLUE,
                         fill_opacity=0.5, stroke_color=BLUE, stroke_width=2)
        fiber.move_to(DOWN * 0.5 + LEFT * 4.0)
        # Striations
        striations = VGroup()
        for j in range(10):
            x = -5.8 + j * 0.4
            st = Line([x, -0.8, 0], [x, -0.2, 0], color=WHITE2, stroke_width=1.5)
            striations.add(st)
        fiber_lbl = Text("Влакно", font_size=18, color=WHITE2)
        fiber_lbl.next_to(fiber, DOWN, buff=0.15)

        # Myofibril — actin + myosin
        myof_lbl = Text("Саркомера — актин + миозин",
                        font_size=20, color=YELLOW, weight=BOLD)
        myof_lbl.move_to(DOWN * 1.7 + RIGHT * 1.0)

        # Sarcomere zoom
        sarc_box = Rectangle(width=4.5, height=1.6, color=WHITE2,
                             fill_opacity=0.1, stroke_color=WHITE2, stroke_width=1)
        sarc_box.move_to(DOWN * 2.5 + RIGHT * 1.0)

        # Z-lines
        z1 = Line(DOWN * 1.8 + RIGHT * (1.0 - 2.0), DOWN * 3.2 + RIGHT * (1.0 - 2.0),
                  color=WHITE2, stroke_width=3)
        z2 = Line(DOWN * 1.8 + RIGHT * (1.0 + 2.0), DOWN * 3.2 + RIGHT * (1.0 + 2.0),
                  color=WHITE2, stroke_width=3)

        # Actin (thin filaments)
        actin_l = Line(DOWN * 2.5 + RIGHT * (1.0 - 1.8), DOWN * 2.5 + RIGHT * (1.0 - 0.4),
                       color=GREEN, stroke_width=5)
        actin_r = Line(DOWN * 2.5 + RIGHT * (1.0 + 0.4), DOWN * 2.5 + RIGHT * (1.0 + 1.8),
                       color=GREEN, stroke_width=5)

        # Myosin (thick filament with heads)
        myosin = Line(DOWN * 2.5 + RIGHT * (1.0 - 1.0), DOWN * 2.5 + RIGHT * (1.0 + 1.0),
                      color=ORANGE, stroke_width=10)

        self.play(GrowFromCenter(whole), Write(whole_lbl), run_time=0.7)
        self.wait(0.2)
        self.play(Create(bundles), Write(bundles_lbl), run_time=0.7)
        self.wait(0.2)
        self.play(Create(fiber), Create(striations), Write(fiber_lbl), run_time=0.8)
        self.wait(0.3)
        self.play(Create(sarc_box), Write(myof_lbl), run_time=0.6)
        self.play(Create(z1), Create(z2), run_time=0.5)
        self.play(Create(actin_l), Create(actin_r), Create(myosin), run_time=0.7)
        self.wait(0.5)

        # Labels for actin / myosin
        act_lbl = Text("актин", font_size=16, color=GREEN)
        act_lbl.next_to(actin_r, UP, buff=0.1)
        myo_lbl = Text("миозин", font_size=16, color=ORANGE)
        myo_lbl.next_to(myosin, DOWN, buff=0.1)
        self.play(FadeIn(act_lbl), FadeIn(myo_lbl), run_time=0.5)

        self.wait(2.0)
        self.play(FadeOut(VGroup(title, whole, whole_lbl, bundles, bundles_lbl,
                                 fiber, fiber_lbl, striations, sarc_box,
                                 z1, z2, actin_l, actin_r, myosin, myof_lbl,
                                 act_lbl, myo_lbl)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  КАКО СЕ СВИВА                                   ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("contraction")
        title = section_title("Како се свива мускулот")
        self.play(Write(title), run_time=0.8)

        # Sarcomere relaxed
        relax_lbl = Text("Опуштена саркомера", font_size=22, color=BLUE, weight=BOLD)
        relax_lbl.move_to(UP * 2.2)

        # Z-lines (far apart)
        z1_r = Line(UP * 1.0, UP * 0.0, color=WHITE2, stroke_width=3)
        z1_r.shift(LEFT * 2.5)
        z2_r = Line(UP * 1.0, UP * 0.0, color=WHITE2, stroke_width=3)
        z2_r.shift(RIGHT * 2.5)

        # Actin from left + right
        act_l_r = Line(LEFT * 2.5 + UP * 0.5, LEFT * 0.7 + UP * 0.5,
                       color=GREEN, stroke_width=6)
        act_r_r = Line(RIGHT * 0.7 + UP * 0.5, RIGHT * 2.5 + UP * 0.5,
                       color=GREEN, stroke_width=6)
        # Myosin
        myo_r = Line(LEFT * 1.2 + UP * 0.5, RIGHT * 1.2 + UP * 0.5,
                     color=ORANGE, stroke_width=12)

        self.play(Write(relax_lbl), run_time=0.6)
        self.play(Create(z1_r), Create(z2_r), run_time=0.5)
        self.play(Create(act_l_r), Create(act_r_r), Create(myo_r), run_time=0.7)
        self.wait(0.6)

        # Transition arrow
        arr = Arrow(UP * 0.0, DOWN * 0.6, color=YELLOW, stroke_width=4)
        arr_lbl = Text("свивање", font_size=18, color=YELLOW)
        arr_lbl.next_to(arr, RIGHT, buff=0.15)
        self.play(GrowArrow(arr), Write(arr_lbl), run_time=0.7)

        # Contracted version (Z-lines closer, actin slides over myosin)
        cont_lbl = Text("Свиена саркомера", font_size=22, color=GREEN, weight=BOLD)
        cont_lbl.move_to(DOWN * 1.1)

        z1_c = Line(DOWN * 1.7, DOWN * 2.7, color=WHITE2, stroke_width=3)
        z1_c.shift(LEFT * 1.6)
        z2_c = Line(DOWN * 1.7, DOWN * 2.7, color=WHITE2, stroke_width=3)
        z2_c.shift(RIGHT * 1.6)

        act_l_c = Line(LEFT * 1.6 + DOWN * 2.2, RIGHT * 0.4 + DOWN * 2.2,
                       color=GREEN, stroke_width=6)
        act_r_c = Line(LEFT * 0.4 + DOWN * 2.2, RIGHT * 1.6 + DOWN * 2.2,
                       color=GREEN, stroke_width=6)
        myo_c = Line(LEFT * 1.2 + DOWN * 2.2, RIGHT * 1.2 + DOWN * 2.2,
                     color=ORANGE, stroke_width=12)

        self.play(Write(cont_lbl), run_time=0.6)
        self.play(Create(z1_c), Create(z2_c), Create(act_l_c), Create(act_r_c),
                  Create(myo_c), run_time=1.0)
        self.wait(0.6)

        punch = Text("Актин се лизга врз миозин.",
                     font_size=24, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.4)
        self.play(Write(punch), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, relax_lbl, z1_r, z2_r, act_l_r, act_r_r,
                                 myo_r, arr, arr_lbl, cont_lbl, z1_c, z2_c,
                                 act_l_c, act_r_c, myo_c, punch)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ИНТЕРЕСНО                                       ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("trivia")
        title = section_title("Интересно за мускулите")
        self.play(Write(title), run_time=0.8)

        facts = VGroup(
            callout("Најголем — глутеус максимус (задник)",
                    width=10.5, bg="#1a3552", border=BLUE, font_size=24),
            callout("Најмал — стапалце во увото (1 мм)",
                    width=10.5, bg="#1a3552", border=GREEN, font_size=24),
            callout("Најсилен — масетер (за џвакање)",
                    width=10.5, bg="#1a3552", border=ORANGE, font_size=24),
            callout("Најактивен — срцето (3 милијарди удари)",
                    width=10.5, bg="#1a3552", border=RED, font_size=24),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        for f in facts:
            self.play(FadeIn(f, shift=UP * 0.15), run_time=0.55)
            self.wait(0.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, facts)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Скелетни — за движење.", font_size=36, color=BLUE, weight=BOLD),
            Text("Глатки — за органи.", font_size=36, color=PURPLE, weight=BOLD),
            Text("Срцеви — за пумпање.", font_size=36, color=RED, weight=BOLD),
            Text("Триецот работи. Заедно.", font_size=42, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
