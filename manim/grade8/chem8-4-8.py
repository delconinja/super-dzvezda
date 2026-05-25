"""
chem8-4-8  —  Киселини и бази во секојдневие
Хемија 8, Единица 4: Киселини, бази и соли (завршна)

Teaching narrative — Andonovski-style: three-beat punches,
acids as friendly helpers, personification, one-word finishers.
Render:  manim -ql chem8-4-8.py Chem848Scene
Output:  media/videos/chem8-4-8/480p15/Chem848Scene.mp4
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


class Chem848Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        beats = VGroup(
            Text("Лимон во чај.",  font_size=38, color=YELLOW, weight=BOLD),
            Text("Сирче во салата.", font_size=38, color=ORANGE, weight=BOLD),
            Text("HCl во стомак.",   font_size=38, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.35).to_edge(UP, buff=0.7)

        for b in beats:
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.65)
            self.wait(0.2)
        self.wait(0.4)

        big = Text("Киселините се секаде.", font_size=40, color=WHITE2).move_to(ORIGIN)
        self.play(Write(big), run_time=1.0)
        self.wait(0.5)

        not_scare = Text("Не плашат.",   font_size=32, color=GREEN).to_edge(DOWN, buff=1.6)
        feed      = Text("Хранат.",      font_size=32, color=YELLOW).to_edge(DOWN, buff=1.1)
        clean     = Text("Чистат.",      font_size=32, color=BLUE).to_edge(DOWN, buff=0.6)
        digest    = Text("Помагаат да варис.", font_size=30, color=ORANGE, weight=BOLD).to_edge(DOWN, buff=0.1)

        self.play(Write(not_scare), run_time=0.6)
        self.play(Write(feed), run_time=0.6)
        self.play(Write(clean), run_time=0.6)
        self.play(Write(digest), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(beats, big, not_scare, feed, clean, digest)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  СЕКОЈДНЕВНИ КИСЕЛИНИ                            ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("acids")

        t2 = section_title("Секојдневни киселини", color=RED)
        self.play(Write(t2), run_time=0.8)

        def acid_card(label, formula, where, color):
            box = RoundedRectangle(width=3.0, height=2.2, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            ttl = Text(label, font_size=22, color=color, weight=BOLD)
            f   = MathTex(formula, font_size=26, color=WHITE2)
            w   = Text(where, font_size=17, color=WHITE2)
            inner = VGroup(ttl, f, w).arrange(DOWN, buff=0.18).move_to(box)
            return VGroup(box, inner)

        a1 = acid_card("лимонска",   r"C_6H_8O_7", "лимон, портокал", YELLOW)
        a2 = acid_card("оцетна",     r"CH_3COOH",  "сирче",           ORANGE)
        a3 = acid_card("хлороводородна", r"HCl",    "желудник",        RED)
        a4 = acid_card("аскорбинска",r"C_6H_8O_6", "витамин C",       GREEN)

        row1 = VGroup(a1, a2).arrange(RIGHT, buff=0.5).shift(UP*0.7)
        row2 = VGroup(a3, a4).arrange(RIGHT, buff=0.5).shift(DOWN*1.5)

        for a in (a1, a2, a3, a4):
            self.play(FadeIn(a, shift=UP*0.2), run_time=0.55)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, a1, a2, a3, a4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  СЕКОЈДНЕВНИ БАЗИ                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("bases")

        t3 = section_title("Секојдневни бази", color=BLUE)
        self.play(Write(t3), run_time=0.8)

        def base_card(label, formula, where, color):
            box = RoundedRectangle(width=3.0, height=2.2, corner_radius=0.25,
                                    fill_color=DARK_CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=2.5)
            ttl = Text(label, font_size=22, color=color, weight=BOLD)
            f   = MathTex(formula, font_size=26, color=WHITE2)
            w   = Text(where, font_size=17, color=WHITE2)
            inner = VGroup(ttl, f, w).arrange(DOWN, buff=0.18).move_to(box)
            return VGroup(box, inner)

        b1 = base_card("натриум хидроксид", r"NaOH",      "сапун, средства", BLUE)
        b2 = base_card("сода бикарбона",    r"NaHCO_3",   "печење, чистење", GREEN)
        b3 = base_card("магнезиум хидрокс.",r"Mg(OH)_2",  "млеко на магн.",  PURPLE)
        b4 = base_card("амонијак",          r"NH_3",      "средства за чист.", ORANGE)

        row1 = VGroup(b1, b2).arrange(RIGHT, buff=0.5).shift(UP*0.7)
        row2 = VGroup(b3, b4).arrange(RIGHT, buff=0.5).shift(DOWN*1.5)

        for b in (b1, b2, b3, b4):
            self.play(FadeIn(b, shift=UP*0.2), run_time=0.55)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, b1, b2, b3, b4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  КИСЕЛИНА ВО СТОМАКОТ                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("stomach")

        t4 = section_title("Стомак — киселинска фабрика", color=RED)
        self.play(Write(t4), run_time=0.8)

        # Stomach shape
        stomach = VMobject(stroke_color=RED, stroke_width=3, fill_color="#5a1a1a",
                           fill_opacity=0.6)
        pts = [
            np.array([-1.0, 1.2, 0]),
            np.array([0.2, 1.6, 0]),
            np.array([1.4, 1.0, 0]),
            np.array([1.6, -0.4, 0]),
            np.array([0.6, -1.4, 0]),
            np.array([-0.8, -1.2, 0]),
            np.array([-1.3, 0.0, 0]),
            np.array([-1.0, 1.2, 0]),
        ]
        stomach.set_points_smoothly(pts)
        stomach.shift(LEFT*3.0 + DOWN*0.2)

        st_lbl = Text("желудник", font_size=22, color=RED).next_to(stomach, DOWN, buff=0.25)
        ph_lbl = Text("pH ≈ 1–2", font_size=24, color=YELLOW, weight=BOLD).next_to(stomach, UP, buff=0.2)

        self.play(Create(stomach), Write(st_lbl), Write(ph_lbl), run_time=1.4)

        # Info on right
        info = VGroup(
            Text("HCl ја вари храната.",         font_size=24, color=WHITE2),
            Text("Убива бактерии.",              font_size=24, color=WHITE2),
            Text("Активира ензими.",             font_size=24, color=WHITE2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(RIGHT*2.5 + DOWN*0.2)
        for ln in info:
            self.play(FadeIn(ln, shift=LEFT*0.2), run_time=0.55)
        self.wait(0.6)

        warn = callout("Кога има многу — горчина и горење.",
                       width=12.0, font_size=24, border=ORANGE)
        warn.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(warn, shift=UP*0.2), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t4, stomach, st_lbl, ph_lbl, info, warn)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  КИСЕЛ ДОЖД                                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("acid_rain")

        t5 = section_title("Кисел дожд — кога науката бесни", color=PURPLE)
        self.play(Write(t5), run_time=0.8)

        # Cloud
        cloud = VGroup(
            Circle(radius=0.6, fill_color=GREY, fill_opacity=0.8, stroke_opacity=0),
            Circle(radius=0.7, fill_color=GREY, fill_opacity=0.8, stroke_opacity=0).shift(LEFT*0.6),
            Circle(radius=0.55, fill_color=GREY, fill_opacity=0.8, stroke_opacity=0).shift(RIGHT*0.6),
            Circle(radius=0.5, fill_color=GREY, fill_opacity=0.8, stroke_opacity=0).shift(UP*0.35 + LEFT*0.2),
        ).shift(UP*1.6 + LEFT*2.5)

        smoke_lbl = Text("SO₂ + NO₂ од фабрики", font_size=20, color=WHITE2).next_to(cloud, UP, buff=0.15)

        # Rain
        drops = VGroup()
        for i in range(8):
            d = Triangle(fill_color=BLUE, fill_opacity=0.9, stroke_opacity=0)
            d.scale(0.15)
            d.rotate(PI)
            d.shift(LEFT*2.5 + UP*0.5 + RIGHT*(i-3.5)*0.35 + DOWN*0.3)
            drops.add(d)

        # Ground & tree
        ground = Rectangle(width=10.0, height=0.5, fill_color="#5d4037",
                            fill_opacity=1, stroke_opacity=0)
        ground.to_edge(DOWN, buff=0.15)

        tree_trunk = Rectangle(width=0.3, height=1.2, fill_color="#3e2723",
                                fill_opacity=1, stroke_opacity=0)
        tree_leaves = Circle(radius=0.7, fill_color=GREEN, fill_opacity=0.8,
                              stroke_opacity=0)
        tree_leaves.next_to(tree_trunk, UP, buff=-0.2)
        tree = VGroup(tree_trunk, tree_leaves).shift(RIGHT*2.5 + DOWN*0.3)

        self.play(FadeIn(cloud), Write(smoke_lbl), run_time=0.9)
        self.play(FadeIn(ground), FadeIn(tree), run_time=0.7)
        self.play(LaggedStartMap(FadeIn, drops, lag_ratio=0.1), run_time=1.0)

        # Damage
        self.play(tree_leaves.animate.set_fill("#6d4c41", opacity=0.7),
                  run_time=1.0)

        damage = Text("Дожд што не милува — гори.",
                      font_size=24, color=RED, weight=BOLD).to_edge(DOWN, buff=0.85)
        self.play(Write(damage), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t5, cloud, smoke_lbl, drops, ground, tree,
                                  damage)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  БЕЗБЕДНОСТ                                      ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("safety")

        t6 = section_title("Безбедност — закон, не препорака", color=ORANGE)
        self.play(Write(t6), run_time=0.8)

        rules = VGroup(
            Text("Не мешај средства за чистење.", font_size=26, color=WHITE2),
            Text("Носи ракавици. Носи очила.",      font_size=26, color=WHITE2),
            Text("Прочитај етикета. Секогаш.",      font_size=26, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        for r in rules:
            self.play(FadeIn(r, shift=UP*0.2), run_time=0.6)
            self.wait(0.15)
        self.wait(1.0)

        far = callout("Далечински контролираш телевизор. Хемија — не.",
                      width=12.5, font_size=24, border=RED)
        far.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(far, shift=UP*0.2), run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t6, rules, far)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSER                                          ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closer")

        close1 = Text("Во чаша.", font_size=42, color=YELLOW, weight=BOLD)
        close1.move_to(UP*0.9)
        self.play(Write(close1), run_time=0.9)
        self.wait(0.3)

        close2 = Text("Во кујна.", font_size=42, color=ORANGE, weight=BOLD)
        close2.move_to(UP*0.15)
        self.play(Write(close2), run_time=0.9)
        self.wait(0.3)

        close3 = Text("Во тебе.", font_size=42, color=RED, weight=BOLD)
        close3.move_to(DOWN*0.6)
        self.play(Write(close3), run_time=0.9)
        self.wait(0.4)

        close4 = Text("Хемија — секој ден.", font_size=38, color=GREEN, weight=BOLD)
        close4.to_edge(DOWN, buff=0.6)
        self.play(Write(close4), run_time=1.2)
        self.wait(1.6)

        self.play(FadeOut(VGroup(close1, close2, close3, close4)), run_time=0.7)
        self.wait(0.3)
