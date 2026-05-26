"""
chem8-3-3  —  Што е соединение?
Хемија 8, Единица 3: Хемиски елементи и соединенија

Teaching narrative — continuous storytelling.
Render:  manim -ql chem8-3-3.py Chem833Scene
Output:  media/videos/chem8-3-3/480p15/Chem833Scene.mp4
"""
from manim import *
import numpy as np

config.background_color = "#0d1b2e"

BLUE      = "#4fc3f7"
YELLOW    = "#ffd54f"
GREEN     = "#81c784"
RED       = "#e57373"
GREY      = "#90a4ae"
ORANGE    = "#ffb74d"
PURPLE    = "#ce93d8"
WHITE2    = "#e8eaf0"
DARK_CARD = "#0f2233"


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


def atom_ball(symbol, color, r=0.55, font_size=26):
    c = Circle(radius=r, fill_color=color, fill_opacity=0.85,
               stroke_color=WHITE2, stroke_width=2)
    s = Text(symbol, font_size=font_size, color=WHITE2, weight=BOLD).move_to(c)
    return VGroup(c, s)


class Chem833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # § 1 HOOK — Неочекувана трансформација                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        l1 = Text("Замисли две опасни супстанции.",
                  font_size=36, color=WHITE2)
        self.play(Write(l1), run_time=1.6)
        self.wait(0.8)
        self.play(l1.animate.to_edge(UP, buff=0.6).scale(0.7), run_time=0.7)

        na = atom_ball("Na", PURPLE, r=0.55, font_size=26)
        na.move_to(LEFT * 3.5 + UP * 0.4)
        na_n1 = Text("Едната — натриум.", font_size=28, color=PURPLE, weight=BOLD)
        na_n1.next_to(na, DOWN, buff=0.35)
        na_n2 = Text("Мек метал што реагира бурно со вода.",
                     font_size=20, color=WHITE2)
        na_n2.next_to(na_n1, DOWN, buff=0.2)

        self.play(FadeIn(na, shift=UP * 0.2), run_time=0.7)
        self.play(Write(na_n1), run_time=0.9)
        self.play(Write(na_n2), run_time=1.0)
        self.wait(0.8)

        cl = atom_ball("Cl", GREEN, r=0.55, font_size=26)
        cl.move_to(RIGHT * 3.5 + UP * 0.4)
        cl_n1 = Text("Другата — хлор.", font_size=28, color=GREEN, weight=BOLD)
        cl_n1.next_to(cl, DOWN, buff=0.35)
        cl_n2 = Text("Отровен зелен гас.", font_size=20, color=WHITE2)
        cl_n2.next_to(cl_n1, DOWN, buff=0.2)

        self.play(FadeIn(cl, shift=UP * 0.2), run_time=0.7)
        self.play(Write(cl_n1), run_time=0.9)
        self.play(Write(cl_n2), run_time=0.9)
        self.wait(1.0)

        bridge = Text("Одделно — опасни.",
                      font_size=28, color=RED, weight=BOLD)
        bridge.to_edge(DOWN, buff=1.4)
        self.play(Write(bridge), run_time=1.0)
        self.wait(1.4)

        bridge2 = Text("Но кога ќе се соединат...",
                       font_size=28, color=YELLOW)
        bridge2.next_to(bridge, DOWN, buff=0.2)
        self.play(Write(bridge2), run_time=1.0)
        self.wait(1.0)

        self.play(FadeOut(VGroup(l1, na, na_n1, na_n2, cl, cl_n1, cl_n2,
                                 bridge, bridge2)), run_time=0.6)

        reveal1 = Text("се создава нешто сосема ново.",
                       font_size=32, color=WHITE2)
        reveal1.move_to(UP * 1.2)
        self.play(Write(reveal1), run_time=1.4)
        self.wait(0.7)

        reveal2 = Text("Обична кујнска сол.",
                       font_size=54, color=YELLOW, weight=BOLD)
        reveal2.move_to(ORIGIN)
        self.play(Write(reveal2), run_time=1.2)
        self.wait(0.5)

        reveal3 = Text("Супстанција што ја користиме секој ден.",
                       font_size=26, color=WHITE2)
        reveal3.next_to(reveal2, DOWN, buff=0.5)
        self.play(Write(reveal3), run_time=1.3)
        self.wait(1.4)

        power1 = Text("Тоа е моќта на хемијата.",
                      font_size=30, color=ORANGE, weight=BOLD)
        power1.to_edge(DOWN, buff=1.2)
        self.play(Write(power1), run_time=1.2)
        self.wait(0.7)

        power2 = Text("Не магија. Туку атоми што се поврзуваат.",
                      font_size=24, color=GREY)
        power2.next_to(power1, DOWN, buff=0.25)
        self.play(Write(power2), run_time=1.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(reveal1, reveal2, reveal3, power1, power2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 2 ШТО Е СОЕДИНЕНИЕ?                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што точно е соединение?")
        self.play(Write(t2), run_time=1.0)
        self.wait(0.6)

        intro = Text("Соединение е супстанција создадена кога:",
                     font_size=28, color=WHITE2)
        intro.next_to(t2, DOWN, buff=0.6)
        self.play(Write(intro), run_time=1.4)
        self.wait(0.4)

        b1 = Text("•  два или повеќе различни елементи",
                  font_size=26, color=BLUE)
        b2 = Text("•  хемиски се поврзуваат",
                  font_size=26, color=GREEN)
        b3 = Text("•  во точен сооднос",
                  font_size=26, color=YELLOW, weight=BOLD)
        bullets = VGroup(b1, b2, b3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        bullets.next_to(intro, DOWN, buff=0.45)
        for b in (b1, b2, b3):
            self.play(Write(b), run_time=0.9)
            self.wait(0.3)
        self.wait(0.8)

        example_lbl = Text("На пример:", font_size=24, color=GREY)
        example_lbl.next_to(bullets, DOWN, buff=0.55)
        self.play(Write(example_lbl), run_time=0.8)

        formula = MathTex(r"H_2 O", font_size=70, color=WHITE2)
        formula.next_to(example_lbl, DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.2)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, intro, bullets, example_lbl)),
                  formula.animate.move_to(UP * 2.2).scale(0.7),
                  run_time=0.8)

        ex1 = Text("Во една молекула вода секогаш има:",
                   font_size=26, color=WHITE2)
        ex1.move_to(UP * 1.0)
        self.play(Write(ex1), run_time=1.4)
        self.wait(0.3)

        cnt1 = Text("2 атоми водород",
                    font_size=28, color=BLUE, weight=BOLD)
        cnt2 = Text("1 атом кислород",
                    font_size=28, color=RED, weight=BOLD)
        cnts = VGroup(cnt1, cnt2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        cnts.next_to(ex1, DOWN, buff=0.4)
        self.play(Write(cnt1), run_time=0.9)
        self.play(Write(cnt2), run_time=0.9)
        self.wait(0.9)

        neg1 = Text("Не 3 и 1.",
                    font_size=28, color=GREY)
        neg2 = Text("Не 1 и 1.",
                    font_size=28, color=GREY)
        pos = Text("Туку секогаш ист сооднос.",
                   font_size=30, color=YELLOW, weight=BOLD)
        negs = VGroup(neg1, neg2, pos).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        negs.next_to(cnts, DOWN, buff=0.5)
        self.play(Write(neg1), run_time=0.8)
        self.play(Write(neg2), run_time=0.8)
        self.play(Write(pos), run_time=1.0)
        self.wait(1.2)

        closing2 = Text("Токму тоа ги прави соединенијата посебни.",
                        font_size=26, color=ORANGE)
        closing2.to_edge(DOWN, buff=0.6)
        self.play(Write(closing2), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(formula, ex1, cnts, negs, closing2)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 3 ДРАМА ВО ТРИ ЧИНА — Na + Cl                      ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("drama")

        # Act 1 — Sodium
        act1 = section_title("Чин 1 — Натриум", color=PURPLE)
        self.play(Write(act1), run_time=0.9)

        na = atom_ball("Na", PURPLE, r=0.85, font_size=36)
        na.move_to(ORIGIN + UP * 0.3)
        self.play(FadeIn(na, scale=0.7), run_time=0.8)

        na_line1 = Text("Натриумот е мек метал.",
                        font_size=28, color=WHITE2)
        na_line1.next_to(na, DOWN, buff=0.5)
        self.play(Write(na_line1), run_time=1.2)
        self.wait(0.7)

        na_line2 = Text("Но не дозволувај изгледот да те измами.",
                        font_size=24, color=GREY)
        na_line2.next_to(na_line1, DOWN, buff=0.25)
        self.play(Write(na_line2), run_time=1.5)
        self.wait(0.7)

        na_line3 = Text("Кога ќе допре вода...",
                        font_size=24, color=WHITE2)
        na_line3.next_to(na_line2, DOWN, buff=0.25)
        self.play(Write(na_line3), run_time=1.1)
        self.wait(0.4)

        na_line4 = Text("реагира експлозивно.",
                        font_size=30, color=RED, weight=BOLD)
        na_line4.next_to(na_line3, DOWN, buff=0.25)
        self.play(Write(na_line4), run_time=1.2)
        self.wait(1.4)

        self.play(FadeOut(VGroup(act1, na, na_line1, na_line2, na_line3, na_line4)),
                  run_time=0.6)

        # Act 2 — Chlorine
        act2 = section_title("Чин 2 — Хлор", color=GREEN)
        self.play(Write(act2), run_time=0.9)

        cl = atom_ball("Cl", GREEN, r=0.85, font_size=36)
        cl.move_to(ORIGIN + UP * 0.3)
        self.play(FadeIn(cl, scale=0.7), run_time=0.8)

        cl_line1 = Text("Хлорот е зеленкаст гас.",
                        font_size=28, color=WHITE2)
        cl_line1.next_to(cl, DOWN, buff=0.5)
        self.play(Write(cl_line1), run_time=1.3)
        self.wait(0.6)

        cl_line2 = Text("Со силна миризба.",
                        font_size=24, color=WHITE2)
        cl_line2.next_to(cl_line1, DOWN, buff=0.25)
        self.play(Write(cl_line2), run_time=1.1)
        self.wait(0.4)

        cl_line3 = Text("И многу опасен за дишење.",
                        font_size=26, color=RED, weight=BOLD)
        cl_line3.next_to(cl_line2, DOWN, buff=0.25)
        self.play(Write(cl_line3), run_time=1.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(act2, cl, cl_line1, cl_line2, cl_line3)),
                  run_time=0.6)

        # Act 3 — Transformation
        act3 = section_title("Чин 3 — Трансформација", color=YELLOW)
        self.play(Write(act3), run_time=0.9)

        na2 = atom_ball("Na", PURPLE, r=0.7, font_size=30).move_to(LEFT * 2.5 + UP * 0.2)
        cl2 = atom_ball("Cl", GREEN, r=0.7, font_size=30).move_to(RIGHT * 2.5 + UP * 0.2)
        self.play(FadeIn(na2, shift=RIGHT * 0.5),
                  FadeIn(cl2, shift=LEFT * 0.5), run_time=1.0)
        self.wait(0.5)

        link_line1 = Text("Кога атомот на натриум",
                          font_size=24, color=PURPLE)
        link_line2 = Text("и атомот на хлор",
                          font_size=24, color=GREEN)
        link_line3 = Text("ќе се поврзат...",
                          font_size=24, color=WHITE2)
        links = VGroup(link_line1, link_line2, link_line3).arrange(DOWN, buff=0.2)
        links.next_to(na2, DOWN, buff=0.8).set_x(0)
        for l in (link_line1, link_line2, link_line3):
            self.play(Write(l), run_time=0.8)
        self.wait(0.5)

        spark = Text("⚡", font_size=72, color=YELLOW).move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(spark, scale=1.6), run_time=0.4)
        self.play(na2.animate.move_to(ORIGIN + UP * 0.2 + LEFT * 0.6),
                  cl2.animate.move_to(ORIGIN + UP * 0.2 + RIGHT * 0.6),
                  FadeOut(spark), FadeOut(links), run_time=1.0)

        bond = Line(na2.get_right(), cl2.get_left(),
                    stroke_color=WHITE2, stroke_width=4)
        self.play(Create(bond), run_time=0.5)

        formed = MathTex("NaCl", font_size=48, color=YELLOW)
        formed.next_to(na2, DOWN, buff=0.7).set_x(0)
        formed_name = Text("натриум-хлорид", font_size=24, color=WHITE2)
        formed_name.next_to(formed, DOWN, buff=0.2)
        self.play(Write(formed), run_time=0.9)
        self.play(Write(formed_name), run_time=0.9)
        self.wait(0.4)

        salt = Text("Трпезна сол.",
                    font_size=32, color=YELLOW, weight=BOLD)
        salt.next_to(formed_name, DOWN, buff=0.4)
        self.play(Write(salt), run_time=1.0)
        self.wait(0.4)

        new_lbl = Text("Нова супстанција со сосема нови својства.",
                       font_size=24, color=GREEN)
        new_lbl.to_edge(DOWN, buff=0.6)
        self.play(Write(new_lbl), run_time=1.5)
        self.wait(1.6)

        self.play(FadeOut(VGroup(act3, na2, cl2, bond, formed, formed_name,
                                 salt, new_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 4 НОВИ СВОЈСТВА                                    ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("new_props")

        t4 = section_title("Нови својства")
        self.play(Write(t4), run_time=0.9)

        intro1 = Text("Кога се создава соединение,",
                      font_size=26, color=WHITE2)
        intro2 = Text("елементите не ги задржуваат старите својства.",
                      font_size=26, color=WHITE2)
        intro3 = Text("Тие создаваат нови.",
                      font_size=28, color=YELLOW, weight=BOLD)
        intro_grp = VGroup(intro1, intro2, intro3).arrange(DOWN, buff=0.2)
        intro_grp.next_to(t4, DOWN, buff=0.5)
        for l in (intro1, intro2, intro3):
            self.play(Write(l), run_time=1.0)
        self.wait(0.6)

        self.play(FadeOut(intro_grp), run_time=0.5)

        def col(symbol, color, lines, x):
            box = RoundedRectangle(
                width=3.8, height=4.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=2.5,
            ).shift(x + DOWN * 0.1)
            s = Text(symbol, font_size=44, color=color, weight=BOLD)
            s.move_to(box.get_top() + DOWN * 0.55)
            txts = VGroup(*[Text(l, font_size=19, color=WHITE2)
                            for l in lines]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            txts.move_to(box.get_center() + DOWN * 0.3)
            return VGroup(box, s, txts)

        c1 = col("Натриум", PURPLE,
                 ["мек метал", "реагира бурно", "експлозивен со вода"],
                 LEFT * 4.5)
        c2 = col("Хлор", GREEN,
                 ["зелен гас", "отровен", "силна миризба"],
                 ORIGIN)
        c3 = col("Натриум-хлорид", YELLOW,
                 ["бел кристал", "безбеден", "растворлив во вода"],
                 RIGHT * 4.5)

        self.play(FadeIn(c1, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(c2, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(c3, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        msg1 = Text("Соединението не е само мешавина.",
                    font_size=24, color=WHITE2)
        msg2 = Text("Тоа е нешто ново.",
                    font_size=28, color=ORANGE, weight=BOLD)
        msgs = VGroup(msg1, msg2).arrange(DOWN, buff=0.2)
        msgs.to_edge(DOWN, buff=0.4)
        self.play(Write(msg1), run_time=1.2)
        self.play(Write(msg2), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, c1, c2, c3, msgs)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 5 СОЕДИНЕНИЈА НАСЕКАДЕ ОКОЛУ ТЕБЕ                  ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("examples")

        t5 = Text("Соединенијата се насекаде.",
                  font_size=42, color=YELLOW, weight=BOLD)
        t5.move_to(UP * 0.5)
        self.play(Write(t5), run_time=1.5)
        self.wait(0.8)
        self.play(t5.animate.scale(0.6).to_edge(UP, buff=0.45), run_time=0.7)

        sub1 = Text("Во водата што ја пиеш.", font_size=26, color=BLUE)
        sub2 = Text("Во воздухот што го дишеш.", font_size=26, color=GREEN)
        sub3 = Text("Во храната.", font_size=26, color=ORANGE)
        sub4 = Text("Па дури и во твоето тело.", font_size=26, color=PURPLE, weight=BOLD)
        subs = VGroup(sub1, sub2, sub3, sub4).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        subs.next_to(t5, DOWN, buff=0.5)
        for s in (sub1, sub2, sub3, sub4):
            self.play(Write(s), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(subs), run_time=0.5)

        list_lbl = Text("Неколку примери:",
                        font_size=24, color=GREY)
        list_lbl.next_to(t5, DOWN, buff=0.45)
        self.play(Write(list_lbl), run_time=0.8)

        def example_row(formula, name, color, y):
            f = MathTex(formula, font_size=40, color=color)
            f.move_to(LEFT * 1.7 + UP * y)
            sep = Text("—", font_size=28, color=GREY).next_to(f, RIGHT, buff=0.3)
            n = Text(name, font_size=26, color=WHITE2).next_to(sep, RIGHT, buff=0.3)
            return VGroup(f, sep, n)

        r1 = example_row(r"H_2 O",    "вода",                BLUE,   1.2)
        r2 = example_row(r"CO_2",     "јаглерод-диоксид",    GREY,   0.45)
        r3 = example_row(r"NaCl",     "трпезна сол",         YELLOW, -0.3)
        r4 = example_row(r"CaCO_3",   "варовник",            ORANGE, -1.05)
        r5 = example_row(r"Fe_2 O_3", "рѓа",                 RED,    -1.8)

        for r in (r1, r2, r3, r4, r5):
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(1.0)

        msg = Text("Хемијата постојано создава нови супстанции околу нас.",
                   font_size=22, color=ORANGE)
        msg.to_edge(DOWN, buff=0.4)
        self.play(Write(msg), run_time=1.6)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t5, list_lbl, r1, r2, r3, r4, r5, msg)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 6 СОЕДИНЕНИЕ vs СМЕСА                              ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vs_mixture")

        warn = Text("Но внимание.",
                    font_size=32, color=ORANGE, weight=BOLD)
        warn.move_to(UP * 0.7)
        self.play(Write(warn), run_time=1.0)
        self.wait(0.6)

        warn2 = Text("Соединение и смеса не се исти.",
                     font_size=30, color=WHITE2)
        warn2.next_to(warn, DOWN, buff=0.35)
        self.play(Write(warn2), run_time=1.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(warn, warn2)), run_time=0.5)

        # Left panel — compound
        left_box = RoundedRectangle(
            width=5.7, height=5.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2.5,
        ).shift(LEFT * 3.3 + DOWN * 0.1)
        comp_lbl = Text("Соединение", font_size=30, color=BLUE, weight=BOLD)
        comp_lbl.move_to(left_box.get_top() + DOWN * 0.45)

        comp_b1 = Text("•  атомите се хемиски поврзани",
                       font_size=20, color=WHITE2)
        comp_b2 = Text("•  соодносот е точен",
                       font_size=20, color=WHITE2)
        comp_b3 = Text("•  потребна е хемиска реакција",
                       font_size=20, color=WHITE2)
        comp_b4 = Text("    за разделување",
                       font_size=20, color=WHITE2)
        comp_bullets = VGroup(comp_b1, comp_b2, comp_b3, comp_b4).arrange(
            DOWN, buff=0.18, aligned_edge=LEFT)
        comp_bullets.next_to(comp_lbl, DOWN, buff=0.45)
        comp_bullets.shift(LEFT * 0.2)

        comp_ex_lbl = Text("Пример:", font_size=22, color=GREY)
        comp_eq = MathTex(r"H_2 O", font_size=44, color=BLUE)
        comp_ex = VGroup(comp_ex_lbl, comp_eq).arrange(DOWN, buff=0.15)
        comp_ex.next_to(comp_bullets, DOWN, buff=0.35)

        self.play(FadeIn(left_box), Write(comp_lbl), run_time=0.8)
        for b in (comp_b1, comp_b2, comp_b3, comp_b4):
            self.play(Write(b), run_time=0.55)
        self.play(Write(comp_ex_lbl), Write(comp_eq), run_time=0.9)
        self.wait(0.8)

        # Right panel — mixture
        right_box = RoundedRectangle(
            width=5.7, height=5.0, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2.5,
        ).shift(RIGHT * 3.3 + DOWN * 0.1)
        mix_lbl = Text("Смеса", font_size=30, color=GREEN, weight=BOLD)
        mix_lbl.move_to(right_box.get_top() + DOWN * 0.45)

        mix_b1 = Text("•  супстанциите само се измешани",
                      font_size=20, color=WHITE2)
        mix_b2 = Text("•  соодносот може да се менува",
                      font_size=20, color=WHITE2)
        mix_b3 = Text("•  може физички да се разделат",
                      font_size=20, color=WHITE2)
        mix_bullets = VGroup(mix_b1, mix_b2, mix_b3).arrange(
            DOWN, buff=0.18, aligned_edge=LEFT)
        mix_bullets.next_to(mix_lbl, DOWN, buff=0.45)
        mix_bullets.shift(LEFT * 0.2)

        mix_ex_lbl = Text("На пример:", font_size=22, color=GREY)
        mix_ex_val = Text("вода + сол", font_size=30, color=GREEN, weight=BOLD)
        mix_ex = VGroup(mix_ex_lbl, mix_ex_val).arrange(DOWN, buff=0.15)
        mix_ex.next_to(mix_bullets, DOWN, buff=0.45)

        self.play(FadeIn(right_box), Write(mix_lbl), run_time=0.8)
        for b in (mix_b1, mix_b2, mix_b3):
            self.play(Write(b), run_time=0.55)
        self.play(Write(mix_ex_lbl), Write(mix_ex_val), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(left_box, comp_lbl, comp_bullets, comp_ex,
                                 right_box, mix_lbl, mix_bullets, mix_ex)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # § 7 CLOSER                                           ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Хемијата не е само мешање супстанции.",
                      font_size=28, color=WHITE2)
        close2 = Text("Таа е создавање нешто ново.",
                      font_size=32, color=YELLOW, weight=BOLD)
        closes = VGroup(close1, close2).arrange(DOWN, buff=0.3)
        closes.move_to(UP * 0.8)
        self.play(Write(close1), run_time=1.4)
        self.play(Write(close2), run_time=1.4)
        self.wait(1.0)

        line3 = Text("Кога атомите се поврзуваат",
                     font_size=24, color=WHITE2)
        line4 = Text("во точен сооднос,",
                     font_size=24, color=WHITE2)
        line5 = Text("се раѓа соединение.",
                     font_size=28, color=ORANGE, weight=BOLD)
        bottom = VGroup(line3, line4, line5).arrange(DOWN, buff=0.18)
        bottom.next_to(closes, DOWN, buff=0.7)
        for l in (line3, line4, line5):
            self.play(Write(l), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(closes, bottom)), run_time=0.6)

        callback1 = Text("И токму така,",
                         font_size=26, color=WHITE2)
        callback2 = Text("од опасен метал",
                         font_size=28, color=PURPLE, weight=BOLD)
        callback3 = Text("и отровен гас...",
                         font_size=28, color=GREEN, weight=BOLD)
        callback4 = Text("се создава нешто",
                         font_size=26, color=WHITE2)
        callback5 = Text("што стои на секоја трпеза.",
                         font_size=32, color=YELLOW, weight=BOLD)
        callbacks = VGroup(callback1, callback2, callback3, callback4, callback5).arrange(
            DOWN, buff=0.25)
        for c in callbacks:
            self.play(Write(c), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(callbacks), run_time=0.7)
        self.wait(0.3)
