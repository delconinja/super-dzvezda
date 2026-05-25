"""
phys8-3-3  —  Рефлексија и закон за рефлексија
Физика 8, Единица 3: Светлина

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-3-3.py Phys833Scene
Output:  media/videos/phys8-3-3/480p15/Phys833Scene.mp4
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


class Phys833Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Огледалото те гледа. И ти него.",
                    font_size=44, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.3)
        self.wait(0.7)

        sub = Text(
            "Зошто добиваш слика — а не само светлина?",
            font_size=32, color=WHITE2,
        )
        sub.next_to(hook, DOWN, buff=0.35)
        self.play(FadeIn(sub, shift=UP * 0.2))
        self.wait(1.8)

        self.play(FadeOut(hook), FadeOut(sub))

        # ══════════════════════════════════════════════════════════
        # 2.  ЗАКОН ЗА РЕФЛЕКСИЈА                            ~16 s
        # ══════════════════════════════════════════════════════════
        self.next_section("law")

        hdr = section_title("Закон за рефлексија")
        self.play(Write(hdr), run_time=0.9)

        # mirror line
        mirror_line = Line(LEFT * 0.1 + DOWN * 2.5, LEFT * 0.1 + UP * 2.5,
                           color=GREY, stroke_width=4)
        mirror_lbl = Text("Огледало", font_size=20, color=GREY)
        mirror_lbl.next_to(mirror_line, RIGHT, buff=0.15).shift(UP * 2.0)

        # normal (dashed)
        normal = DashedLine(LEFT * 0.1 + UP * 2.0, LEFT * 0.1 + DOWN * 2.0,
                            color=GREY, stroke_width=1.5, dash_length=0.14)
        normal_lbl = Text("нормала", font_size=18, color=GREY)
        normal_lbl.next_to(normal.get_end(), DOWN, buff=0.1)

        # incident ray
        inc_angle = 40  # degrees from normal
        inc_dir   = np.array([-np.cos(np.radians(inc_angle)),
                               -np.sin(np.radians(inc_angle)), 0.0])
        hit_point = np.array([-0.1, 0.0, 0.0])
        inc_start = hit_point - inc_dir * 3.5

        inc_ray = Arrow(inc_start, hit_point,
                        color=YELLOW, buff=0, stroke_width=3.5,
                        max_tip_length_to_length_ratio=0.15)

        # reflected ray (mirror about normal = x-axis here)
        ref_dir = np.array([-inc_dir[0], inc_dir[1], 0.0])
        ref_end = hit_point + ref_dir * 3.5
        ref_ray = Arrow(hit_point, ref_end,
                        color=ORANGE, buff=0, stroke_width=3.5,
                        max_tip_length_to_length_ratio=0.15)

        # angle arcs
        inc_arc = Arc(radius=0.7, start_angle=PI / 2,
                      angle=-np.radians(inc_angle),
                      color=YELLOW, stroke_width=2).shift(hit_point)
        ref_arc = Arc(radius=0.7, start_angle=PI / 2,
                      angle=np.radians(inc_angle),
                      color=ORANGE, stroke_width=2).shift(hit_point)

        alpha_lbl = Text("α", font_size=24, color=YELLOW)
        alpha_lbl.next_to(inc_arc, UP + LEFT, buff=0.05)
        beta_lbl = Text("β", font_size=24, color=ORANGE)
        beta_lbl.next_to(ref_arc, UP + RIGHT, buff=0.05)

        inc_lbl = Text("паѓачки зрак", font_size=20, color=YELLOW)
        inc_lbl.next_to(inc_ray.get_start(), LEFT, buff=0.1)
        ref_lbl = Text("одбиен зрак", font_size=20, color=ORANGE)
        ref_lbl.next_to(ref_ray.get_end(), RIGHT, buff=0.1)

        self.play(Create(mirror_line), Write(mirror_lbl))
        self.play(Create(normal), Write(normal_lbl))
        self.play(GrowArrow(inc_ray), Write(inc_lbl))
        self.play(Create(inc_arc), Write(alpha_lbl))
        self.play(GrowArrow(ref_ray), Write(ref_lbl))
        self.play(Create(ref_arc), Write(beta_lbl))
        self.wait(0.8)

        law_box = callout(
            "Агол на паѓање (α) = Агол на одбивање (β)   —   секогаш!",
            width=10.5, bg="#0d2b44", border=YELLOW, font_size=26,
        )
        law_box.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(law_box, shift=UP * 0.2))
        self.play(Indicate(law_box, scale_factor=1.05, color=YELLOW))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [
            hdr, mirror_line, mirror_lbl, normal, normal_lbl,
            inc_ray, inc_lbl, ref_ray, ref_lbl,
            inc_arc, ref_arc, alpha_lbl, beta_lbl, law_box,
        ]])

        # ══════════════════════════════════════════════════════════
        # 3.  ПРАВИЛНА VS ДИФУЗНА РЕФЛЕКСИЈА                 ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("specular_diffuse")

        hdr2 = section_title("Правилна наспроти дифузна рефлексија")
        self.play(Write(hdr2), run_time=0.9)

        # Specular
        spec_surface = Line(LEFT * 5.5 + DOWN * 1.2, LEFT * 2.5 + DOWN * 1.2,
                            color=BLUE, stroke_width=5)
        spec_lbl = Text("Рамна (правилна)", font_size=20, color=BLUE, weight=BOLD)
        spec_lbl.next_to(spec_surface, DOWN, buff=0.2)

        spec_rays_in  = VGroup()
        spec_rays_out = VGroup()
        for i in range(3):
            x = -5.0 + i * 1.0
            start_in  = np.array([x, 0.2, 0])
            end_hit   = np.array([x, -1.2, 0])
            end_out   = np.array([x, 0.2, 0]) + np.array([0.8, 0.0, 0]) * (i + 1) * 0.4
            spec_rays_in.add(Arrow(start_in, end_hit, color=YELLOW, buff=0,
                                   stroke_width=2.5, max_tip_length_to_length_ratio=0.2))
            spec_rays_out.add(Arrow(end_hit, np.array([x + 0.5, 0.3, 0]),
                                    color=ORANGE, buff=0, stroke_width=2.5,
                                    max_tip_length_to_length_ratio=0.2))

        self.play(Create(spec_surface), Write(spec_lbl))
        self.play(*[GrowArrow(r) for r in spec_rays_in])
        self.play(*[GrowArrow(r) for r in spec_rays_out])
        spec_note = Text("Паралелни зраци → паралелна рефлексија → слика", font_size=20, color=BLUE)
        spec_note.move_to(LEFT * 4.0 + UP * 1.5)
        self.play(Write(spec_note))
        self.wait(1.0)

        # Diffuse
        diff_pts = [LEFT * 1.5 + DOWN * 0.9, LEFT * 0.8 + DOWN * 1.4,
                    ORIGIN + DOWN * 1.0, RIGHT * 0.9 + DOWN * 1.3, RIGHT * 1.8 + DOWN * 0.8]
        diff_surface = VMobject(color=GREY, stroke_width=4)
        diff_surface.set_points_as_corners([p.get_center() if hasattr(p, 'get_center')
                                            else p for p in diff_pts])
        diff_lbl = Text("Груба (дифузна)", font_size=20, color=GREY, weight=BOLD)
        diff_lbl.next_to(diff_surface, DOWN, buff=0.25)

        diff_rays_in  = VGroup()
        diff_rays_out = VGroup()
        for i in range(4):
            x = -1.2 + i * 0.9
            start_d = np.array([x, 0.2, 0])
            hit_d   = np.array([x, -1.05, 0])
            angle_out = np.radians(np.random.choice([-50, -20, 20, 50]))
            end_d = hit_d + np.array([np.sin(angle_out) * 0.9, np.cos(angle_out) * 0.9, 0])
            diff_rays_in.add(Arrow(start_d, hit_d, color=YELLOW, buff=0,
                                   stroke_width=2, max_tip_length_to_length_ratio=0.2))
            diff_rays_out.add(Arrow(hit_d, end_d, color=ORANGE, buff=0,
                                    stroke_width=2, max_tip_length_to_length_ratio=0.2))

        self.play(Create(diff_surface), Write(diff_lbl))
        self.play(*[GrowArrow(r) for r in diff_rays_in])
        self.play(*[GrowArrow(r) for r in diff_rays_out])
        diff_note = Text("Зраци се расфрлуваат → нема слика, но можеме да го видиме предметот",
                         font_size=18, color=GREY)
        diff_note.move_to(RIGHT * 1.5 + UP * 1.4)
        self.play(Write(diff_note))
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            hdr2, spec_surface, spec_lbl, spec_rays_in, spec_rays_out, spec_note,
            diff_surface, diff_lbl, diff_rays_in, diff_rays_out, diff_note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 4.  ВИДОВИ ОГЛЕДАЛА                                ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mirror_types")

        hdr3 = section_title("Видови огледала")
        self.play(Write(hdr3), run_time=0.8)

        mirror_data = [
            ("Рамно огледало",     "иста голема слика, виртуелна, исправена",  BLUE,   "огледало во бања"),
            ("Конкавно (вдлабнато)", "зголемува предмети близу → виртуелна слика; оддалечено → реална, превртена", GREEN, "бричење, грло, фенер"),
            ("Конвексно (испакнато)", "намалена слика, поширок агол на гледање",  ORANGE, "огледало на автомобил"),
        ]

        cards = VGroup()
        for name, description, col, example in mirror_data:
            bg = RoundedRectangle(
                width=12.0, height=1.4, corner_radius=0.22,
                fill_color=f"{col}14", fill_opacity=1,
                stroke_color=col, stroke_width=1.8,
            )
            nt = Text(name, font_size=22, color=col, weight=BOLD)
            nt.next_to(bg.get_left(), RIGHT, buff=0.3).shift(UP * 0.25)
            dt = Text(description, font_size=17, color=WHITE2)
            dt.next_to(bg.get_left(), RIGHT, buff=0.3).shift(DOWN * 0.2)
            et = Text(f"пример: {example}", font_size=16, color=GREY)
            et.next_to(bg.get_right(), LEFT, buff=0.3)
            cards.add(VGroup(bg, nt, dt, et))

        cards.arrange(DOWN, buff=0.35)
        cards.shift(DOWN * 0.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.55)
            self.wait(0.8)

        self.wait(1.5)
        self.play(FadeOut(hdr3), FadeOut(cards))

        # ══════════════════════════════════════════════════════════
        # 5.  ПЕРИСКОП — ПРАКТИЧНА ПРИМЕНА                    ~13 s
        # ══════════════════════════════════════════════════════════
        self.next_section("periscope")

        hdr4 = section_title("Перископ — две огледала по 45°")
        self.play(Write(hdr4), run_time=0.8)

        # Periscope schematic: vertical tube, 2 mirrors at 45 degrees
        # outer tube
        tube = Rectangle(width=0.8, height=4.5,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=GREY, stroke_width=2)
        tube.shift(LEFT * 1.5 + DOWN * 0.3)

        # top mirror at 45°
        mir_top = Line(tube.get_corner(UL) + RIGHT * 0.05 + DOWN * 0.05,
                       tube.get_corner(UR) + LEFT * 0.05 + UP * 0.05,
                       color=BLUE, stroke_width=4)
        # bottom mirror at 45° (other direction)
        mir_bot = Line(tube.get_corner(DL) + RIGHT * 0.05 + UP * 0.05,
                       tube.get_corner(DR) + LEFT * 0.05 + DOWN * 0.05,
                       color=BLUE, stroke_width=4)

        # ray path
        ray_in   = Arrow(LEFT * 4.5 + UP * 1.9, LEFT * 1.9 + UP * 1.9,
                         color=YELLOW, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.15)
        ray_down = Arrow(LEFT * 1.5 + UP * 1.9, LEFT * 1.5 + DOWN * 2.8,
                         color=YELLOW, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.15)
        ray_out  = Arrow(LEFT * 1.1 + DOWN * 2.55, RIGHT * 2.0 + DOWN * 2.55,
                         color=YELLOW, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.15)

        steps_p = VGroup(
            Text("1. Зракот влегува одозгора", font_size=20, color=WHITE2),
            Text("2. Горно огледало го свртува надолу (90°)", font_size=20, color=WHITE2),
            Text("3. Долно огледало го свртува нанадвор (90°)", font_size=20, color=WHITE2),
            Text("4. Набљудувачот гледа предметот", font_size=20, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps_p.shift(RIGHT * 2.8 + DOWN * 0.2)

        self.play(Create(tube))
        self.play(Create(mir_top), Create(mir_bot))
        self.play(GrowArrow(ray_in))
        self.play(GrowArrow(ray_down))
        self.play(GrowArrow(ray_out))

        for step in steps_p:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.45)
            self.wait(0.35)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in [
            hdr4, tube, mir_top, mir_bot, ray_in, ray_down, ray_out, steps_p,
        ]])

        # ══════════════════════════════════════════════════════════
        # 6.  АНDONОВСКИ МОМЕНТ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Огледалото не лаже.",            WHITE2, 38),
            ("Но и не кажува сè.",              WHITE2, 38),
            ("Го менува лево и десно.",         WHITE2, 34),
            ("Секогаш.",                        YELLOW, 60),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.42)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.45)

        self.play(Indicate(grp[-1], scale_factor=1.35, color=YELLOW))
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
            (YELLOW, "Рефлексија = одбивање на светлина"),
            (BLUE,   "Агол на паѓање = агол на одбивање (закон за рефлексија)"),
            (GREEN,  "Правилна (рамна) → слика; дифузна (груба) → без слика"),
            (ORANGE, "Конвексно → поширок поглед (авто); конкавно → зголемување"),
            (PURPLE, "Перископ = 2 огледала по 45°"),
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
