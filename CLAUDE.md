# CLAUDE.md — super-dzvezda project compass

> Read this entire file before touching anything. It is the single source of truth for every Claude session on this repo.

---

## What this project is

**super-dzvezda** is a Macedonian-language learning platform for grades 1–9, built with Next.js 16 + Supabase + Tailwind CSS. Students progress through lesson cards, exercises (multiple-choice, true/false, fill-in, drag-drop), and challenge units. Content is stored as structured TypeScript in `src/lib/content.ts` (~95,600 lines, 1,327 lessons across grades 1–9).

The active development goal on `phase2/narration-to-manim` is a **sandbox-style interactive lesson engine**: an AI-generation pipeline (OpenAI) that produces structured lesson specs, rendered by a scene/state runtime in the browser.

---

## Team

| Person | Role | GitHub |
|---|---|---|
| Delco | Lead / repo owner | delconinja |
| Marija | Dev 2 | — |
| Stefanija | Dev 3 | — |
| mkaragonov | Dev 4 (you) | mkaragonov-ctrl |

**Memory does NOT sync between Claude sessions.** Only what is committed to the repo is shared. Keep this file up to date.

---

## Branch policy

| Branch | Purpose |
|---|---|
| `phase2/narration-to-manim` | **Active working branch — all new work goes here** |
| `main` | Intentionally divergent / reverted state |

**Never merge `phase2/narration-to-manim` → `main` without explicit direction from Delco.**

---

## Tech stack

- **Framework:** Next.js 16.2.4 (App Router)
- **Auth + DB:** Supabase (`@supabase/ssr` + `@supabase/supabase-js`)
- **Styling:** Tailwind CSS v4
- **Language:** TypeScript (strict)
- **AI generation:** OpenAI API (sandbox only, not in production)
- **Deployment:** Vercel

---

## File layout

### Stable production files — handle with care

| Path | Description |
|---|---|
| `src/lib/content.ts` | 95,600-line corpus — 1,327 lessons, grades 1–9. Never auto-edit. |
| `src/lib/content-v2.ts` | Content v2 variant (do not confuse with v1) |
| `src/app/lesson/[lessonId]/page.tsx` | 1,146-line production lesson route — **DO NOT TOUCH** |
| `src/lib/subjects.ts` | Subject display order — **LOCKED, do not reorder** |
| `src/lib/schools.ts` | School registry |
| `src/components/math/` | Math visual components (FractionBar, NumberLine, PlaceValueTable, etc.) |
| `src/app/api/tts/route.ts` | TTS endpoint |

### Sandbox / interactive engine (phase2 target — build here)

These files are the goal of `phase2/narration-to-manim`. Create them if they do not yet exist:

| Path | Description |
|---|---|
| `src/app/sandbox/page.tsx` | Sandbox UI — topic input, quick presets, "Генерирај лекција" button |
| `src/app/api/sandbox/generate-lesson/route.ts` | OpenAI generation endpoint |
| `src/components/interactive/LessonRunner.tsx` | Scene/state runtime |
| `src/components/interactive/Widgets.tsx` | Widget dispatcher |
| `src/lib/interactive/math6-1-5-spec.ts` | Hand-written reference spec (the gold standard for output format) |

### Scrapped — do not touch

| Path | Reason |
|---|---|
| `manim/` | Entire folder scrapped 2026-05-27. Do not resurrect, modify, or reference. |

### Build scripts (root level)

`_g4_build.py`, `_g5_build.py`, `_g6_build.py` — Python build scripts for generating grade content. Grade-specific scripts: `g4_math.py`, `g4_mk.py`, etc.

---

## Non-negotiable rules — check before every commit

### 1. TypeScript must compile
```
npx tsc --noEmit
```
Must pass with zero errors. Do not commit if it fails.

### 2. MK glyph sweep
Macedonian Cyrillic and Latin share visually identical glyphs. LLMs silently substitute Latin characters into Cyrillic words. Before committing any content changes, verify that Cyrillic words contain no Latin lookalikes:

| Latin (wrong) | Cyrillic (correct) |
|---|---|
| a | а |
| e | е |
| o | о |
| c | с |
| p | р |
| x | х |

Run a grep or manual scan on any text you generate or edit.

### 3. BRO 1:1 (Books-to-Repo 1:1)
Unit and lesson **titles** must exactly match the official Macedonian school textbooks. Never paraphrase, translate, or creatively rewrite titles. If you are unsure of the exact title, ask Delco — do not guess.

### 4. No triple backticks in template literals
Triple backticks inside template literal strings break the TypeScript parser. Use escaped single backticks or restructure the string.

### 5. Apostrophes in single-quoted TS strings must be escaped
```typescript
// Wrong
const s = 'it's broken'
// Correct
const s = 'it\'s fine'
```

---

## What is deferred — do not attempt without explicit direction

- **Upload corpus to OpenAI** — waiting on licensed school textbook clearance
- **Resurrect anything in `manim/`** — scrapped 2026-05-27, dead end
- **Merge `phase2/narration-to-manim` → `main`** — main is intentionally divergent
- **Deploy `/sandbox` routes to production Vercel** — no auth gate yet; would expose Delco's OpenAI billing to the public
- **Touch `src/app/lesson/[lessonId]/page.tsx`** — 1,146-line production route, off-limits
- **Touch `src/lib/subjects.ts` display order** — locked
- **Push files from `reference_raw/`** — gitignored, copyright-protected source material
- **Touch `credentials.md` or share `.env.local` in chat**

---

## Environment setup

### Required `.env.local` (never commit)
```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
OPENAI_API_KEY=        # only needed for sandbox/AI generation work
```
Get values from Delco via 1Password / Bitwarden / encrypted DM.

### Install and run
```bash
npm install            # ignore peer-deps warnings; stop on hard errors
npm run dev            # dev server at localhost:3000 (or 3001 if busy)
```

### Sandbox smoke test
With `OPENAI_API_KEY` set, open `http://localhost:PORT/sandbox`, click "Генерирај лекција" with the default topic. A lesson should render within 15 seconds.

---

## Git workflow

```bash
# Always work on the active branch
git checkout phase2/narration-to-manim
git pull

# Before committing
npx tsc --noEmit        # must be clean
# MK glyph sweep on any changed content
# BRO 1:1 check on any title changes

git push origin phase2/narration-to-manim
```

---

## Content scale reference

| Grade | Subjects | Lessons (approx) |
|---|---|---|
| 1–3 | Math, Macedonian, Nature/Society | ~200 |
| 4–6 | Math, MK, English, History, Science, Tech (+ foreign langs in G6) | ~500 |
| 7–9 | Full curriculum | ~600 |
| **Total** | | **~1,327** |

Lesson IDs follow the pattern: `{subject}{grade}-{unit}-{lesson}` e.g. `math6-1-5`.
