"""
geo8-1-3  —  Клима на Европа
Географија 8, Единица 1: Природно-географски карактеристики на Европа

Teaching narrative — Andonovski-style: three-beat punches,
sun as visitor, wind as messenger, Gulf Stream as natural heater.
Render:  manim -ql geo8-1-3.py Geo813Scene
Output:  media/videos/geo8-1-3/480p15/Geo813Scene.mp4
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


def climate_card(name, summer, winter, color, pos):
    box = RoundedRectangle(
        width=3.0, height=2.4, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    ).move_to(pos)
    n = Text(name, font_size=20, color=color, weight=BOLD)
    n.move_to(box.get_center() + UP * 0.8)
    s = Text(f"Лето: {summer}", font_size=15, color=ORANGE)
    s.move_to(box.get_center() + UP * 0.1)
    w = Text(f"Зима: {winter}", font_size=15, color=BLUE)
    w.move_to(box.get_center() + DOWN * 0.3)
    return VGroup(box, n, s, w)


class Geo813Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK — Лондон и Њујорк                           ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Лондон е посеверно од Њујорк.",
                     font_size=40, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.7)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Но потопло.", font_size=42, color=ORANGE, weight=BOLD),
            Text("Зошто?", font_size=38, color=WHITE2),
            Text("Голфската струја.", font_size=36, color=BLUE, weight=BOLD),
            Text("Топлата река во океанот.", font_size=30, color=GREEN, slant=ITALIC),
            Text("Природна греалка.", font_size=34, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(hook1, DOWN, buff=0.5)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.65)
            self.wait(0.2)

        self.wait(1.4)
        self.play(FadeOut(hook1), FadeOut(beats), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  ФАКТОРИ ЗА КЛИМА                                  ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("faktori")

        t2 = section_title("Што ja прави климата?", color=BLUE)
        self.play(Write(t2), run_time=0.9)

        factors = [
            ("Географска ширина", "колку сонце", YELLOW,  LEFT * 4.5 + UP * 0.4),
            ("Близина на море",    "влага и топлина", BLUE,    LEFT * 1.5 + UP * 0.4),
            ("Релјеф",             "висина = студ",   GREY,    RIGHT * 1.5 + UP * 0.4),
            ("Морски струи",       "Голфска струја",  ORANGE,  RIGHT * 4.5 + UP * 0.4),
        ]

        cards = []
        for name, sub, col, pos in factors:
            box = RoundedRectangle(
                width=2.7, height=2.0, corner_radius=0.2,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            ).move_to(pos)
            n = Text(name, font_size=18, color=col, weight=BOLD)
            n.move_to(box.get_center() + UP * 0.5)
            s = Text(sub, font_size=15, color=WHITE2)
            s.move_to(box.get_center() + DOWN * 0.2)
            cards.append(VGroup(box, n, s))

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.55)
            self.wait(0.1)

        note = Text("Четири фактори. Илјади места. Илјади микро-клими.",
                    font_size=22, color=YELLOW, slant=ITALIC).to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=1.0)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(*cards, note, t2)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 3.  ЧЕТИРИ КЛИМАТСКИ ПОЈАСИ                          ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("pojasi")

        t3 = section_title("Четири клими — четири карактери", color=GREEN)
        self.play(Write(t3), run_time=0.9)

        c1 = climate_card("Атлантска",   "благо",   "благо, влажно", BLUE,
                          LEFT * 4.5 + DOWN * 0.3)
        c2 = climate_card("Континентална", "топло", "ладно, суво",   ORANGE,
                          LEFT * 1.5 + DOWN * 0.3)
        c3 = climate_card("Средоземна",  "врело, суво", "благо, влажно", YELLOW,
                          RIGHT * 1.5 + DOWN * 0.3)
        c4 = climate_card("Субарктичка", "кратко",  "долго, мраз",   GREY,
                          RIGHT * 4.5 + DOWN * 0.3)

        for c in [c1, c2, c3, c4]:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
            self.wait(0.2)

        punch = Text("Запад мек. Центар силен. Југ страстен. Север строг.",
                     font_size=22, color=WHITE2, slant=ITALIC).to_edge(DOWN, buff=0.4)
        self.play(Write(punch), run_time=1.2)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(c1, c2, c3, c4, punch, t3)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 4.  АТЛАНТСКА vs КОНТИНЕНТАЛНА — графикон             ~55 s
        # ══════════════════════════════════════════════════════════
        self.next_section("graf")

        t4 = section_title("Температури низ годината", color=ORANGE)
        self.play(Write(t4), run_time=0.9)

        axes = Axes(
            x_range=[0, 12, 1],
            y_range=[-15, 30, 5],
            x_length=9.0,
            y_length=4.0,
            axis_config={"color": GREY, "stroke_width": 1.5},
            tips=False,
        ).shift(DOWN * 0.4)

        x_lab = Text("месеци", font_size=18, color=WHITE2)
        x_lab.next_to(axes.x_axis, DOWN, buff=0.2)
        y_lab = Text("°C", font_size=18, color=WHITE2)
        y_lab.next_to(axes.y_axis, LEFT, buff=0.2)

        self.play(Create(axes), FadeIn(x_lab), FadeIn(y_lab), run_time=1.2)

        # Atlantic (London): mild swing ~5 to 18
        atl_data = [5, 5, 7, 10, 13, 16, 18, 18, 15, 12, 8, 6]
        atl_pts = [axes.c2p(i + 0.5, v) for i, v in enumerate(atl_data)]
        atl_curve = VMobject(color=BLUE, stroke_width=4)
        atl_curve.set_points_as_corners(atl_pts)
        atl_lab = Text("Атлантска (Лондон)", font_size=18, color=BLUE)
        atl_lab.move_to(axes.c2p(2.5, 22))

        # Continental (Moscow): big swing -10 to 22
        cont_data = [-9, -8, -3, 5, 12, 17, 19, 17, 11, 4, -2, -6]
        cont_pts = [axes.c2p(i + 0.5, v) for i, v in enumerate(cont_data)]
        cont_curve = VMobject(color=ORANGE, stroke_width=4)
        cont_curve.set_points_as_corners(cont_pts)
        cont_lab = Text("Континентална (Москва)", font_size=18, color=ORANGE)
        cont_lab.move_to(axes.c2p(9.5, 25))

        # Mediterranean (Athens): warm, no winter chill
        med_data = [10, 10, 12, 16, 21, 26, 29, 28, 24, 19, 14, 11]
        med_pts = [axes.c2p(i + 0.5, v) for i, v in enumerate(med_data)]
        med_curve = VMobject(color=YELLOW, stroke_width=4)
        med_curve.set_points_as_corners(med_pts)
        med_lab = Text("Средоземна (Атина)", font_size=18, color=YELLOW)
        med_lab.move_to(axes.c2p(5.5, -10))

        self.play(Create(atl_curve), FadeIn(atl_lab), run_time=1.4)
        self.wait(0.4)
        self.play(Create(cont_curve), FadeIn(cont_lab), run_time=1.4)
        self.wait(0.4)
        self.play(Create(med_curve), FadeIn(med_lab), run_time=1.4)

        self.wait(1.2)

        verdict = Text("Море смирува. Копно бесни. Сонцето — спор судија.",
                       font_size=20, color=WHITE2, slant=ITALIC).to_edge(DOWN, buff=0.3)
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(axes, x_lab, y_lab, atl_curve, atl_lab,
                           cont_curve, cont_lab, med_curve, med_lab,
                           verdict, t4)),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════
        # 5.  ГОЛФСКАТА СТРУЈА                                  ~60 s
        # ══════════════════════════════════════════════════════════
        self.next_section("golf")

        t5 = section_title("Голфската струја — топлата река", color=RED)
        self.play(Write(t5), run_time=0.9)

        # Two simplified continents
        americas = RoundedRectangle(
            width=2.4, height=4.0, corner_radius=0.3,
            fill_color="#3a2a0a", fill_opacity=0.7,
            stroke_color=ORANGE, stroke_width=2,
        ).shift(LEFT * 4.5 + DOWN * 0.2)
        am_lab = Text("Северна\nАмерика", font_size=18, color=ORANGE, weight=BOLD)
        am_lab.move_to(americas)

        europe = RoundedRectangle(
            width=2.6, height=3.8, corner_radius=0.3,
            fill_color="#0a2a4a", fill_opacity=0.7,
            stroke_color=BLUE, stroke_width=2,
        ).shift(RIGHT * 4.5 + UP * 0.0)
        eu_lab = Text("Европа", font_size=20, color=BLUE, weight=BOLD)
        eu_lab.move_to(europe)

        self.play(FadeIn(americas), Write(am_lab),
                  FadeIn(europe), Write(eu_lab), run_time=1.0)

        # Gulf Stream — curve from Gulf of Mexico (bottom left) up across Atlantic to Europe
        # Use arc / parametric
        gulf = ParametricFunction(
            lambda t: np.array([
                -3.3 + 6.6 * t + 0.4 * np.sin(t * PI * 2),
                -2.0 + 2.5 * t + 0.5 * np.sin(t * PI),
                0,
            ]),
            t_range=[0, 1],
            color=RED, stroke_width=6,
        )
        # Arrowhead at end
        end_pt = gulf.get_end()
        tail_pt = gulf.point_from_proportion(0.92)
        arrow_head = Arrow(tail_pt, end_pt, color=RED, buff=0,
                           stroke_width=5, max_tip_length_to_length_ratio=0.4)

        self.play(Create(gulf), run_time=2.0)
        self.play(GrowArrow(arrow_head), run_time=0.5)

        gulf_lab = Text("Голфска струја", font_size=22, color=RED, weight=BOLD)
        gulf_lab.move_to(UP * 0.2)
        self.play(Write(gulf_lab), run_time=0.7)

        # Effect facts
        effect = VGroup(
            Text("Топла вода од Мексиканскиот Залив",
                 font_size=20, color=ORANGE),
            Text("Се движи кон Европа со ≈ 4 км/ч",
                 font_size=20, color=YELLOW),
            Text("Затоплува воздух 5–10 °C над просек",
                 font_size=20, color=RED),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.4)

        for ln in effect:
            self.play(FadeIn(ln, shift=UP * 0.15), run_time=0.55)
            self.wait(0.15)

        self.wait(1.4)
        self.play(
            FadeOut(VGroup(americas, am_lab, europe, eu_lab,
                           gulf, arrow_head, gulf_lab, effect, t5)),
            run_time=0.7,
        )

        # ══════════════════════════════════════════════════════════
        # 6.  ВЕТРОВИ И ВЛАГА                                   ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("vetrovi")

        t6 = section_title("Западни ветрови — патници на влага", color=GREEN)
        self.play(Write(t6), run_time=0.9)

        # Simple band of arrows from west to east
        for i in range(5):
            y = 1.5 - i * 0.7
            arr = Arrow(LEFT * 5.5 + UP * y, RIGHT * 5.5 + UP * y,
                        color=BLUE, buff=0, stroke_width=3,
                        max_tip_length_to_length_ratio=0.05)
            self.play(GrowArrow(arr), run_time=0.4)

        info = VGroup(
            callout("Доминантни — западни ветрови",
                    width=8.5, bg=DARK_CARD, border=BLUE, font_size=22),
            callout("Носат влага од Атлантик кон копно",
                    width=8.5, bg=DARK_CARD, border=GREEN, font_size=22),
            callout("Чим внатре — влагата паѓа како дожд",
                    width=8.5, bg=DARK_CARD, border=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.4)

        for c in info:
            self.play(FadeIn(c, shift=UP * 0.15), run_time=0.55)
            self.wait(0.15)

        self.wait(1.2)
        self.play(FadeOut(*[m for m in self.mobjects]), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 7.  ЗАКЛУЧОК                                          ~28 s
        # ══════════════════════════════════════════════════════════
        self.next_section("zakluchok")

        final_title = Text("Клима = средба.",
                           font_size=46, color=YELLOW, weight=BOLD)
        final_title.to_edge(UP, buff=0.8)
        self.play(Write(final_title), run_time=1.0)

        summary = VGroup(
            Text("Сонце дава. Море смирува. Релјеф крие.",
                 font_size=26, color=BLUE),
            Text("Запад благ. Центар силен. Југ топол. Север студен.",
                 font_size=22, color=ORANGE),
            Text("Голфската струја — топла рака преку океан.",
                 font_size=24, color=RED, slant=ITALIC),
            Text("Европа дише низ четири времиња.",
                 font_size=28, color=GREEN, weight=BOLD),
            Text("Без застој.",
                 font_size=36, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.35).next_to(final_title, DOWN, buff=0.6)

        for line in summary:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)

        self.wait(2.0)
        self.play(FadeOut(VGroup(final_title, summary)), run_time=0.8)
        self.wait(0.4)
