"""
geo8-5-1  —  Скандинавски земји
Географија 8, Единица 5: Северна Европа

Teaching narrative — Andonovski-style: three-beat punches,
Scandinavia as cold-but-happy paradox. Not luck — system.
Five sisters of the north — fjords, forests, bridges, lakes, fire.
Render:  manim -ql geo8-5-1.py Geo851Scene
Output:  media/videos/geo8-5-1/480p15/Geo851Scene.mp4
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


def nordic_card(name, capital, icon, color, pos):
    box = RoundedRectangle(
        width=2.6, height=2.4, corner_radius=0.25,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    ic = Text(icon, font_size=30, color=color, weight=BOLD)
    ic.move_to(box.get_center() + UP * 0.7)
    nm = Text(name, font_size=20, color=color, weight=BOLD)
    nm.move_to(box.get_center() + UP * 0.05)
    cap = Text(capital, font_size=14, color=WHITE2)
    cap.move_to(box.get_center() + DOWN * 0.45)
    return VGroup(box, ic, nm, cap)


def hdi_bar(name, value, color, y):
    width = 7.0 * (value / 100)
    bar = Rectangle(width=width, height=0.5,
                    fill_color=color, fill_opacity=0.9,
                    stroke_color=color, stroke_width=1)
    bar.move_to(np.array([-3.0 + width / 2, y, 0]))
    nm = Text(name, font_size=18, color=WHITE2, weight=BOLD)
    nm.next_to(bar, LEFT, buff=0.2).align_to(bar, LEFT).shift(LEFT * 2.5)
    vl = Text(f"{value}", font_size=16, color=color, weight=BOLD)
    vl.next_to(bar, RIGHT, buff=0.15)
    return VGroup(bar, nm, vl)


class Geo851Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        h1 = Text("Скандинавија е ладна.", font_size=40, color=BLUE, weight=BOLD)
        h2 = Text("Темна половина година.", font_size=32, color=GREY)
        h3 = Text("Но среќна.", font_size=38, color=YELLOW, weight=BOLD)
        h4 = Text("Нордиските држави секогаш на врвот.", font_size=26, color=WHITE2)
        h5 = Text("Не среќа. Систем.", font_size=34, color=GREEN, weight=BOLD)

        hook = VGroup(h1, h2, h3, h4, h5).arrange(DOWN, buff=0.35)

        self.play(Write(h1), run_time=1.1)
        self.play(FadeIn(h2, shift=UP * 0.3), run_time=1.0)
        self.wait(0.4)
        self.play(Write(h3), run_time=1.0)
        self.play(FadeIn(h4), run_time=1.0)
        self.wait(0.3)
        self.play(Write(h5), run_time=1.2)
        self.wait(2.2)
        self.play(FadeOut(hook), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 2.  FIVE COUNTRIES                                  ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("five")

        t2 = section_title("Пет нордиски сестри", color=YELLOW)
        self.play(Write(t2), run_time=1.0)

        nor = nordic_card("Норвешка",  "Осло",       "Фјорди",  BLUE,   LEFT * 5.0 + UP * 0.3)
        swe = nordic_card("Шведска",   "Стокхолм",   "Шуми",    GREEN,  LEFT * 2.4 + UP * 0.3)
        den = nordic_card("Данска",    "Копенхаген", "Мостови", RED,    UP * 0.3)
        fin = nordic_card("Финска",    "Хелсинки",   "Езера",   PURPLE, RIGHT * 2.4 + UP * 0.3)
        ice = nordic_card("Исланд",    "Рејкјавик",  "Вулкани", ORANGE, RIGHT * 5.0 + UP * 0.3)

        self.play(FadeIn(nor, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(swe, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(den, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(fin, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(ice, shift=UP * 0.3), run_time=0.6)
        self.wait(0.6)

        co2 = callout("Различни. Но заедно — Северниот совет.",
                      width=11.0, bg="#0d2b44", border=BLUE, font_size=26)
        co2.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(co2, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t2), FadeOut(nor), FadeOut(swe), FadeOut(den),
                  FadeOut(fin), FadeOut(ice), FadeOut(co2), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  NORWAY — FJORDS & OIL                           ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("norway")

        t3 = section_title("Норвешка — фјорди и нафта", color=BLUE)
        self.play(Write(t3), run_time=1.0)

        # Fjord cross-section
        # mountain walls
        wall_l = Polygon(
            np.array([-5, 2, 0]), np.array([-2.5, 2, 0]),
            np.array([-2.0, -0.5, 0]), np.array([-5, -0.5, 0]),
            color=GREY, fill_color=GREY, fill_opacity=0.7, stroke_width=2,
        )
        wall_r = Polygon(
            np.array([2.0, 2, 0]), np.array([5, 2, 0]),
            np.array([5, -0.5, 0]), np.array([2.5, -0.5, 0]),
            color=GREY, fill_color=GREY, fill_opacity=0.7, stroke_width=2,
        )
        water = Polygon(
            np.array([-2.0, -0.5, 0]), np.array([2.5, -0.5, 0]),
            np.array([2.5, -2.5, 0]), np.array([-2.0, -2.5, 0]),
            color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=0,
        )

        self.play(FadeIn(wall_l), FadeIn(wall_r), run_time=1.0)
        self.play(FadeIn(water), run_time=0.8)

        fjord_lbl = Text("Фјорд", font_size=26, color=BLUE, weight=BOLD)
        fjord_lbl.move_to(water.get_center())
        mountain_lbl = Text("Карпи", font_size=20, color=GREY)
        mountain_lbl.move_to(wall_l.get_center())
        self.play(Write(fjord_lbl), Write(mountain_lbl), run_time=0.9)

        # oil rig (small)
        rig_base = Rectangle(width=1.0, height=0.3,
                             color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        rig_base.move_to(LEFT * 0.5 + DOWN * 0.7)
        rig_tower = Line(LEFT * 0.5 + DOWN * 0.5, LEFT * 0.5 + UP * 0.4,
                         color=ORANGE, stroke_width=4)
        rig_top = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=0.8)
        rig_top.scale(0.25).next_to(rig_tower, UP, buff=0.0)
        rig = VGroup(rig_base, rig_tower, rig_top)
        rig_lbl = Text("Нафтена платформа", font_size=14, color=ORANGE)
        rig_lbl.next_to(rig, UP, buff=0.2)

        self.play(FadeIn(rig), Write(rig_lbl), run_time=1.0)

        nor_facts = VGroup(
            Text("Најбогата нордиска земја", font_size=22, color=YELLOW),
            Text("Северно море — нафта и гас", font_size=20, color=ORANGE),
            Text("Не е членка на ЕУ", font_size=20, color=RED),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.4)
        self.play(Write(nor_facts), run_time=1.6)
        self.wait(2.0)
        self.play(FadeOut(t3), FadeOut(wall_l), FadeOut(wall_r), FadeOut(water),
                  FadeOut(fjord_lbl), FadeOut(mountain_lbl), FadeOut(rig),
                  FadeOut(rig_lbl), FadeOut(nor_facts), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  SWEDEN, DENMARK, FINLAND                        ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("swe_den_fin")

        t4 = section_title("Шведска, Данска, Финска", color=GREEN)
        self.play(Write(t4), run_time=1.0)

        # Three columns
        # Sweden
        swe_h = Text("Шведска", font_size=28, color=GREEN, weight=BOLD)
        swe_h.move_to(LEFT * 4.0 + UP * 2.2)
        swe_items = VGroup(
            Text("• 10 мил. жители", font_size=18, color=WHITE2),
            Text("• Шуми и железо", font_size=18, color=WHITE2),
            Text("• IKEA, Volvo, Spotify", font_size=18, color=YELLOW),
            Text("• Неутрална историски", font_size=18, color=GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        swe_items.next_to(swe_h, DOWN, buff=0.3).align_to(swe_h, LEFT)

        # Denmark
        den_h = Text("Данска", font_size=28, color=RED, weight=BOLD)
        den_h.move_to(UP * 2.2)
        den_items = VGroup(
            Text("• 5.9 мил. жители", font_size=18, color=WHITE2),
            Text("• Копенхаген", font_size=18, color=WHITE2),
            Text("• Лего, ветерници", font_size=18, color=YELLOW),
            Text("• Мост до Шведска", font_size=18, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        den_items.next_to(den_h, DOWN, buff=0.3).align_to(den_h, LEFT)

        # Finland
        fin_h = Text("Финска", font_size=28, color=PURPLE, weight=BOLD)
        fin_h.move_to(RIGHT * 4.0 + UP * 2.2)
        fin_items = VGroup(
            Text("• 5.5 мил. жители", font_size=18, color=WHITE2),
            Text("• 188.000 езера", font_size=18, color=BLUE),
            Text("• Nokia, дигитално", font_size=18, color=YELLOW),
            Text("• Сауна — секаде", font_size=18, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fin_items.next_to(fin_h, DOWN, buff=0.3).align_to(fin_h, LEFT)

        self.play(Write(swe_h), run_time=0.5)
        self.play(Write(swe_items), run_time=1.2)
        self.play(Write(den_h), run_time=0.5)
        self.play(Write(den_items), run_time=1.2)
        self.play(Write(fin_h), run_time=0.5)
        self.play(Write(fin_items), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(t4), FadeOut(swe_h), FadeOut(swe_items),
                  FadeOut(den_h), FadeOut(den_items),
                  FadeOut(fin_h), FadeOut(fin_items), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  ICELAND — FIRE AND ICE                          ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("iceland")

        t5 = section_title("Исланд — оган и мраз", color=ORANGE)
        self.play(Write(t5), run_time=1.0)

        # Volcano + glacier
        glacier = Polygon(
            np.array([-6, 0.5, 0]), np.array([-2, 0.5, 0]),
            np.array([-2.5, -2, 0]), np.array([-6, -2, 0]),
            color=WHITE2, fill_color=WHITE2, fill_opacity=0.7, stroke_width=2,
        )
        gl_lbl = Text("Глечер", font_size=22, color="#0d1b2e", weight=BOLD)
        gl_lbl.move_to(glacier.get_center())

        # volcano
        volcano = Polygon(
            np.array([0, -2, 0]), np.array([4, -2, 0]),
            np.array([3, 0.8, 0]), np.array([1, 0.8, 0]),
            color=GREY, fill_color=GREY, fill_opacity=0.9, stroke_color=GREY,
        )
        crater = Polygon(
            np.array([1, 0.8, 0]), np.array([3, 0.8, 0]),
            np.array([2.5, 0.4, 0]), np.array([1.5, 0.4, 0]),
            color=DARK_CARD, fill_color=DARK_CARD, fill_opacity=1,
        )
        lava1 = Polygon(
            np.array([1.6, 0.8, 0]), np.array([2.4, 0.8, 0]),
            np.array([2.7, 1.8, 0]), np.array([1.3, 1.8, 0]),
            color=RED, fill_color=RED, fill_opacity=0.85,
        )
        lava2 = Polygon(
            np.array([1.8, 1.5, 0]), np.array([2.2, 1.5, 0]),
            np.array([2.5, 2.5, 0]), np.array([1.5, 2.5, 0]),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.9,
        )
        vol_lbl = Text("Вулкан", font_size=22, color=ORANGE, weight=BOLD)
        vol_lbl.move_to(volcano.get_center() + DOWN * 0.5)

        self.play(FadeIn(glacier), Write(gl_lbl), run_time=1.0)
        self.play(FadeIn(volcano), FadeIn(crater), Write(vol_lbl), run_time=1.0)
        self.play(FadeIn(lava1), FadeIn(lava2), run_time=0.9)

        ice_facts = VGroup(
            Text("Геотермална енергија — 100% обновлива", font_size=22, color=GREEN),
            Text("Само 370.000 жители", font_size=20, color=WHITE2),
            Text("Викинзи го откриле — 9 век", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.4)
        self.play(Write(ice_facts), run_time=1.6)
        self.wait(2.0)
        self.play(FadeOut(t5), FadeOut(glacier), FadeOut(gl_lbl),
                  FadeOut(volcano), FadeOut(crater), FadeOut(lava1),
                  FadeOut(lava2), FadeOut(vol_lbl), FadeOut(ice_facts),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 6.  HAPPINESS INDEX                                 ~50 s
        # ══════════════════════════════════════════════════════════
        self.next_section("happiness")

        t6 = section_title("Среќа — нордиски рецепт", color=YELLOW)
        self.play(Write(t6), run_time=1.0)

        # Stylized HDI/happiness scores (illustrative)
        bars = VGroup(
            hdi_bar("Финска",        96, PURPLE, 2.0),
            hdi_bar("Данска",        94, RED,    1.2),
            hdi_bar("Исланд",        92, ORANGE, 0.4),
            hdi_bar("Шведска",       91, GREEN,  -0.4),
            hdi_bar("Норвешка",      90, BLUE,   -1.2),
            hdi_bar("Просек ЕУ",     74, GREY,   -2.0),
        )

        for b in bars:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.45)
        self.wait(0.5)

        co6 = callout("Високи даноци. Бесплатно образование. Доверба.",
                      width=11.5, bg="#1a2d18", border=GREEN, font_size=24)
        co6.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(co6, shift=UP * 0.3), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(t6), FadeOut(bars), FadeOut(co6), run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 7.  VIKINGS — CLOSING                               ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vikings")

        t7 = section_title("Викинзи — корен на Север", color=ORANGE)
        self.play(Write(t7), run_time=1.0)

        # viking ship silhouette
        ship_hull = Polygon(
            np.array([-3, -0.5, 0]), np.array([3, -0.5, 0]),
            np.array([2.5, -1.3, 0]), np.array([-2.5, -1.3, 0]),
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.9,
        )
        mast = Line(DOWN * 0.5, UP * 1.8, color=GREY, stroke_width=4)
        sail = Polygon(
            np.array([-1.2, 0, 0]), np.array([1.2, 0, 0]),
            np.array([1.0, 1.6, 0]), np.array([-1.0, 1.6, 0]),
            color=RED, fill_color=RED, fill_opacity=0.7,
        )
        stripe1 = Line(LEFT * 1.0 + UP * 0.5, RIGHT * 1.0 + UP * 0.5,
                       color=WHITE2, stroke_width=2)
        stripe2 = Line(LEFT * 1.0 + UP * 1.0, RIGHT * 1.0 + UP * 1.0,
                       color=WHITE2, stroke_width=2)
        ship = VGroup(ship_hull, mast, sail, stripe1, stripe2).shift(DOWN * 0.4)

        self.play(FadeIn(ship_hull), run_time=0.7)
        self.play(Create(mast), run_time=0.5)
        self.play(FadeIn(sail), FadeIn(stripe1), FadeIn(stripe2), run_time=0.8)
        self.play(ship.animate.shift(RIGHT * 2.0), run_time=2.0)
        self.wait(0.5)
        self.play(FadeOut(t7), FadeOut(ship), run_time=0.8)

        # Final punch
        f1 = Text("Север.", font_size=46, color=BLUE, weight=BOLD)
        f2 = Text("Студ. Темнина.", font_size=32, color=GREY)
        f3 = Text("И сепак — светилник на светот.", font_size=30, color=YELLOW)
        f4 = Text("Систем.", font_size=46, color=GREEN, weight=BOLD)

        finale = VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.45)
        self.play(Write(f1), run_time=1.0)
        self.play(FadeIn(f2, shift=UP * 0.3), run_time=1.0)
        self.play(Write(f3), run_time=1.0)
        self.wait(0.3)
        self.play(Write(f4), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(finale), run_time=1.0)
