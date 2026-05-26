"""Generate complete Grade 5 BRO 1:1 TypeScript and splice into content.ts.

Run: python _g5_build.py
"""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SUBJECTS_ORDER = ['math', 'mk', 'history', 'science', 'tech', 'english']

def safe(s: str) -> str:
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

import builtins
builtins.mc = mc
builtins.tf = tf
builtins.lesson = lesson
builtins.unit = unit
builtins.safe = safe

from g5_math import MATH
from g5_mk import MK
from g5_history import HISTORY
from g5_science import SCIENCE
from g5_tech import TECH
from g5_english import ENGLISH

ALL = {
    'math': MATH, 'mk': MK, 'history': HISTORY,
    'science': SCIENCE, 'tech': TECH, 'english': ENGLISH,
}

subj_strs = []
for key in SUBJECTS_ORDER:
    units = ALL[key]
    if not units:
        subj_strs.append(f"  {key}: []")
        continue
    subj_strs.append(subject(key, units))

body = ',\n\n'.join(subj_strs)
full_block = "export const GRADE5_CONTENT: Record<string, UnitData[]> = {\n" + body + ",\n};\n"

CONTENT_PATH = r'C:\Users\User\super-dzvedza\src\lib\content.ts'
with open(CONTENT_PATH, 'r', encoding='utf-8') as f:
    src = f.read()

m = re.search(r'export const GRADE5_CONTENT[^\n]*\n', src)
assert m
start = m.start()
m2 = re.search(r'\nexport const GRADE\d_CONTENT', src[m.end():])
assert m2
end = m.end() + m2.start() + 1

old = src[start:end]
new_src = src[:start] + full_block + '\n' + src[end:]

with open(CONTENT_PATH, 'w', encoding='utf-8') as f:
    f.write(new_src)

print(f'OK — replaced GRADE5_CONTENT')
print(f'  old block: {len(old):>7} chars')
print(f'  new block: {len(full_block):>7} chars')
print(f'  ids in new: {full_block.count("id: ")}')
