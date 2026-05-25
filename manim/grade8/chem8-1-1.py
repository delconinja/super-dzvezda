"""
chem8-1-1  —  Својства на агрегатните состојби
Хемија 8, Единица 1: Агрегатни состојби на материјата

Teaching narrative — Andonovski-style: three-beat punches,
particles as characters, не...туку contrast, one-word finishers.
Render:  manim -ql chem8-1-1.py Chem811Scene
Output:  media/videos/chem8-1-1/480p15/Chem811Scene.mp4
"""
from manim import *
import numpy as np
import random

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


def particle(pos, color=BLUE, r=0.18):
    return Circle(radius=r, fill_color=color, fill_opacity=1,
                  stroke_color=WHITE2, stroke_width=1.2).move_to(pos)


class Chem811Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Иста материја. Три лица.",
                    font_size=52, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.5)
        self.wait(0.6)

        # Three small ice/water/steam icons under hook
        ice = RoundedRectangle(width=1.4, height=1.0, corner_radius=0.1,
                               fill_color=BLUE, fill_opacity=0.8,
                               stroke_color=WHITE2, stroke_width=2)
        ice_label = Text("лед", font_size=24, color=WHITE2).next_to(ice, DOWN, buff=0.15)
        ice_g = VGroup(ice, ice_label).move_to(LEFT * 4.2 + DOWN * 0.5)

        water_drop = Circle(radius=0.5, fill_color=BLUE, fill_opacity=0.6,
                            stroke_color=WHITE2, stroke_width=2)
        water_label = Text("вода", font_size=24, color=WHITE2).next_to(water_drop, DOWN, buff=0.15)
        water_g = VGroup(water_drop, water_label).move_to(DOWN * 0.5)

        steam_dots = VGroup(*[
            Circle(radius=0.12, fill_color=GREY, fill_opacity=0.7,
                   stroke_width=0).move_to(np.array([
                random.uniform(-0.5, 0.5),
                random.uniform(-0.4, 0.4), 0]))
            for _ in range(10)
        ])
        steam_label = Text("пареа", font_size=24, color=WHITE2).next_to(steam_dots, DOWN, buff=0.15)
        steam_g = VGroup(steam_dots, steam_label).move_to(RIGHT * 4.2 + DOWN * 0.5)

        self.play(FadeIn(ice_g), run_time=0.6)
        self.play(FadeIn(water_g), run_time=0.6)
        self.play(FadeIn(steam_g), run_time=0.6)
        self.wait(0.6)

        line2 = Text("Самата вода — лед, вода, пареа.",
                     font_size=32, color=WHITE2)
        line2.next_to(hook, DOWN, buff=2.2)
        line2.shift(DOWN * 0.3)
        self.play(Write(line2), run_time=1.2)
        self.wait(0.6)

        line3 = Text("Се менува. Но не умира.",
                     font_size=36, color=GREEN, weight=BOLD)
        line3.next_to(line2, DOWN, buff=0.35)
        self.play(Write(line3), run_time=1.3)
        self.wait(1.4)

        self.play(FadeOut(VGroup(hook, ice_g, water_g, steam_g, line2, line3)))

        # ══════════════════════════════════════════════════════════
        # 2.  ДЕФИНИЦИЈА                                      ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        t2 = section_title("Што е агрегатна состојба?")
        self.play(Write(t2), run_time=1.0)

        defn = callout("Агрегатна состојба = форма во која се наоѓа материјата.",
                       width=11.5, font_size=26)
        defn.next_to(t2, DOWN, buff=0.6)
        self.play(FadeIn(defn), run_time=0.8)
        self.wait(0.5)

        three = Text("Три. Цврста. Течна. Гасовита.",
                     font_size=38, color=YELLOW, weight=BOLD)
        three.next_to(defn, DOWN, buff=0.7)
        self.play(Write(three), run_time=1.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t2, defn, three)))

        # ══════════════════════════════════════════════════════════
        # 3.  ТРИ ПОЛИЊА СО ЧЕСТИЦИ                           ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("particle_boxes")

        t3 = section_title("Како се распоредени честиците?")
        self.play(Write(t3), run_time=0.9)

        # Three boxes
        def make_box(label_text, color, pos):
            box = RoundedRectangle(width=3.6, height=3.0, corner_radius=0.2,
                                   fill_color=DARK_CARD, fill_opacity=1,
                                   stroke_color=color, stroke_width=3).move_to(pos)
            lbl = Text(label_text, font_size=26, color=color, weight=BOLD)
            lbl.next_to(box, UP, buff=0.2)
            return box, lbl

        solid_box, solid_lbl = make_box("Цврста", BLUE, LEFT * 4.6 + DOWN * 0.4)
        liq_box, liq_lbl = make_box("Течна", GREEN, DOWN * 0.4)
        gas_box, gas_lbl = make_box("Гасовита", ORANGE, RIGHT * 4.6 + DOWN * 0.4)

        self.play(
            FadeIn(VGroup(solid_box, solid_lbl)),
            FadeIn(VGroup(liq_box, liq_lbl)),
            FadeIn(VGroup(gas_box, gas_lbl)),
            run_time=0.9,
        )

        # SOLID: regular lattice
        solid_particles = VGroup()
        for i in range(4):
            for j in range(4):
                p = particle(
                    solid_box.get_center() + np.array([-1.2 + j * 0.8, -1.0 + i * 0.66, 0]),
                    color=BLUE, r=0.16,
                )
                solid_particles.add(p)

        # LIQUID: closer packed but irregular
        liq_particles = VGroup()
        random.seed(7)
        for _ in range(14):
            p = particle(
                liq_box.get_center() + np.array([
                    random.uniform(-1.3, 1.3),
                    random.uniform(-1.2, 1.0), 0]),
                color=GREEN, r=0.18,
            )
            liq_particles.add(p)

        # GAS: scattered
        gas_particles = VGroup()
        for _ in range(8):
            p = particle(
                gas_box.get_center() + np.array([
                    random.uniform(-1.5, 1.5),
                    random.uniform(-1.3, 1.2), 0]),
                color=ORANGE, r=0.16,
            )
            gas_particles.add(p)

        self.play(
            LaggedStartMap(FadeIn, solid_particles, lag_ratio=0.04),
            LaggedStartMap(FadeIn, liq_particles, lag_ratio=0.04),
            LaggedStartMap(FadeIn, gas_particles, lag_ratio=0.06),
            run_time=1.8,
        )
        self.wait(0.5)

        # Movement annotations under each box
        cap_s = Text("Вибрираат на место.", font_size=20, color=WHITE2)
        cap_s.next_to(solid_box, DOWN, buff=0.2)
        cap_l = Text("Лизгаат. Течат.", font_size=20, color=WHITE2)
        cap_l.next_to(liq_box, DOWN, buff=0.2)
        cap_g = Text("Летаат. Слободни.", font_size=20, color=WHITE2)
        cap_g.next_to(gas_box, DOWN, buff=0.2)

        self.play(Write(cap_s), Write(cap_l), Write(cap_g), run_time=1.0)

        # Tiny jiggle for solid particles
        solid_jiggle_anims = []
        for p in solid_particles:
            dx = random.uniform(-0.05, 0.05)
            dy = random.uniform(-0.05, 0.05)
            solid_jiggle_anims.append(p.animate.shift(np.array([dx, dy, 0])))
        # Liquid: medium shifts
        liq_anims = []
        for p in liq_particles:
            dx = random.uniform(-0.25, 0.25)
            dy = random.uniform(-0.25, 0.25)
            liq_anims.append(p.animate.shift(np.array([dx, dy, 0])))
        # Gas: big shifts
        gas_anims = []
        for p in gas_particles:
            dx = random.uniform(-0.7, 0.7)
            dy = random.uniform(-0.6, 0.6)
            gas_anims.append(p.animate.shift(np.array([dx, dy, 0])))

        self.play(*solid_jiggle_anims, *liq_anims, *gas_anims, run_time=1.5)
        self.wait(0.8)

        punch = Text("Цврсти стојат. Течните одат. Гасните летаат.",
                     font_size=28, color=YELLOW, weight=BOLD)
        punch.to_edge(DOWN, buff=0.3)
        self.play(Write(punch), run_time=1.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            t3, solid_box, solid_lbl, liq_box, liq_lbl, gas_box, gas_lbl,
            solid_particles, liq_particles, gas_particles,
            cap_s, cap_l, cap_g, punch,
        )))

        # ══════════════════════════════════════════════════════════
        # 4.  ТАБЕЛА НА СВОЈСТВА                              ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("properties_table")

        t4 = section_title("Споредба на својствата")
        self.play(Write(t4), run_time=0.9)

        # Manual table
        rows = [
            ["Својство", "Цврста", "Течна", "Гасовита"],
            ["Облик", "сопствен", "на садот", "на садот"],
            ["Обем", "сопствен", "сопствен", "се шири"],
            ["Густина", "висока", "средна", "мала"],
            ["Компресибилност", "не", "малку", "многу"],
        ]
        col_x = [-5.2, -1.6, 1.4, 4.4]
        col_color = [WHITE2, BLUE, GREEN, ORANGE]
        row_y_start = 1.8
        row_dy = 0.65

        table_group = VGroup()
        for ri, row in enumerate(rows):
            for ci, cell in enumerate(row):
                if ri == 0:
                    txt = Text(cell, font_size=22, color=col_color[ci], weight=BOLD)
                else:
                    txt = Text(cell, font_size=20, color=WHITE2 if ci == 0 else col_color[ci])
                txt.move_to(np.array([col_x[ci], row_y_start - ri * row_dy, 0]))
                table_group.add(txt)

        # Header underline
        hdr_line = Line(
            np.array([-6.2, row_y_start - 0.32, 0]),
            np.array([5.6, row_y_start - 0.32, 0]),
            color=GREY, stroke_width=1.5,
        )
        table_group.add(hdr_line)

        self.play(FadeIn(table_group), run_time=1.5)
        self.wait(2.0)

        contrast = Text("Не само облик. Не само обем. Туку и однесување.",
                        font_size=26, color=YELLOW)
        contrast.to_edge(DOWN, buff=0.45)
        self.play(Write(contrast), run_time=1.6)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t4, table_group, contrast)))

        # ══════════════════════════════════════════════════════════
        # 5.  КИНЕТИЧКА ТЕОРИЈА                               ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("kinetic_theory")

        t5 = section_title("Кинетичка теорија на материјата")
        self.play(Write(t5), run_time=0.9)

        line_a = Text("Атом не молчи.", font_size=36, color=WHITE2, weight=BOLD)
        line_b = Text("Атом вибрира.", font_size=36, color=BLUE, weight=BOLD)
        line_c = Text("Дури и при −273°C.", font_size=30, color=YELLOW)
        line_d = Text("Никогаш не запира.", font_size=36, color=GREEN, weight=BOLD)

        lines = VGroup(line_a, line_b, line_c, line_d).arrange(DOWN, buff=0.35)
        lines.move_to(ORIGIN + DOWN * 0.2)

        for ln in lines:
            self.play(Write(ln), run_time=0.7)
            self.wait(0.2)
        self.wait(1.2)

        self.play(FadeOut(VGroup(t5, lines)))

        # Postulates
        t5b = section_title("Четири поставки")
        self.play(Write(t5b), run_time=0.8)

        postulates = [
            ("1.", "Материјата = честици"),
            ("2.", "Честиците секогаш се движат"),
            ("3.", "Брзината зависи од температура"),
            ("4.", "Привлечноста ги држи заедно"),
        ]
        post_group = VGroup()
        for i, (num, txt) in enumerate(postulates):
            n = Text(num, font_size=28, color=YELLOW, weight=BOLD)
            t = Text(txt, font_size=26, color=WHITE2)
            row = VGroup(n, t).arrange(RIGHT, buff=0.3)
            row.move_to(np.array([0, 1.6 - i * 0.85, 0]))
            post_group.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t5b, post_group)))

        # ══════════════════════════════════════════════════════════
        # 6.  ПЛАЗМА — ЧЕТВРТА СОСТОЈБА                       ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("plasma")

        t6 = section_title("А има и четврта", color=PURPLE)
        self.play(Write(t6), run_time=0.8)

        plasma_word = Text("Плазма.", font_size=64, color=PURPLE, weight=BOLD)
        plasma_word.move_to(UP * 1.2)
        self.play(Write(plasma_word), run_time=1.0)

        plasma_def = callout("Јонизиран гас — атомите ги губат електроните.",
                             width=10.5, font_size=24, border=PURPLE)
        plasma_def.next_to(plasma_word, DOWN, buff=0.5)
        self.play(FadeIn(plasma_def), run_time=0.7)

        examples = Text("Сонце. Ѕвезди. Северна светлина. Молња.",
                        font_size=28, color=YELLOW)
        examples.next_to(plasma_def, DOWN, buff=0.45)
        self.play(Write(examples), run_time=1.4)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t6, plasma_word, plasma_def, examples)))

        # ══════════════════════════════════════════════════════════
        # 7.  SUMMARY                                          ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        t7 = section_title("Запомни", color=GREEN)
        self.play(Write(t7), run_time=0.8)

        bullets = [
            (BLUE,   "Цврста: сопствен облик и обем"),
            (GREEN,  "Течна: облик на садот, сопствен обем"),
            (ORANGE, "Гас: облик и обем на садот"),
            (PURPLE, "Плазма: јонизиран гас, Сонце"),
            (YELLOW, "Температура диктира сè"),
        ]
        bg = VGroup()
        for i, (c, txt) in enumerate(bullets):
            dot = Dot(color=c, radius=0.12)
            t = Text(txt, font_size=24, color=WHITE2)
            row = VGroup(dot, t).arrange(RIGHT, buff=0.3)
            row.move_to(np.array([0, 1.6 - i * 0.75, 0]))
            bg.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.45)

        self.wait(2.0)

        final = Text("Една материја. Многу лица.",
                     font_size=34, color=YELLOW, weight=BOLD)
        final.to_edge(DOWN, buff=0.4)
        self.play(Write(final), run_time=1.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(t7, bg, final)))
        self.wait(0.4)
