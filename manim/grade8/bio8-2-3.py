"""
bio8-2-3  —  Зглобови — видови
Биологија 8, Единица 2: Движењето кај луѓето

Teaching narrative — Andonovski-style: three-beat punches,
joints as different freedoms, cartilage as cushion.
Render:  manim -ql bio8-2-3.py Bio823Scene
Output:  media/videos/bio8-2-3/480p15/Bio823Scene.mp4
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


def joint_card(name, example, color, pos):
    box = RoundedRectangle(width=3.0, height=1.6, corner_radius=0.2,
                           fill_color=DARK_CARD, fill_opacity=1,
                           stroke_color=color, stroke_width=2)
    box.move_to(pos)
    nm = Text(name, font_size=22, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.3)
    ex = Text(example, font_size=16, color=WHITE2)
    ex.move_to(box.get_center() + DOWN * 0.3)
    return VGroup(box, nm, ex)


class Bio823Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Колено се свиткува напред-назад.",
                  font_size=36, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.8)
        self.play(Write(h1), run_time=1.3)
        self.wait(0.3)

        h2 = Text("Рамо се ротира во сите страни.",
                  font_size=36, color=BLUE, weight=BOLD)
        h2.next_to(h1, DOWN, buff=0.5)
        self.play(Write(h2), run_time=1.3)
        self.wait(0.3)

        h3 = VGroup(
            Text("Различни зглобови.", font_size=34, color=GREEN),
            Text("Различни слободи.", font_size=34, color=ORANGE),
        ).arrange(DOWN, buff=0.3).next_to(h2, DOWN, buff=0.7)

        for line in h3:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, h2, h3)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ТРИ ОСНОВНИ ВИДОВИ                              ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("three_types")
        title = section_title("Три основни видови зглобови")
        self.play(Write(title), run_time=0.8)

        # Immovable — skull suture (two interlocking shapes)
        sk1 = Polygon([-0.6, 0.4, 0], [0, 0.4, 0], [-0.3, 0, 0], [0, -0.4, 0], [-0.6, -0.4, 0],
                      color=WHITE2, fill_opacity=0.4, stroke_width=2)
        sk2 = Polygon([0, 0.4, 0], [0.6, 0.4, 0], [0.6, -0.4, 0], [0, -0.4, 0], [0.3, 0, 0],
                      color=WHITE2, fill_opacity=0.4, stroke_width=2)
        immov = VGroup(sk1, sk2)
        immov.scale(0.9).move_to(LEFT * 4.0 + UP * 0.7)
        im_name = Text("Неподвижни", font_size=22, color=RED, weight=BOLD)
        im_name.next_to(immov, DOWN, buff=0.4)
        im_ex = Text("шевови на череп", font_size=16, color=WHITE2)
        im_ex.next_to(im_name, DOWN, buff=0.15)

        # Slightly movable — vertebrae (two blocks with disc)
        v1 = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1,
                              color=WHITE2, fill_opacity=0.4, stroke_width=2)
        v1.move_to(UP * 0.4)
        v2 = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1,
                              color=WHITE2, fill_opacity=0.4, stroke_width=2)
        v2.move_to(DOWN * 0.4)
        disc = Ellipse(width=1.3, height=0.18, color=ORANGE,
                       fill_opacity=0.7, stroke_color=ORANGE, stroke_width=1)
        slight = VGroup(v1, v2, disc)
        slight.move_to(UP * 0.7)
        sl_name = Text("Слабо подвижни", font_size=22, color=ORANGE, weight=BOLD)
        sl_name.next_to(slight, DOWN, buff=0.4)
        sl_ex = Text("пршлени на кичма", font_size=16, color=WHITE2)
        sl_ex.next_to(sl_name, DOWN, buff=0.15)

        # Freely movable — ball and socket
        socket = Arc(radius=0.55, start_angle=PI / 2, angle=PI, color=WHITE2,
                     stroke_width=3)
        ball = Circle(radius=0.4, color=GREEN, fill_opacity=0.6, stroke_width=2)
        ball.move_to(socket.get_center() + RIGHT * 0.1)
        free = VGroup(socket, ball)
        free.move_to(RIGHT * 4.0 + UP * 0.7)
        fr_name = Text("Слободни", font_size=22, color=GREEN, weight=BOLD)
        fr_name.next_to(free, DOWN, buff=0.4)
        fr_ex = Text("рамо, колк, лакт", font_size=16, color=WHITE2)
        fr_ex.next_to(fr_name, DOWN, buff=0.15)

        groups = [
            (immov, im_name, im_ex),
            (slight, sl_name, sl_ex),
            (free, fr_name, fr_ex),
        ]
        for shape, nm, ex in groups:
            self.play(Create(shape), run_time=0.7)
            self.play(FadeIn(nm), FadeIn(ex), run_time=0.5)
            self.wait(0.2)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, immov, slight, free,
                                 im_name, sl_name, fr_name,
                                 im_ex, sl_ex, fr_ex)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  СИНОВИЈАЛНИ ЗГЛОБОВИ                            ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("synovial")
        title = section_title("Слободни — пет подвидови")
        self.play(Write(title), run_time=0.8)

        hinge = joint_card("Шарка", "колено, лакт", BLUE, UP * 1.5 + LEFT * 4.5)
        ball = joint_card("Топка", "рамо, колк", GREEN, UP * 1.5 + LEFT * 1.5)
        pivot = joint_card("Свртувачки", "врат", ORANGE, UP * 1.5 + RIGHT * 1.5)
        saddle = joint_card("Седлест", "палец", PURPLE, UP * 1.5 + RIGHT * 4.5)
        glide = joint_card("Лизгачки", "рачен зглоб", RED, DOWN * 0.5)

        for c in (hinge, ball, pivot, saddle, glide):
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.55)
            self.wait(0.15)

        self.wait(1.2)

        punch = callout("Пет видови. Различни движења.",
                        width=9.0, bg="#1a3552", border=YELLOW, font_size=30)
        punch.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(punch, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, hinge, ball, pivot, saddle, glide, punch)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  ШАРКА vs ТОПКА                                  ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hinge_vs_ball")
        title = section_title("Шарка vs Топка")
        self.play(Write(title), run_time=0.8)

        # Left: hinge joint (knee)
        h_title = Text("Шарка — колено", font_size=26, color=BLUE, weight=BOLD)
        h_title.move_to(LEFT * 3.5 + UP * 2.4)

        # Upper bone
        h_upper = Line(LEFT * 3.5 + UP * 1.7, LEFT * 3.5 + UP * 0.2,
                       color=WHITE2, stroke_width=8)
        h_pivot_pt = LEFT * 3.5 + UP * 0.2
        h_pivot_dot = Dot(h_pivot_pt, radius=0.12, color=BLUE)
        # Lower bone — will rotate
        h_lower = Line(h_pivot_pt, h_pivot_pt + DOWN * 1.6,
                       color=WHITE2, stroke_width=8)

        h_arrow_lbl = Text("напред-назад", font_size=18, color=BLUE)
        h_arrow_lbl.move_to(LEFT * 3.5 + DOWN * 2.4)

        # Right: ball-and-socket (shoulder)
        b_title = Text("Топка — рамо", font_size=26, color=GREEN, weight=BOLD)
        b_title.move_to(RIGHT * 3.5 + UP * 2.4)

        b_socket = Arc(radius=0.7, start_angle=PI, angle=PI, color=WHITE2,
                       stroke_width=3)
        b_socket.move_to(RIGHT * 3.5 + UP * 1.5)
        b_ball = Circle(radius=0.4, color=GREEN, fill_opacity=0.7, stroke_width=2)
        b_ball.move_to(RIGHT * 3.5 + UP * 1.4)

        b_arm_start = RIGHT * 3.5 + UP * 1.4
        b_arm = Line(b_arm_start, b_arm_start + DOWN * 1.6, color=WHITE2,
                     stroke_width=8)

        b_arrow_lbl = Text("во сите страни", font_size=18, color=GREEN)
        b_arrow_lbl.move_to(RIGHT * 3.5 + DOWN * 2.4)

        self.play(Write(h_title), Write(b_title), run_time=0.8)
        self.play(Create(h_upper), Create(h_lower), Create(h_pivot_dot),
                  Create(b_socket), Create(b_ball), Create(b_arm), run_time=1.0)
        self.play(FadeIn(h_arrow_lbl), FadeIn(b_arrow_lbl), run_time=0.5)
        self.wait(0.5)

        # Animate hinge — bend back and forth
        for angle in [PI / 3, -PI / 3, PI / 4, -PI / 4]:
            self.play(Rotate(h_lower, angle=angle, about_point=h_pivot_pt),
                      run_time=0.6)

        # Reset
        self.play(Rotate(h_lower, angle=PI / 6, about_point=h_pivot_pt),
                  run_time=0.3)

        # Animate ball — rotate in all directions
        self.play(Rotate(b_arm, angle=PI / 4, about_point=b_arm_start), run_time=0.6)
        self.play(Rotate(b_arm, angle=-PI / 2, about_point=b_arm_start), run_time=0.6)
        self.play(Rotate(b_arm, angle=PI / 3, about_point=b_arm_start), run_time=0.6)
        self.play(Rotate(b_arm, angle=-PI / 6, about_point=b_arm_start), run_time=0.5)

        self.wait(1.0)
        self.play(FadeOut(VGroup(title, h_title, b_title, h_upper, h_lower,
                                 h_pivot_dot, b_socket, b_ball, b_arm,
                                 h_arrow_lbl, b_arrow_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  ВНАТРЕ ВО ЗГЛОБОТ                               ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("inside_joint")
        title = section_title("Внатре во зглобот")
        self.play(Write(title), run_time=0.8)

        # Two bone ends with cartilage cushion between
        bone1 = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.5,
                                 color=WHITE2, fill_opacity=0.3, stroke_width=2)
        bone1.move_to(LEFT * 1.8 + UP * 0.3)
        bone2 = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.5,
                                 color=WHITE2, fill_opacity=0.3, stroke_width=2)
        bone2.move_to(RIGHT * 1.8 + UP * 0.3)

        # Cartilage caps
        cart1 = Arc(radius=0.55, start_angle=-PI / 2, angle=PI, color=BLUE,
                    fill_opacity=0.7, stroke_color=BLUE, stroke_width=2)
        cart1.move_to(LEFT * 0.9 + UP * 0.3)
        cart2 = Arc(radius=0.55, start_angle=PI / 2, angle=PI, color=BLUE,
                    fill_opacity=0.7, stroke_color=BLUE, stroke_width=2)
        cart2.move_to(RIGHT * 0.9 + UP * 0.3)

        # Joint capsule
        capsule = Ellipse(width=3.2, height=2.0, color=ORANGE,
                          fill_opacity=0.15, stroke_color=ORANGE, stroke_width=2)
        capsule.move_to(UP * 0.3)

        # Ligaments — lines outside capsule
        lig1 = Line(LEFT * 1.0 + UP * 1.4, RIGHT * 1.0 + UP * 1.4,
                    color=GREEN, stroke_width=4)
        lig2 = Line(LEFT * 1.0 + DOWN * 0.8, RIGHT * 1.0 + DOWN * 0.8,
                    color=GREEN, stroke_width=4)

        self.play(Create(bone1), Create(bone2), run_time=0.7)
        self.play(Create(cart1), Create(cart2), run_time=0.6)
        self.play(Create(capsule), run_time=0.5)
        self.play(Create(lig1), Create(lig2), run_time=0.5)
        self.wait(0.3)

        # Labels
        lbl_cart = Text("Рскавица — амортизер", font_size=20, color=BLUE)
        lbl_cart.move_to(DOWN * 1.7)

        lbl_caps = Text("Зглобна капсула — синовијална течност",
                        font_size=20, color=ORANGE)
        lbl_caps.move_to(DOWN * 2.2)

        lbl_lig = Text("Лигаменти — врзуваат коски", font_size=20, color=GREEN)
        lbl_lig.move_to(DOWN * 2.7)

        for lbl in (lbl_cart, lbl_caps, lbl_lig):
            self.play(FadeIn(lbl, shift=UP * 0.15), run_time=0.6)
            self.wait(0.2)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, bone1, bone2, cart1, cart2,
                                 capsule, lig1, lig2, lbl_cart, lbl_caps,
                                 lbl_lig)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ПРИМЕРИ ВО ТЕЛОТО                               ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("body_examples")
        title = section_title("Каде се наоѓаат?")
        self.play(Write(title), run_time=0.8)

        examples = VGroup(
            callout("Череп — неподвижни шевови",
                    width=10.5, bg="#1a3552", border=RED, font_size=24),
            callout("Кичма — слабо подвижни пршлени",
                    width=10.5, bg="#1a3552", border=ORANGE, font_size=24),
            callout("Рамо и колк — топчести (слободни)",
                    width=10.5, bg="#1a3552", border=GREEN, font_size=24),
            callout("Лакт и колено — шарки",
                    width=10.5, bg="#1a3552", border=BLUE, font_size=24),
            callout("Врат — свртувачки (атлас-аксис)",
                    width=10.5, bg="#1a3552", border=PURPLE, font_size=24),
        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        for ex in examples:
            self.play(FadeIn(ex, shift=UP * 0.15), run_time=0.55)
            self.wait(0.15)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, examples)), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАВРШНИЦА                                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        final = VGroup(
            Text("Зглобот спојува.", font_size=42, color=BLUE, weight=BOLD),
            Text("Зглобот дозволува.", font_size=42, color=GREEN, weight=BOLD),
            Text("Зглобот ограничува.", font_size=42, color=ORANGE, weight=BOLD),
            Text("Совршен баланс.", font_size=46, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        for line in final:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(final), run_time=0.8)
