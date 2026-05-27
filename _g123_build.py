"""Splice Grade 1, 2, 3 BRO 1:1 content into content.ts.

Run: python _g123_build.py [1|2|3|all]
"""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Subject order for Grades 1-3: math, mk, society, science, english (no history)
SUBJECTS_ORDER = ['math', 'mk', 'society', 'science', 'english']

def safe(s): return s.replace("'", "’")
def mc(eid, q, opts, correct, hint, expl):
    opts_str = ', '.join(f"'{safe(o)}'" for o in opts)
    return (f"            {{ id: '{eid}', type: 'multiple-choice', question: '{safe(q)}', "
            f"options: [{opts_str}], correct: '{safe(correct)}', hint: '{safe(hint)}', "
            f"explanation: '{safe(expl)}' }}")
def tf(eid, q, correct, hint, expl, mk=True):
    opts = "['Точно', 'Неточно']" if mk else "['True', 'False']"
    return (f"            {{ id: '{eid}', type: 'true-false', question: '{safe(q)}', "
            f"options: {opts}, correct: '{safe(correct)}', hint: '{safe(hint)}', "
            f"explanation: '{safe(expl)}' }}")
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
    return f"""    {{
      id: '{uid}',
      title: '{safe(title)}',
      lessons: [
{','.join(['\n' + l for l in lessons_list])[1:]},
      ],
    }}"""
def subject(key, units_list):
    return f"  {key}: [\n{','.join(['\n' + u for u in units_list])[1:]},\n  ]"

import builtins
for fn in (mc, tf, lesson, unit, safe):
    setattr(builtins, fn.__name__, fn)

GRADES = sys.argv[1:] if len(sys.argv) > 1 else ['1', '2', '3']
if 'all' in GRADES: GRADES = ['1', '2', '3']

CONTENT = r'C:\Users\User\super-dzvedza\src\lib\content.ts'
with open(CONTENT, encoding='utf-8') as f: src = f.read()

for grade in GRADES:
    mod = __import__(f'g{grade}_all')
    ALL = mod.ALL
    subj_strs = []
    for key in SUBJECTS_ORDER:
        if key not in ALL: continue
        units = ALL[key]
        if not units:
            subj_strs.append(f"  {key}: []")
            continue
        subj_strs.append(subject(key, units))
    body = ',\n\n'.join(subj_strs)
    full_block = f"export const GRADE{grade}_CONTENT: Record<string, UnitData[]> = {{\n{body},\n}};\n"

    m = re.search(rf'export const GRADE{grade}_CONTENT[^\n]*\n', src)
    if not m:
        print(f'GRADE{grade}_CONTENT not found, skipping'); continue
    start = m.start()
    m2 = re.search(r'\nexport const GRADE\d_CONTENT', src[m.end():])
    end = m.end() + m2.start() + 1 if m2 else len(src)
    old = src[start:end]
    src = src[:start] + full_block + '\n' + src[end:]
    print(f'G{grade}: old {len(old):>6} → new {len(full_block):>6}, ids: {full_block.count("id: ")}')

with open(CONTENT, 'w', encoding='utf-8') as f: f.write(src)
print('Done.')
