"""
chem8-4-3  —  Реакции со кислород — оксиди
Хемија 8, Единица 4: Хемиски реакции

Teaching narrative — Andonovski-style: oxygen as attacker,
metals and non-metals as victims, slow rust as inevitable time.
Render:  manim -ql chem8-4-3.py Chem843Scene
Output:  media/videos/chem8-4-3/480p15/Chem843Scene.mp4
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
RUST    = "#a1572b"


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


class Chem843Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — OXYGEN ATTACKS
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Кислородот напаѓа.",
                  font_size=44, color=RED, weight=BOLD)
        h2 = Text("Метал — оксид.",
                  font_size=38, color=BLUE)
        h3 = Text("Дрво — пепел.",
                  font_size=38, color=ORANGE)
        h4 = Text("Железо — рѓа.",
                  font_size=38, color=RUST)
        h5 = Text("Време прави сè.",
                  font_size=34, color=WHITE2, slant=ITALIC)
        h6 = Text("Не бавно. Но сигурно.",
                  font_size=36, color=YELLOW, weight=BOLD)
        hook = VGroup(h1, h2, h3, h4, h5, h6).arrange(DOWN, buff=0.25)
        hook.move_to(ORIGIN)

        self.play(Write(h1), run_time=1.0)
        self.wait(0.3)
        for line in (h2, h3, h4):
            self.play(FadeIn(line, shift=RIGHT * 0.15), run_time=0.6)
            self.wait(0.15)
        self.play(FadeIn(h5), run_time=0.7)
        self.wait(0.2)
        self.play(Write(h6), run_time=1.1)
        self.wait(1.4)
        self.play(FadeOut(hook), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHAT IS AN OXIDE?
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е оксид?", BLUE)
        self.play(Write(title), run_time=0.8)

        defn = Text("Соединение на елемент со кислород.",
                    font_size=32, color=WHITE2)
        defn.move_to(UP * 1.3)
        self.play(Write(defn), run_time=1.1)
        self.wait(0.4)

        formula = MathTex(r"\text{Елемент}", r"+", r"O_2", r"\to", r"\text{Оксид}",
                          font_size=54)
        formula[0].set_color(BLUE)
        formula[2].set_color(RED)
        formula[4].set_color(GREEN)
        formula.move_to(ORIGIN)
        self.play(Write(formula), run_time=1.4)
        self.wait(0.5)

        examples = VGroup(
            MathTex(r"2\,Mg + O_2 \to 2\,MgO", font_size=36, color=WHITE2),
            MathTex(r"C + O_2 \to CO_2", font_size=36, color=WHITE2),
            MathTex(r"S + O_2 \to SO_2", font_size=36, color=WHITE2),
        ).arrange(DOWN, buff=0.25)
        examples.move_to(DOWN * 1.7)
        for ex in examples:
            self.play(Write(ex), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, defn, formula, examples)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  TWO FAMILIES — METAL VS NON-METAL OXIDES
        # ══════════════════════════════════════════════════════════
        self.next_section("families")

        title2 = section_title("Две семејства", YELLOW)
        self.play(Write(title2), run_time=0.8)

        # Left column: metal oxides
        left_box = RoundedRectangle(width=5.8, height=4.5, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=BLUE, stroke_width=2)
        left_box.move_to(LEFT * 3.4 + DOWN * 0.4)
        left_title = Text("Метални оксиди", font_size=28,
                          color=BLUE, weight=BOLD)
        left_title.move_to(left_box.get_top() + DOWN * 0.4)
        left_sub = Text("базни", font_size=22, color=GREEN, slant=ITALIC)
        left_sub.next_to(left_title, DOWN, buff=0.15)
        left_items = VGroup(
            Text("MgO  —  магнезиум-оксид", font_size=22, color=WHITE2),
            Text("CaO  —  живо вапно", font_size=22, color=WHITE2),
            Text("Fe₂O₃  —  рѓа", font_size=22, color=RUST),
            Text("Na₂O  —  натриум-оксид", font_size=22, color=WHITE2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        left_items.next_to(left_sub, DOWN, buff=0.45)
        left_g = VGroup(left_box, left_title, left_sub, left_items)

        # Right column: non-metal oxides
        right_box = RoundedRectangle(width=5.8, height=4.5, corner_radius=0.25,
                                     fill_color=DARK_CARD, fill_opacity=1,
                                     stroke_color=ORANGE, stroke_width=2)
        right_box.move_to(RIGHT * 3.4 + DOWN * 0.4)
        right_title = Text("Неметални оксиди", font_size=28,
                           color=ORANGE, weight=BOLD)
        right_title.move_to(right_box.get_top() + DOWN * 0.4)
        right_sub = Text("кисели", font_size=22, color=RED, slant=ITALIC)
        right_sub.next_to(right_title, DOWN, buff=0.15)
        right_items = VGroup(
            Text("CO₂  —  јаглерод-диоксид", font_size=22, color=WHITE2),
            Text("SO₂  —  сулфур-диоксид", font_size=22, color=WHITE2),
            Text("NO₂  —  азот-диоксид", font_size=22, color=WHITE2),
            Text("P₂O₅  —  фосфорен", font_size=22, color=WHITE2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_items.next_to(right_sub, DOWN, buff=0.45)
        right_g = VGroup(right_box, right_title, right_sub, right_items)

        self.play(FadeIn(left_g), run_time=0.9)
        self.play(FadeIn(right_g), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title2, left_g, right_g)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  MAGNESIUM BURNS — DRAMATIC FLASH
        # ══════════════════════════════════════════════════════════
        self.next_section("magnesium")

        title3 = section_title("Магнезиумот гори", ORANGE)
        self.play(Write(title3), run_time=0.8)

        story = Text("Лента магнезиум. Чкорче. Светлина.",
                     font_size=28, color=WHITE2)
        story.move_to(UP * 1.7)
        self.play(FadeIn(story), run_time=0.9)

        # Magnesium ribbon as silver bar
        ribbon = Rectangle(width=2.4, height=0.3, fill_color=GREY,
                           fill_opacity=1, stroke_color=WHITE2, stroke_width=1.5)
        ribbon.move_to(LEFT * 3.5 + DOWN * 0.2)
        rb_lbl = Text("Mg", font_size=24, color=WHITE2).next_to(ribbon, DOWN, buff=0.2)

        # Bright flash
        flash = Star(n=8, outer_radius=1.0, inner_radius=0.5,
                     fill_color=YELLOW, fill_opacity=0.9,
                     stroke_color=WHITE2, stroke_width=2)
        flash.move_to(DOWN * 0.2)

        # White powder pile
        powder = Ellipse(width=1.8, height=0.5, fill_color=WHITE2,
                         fill_opacity=0.9, stroke_color=GREY, stroke_width=1.5)
        powder.move_to(RIGHT * 3.5 + DOWN * 0.4)
        pw_lbl = Text("MgO", font_size=24, color=WHITE2).next_to(powder, DOWN, buff=0.2)
        pw_lbl2 = Text("бел прав", font_size=20, color=GREEN).next_to(pw_lbl, DOWN, buff=0.1)

        self.play(FadeIn(ribbon), Write(rb_lbl), run_time=0.7)
        self.play(GrowFromCenter(flash), run_time=0.6)
        # pulsing flash
        self.play(flash.animate.scale(1.4), run_time=0.4)
        self.play(flash.animate.scale(0.7).set_fill(opacity=0.4), run_time=0.5)
        self.play(FadeIn(powder), Write(pw_lbl), Write(pw_lbl2), run_time=0.8)

        eq = MathTex(r"2\,Mg", r"+", r"O_2", r"\to", r"2\,MgO",
                     font_size=46)
        eq[0].set_color(GREY)
        eq[2].set_color(RED)
        eq[4].set_color(GREEN)
        eq.move_to(DOWN * 2.3)
        self.play(Write(eq), run_time=1.3)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title3, story, ribbon, rb_lbl,
                                  flash, powder, pw_lbl, pw_lbl2, eq)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  RUST — SLOW OXIDATION
        # ══════════════════════════════════════════════════════════
        self.next_section("rust")

        title4 = section_title("Рѓата — бавна оксидација", RUST)
        self.play(Write(title4), run_time=0.8)

        # Three stages of iron nail
        stage1 = Rectangle(width=2.0, height=0.45,
                           fill_color=GREY, fill_opacity=1,
                           stroke_color=WHITE2, stroke_width=1.5)
        s1_lbl = Text("ден 1: железо", font_size=22, color=WHITE2)
        s1_lbl.next_to(stage1, DOWN, buff=0.2)
        s1_g = VGroup(stage1, s1_lbl).move_to(LEFT * 4 + UP * 0.2)

        stage2 = Rectangle(width=2.0, height=0.45,
                           fill_color=ORANGE, fill_opacity=0.7,
                           stroke_color=RUST, stroke_width=1.5)
        s2_lbl = Text("ден 30: рб појава", font_size=22, color=WHITE2)
        s2_lbl.next_to(stage2, DOWN, buff=0.2)
        s2_g = VGroup(stage2, s2_lbl).move_to(UP * 0.2)

        stage3 = Rectangle(width=2.0, height=0.45,
                           fill_color=RUST, fill_opacity=1,
                           stroke_color="#6b3010", stroke_width=1.5)
        s3_lbl = Text("ден 365: Fe₂O₃", font_size=22, color=WHITE2)
        s3_lbl.next_to(stage3, DOWN, buff=0.2)
        s3_g = VGroup(stage3, s3_lbl).move_to(RIGHT * 4 + UP * 0.2)

        self.play(FadeIn(s1_g), run_time=0.6)
        self.play(FadeIn(s2_g), run_time=0.7)
        self.play(FadeIn(s3_g), run_time=0.8)

        rust_eq = MathTex(r"4\,Fe", r"+", r"3\,O_2", r"\to", r"2\,Fe_2O_3",
                          font_size=44)
        rust_eq[0].set_color(GREY)
        rust_eq[2].set_color(RED)
        rust_eq[4].set_color(RUST)
        rust_eq.move_to(DOWN * 1.5)
        self.play(Write(rust_eq), run_time=1.4)
        self.wait(0.5)

        sloweq = Text("Бавно. Тивко. Неизбежно.",
                      font_size=30, color=YELLOW, slant=ITALIC, weight=BOLD)
        sloweq.move_to(DOWN * 2.7)
        self.play(Write(sloweq), run_time=1.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, s1_g, s2_g, s3_g, rust_eq, sloweq)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  CO VS CO2 — INVISIBLE DANGER
        # ══════════════════════════════════════════════════════════
        self.next_section("co_warning")

        title5 = section_title("Внимавај: CO", RED)
        self.play(Write(title5), run_time=0.8)

        # Two cards side by side
        co2_card = RoundedRectangle(width=5.5, height=3.6, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=GREEN, stroke_width=2)
        co2_card.move_to(LEFT * 3.3 + DOWN * 0.3)
        co2_t = Text("CO₂", font_size=46, color=GREEN, weight=BOLD)
        co2_t.move_to(co2_card.get_top() + DOWN * 0.7)
        co2_d = VGroup(
            Text("јаглерод-диоксид", font_size=22, color=WHITE2),
            Text("од потполно горење", font_size=22, color=WHITE2),
            Text("растенијата го впиваат", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.2)
        co2_d.next_to(co2_t, DOWN, buff=0.35)

        co_card = RoundedRectangle(width=5.5, height=3.6, corner_radius=0.25,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=RED, stroke_width=2)
        co_card.move_to(RIGHT * 3.3 + DOWN * 0.3)
        co_t = Text("CO", font_size=46, color=RED, weight=BOLD)
        co_t.move_to(co_card.get_top() + DOWN * 0.7)
        co_d = VGroup(
            Text("јаглерод-моноксид", font_size=22, color=WHITE2),
            Text("без боја, без мирис", font_size=22, color=WHITE2),
            Text("отровен!", font_size=24, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        co_d.next_to(co_t, DOWN, buff=0.35)

        self.play(FadeIn(VGroup(co2_card, co2_t, co2_d)), run_time=0.8)
        self.play(FadeIn(VGroup(co_card, co_t, co_d)), run_time=0.8)
        self.wait(0.6)

        bottom = Text("Вентилирај. Секогаш.",
                      font_size=30, color=YELLOW, weight=BOLD)
        bottom.to_edge(DOWN, buff=0.45)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title5, co2_card, co2_t, co2_d,
                                  co_card, co_t, co_d, bottom)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        c1 = Text("Кислородот не мирува.",
                  font_size=34, color=RED)
        c2 = Text("Метал станува оксид.",
                  font_size=32, color=BLUE)
        c3 = Text("Неметал станува киселина.",
                  font_size=32, color=ORANGE)
        c4 = Text("Време. И воздух.",
                  font_size=30, color=WHITE2, slant=ITALIC)
        c5 = Text("Реагираат.",
                  font_size=56, color=YELLOW, weight=BOLD)
        close = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, buff=0.35)
        close.move_to(ORIGIN)

        self.play(Write(c1), run_time=0.9)
        self.wait(0.2)
        self.play(Write(c2), run_time=0.9)
        self.wait(0.2)
        self.play(Write(c3), run_time=0.9)
        self.wait(0.2)
        self.play(FadeIn(c4), run_time=0.8)
        self.wait(0.3)
        self.play(Write(c5), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
        self.wait(0.4)
