#!/usr/bin/env python3
"""
gen_narrations.py — auto-generate Grade 8 narrations via LLM API.

Pipeline (per RULES.md):
  1. Parse src/lib/content.ts, extract each lesson's id, title, content field
  2. Extract lesson metadata: subject, grade, curriculum bullets
  3. Substitute all placeholders into PROMPT_TEMPLATE_v2.md
  4. Send full prompt to the LLM (Gemini default, OpenAI optional)
  5. Save the response to manim/grade8/narrations/{id}.md

Provider setup (pick one):
  Gemini  (free tier — recommended):
      pip install google-genai
      set GEMINI_API_KEY first (get one at https://aistudio.google.com/apikey)
  OpenAI  (paid):
      pip install openai
      set OPENAI_API_KEY first

Usage examples:

    # one lesson via Gemini (default)
    python gen_narrations.py --subject phys --unit 1 --lesson 5

    # whole subject
    python gen_narrations.py --subject phys --all

    # whole Grade 8 video set (~126 lessons)
    python gen_narrations.py --all

    # pick the model
    python gen_narrations.py --subject chem --all --model gemini-2.5-pro
    python gen_narrations.py --subject chem --all --model gemini-2.5-flash

    # switch provider
    python gen_narrations.py --subject phys --all --provider openai --model gpt-5

    # preview without spending tokens / quota
    python gen_narrations.py --subject bio --all --dry-run

    # overwrite existing narrations (otherwise skip them)
    python gen_narrations.py --subject phys --all --force
"""
import argparse
import os
import re
import sys
import time
from pathlib import Path


# Paths -----------------------------------------------------------------------

ROOT       = Path(__file__).resolve().parent       # .../manim/grade8/
PROJECT    = ROOT.parent.parent                    # .../super-dzvedza/
CONTENT_TS = PROJECT / "src" / "lib" / "content.ts"
TEMPLATE   = ROOT / "PROMPT_TEMPLATE_v2.md"
NARRATIONS = ROOT / "narrations"

# Placeholders for the new v2 template
PLACEHOLDERS = {
    "SUBJECT": "[INSERT SUBJECT]",
    "GRADE": "[INSERT GRADE]",
    "TITLE": "[INSERT TITLE]",
    "BULLETS": "[INSERT BULLETS]",
    "TEXT": "[INSERT TEXT]",
}

# Subject prefixes ------------------------------------------------------------

SUBJECT_PREFIXES = {
    "phys":  "phys8",
    "chem":  "chem8",
    "bio":   "bio8",
    "geo":   "geo8",
    "m":     "m8",
    "math":  "m8",
}

# Subjects that have video lessons in Grade 8 (the scope of the pipeline).
VIDEO_SUBJECT_PREFIXES = {"phys8", "chem8", "bio8", "geo8", "m8"}

# Subject ID to readable name mapping
SUBJECT_NAMES = {
    "phys8": "Physics",
    "chem8": "Chemistry",
    "bio8": "Biology",
    "geo8": "Geography",
    "m8": "Mathematics",
}

# Lesson parser ---------------------------------------------------------------
# Each lesson in content.ts looks like:
#   id: 'phys8-1-7',
#   title: 'Триење',
#   content: `## Што е триење?
#   ...
#   ...`,
#   exercises: [ ... ]
# The 'exercises:' field reliably follows 'content:' for every lesson.

LESSON_RE = re.compile(
    r"id:\s*['\"]([a-z]+\d+-\d+-\d+)['\"]"
    r"\s*,\s*"
    r"title:\s*['\"]([^'\"]+)['\"]"
    r"\s*,\s*"
    r"(?:videoUrl:\s*['\"][^'\"]*['\"],\s*)?"  # Skip optional videoUrl field
    r"content:\s*`([\s\S]*?)`"
    r"\s*,\s*"
    r"exercises:",
)


def parse_lessons():
    if not CONTENT_TS.exists():
        sys.exit(f"content.ts not found: {CONTENT_TS}")
    src = CONTENT_TS.read_text(encoding="utf-8")
    lessons = []
    for m in LESSON_RE.finditer(src):
        lesson_id = m.group(1)
        title = m.group(2)
        content = m.group(3).strip()
        lessons.append({
            "id": lesson_id,
            "title": title,
            "content": content,
        })
    return lessons


def extract_prompt(template_text):
    """Return prompt body (PROMPT_TEMPLATE_v2.md is plain text, no code block wrapper)."""
    return template_text


def extract_subject_name(lesson_id):
    """Map lesson ID prefix to human-readable subject name."""
    subj_prefix = lesson_id.split("-")[0]
    return SUBJECT_NAMES.get(subj_prefix, subj_prefix)


def extract_curriculum_bullets(content):
    """Extract ## headings and bullet points from lesson content as curriculum outline."""
    lines = content.split("\n")
    bullets = []
    for line in lines:
        # Capture ## headings (curriculum section headers)
        if line.startswith("## "):
            bullets.append(line[3:].strip())
        # Capture bullet points (- or ### items)
        elif line.startswith("- "):
            bullets.append("  " + line[2:].strip())
        elif line.startswith("### "):
            bullets.append(line[4:].strip())
    return "\n".join(bullets) if bullets else content[:500]  # fallback to first 500 chars


def build_prompt(prompt_body, lesson_id, lesson_title, lesson_content):
    """Substitute all v2 template placeholders with lesson metadata."""
    # Extract metadata
    subject_name = extract_subject_name(lesson_id)
    grade = "8"
    curriculum_bullets = extract_curriculum_bullets(lesson_content)

    # Verify all placeholders exist
    for key, placeholder in PLACEHOLDERS.items():
        if placeholder not in prompt_body:
            raise ValueError(
                f"Placeholder {placeholder} not found in PROMPT_TEMPLATE_v2.md"
            )

    # Substitute all placeholders
    result = prompt_body
    result = result.replace(PLACEHOLDERS["SUBJECT"], subject_name)
    result = result.replace(PLACEHOLDERS["GRADE"], grade)
    result = result.replace(PLACEHOLDERS["TITLE"], lesson_title)
    result = result.replace(PLACEHOLDERS["BULLETS"], curriculum_bullets)
    result = result.replace(PLACEHOLDERS["TEXT"], lesson_content)

    return result


def filter_lessons(lessons, subject, unit, lesson, include_all_subjects=False):
    """Filter lessons by subject/unit/lesson.

    Without --subject, defaults to the 5 Grade-8 video subjects
    (phys/chem/bio/geo/m).  Pass include_all_subjects=True to widen.
    """
    pref = SUBJECT_PREFIXES.get(subject) if subject else None
    out = []
    for L in lessons:
        subj_part = L["id"].split("-")[0]
        if pref:
            if not L["id"].startswith(pref + "-"):
                continue
        else:
            # No --subject given: restrict to Grade-8 video subjects unless asked otherwise
            if not include_all_subjects and subj_part not in VIDEO_SUBJECT_PREFIXES:
                continue
        parts = L["id"].split("-")  # e.g. ['phys8', '1', '7']
        if unit is not None and parts[1] != str(unit):
            continue
        if lesson is not None and parts[2] != str(lesson):
            continue
        out.append(L)
    return out


def make_client(provider):
    """Return a call_fn for the chosen provider."""
    if provider == "gemini":
        try:
            from google import genai
            from google.genai import types
        except ImportError:
            sys.exit("Install the Gemini SDK first:\n    pip install google-genai")
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            sys.exit("Set the GEMINI_API_KEY environment variable first.\n"
                     "Get a free key at https://aistudio.google.com/apikey")
        client = genai.Client(api_key=api_key)

        def call(model, prompt, temperature):
            resp = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=temperature),
            )
            return resp.text

        return call

    if provider == "openai":
        try:
            from openai import OpenAI
        except ImportError:
            sys.exit("Install the OpenAI SDK first:\n    pip install openai")
        if not os.environ.get("OPENAI_API_KEY"):
            sys.exit("Set the OPENAI_API_KEY environment variable first.")
        client = OpenAI()

        def call(model, prompt, temperature):
            kwargs = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
            }
            # GPT-5 / reasoning models only accept temperature=1.
            if model.startswith("gpt-4"):
                kwargs["temperature"] = temperature
            resp = client.chat.completions.create(**kwargs)
            return resp.choices[0].message.content

        return call

    if provider == "groq":
        try:
            from groq import Groq
        except ImportError:
            sys.exit("Install the Groq SDK first:\n    pip install groq")
        if not os.environ.get("GROQ_API_KEY"):
            sys.exit("Set the GROQ_API_KEY environment variable first.\n"
                     "Get a free key at https://console.groq.com/keys")
        client = Groq()

        def call(model, prompt, temperature):
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=8000,
            )
            return resp.choices[0].message.content

        return call

    sys.exit(f"Unknown provider: {provider}")


DEFAULT_MODELS = {
    "gemini": "gemini-2.5-pro",
    "openai": "gpt-5",
    "groq":   "llama-3.3-70b-versatile",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--subject", choices=list(SUBJECT_PREFIXES.keys()),
                        help="phys | chem | bio | geo | m (math)")
    parser.add_argument("--unit", type=int, help="Unit number (1..7)")
    parser.add_argument("--lesson", type=int, help="Lesson number within unit")
    parser.add_argument("--all", action="store_true",
                        help="All lessons matching the subject "
                             "(or all 5 Grade-8 video subjects if no --subject)")
    parser.add_argument("--include-all-subjects", action="store_true",
                        help="With --all and no --subject, widen scope beyond the 5 video subjects")
    parser.add_argument("--provider", choices=["gemini", "openai", "groq"], default="gemini",
                        help="LLM provider (default: gemini)")
    parser.add_argument("--model", default=None,
                        help="Model name.  Defaults: gemini-2.5-pro for Gemini, gpt-5 for OpenAI")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing narration .md files")
    parser.add_argument("--dry-run", action="store_true",
                        help="List target lessons without calling the API")
    parser.add_argument("--export-prompts", action="store_true",
                        help="Write each lesson's full prompt as prompts/{id}.txt "
                             "for manual paste into ChatGPT or another web LLM. "
                             "Skips lessons that already have a narration unless --force.")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="Sampling temperature (ignored for gpt-5 / reasoning models)")
    args = parser.parse_args()

    if not (args.all or args.subject):
        parser.error("Specify --subject (and optional --unit/--lesson) or --all")

    if not TEMPLATE.exists():
        sys.exit(f"PROMPT_TEMPLATE_v2.md not found: {TEMPLATE}")

    template_text = TEMPLATE.read_text(encoding="utf-8")
    prompt_body = extract_prompt(template_text)

    NARRATIONS.mkdir(parents=True, exist_ok=True)

    lessons = parse_lessons()
    if not lessons:
        sys.exit("No lessons parsed from content.ts (the regex may need updating)")
    print(f"Parsed {len(lessons)} lessons from content.ts")

    targets = filter_lessons(lessons, args.subject, args.unit, args.lesson,
                             include_all_subjects=args.include_all_subjects)
    if not targets:
        sys.exit("No lessons matched the filter")
    print(f"Matched {len(targets)} lesson(s) for current filter")

    if args.dry_run:
        for L in targets:
            exists = (NARRATIONS / f"{L['id']}.md").exists()
            tag = " (exists)" if exists else ""
            print(f"  {L['id']}  —  {L['title']}{tag}")
        return

    if args.export_prompts:
        prompts_dir = ROOT / "prompts"
        prompts_dir.mkdir(parents=True, exist_ok=True)
        written = skipped = 0
        for L in targets:
            narr_path = NARRATIONS / f"{L['id']}.md"
            if narr_path.exists() and not args.force:
                skipped += 1
                continue
            prompt = build_prompt(prompt_body, L["id"], L["title"], L["content"])
            out = prompts_dir / f"{L['id']}.txt"
            header = (f"=== {L['id']}  —  {L['title']} ===\n"
                      f"Save the ChatGPT response to:\n"
                      f"  manim/grade8/narrations/{L['id']}.md\n"
                      f"with a leading line:\n"
                      f"  # {L['id']} — {L['title']}\n\n"
                      f"=" * 60 + "\n\n")
            out.write_text(header + prompt, encoding="utf-8")
            written += 1
        print(f"\nExported {written} prompts to {prompts_dir}")
        print(f"Skipped {skipped} (narrations already exist; use --force to re-export)")
        return

    model = args.model or DEFAULT_MODELS[args.provider]
    call = make_client(args.provider)

    total = len(targets)
    done = skipped = failed = 0

    print(f"Provider: {args.provider}   Model: {model}\n")

    for i, L in enumerate(targets, 1):
        out_path = NARRATIONS / f"{L['id']}.md"
        if out_path.exists() and not args.force:
            print(f"[{i}/{total}] {L['id']:14s}  SKIP — exists (use --force to overwrite)")
            skipped += 1
            continue

        prompt = build_prompt(prompt_body, L["id"], L["title"], L["content"])
        print(f"[{i}/{total}] {L['id']:14s}  →  calling {model}...", flush=True)
        t0 = time.time()
        try:
            text = call(model, prompt, args.temperature)
            elapsed = time.time() - t0
            if not text:
                raise RuntimeError("empty response from model")
            header = f"# {L['id']} — {L['title']}\n\n"
            out_path.write_text(header + text.strip() + "\n", encoding="utf-8")
            print(f"            done in {elapsed:.1f}s   "
                  f"({len(text)} chars)   →  narrations/{out_path.name}")
            done += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            break
        except Exception as exc:
            print(f"            FAILED: {exc}", file=sys.stderr)
            failed += 1

    print(f"\nFinished.  written: {done}   skipped: {skipped}   failed: {failed}")


if __name__ == "__main__":
    main()
