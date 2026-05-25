"""
phys8-2-5  —  Искористување и губење на енергија
Физика 8, Единица 2: Енергија

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-2-5.py Phys825Scene
Output:  media/videos/phys8-2-5/480p15/Phys825Scene.mp4
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


class Phys825Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Зошто светилката е толку топла?",
                    font_size=44, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.3)
        self.wait(0.7)

        ans = Text(
            "Затоа што само 5% стануваат светлина.\nОстанатото 95% е — топлина.",
            font_size=30, color=WHITE2,
        )
        ans.shift(UP * 0.3)
        self.play(FadeIn(ans, shift=UP * 0.2))
        self.wait(2.5)

        self.play(FadeOut(hook), FadeOut(ans))

        # ══════════════════════════════════════════════════════════
        # 2.  ЕФИКАСНОСТ — ДЕФИНИЦИЈА                        ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("efficiency")

        hdr = section_title("Искористеност (ефикасност)")
        self.play(Write(hdr), run_time=0.9)

        eff_box = callout(
            "η = (корисна енергија / вкупна влезна) × 100 %",
            width=10.2, bg="#0d2b44", border=YELLOW, font_size=28,
        )
        eff_box.shift(UP * 1.5)
        self.play(FadeIn(eff_box, shift=DOWN * 0.25))
        self.wait(0.8)

        second_law = callout(
            "2. закон на термодинамика: ниедна претворба не е 100%",
            width=10.5, bg="#2b0d0d", border=RED, font_size=24,
        )
        second_law.next_to(eff_box, DOWN, buff=0.45)
        self.play(FadeIn(second_law, shift=DOWN * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hdr), FadeOut(eff_box), FadeOut(second_law))

        # ══════════════════════════════════════════════════════════
        # 3.  САНКИ ДИЈАГРАМ — СВЕТИЛКИ                      ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("bulb_sankey")

        hdr2 = section_title("Санки дијаграм: светилки")
        self.play(Write(hdr2), run_time=0.8)

        def sankey_bars(title, light_pct, heat_pct, x_center, light_col, heat_col):
            total_h = 4.0
            light_h = total_h * light_pct / 100
            heat_h  = total_h * heat_pct  / 100

            bg_bar = Rectangle(width=1.2, height=total_h,
                                fill_color=DARK_CARD, fill_opacity=1,
                                stroke_color=GREY, stroke_width=1.5)
            bg_bar.move_to(np.array([x_center, -0.3, 0]))

            light_bar = Rectangle(width=1.2, height=light_h,
                                  fill_color=light_col, fill_opacity=0.9,
                                  stroke_width=0)
            light_bar.align_to(bg_bar, DOWN)
            light_bar.align_to(bg_bar, LEFT)

            heat_bar = Rectangle(width=1.2, height=heat_h,
                                 fill_color=heat_col, fill_opacity=0.9,
                                 stroke_width=0)
            heat_bar.next_to(light_bar, UP, buff=0)

            title_t = Text(title, font_size=22, color=WHITE2, weight=BOLD)
            title_t.next_to(bg_bar, UP, buff=0.25)

            lp = Text(f"{light_pct}% светлина", font_size=18, color=light_col)
            lp.next_to(bg_bar, RIGHT, buff=0.15).shift(DOWN * 0.8)
            hp = Text(f"{heat_pct}% топлина", font_size=18, color=heat_col)
            hp.next_to(bg_bar, RIGHT, buff=0.15).shift(UP * 0.4)

            return VGroup(bg_bar, light_bar, heat_bar, title_t, lp, hp)

        old_grp = sankey_bars("Стара светилка", 5,  95, -3.2, YELLOW, RED)
        led_grp = sankey_bars("LED",            80, 20,  3.2, YELLOW, ORANGE)

        vs_t = Text("vs", font_size=36, color=GREY, weight=BOLD)
        vs_t.move_to(ORIGIN + DOWN * 0.3)

        self.play(FadeIn(old_grp, shift=RIGHT * 0.3))
        self.play(FadeIn(vs_t))
        self.play(FadeIn(led_grp, shift=LEFT * 0.3))
        self.wait(2.5)

        self.play(FadeOut(hdr2), FadeOut(old_grp), FadeOut(vs_t), FadeOut(led_grp))

        # ══════════════════════════════════════════════════════════
        # 4.  АВТОМОБИЛ — ЗАГУБИ                             ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("car_losses")

        hdr3 = section_title("Автомобил: каде оди горивото?")
        self.play(Write(hdr3), run_time=0.8)

        car_data = [
            ("Кинетичка (движење)", 25, BLUE),
            ("Топлина во мотор",    60, RED),
            ("Издувни гасови",      10, GREY),
            ("Звук / триење",        5, ORANGE),
        ]

        bars = VGroup()
        x_start = -5.5
        for label, pct, col in car_data:
            bar_w = pct * 0.09
            bar = Rectangle(width=bar_w, height=0.65,
                            fill_color=col, fill_opacity=0.9, stroke_width=0)
            lbl_t = Text(f"{label}  {pct}%", font_size=20, color=col)
            bar.shift(LEFT * ((10 - bar_w) / 2 - 0.3))
            lbl_t.next_to(bar.get_right(), RIGHT, buff=0.2)
            bars.add(VGroup(bar, lbl_t))

        bars.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        bars.shift(DOWN * 0.3 + LEFT * 2.5)

        for bar in bars:
            self.play(FadeIn(bar, shift=RIGHT * 0.4), run_time=0.5)
            self.wait(0.35)

        self.wait(1.5)
        self.play(FadeOut(hdr3), FadeOut(bars))

        # ══════════════════════════════════════════════════════════
        # 5.  РЕГЕНЕРАТИВНО КОЧЕЊЕ                           ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("regen_braking")

        hdr4 = section_title("Регенеративно кочење")
        self.play(Write(hdr4), run_time=0.8)

        chain = VGroup(
            Text("Кинетичка", font_size=26, color=BLUE),
            Text("→", font_size=30, color=GREY),
            Text("Електрична", font_size=26, color=GREEN),
            Text("→", font_size=30, color=GREY),
            Text("Батерија", font_size=26, color=ORANGE),
        ).arrange(RIGHT, buff=0.35)
        chain.shift(UP * 0.8)

        self.play(FadeIn(chain, shift=DOWN * 0.2))
        self.wait(0.8)

        saving = callout(
            "Штедење: до 20% во градски сообраќај",
            width=9.0, bg="#0b2418", border=GREEN, font_size=26,
        )
        saving.next_to(chain, DOWN, buff=0.7)
        self.play(FadeIn(saving, shift=DOWN * 0.2))
        self.wait(1.5)

        tips_hdr = Text("Заштеда дома:", font_size=28, color=YELLOW, weight=BOLD)
        tips_hdr.next_to(saving, DOWN, buff=0.55)
        self.play(Write(tips_hdr))

        tips = VGroup(
            Text("изолација на ѕидови + прозорци", font_size=22, color=WHITE2),
            Text("LED сијалици", font_size=22, color=WHITE2),
            Text("уреди класа A+++", font_size=22, color=WHITE2),
            Text("не остава на standby", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        tips.next_to(tips_hdr, DOWN, buff=0.3)

        for tip in tips:
            self.play(FadeIn(tip, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(hdr4), FadeOut(chain), FadeOut(saving),
                  FadeOut(tips_hdr), FadeOut(tips))

        # ══════════════════════════════════════════════════════════
        # 6.  АНDONОВСКИ МОМЕНТ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Ниедна машина не е совршена.",  WHITE2, 36),
            ("Секогаш дел се губи.",           WHITE2, 36),
            ("Тоа е законот.",                 WHITE2, 36),
            ("Не правило.",                    WHITE2, 34),
            ("Закон.",                         YELLOW, 60),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.32)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.42)

        self.play(Indicate(grp[-1], scale_factor=1.3, color=YELLOW))
        self.wait(3.0)

        self.play(FadeOut(grp))

        # ══════════════════════════════════════════════════════════
        # 7.  РЕЗИМЕ                                          ~9 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        sum_hdr = Text("Запомни:", font_size=44, color=YELLOW, weight=BOLD)
        sum_hdr.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 0.1)
        self.play(Write(sum_hdr))

        bullets = [
            (RED,    "Ниедна претворба не е 100% — 2. закон на термодинамика"),
            (YELLOW, "Стара светилка: 5% светлина; LED: 80% светлина"),
            (BLUE,   "Автомобил: 25% кинетичка, 60% топлина"),
            (GREEN,  "Регенеративно кочење штедува до 20%"),
            (ORANGE, "Дома: изолација + LED + A+++ = голема заштеда"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=22, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.shift(DOWN * 0.65 + RIGHT * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.5)
            self.wait(0.42)

        self.wait(3.0)
