"""
phys8-2-1  —  Облици на енергија
Физика 8, Единица 2: Енергија

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-2-1.py Phys821Scene
Output:  media/videos/phys8-2-1/480p15/Phys821Scene.mp4
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


class Phys821Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — Енергијата е насекаде               ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Зошто топката се движи откако ја удриш?",
                    font_size=40, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.5)
        self.wait(0.8)

        ans1 = Text("Не случајно.", font_size=36, color=WHITE2, weight=BOLD)
        ans2 = Text("Не сама.", font_size=36, color=WHITE2, weight=BOLD)
        ans3 = Text("Туку со енергија.", font_size=42, color=YELLOW, weight=BOLD)
        ans1.shift(UP * 0.6)
        ans2.next_to(ans1, RIGHT, buff=0.6)
        ans3.shift(DOWN * 0.2)

        self.play(FadeIn(ans1, shift=UP * 0.2))
        self.wait(0.4)
        self.play(FadeIn(ans2, shift=UP * 0.2))
        self.wait(0.4)
        self.play(Write(ans3))
        self.play(Indicate(ans3, scale_factor=1.15, color=YELLOW))
        self.wait(1.8)

        self.play(*[FadeOut(m) for m in [hook, ans1, ans2, ans3]])

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                     ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        big = Text("ЕНЕРГИЈА", font_size=90, color=YELLOW, weight=BOLD)
        self.play(Write(big), run_time=1.0)
        self.play(Wiggle(big, scale_value=1.12, n_wiggles=2))
        self.wait(0.3)
        self.play(big.animate.scale(0.38).to_corner(UL).shift(RIGHT * 0.25 + DOWN * 0.1))

        defn = callout(
            "Енергија = способност да се изврши работа",
            width=9.6, bg="#0d2b44", border=YELLOW, font_size=30,
        )
        defn.shift(UP * 1.4)
        self.play(FadeIn(defn, shift=DOWN * 0.3))
        self.wait(0.8)

        unit = callout(
            "Единица:  Џул  (J)  =  N · m  =  kg · m² / s²",
            width=9.6, bg="#0f2233", border=BLUE, font_size=27,
        )
        unit.next_to(defn, DOWN, buff=0.55)
        self.play(FadeIn(unit, shift=DOWN * 0.3))
        self.wait(1.8)

        self.play(FadeOut(big), FadeOut(defn), FadeOut(unit))

        # ══════════════════════════════════════════════════════════
        # 3.  ДЕСЕТ ОБЛИЦИ — МРЕЖА 4×3                      ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("forms")

        hdr = section_title("Десет облици на енергија")
        self.play(Write(hdr), run_time=1.0)
        self.wait(0.5)

        forms = [
            ("Кинетичка",       "Eₖ = ½mv²",          BLUE),
            ("Потенцијална",    "Eₚ = mgh",            GREEN),
            ("Топлинска",       "молекуларна вибр.",   RED),
            ("Светлосна",       "фотони, бранови",     YELLOW),
            ("Звучна",          "вибрации на воздух",  ORANGE),
            ("Електрична",      "движење на наелект.", PURPLE),
            ("Хемиска",         "хем. врски",          GREEN),
            ("Нуклеарна",       "јадрото на атомот",   RED),
            ("Магнетна",        "магнетно поле",       BLUE),
            ("Еластична",       "деформиран предмет",  ORANGE),
        ]

        cards = VGroup()
        for name, detail, col in forms:
            bg = RoundedRectangle(
                width=4.4, height=1.1, corner_radius=0.22,
                fill_color=f"{col}18", fill_opacity=1,
                stroke_color=col, stroke_width=1.6,
            )
            name_t = Text(name, font_size=22, color=col, weight=BOLD)
            name_t.next_to(bg.get_top(), DOWN, buff=0.18)
            detail_t = Text(detail, font_size=17, color=GREY)
            detail_t.next_to(name_t, DOWN, buff=0.08)
            cards.add(VGroup(bg, name_t, detail_t))

        # arrange in 2 columns of 5
        col_a = VGroup(*cards[:5]).arrange(DOWN, buff=0.22)
        col_b = VGroup(*cards[5:]).arrange(DOWN, buff=0.22)
        col_a.shift(LEFT * 3.2 + DOWN * 0.5)
        col_b.shift(RIGHT * 2.0 + DOWN * 0.5)

        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=RIGHT * 0.3 if i < 5 else LEFT * 0.3),
                      run_time=0.3)
        self.wait(2.5)

        self.play(FadeOut(hdr), FadeOut(col_a), FadeOut(col_b))

        # ══════════════════════════════════════════════════════════
        # 4.  НИШАЛОТО — ПРЕТВОРАЊЕ НА ЕНЕРГИЈА            ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pendulum")

        hdr2 = section_title("Претворање: нишало")
        self.play(Write(hdr2), run_time=0.9)

        pivot = np.array([0.0, 2.2, 0.0])
        pivot_dot = Dot(pivot, color=GREY, radius=0.12)

        def pendulum_pos(angle_deg):
            a = np.radians(angle_deg)
            return pivot + np.array([2.5 * np.sin(a), -2.5 * np.cos(a), 0.0])

        left_pos  = pendulum_pos(-38)
        mid_pos   = pendulum_pos(0)
        right_pos = pendulum_pos(38)

        bob = Circle(radius=0.28, fill_color=ORANGE, fill_opacity=1,
                     stroke_color=WHITE, stroke_width=2)
        bob.move_to(left_pos)
        rod = Line(pivot, left_pos, color=GREY, stroke_width=3)

        self.play(FadeIn(pivot_dot), FadeIn(bob), Create(rod))

        ep_lbl = Text("Eₚ = max", font_size=26, color=GREEN, weight=BOLD)
        ek_lbl = Text("Eₖ = 0",   font_size=26, color=BLUE,  weight=BOLD)
        ep_lbl.next_to(bob, DOWN, buff=0.22)
        ek_lbl.next_to(ep_lbl, RIGHT, buff=0.4)
        self.play(Write(ep_lbl), Write(ek_lbl))
        self.wait(1.0)

        # swing to bottom
        self.play(
            bob.animate.move_to(mid_pos),
            rod.animate.put_start_and_end_on(pivot, mid_pos),
            run_time=0.9, rate_func=rush_into,
        )
        self.play(FadeOut(ep_lbl), FadeOut(ek_lbl))
        ep_lbl2 = Text("Eₚ = 0",   font_size=26, color=GREEN, weight=BOLD)
        ek_lbl2 = Text("Eₖ = max", font_size=26, color=BLUE,  weight=BOLD)
        ep_lbl2.next_to(bob, DOWN, buff=0.22)
        ek_lbl2.next_to(ep_lbl2, RIGHT, buff=0.4)
        self.play(Write(ep_lbl2), Write(ek_lbl2))
        self.wait(1.0)

        # swing to right
        self.play(
            bob.animate.move_to(right_pos),
            rod.animate.put_start_and_end_on(pivot, right_pos),
            run_time=0.9, rate_func=rush_from,
        )
        self.play(FadeOut(ep_lbl2), FadeOut(ek_lbl2))
        ep_lbl3 = Text("Eₚ = max", font_size=26, color=GREEN, weight=BOLD)
        ek_lbl3 = Text("Eₖ = 0",   font_size=26, color=BLUE,  weight=BOLD)
        ep_lbl3.next_to(bob, DOWN, buff=0.22)
        ek_lbl3.next_to(ep_lbl3, RIGHT, buff=0.4)
        self.play(Write(ep_lbl3), Write(ek_lbl3))

        sound_note = Text("...и звук кога ќе удри!", font_size=24, color=ORANGE)
        sound_note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sound_note, shift=UP * 0.2))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [
            hdr2, pivot_dot, bob, rod, ep_lbl3, ek_lbl3, sound_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 5.  ФОРМУЛИ И ПРЕСМЕТКИ                           ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("formulas")

        hdr3 = section_title("Пресметки")
        self.play(Write(hdr3), run_time=0.8)

        ep_box = callout("Eₚ = m · g · h    →    3 kg × 10 m/s² × 5 m = 150 J",
                         width=10.2, bg="#0b2418", border=GREEN, font_size=26)
        ep_box.shift(UP * 1.2)
        self.play(FadeIn(ep_box, shift=DOWN * 0.2))
        self.wait(1.0)

        ek_box = callout("Eₖ = ½ · m · v²   →    ½ × 2 kg × (5 m/s)² = 25 J",
                         width=10.2, bg="#0d2344", border=BLUE, font_size=26)
        ek_box.next_to(ep_box, DOWN, buff=0.5)
        self.play(FadeIn(ek_box, shift=DOWN * 0.2))
        self.wait(1.2)

        note = Text(
            "Еднаш научена — истата формула важи насекаде во вселената.",
            font_size=24, color=GREY,
        )
        note.to_edge(DOWN, buff=1.0)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hdr3), FadeOut(ep_box), FadeOut(ek_box), FadeOut(note))

        # ══════════════════════════════════════════════════════════
        # 6.  ЗАКОН ЗА ЗАЧУВУВАЊЕ                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("conservation")

        big2 = Text("Закон за зачувување на енергијата",
                    font_size=36, color=YELLOW, weight=BOLD)
        big2.to_edge(UP, buff=0.55)
        self.play(Write(big2), run_time=1.2)

        law_box = callout(
            "Не се создава. Туку се претвора.",
            width=8.5, bg="#0d2b44", border=YELLOW, font_size=34,
        )
        law_box.shift(UP * 0.8)
        self.play(FadeIn(law_box, shift=DOWN * 0.3))
        self.play(Indicate(law_box, scale_factor=1.06, color=YELLOW))
        self.wait(1.0)

        full_law = Text(
            "Вкупната енергија во изолиран систем — секогаш иста.",
            font_size=26, color=WHITE2,
        )
        full_law.next_to(law_box, DOWN, buff=0.55)
        self.play(FadeIn(full_law, shift=UP * 0.2))
        self.wait(1.0)

        # Andonovski moment
        ando1 = Text("Енергијата не умира.", font_size=34, color=WHITE2, weight=BOLD)
        ando2 = Text("Само се преселува.", font_size=34, color=WHITE2, weight=BOLD)
        ando3 = Text("Од форма во форма.", font_size=34, color=WHITE2, weight=BOLD)
        ando4 = Text("Засекогаш.", font_size=42, color=YELLOW, weight=BOLD)

        ando_grp = VGroup(ando1, ando2, ando3, ando4).arrange(DOWN, buff=0.32)
        ando_grp.to_edge(DOWN, buff=0.55)

        self.play(FadeOut(big2), FadeOut(law_box), FadeOut(full_law))
        for line in ando_grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.6)
            self.wait(0.5)
        self.play(Indicate(ando4, scale_factor=1.3, color=YELLOW))
        self.wait(3.0)

        self.play(FadeOut(ando_grp))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                         ~9 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=44, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        bullets = [
            (YELLOW, "Енергија = способност за работа, единица J"),
            (BLUE,   "Кинетичка: Eₖ = ½mv²"),
            (GREEN,  "Потенцијална: Eₚ = mgh"),
            (ORANGE, "10 облици — сите меѓусебно претворливи"),
            (RED,    "Закон: не се создава, не се уништува"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=26, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.shift(DOWN * 0.65 + RIGHT * 0.4)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.5)
            self.wait(0.45)

        self.wait(3.0)
