"""Build complete Grade 6 BRO 1:1 TypeScript and splice into content.ts.

Run: python _g6_build.py
Result: content.ts is updated with new GRADE6_CONTENT section.

Constraints honored:
- UnitData / LessonData / ExerciseData shapes match types/index.ts
- single-quoted strings — NO apostrophes inside (use unicode quotes or rewrites)
- correct: not correctAnswer:
- true-false options: ['Точно','Неточно'] (MK) or ['True','False'] (EN/DE/FR/IT/RU)
- isTest:true for test lessons

This file imports the per-subject content from sibling modules.
"""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load all subject content from a single content module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Subjects list in source order
SUBJECTS_ORDER = ['math', 'mk', 'history', 'science', 'tech',
                  'english', 'german', 'french', 'italian', 'russian']

# ---------------------------------------------------------------------------
# Formatters
# ---------------------------------------------------------------------------

def safe(s: str) -> str:
    """Apostrophe safety: replace ASCII ' with U+2019 inside JS single-quoted strings."""
    return s.replace("'", "’")

def mc(eid, q, opts, correct, hint, expl):
    opts_str = ', '.join(f"'{safe(o)}'" for o in opts)
    return (
        f"            {{ id: '{eid}', type: 'multiple-choice', "
        f"question: '{safe(q)}', options: [{opts_str}], correct: '{safe(correct)}', "
        f"hint: '{safe(hint)}', explanation: '{safe(expl)}' }}"
    )

def tf(eid, q, correct, hint, expl, mk=True):
    opts = "['Точно', 'Неточно']" if mk else "['True', 'False']"
    return (
        f"            {{ id: '{eid}', type: 'true-false', "
        f"question: '{safe(q)}', options: {opts}, correct: '{safe(correct)}', "
        f"hint: '{safe(hint)}', explanation: '{safe(expl)}' }}"
    )

def lesson(lid, title, content_md, exercises, is_test=False):
    flag = "          isTest: true,\n" if is_test else ""
    ex_str = ',\n'.join(exercises)
    # Use raw template literal; markdown content goes between backticks.
    # Escape backslashes/backticks in content_md if needed.
    safe_md = content_md.replace('\\', '\\\\').replace('`', '\\`')
    return f"""        {{
          id: '{lid}',
          title: '{safe(title)}',
{flag}          content: `{safe_md}`,
          exercises: [
{ex_str},
          ],
        }}"""

def unit(uid, title, lessons_list):
    inner = ',\n'.join(lessons_list)
    return f"""    {{
      id: '{uid}',
      title: '{safe(title)}',
      lessons: [
{inner},
      ],
    }}"""

def subject(key, units_list):
    inner = ',\n'.join(units_list)
    return f"  {key}: [\n{inner},\n  ]"

# Expose helpers to importable subject modules
import builtins
builtins.mc = mc
builtins.tf = tf
builtins.lesson = lesson
builtins.unit = unit
builtins.safe = safe

# ---------------------------------------------------------------------------
# Import subject content
# ---------------------------------------------------------------------------

from g6_math import MATH
from g6_mk import MK
from g6_history import HISTORY
from g6_science import SCIENCE
from g6_tech import TECH
from g6_english import ENGLISH
from g6_german import GERMAN
from g6_french import FRENCH
from g6_italian import ITALIAN
from g6_russian import RUSSIAN

ALL = {
    'math': MATH,
    'mk': MK,
    'history': HISTORY,
    'science': SCIENCE,
    'tech': TECH,
    'english': ENGLISH,
    'german': GERMAN,
    'french': FRENCH,
    'italian': ITALIAN,
    'russian': RUSSIAN,
}

# ---------------------------------------------------------------------------
# Build the full GRADE6_CONTENT body
# ---------------------------------------------------------------------------

subj_strs = []
for key in SUBJECTS_ORDER:
    units = ALL[key]
    if not units:
        # empty subject — leave a stub
        subj_strs.append(f"  {key}: []")
        continue
    subj_strs.append(subject(key, units))

body = ',\n\n'.join(subj_strs)
full_block = "export const GRADE6_CONTENT: Record<string, UnitData[]> = {\n" + body + ",\n};\n"

# Quick stats
lesson_count = full_block.count("id: 'math6-") + full_block.count("id: 'mk6-") + \
               full_block.count("id: 'hist6-") + full_block.count("id: 'sci6-") + \
               full_block.count("id: 'tech6-") + full_block.count("id: 'en6-") + \
               full_block.count("id: 'de6-") + full_block.count("id: 'fr6-") + \
               full_block.count("id: 'it6-") + full_block.count("id: 'ru6-")
# subtract units (each unit also has id matching the same prefix patterns we counted) — rough estimate

# ---------------------------------------------------------------------------
# Splice into content.ts
# ---------------------------------------------------------------------------

CONTENT_PATH = r'C:\Users\User\super-dzvedza\src\lib\content.ts'
with open(CONTENT_PATH, 'r', encoding='utf-8') as f:
    src = f.read()

m = re.search(r'export const GRADE6_CONTENT[^\n]*\n', src)
assert m, 'GRADE6_CONTENT not found'
start = m.start()
# find next `export const GRADE` header after GRADE6_CONTENT
m2 = re.search(r'\nexport const GRADE\d_CONTENT', src[m.end():])
assert m2, 'next GRADE export not found'
end = m.end() + m2.start() + 1  # +1 to keep the trailing newline before next export

old = src[start:end]
new_src = src[:start] + full_block + '\n' + src[end:]

with open(CONTENT_PATH, 'w', encoding='utf-8') as f:
    f.write(new_src)

print(f'OK — replaced GRADE6_CONTENT')
print(f'  old block:  {len(old):>6} chars')
print(f'  new block:  {len(full_block):>6} chars')
print(f'  raw lesson ids found in new block: {full_block.count("id: ")}')
