"""
geo8-3-2  —  Италија и Апенински Полуостров
Географија 8, Единица 3: Јужна Европа

Teaching narrative — Andonovski-style: three-beat punches,
Italy as a boot, peninsulas as branches of land.
Render:  manim -ql geo8-3-2.py Geo832Scene
Output:  media/videos/geo8-3-2/480p15/Geo832Scene.mp4
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


def city_dot(name, pos, color=YELLOW, fs=18):
    d = Dot(pos, radius=0.10, color=color)
    lab = Text(name, font_size=fs, color=color, weight=BOLD)
    lab.next_to(d, RIGHT, buff=0.15)
    return VGroup(d, lab)


class Geo832Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — "Италија е чизма"                      ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Италија е чизма.", font_size=58, color=YELLOW, weight=BOLD)
        h1.to_edge(UP, buff=0.7)
        self.play(Write(h1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Со потпетица — Калабрија.", font_size=36, color=ORANGE),
            Text("Со прст — Сицилија.", font_size=36, color=RED),
            Text("Сите ја знаат.", font_size=36, color=WHITE2),
            Text("Сите ѝ се восхитуваат.", font_size=40, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.32).next_to(h1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.55)
            self.wait(0.18)

        self.wait(0.8)
        self.play(FadeOut(VGroup(h1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  THE BOOT SHAPE                                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("boot")

        t2 = section_title("Чизмата на Европа")
        self.play(Write(t2), run_time=0.8)

        # Boot outline — north thicker, narrowing south
        boot = Polygon(
            [-1.2,  2.4, 0],   # NW (Alps)
            [ 1.2,  2.5, 0],   # NE
            [ 1.5,  1.5, 0],   # north-east coast
            [ 0.8,  0.5, 0],
            [ 1.0, -0.5, 0],
            [ 0.5, -1.5, 0],
            [ 1.2, -2.0, 0],   # heel
            [ 1.8, -2.2, 0],
            [ 1.6, -2.6, 0],   # tip of heel
            [ 0.2, -2.4, 0],
            [-0.4, -1.8, 0],
            [-0.2, -1.2, 0],
            [-0.5, -0.6, 0],
            [-0.8,  0.4, 0],
            [-1.0,  1.4, 0],
            fill_color="#3d6b4a", fill_opacity=0.8,
            stroke_color=GREEN, stroke_width=3,
        )

        # Sicily (toe)
        sicily = RegularPolygon(n=3, color=GREEN,
            fill_color="#3d6b4a", fill_opacity=0.8, stroke_width=2)
        sicily.scale(0.55).rotate(PI).move_to([-1.6, -2.6, 0])

        # Sardinia
        sardinia = Ellipse(width=0.7, height=1.2,
            fill_color="#3d6b4a", fill_opacity=0.8,
            stroke_color=GREEN, stroke_width=2)
        sardinia.move_to([-2.6, -0.8, 0])

        self.play(FadeIn(boot), run_time=1.0)
        self.play(FadeIn(sicily), FadeIn(sardinia), run_time=0.8)

        lab_sic = Text("Сицилија", font_size=18, color=YELLOW, weight=BOLD)
        lab_sic.next_to(sicily, DOWN, buff=0.15)
        lab_sar = Text("Сардинија", font_size=18, color=YELLOW, weight=BOLD)
        lab_sar.next_to(sardinia, LEFT, buff=0.15)
        lab_heel = Text("Калабрија", font_size=16, color=ORANGE)
        lab_heel.move_to([2.6, -2.0, 0])
        arr_heel = Arrow(lab_heel.get_left(), [1.7, -2.2, 0], color=ORANGE, buff=0.05, stroke_width=3)

        self.play(Write(lab_sic), Write(lab_sar), run_time=0.8)
        self.play(Write(lab_heel), GrowArrow(arr_heel), run_time=0.7)

        seas = VGroup(
            Text("Јадранско\nморе", font_size=16, color=BLUE).move_to([3.5, 0.5, 0]),
            Text("Тиренско\nморе", font_size=16, color=BLUE).move_to([-3.0, -2.0, 0]),
            Text("Јонско\nморе", font_size=16, color=BLUE).move_to([3.5, -2.3, 0]),
        )
        for s in seas:
            self.play(FadeIn(s), run_time=0.4)

        info = Text("Околу 1200 km од север до југ.", font_size=24, color=WHITE2, weight=BOLD)
        info.to_edge(DOWN, buff=0.5)
        self.play(Write(info), run_time=0.8)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t2, boot, sicily, sardinia, lab_sic, lab_sar,
                                  lab_heel, arr_heel, seas, info)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 3.  APENNINES — spine                               ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("apennines")

        t3 = section_title("Апенини — рбетот на чизмата")
        self.play(Write(t3), run_time=0.8)

        # Spine curve
        spine = ParametricFunction(
            lambda t: np.array([0.3*np.sin(2*t) + 0.5, 2.2 - 0.85*t, 0]),
            t_range=[0, 5], color=GREY, stroke_width=6,
        )
        self.play(Create(spine), run_time=2.0)

        # Alps to the north
        alps_curve = ParametricFunction(
            lambda t: np.array([t, 2.5 + 0.3*np.sin(3*t), 0]),
            t_range=[-3, 3], color=WHITE2, stroke_width=5,
        )
        alps_lab = Text("Алпи", font_size=22, color=WHITE2, weight=BOLD)
        alps_lab.next_to(alps_curve, UP, buff=0.1)
        self.play(Create(alps_curve), Write(alps_lab), run_time=1.2)

        spine_lab = Text("Апенини", font_size=22, color=GREY, weight=BOLD)
        spine_lab.move_to([2.5, 0.5, 0])
        arr_spine = Arrow(spine_lab.get_left(), [0.5, 0.5, 0], color=GREY, buff=0.1, stroke_width=3)
        self.play(Write(spine_lab), GrowArrow(arr_spine), run_time=0.8)

        # Po Valley
        po = Rectangle(width=4.0, height=0.5,
            fill_color="#4a7d3a", fill_opacity=0.7,
            stroke_color=GREEN, stroke_width=2)
        po.move_to([0, 1.7, 0])
        po_lab = Text("Падска низина", font_size=18, color=GREEN, weight=BOLD)
        po_lab.next_to(po, LEFT, buff=0.2)
        self.play(FadeIn(po), Write(po_lab), run_time=0.8)

        facts = VGroup(
            Text("Апенините се протегаат низ целата земја.", font_size=22, color=WHITE2),
            Text("Падската низина — житница на север.", font_size=22, color=GREEN),
            Text("Везув и Етна — вулкани кои дишат.", font_size=22, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.4)

        for f in facts:
            self.play(FadeIn(f, shift=UP*0.15), run_time=0.6)
            self.wait(0.18)

        self.wait(1.0)
        self.play(FadeOut(VGroup(t3, spine, alps_curve, alps_lab, spine_lab,
                                  arr_spine, po, po_lab, facts)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 4.  CITIES — Rome, Milan, Naples                    ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("cities")

        t4 = section_title("Три градови. Три карактери.")
        self.play(Write(t4), run_time=0.8)

        rome = country_card_v = RoundedRectangle(
            width=3.8, height=2.2, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=YELLOW, stroke_width=2,
        ).move_to([-4.0, 0.5, 0])
        r_nm = Text("Рим", font_size=30, color=YELLOW, weight=BOLD).move_to(rome.get_top()+DOWN*0.4)
        r_l1 = Text("Главен град", font_size=18, color=WHITE2).move_to(rome.get_center()+UP*0.1)
        r_l2 = Text("Вечниот град", font_size=16, color=GREY).move_to(rome.get_center()+DOWN*0.3)
        r_l3 = Text("Колосеум • Ватикан", font_size=14, color=ORANGE).move_to(rome.get_bottom()+UP*0.3)
        rome_g = VGroup(rome, r_nm, r_l1, r_l2, r_l3)

        mil = RoundedRectangle(
            width=3.8, height=2.2, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).move_to([0.0, 0.5, 0])
        m_nm = Text("Милано", font_size=30, color=BLUE, weight=BOLD).move_to(mil.get_top()+DOWN*0.4)
        m_l1 = Text("Север. Богатство.", font_size=18, color=WHITE2).move_to(mil.get_center()+UP*0.1)
        m_l2 = Text("Мода. Индустрија.", font_size=16, color=GREY).move_to(mil.get_center()+DOWN*0.3)
        m_l3 = Text("Срцето на бизнисот", font_size=14, color=ORANGE).move_to(mil.get_bottom()+UP*0.3)
        mil_g = VGroup(mil, m_nm, m_l1, m_l2, m_l3)

        nap = RoundedRectangle(
            width=3.8, height=2.2, corner_radius=0.2,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=RED, stroke_width=2,
        ).move_to([4.0, 0.5, 0])
        n_nm = Text("Неапол", font_size=30, color=RED, weight=BOLD).move_to(nap.get_top()+DOWN*0.4)
        n_l1 = Text("Југ. Страст.", font_size=18, color=WHITE2).move_to(nap.get_center()+UP*0.1)
        n_l2 = Text("Везув. Пица.", font_size=16, color=GREY).move_to(nap.get_center()+DOWN*0.3)
        n_l3 = Text("Стариот вкус", font_size=14, color=ORANGE).move_to(nap.get_bottom()+UP*0.3)
        nap_g = VGroup(nap, n_nm, n_l1, n_l2, n_l3)

        self.play(FadeIn(rome_g, shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(mil_g, shift=UP*0.2), run_time=0.7)
        self.play(FadeIn(nap_g, shift=UP*0.2), run_time=0.7)

        sum_t = Text("Еден народ. Три лица.", font_size=28, color=YELLOW, weight=BOLD)
        sum_t.to_edge(DOWN, buff=0.7)
        self.play(Write(sum_t), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t4, rome_g, mil_g, nap_g, sum_t)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 5.  VATICAN — smallest country                      ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vatican")

        t5 = section_title("Ватикан — држава во град")
        self.play(Write(t5), run_time=0.8)

        # Tiny circle next to a big circle
        big = Circle(radius=2.2, color=YELLOW, stroke_width=3,
                     fill_color=DARK_CARD, fill_opacity=0.5).shift(LEFT*2.5)
        big_l = Text("Рим\n1285 km²", font_size=20, color=YELLOW, weight=BOLD).move_to(big)

        tiny = Circle(radius=0.15, color=PURPLE, stroke_width=2,
                      fill_color=PURPLE, fill_opacity=0.7).move_to(big.get_center() + RIGHT*0.5)
        tiny_l = Text("Ватикан", font_size=18, color=PURPLE, weight=BOLD)
        tiny_l.move_to([3.0, 1.5, 0])
        arr_v = Arrow(tiny_l.get_left(), tiny.get_right(), color=PURPLE, buff=0.05, stroke_width=2)

        self.play(FadeIn(big), Write(big_l), run_time=0.8)
        self.play(FadeIn(tiny), Write(tiny_l), GrowArrow(arr_v), run_time=0.8)

        facts = VGroup(
            Text("0.49 km² — најмала држава на свет.", font_size=22, color=WHITE2),
            Text("Седиште на Папата.", font_size=22, color=PURPLE),
            Text("Држава во град. Град во држава.", font_size=22, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.2).shift(RIGHT*0.5+DOWN*1.0)

        for f in facts:
            self.play(FadeIn(f, shift=UP*0.15), run_time=0.6)
            self.wait(0.18)

        self.wait(1.2)
        self.play(FadeOut(VGroup(t5, big, big_l, tiny, tiny_l, arr_v, facts)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  ECONOMY & CULTURE                               ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("economy")

        t6 = section_title("Што дава Италија на светот?")
        self.play(Write(t6), run_time=0.8)

        # 4 quadrants
        quads = [
            ("Храна",       "Паста • Пица\nМаслинка • Вино",        GREEN,  [-3.2, 1.2, 0]),
            ("Уметност",    "Микеланџело\nЛеонардо да Винчи",       PURPLE, [ 3.2, 1.2, 0]),
            ("Мода",        "Гучи • Прада\nАрмани • Версаче",       BLUE,   [-3.2,-1.4, 0]),
            ("Автомобили",  "Ферари • Ламборгини\nФиат",            RED,    [ 3.2,-1.4, 0]),
        ]
        boxes = VGroup()
        for nm, det, col, pos in quads:
            box = RoundedRectangle(
                width=4.6, height=1.9, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            h = Text(nm, font_size=24, color=col, weight=BOLD).move_to(box.get_top()+DOWN*0.3)
            d = Text(det, font_size=16, color=WHITE2).move_to(box.get_center()+DOWN*0.2)
            boxes.add(VGroup(box, h, d))

        for b in boxes:
            self.play(FadeIn(b, scale=0.9), run_time=0.5)

        self.wait(0.6)

        msg = callout("Антички Рим живее. Денес во чизма.", width=8.5, border=YELLOW)
        msg.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(msg, shift=UP*0.2), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(t6, boxes, msg)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  CLOSING                                         ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        end1 = Text("Италија.", font_size=64, color=YELLOW, weight=BOLD)
        end1.move_to(UP * 1.6)
        self.play(Write(end1), run_time=1.0)

        end_lines = VGroup(
            Text("Чизма во море.", font_size=32, color=WHITE2),
            Text("Срце на медитеранот.", font_size=32, color=ORANGE),
            Text("Кујна на светот.", font_size=38, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).next_to(end1, DOWN, buff=0.5)

        for L in end_lines:
            self.play(FadeIn(L, shift=UP*0.15), run_time=0.7)
            self.wait(0.2)

        self.wait(2.0)
