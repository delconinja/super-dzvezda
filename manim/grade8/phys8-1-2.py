from manim import *
import numpy as np

config.background_color = "#0d1b2e"
BLUE   = "#4fc3f7"
YELLOW = "#ffd54f"
GREEN  = "#81c784"
RED    = "#e57373"
GREY   = "#90a4ae"
ORANGE = "#ffb74d"
PURPLE = "#ce93d8"
WHITE2 = "#e8eaf0"
DARK_CARD = "#0f2233"


def callout(text, width=9.0, bg="#0d2b44", border=BLUE, font_size=28):
    box = RoundedRectangle(width=width, height=1.4, corner_radius=0.3,
        fill_color=bg, fill_opacity=1, stroke_color=border, stroke_width=2)
    label = Text(text, font_size=font_size, color=WHITE2)
    label.move_to(box)
    return VGroup(box, label)


def section_title(text, color=YELLOW):
    t = Text(text, font_size=44, color=color, weight=BOLD)
    t.to_edge(UP, buff=0.45)
    return t


class Phys812Scene(Scene):
    def construct(self):
        self.hook()
        self.deformation_types()
        self.hookes_law()
        self.worked_example()
        self.real_world()
        self.summary()

    # ── 1. HOOK ───────────────────────────────────────────────────────────────
    def hook(self):
        q = Text("Зошто пружината се враќа?", font_size=52, color=YELLOW)
        q.move_to(ORIGIN + UP)
        ans = Text("Памет.  Молекулска памет.", font_size=38, color=BLUE)
        ans.next_to(q, DOWN, buff=0.55)
        self.play(Write(q), run_time=1.8)
        self.wait(0.6)
        self.play(FadeIn(ans, shift=UP * 0.3))
        self.wait(1.2)

        sub = Text("Некои материјали памтат. Некои заборавуваат. Некои — никогаш.",
                   font_size=26, color=GREY)
        sub.next_to(ans, DOWN, buff=0.6)
        self.play(FadeIn(sub))
        self.wait(1.5)
        self.play(FadeOut(VGroup(q, ans, sub)))

    # ── 2. ВИДОВИ ДЕФОРМАЦИИ ──────────────────────────────────────────────────
    def deformation_types(self):
        title = section_title("Видови деформации")
        self.play(Write(title))

        # Three panels
        labels = ["Еластична", "Пластична", "Кршење"]
        colors = [GREEN, ORANGE, RED]
        examples = ["пружина, гума", "пластелин, метал", "стакло, керамика"]
        descs = [
            "Се враќа во\nпочетна форма",
            "Останува\nдеформирана",
            "Се распаѓа\nнеповратно",
        ]

        panels = VGroup()
        for i, (lbl, col, ex, desc) in enumerate(zip(labels, colors, examples, descs)):
            card = RoundedRectangle(width=3.6, height=4.2, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.5)
            t_lbl = Text(lbl, font_size=30, color=col, weight=BOLD)
            t_lbl.next_to(card.get_top(), DOWN, buff=0.3)
            t_ex = Text(ex, font_size=22, color=YELLOW)
            t_ex.next_to(t_lbl, DOWN, buff=0.25)
            t_desc = Text(desc, font_size=20, color=WHITE2, line_spacing=1.3)
            t_desc.next_to(t_ex, DOWN, buff=0.3)
            panel = VGroup(card, t_lbl, t_ex, t_desc)
            panels.add(panel)

        panels.arrange(RIGHT, buff=0.5)
        panels.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in panels],
                              lag_ratio=0.25), run_time=1.8)
        self.wait(0.5)

        # Andonovski punch
        punch = Text(
            "Пружината се враќа.  Пластелинот не.\nНекои нешта заборавуваат.  Некои — никогаш.",
            font_size=26, color=WHITE2, line_spacing=1.4)
        punch.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(punch))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, panels, punch)))

    # ── 3. ХУКОВ ЗАКОН ────────────────────────────────────────────────────────
    def hookes_law(self):
        title = section_title("Хуков закон", color=BLUE)
        self.play(Write(title))

        # Spring visual (coil approximation with zigzag)
        coil = self._draw_spring(center=LEFT * 3.2 + DOWN * 0.3, length=2.5)
        weight_box = Square(side_length=0.7, fill_color=ORANGE,
                            fill_opacity=1, stroke_color=YELLOW, stroke_width=2)
        weight_box.next_to(coil, DOWN, buff=0.05)
        w_lbl = Text("F", font_size=26, color=YELLOW, weight=BOLD)
        w_lbl.move_to(weight_box)

        self.play(Create(coil), run_time=1.2)
        self.play(FadeIn(weight_box), Write(w_lbl))
        self.wait(0.4)

        # Extension arrow x
        x_arrow = Arrow(start=weight_box.get_bottom() + DOWN * 0.1,
                        end=weight_box.get_bottom() + DOWN * 1.0,
                        buff=0, color=RED, stroke_width=3)
        x_lbl = Text("x", font_size=28, color=RED)
        x_lbl.next_to(x_arrow, RIGHT, buff=0.15)
        self.play(GrowArrow(x_arrow), Write(x_lbl))
        self.wait(0.3)

        # Formula
        formula_box = callout("F  =  k  ×  x", width=7.5, border=GREEN, font_size=36)
        formula_box.shift(RIGHT * 1.5 + UP * 0.5)
        self.play(FadeIn(formula_box))

        # Legend rows
        legends = [
            ("F", YELLOW, " — сила  [N]"),
            ("k", GREEN,  " — константа на пружина  [N/m]"),
            ("x", RED,    " — издолжување  [m]"),
        ]
        leg_group = VGroup()
        for sym, col, rest in legends:
            row = VGroup(
                Text(sym, font_size=24, color=col, weight=BOLD),
                Text(rest, font_size=24, color=WHITE2),
            ).arrange(RIGHT, buff=0.1)
            leg_group.add(row)
        leg_group.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        leg_group.next_to(formula_box, DOWN, buff=0.45)
        leg_group.shift(RIGHT * 1.5)
        self.play(LaggedStart(*[FadeIn(r) for r in leg_group], lag_ratio=0.2))

        # Elastic limit note
        el_note = callout("Граница на еластичност: над неа — пластична деформација!",
                          width=9.5, border=RED, font_size=23)
        el_note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(el_note))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, coil, weight_box, w_lbl,
                                 x_arrow, x_lbl, formula_box, leg_group, el_note)))

    # ── 4. WORKED EXAMPLE ─────────────────────────────────────────────────────
    def worked_example(self):
        title = section_title("Пресметка — Хуков закон", color=GREEN)
        self.play(Write(title))

        problem = callout(
            "Пружина: k = 200 N/m. Сила: F = 50 N. Колку се издолжи?",
            width=10.0, border=YELLOW, font_size=26)
        problem.shift(UP * 1.5)
        self.play(FadeIn(problem))
        self.wait(0.8)

        steps = [
            ("Формула:", "F  =  k × x", WHITE2, BLUE),
            ("Изразуваме x:", "x  =  F / k", WHITE2, GREEN),
            ("Заменуваме:", "x  =  50 / 200", WHITE2, YELLOW),
            ("Резултат:", "x  =  0.25 m", WHITE2, ORANGE),
        ]
        step_group = VGroup()
        for label, val, lc, vc in steps:
            row = VGroup(
                Text(label, font_size=27, color=lc),
                Text(val, font_size=30, color=vc, weight=BOLD),
            ).arrange(RIGHT, buff=0.5)
            step_group.add(row)
        step_group.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        step_group.shift(DOWN * 0.4)

        for row in step_group:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.4)

        self.wait(1.2)
        self.play(FadeOut(VGroup(title, problem, step_group)))

    # ── 5. REAL-WORLD ─────────────────────────────────────────────────────────
    def real_world(self):
        title = section_title("Во секојдневниот живот", color=ORANGE)
        self.play(Write(title))

        items = [
            ("🏹", "Лак и стрела", "еластична деф."),
            ("🚗", "Амортизери", "k = стотици N/m"),
            ("🧱", "Скакање на батут", "граница → пластичност"),
            ("⌚", "Пружина во часовник", "прецизно k"),
        ]
        cards = VGroup()
        for emoji, name, detail in items:
            c = RoundedRectangle(width=3.0, height=2.2, corner_radius=0.25,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=BLUE, stroke_width=1.8)
            em = Text(emoji, font_size=34)
            nm = Text(name, font_size=24, color=YELLOW)
            dt = Text(detail, font_size=20, color=GREY)
            em.move_to(c.get_center() + UP * 0.55)
            nm.move_to(c.get_center() + UP * 0.05)
            dt.move_to(c.get_center() + DOWN * 0.48)
            cards.add(VGroup(c, em, nm, dt))

        cards.arrange_in_grid(2, 2, buff=0.4)
        cards.shift(DOWN * 0.3)
        self.play(LaggedStart(*[FadeIn(c, scale=0.85) for c in cards], lag_ratio=0.18))
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, cards)))

    # ── 6. SUMMARY ────────────────────────────────────────────────────────────
    def summary(self):
        title = section_title("Резиме", color=YELLOW)
        self.play(Write(title))

        bullets = [
            (GREEN,  "Еластична деф. — материјалот се враќа"),
            (ORANGE, "Пластична деф. — останува изменет"),
            (RED,    "Кршење — неповратно"),
            (BLUE,   "Хуков закон:  F = k × x"),
            (PURPLE, "Граница на еластичност — важна граница"),
        ]
        rows = VGroup()
        for col, text in bullets:
            dot = Dot(radius=0.13, color=col)
            lbl = Text(text, font_size=28, color=WHITE2)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.shift(DOWN * 0.3)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.2))
        self.wait(1.0)

        fin = Text("Пружината знае.  Ти — сега исто.", font_size=30, color=YELLOW)
        fin.to_edge(DOWN, buff=0.4)
        self.play(Write(fin))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rows, fin)))

    # ── HELPER: draw spring ───────────────────────────────────────────────────
    def _draw_spring(self, center=ORIGIN, length=2.5, coils=8, color=GREY):
        pts = [center + UP * length / 2]
        coil_h = length / coils
        for i in range(coils):
            y = length / 2 - coil_h * (i + 0.25)
            pts.append(center + np.array([0.35, y, 0]))
            y2 = length / 2 - coil_h * (i + 0.75)
            pts.append(center + np.array([-0.35, y2, 0]))
        pts.append(center + DOWN * length / 2)
        spring = VMobject(stroke_color=color, stroke_width=3)
        spring.set_points_as_corners(pts)
        return spring
