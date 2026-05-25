"""
chem8-4-1  —  Физичка промена или хемиска реакција?
Хемија 8, Единица 4: Хемиски реакции

Teaching narrative — Andonovski-style: three-beat punches,
reactions as drama, atoms as characters, не...туку contrast.
Render:  manim -ql chem8-4-1.py Chem841Scene
Output:  media/videos/chem8-4-1/480p15/Chem841Scene.mp4
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


class Chem841Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Ледот се топи — иста супстанца.",
                     font_size=38, color=BLUE, weight=BOLD)
        hook2 = Text("Дрвото гори — нова.",
                     font_size=38, color=RED, weight=BOLD)
        hook3 = Text("Едното — форма. Другото — суштина.",
                     font_size=34, color=WHITE2)
        hook4 = Text("Хемија и физика се сретнуваат тука.",
                     font_size=32, color=YELLOW, slant=ITALIC)
        hook_g = VGroup(hook1, hook2, hook3, hook4).arrange(DOWN, buff=0.35)
        hook_g.move_to(ORIGIN)

        self.play(Write(hook1), run_time=1.2)
        self.wait(0.4)
        self.play(Write(hook2), run_time=1.2)
        self.wait(0.4)
        self.play(FadeIn(hook3), run_time=0.9)
        self.wait(0.3)
        self.play(Write(hook4), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(hook_g), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  PHYSICAL CHANGE — ICE MELTING
        # ══════════════════════════════════════════════════════════
        self.next_section("physical")

        title = section_title("Физичка промена", BLUE)
        self.play(Write(title), run_time=0.9)

        # Ice cube
        ice = RoundedRectangle(width=1.8, height=1.4, corner_radius=0.15,
                               fill_color=BLUE, fill_opacity=0.75,
                               stroke_color=WHITE2, stroke_width=2)
        ice_label = Text("лед", font_size=28, color=WHITE2).next_to(ice, DOWN, buff=0.2)
        ice_g = VGroup(ice, ice_label).move_to(LEFT * 4 + DOWN * 0.3)

        arrow = Arrow(LEFT * 2.4, RIGHT * 2.4, color=YELLOW, buff=0.1, stroke_width=4)
        arrow_label = Text("топење", font_size=24, color=YELLOW).next_to(arrow, UP, buff=0.15)
        arrow_g = VGroup(arrow, arrow_label).move_to(DOWN * 0.3)

        water = Circle(radius=0.8, fill_color=BLUE, fill_opacity=0.55,
                       stroke_color=WHITE2, stroke_width=2)
        water_label = Text("вода", font_size=28, color=WHITE2).next_to(water, DOWN, buff=0.2)
        water_g = VGroup(water, water_label).move_to(RIGHT * 4 + DOWN * 0.3)

        self.play(FadeIn(ice_g), run_time=0.7)
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=0.9)
        self.play(FadeIn(water_g), run_time=0.7)

        same = Text("H₂O — иста супстанца. Само форма.",
                    font_size=30, color=GREEN, weight=BOLD)
        same.to_edge(DOWN, buff=0.7)
        self.play(Write(same), run_time=1.3)
        self.wait(0.8)

        rev = Text("Може да се врати. Реверзибилна.",
                   font_size=28, color=WHITE2, slant=ITALIC)
        rev.next_to(same, UP, buff=0.25)
        self.play(FadeIn(rev), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, ice_g, arrow_g, water_g, same, rev)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  CHEMICAL CHANGE — WOOD BURNING
        # ══════════════════════════════════════════════════════════
        self.next_section("chemical")

        title2 = section_title("Хемиска реакција", RED)
        self.play(Write(title2), run_time=0.9)

        # Wood block
        wood = Rectangle(width=1.8, height=1.2,
                        fill_color="#6d4c41", fill_opacity=0.9,
                        stroke_color=ORANGE, stroke_width=2)
        wood_label = Text("дрво", font_size=26, color=WHITE2).next_to(wood, DOWN, buff=0.2)
        wood_g = VGroup(wood, wood_label).move_to(LEFT * 4.5 + DOWN * 0.2)

        # Flame
        flame = Triangle(fill_color=ORANGE, fill_opacity=0.9,
                         stroke_color=YELLOW, stroke_width=2).scale(0.8)
        flame.rotate(PI)
        flame_label = Text("оган", font_size=24, color=YELLOW).next_to(flame, DOWN, buff=0.15)
        flame_g = VGroup(flame, flame_label).move_to(LEFT * 1.5 + DOWN * 0.2)

        # Arrow
        arr2 = Arrow(LEFT * 0.3, RIGHT * 1.4, color=YELLOW, buff=0.1, stroke_width=4)
        arr2.move_to(RIGHT * 0.6 + DOWN * 0.2)

        # Products
        products = VGroup(
            Text("CO₂", font_size=30, color=GREY),
            Text("H₂O", font_size=30, color=BLUE),
            Text("пепел", font_size=26, color="#6d4c41"),
        ).arrange(DOWN, buff=0.2)
        products.move_to(RIGHT * 3.8 + DOWN * 0.2)
        prod_label = Text("нови супстанци", font_size=22, color=GREEN)
        prod_label.next_to(products, DOWN, buff=0.25)

        self.play(FadeIn(wood_g), run_time=0.6)
        self.play(FadeIn(flame_g), run_time=0.6)
        self.play(GrowArrow(arr2), run_time=0.5)
        self.play(FadeIn(products), run_time=0.8)
        self.play(Write(prod_label), run_time=0.6)
        self.wait(0.6)

        irrev = Text("Не може назад. Иста суштина — изгубена.",
                     font_size=28, color=RED, weight=BOLD)
        irrev.to_edge(DOWN, buff=0.6)
        self.play(Write(irrev), run_time=1.3)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title2, wood_g, flame_g, arr2, products, prod_label, irrev)),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  FIVE SIGNS OF CHEMICAL REACTION
        # ══════════════════════════════════════════════════════════
        self.next_section("signs")

        title3 = section_title("Пет знаци на реакција", YELLOW)
        self.play(Write(title3), run_time=0.9)

        signs = [
            ("Боја се менува", "јаболко → кафеаво", PURPLE),
            ("Излегува гас", "сода + оцет → CO₂", BLUE),
            ("Се формира талог", "бистро → замат", GREY),
            ("Температура скока", "топло или ладно", ORANGE),
            ("Излегува светлина", "магнезиум гори", YELLOW),
        ]

        sign_group = VGroup()
        for i, (sign, ex, col) in enumerate(signs):
            num = Text(f"{i+1}.", font_size=30, color=col, weight=BOLD)
            txt = Text(sign, font_size=28, color=WHITE2, weight=BOLD)
            extra = Text(ex, font_size=22, color=GREY, slant=ITALIC)
            row = VGroup(num, txt, extra).arrange(RIGHT, buff=0.35, aligned_edge=DOWN)
            sign_group.add(row)
        sign_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        sign_group.next_to(title3, DOWN, buff=0.5)

        for row in sign_group:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.55)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, sign_group)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  EQUATION FORM — REACTANTS → PRODUCTS
        # ══════════════════════════════════════════════════════════
        self.next_section("equation")

        title4 = section_title("Запис на реакција", GREEN)
        self.play(Write(title4), run_time=0.8)

        word_eq = Text("Магнезиум + Кислород → Магнезиум-оксид",
                       font_size=30, color=WHITE2)
        word_eq.move_to(UP * 1.4)
        self.play(Write(word_eq), run_time=1.5)
        self.wait(0.5)

        sym_eq = MathTex(r"2\,Mg", r"+", r"O_2", r"\to", r"2\,MgO",
                         font_size=58)
        sym_eq[0].set_color(BLUE)
        sym_eq[2].set_color(RED)
        sym_eq[4].set_color(GREEN)
        sym_eq.move_to(ORIGIN)
        self.play(Write(sym_eq), run_time=1.6)
        self.wait(0.4)

        # Labels: reactants / arrow / products
        reactant_brace = Brace(VGroup(sym_eq[0], sym_eq[2]), DOWN, buff=0.25)
        reactant_lbl = Text("реактанти", font_size=26, color=BLUE).next_to(reactant_brace, DOWN, buff=0.1)
        product_brace = Brace(sym_eq[4], DOWN, buff=0.25)
        product_lbl = Text("продукт", font_size=26, color=GREEN).next_to(product_brace, DOWN, buff=0.1)

        self.play(GrowFromCenter(reactant_brace), FadeIn(reactant_lbl), run_time=0.7)
        self.play(GrowFromCenter(product_brace), FadeIn(product_lbl), run_time=0.7)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, word_eq, sym_eq,
                                  reactant_brace, reactant_lbl,
                                  product_brace, product_lbl)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  CONSERVATION OF MASS — LAVOISIER
        # ══════════════════════════════════════════════════════════
        self.next_section("conservation")

        title5 = section_title("Закон на зачувување", PURPLE)
        self.play(Write(title5), run_time=0.8)

        lav = Text("Лавоазјé. 1789.",
                   font_size=38, color=YELLOW, weight=BOLD)
        lav.move_to(UP * 1.8)
        self.play(Write(lav), run_time=1.1)
        self.wait(0.4)

        # Balance: scale visualization
        m_eq = MathTex(r"\underbrace{2g\, H_2 + 16g\, O_2}_{\text{реактанти}}",
                       r"\,=\,",
                       r"\underbrace{18g\, H_2O}_{\text{продукт}}",
                       font_size=42)
        m_eq[0].set_color(BLUE)
        m_eq[2].set_color(GREEN)
        m_eq.move_to(ORIGIN)
        self.play(Write(m_eq), run_time=1.8)
        self.wait(0.6)

        rules = VGroup(
            Text("Маса влегува. Маса излегува.",
                 font_size=28, color=WHITE2),
            Text("Збирот — ист.",
                 font_size=30, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.25)
        rules.next_to(m_eq, DOWN, buff=0.55)
        for r in rules:
            self.play(FadeIn(r), run_time=0.7)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title5, lav, m_eq, rules)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSE
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        c1 = Text("Форма се менува — физика.",
                  font_size=34, color=BLUE)
        c2 = Text("Суштина се менува — хемија.",
                  font_size=34, color=RED)
        c3 = Text("Гледај знаци. Слушај супстанци.",
                  font_size=32, color=WHITE2, slant=ITALIC)
        c4 = Text("Распознај.",
                  font_size=52, color=YELLOW, weight=BOLD)
        close = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.4)
        close.move_to(ORIGIN)

        self.play(Write(c1), run_time=1.0)
        self.wait(0.3)
        self.play(Write(c2), run_time=1.0)
        self.wait(0.3)
        self.play(FadeIn(c3), run_time=0.9)
        self.wait(0.4)
        self.play(Write(c4), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
        self.wait(0.4)
