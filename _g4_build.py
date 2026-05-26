"""Generate Grade 4 BRO 1:1 TS and splice into content.ts."""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SUBJECTS_ORDER = ['math', 'mk', 'history', 'science', 'tech', 'english']

def safe(s): return s.replace("'", "’")

def mc(eid, q, opts, correct, hint, expl):
    opts_str = ', '.join(f"'{safe(o)}'" for o in opts)
    return (f"            {{ id: '{eid}', type: 'multiple-choice', "
            f"question: '{safe(q)}', options: [{opts_str}], correct: '{safe(correct)}', "
            f"hint: '{safe(hint)}', explanation: '{safe(expl)}' }}")

def tf(eid, q, correct, hint, expl, mk=True):
    opts = "['Точно', 'Неточно']" if mk else "['True', 'False']"
    return (f"            {{ id: '{eid}', type: 'true-false', "
            f"question: '{safe(q)}', options: {opts}, correct: '{safe(correct)}', "
            f"hint: '{safe(hint)}', explanation: '{safe(expl)}' }}")

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
builtins.mc = mc; builtins.tf = tf; builtins.lesson = lesson; builtins.unit = unit; builtins.safe = safe

from g4_math import MATH
from g4_mk import MK
from g4_history import HISTORY
from g4_science import SCIENCE
from g4_tech import TECH
from g4_english import ENGLISH

ALL = {'math': MATH, 'mk': MK, 'history': HISTORY, 'science': SCIENCE, 'tech': TECH, 'english': ENGLISH}

subj_strs = [subject(k, ALL[k]) for k in SUBJECTS_ORDER]
body = ',\n\n'.join(subj_strs)
full_block = "export const GRADE4_CONTENT: Record<string, UnitData[]> = {\n" + body + ",\n};\n"

CONTENT = r'C:\Users\User\super-dzvedza\src\lib\content.ts'
with open(CONTENT, encoding='utf-8') as f: src = f.read()

m = re.search(r'export const GRADE4_CONTENT[^\n]*\n', src)
start = m.start()
m2 = re.search(r'\nexport const GRADE\d_CONTENT', src[m.end():])
end = m.end() + m2.start() + 1

old = src[start:end]
new_src = src[:start] + full_block + '\n' + src[end:]
with open(CONTENT, 'w', encoding='utf-8') as f: f.write(new_src)

print(f'OK — replaced GRADE4_CONTENT')
print(f'  old: {len(old):>7} chars')
print(f'  new: {len(full_block):>7} chars')
print(f'  ids: {full_block.count("id: ")}')
