#!/usr/bin/env python3
"""
qa_narrations.py — automated language quality check for narrations.

Scans every .md in narrations/ and scores it against RULES.md requirements:
  - Latin/Cyrillic homoglyph contamination
  - Minimum length (RULES.md: 5000+ chars for full storytelling)
  - All §1-§7 MK section headers present
  - English label leaks (HOOK, EXAMPLE, FORMULA, etc.)
  - Serbian/Bulgarian word leaks (пуж, тачка, итд.)
  - Missing worked example for math/chem/phys formula lessons
  - Common MK gender agreement errors (тело кој, сила кој, ...)

Outputs a ranked list — worst first — so you know which to re-do
via a stronger model.

Usage:
    python qa_narrations.py                # all narrations
    python qa_narrations.py --subject phys # one subject
    python qa_narrations.py --json out.json # machine-readable
    python qa_narrations.py --top 20       # show only worst 20
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NARRATIONS = ROOT / "narrations"

# Words that should never appear (Serbian/Bulgarian leaks; expand as found)
FORBIDDEN_WORDS = {
    "пуж":      "Serbian for snail. Use MK 'полжав'",
    "тачка":    "Serbian. MK uses 'точка'",
    "вапно":    "older form. Use MK 'вар'",
    "дистанциски": "non-standard. Use MK 'далечински'",
    "ваздух":   "Serbian. MK uses 'воздух'",
    "хвала":    "Serbian/Croatian. MK uses 'благодарам'",
    "молим":    "Serbian. MK uses 'те молам' / 'ве молам'",
    "сада":     "Serbian. MK uses 'сега'",
}

# English labels that leaked through from older prompt template
ENGLISH_LABELS = [
    "HOOK", "CORE CONCEPT", "DEFINITION", "STORY", "VISUAL DEMO",
    "KEY PROPERTIES", "INSIGHT", "REAL-WORLD", "EXAMPLES", "COMPARISON",
    "CLOSING MESSAGE", "FORMULA",
]

# Required MK section headers (must all be present)
REQUIRED_HEADERS_MK = [
    "КУКА", "СУШТИНА", "ПРИКАЗНА", "СВОЈСТВА", "ПРИМЕРИ",
    "СПОРЕДБА", "ЗАКЛУЧОК",
]
# §6 СПОРЕДБА is "if applicable" so we don't hard-require it.

# Latin chars masquerading as Cyrillic — only flag when inside a Cyrillic word
LATIN_HOMOGLYPHS = {
    "j": "ј", "a": "а", "o": "о", "e": "е", "c": "с", "p": "р", "y": "у",
}

CYRILLIC_RANGE = re.compile(r"[Ѐ-ӿ]")

# Gender mismatch patterns — neuter/feminine nouns paired with masculine pronoun
GENDER_PATTERNS = [
    (r"\bтело\s+кој\b", "neuter 'тело' should pair with 'кое' not 'кој'"),
    (r"\bјаболко\s+кој\b", "neuter 'јаболко' should pair with 'кое'"),
    (r"\bсила\s+кој\b", "feminine 'сила' should pair with 'која' not 'кој'"),
    (r"\bземја\s+кој\b", "feminine 'земја' should pair with 'која'"),
    (r"\bмолекула\s+кој\b", "feminine 'молекула' should pair with 'која'"),
]

MIN_CHARS = 5000  # RULES.md target


def check_homoglyphs(text):
    """Find Latin chars inside Cyrillic words."""
    out = []
    for word in re.findall(r"\S+", text):
        if not CYRILLIC_RANGE.search(word):
            continue
        # word contains at least one Cyrillic char — flag any Latin that looks Cyrillic
        for ch in word:
            if ch.lower() in LATIN_HOMOGLYPHS:
                # but only if the char is sandwiched between Cyrillic neighbors
                idx = word.find(ch)
                left = word[idx-1] if idx > 0 else ""
                right = word[idx+1] if idx + 1 < len(word) else ""
                if (CYRILLIC_RANGE.search(left) or CYRILLIC_RANGE.search(right)):
                    out.append((word, ch, LATIN_HOMOGLYPHS[ch.lower()]))
                    break
    return out


def is_formula_lesson(lesson_id):
    return lesson_id.split("-")[0] in ("m8", "phys8", "chem8")


def check_worked_example(text, lesson_id):
    """Formula lessons must have step-by-step + verification per RULES.md."""
    if not is_formula_lesson(lesson_id):
        return True
    has_step = bool(re.search(r"чекор", text, re.IGNORECASE))
    has_check = bool(re.search(r"провер|проверка", text, re.IGNORECASE))
    return has_step and has_check


def qa_one(path):
    text = path.read_text(encoding="utf-8")
    lesson_id = path.stem
    issues = []

    # 1. Length
    char_count = len(text)
    if char_count < MIN_CHARS:
        issues.append(("LEN", f"only {char_count} chars (need >= {MIN_CHARS})"))

    # 2. Required MK section headers
    missing = [h for h in REQUIRED_HEADERS_MK if h not in text and h != "СПОРЕДБА"]
    if missing:
        issues.append(("HEADERS", f"missing MK sections: {', '.join(missing)}"))

    # 3. English label leaks
    leaked = [lbl for lbl in ENGLISH_LABELS if lbl in text]
    if leaked:
        issues.append(("ENGLISH", f"English labels in MK text: {', '.join(leaked)}"))

    # 4. Forbidden words
    bad_words = []
    for w, reason in FORBIDDEN_WORDS.items():
        if re.search(rf"\b{w}\b", text, re.IGNORECASE):
            bad_words.append(f"'{w}' ({reason})")
    if bad_words:
        issues.append(("WORDS", "; ".join(bad_words)))

    # 5. Latin/Cyrillic homoglyphs
    homo = check_homoglyphs(text)
    if homo:
        examples = ", ".join(f"{w} ({lat}→{cyr})" for w, lat, cyr in homo[:5])
        issues.append(("HOMOGLYPH", f"{len(homo)} word(s): {examples}"))

    # 6. Gender agreement
    bad_gender = []
    for pat, msg in GENDER_PATTERNS:
        if re.search(pat, text):
            bad_gender.append(msg)
    if bad_gender:
        issues.append(("GENDER", "; ".join(bad_gender)))

    # 7. Worked example for math/chem/phys
    if not check_worked_example(text, lesson_id):
        issues.append(("EXAMPLE", "no step-by-step worked example (RULES.md required for formula lessons)"))

    return {
        "id": lesson_id,
        "chars": char_count,
        "issues": issues,
        "score": len(issues),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", help="filter to one subject prefix (phys/chem/bio/geo/m)")
    parser.add_argument("--top", type=int, help="show only worst N")
    parser.add_argument("--json", help="dump full results to JSON file")
    parser.add_argument("--clean", action="store_true", help="only show files with zero issues")
    args = parser.parse_args()

    files = sorted(NARRATIONS.glob("*.md"))
    if args.subject:
        prefix_map = {"phys": "phys8", "chem": "chem8", "bio": "bio8",
                      "geo": "geo8", "m": "m8"}
        pref = prefix_map.get(args.subject, args.subject)
        files = [f for f in files if f.stem.startswith(pref + "-")]

    results = [qa_one(f) for f in files]
    # Sort worst-first
    results.sort(key=lambda r: (-r["score"], r["chars"]))

    if args.clean:
        results = [r for r in results if r["score"] == 0]
    if args.top:
        results = results[:args.top]

    print(f"Scanned {len(results)} narrations.\n")

    by_score = {}
    for r in results:
        by_score.setdefault(r["score"], 0)
        by_score[r["score"]] += 1

    print("Score histogram (issues per file):")
    for s in sorted(by_score.keys()):
        bar = "#" * min(by_score[s], 40)
        print(f"  {s} issues:  {by_score[s]:3d}  {bar}")
    print()

    if not args.clean:
        print("Worst-first ranking:\n")
        for r in results:
            tag = "CLEAN" if r["score"] == 0 else f"{r['score']} issue(s)"
            print(f"  [{tag}]  {r['id']:15s}  ({r['chars']:5d} chars)")
            for code, msg in r["issues"]:
                print(f"          {code}:  {msg}")
            if r["issues"]:
                print()

    if args.json:
        Path(args.json).write_text(json.dumps(results, ensure_ascii=False, indent=2),
                                   encoding="utf-8")
        print(f"\nFull results written to {args.json}")


if __name__ == "__main__":
    main()
