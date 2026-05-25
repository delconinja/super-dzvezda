"""
bio8-1-7  —  Ендокрин систем и хормонална регулација
Биологија 8, Единица 1: Нервен и сетилен систем

Teaching narrative — Andonovski-style: three-beat punches,
hormones as slow messengers, glands as broadcasters,
one-word finishers.
Render:  manim -ql bio8-1-7.py Bio817Scene
Output:  media/videos/bio8-1-7/480p15/Bio817Scene.mp4
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


class Bio817Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — две брзини                                ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Телото има две сообраќајни мрежи.",
                  font_size=38, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.4)
        self.wait(0.4)

        # Two columns: nerves vs hormones
        nerve_box = RoundedRectangle(width=5.5, height=2.6, corner_radius=0.3,
                                     fill_color="#10293a", fill_opacity=1,
                                     stroke_color=BLUE, stroke_width=2.5)
        nerve_box.move_to(LEFT*3.3 + DOWN*0.4)
        nerve_lbl = Text("Нерви", font_size=32, color=BLUE, weight=BOLD)
        nerve_lbl.move_to(nerve_box.get_top() + DOWN*0.4)
        nerve_l1 = Text("Зборуваат брзо.", font_size=24, color=WHITE2)
        nerve_l2 = Text("Дејството — мигнато.", font_size=22, color=GREY)
        nerve_l1.next_to(nerve_lbl, DOWN, buff=0.35)
        nerve_l2.next_to(nerve_l1, DOWN, buff=0.2)

        horm_box = RoundedRectangle(width=5.5, height=2.6, corner_radius=0.3,
                                    fill_color="#2a1a3a", fill_opacity=1,
                                    stroke_color=PURPLE, stroke_width=2.5)
        horm_box.move_to(RIGHT*3.3 + DOWN*0.4)
        horm_lbl = Text("Хормони", font_size=32, color=PURPLE, weight=BOLD)
        horm_lbl.move_to(horm_box.get_top() + DOWN*0.4)
        horm_l1 = Text("Зборуваат бавно.", font_size=24, color=WHITE2)
        horm_l2 = Text("Дејството — со часови.", font_size=22, color=GREY)
        horm_l1.next_to(horm_lbl, DOWN, buff=0.35)
        horm_l2.next_to(horm_l1, DOWN, buff=0.2)

        self.play(FadeIn(nerve_box), Write(nerve_lbl), run_time=0.8)
        self.play(FadeIn(nerve_l1), run_time=0.5)
        self.play(FadeIn(nerve_l2), run_time=0.5)
        self.wait(0.3)

        self.play(FadeIn(horm_box), Write(horm_lbl), run_time=0.8)
        self.play(FadeIn(horm_l1), run_time=0.5)
        self.play(FadeIn(horm_l2), run_time=0.5)
        self.wait(0.4)

        finisher = Text("Но дејството трае подолго.",
                        font_size=30, color=ORANGE, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.5)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(h1, nerve_box, nerve_lbl, nerve_l1, nerve_l2,
                                 horm_box, horm_lbl, horm_l1, horm_l2,
                                 finisher)),
                  run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 2.  ЖЛЕЗДИ ВО ТЕЛОТО                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("glands")

        title = section_title("Ендокрини жлезди", color=YELLOW)
        self.play(Write(title), run_time=0.8)

        # body silhouette
        head = Circle(radius=0.55, color=WHITE2,
                      fill_color=DARK_CARD, fill_opacity=1, stroke_width=2)
        head.move_to(LEFT*3.5 + UP*2.3)
        torso = RoundedRectangle(width=2.0, height=3.0, corner_radius=0.4,
                                 fill_color=DARK_CARD, fill_opacity=1,
                                 stroke_color=WHITE2, stroke_width=2)
        torso.next_to(head, DOWN, buff=0.05)
        legs = Rectangle(width=1.8, height=1.2,
                         fill_color=DARK_CARD, fill_opacity=1,
                         stroke_color=WHITE2, stroke_width=2)
        legs.next_to(torso, DOWN, buff=0.05)

        body = VGroup(head, torso, legs)
        self.play(FadeIn(body), run_time=0.8)

        # glands as dots on the body
        pituitary = Dot(head.get_center() + DOWN*0.2, color=YELLOW, radius=0.08)
        thyroid   = Dot(torso.get_top() + DOWN*0.25, color=GREEN, radius=0.08)
        adrenal_l = Dot(torso.get_center() + LEFT*0.4 + UP*0.2, color=RED, radius=0.08)
        adrenal_r = Dot(torso.get_center() + RIGHT*0.4 + UP*0.2, color=RED, radius=0.08)
        pancreas  = Dot(torso.get_center() + DOWN*0.3, color=BLUE, radius=0.08)
        gonad_l   = Dot(torso.get_bottom() + LEFT*0.25 + UP*0.15, color=PURPLE, radius=0.08)
        gonad_r   = Dot(torso.get_bottom() + RIGHT*0.25 + UP*0.15, color=PURPLE, radius=0.08)

        # labels on right
        labels = VGroup(
            VGroup(Dot(color=YELLOW, radius=0.08),
                   Text("Хипофиза — главен диригент", font_size=22, color=WHITE2)),
            VGroup(Dot(color=GREEN, radius=0.08),
                   Text("Тироидеа — метаболизам", font_size=22, color=WHITE2)),
            VGroup(Dot(color=RED, radius=0.08),
                   Text("Надбубрежни — стрес", font_size=22, color=WHITE2)),
            VGroup(Dot(color=BLUE, radius=0.08),
                   Text("Панкреас — шеќер", font_size=22, color=WHITE2)),
            VGroup(Dot(color=PURPLE, radius=0.08),
                   Text("Полови жлезди — развој", font_size=22, color=WHITE2)),
        )
        for row in labels:
            row.arrange(RIGHT, buff=0.25)
        labels.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        labels.move_to(RIGHT*2.7 + UP*0.0)

        # animate dot + label pairs
        gland_pairs = [
            (pituitary, labels[0]),
            (thyroid,   labels[1]),
            (VGroup(adrenal_l, adrenal_r), labels[2]),
            (pancreas,  labels[3]),
            (VGroup(gonad_l, gonad_r), labels[4]),
        ]
        for gland, lbl in gland_pairs:
            self.play(FadeIn(gland), FadeIn(lbl, shift=LEFT*0.2), run_time=0.6)
            self.wait(0.15)

        self.wait(1.4)

        all_dots = VGroup(pituitary, thyroid, adrenal_l, adrenal_r,
                          pancreas, gonad_l, gonad_r)
        self.play(FadeOut(VGroup(title, body, all_dots, labels)),
                  run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 3.  ХОРМОНИТЕ КАКО ПОРАКИ                            ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("messengers")

        title = section_title("Хормоните — хемиски пораки", color=GREEN)
        self.play(Write(title), run_time=0.8)

        # gland on left
        gland = Circle(radius=0.6, color=YELLOW,
                       fill_color=YELLOW, fill_opacity=0.7,
                       stroke_color=WHITE2, stroke_width=2)
        gland.move_to(LEFT*5 + UP*0.5)
        g_lbl = Text("Жлезда", font_size=20, color=WHITE2)
        g_lbl.next_to(gland, DOWN, buff=0.2)

        # blood vessel (long curve)
        vessel = Line(LEFT*4 + UP*0.5, RIGHT*4 + UP*0.5,
                      color=RED, stroke_width=6)
        vessel_lbl = Text("крвоток", font_size=18, color=RED)
        vessel_lbl.next_to(vessel, UP, buff=0.15).shift(LEFT*1)

        # target cell on right
        cell = Square(side_length=1.0, color=GREEN,
                      fill_color=GREEN, fill_opacity=0.5,
                      stroke_color=WHITE2, stroke_width=2)
        cell.move_to(RIGHT*5 + UP*0.5)
        c_lbl = Text("Целна клетка", font_size=20, color=WHITE2)
        c_lbl.next_to(cell, DOWN, buff=0.2)

        self.play(FadeIn(gland), Write(g_lbl),
                  Create(vessel), Write(vessel_lbl),
                  FadeIn(cell), Write(c_lbl), run_time=1.2)
        self.wait(0.3)

        # hormones travel
        hormones = VGroup(*[
            Dot(gland.get_center(), color=ORANGE, radius=0.1)
            for _ in range(5)
        ])
        self.add(hormones)

        anims = []
        for i, h in enumerate(hormones):
            anims.append(h.animate.move_to(cell.get_center()))
        self.play(*anims, run_time=2.2, rate_func=linear)
        self.play(Flash(cell.get_center(), color=YELLOW,
                        flash_radius=0.8, num_lines=12), run_time=0.6)
        self.wait(0.3)

        msg = Text("Хормонот наоѓа само СВОЈА клетка.",
                   font_size=26, color=ORANGE, weight=BOLD)
        msg.to_edge(DOWN, buff=0.5)
        self.play(Write(msg), run_time=1.1)
        self.wait(1.6)

        mess_grp = VGroup(gland, g_lbl, vessel, vessel_lbl,
                          cell, c_lbl, hormones, msg)
        self.play(FadeOut(VGroup(title, mess_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 4.  ИНСУЛИН ↔ ГЛУКАГОН                               ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("blood-sugar")

        title = section_title("Шеќер во крвта — рамнотежа", color=BLUE)
        self.play(Write(title), run_time=0.8)

        # balance bar (a horizontal beam pivoted in middle)
        fulcrum = Triangle(color=GREY, fill_color=GREY, fill_opacity=1).scale(0.35)
        fulcrum.move_to(DOWN*1.5)
        beam = Line(LEFT*3 + DOWN*1.0, RIGHT*3 + DOWN*1.0,
                    color=WHITE2, stroke_width=5)

        # left pan: insulin (lowers sugar)
        ins_box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.2,
                                   fill_color="#10293a", fill_opacity=1,
                                   stroke_color=BLUE, stroke_width=2)
        ins_box.move_to(LEFT*3 + UP*0.0)
        ins_lbl = Text("Инсулин", font_size=26, color=BLUE, weight=BOLD)
        ins_lbl.move_to(ins_box)
        ins_arrow = Text("↓ шеќер", font_size=22, color=BLUE)
        ins_arrow.next_to(ins_box, UP, buff=0.2)
        ins_grp = VGroup(ins_box, ins_lbl, ins_arrow)

        # right pan: glucagon (raises sugar)
        glu_box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.2,
                                   fill_color="#3a2510", fill_opacity=1,
                                   stroke_color=ORANGE, stroke_width=2)
        glu_box.move_to(RIGHT*3 + UP*0.0)
        glu_lbl = Text("Глукагон", font_size=26, color=ORANGE, weight=BOLD)
        glu_lbl.move_to(glu_box)
        glu_arrow = Text("↑ шеќер", font_size=22, color=ORANGE)
        glu_arrow.next_to(glu_box, UP, buff=0.2)
        glu_grp = VGroup(glu_box, glu_lbl, glu_arrow)

        self.play(Create(beam), FadeIn(fulcrum), run_time=0.7)
        self.play(FadeIn(ins_grp), FadeIn(glu_grp), run_time=0.9)
        self.wait(0.4)

        # show source — pancreas
        source = Text("Извор: панкреас", font_size=22, color=YELLOW)
        source.next_to(fulcrum, DOWN, buff=0.25)
        self.play(Write(source), run_time=0.8)
        self.wait(0.3)

        # Below: a numeric range
        scale_line = NumberLine(
            x_range=[3.5, 7.5, 0.5],
            length=8,
            include_numbers=True,
            font_size=20,
            color=GREY,
        )
        scale_line.next_to(source, DOWN, buff=0.5)
        marker = Dot(scale_line.n2p(5.5), color=GREEN, radius=0.12)
        marker_lbl = Text("норма ~5,5 mmol/L", font_size=18, color=GREEN)
        marker_lbl.next_to(marker, UP, buff=0.15)

        self.play(Create(scale_line), run_time=0.8)
        self.play(FadeIn(marker), Write(marker_lbl), run_time=0.7)
        self.wait(0.4)

        # show: high -> insulin -> down
        high_dot = Dot(scale_line.n2p(7), color=RED, radius=0.12)
        self.play(Transform(marker, high_dot),
                  marker_lbl.animate.next_to(high_dot, UP, buff=0.15).set_color(RED),
                  Indicate(ins_grp, color=BLUE), run_time=1.0)
        marker_lbl_v = Text("высок шеќер", font_size=18, color=RED)
        marker_lbl_v.next_to(high_dot, UP, buff=0.15)
        self.wait(0.4)

        low_dot = Dot(scale_line.n2p(5.5), color=GREEN, radius=0.12)
        self.play(Transform(marker, low_dot),
                  marker_lbl.animate.next_to(low_dot, UP, buff=0.15).set_color(GREEN),
                  run_time=0.9)
        self.wait(0.4)

        # low -> glucagon -> up
        low2 = Dot(scale_line.n2p(4), color=ORANGE, radius=0.12)
        self.play(Transform(marker, low2),
                  marker_lbl.animate.next_to(low2, UP, buff=0.15).set_color(ORANGE),
                  Indicate(glu_grp, color=ORANGE), run_time=1.0)
        self.wait(0.4)

        back = Dot(scale_line.n2p(5.5), color=GREEN, radius=0.12)
        self.play(Transform(marker, back),
                  marker_lbl.animate.next_to(back, UP, buff=0.15).set_color(GREEN),
                  run_time=0.9)
        self.wait(0.8)

        balance_grp = VGroup(beam, fulcrum, ins_grp, glu_grp, source,
                             scale_line, marker, marker_lbl)
        self.play(FadeOut(VGroup(title, balance_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 5.  АДРЕНАЛИН — БОРБА ИЛИ БЕГ                        ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("adrenaline")

        title = section_title("Адреналин — борба или бег", color=RED)
        self.play(Write(title), run_time=0.8)

        # trigger
        trigger = callout("Опасност!", border=RED, bg="#3a1010",
                          font_size=32, width=4.5)
        trigger.to_edge(UP, buff=1.4)
        self.play(FadeIn(trigger, shift=DOWN*0.2), run_time=0.7)
        self.wait(0.3)

        # adrenal gland icon
        adrenal = Triangle(color=RED, fill_color=RED, fill_opacity=0.8,
                           stroke_color=WHITE2, stroke_width=2).scale(0.5)
        adrenal.move_to(LEFT*5 + DOWN*0.3)
        a_lbl = Text("Надбубрежна жлезда", font_size=18, color=WHITE2)
        a_lbl.next_to(adrenal, DOWN, buff=0.2)

        self.play(FadeIn(adrenal), Write(a_lbl), run_time=0.7)

        arrow = Arrow(adrenal.get_right(), adrenal.get_right() + RIGHT*1.0,
                      color=RED, stroke_width=4)
        adr_lbl = Text("Адреналин", font_size=24, color=RED, weight=BOLD)
        adr_lbl.next_to(arrow, UP, buff=0.15)
        self.play(GrowArrow(arrow), Write(adr_lbl), run_time=0.7)

        # cascade effects
        effects = VGroup(
            Text("• Срцето чука побрзо.", font_size=22, color=YELLOW),
            Text("• Зениците се шират.", font_size=22, color=ORANGE),
            Text("• Дишењето се забрзува.", font_size=22, color=GREEN),
            Text("• Мускулите примаат повеќе крв.", font_size=22, color=BLUE),
            Text("• Шеќерот скока во крвта.", font_size=22, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        effects.move_to(RIGHT*1.5 + DOWN*0.3)

        for e in effects:
            self.play(FadeIn(e, shift=LEFT*0.2), run_time=0.4)
            self.wait(0.1)

        self.wait(0.8)

        finisher = Text("Тело — подготвено за акција.",
                        font_size=28, color=RED, weight=BOLD)
        finisher.to_edge(DOWN, buff=0.4)
        self.play(Write(finisher), run_time=1.0)
        self.wait(1.5)

        adr_grp = VGroup(trigger, adrenal, a_lbl, arrow, adr_lbl,
                         effects, finisher)
        self.play(FadeOut(VGroup(title, adr_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 6.  СПОРЕДБА — НЕРВИ vs ХОРМОНИ                      ~25 s
        # ══════════════════════════════════════════════════════════
        self.next_section("compare")

        title = section_title("Кратка споредба", color=PURPLE)
        self.play(Write(title), run_time=0.8)

        # Table-like rows
        rows = VGroup(
            VGroup(Text("Брзина:", font_size=24, color=YELLOW, weight=BOLD),
                   Text("милисекунди", font_size=22, color=BLUE),
                   Text("минути–часови", font_size=22, color=PURPLE)),
            VGroup(Text("Пат:", font_size=24, color=YELLOW, weight=BOLD),
                   Text("нерви", font_size=22, color=BLUE),
                   Text("крв", font_size=22, color=PURPLE)),
            VGroup(Text("Траење:", font_size=24, color=YELLOW, weight=BOLD),
                   Text("краткотрајно", font_size=22, color=BLUE),
                   Text("долготрајно", font_size=22, color=PURPLE)),
            VGroup(Text("Цел:", font_size=24, color=YELLOW, weight=BOLD),
                   Text("конкретна", font_size=22, color=BLUE),
                   Text("повеќе клетки", font_size=22, color=PURPLE)),
        )
        for r in rows:
            r.arrange(RIGHT, buff=1.0)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.move_to(ORIGIN + DOWN*0.2)

        # header row
        hdr = VGroup(
            Text(" ", font_size=24),
            Text("Нерви", font_size=26, color=BLUE, weight=BOLD),
            Text("Хормони", font_size=26, color=PURPLE, weight=BOLD),
        ).arrange(RIGHT, buff=1.0)
        hdr.next_to(rows, UP, buff=0.4)

        self.play(Write(hdr), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=UP*0.1), run_time=0.45)
            self.wait(0.1)

        self.wait(1.4)
        cmp_grp = VGroup(hdr, rows)
        self.play(FadeOut(VGroup(title, cmp_grp)), run_time=0.9)

        # ══════════════════════════════════════════════════════════
        # 7.  FINISHER                                         ~18 s
        # ══════════════════════════════════════════════════════════
        self.next_section("close")

        f1 = Text("Нервите вреат.", font_size=44, color=BLUE, weight=BOLD)
        f2 = Text("Хормоните течат.", font_size=44, color=PURPLE, weight=BOLD)
        f3 = Text("Заедно — телото живее.",
                  font_size=44, color=YELLOW, weight=BOLD)
        f4 = Text("Хармонија.", font_size=54, color=GREEN, weight=BOLD)

        block = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN)

        for line in [f1, f2, f3]:
            self.play(Write(line), run_time=0.7)
            self.wait(0.2)
        self.play(Write(f4), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(block), run_time=1.0)
        self.wait(0.5)
