"""
bio8-7-2  —  Изработка на модел на фосил
Биологија 8, Единица 7: Запис во карпите

Teaching narrative — Andonovski-style: three-beat punches,
hands as nature, classroom as lab.
Render:  manim -ql bio8-7-2.py Bio872Scene
Output:  media/videos/bio8-7-2/480p15/Bio872Scene.mp4
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


def leaf_shape(color=GREEN, scale=1.0):
    """Stylized leaf — ellipse with central vein."""
    blade = Ellipse(width=1.4, height=0.7, color=color, fill_color=color, fill_opacity=0.9, stroke_width=2)
    blade.rotate(PI / 5)
    vein = Line(blade.get_corner(DL), blade.get_corner(UR), color="#2e7d32", stroke_width=3)
    stem = Line(blade.get_corner(DL), blade.get_corner(DL) + DOWN * 0.3 + LEFT * 0.1,
                color="#5d4037", stroke_width=4)
    g = VGroup(blade, vein, stem)
    g.scale(scale)
    return g


def shell_shape(color=ORANGE, scale=1.0):
    """A scallop-like shell with radial lines."""
    body = Sector(radius=0.8, angle=PI, fill_color=color, fill_opacity=1, stroke_color="#5d4037", stroke_width=2)
    body.rotate(PI)
    # radial lines
    lines = VGroup()
    for a in np.linspace(0, PI, 7):
        end = np.array([np.cos(a + PI), np.sin(a + PI), 0]) * 0.75
        ln = Line(ORIGIN, end, color="#5d4037", stroke_width=2)
        lines.add(ln)
    g = VGroup(body, lines)
    g.scale(scale)
    return g


def clay_block(color="#8d6e63", width=3.0, height=1.0):
    """A rounded clay slab."""
    block = RoundedRectangle(
        width=width, height=height, corner_radius=0.15,
        fill_color=color, fill_opacity=1,
        stroke_color="#5d4037", stroke_width=2,
    )
    return block


class Bio872Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — Leaf in clay                              ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = VGroup(
            Text("Лист во глина.",          font_size=52, color=GREEN,  weight=BOLD),
            Text("Притисни.",               font_size=46, color=YELLOW, weight=BOLD),
            Text("Извади.",                 font_size=46, color=ORANGE, weight=BOLD),
            Text("Останува отпечаток.",     font_size=42, color=BLUE),
            Text("Тоа е фосил.",            font_size=50, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35)

        for h in hook:
            self.play(FadeIn(h, shift=UP * 0.15), run_time=0.55)
            self.wait(0.25)
        self.wait(1.0)

        finisher_hook = Text("Природата го прави со време. Ние — со прсти.",
                             font_size=30, color=PURPLE)
        finisher_hook.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher_hook), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(hook, finisher_hook)), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  WHY MAKE A MODEL                                 ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("why")

        t2 = section_title("Зошто правиме модел?", color=BLUE)
        self.play(Write(t2), run_time=0.7)

        reasons = VGroup(
            callout("Да го разбереме процесот со раце.", width=11, border=BLUE, font_size=28),
            callout("Не со зборови — со прсти, со глина, со гипс.", width=11, border=GREEN, font_size=28),
            callout("Тогаш науката се чувствува.", width=11, border=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.4).next_to(t2, DOWN, buff=0.6)

        for r in reasons:
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.6)
            self.wait(0.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t2, reasons)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  MOLD vs CAST — definitions                       ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mold-cast")

        t3 = section_title("Калап и одлеан", color=ORANGE)
        self.play(Write(t3), run_time=0.7)

        # mold
        mold_box = RoundedRectangle(
            width=5.5, height=3.2, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).move_to([-3.2, -0.3, 0])
        mold_ttl = Text("Калап (mold)", font_size=30, color=BLUE, weight=BOLD).move_to(mold_box.get_top() + DOWN * 0.4)
        mold_def = Text("Празнина во облик\nна суштеството.", font_size=22, color=WHITE2).move_to(mold_box).shift(DOWN * 0.2)
        # negative — clay with cavity
        clay = clay_block(width=3.5, height=1.2).move_to(mold_box).shift(DOWN * 1.0)
        cavity = Ellipse(width=1.0, height=0.45, color="#0d1b2e", fill_color="#0d1b2e", fill_opacity=1, stroke_width=2, stroke_color=BLUE)
        cavity.move_to(clay)

        # cast
        cast_box = RoundedRectangle(
            width=5.5, height=3.2, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=ORANGE, stroke_width=2,
        ).move_to([3.2, -0.3, 0])
        cast_ttl = Text("Одлеан (cast)", font_size=30, color=ORANGE, weight=BOLD).move_to(cast_box.get_top() + DOWN * 0.4)
        cast_def = Text("Калапот се полни.\nОстанува облик.", font_size=22, color=WHITE2).move_to(cast_box).shift(DOWN * 0.2)
        # positive — clay with shape
        clay2 = clay_block(width=3.5, height=1.2).move_to(cast_box).shift(DOWN * 1.0)
        bump = Ellipse(width=1.0, height=0.45, color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_width=2, stroke_color="#5d4037")
        bump.move_to(clay2)

        self.play(FadeIn(VGroup(mold_box, mold_ttl, mold_def, clay, cavity)), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(VGroup(cast_box, cast_ttl, cast_def, clay2, bump)), run_time=1.0)
        self.wait(1.8)

        rule = Text("Природата прави и калап и одлеан.",
                    font_size=28, color=GREEN)
        rule.to_edge(DOWN, buff=0.5)
        self.play(Write(rule), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t3, mold_box, mold_ttl, mold_def, clay, cavity,
                                 cast_box, cast_ttl, cast_def, clay2, bump, rule)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  EXPERIMENT 1 — LEAF IMPRINT IN CLAY              ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("leaf-imprint")

        t4 = section_title("Експеримент 1: Отпечаток од лист", color=GREEN)
        self.play(Write(t4), run_time=0.7)

        # стапка 1: глина
        step_lbl = Text("Чекор 1: Подготви глина", font_size=26, color=YELLOW).to_corner(UL, buff=0.6).shift(DOWN * 0.5)
        self.play(Write(step_lbl), run_time=0.6)

        clay_slab = clay_block(width=4.5, height=1.6, color="#8d6e63")
        clay_slab.move_to(DOWN * 0.5)
        self.play(FadeIn(clay_slab), run_time=0.8)
        self.wait(0.5)

        # стапка 2: лист
        step_lbl2 = Text("Чекор 2: Постави лист", font_size=26, color=YELLOW).move_to(step_lbl)
        self.play(Transform(step_lbl, step_lbl2), run_time=0.4)

        leaf = leaf_shape(color=GREEN, scale=1.2)
        leaf.next_to(clay_slab, UP, buff=1.2)
        self.play(FadeIn(leaf, shift=DOWN * 0.3), run_time=0.7)
        self.wait(0.4)

        # стапка 3: притисни
        step_lbl3 = Text("Чекор 3: Притисни нежно", font_size=26, color=YELLOW).move_to(step_lbl)
        self.play(Transform(step_lbl, step_lbl3), run_time=0.4)

        self.play(leaf.animate.move_to(clay_slab.get_center()).scale(0.95), run_time=1.2)
        self.wait(0.6)

        # стапка 4: извади
        step_lbl4 = Text("Чекор 4: Извади листот", font_size=26, color=YELLOW).move_to(step_lbl)
        self.play(Transform(step_lbl, step_lbl4), run_time=0.4)

        # imprint — leaf-shape carved in dark
        imprint = Ellipse(width=1.4 * 0.95, height=0.7 * 0.95,
                          color="#3e2723", fill_color="#3e2723", fill_opacity=1,
                          stroke_color=BLUE, stroke_width=2)
        imprint.rotate(PI / 5).move_to(clay_slab.get_center())
        vein_mark = Line(imprint.get_corner(DL), imprint.get_corner(UR),
                         color="#5d4037", stroke_width=2)
        imprint_group = VGroup(imprint, vein_mark)
        imprint_group.set_opacity(0)
        self.add(imprint_group)

        self.play(
            leaf.animate.next_to(clay_slab, UP, buff=1.2).scale(1.05),
            imprint_group.animate.set_opacity(1),
            run_time=1.2,
        )
        self.wait(0.6)

        # стапка 5: фосил
        step_lbl5 = Text("Чекор 5: Имаш модел на фосил!", font_size=26, color=GREEN, weight=BOLD).move_to(step_lbl)
        self.play(Transform(step_lbl, step_lbl5), FadeOut(leaf), run_time=0.7)
        self.wait(0.6)

        arrow = Arrow(imprint_group.get_right() + RIGHT * 0.1, imprint_group.get_right() + RIGHT * 1.5,
                      color=YELLOW, buff=0)
        arrow_lbl = Text("отпечаток", font_size=24, color=YELLOW).next_to(arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(t4, step_lbl, clay_slab, imprint_group, arrow, arrow_lbl)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  EXPERIMENT 2 — PLASTER CAST OF SHELL             ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("shell-cast")

        t5 = section_title("Експеримент 2: Гипс одлеан од школка", color=ORANGE)
        self.play(Write(t5), run_time=0.7)

        # five mini-panels in a row
        # panel 1: shell + clay
        panels = []
        panel_w = 2.4
        panel_y = 0.5
        labels_text = [
            "1. Школка во глина",
            "2. Извади школка",
            "3. Имаш калап",
            "4. Истури гипс",
            "5. Имаш одлеан",
        ]
        panel_boxes = VGroup()
        panel_labels = VGroup()
        for i, lt in enumerate(labels_text):
            x = -4.8 + i * 2.4
            box = RoundedRectangle(
                width=panel_w, height=2.0, corner_radius=0.18,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=ORANGE, stroke_width=2,
            ).move_to([x, panel_y, 0])
            lbl = Text(lt, font_size=15, color=WHITE2).next_to(box, DOWN, buff=0.15)
            panel_boxes.add(box)
            panel_labels.add(lbl)

        self.play(LaggedStart(*[FadeIn(b) for b in panel_boxes], lag_ratio=0.1), run_time=1.0)
        self.play(LaggedStart(*[Write(l) for l in panel_labels], lag_ratio=0.08), run_time=1.2)

        # panel 1: clay + shell pressed
        p1_clay = clay_block(width=1.8, height=0.5).move_to(panel_boxes[0]).shift(DOWN * 0.3)
        p1_shell = shell_shape(color=ORANGE, scale=0.7).move_to(panel_boxes[0]).shift(UP * 0.2)
        self.play(FadeIn(p1_clay), FadeIn(p1_shell), run_time=0.6)
        self.wait(0.3)

        # panel 2: shell removed, cavity remains
        p2_clay = clay_block(width=1.8, height=0.5).move_to(panel_boxes[1]).shift(DOWN * 0.3)
        p2_cav = Sector(radius=0.4, angle=PI, fill_color="#0d1b2e", fill_opacity=1,
                        stroke_color=ORANGE, stroke_width=2).rotate(PI).move_to(p2_clay)
        p2_shell_above = shell_shape(color=ORANGE, scale=0.6).move_to(panel_boxes[1]).shift(UP * 0.4)
        self.play(FadeIn(p2_clay), FadeIn(p2_cav), FadeIn(p2_shell_above), run_time=0.6)
        self.wait(0.3)

        # panel 3: just the mold (cavity)
        p3_clay = clay_block(width=1.8, height=0.5).move_to(panel_boxes[2])
        p3_cav = Sector(radius=0.4, angle=PI, fill_color="#0d1b2e", fill_opacity=1,
                        stroke_color=BLUE, stroke_width=2).rotate(PI).move_to(p3_clay)
        p3_lbl = Text("калап", font_size=16, color=BLUE).next_to(p3_clay, UP, buff=0.1)
        self.play(FadeIn(p3_clay), FadeIn(p3_cav), FadeIn(p3_lbl), run_time=0.6)
        self.wait(0.3)

        # panel 4: pouring plaster
        p4_clay = clay_block(width=1.8, height=0.5).move_to(panel_boxes[3]).shift(DOWN * 0.3)
        p4_plaster = Sector(radius=0.4, angle=PI, fill_color=WHITE2, fill_opacity=1,
                            stroke_color="#5d4037", stroke_width=1).rotate(PI).move_to(p4_clay)
        p4_drip = Triangle(color=WHITE2, fill_color=WHITE2, fill_opacity=1, stroke_width=0).scale(0.15)
        p4_drip.next_to(p4_plaster, UP, buff=0.2)
        self.play(FadeIn(p4_clay), FadeIn(p4_plaster), FadeIn(p4_drip), run_time=0.6)
        self.wait(0.3)

        # panel 5: cast removed
        p5_clay = clay_block(width=1.8, height=0.5).move_to(panel_boxes[4]).shift(DOWN * 0.3)
        p5_cast = Sector(radius=0.4, angle=PI, fill_color=WHITE2, fill_opacity=1,
                         stroke_color="#5d4037", stroke_width=2).rotate(PI).move_to(panel_boxes[4]).shift(UP * 0.2)
        p5_lbl = Text("одлеан", font_size=16, color=ORANGE).next_to(p5_cast, DOWN, buff=0.1)
        self.play(FadeIn(p5_clay), FadeIn(p5_cast), FadeIn(p5_lbl), run_time=0.6)
        self.wait(1.4)

        # caption
        cap = Text("Од школка → калап → одлеан. Како во природата.",
                   font_size=26, color=YELLOW)
        cap.to_edge(DOWN, buff=0.4)
        self.play(Write(cap), run_time=1.0)
        self.wait(1.6)

        self.play(FadeOut(VGroup(
            t5, panel_boxes, panel_labels,
            p1_clay, p1_shell, p2_clay, p2_cav, p2_shell_above,
            p3_clay, p3_cav, p3_lbl, p4_clay, p4_plaster, p4_drip,
            p5_clay, p5_cast, p5_lbl, cap,
        )), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  DOUGH FOSSIL — alternate kitchen version         ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("dough")

        t6 = section_title("Тесто-фосил: дома", color=PURPLE)
        self.play(Write(t6), run_time=0.7)

        recipe_box = RoundedRectangle(
            width=11, height=2.4, corner_radius=0.25,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=PURPLE, stroke_width=2,
        ).next_to(t6, DOWN, buff=0.5)
        recipe = VGroup(
            Text("Рецепт за тесто:", font_size=26, color=YELLOW, weight=BOLD),
            Text("2 чаши брашно + 1 чаша сол + 1 чаша вода", font_size=24, color=WHITE2),
            Text("Замеси. Стави цвет, школка или коска. Притисни.", font_size=22, color=WHITE2),
            Text("Пеци на 100°C, 2 часа. Готово.", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.15).move_to(recipe_box)

        self.play(FadeIn(recipe_box), Write(recipe), run_time=1.6)
        self.wait(2.4)

        kid_note = Text("Лесно. Безбедно. Точно.",
                        font_size=32, color=YELLOW, weight=BOLD)
        kid_note.to_edge(DOWN, buff=0.6)
        self.play(Write(kid_note), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(t6, recipe_box, recipe, kid_note)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  OUTRO — what we learned                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("outro")

        outro = VGroup(
            Text("Со прсти.",          font_size=50, color=YELLOW, weight=BOLD),
            Text("Со глина.",          font_size=50, color=ORANGE, weight=BOLD),
            Text("Со гипс.",           font_size=50, color=BLUE,   weight=BOLD),
            Text("Така прави и Земјата.", font_size=40, color=WHITE2),
            Text("Само — побавно.",    font_size=46, color=GREEN,  weight=BOLD),
        ).arrange(DOWN, buff=0.35)

        for o in outro:
            self.play(FadeIn(o, shift=UP * 0.15), run_time=0.55)
            self.wait(0.25)
        self.wait(2.0)
        self.play(FadeOut(outro), run_time=0.8)
