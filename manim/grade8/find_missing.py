#!/usr/bin/env python3
import re
from pathlib import Path

CONTENT_TS = Path('../../src/lib/content.ts')
src = CONTENT_TS.read_text(encoding='utf-8')

# Try current regex
LESSON_RE = re.compile(
    r"id:\s*['\"]([a-z]+\d+-\d+-\d+)['\"]"
    r"\s*,\s*"
    r"title:\s*['\"]([^'\"]+)['\"]"
    r"\s*,\s*"
    r"content:\s*`([\s\S]*?)`"
    r"\s*,\s*"
    r"exercises:",
)

matched = set()
for m in LESSON_RE.finditer(src):
    lesson_id = m.group(1)
    if lesson_id.endswith(('8-1-1', '8-1-2', '8-1-3', '8-1-4', '8-1-5', '8-1-6', '8-1-7')):
        # Check each subject
        if any(lesson_id.startswith(s) for s in ['chem8', 'bio8', 'm8']):
            matched.add(lesson_id)

# Find all lesson IDs in the file (any format)
all_ids = set(re.findall(r"id:\s*['\"]([a-z]+8-\d+-\d+)['\"]", src))

# Check for missing
chem8_all = sorted([x for x in all_ids if x.startswith('chem8')])
bio8_all = sorted([x for x in all_ids if x.startswith('bio8')])
m8_all = sorted([x for x in all_ids if x.startswith('m8')])

chem8_parsed = set(m.group(1) for m in LESSON_RE.finditer(src) if m.group(1).startswith('chem8'))
bio8_parsed = set(m.group(1) for m in LESSON_RE.finditer(src) if m.group(1).startswith('bio8'))
m8_parsed = set(m.group(1) for m in LESSON_RE.finditer(src) if m.group(1).startswith('m8'))

print("Chemistry (chem8):")
print(f"  Total in file: {len(chem8_all)}")
print(f"  Parsed by regex: {len(chem8_parsed)}")
missing_chem = set(chem8_all) - chem8_parsed
if missing_chem:
    print(f"  Missing: {sorted(missing_chem)}")

print("\nBiology (bio8):")
print(f"  Total in file: {len(bio8_all)}")
print(f"  Parsed by regex: {len(bio8_parsed)}")
missing_bio = set(bio8_all) - bio8_parsed
if missing_bio:
    print(f"  Missing: {sorted(missing_bio)}")

print("\nMath (m8):")
print(f"  Total in file: {len(m8_all)}")
print(f"  Parsed by regex: {len(m8_parsed)}")
missing_m = set(m8_all) - m8_parsed
if missing_m:
    print(f"  Missing: {sorted(missing_m)}")
