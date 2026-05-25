"""
phys8-2-4  —  Извори на електрична енергија
Физика 8, Единица 2: Енергија

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-2-4.py Phys824Scene
Output:  media/videos/phys8-2-4/480p15/Phys824Scene.mp4
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


class Phys824Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Притискаш прекинувач. Се пали светло.",
                    font_size=40, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.4)
        self.wait(0.7)

        sub = Text("Но одкаде доаѓа струјата?",
                   font_size=34, color=WHITE2)
        sub.next_to(hook, DOWN, buff=0.4)
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.8)

        self.play(FadeOut(hook), FadeOut(sub))

        # ══════════════════════════════════════════════════════════
        # 2.  ПРИНЦИП НА ГЕНЕРАТОР — Фарадеј 1831            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("generator")

        hdr = section_title("Генераторот — Фарадеј, 1831")
        self.play(Write(hdr), run_time=0.9)

        # Coil schematic
        coil_rect = Rectangle(width=2.8, height=1.6,
                               fill_color=DARK_CARD, fill_opacity=1,
                               stroke_color=ORANGE, stroke_width=3)
        coil_rect.shift(LEFT * 2.5 + DOWN * 0.5)
        coil_lbl = Text("Намотка", font_size=22, color=ORANGE, weight=BOLD)
        coil_lbl.next_to(coil_rect, DOWN, buff=0.2)

        magnet = RoundedRectangle(width=1.0, height=2.0, corner_radius=0.15,
                                  fill_color=RED, fill_opacity=0.9,
                                  stroke_color=WHITE, stroke_width=2)
        magnet.shift(RIGHT * 1.5 + DOWN * 0.5)
        mag_lbl = Text("Магнет", font_size=22, color=RED, weight=BOLD)
        mag_lbl.next_to(magnet, DOWN, buff=0.2)

        move_arr = Arrow(magnet.get_top() + LEFT * 0.0,
                         magnet.get_top() + LEFT * 1.5,
                         color=YELLOW, buff=0, stroke_width=4)
        move_note = Text("движење →", font_size=20, color=YELLOW)
        move_note.next_to(move_arr, UP, buff=0.1)

        faraday = callout(
            "Движечки магнет покрај жица → електрична струја",
            width=10.2, bg="#0d2233", border=BLUE, font_size=24,
        )
        faraday.shift(UP * 1.8)

        self.play(FadeIn(coil_rect), Write(coil_lbl))
        self.play(FadeIn(magnet), Write(mag_lbl))
        self.play(GrowArrow(move_arr), Write(move_note))
        self.play(FadeIn(faraday, shift=DOWN * 0.25))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [
            hdr, coil_rect, coil_lbl, magnet, mag_lbl, move_arr, move_note, faraday,
        ]])

        # ══════════════════════════════════════════════════════════
        # 3.  ОБНОВЛИВИ vs НЕОБНОВЛИВИ                       ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sources")

        hdr2 = section_title("Извори на електрична енергија")
        self.play(Write(hdr2), run_time=0.9)

        ren_panel = RoundedRectangle(
            width=6.2, height=5.2, corner_radius=0.35,
            fill_color="#0b2418", fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).shift(LEFT * 3.5 + DOWN * 0.8)
        ren_title = Text("Обновливи", font_size=28, color=GREEN, weight=BOLD)
        ren_title.next_to(ren_panel.get_top(), DOWN, buff=0.35)

        ren_items = VGroup(
            Text("☀  Сончева (фотоволтаик)", font_size=22, color=WHITE2),
            Text("💧 Хидроелектрани",         font_size=22, color=WHITE2),
            Text("🌬 Ветерни турбини",         font_size=22, color=WHITE2),
            Text("🌋 Геотермална",             font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        ren_items.next_to(ren_title, DOWN, buff=0.45)

        non_panel = RoundedRectangle(
            width=6.2, height=5.2, corner_radius=0.35,
            fill_color="#2b0d0d", fill_opacity=1,
            stroke_color=RED, stroke_width=2,
        ).shift(RIGHT * 3.5 + DOWN * 0.8)
        non_title = Text("Необновливи", font_size=28, color=RED, weight=BOLD)
        non_title.next_to(non_panel.get_top(), DOWN, buff=0.35)

        non_items = VGroup(
            Text("⛏  Јагленова (топлинска)",  font_size=22, color=WHITE2),
            Text("⛽ Нафта / гас → пареа",     font_size=22, color=WHITE2),
            Text("☢  Нуклеарна (ураниум)",    font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        non_items.next_to(non_title, DOWN, buff=0.45)

        mk_note = Text("МК: главно јагленова (РЕК Битола) + хидро (Маврово)",
                       font_size=20, color=YELLOW)
        mk_note.to_edge(DOWN, buff=0.5)

        self.play(Create(ren_panel))
        self.play(Write(ren_title))
        for item in ren_items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.35)

        self.play(Create(non_panel))
        self.play(Write(non_title))
        for item in non_items:
            self.play(FadeIn(item, shift=LEFT * 0.2), run_time=0.35)

        self.play(FadeIn(mk_note, shift=UP * 0.2))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr2, ren_panel, ren_title, ren_items,
            non_panel, non_title, non_items, mk_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 4.  AC vs DC                                        ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ac_dc")

        hdr3 = section_title("AC наспроти DC")
        self.play(Write(hdr3), run_time=0.8)

        ac_box = callout(
            "AC (наизменична) — 50 Hz, електрична мрежа, за домови",
            width=10.5, bg="#0d2b44", border=BLUE, font_size=24,
        )
        ac_box.shift(UP * 1.2)
        self.play(FadeIn(ac_box, shift=DOWN * 0.2))
        self.wait(0.7)

        dc_box = callout(
            "DC (еднонасочна) — батерии, електроника, LED",
            width=10.5, bg="#0f2233", border=ORANGE, font_size=24,
        )
        dc_box.next_to(ac_box, DOWN, buff=0.45)
        self.play(FadeIn(dc_box, shift=DOWN * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hdr3), FadeOut(ac_box), FadeOut(dc_box))

        # ══════════════════════════════════════════════════════════
        # 5.  ПРЕНОС — ЗОШТО ВИСОК НАПОН?                    ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("transmission")

        hdr4 = section_title("Пренос на електрична енергија")
        self.play(Write(hdr4), run_time=0.9)

        steps_data = [
            ("Генератор",          "10 kV",    BLUE,   LEFT * 5.5),
            ("Трансформатор ↑",    "400 kV",   YELLOW, LEFT * 2.2),
            ("Далноводи",          "400 kV",   GREY,   ORIGIN + RIGHT * 0.6),
            ("Трансформатор ↓",    "220 V",    GREEN,  RIGHT * 3.5),
            ("Домаќинства",        "220 V",    ORANGE, RIGHT * 6.2),
        ]

        nodes = VGroup()
        for lbl, val, col, pos in steps_data:
            bg = RoundedRectangle(
                width=2.0, height=1.4, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            lt = Text(lbl, font_size=16, color=col, weight=BOLD)
            lt.move_to(bg).shift(UP * 0.22)
            vt = Text(val, font_size=18, color=WHITE2)
            vt.move_to(bg).shift(DOWN * 0.2)
            n = VGroup(bg, lt, vt)
            n.move_to(pos + DOWN * 0.6)
            nodes.add(n)

        arrows_t = VGroup()
        for i in range(len(nodes) - 1):
            arr = Arrow(nodes[i].get_right(), nodes[i + 1].get_left(),
                        color=GREY, buff=0.05, stroke_width=2.5,
                        max_tip_length_to_length_ratio=0.25)
            arrows_t.add(arr)

        for node, arr in zip(nodes[:-1], arrows_t):
            self.play(FadeIn(node, shift=RIGHT * 0.2), GrowArrow(arr), run_time=0.4)
        self.play(FadeIn(nodes[-1], shift=RIGHT * 0.2))

        loss_note = callout(
            "Загуба = I²R   →   висок напон = мала струја = малку загуба",
            width=10.5, bg="#0d2b44", border=RED, font_size=22,
        )
        loss_note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(loss_note, shift=UP * 0.2))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [hdr4, nodes, arrows_t, loss_note]])

        # ══════════════════════════════════════════════════════════
        # 6.  АНDONОВСКИ МОМЕНТ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Јагленот гори.",          WHITE2, 36),
            ("Пареата се дига.",         WHITE2, 36),
            ("Турбината врти.",          WHITE2, 36),
            ("Во жица — светлина.",      WHITE2, 36),
            ("Сè уште магија. Дури и денеска.", YELLOW, 38),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.36)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.42)

        self.play(Indicate(grp[-1], scale_factor=1.15, color=YELLOW))
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
            (BLUE,   "Генератор: магнет + намотка → струја (Фарадеј, 1831)"),
            (GREEN,  "Обновливи: сонце, ветер, вода, геотермала"),
            (RED,    "Необновливи: јаглен, нафта, нуклеарна"),
            (YELLOW, "Висок напон при пренос → мала загуба (I²R)"),
            (ORANGE, "МК: РЕК Битола (јаглен) + Маврово (хидро)"),
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
