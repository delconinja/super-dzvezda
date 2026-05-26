#!/usr/bin/env python3
import re
from pathlib import Path

CONTENT_TS = Path('../../src/lib/content.ts')
src = CONTENT_TS.read_text(encoding='utf-8')

# Count all Grade 8 lessons
pattern = r"id: '([a-z]+8-[0-9]+-[0-9]+)'"
matches = re.findall(pattern, src)
print(f'Total Grade 8 lessons: {len(matches)}')
print()

# Count by subject
subjects = {}
for m in matches:
    subj = m.split('-')[0]
    subjects[subj] = subjects.get(subj, 0) + 1

for subj in sorted(subjects.keys()):
    print(f'  {subj}: {subjects[subj]}')

# Sum only the video subjects (for TARGET pipeline)
VIDEO_SUBJECTS = {"phys8", "chem8", "bio8", "geo8", "m8", "mk8", "en8"}
video_total = sum(v for k, v in subjects.items() if k in VIDEO_SUBJECTS)
print()
print(f'Video subjects total (phys/chem/bio/geo/m/mk/en): {video_total}')

# Other grades
other_subjects = {k: v for k, v in subjects.items() if k not in VIDEO_SUBJECTS}
if other_subjects:
    print(f'Other Grade 8 subjects: {other_subjects}')
