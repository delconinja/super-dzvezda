"""
Супер Ѕвезда — Математика 5-то одделение
Лекција: Местна вредност на цифрите

Run with:
    manim -pql lesson_mesna_vrednost.py MesnaVrednost       (low quality, fast preview)
    manim -pqh lesson_mesna_vrednost.py MesnaVrednost       (high quality, final)
"""

from manim import *

# ── Brand colours (match the app) ─────────────────────────────────
C_SI  = "#F59E42"   # orange  – стотки илјади
C_DI  = "#FBBF24"   # yellow  – десетки илјади
C_EI  = "#FDE68A"   # pale y  – единици илјади
C_S   = "#86EFAC"   # green   – стотки
C_D   = "#6EE7B7"   # teal    – десетки
C_E   = "#5EEAD4"   # cyan    – единици
C_BG  = "#0D1B2A"   # app dark background
C_TXT = "#EDE8DF"   # app ivory text
C_ACC = "#C4975A"   # app gold accent


class MesnaVrednost(Scene):

    def construct(self):
        self.camera.background_color = C_BG

        self._intro()
        self._show_number()
        self._build_table()
        self._highlight_columns()
        self._expanded_form()
        self._summary()

    # ── 1. Title card ──────────────────────────────────────────────
    def _intro(self):
        title = Text("Местна вредност", font="sans-serif", font_size=52,
                     color=C_ACC, weight=BOLD)
        sub = Text("на цифрите во броевите до 1 000 000",
                   font="sans-serif", font_size=26, color=C_TXT)
        sub.next_to(title, DOWN, buff=0.35)
        grade = Text("Математика · 5-то одделение",
                     font="sans-serif", font_size=18, color=GRAY)
        grade.to_edge(DOWN)

        self.play(Write(title, run_time=1.2))
        self.play(FadeIn(sub), FadeIn(grade))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(sub), FadeOut(grade))

    # ── 2. Introduce the number ────────────────────────────────────
    def _show_number(self):
        prompt = Text("Погледни го овој број:",
                      font="sans-serif", font_size=30, color=C_TXT)
        prompt.to_edge(UP, buff=0.8)

        number = Text("374 826", font="sans-serif", font_size=88,
                      color=WHITE, weight=BOLD)

        question = Text("Каква вредност носи секоја цифра?",
                        font="sans-serif", font_size=28, color=C_TXT)
        question.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(prompt))
        self.play(Write(number, run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(question))
        self.wait(2)
        self.play(FadeOut(prompt), FadeOut(number), FadeOut(question))

    # ── 3. Build the place-value table ────────────────────────────
    def _build_table(self):
        COLS = [
            ("СИ", "3", C_SI),
            ("ДИ", "7", C_DI),
            ("ЕИ", "4", C_EI),
            ("С",  "8", C_S),
            ("Д",  "2", C_D),
            ("Е",  "6", C_E),
        ]

        full_labels = [
            "Стотки илјади",
            "Десетки илјади",
            "Единици илјади",
            "Стотки",
            "Десетки",
            "Единици",
        ]

        cell_w = 1.15
        cell_h = 0.75
        digit_h = 0.95
        start_x = -(len(COLS) - 1) * cell_w / 2
        y_header = 1.4
        y_digit  = 0.4

        header_cells = VGroup()
        digit_cells  = VGroup()

        for i, (label, digit, col) in enumerate(COLS):
            x = start_x + i * cell_w

            # Header rectangle
            rect_h = Rectangle(width=cell_w - 0.06, height=cell_h,
                                fill_color=col, fill_opacity=0.85,
                                stroke_color=col, stroke_width=1.5)
            rect_h.move_to([x, y_header, 0])
            lbl = Text(label, font="sans-serif", font_size=20,
                       color=WHITE, weight=BOLD)
            lbl.move_to(rect_h.get_center())
            header_cells.add(VGroup(rect_h, lbl))

            # Digit rectangle
            rect_d = Rectangle(width=cell_w - 0.06, height=digit_h,
                                fill_color=WHITE, fill_opacity=0.08,
                                stroke_color=col, stroke_width=1.5)
            rect_d.move_to([x, y_digit, 0])
            dig = Text(digit, font="sans-serif", font_size=44,
                       color=WHITE, weight=BOLD)
            dig.move_to(rect_d.get_center())
            digit_cells.add(VGroup(rect_d, dig))

        # Full column labels (bottom)
        full_lbl_group = VGroup()
        for i, (flabel, (_, _, col)) in enumerate(zip(full_labels, COLS)):
            x = start_x + i * cell_w
            ft = Text(flabel, font="sans-serif", font_size=13, color=col)
            ft.rotate(PI / 5)
            ft.move_to([x, -0.65, 0])
            full_lbl_group.add(ft)

        # Animate table appearing column by column
        self.play(FadeIn(header_cells[0], shift=UP * 0.2),
                  FadeIn(digit_cells[0],  shift=UP * 0.2))
        for i in range(1, len(COLS)):
            self.play(FadeIn(header_cells[i], shift=UP * 0.1),
                      FadeIn(digit_cells[i],  shift=UP * 0.1),
                      run_time=0.4)

        self.wait(0.5)
        self.play(FadeIn(full_lbl_group, lag_ratio=0.15))
        self.wait(1.5)

        # Store for next scenes
        self.header_cells = header_cells
        self.digit_cells  = digit_cells
        self.full_lbl_group = full_lbl_group
        self.col_data = COLS
        self.start_x  = start_x
        self.cell_w   = cell_w

    # ── 4. Highlight each column with its value ───────────────────
    def _highlight_columns(self):
        VALUES = [
            ("3 × 100 000 =", "300 000", C_SI),
            ("7 × 10 000 =",  "70 000",  C_DI),
            ("4 × 1 000 =",   "4 000",   C_EI),
            ("8 × 100 =",     "800",     C_S),
            ("2 × 10 =",      "20",      C_D),
            ("6 × 1 =",       "6",       C_E),
        ]

        val_display = None

        for i, (expr, result, col) in enumerate(VALUES):
            x = self.start_x + i * self.cell_w

            # Flash the column
            highlight = Rectangle(
                width=self.cell_w - 0.02,
                height=1.75,
                fill_color=col,
                fill_opacity=0.3,
                stroke_color=col,
                stroke_width=2.5,
            )
            highlight.move_to([x, 0.9, 0])

            # Value text
            new_val = VGroup(
                Text(expr,   font="sans-serif", font_size=26, color=col),
                Text(result, font="sans-serif", font_size=40, color=WHITE, weight=BOLD),
            ).arrange(RIGHT, buff=0.25)
            new_val.move_to([0, -1.6, 0])

            if val_display is None:
                self.play(FadeIn(highlight, run_time=0.3),
                          FadeIn(new_val,  run_time=0.4))
            else:
                self.play(FadeIn(highlight, run_time=0.3),
                          Transform(val_display, new_val, run_time=0.4))

            val_display = new_val
            self.wait(1.0)
            self.play(FadeOut(highlight, run_time=0.25))

        self.wait(0.5)
        self.play(FadeOut(val_display))

    # ── 5. Expanded form ──────────────────────────────────────────
    def _expanded_form(self):
        self.play(
            FadeOut(self.header_cells),
            FadeOut(self.digit_cells),
            FadeOut(self.full_lbl_group),
        )

        title = Text("Развиена форма:", font="sans-serif",
                     font_size=32, color=C_ACC, weight=BOLD)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title))

        # (text, colour, bold?)
        parts = [
            ("300 000", C_SI,  True),
            ("+",       WHITE, False),
            ("70 000",  C_DI,  True),
            ("+",       WHITE, False),
            ("4 000",   C_EI,  True),
            ("+",       WHITE, False),
            ("800",     C_S,   True),
            ("+",       WHITE, False),
            ("20",      C_D,   True),
            ("+",       WHITE, False),
            ("6",       C_E,   True),
        ]

        row1 = VGroup(*[
            Text(t, font="sans-serif", font_size=34,
                 color=c, weight=BOLD if bold else "NORMAL")
            for t, c, bold in parts
        ]).arrange(RIGHT, buff=0.18)
        row1.move_to([0, 0.5, 0])

        equals = Text("= 374 826", font="sans-serif", font_size=44,
                      color=WHITE, weight=BOLD)
        equals.next_to(row1, DOWN, buff=0.5)

        for mob in row1:
            self.play(FadeIn(mob, shift=UP * 0.15), run_time=0.25)
        self.wait(0.5)
        self.play(Write(equals, run_time=1.0))
        self.wait(2)

        self.play(FadeOut(row1), FadeOut(equals), FadeOut(title))

    # ── 6. Summary / key rule ─────────────────────────────────────
    def _summary(self):
        box = RoundedRectangle(width=9, height=3.2, corner_radius=0.3,
                               fill_color=C_ACC, fill_opacity=0.12,
                               stroke_color=C_ACC, stroke_width=2)

        rule = Text(
            "Местната вредност на цифрата зависи\nод нејзиното место во бројот!",
            font="sans-serif", font_size=30, color=WHITE,
            line_spacing=1.4, weight=BOLD,
        )
        rule.move_to(box.get_center())

        emoji = Text("💡", font_size=40)
        emoji.next_to(box, LEFT, buff=0.3)

        self.play(DrawBorderThenFill(box))
        self.play(Write(rule))
        self.play(FadeIn(emoji))
        self.wait(3)
        self.play(FadeOut(box), FadeOut(rule), FadeOut(emoji))

        bye = Text("Супер Ѕвезда ⭐", font="sans-serif",
                   font_size=36, color=C_ACC, weight=BOLD)
        self.play(Write(bye))
        self.wait(1.5)
        self.play(FadeOut(bye))
