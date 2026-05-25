"""
bio8-6-2  —  Подредување на рбетници
Биологија 8, Единица 6: Класификација

Teaching narrative — Andonovski-style: five classes, same spine,
different stories. Animals as characters with destinies.
Render:  manim -ql bio8-6-2.py Bio862Scene
Output:  media/videos/bio8-6-2/480p15/Bio862Scene.mp4
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


class Bio862Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — five classes, one spine                  ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Пет класи.",
                     font_size=54, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.0)
        self.wait(0.3)

        beats = VGroup(
            Text("Иста основа — 'рбет.",         font_size=40, color=GREEN, weight=BOLD),
            Text("Но различни приказни.",         font_size=38, color=WHITE2),
            Text("Риба плива.",                   font_size=36, color=BLUE, weight=BOLD),
            Text("Птица лета.",                   font_size=36, color=ORANGE, weight=BOLD),
            Text("Цицач гради дом.",              font_size=36, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.4).next_to(hook1, DOWN, buff=0.6)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  WHAT IS A VERTEBRATE                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Рбетници")
        self.play(Write(title), run_time=0.8)

        # Draw simplified spine
        spine_dots = VGroup()
        for i in range(9):
            d = Circle(radius=0.22, color=WHITE2,
                       fill_color=BLUE, fill_opacity=0.85, stroke_width=2)
            d.move_to(np.array([-3.5 + i * 0.9, 0.5, 0]))
            spine_dots.add(d)

        spine_label = Text("'Рбетен столб", font_size=28, color=BLUE, weight=BOLD)
        spine_label.next_to(spine_dots, UP, buff=0.4)

        self.play(Write(spine_label), run_time=0.7)
        for d in spine_dots:
            self.play(FadeIn(d, scale=0.5), run_time=0.18)
        self.wait(0.7)

        defn = callout("Животни со внатрешен скелет и 'рбетен столб.",
                       width=11.5, border=BLUE, font_size=28)
        defn.next_to(spine_dots, DOWN, buff=1.0)
        self.play(FadeIn(defn), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, spine_label, spine_dots, defn)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  FISH — gills, scales, water                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("fish")

        title2 = section_title("Риби", color=BLUE)
        self.play(Write(title2), run_time=0.8)

        # Simple fish drawing
        fish_body = Ellipse(width=3.0, height=1.4, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.7, stroke_width=3)
        tail = Polygon(
            np.array([1.5, 0, 0]),
            np.array([2.4, 0.7, 0]),
            np.array([2.4, -0.7, 0]),
            color=BLUE, fill_color=BLUE, fill_opacity=0.7, stroke_width=3,
        )
        eye = Dot(point=np.array([-0.9, 0.25, 0]), radius=0.12, color=WHITE2)
        gill = Line(start=np.array([-0.5, 0.4, 0]),
                    end=np.array([-0.5, -0.4, 0]),
                    color=RED, stroke_width=3)
        fish = VGroup(fish_body, tail, eye, gill).shift(LEFT * 3)

        self.play(Create(fish), run_time=1.2)
        self.wait(0.4)

        features = VGroup(
            Text("• Жабри — дишат под вода", font_size=24, color=GREEN),
            Text("• Лушпи — заштитна обвивка", font_size=24, color=GREEN),
            Text("• Студенокрвни", font_size=24, color=BLUE),
            Text("• Несат икра во вода", font_size=24, color=YELLOW),
            Text("Пример: пастрмка, шаран", font_size=22, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features.next_to(fish, RIGHT, buff=0.8)

        for f in features:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title2, fish, features)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  AMPHIBIANS — two worlds                          ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("amphibians")

        title3 = section_title("Водоземци", color=GREEN)
        self.play(Write(title3), run_time=0.8)

        # Frog silhouette
        frog_body = Ellipse(width=2.0, height=1.4, color=GREEN,
                            fill_color=GREEN, fill_opacity=0.7, stroke_width=3)
        eye_l = Dot(point=np.array([-0.4, 0.6, 0]), radius=0.18, color=WHITE2)
        eye_r = Dot(point=np.array([0.4, 0.6, 0]), radius=0.18, color=WHITE2)
        pupil_l = Dot(point=np.array([-0.4, 0.6, 0]), radius=0.08, color="#0d1b2e")
        pupil_r = Dot(point=np.array([0.4, 0.6, 0]), radius=0.08, color="#0d1b2e")
        leg1 = Line(np.array([-0.9, -0.3, 0]), np.array([-1.5, -1.0, 0]),
                    color=GREEN, stroke_width=4)
        leg2 = Line(np.array([0.9, -0.3, 0]), np.array([1.5, -1.0, 0]),
                    color=GREEN, stroke_width=4)
        frog = VGroup(frog_body, leg1, leg2, eye_l, eye_r, pupil_l, pupil_r)
        frog.shift(LEFT * 3.5)

        self.play(Create(frog), run_time=1.2)
        self.wait(0.3)

        features3 = VGroup(
            Text("• Млади во вода (полноглавци)", font_size=23, color=BLUE),
            Text("• Возрасни на копно", font_size=23, color=ORANGE),
            Text("• Влажна кожа — дише низ неа", font_size=23, color=GREEN),
            Text("• Студенокрвни", font_size=23, color=BLUE),
            Text("Пример: жаба, дождовник", font_size=22, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features3.next_to(frog, RIGHT, buff=0.7)

        for f in features3:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.0)

        punch = Text("Два света. Една кожа.",
                     font_size=30, color=PURPLE, weight=BOLD)
        punch.to_edge(DOWN, buff=0.5)
        self.play(Write(punch), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title3, frog, features3, punch)),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  REPTILES — scales on land                       ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("reptiles")

        title4 = section_title("Влекачи", color=ORANGE)
        self.play(Write(title4), run_time=0.8)

        # Lizard silhouette
        liz_body = Ellipse(width=3.4, height=0.7, color=ORANGE,
                           fill_color=ORANGE, fill_opacity=0.7, stroke_width=3)
        liz_head = Ellipse(width=1.0, height=0.6, color=ORANGE,
                           fill_color=ORANGE, fill_opacity=0.7, stroke_width=3)
        liz_head.next_to(liz_body, LEFT, buff=-0.2)
        liz_tail = Polygon(
            np.array([1.7, 0.2, 0]),
            np.array([3.0, 0.0, 0]),
            np.array([1.7, -0.2, 0]),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.7, stroke_width=3,
        )
        leg_a = Line(np.array([-0.8, -0.3, 0]), np.array([-1.2, -0.9, 0]),
                     color=ORANGE, stroke_width=4)
        leg_b = Line(np.array([0.8, -0.3, 0]), np.array([1.2, -0.9, 0]),
                     color=ORANGE, stroke_width=4)
        lizard = VGroup(liz_body, liz_head, liz_tail, leg_a, leg_b).shift(LEFT * 3)

        self.play(Create(lizard), run_time=1.2)
        self.wait(0.3)

        features4 = VGroup(
            Text("• Сува кожа со лушпи", font_size=23, color=YELLOW),
            Text("• Несат јајца на копно", font_size=23, color=GREEN),
            Text("• Студенокрвни — се грејат на сонце", font_size=23, color=RED),
            Text("• Бели дробови", font_size=23, color=BLUE),
            Text("Пример: гуштер, змија, желка", font_size=22, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features4.next_to(lizard, RIGHT, buff=0.7)

        for f in features4:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title4, lizard, features4)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  BIRDS — feathers and warmth                     ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("birds")

        title5 = section_title("Птици", color=YELLOW)
        self.play(Write(title5), run_time=0.8)

        # Bird silhouette
        bird_body = Ellipse(width=2.2, height=1.4, color=YELLOW,
                            fill_color=YELLOW, fill_opacity=0.7, stroke_width=3)
        wing = Polygon(
            np.array([0.2, 0.3, 0]),
            np.array([1.4, 0.9, 0]),
            np.array([0.9, 0.0, 0]),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.85, stroke_width=2,
        )
        beak = Polygon(
            np.array([-1.1, 0.2, 0]),
            np.array([-1.6, 0.0, 0]),
            np.array([-1.1, -0.1, 0]),
            color=ORANGE, fill_color=ORANGE, fill_opacity=1, stroke_width=2,
        )
        bird_eye = Dot(point=np.array([-0.8, 0.35, 0]), radius=0.1, color="#0d1b2e")
        bird = VGroup(bird_body, wing, beak, bird_eye).shift(LEFT * 3.5)

        self.play(Create(bird), run_time=1.2)
        self.wait(0.3)

        features5 = VGroup(
            Text("• Перја — топлина и лет", font_size=23, color=YELLOW),
            Text("• Топлокрвни", font_size=23, color=RED),
            Text("• Шупливи коски — полесни", font_size=23, color=BLUE),
            Text("• Несат јајца со тврда лушпа", font_size=23, color=GREEN),
            Text("Пример: орел, ласта, кокошка", font_size=22, color=ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features5.next_to(bird, RIGHT, buff=0.7)

        for f in features5:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title5, bird, features5)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  MAMMALS — fur, milk, family                     ~32 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mammals")

        title6 = section_title("Цицачи", color=PURPLE)
        self.play(Write(title6), run_time=0.8)

        # Generic mammal (dog-like)
        m_body = Ellipse(width=2.8, height=1.3, color=PURPLE,
                         fill_color=PURPLE, fill_opacity=0.7, stroke_width=3)
        m_head = Circle(radius=0.7, color=PURPLE,
                        fill_color=PURPLE, fill_opacity=0.7, stroke_width=3)
        m_head.next_to(m_body, LEFT, buff=-0.3).shift(UP * 0.2)
        ear_l = Polygon(
            np.array([-1.9, 0.7, 0]),
            np.array([-1.6, 1.2, 0]),
            np.array([-1.4, 0.6, 0]),
            color=PURPLE, fill_color=PURPLE, fill_opacity=0.85, stroke_width=2,
        )
        leg_aa = Line(np.array([-0.6, -0.6, 0]), np.array([-0.6, -1.3, 0]),
                      color=PURPLE, stroke_width=5)
        leg_bb = Line(np.array([0.7, -0.6, 0]), np.array([0.7, -1.3, 0]),
                      color=PURPLE, stroke_width=5)
        m_eye = Dot(point=np.array([-1.9, 0.3, 0]), radius=0.09, color="#0d1b2e")
        mammal = VGroup(m_body, m_head, ear_l, leg_aa, leg_bb, m_eye).shift(LEFT * 3)

        self.play(Create(mammal), run_time=1.3)
        self.wait(0.3)

        features6 = VGroup(
            Text("• Влакна (крзно) — топлина", font_size=23, color=ORANGE),
            Text("• Млечни жлезди — храна за младите", font_size=23, color=YELLOW),
            Text("• Топлокрвни", font_size=23, color=RED),
            Text("• Раѓаат живи младенци", font_size=23, color=GREEN),
            Text("Пример: човек, волк, кит, лилјак", font_size=22, color=PURPLE, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        features6.next_to(mammal, RIGHT, buff=0.7)

        for f in features6:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title6, mammal, features6)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 8.  CLOSE — one-word finisher                        ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        close1 = Text("Пет класи.",
                      font_size=46, color=BLUE, weight=BOLD)
        close2 = Text("Едно семејство.",
                      font_size=42, color=GREEN, weight=BOLD)
        close3 = Text("Сите со 'рбет —",
                      font_size=38, color=ORANGE)
        close4 = Text("роднини.",
                      font_size=72, color=YELLOW, weight=BOLD)
        cg = VGroup(close1, close2, close3, close4).arrange(DOWN, buff=0.5)

        for line in cg:
            self.play(Write(line), run_time=0.9)
            self.wait(0.35)
        self.wait(2.0)

        self.play(FadeOut(cg), run_time=1.0)
        self.wait(0.5)
