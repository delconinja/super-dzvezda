"""
m8-5-1  —  Планирање и собирање податоци
Математика 8, Единица 5: Ракување со податоци

Andonovski-style: податокот како семе, истражувањето како растење.
Render:  manim -ql m8-5-1.py M851Scene
Output:  media/videos/m8-5-1/480p15/M851Scene.mp4
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


def step_card(idx, title, color=BLUE, w=2.2, h=1.2):
    box = RoundedRectangle(
        width=w, height=h, corner_radius=0.2,
        fill_color=DARK_CARD, fill_opacity=1,
        stroke_color=color, stroke_width=2,
    )
    n = Text(str(idx), font_size=28, color=color, weight=BOLD)
    t = Text(title, font_size=18, color=WHITE2)
    n.move_to(box.get_top() + DOWN * 0.3)
    t.move_to(box.get_center() + DOWN * 0.15)
    return VGroup(box, n, t)


class M851Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~12 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Прашањето е семе.", font_size=42, color=YELLOW, weight=BOLD)
        hook2 = Text("Податокот е растение.", font_size=42, color=GREEN, weight=BOLD)
        hook3 = Text("Заклучокот е плод.", font_size=42, color=ORANGE, weight=BOLD)
        hook4 = Text("Без семе — нема плод.", font_size=36, color=WHITE2)

        hooks = VGroup(hook1, hook2, hook3, hook4).arrange(DOWN, buff=0.4)
        hooks.move_to(ORIGIN)

        for h in hooks:
            self.play(Write(h), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(hooks), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 2.  6 ЧЕКОРИ                                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("steps")

        title2 = section_title("Шест чекори на истражувањето")
        self.play(Write(title2), run_time=1.0)

        steps = [
            ("Прашање", BLUE),
            ("План", GREEN),
            ("Собирање", YELLOW),
            ("Обработка", ORANGE),
            ("Анализа", PURPLE),
            ("Заклучок", RED),
        ]

        cards = VGroup()
        for i, (name, col) in enumerate(steps, start=1):
            cards.add(step_card(i, name, color=col, w=1.8, h=1.0))

        # Two rows
        top_row = VGroup(*cards[:3]).arrange(RIGHT, buff=0.4)
        bot_row = VGroup(*cards[3:]).arrange(RIGHT, buff=0.4)
        top_row.move_to(UP * 1.0)
        bot_row.move_to(DOWN * 0.8)

        for c in top_row:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.35)

        # Arrows between top row
        for i in range(2):
            a = Arrow(
                cards[i].get_right(), cards[i+1].get_left(),
                color=YELLOW, stroke_width=4, buff=0.05,
            )
            self.play(GrowArrow(a), run_time=0.25)

        # Connector down
        conn = Arrow(
            cards[2].get_bottom(), cards[3].get_top(),
            color=YELLOW, stroke_width=4, buff=0.05,
        )
        self.play(GrowArrow(conn), run_time=0.3)

        for c in bot_row:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.35)

        for i in range(3, 5):
            a = Arrow(
                cards[i].get_right(), cards[i+1].get_left(),
                color=YELLOW, stroke_width=4, buff=0.05,
            )
            self.play(GrowArrow(a), run_time=0.25)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 3.  ДИСКРЕТНИ vs КОНТИНУИРАНИ                       ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("discrete_continuous")

        title3 = section_title("Дискретни и континуирани")
        self.play(Write(title3), run_time=1.0)

        # Two columns
        left_box = RoundedRectangle(
            width=5.5, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=BLUE, stroke_width=2,
        ).move_to(LEFT * 3.2 + DOWN * 0.2)

        right_box = RoundedRectangle(
            width=5.5, height=4.5, corner_radius=0.3,
            fill_color=DARK_CARD, fill_opacity=1,
            stroke_color=GREEN, stroke_width=2,
        ).move_to(RIGHT * 3.2 + DOWN * 0.2)

        self.play(Create(left_box), Create(right_box), run_time=1.0)

        l_title = Text("Дискретни", font_size=30, color=BLUE, weight=BOLD)
        l_title.move_to(left_box.get_top() + DOWN * 0.4)
        l_sub = Text("(се бројат, точни)", font_size=20, color=WHITE2)
        l_sub.next_to(l_title, DOWN, buff=0.15)

        l_examples = VGroup(
            Text("• број на деца", font_size=22, color=WHITE2),
            Text("• книги во ранец", font_size=22, color=WHITE2),
            Text("• оценки на тест", font_size=22, color=WHITE2),
            Text("• автомобили на пат", font_size=22, color=WHITE2),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        l_examples.next_to(l_sub, DOWN, buff=0.3)
        l_examples.shift(LEFT * 0.3)

        r_title = Text("Континуирани", font_size=30, color=GREEN, weight=BOLD)
        r_title.move_to(right_box.get_top() + DOWN * 0.4)
        r_sub = Text("(се мерат, секаква вредност)", font_size=20, color=WHITE2)
        r_sub.next_to(r_title, DOWN, buff=0.15)

        r_examples = VGroup(
            Text("• висина", font_size=22, color=WHITE2),
            Text("• тежина", font_size=22, color=WHITE2),
            Text("• температура", font_size=22, color=WHITE2),
            Text("• време во трка", font_size=22, color=WHITE2),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        r_examples.next_to(r_sub, DOWN, buff=0.3)
        r_examples.shift(LEFT * 0.5)

        self.play(Write(l_title), Write(r_title), run_time=0.8)
        self.play(Write(l_sub), Write(r_sub), run_time=0.6)

        for le, re in zip(l_examples, r_examples):
            self.play(FadeIn(le, shift=RIGHT * 0.2), FadeIn(re, shift=RIGHT * 0.2), run_time=0.4)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 4.  ПРИМАРНИ vs СЕКУНДАРНИ + АНКЕТА                ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sources")

        title4 = section_title("Извори на податоци")
        self.play(Write(title4), run_time=1.0)

        prim = callout("Примарни — ти ги собираш (анкета, опит, набљудување)",
                       width=11, bg="#0d2b44", border=BLUE, font_size=26)
        prim.move_to(UP * 1.6)
        sec = callout("Секундарни — од други (извештаи, статистики)",
                      width=11, bg="#0d2b44", border=GREEN, font_size=26)
        sec.move_to(UP * 0.1)

        self.play(FadeIn(prim, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(sec, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        # Survey question types
        q_title = Text("Прашања во анкета", font_size=28, color=YELLOW, weight=BOLD)
        q_title.move_to(DOWN * 1.0)
        self.play(Write(q_title), run_time=0.8)

        closed = Text("Затворени: Да/Не, А/Б/В/Г", font_size=24, color=WHITE2)
        opened = Text("Отворени: слободен одговор", font_size=24, color=WHITE2)
        closed.next_to(q_title, DOWN, buff=0.3)
        opened.next_to(closed, DOWN, buff=0.2)

        self.play(Write(closed), run_time=0.8)
        self.play(Write(opened), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 5.  СОВЕТИ И ГОЛЕМИНА НА ПРИМЕРОК                   ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("sample")

        title5 = section_title("Совети за анкета")
        self.play(Write(title5), run_time=1.0)

        tips = VGroup(
            Text("• Кратко.", font_size=30, color=GREEN, weight=BOLD),
            Text("• Јасно.", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Без наведување.", font_size=30, color=ORANGE, weight=BOLD),
        )
        tips.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        tips.move_to(UP * 1.5)

        for t in tips:
            self.play(Write(t), run_time=0.7)
        self.wait(0.8)

        # Bad vs good question
        bad = Text("Лошо: \"Зар не мислиш дека пушењето е лошо?\"",
                   font_size=24, color=RED)
        good = Text("Добро: \"Колку често пушиш?\"",
                    font_size=24, color=GREEN)
        bad.move_to(DOWN * 0.3)
        good.next_to(bad, DOWN, buff=0.3)

        self.play(Write(bad), run_time=1.0)
        self.play(Write(good), run_time=1.0)
        self.wait(1.2)

        sample = Text("Премал примерок = непретставителен. 100+ за статистика.",
                      font_size=24, color=YELLOW)
        sample.move_to(DOWN * 2.3)
        self.play(Write(sample), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 6.  ТАБЕЛА НА ФРЕКВЕНЦИИ                            ~45 s
        # ══════════════════════════════════════════════════════════
        self.next_section("frequency")

        title6 = section_title("Табела на фреквенции")
        self.play(Write(title6), run_time=1.0)

        # Frequency table for test scores 1-5
        headers = VGroup(
            Text("Оценка", font_size=26, color=YELLOW, weight=BOLD),
            Text("Тали", font_size=26, color=YELLOW, weight=BOLD),
            Text("Фреквенција", font_size=26, color=YELLOW, weight=BOLD),
        )
        headers[0].move_to(LEFT * 3.5 + UP * 1.8)
        headers[1].move_to(UP * 1.8)
        headers[2].move_to(RIGHT * 3.5 + UP * 1.8)
        self.play(Write(headers), run_time=1.0)

        rows = [
            ("1", "||",       "2"),
            ("2", "||||",     "4"),
            ("3", "|||| ||",  "7"),
            ("4", "|||| |",   "6"),
            ("5", "|||",      "3"),
        ]

        ystart = 1.1
        row_mobs = VGroup()
        for i, (g, tally, f) in enumerate(rows):
            y = ystart - i * 0.55
            g_t = Text(g, font_size=26, color=WHITE2).move_to(LEFT * 3.5 + UP * y)
            t_t = Text(tally, font_size=26, color=BLUE).move_to(UP * y)
            f_t = Text(f, font_size=26, color=GREEN, weight=BOLD).move_to(RIGHT * 3.5 + UP * y)
            row_mobs.add(g_t, t_t, f_t)

        # Animate row by row
        for i in range(0, len(row_mobs), 3):
            self.play(Write(row_mobs[i]), Write(row_mobs[i+1]), Write(row_mobs[i+2]),
                      run_time=0.6)

        self.wait(1.0)

        total = Text("Вкупно: 22 ученика", font_size=26, color=ORANGE, weight=BOLD)
        total.move_to(DOWN * 2.4)
        self.play(Write(total), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 7.  КЛАСНИ ИНТЕРВАЛИ + ЕТИКА                        ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("intervals_ethics")

        title7 = section_title("Класни интервали")
        self.play(Write(title7), run_time=1.0)

        sub = Text("За континуирани податоци — еднакви интервали, без преклопување.",
                   font_size=24, color=WHITE2)
        sub.move_to(UP * 2.0)
        self.play(Write(sub), run_time=1.2)

        intervals = ["140–150", "150–160", "160–170", "170–180", "180–190"]
        heights   = [0.6, 1.4, 2.0, 1.1, 0.5]

        bars = VGroup()
        labels = VGroup()
        x = -4.0
        for i, (lbl, h) in enumerate(zip(intervals, heights)):
            bar = Rectangle(
                width=1.4, height=h,
                fill_color=BLUE, fill_opacity=0.7,
                stroke_color=BLUE, stroke_width=2,
            )
            bar.move_to(np.array([x, -1.5 + h / 2, 0]))
            bars.add(bar)
            t = Text(lbl, font_size=18, color=WHITE2)
            t.move_to(np.array([x, -1.8, 0]))
            labels.add(t)
            x += 1.6

        for b, l in zip(bars, labels):
            self.play(GrowFromEdge(b, DOWN), FadeIn(l), run_time=0.4)

        unit = Text("cm (висина)", font_size=20, color=GREY)
        unit.move_to(DOWN * 2.5)
        self.play(Write(unit), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(sub), FadeOut(bars), FadeOut(labels), FadeOut(unit), run_time=0.5)

        ethics = section_title("Етика", color=ORANGE)
        # Replace title
        self.play(Transform(title7, ethics), run_time=0.6)

        eth = VGroup(
            Text("• Анонимност", font_size=30, color=BLUE),
            Text("• Согласност", font_size=30, color=GREEN),
            Text("• Чесност", font_size=30, color=YELLOW),
        )
        eth.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        eth.move_to(ORIGIN)

        for e in eth:
            self.play(Write(e), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(*self.mobjects), run_time=0.6)

        # ══════════════════════════════════════════════════════════
        # 8.  CLOSING                                         ~10 s
        # ══════════════════════════════════════════════════════════
        self.next_section("closing")

        close = Text("Добри прашања раѓаат добри одговори.",
                     font_size=38, color=YELLOW, weight=BOLD)
        close.move_to(ORIGIN)
        self.play(Write(close), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(close), run_time=0.8)
