"""Download materijalizanas educational resources via Google Drive direct URLs.

Strategy:
1. For each (subject, grade), fetch the Google Sites page HTML
2. Extract (file_id, filename) pairs from the HTML
3. Download each via https://drive.google.com/uc?id=X&export=download
4. Save to reference_raw/<subject_eng>/teacher_materials/g<N>/

Skip subjects not in scope (music, art, PE, religion, ethics).
"""

import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
import http.client

# Mapping of MK subject names → English folder name
SUBJECTS = {
    'математика': 'math',
    'македонски-јазик': 'mk',
    'англиски-јазик': 'english',
    'природни-науки': 'science',
    'општество': 'society',  # grades 1-3 only, maps to mk society? actually goes to subject 'society' but our platform uses 'society' too
    'информатика': 'tech',
    'историја': 'history',
    'географија': 'geography',
    'граѓанско-образование': 'civics',
    'биологија': 'biology',
    'физика': 'physics',
    'хемија': 'chemistry',
    'иновации': 'innovation',
    'техничко-образование': 'tech',
}

# Subjects to skip (out of scope)
SKIP_SUBJECTS = {'музичко-образование', 'ликовно-образование', 'физичко-образование',
                 'воведување-во-религиите', 'етика', 'музичко', 'ликовно', 'физичко',
                 'македонски', 'наставнички-листови'}

GRADE_SLUGS = {
    1: 'прво-одделение',
    2: 'второ-одделение',
    3: 'трето-одделение',
    4: 'четврто-одделение',
    5: 'петто-одделение',
    6: 'шесто-одделение',
    7: 'седмо-одделение',
    8: 'осмо-одделение',
    9: 'деветто-одделение',
}

BASE = 'https://sites.google.com/view/materijalizanas/основно'

# Pair pattern: extracts (file_id, filename) from HTML
PAIR_RE = re.compile(
    r'drive\.google\.com/file/d/([a-zA-Z0-9_-]{25,35})/preview.{0,1500}?\"([^\"]+\.(?:docx|pptx|pdf|xlsx|doc|ppt))\"',
    re.DOTALL
)


def fetch(url, timeout=30):
    """Fetch URL, return body as string or None on error."""
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return None
    except (urllib.error.URLError, http.client.RemoteDisconnected, TimeoutError) as e:
        return None


def sanitize(name):
    """Make filename safe + strip 'Drive, ok ' prefix."""
    name = re.sub(r'^(Drive,\s*)?(ok\s+)?', '', name)
    name = name.replace(' ', '_').replace(',', '').replace('/', '_').replace('\\', '_')
    return name


def download_file(file_id, out_path):
    """Download a Drive file by ID. Returns size or None."""
    url = f'https://drive.google.com/uc?id={file_id}&export=download'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
            with open(out_path, 'wb') as f:
                f.write(data)
            return len(data)
    except Exception as e:
        return None


def process_subject_grade(subject_mk, grade, base_dir='reference_raw'):
    """Fetch page for (subject, grade), download all files."""
    if subject_mk in SKIP_SUBJECTS:
        return
    if subject_mk not in SUBJECTS:
        print(f'  skip unknown subject: {subject_mk}')
        return

    subject_eng = SUBJECTS[subject_mk]
    grade_slug = GRADE_SLUGS[grade]
    slug = f'{subject_mk}-{grade}'

    # URL-encode Cyrillic path segments
    path = f'/{urllib.parse.quote(grade_slug)}/{urllib.parse.quote(slug)}'
    url = BASE.replace('/основно', '/' + urllib.parse.quote('основно')) + path

    out_dir = os.path.join(base_dir, subject_eng, 'teacher_materials', f'g{grade}')
    os.makedirs(out_dir, exist_ok=True)

    html = fetch(url)
    if html is None:
        print(f'  [g{grade} {subject_mk}] no page (404 or fetch error)')
        return

    pairs = []
    seen = set()
    for m in PAIR_RE.finditer(html):
        fid, fname = m.group(1), m.group(2)
        if (fid, fname) in seen:
            continue
        seen.add((fid, fname))
        pairs.append((fid, fname))

    if not pairs:
        print(f'  [g{grade} {subject_mk}] no files found')
        return

    print(f'  [g{grade} {subject_mk}] {len(pairs)} files')

    for fid, fname in pairs:
        safe = sanitize(fname)
        out_path = os.path.join(out_dir, safe)
        if os.path.exists(out_path):
            print(f'    skip existing: {safe}')
            continue
        size = download_file(fid, out_path)
        if size is None:
            print(f'    FAIL: {safe}')
        else:
            kb = size / 1024
            print(f'    {kb:7.1f} KB  {safe}')
        time.sleep(0.3)  # polite


def main():
    subjects_to_run = sys.argv[1:] if len(sys.argv) > 1 else list(SUBJECTS.keys())
    print(f'Subjects: {subjects_to_run}')
    for subject in subjects_to_run:
        print(f'\n=== {subject} ===')
        for grade in range(1, 10):
            process_subject_grade(subject, grade)


if __name__ == '__main__':
    main()
