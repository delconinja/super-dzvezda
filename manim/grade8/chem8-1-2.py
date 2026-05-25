from manim import *
import random

config.background_color = "#1a1a2e"

MK_BLUE   = "#4fc3f7"
MK_YELLOW = "#ffd54f"
MK_GREEN  = "#81c784"
MK_RED    = "#e57373"
MK_GREY   = "#90a4ae"
MK_PURPLE = "#ce93d8"
MK_ORANGE = "#ffab91"

random.seed(42)


# ── helpers ────────────────────────────────────────────────────────────────

def make_solid_particles(center, rows=4, cols=4, spacing=0.38, color=MK_BLUE):
    dots = VGroup()
    for r in range(rows):
        for c in range(cols):
            x = (c - (cols - 1) / 2) * spacing
            y = (r - (rows - 1) / 2) * spacing
            dots.add(Dot(center + np.array([x, y, 0]),
                         radius=0.1, color=color))
    return dots


def make_liquid_particles(center, n=14, color=MK_GREEN):
    dots = VGroup()
    positions = [
        (-0.5, 0.5), (0.0, 0.6), (0.5, 0.5),
        (-0.65, 0.1), (-0.15, 0.2), (0.2, 0.15), (0.65, 0.0),
        (-0.6, -0.3), (-0.1, -0.2), (0.3, -0.3), (0.65, -0.35),
        (-0.4, -0.6), (0.1, -0.55), (0.55, -0.6),
    ]
    for px, py in positions[:n]:
        dots.add(Dot(center + np.array([px, py, 0]),
                     radius=0.1, color=color))
    return dots


def make_gas_particles(center, color=MK_RED):
    positions = [
        (-0.8, 0.7), (0.0, 0.8), (0.8, 0.6),
        (-0.9, 0.0), (-0.2, 0.2), (0.5, 0.1), (0.9, -0.1),
        (-0.7, -0.6), (0.1, -0.5), (0.8, -0.7),
    ]
    dots = VGroup()
    for px, py in positions:
        dots.add(Dot(center + np.array([px, py, 0]),
                     radius=0.1, color=color))
    return dots


def state_box(center, label_text, subtitle, color, particles_fn):
    box = RoundedRectangle(width=2.8, height=3.2, corner_radius=0.2,
                           color=color, stroke_width=2)
    box.move_to(center)
    lbl = Text(label_text, font_size=30, color=color, weight=BOLD)
    lbl.next_to(box, UP, buff=0.2)
    sub = Text(subtitle, font_size=20, color=MK_GREY)
    sub.next_to(box, DOWN, buff=0.15)
    pts = particles_fn(center)
    return VGroup(box, lbl, sub, pts)


# ── scene ─────────────────────────────────────────────────────────────────

class Chem812Scene(Scene):
    def construct(self):

        # ─── 1. TITLE ─────────────────────────────────────────── ~3 s ──
        self.next_section("title")
        title = Text("Промени на агрегатната состојба",
                     font_size=48, color=MK_YELLOW, weight=BOLD)
        sub   = Text("Хемија 8  ·  Единица 1 — Агрегатни состојби",
                     font_size=26, color=MK_BLUE)
        sub.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub))

        # ─── 2. THREE STATES WITH PARTICLES ──────────────────── ~10 s ──
        self.next_section("three_states")
        centers = [LEFT * 4, ORIGIN, RIGHT * 4]

        solid_grp  = state_box(centers[0], "ЦВРСТО", "мраз / метал",
                               MK_BLUE,
                               lambda c: make_solid_particles(c))
        liquid_grp = state_box(centers[1], "ТЕЧНО", "вода / нафта",
                               MK_GREEN,
                               lambda c: make_liquid_particles(c))
        gas_grp    = state_box(centers[2], "ГАС", "пара / воздух",
                               MK_RED,
                               lambda c: make_gas_particles(c))

        # Animate each box in
        self.play(FadeIn(solid_grp,  shift=UP * 0.4), run_time=0.8)
        self.play(FadeIn(liquid_grp, shift=UP * 0.4), run_time=0.8)
        self.play(FadeIn(gas_grp,    shift=UP * 0.4), run_time=0.8)
        self.wait(0.5)

        # Pulse particles to suggest motion
        solid_pts  = solid_grp[3]
        liquid_pts = liquid_grp[3]
        gas_pts    = gas_grp[3]

        # Solid: tiny wiggle (structured, barely moves)
        self.play(Wiggle(solid_pts, scale_value=1.04, n_wiggles=3,
                         run_time=1.2))

        # Liquid: gentle shift of pairs
        self.play(
            liquid_pts[0].animate.shift(RIGHT * 0.08 + UP * 0.05),
            liquid_pts[4].animate.shift(LEFT * 0.1),
            liquid_pts[8].animate.shift(RIGHT * 0.07 + DOWN * 0.06),
            liquid_pts[12].animate.shift(LEFT * 0.08),
            run_time=0.8,
        )
        self.play(
            liquid_pts[0].animate.shift(LEFT * 0.08 + DOWN * 0.05),
            liquid_pts[4].animate.shift(RIGHT * 0.1),
            liquid_pts[8].animate.shift(LEFT * 0.07 + UP * 0.06),
            liquid_pts[12].animate.shift(RIGHT * 0.08),
            run_time=0.8,
        )

        # Gas: large spread-out movement
        self.play(
            *[gas_pts[i].animate.shift(
                np.array([random.uniform(-0.2, 0.2),
                          random.uniform(-0.2, 0.2), 0]))
              for i in range(len(gas_pts))],
            run_time=0.9,
        )
        self.play(
            *[gas_pts[i].animate.shift(
                np.array([random.uniform(-0.2, 0.2),
                          random.uniform(-0.2, 0.2), 0]))
              for i in range(len(gas_pts))],
            run_time=0.9,
        )
        self.wait(0.8)

        # Energy caption
        energy_note = Text(
            "Повеќе енергија  →  почесто и посилно движење на честиците",
            font_size=24, color=MK_YELLOW,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(energy_note, shift=UP * 0.2))
        self.wait(1)
        self.play(FadeOut(solid_grp), FadeOut(liquid_grp),
                  FadeOut(gas_grp),   FadeOut(energy_note))

        # ─── 3. SIX TRANSITIONS ───────────────────────────────── ~9 s ──
        self.next_section("transitions")

        # Three state labels
        s_lbl = Text("ЦВРСТО", font_size=34, color=MK_BLUE,  weight=BOLD).move_to(LEFT  * 4.5 + UP * 1)
        l_lbl = Text("ТЕЧНО",  font_size=34, color=MK_GREEN, weight=BOLD).move_to(ORIGIN + UP * 1)
        g_lbl = Text("ГАС",    font_size=34, color=MK_RED,   weight=BOLD).move_to(RIGHT * 4.5 + UP * 1)

        self.play(FadeIn(s_lbl), FadeIn(l_lbl), FadeIn(g_lbl))

        def double_arrow(start, end, label_up, label_dn,
                         color_up=MK_YELLOW, color_dn=MK_GREY):
            offset = UP * 0.22
            arr_up = Arrow(start + offset, end + offset,
                           color=color_up, buff=0.1,
                           stroke_width=3, max_tip_length_to_length_ratio=0.12)
            arr_dn = Arrow(end - offset, start - offset,
                           color=color_dn, buff=0.1,
                           stroke_width=3, max_tip_length_to_length_ratio=0.12)
            mid = (start + end) / 2
            lbl_u = Text(label_up, font_size=22, color=color_up)
            lbl_d = Text(label_dn, font_size=22, color=color_dn)
            lbl_u.next_to(arr_up, UP, buff=0.1)
            lbl_d.next_to(arr_dn, DOWN, buff=0.1)
            return VGroup(arr_up, arr_dn, lbl_u, lbl_d)

        # Solid ↔ Liquid  (horizontal, left side)
        sl_arrows = double_arrow(
            LEFT * 4.5 + DOWN * 0.3,
            LEFT * 0.8  + DOWN * 0.3,
            "Топење  →", "←  Замрзнување",
            color_up=MK_RED, color_dn=MK_BLUE,
        )
        self.play(GrowArrow(sl_arrows[0]), GrowArrow(sl_arrows[1]),
                  run_time=1)
        self.play(Write(sl_arrows[2]), Write(sl_arrows[3]))
        self.wait(0.4)

        # Liquid ↔ Gas  (horizontal, right side)
        lg_arrows = double_arrow(
            RIGHT * 0.8  + DOWN * 0.3,
            RIGHT * 4.5  + DOWN * 0.3,
            "Испарување  →", "←  Кондензација",
            color_up=MK_RED, color_dn=MK_BLUE,
        )
        self.play(GrowArrow(lg_arrows[0]), GrowArrow(lg_arrows[1]),
                  run_time=1)
        self.play(Write(lg_arrows[2]), Write(lg_arrows[3]))
        self.wait(0.4)

        # Solid ↔ Gas  (curved arrow below)
        sg_up = CurvedArrow(LEFT * 4.5 + DOWN * 1.5,
                            RIGHT * 4.5 + DOWN * 1.5,
                            angle=-TAU / 6, color=MK_PURPLE,
                            stroke_width=3)
        sg_dn = CurvedArrow(RIGHT * 4.5 + DOWN * 2.0,
                            LEFT  * 4.5 + DOWN * 2.0,
                            angle=-TAU / 6, color=MK_GREY,
                            stroke_width=3)
        sg_up_lbl = Text("Сублимација", font_size=22, color=MK_PURPLE)
        sg_dn_lbl = Text("Десублимација", font_size=22, color=MK_GREY)
        sg_up_lbl.next_to(sg_up, DOWN, buff=0.08)
        sg_dn_lbl.next_to(sg_dn, DOWN, buff=0.08)

        self.play(Create(sg_up), run_time=1)
        self.play(Write(sg_up_lbl))
        self.play(Create(sg_dn), run_time=1)
        self.play(Write(sg_dn_lbl))
        self.wait(1.2)

        self.play(
            FadeOut(s_lbl), FadeOut(l_lbl), FadeOut(g_lbl),
            FadeOut(sl_arrows), FadeOut(lg_arrows),
            FadeOut(sg_up), FadeOut(sg_dn),
            FadeOut(sg_up_lbl), FadeOut(sg_dn_lbl),
        )

        # ─── 4. HEATING CURVE ────────────────────────────────── ~10 s ──
        self.next_section("heating_curve")

        curve_title = Text("Графикон на загревање на вода",
                           font_size=34, color=MK_YELLOW)
        curve_title.to_edge(UP, buff=0.3)
        self.play(Write(curve_title))

        # Axes — no LaTeX numbers
        ax = Axes(
            x_range=[0, 14, 1], y_range=[-15, 120, 10],
            x_length=9, y_length=5,
            axis_config={"color": WHITE, "include_tip": True,
                         "tip_length": 0.18, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        x_lbl = Text("Време (min)", font_size=22, color=MK_GREY)
        y_lbl = Text("Температура (°C)", font_size=22, color=MK_GREY)
        x_lbl.next_to(ax.x_axis.get_end(), DOWN + RIGHT, buff=0.1)
        y_lbl.rotate(PI / 2).next_to(ax.y_axis.get_end(), LEFT, buff=0.18)

        # Manual tick labels
        x_ticks = VGroup(*[
            Text(str(v), font_size=18, color=MK_GREY
                 ).next_to(ax.c2p(v, -15), DOWN, buff=0.12)
            for v in [2, 5, 9, 12, 14]
        ])
        y_ticks = VGroup(*[
            Text(str(v) + "°", font_size=18, color=MK_GREY
                 ).next_to(ax.c2p(0, v), LEFT, buff=0.12)
            for v in [-10, 0, 50, 100, 115]
        ])

        self.play(Create(ax), Write(x_lbl), Write(y_lbl),
                  FadeIn(x_ticks), FadeIn(y_ticks), run_time=1.2)

        # Piecewise heating curve — 5 segments
        # 1) Ice heating:  t 0→2,   T -10→0
        seg1 = ax.plot(lambda t: -10 + 5 * t,      x_range=[0, 2],
                       color=MK_BLUE,   stroke_width=4)
        # 2) Melting:      t 2→5,   T = 0
        seg2 = ax.plot(lambda t: 0,                 x_range=[2, 5],
                       color=MK_GREEN,  stroke_width=4)
        # 3) Water heating: t 5→9,  T 0→100
        seg3 = ax.plot(lambda t: 25 * (t - 5),      x_range=[5, 9],
                       color=MK_BLUE,   stroke_width=4)
        # 4) Boiling:      t 9→12,  T = 100
        seg4 = ax.plot(lambda t: 100,               x_range=[9, 12],
                       color=MK_RED,    stroke_width=4)
        # 5) Steam heating: t 12→14, T 100→115
        seg5 = ax.plot(lambda t: 100 + 7.5 * (t - 12), x_range=[12, 14],
                       color=MK_YELLOW, stroke_width=4)

        # Animated dot travels the full curve
        full_path = VMobject()
        full_path.set_points_smoothly([
            ax.c2p(t, (-10 + 5*t) if t <= 2
                   else 0 if t <= 5
                   else (25*(t-5)) if t <= 9
                   else 100 if t <= 12
                   else (100 + 7.5*(t-12)))
            for t in [i * 0.25 for i in range(57)]
        ])

        dot = Dot(ax.c2p(0, -10), color=MK_YELLOW, radius=0.12)
        self.add(dot)

        def annotate(seg, label, pos, color):
            lbl = Text(label, font_size=21, color=color)
            lbl.move_to(pos)
            return lbl

        # Draw segment by segment with annotations
        ann1 = annotate(seg1, "Лед се загрева",
                        ax.c2p(0.7, 8),  MK_BLUE)        # above seg1 endpoint
        self.play(Create(seg1),
                  dot.animate.move_to(ax.c2p(2, 0)), run_time=1)
        self.play(FadeIn(ann1, shift=RIGHT * 0.2))

        ann2 = annotate(seg2, "Топење  —  T не се менува!",
                        ax.c2p(3.5, 18), MK_GREEN)        # above melting line
        self.play(Create(seg2),
                  dot.animate.move_to(ax.c2p(5, 0)), run_time=1.2)
        self.play(FadeIn(ann2, shift=RIGHT * 0.2))
        self.wait(0.5)

        ann3 = annotate(seg3, "Вода се загрева",
                        ax.c2p(5.8, 74), MK_BLUE)         # above water segment
        self.play(Create(seg3),
                  dot.animate.move_to(ax.c2p(9, 100)), run_time=1.2)
        self.play(FadeIn(ann3, shift=RIGHT * 0.2))

        ann4 = annotate(seg4, "Вриење  —  T не се менува!",
                        ax.c2p(10.5, 82), MK_RED)         # below boiling line
        self.play(Create(seg4),
                  dot.animate.move_to(ax.c2p(12, 100)), run_time=1.1)
        self.play(FadeIn(ann4, shift=RIGHT * 0.2))
        self.wait(0.5)

        ann5 = annotate(seg5, "Пара",
                        ax.c2p(13.2, 112), MK_YELLOW)     # above steam segment
        self.play(Create(seg5),
                  dot.animate.move_to(ax.c2p(14, 115)), run_time=0.8)
        self.play(FadeIn(ann5))
        self.wait(1.5)

        self.play(
            FadeOut(ax), FadeOut(x_lbl), FadeOut(y_lbl),
            FadeOut(x_ticks), FadeOut(y_ticks), FadeOut(curve_title),
            FadeOut(seg1), FadeOut(seg2), FadeOut(seg3),
            FadeOut(seg4), FadeOut(seg5), FadeOut(dot),
            FadeOut(ann1), FadeOut(ann2), FadeOut(ann3),
            FadeOut(ann4), FadeOut(ann5),
        )

        # ─── 5. SUMMARY ───────────────────────────────────────── ~5 s ──
        self.next_section("summary")
        hdr = Text("Запамти:", font_size=42, color=MK_YELLOW, weight=BOLD)
        hdr.to_corner(UL).shift(RIGHT * 0.6 + DOWN * 0.2)

        bullets = VGroup(
            Text("➤  Цврсто → Течно    =  Топење      (загревање)",  font_size=29, color=MK_RED),
            Text("➤  Течно  → Цврсто   =  Замрзнување  (ладење)",    font_size=29, color=MK_BLUE),
            Text("➤  Течно  → Гас      =  Испарување  (загревање)",  font_size=29, color=MK_RED),
            Text("➤  Гас    → Течно    =  Кондензација (ладење)",    font_size=29, color=MK_BLUE),
            Text("➤  За време на промена — температурата НЕ се менува!",
                 font_size=29, color=MK_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        bullets.shift(DOWN * 0.5 + RIGHT * 0.3)

        self.play(Write(hdr))
        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.45)
        self.wait(2.5)
