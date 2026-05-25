"""
phys8-3-1  —  Само-светлечки и несветлечки предмети
Физика 8, Единица 3: Светлина

Teaching narrative — Andonovski-style text.
Render:  manim -ql phys8-3-1.py Phys831Scene
Output:  media/videos/phys8-3-1/480p15/Phys831Scene.mp4
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


class Phys831Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                           ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook = Text("Зошто ја гледаме Месечината?",
                    font_size=44, color=YELLOW, weight=BOLD)
        hook.to_edge(UP, buff=0.55)
        self.play(Write(hook), run_time=1.3)
        self.wait(0.7)

        ans1 = Text("Не затоа што свети.", font_size=34, color=WHITE2, weight=BOLD)
        ans2 = Text("Туку затоа што одбива сончева светлина.", font_size=34, color=WHITE2)
        ans1.shift(UP * 0.4)
        ans2.next_to(ans1, DOWN, buff=0.3)
        self.play(FadeIn(ans1, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeIn(ans2, shift=UP * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hook), FadeOut(ans1), FadeOut(ans2))

        # ══════════════════════════════════════════════════════════
        # 2.  КЛАСИФИКАЦИЈА — МРЕЖА                          ~20 s
        # ══════════════════════════════════════════════════════════
        self.next_section("classification")

        hdr = section_title("Светлечки и несветлечки предмети")
        self.play(Write(hdr), run_time=0.9)

        pri_panel = RoundedRectangle(
            width=6.2, height=5.2, corner_radius=0.35,
            fill_color="#1f1408", fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2,
        ).shift(LEFT * 3.5 + DOWN * 0.8)
        pri_title = Text("Примарни извори", font_size=26, color=YELLOW, weight=BOLD)
        pri_title.next_to(pri_panel.get_top(), DOWN, buff=0.3)
        pri_sub = Text("(само-светлечки)", font_size=19, color=GREY)
        pri_sub.next_to(pri_title, DOWN, buff=0.06)

        pri_items = VGroup(
            Text("☀  Сонце, ѕвезди",       font_size=22, color=WHITE2),
            Text("🔥 Оган, свеќа",          font_size=22, color=WHITE2),
            Text("💡 Сијалица, LED",        font_size=22, color=WHITE2),
            Text("⚡ Молња",               font_size=22, color=WHITE2),
            Text("🌊 Медуза (биолум.)",    font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        pri_items.next_to(pri_sub, DOWN, buff=0.4)

        sec_panel = RoundedRectangle(
            width=6.2, height=5.2, corner_radius=0.35,
            fill_color="#0b1e30", fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).shift(RIGHT * 3.5 + DOWN * 0.8)
        sec_title = Text("Секундарни извори", font_size=26, color=BLUE, weight=BOLD)
        sec_title.next_to(sec_panel.get_top(), DOWN, buff=0.3)
        sec_sub = Text("(одбивачи на светлина)", font_size=19, color=GREY)
        sec_sub.next_to(sec_title, DOWN, buff=0.06)

        sec_items = VGroup(
            Text("🌕 Месечина, планети", font_size=22, color=WHITE2),
            Text("📖 Хартија, книги",    font_size=22, color=WHITE2),
            Text("🪞 Огледало",         font_size=22, color=WHITE2),
            Text("🧱 Ѕидови, предмети", font_size=22, color=WHITE2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        sec_items.next_to(sec_sub, DOWN, buff=0.4)

        self.play(Create(pri_panel))
        self.play(Write(pri_title), Write(pri_sub))
        for item in pri_items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.32)

        self.play(Create(sec_panel))
        self.play(Write(sec_title), Write(sec_sub))
        for item in sec_items:
            self.play(FadeIn(item, shift=LEFT * 0.2), run_time=0.32)

        self.wait(2.0)
        self.play(*[FadeOut(m) for m in [
            hdr,
            pri_panel, pri_title, pri_sub, pri_items,
            sec_panel, sec_title, sec_sub, sec_items,
        ]])

        # ══════════════════════════════════════════════════════════
        # 3.  ЗОШТО ГО ГЛЕДАМЕ — ЗРАЧЕН ДИЈАГРАМ             ~14 s
        # ══════════════════════════════════════════════════════════
        self.next_section("ray_diagram")

        hdr2 = section_title("Зошто го гледаме предметот?")
        self.play(Write(hdr2), run_time=0.9)

        # source → object → eye
        src = Circle(radius=0.4, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        src.shift(LEFT * 5.5)
        src_lbl = Text("Извор", font_size=20, color=YELLOW, weight=BOLD)
        src_lbl.next_to(src, DOWN, buff=0.2)

        obj = RoundedRectangle(width=0.8, height=1.1, corner_radius=0.12,
                               fill_color=ORANGE, fill_opacity=0.9, stroke_width=0)
        obj.shift(LEFT * 1.5)
        obj_lbl = Text("Предмет", font_size=20, color=ORANGE, weight=BOLD)
        obj_lbl.next_to(obj, DOWN, buff=0.2)

        eye = Circle(radius=0.35, fill_color=DARK_CARD, fill_opacity=1,
                     stroke_color=BLUE, stroke_width=2)
        eye.shift(RIGHT * 4.5)
        eye_dot = Dot(eye.get_center(), color=BLUE, radius=0.12)
        eye_lbl = Text("Oko", font_size=20, color=BLUE, weight=BOLD)
        eye_lbl.next_to(eye, DOWN, buff=0.2)

        self.play(FadeIn(src), Write(src_lbl))
        self.play(FadeIn(obj), Write(obj_lbl))
        self.play(FadeIn(eye), FadeIn(eye_dot), Write(eye_lbl))

        ray1 = Arrow(src.get_right(), obj.get_left(),
                     color=YELLOW, buff=0.08, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.18)
        ray2 = Arrow(obj.get_right(), eye.get_left(),
                     color=YELLOW, buff=0.08, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.18)

        self.play(GrowArrow(ray1))
        self.wait(0.3)
        self.play(GrowArrow(ray2))
        self.wait(0.5)

        note = callout(
            "Светлина → удира → делумно се одбива → влегува во окото → мозокот создава слика",
            width=12.0, bg="#0d2233", border=BLUE, font_size=20,
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [
            hdr2, src, src_lbl, obj, obj_lbl, eye, eye_dot, eye_lbl, ray1, ray2, note,
        ]])

        # ══════════════════════════════════════════════════════════
        # 4.  БРЗИНА НА СВЕТЛИНА                             ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("speed_of_light")

        hdr3 = section_title("Брзина на светлина")
        self.play(Write(hdr3), run_time=0.8)

        c_big = Text("c = 300 000 km/s", font_size=64, color=YELLOW, weight=BOLD)
        c_big.shift(UP * 0.8)
        self.play(Write(c_big), run_time=1.0)
        self.play(Indicate(c_big, scale_factor=1.1, color=YELLOW))
        self.wait(0.7)

        facts = VGroup(
            Text("Сонце → Земја:  8 минути", font_size=26, color=ORANGE),
            Text("Месечина → Земја:  1.3 секунди", font_size=26, color=BLUE),
            Text("Најбрзото нешто во вселената.", font_size=26, color=WHITE2),
        ).arrange(DOWN, buff=0.35)
        facts.shift(DOWN * 0.8)

        for f in facts:
            self.play(FadeIn(f, shift=UP * 0.2), run_time=0.6)
            self.wait(0.4)

        self.wait(1.5)
        self.play(FadeOut(hdr3), FadeOut(c_big), FadeOut(facts))

        # ══════════════════════════════════════════════════════════
        # 5.  ПРОЅИРНОСТ                                      ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("transparency")

        hdr4 = section_title("Проѕирност на материјалите")
        self.play(Write(hdr4), run_time=0.8)

        trans_data = [
            ("Проѕирни",      "стакло, вода, воздух",     BLUE,   1.0),
            ("Полупроѕирни",  "матово стакло, мускавит",  ORANGE, 0.55),
            ("Непроѕирни",    "дрво, метал, бетон",       GREY,   0.15),
        ]

        trans_cards = VGroup()
        for name, example, col, opacity in trans_data:
            bg = RoundedRectangle(
                width=10.5, height=1.0, corner_radius=0.2,
                fill_color=f"{col}20", fill_opacity=1,
                stroke_color=col, stroke_width=1.8,
            )
            nt = Text(name, font_size=24, color=col, weight=BOLD)
            nt.next_to(bg.get_left(), RIGHT, buff=0.3)
            et = Text(example, font_size=21, color=WHITE2)
            et.move_to(bg).shift(RIGHT * 1.0)
            # mini opacity bar
            bar_bg = Rectangle(width=1.4, height=0.35,
                               fill_color=DARK_CARD, fill_opacity=1, stroke_width=0)
            bar_fg = Rectangle(width=1.4 * opacity, height=0.35,
                               fill_color=col, fill_opacity=0.85, stroke_width=0)
            bar_fg.align_to(bar_bg, LEFT)
            bar_grp = VGroup(bar_bg, bar_fg)
            bar_grp.next_to(bg.get_right(), LEFT, buff=0.3)
            trans_cards.add(VGroup(bg, nt, et, bar_grp))

        trans_cards.arrange(DOWN, buff=0.35)
        trans_cards.shift(DOWN * 0.5)

        for card in trans_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.5)

        straight_note = callout(
            "Светлината се шири праволиниски → причина за сенки",
            width=10.5, bg="#0d2233", border=GREEN, font_size=24,
        )
        straight_note.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(straight_note, shift=UP * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hdr4), FadeOut(trans_cards), FadeOut(straight_note))

        # ══════════════════════════════════════════════════════════
        # 6.  АНDONОВСКИ МОМЕНТ                              ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("andonovski")

        lines_ando = [
            ("Кога гледаш ѕвезда —",           WHITE2, 34),
            ("гледаш минатото.",                WHITE2, 36),
            ("Светлина која патувала години.", WHITE2, 30),
            ("Можеби ѕвездата веќе не постои.", WHITE2, 28),
            ("Но светлина — патува уште.",      YELLOW, 40),
        ]

        grp = VGroup()
        for txt, col, fs in lines_ando:
            grp.add(Text(txt, font_size=fs, color=col, weight=BOLD))
        grp.arrange(DOWN, buff=0.34)

        for line in grp:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.42)

        self.play(Indicate(grp[-1], scale_factor=1.2, color=YELLOW))
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
            (YELLOW, "Примарни: сами светат (Сонце, оган, LED)"),
            (BLUE,   "Секундарни: одбиваат светлина (Месечина, хартија)"),
            (ORANGE, "Зрак: извор → предмет → одбивање → oko → мозок"),
            (GREEN,  "c = 300 000 km/s — најбрзо во вселената"),
            (GREY,   "Проѕирни / полупроѕирни / непроѕирни"),
        ]

        rows = VGroup()
        for col, txt in bullets:
            dot = Circle(radius=0.13, fill_color=col, fill_opacity=1, stroke_width=0)
            t = Text(txt, font_size=23, color=WHITE2)
            t.next_to(dot, RIGHT, buff=0.22)
            rows.add(VGroup(dot, t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.shift(DOWN * 0.65 + RIGHT * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.28), run_time=0.5)
            self.wait(0.42)

        self.wait(3.0)
