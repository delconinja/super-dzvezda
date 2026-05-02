"""
Супер Ѕвезда — Математика 5-то одделение
Лекција: Видови триаголници

Run:
    manim -pql lesson_vidovi_triagolnici.py VidoviTriagolnici   (preview)
    manim -pqh lesson_vidovi_triagolnici.py VidoviTriagolnici   (HD final)
"""

from manim import *
import numpy as np

C_BG     = "#0D1B2A"
C_TXT    = "#EDE8DF"
C_ACC    = "#C4975A"
C_ACUTE  = "#3B82F6"   # blue  — остар
C_RIGHT  = "#8B5CF6"   # purple — правоаголен
C_OBTUSE = "#10B981"   # green  — тап


def make_triangle(a_deg, b_deg, scale=1.8):
    """Return a Polygon given bottom-left and bottom-right angles."""
    a = np.radians(a_deg)
    b = np.radians(b_deg)
    c = np.radians(180 - a_deg - b_deg)
    base = scale
    # Law of sines
    t1 = base * np.sin(b) / np.sin(c)
    v1 = np.array([-base / 2, -0.9, 0])
    v2 = np.array([ base / 2, -0.9, 0])
    v3 = np.array([v1[0] + t1 * np.cos(a), v1[1] + t1 * np.sin(a), 0])
    return v1, v2, v3


def angle_label(vertex, neighbor1, neighbor2, angle_deg, color, radius=0.32):
    """Small arc + degree text at a triangle vertex."""
    # Direction vectors from vertex
    d1 = normalize(neighbor1 - vertex)
    d2 = normalize(neighbor2 - vertex)
    mid_dir = normalize(d1 + d2)
    label_pos = vertex + mid_dir * (radius + 0.28)
    txt = Text(f"{angle_deg}°", font_size=18, color=color, weight=BOLD)
    txt.move_to(label_pos)
    return txt


def normalize(v):
    n = np.linalg.norm(v)
    return v / n if n > 0 else v


class VidoviTriagolnici(Scene):

    def construct(self):
        self.camera.background_color = C_BG
        self._intro()
        self._rule_sum()
        self._acute()
        self._right()
        self._obtuse()
        self._comparison()
        self._by_sides()
        self._summary()

    # ── 1. Title ──────────────────────────────────────────────────
    def _intro(self):
        title = Text("Видови триаголници", font_size=54,
                     color=C_ACC, weight=BOLD)
        sub = Text("Математика · 5-то одделение",
                   font_size=22, color=C_TXT)
        sub.next_to(title, DOWN, buff=0.4)

        self.play(Write(title, run_time=1.2))
        self.play(FadeIn(sub))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(sub))

    # ── 2. Key rule: angles sum to 180° ──────────────────────────
    def _rule_sum(self):
        rule_box = RoundedRectangle(width=8, height=1.6,
                                    corner_radius=0.25,
                                    fill_color=C_ACC, fill_opacity=0.12,
                                    stroke_color=C_ACC, stroke_width=2)
        rule_txt = Text("Збирот на аглите на секој триаголник = 180°",
                        font_size=28, color=WHITE, weight=BOLD)
        rule_txt.move_to(rule_box)
        icon = Text("💡", font_size=34)
        icon.next_to(rule_box, LEFT, buff=0.2)

        self.play(DrawBorderThenFill(rule_box), run_time=0.8)
        self.play(Write(rule_txt), FadeIn(icon))
        self.wait(2)
        self.play(FadeOut(rule_box), FadeOut(rule_txt), FadeOut(icon))

    # ── 3. Acute triangle ─────────────────────────────────────────
    def _acute(self):
        self._show_triangle_type(
            a_deg=60, b_deg=70,
            color=C_ACUTE,
            mk_name="Остар триаголник",
            rule="Сите 3 агли < 90°",
            scale=2.2,
        )

    # ── 4. Right triangle ─────────────────────────────────────────
    def _right(self):
        self._show_triangle_type(
            a_deg=90, b_deg=45,
            color=C_RIGHT,
            mk_name="Правоаголен триаголник",
            rule="Точно 1 агол = 90°",
            scale=2.0,
            is_right=True,
        )

    # ── 5. Obtuse triangle ────────────────────────────────────────
    def _obtuse(self):
        self._show_triangle_type(
            a_deg=31, b_deg=31,
            color=C_OBTUSE,
            mk_name="Тап триаголник",
            rule="Еден агол > 90°",
            scale=2.4,
        )

    def _show_triangle_type(self, a_deg, b_deg, color, mk_name,
                             rule, scale=2.0, is_right=False):
        c_deg = 180 - a_deg - b_deg
        v1, v2, v3 = make_triangle(a_deg, b_deg, scale)

        tri = Polygon(v1, v2, v3,
                      fill_color=color, fill_opacity=0.18,
                      stroke_color=color, stroke_width=2.5)
        tri.shift(DOWN * 0.3)

        # Right-angle box
        if is_right:
            box_size = 0.18
            right_box = Square(side_length=box_size,
                               stroke_color=color, stroke_width=1.5,
                               fill_opacity=0)
            corner = tri.get_vertices()[0]  # v1 = bottom-left = 90°
            right_box.move_to(corner + np.array([box_size / 2, box_size / 2, 0]))

        # Angle labels
        verts = tri.get_vertices()
        lbl_a = angle_label(verts[0], verts[1], verts[2], a_deg, color)
        lbl_b = angle_label(verts[1], verts[0], verts[2], b_deg, color)
        lbl_c = angle_label(verts[2], verts[0], verts[1], c_deg, color)

        # Name + rule
        name = Text(mk_name, font_size=36, color=color, weight=BOLD)
        name.to_edge(UP, buff=0.6)
        rule_txt = Text(rule, font_size=24, color=C_TXT)
        rule_txt.next_to(name, DOWN, buff=0.2)

        # Animate
        self.play(FadeIn(name), FadeIn(rule_txt))
        self.play(DrawBorderThenFill(tri, run_time=1.2))
        if is_right:
            self.play(FadeIn(right_box))
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), FadeIn(lbl_c))

        # Highlight each angle
        for lbl, deg in [(lbl_a, a_deg), (lbl_b, b_deg), (lbl_c, c_deg)]:
            self.play(lbl.animate.scale(1.35), run_time=0.3)
            self.wait(0.4)
            self.play(lbl.animate.scale(1 / 1.35), run_time=0.3)

        self.wait(1.2)

        objs = [tri, name, rule_txt, lbl_a, lbl_b, lbl_c]
        if is_right:
            objs.append(right_box)
        self.play(*[FadeOut(o) for o in objs])

    # ── 6. Side-by-side comparison ────────────────────────────────
    def _comparison(self):
        title = Text("Споредба", font_size=36, color=C_ACC, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        configs = [
            (55, 65, C_ACUTE,  "Остар",        "сите < 90°", -3.8),
            (90, 50, C_RIGHT,  "Правоаголен",  "еден = 90°",  0.0),
            (31, 31, C_OBTUSE, "Тап",          "еден > 90°",  3.8),
        ]

        triangles = []
        for a, b, col, name, desc, xoff in configs:
            v1, v2, v3 = make_triangle(a, b, scale=1.3)
            tri = Polygon(v1, v2, v3,
                          fill_color=col, fill_opacity=0.18,
                          stroke_color=col, stroke_width=2)
            tri.shift(RIGHT * xoff + DOWN * 0.4)

            lbl = Text(name, font_size=22, color=col, weight=BOLD)
            lbl.next_to(tri, DOWN, buff=0.25)
            desc_t = Text(desc, font_size=16, color=C_TXT)
            desc_t.next_to(lbl, DOWN, buff=0.1)

            triangles.extend([tri, lbl, desc_t])
            self.play(DrawBorderThenFill(tri, run_time=0.7),
                      FadeIn(lbl), FadeIn(desc_t))

        self.wait(2.5)
        self.play(*[FadeOut(o) for o in triangles], FadeOut(title))

    # ── 7. Classification by sides ────────────────────────────────
    def _by_sides(self):
        title = Text("По страни", font_size=36, color=C_ACC, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        rows = [
            ("Рамностран", "3 еднакви страни · 60°, 60°, 60°", C_ACUTE),
            ("Рамнокрак",  "2 еднакви страни",                  C_RIGHT),
            ("Разностран", "Сите страни различни",              C_OBTUSE),
        ]

        items = VGroup()
        for kind, desc, col in rows:
            dot = Dot(color=col, radius=0.08)
            k = Text(kind, font_size=24, color=col, weight=BOLD)
            d = Text(desc, font_size=20, color=C_TXT)
            row = VGroup(dot, k, d).arrange(RIGHT, buff=0.3)
            items.add(row)

        items.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        items.move_to(ORIGIN)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(items), FadeOut(title))

    # ── 8. Summary ────────────────────────────────────────────────
    def _summary(self):
        lines = VGroup(
            Text("Запомни:", font_size=30, color=C_ACC, weight=BOLD),
            Text("Остар  → сите агли < 90°",   font_size=26, color=C_ACUTE),
            Text("Правоаголен  → еден агол = 90°", font_size=26, color=C_RIGHT),
            Text("Тап  → еден агол > 90°",     font_size=26, color=C_OBTUSE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        lines.move_to(ORIGIN)

        box = SurroundingRectangle(lines, color=C_ACC,
                                   buff=0.4, corner_radius=0.2,
                                   stroke_width=1.5)

        self.play(DrawBorderThenFill(box, run_time=0.6))
        for line in lines:
            self.play(FadeIn(line, shift=UP * 0.1), run_time=0.4)
        self.wait(2.5)

        bye = Text("Супер Ѕвезда ⭐", font_size=36, color=C_ACC, weight=BOLD)
        self.play(FadeOut(lines), FadeOut(box))
        self.play(Write(bye))
        self.wait(1.5)
        self.play(FadeOut(bye))
