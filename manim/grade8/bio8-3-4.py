"""
bio8-3-4  —  Белковини — важност и извори
Биологија 8, Единица 3: Исхрана и здравје

Teaching narrative — Andonovski-style: three-beat punches,
amino acids as letters, proteins as words, sources as story.
Render:  manim -ql bio8-3-4.py Bio834Scene
Output:  media/videos/bio8-3-4/480p15/Bio834Scene.mp4
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


def amino_block(letter, color):
    """Returns a small square 'amino acid' tile."""
    sq = RoundedRectangle(
        width=0.6, height=0.6, corner_radius=0.1,
        fill_color=color, fill_opacity=0.85,
        stroke_color=WHITE2, stroke_width=1.5,
    )
    t = Text(letter, font_size=22, color=DARK_CARD, weight=BOLD)
    t.move_to(sq)
    return VGroup(sq, t)


class Bio834Scene(Scene):
    def construct(self):

        # ══════════════════════════════════════════════════════════
        # 1.  HOOK                                            ~22 s
        # ══════════════════════════════════════════════════════════
        self.next_section("hook")

        hook1 = Text("Дваесет аминокиселини.",
                     font_size=44, color=YELLOW, weight=BOLD)
        hook1.to_edge(UP, buff=0.6)
        self.play(Write(hook1), run_time=1.2)
        self.wait(0.3)

        beats = VGroup(
            Text("Деветте мора да доаѓаат од храна.",
                 font_size=34, color=ORANGE),
            Text("Телото не може да ги направи.",
                 font_size=32, color=RED),
            Text("Без нив — нема раст.",
                 font_size=36, color=PURPLE, weight=BOLD),
            Text("Без нив — нема живот.",
                 font_size=40, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45).next_to(hook1, DOWN, buff=0.7)

        for line in beats:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.7)
            self.wait(0.25)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, beats)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 2.  DEFINITION — what is a protein                  ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("definition")

        title = section_title("Што е белковина")
        self.play(Write(title), run_time=0.8)

        # 20 amino acid blocks (letters A-T-ish, mixed colors)
        letters = list("АВГДЕЖЗИКЛМНОПРСТУФХ")
        palette = [BLUE, YELLOW, GREEN, RED, ORANGE, PURPLE, GREY]
        aminos = VGroup()
        for i, ch in enumerate(letters):
            col = palette[i % len(palette)]
            aminos.add(amino_block(ch, col))
        aminos.arrange_in_grid(rows=2, cols=10, buff=0.18)
        aminos.shift(UP * 0.8)

        label_aa = Text("20 аминокиселини", font_size=26, color=WHITE2)
        label_aa.next_to(aminos, UP, buff=0.4)

        self.play(FadeIn(label_aa), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.1) for a in aminos],
                              lag_ratio=0.05), run_time=1.8)
        self.wait(0.5)

        # 9 essential — highlight
        essential_indices = [0, 2, 4, 6, 8, 10, 12, 14, 16]
        highlights = VGroup()
        for i in essential_indices:
            ring = Circle(radius=0.45, color=RED, stroke_width=3)
            ring.move_to(aminos[i].get_center())
            highlights.add(ring)

        ess_label = Text("9 неопходни — само од храна",
                         font_size=24, color=RED, weight=BOLD)
        ess_label.next_to(aminos, DOWN, buff=0.5)

        self.play(LaggedStart(*[Create(r) for r in highlights],
                              lag_ratio=0.08), run_time=1.2)
        self.play(FadeIn(ess_label), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(VGroup(title, label_aa, aminos, highlights, ess_label)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 3.  MECHANISM — amino acids form chain              ~35 s
        # ══════════════════════════════════════════════════════════
        self.next_section("mechanism")

        title = section_title("Од градивни блокчиња до синџир")
        self.play(Write(title), run_time=0.8)

        # 6 separated amino acids
        chain_letters = list("МЕТАЛИ")
        chain_colors = [BLUE, YELLOW, GREEN, RED, ORANGE, PURPLE]
        free_aas = VGroup(*[
            amino_block(ch, col)
            for ch, col in zip(chain_letters, chain_colors)
        ])

        # Position them spread out
        for i, a in enumerate(free_aas):
            a.move_to(LEFT * 5 + RIGHT * i * 1.8 + UP * 1.2)

        self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.2) for a in free_aas],
                              lag_ratio=0.15), run_time=1.5)
        self.wait(0.4)

        # Animate them connecting into a chain
        chain_positions = [LEFT * 4.5 + RIGHT * i * 1.05 + DOWN * 0.8
                           for i in range(6)]
        self.play(*[a.animate.move_to(p)
                    for a, p in zip(free_aas, chain_positions)],
                  run_time=1.4)

        # Draw bonds between them
        bonds = VGroup()
        for i in range(5):
            b = Line(
                free_aas[i].get_right(),
                free_aas[i+1].get_left(),
                color=WHITE2, stroke_width=3,
            )
            bonds.add(b)

        self.play(LaggedStart(*[Create(b) for b in bonds],
                              lag_ratio=0.15), run_time=1.0)

        # Bracket + label
        chain_group = VGroup(free_aas, bonds)
        brace = Brace(chain_group, DOWN, color=GREEN)
        brace_lbl = brace.get_text("белковина — синџир од аминокиселини")
        brace_lbl.set_color(GREEN)

        self.play(GrowFromCenter(brace), FadeIn(brace_lbl), run_time=0.9)
        self.wait(0.5)

        # Folding hint
        fold_note = Text("се свиткува во 3D облик",
                         font_size=22, color=YELLOW)
        fold_note.move_to(DOWN * 2.8)
        self.play(FadeIn(fold_note), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, free_aas, bonds, brace, brace_lbl, fold_note)),
                  run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 4.  EXAMPLE — food sources grid                     ~40 s
        # ══════════════════════════════════════════════════════════
        self.next_section("example")

        title = section_title("Извори на белковини")
        self.play(Write(title), run_time=0.8)

        # Two columns: animal vs plant
        animal_header = Text("Животински извори", font_size=26,
                             color=RED, weight=BOLD)
        animal_header.move_to(LEFT * 3.4 + UP * 2.3)
        plant_header = Text("Растителни извори", font_size=26,
                            color=GREEN, weight=BOLD)
        plant_header.move_to(RIGHT * 3.4 + UP * 2.3)

        # Divider
        divider = Line(UP * 2.0, DOWN * 2.6,
                       color=GREY, stroke_width=1.5)

        self.play(FadeIn(animal_header), FadeIn(plant_header),
                  Create(divider), run_time=0.8)

        animals = [
            ("Месо",   "26 g/100 g"),
            ("Јајца",  "13 g/100 g"),
            ("Млеко",  "3.5 g/100 g"),
            ("Сирење", "25 g/100 g"),
            ("Риба",   "20 g/100 g"),
        ]
        plants = [
            ("Леќа",   "9 g/100 g"),
            ("Грав",   "21 g/100 g"),
            ("Ораси",  "15 g/100 g"),
            ("Соја",   "36 g/100 g"),
            ("Бадеми", "21 g/100 g"),
        ]

        a_cards = VGroup()
        for name, amt in animals:
            box = RoundedRectangle(
                width=5.0, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=RED, stroke_width=1.8,
            )
            n = Text(name, font_size=22, color=WHITE2, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.2)
            a = Text(amt, font_size=20, color=YELLOW)
            a.move_to(box.get_left() + RIGHT * 3.5)
            a_cards.add(VGroup(box, n, a))
        a_cards.arrange(DOWN, buff=0.15)
        a_cards.move_to(LEFT * 3.4 + DOWN * 0.4)

        p_cards = VGroup()
        for name, amt in plants:
            box = RoundedRectangle(
                width=5.0, height=0.55, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=GREEN, stroke_width=1.8,
            )
            n = Text(name, font_size=22, color=WHITE2, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.2)
            a = Text(amt, font_size=20, color=YELLOW)
            a.move_to(box.get_left() + RIGHT * 3.5)
            p_cards.add(VGroup(box, n, a))
        p_cards.arrange(DOWN, buff=0.15)
        p_cards.move_to(RIGHT * 3.4 + DOWN * 0.4)

        for i in range(5):
            self.play(FadeIn(a_cards[i], shift=RIGHT * 0.2),
                      FadeIn(p_cards[i], shift=LEFT * 0.2),
                      run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, animal_header, plant_header, divider,
            a_cards, p_cards)),
            run_time=0.8)

        # ══════════════════════════════════════════════════════════
        # 5.  REAL-WORLD — daily need + muscle role            ~30 s
        # ══════════════════════════════════════════════════════════
        self.next_section("realworld")

        title = section_title("Колку и за што")
        self.play(Write(title), run_time=0.8)

        # Daily need callout
        need = callout("Околу 50 g белковини дневно",
                       width=8.5, border=YELLOW, font_size=32)
        need.move_to(UP * 1.7)
        self.play(FadeIn(need, shift=UP * 0.2), run_time=0.8)

        # Roles
        roles = [
            ("Раст",        "Деца и тинејџери растат.",     GREEN),
            ("Поправка",    "Раните се закрепнуваат.",      BLUE),
            ("Мускули",     "Влакна од белковини.",         RED),
            ("Ензими",      "Помагаат во храноварењето.",   PURPLE),
            ("Антитела",    "Бранат од болести.",           ORANGE),
        ]

        cards = VGroup()
        for name, role, col in roles:
            box = RoundedRectangle(
                width=11.5, height=0.6, corner_radius=0.12,
                fill_color=DARK_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2,
            )
            n = Text(name, font_size=24, color=col, weight=BOLD)
            n.move_to(box.get_left() + RIGHT * 1.5)
            r = Text(role, font_size=22, color=WHITE2)
            r.move_to(box.get_left() + RIGHT * 6.5)
            cards.add(VGroup(box, n, r))
        cards.arrange(DOWN, buff=0.15)
        cards.next_to(need, DOWN, buff=0.5)

        for c in cards:
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.45)
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, need, cards)), run_time=0.7)

        # ══════════════════════════════════════════════════════════
        # 6.  SUMMARY                                          ~15 s
        # ══════════════════════════════════════════════════════════
        self.next_section("summary")

        title = section_title("Запомни", color=GREEN)
        self.play(Write(title), run_time=0.8)

        bullets = VGroup(
            Text("20 аминокиселини. 9 само од храна.",
                 font_size=30, color=YELLOW, weight=BOLD),
            Text("Извори: месо, јајца, риба, грав, соја.",
                 font_size=28, color=BLUE),
            Text("Околу 50 g дневно.",
                 font_size=28, color=ORANGE),
            Text("Без нив — нема живот.",
                 font_size=34, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.7)

        for b in bullets:
            self.play(Write(b), run_time=0.7)
            self.wait(0.25)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, bullets)), run_time=0.9)
        self.wait(0.3)
