"""Upload one subject's reference materials to an OpenAI Vector Store.

Steps:
1. Walk reference_raw/<subject>/ for supported files (.pdf .docx .pptx)
2. Upload each to OpenAI Files API (purpose=assistants)
3. Create vector store <subject>-knowledge with those file IDs
4. Poll until file_counts.completed == total
5. Write vector store ID to corpus_config.json

Idempotent: if config already has an entry for this subject, prints it and exits
unless --force is passed.

Usage:
  python corpus_upload.py math
  python corpus_upload.py math --force
"""
import os
import sys
import json
import time
import urllib.request
from pathlib import Path

# --- config ---
OPENAI_KEY = None
for line in Path('.env.local').read_text().splitlines():
    if line.startswith('OPENAI_API_KEY='):
        OPENAI_KEY = line.split('=', 1)[1].strip()
        break
if not OPENAI_KEY:
    print('FATAL: OPENAI_API_KEY not in .env.local')
    sys.exit(1)

API = 'https://api.openai.com/v1'
HEADERS_JSON = {
    'Authorization': f'Bearer {OPENAI_KEY}',
    'Content-Type': 'application/json',
}

SUPPORTED_EXTS = {'.pdf', '.docx', '.pptx'}
CONFIG_PATH = Path('corpus_config.json')


def http(method, path, body=None, raw_bytes=None, content_type=None):
    url = f'{API}{path}'
    if raw_bytes is not None:
        req = urllib.request.Request(url, method=method, data=raw_bytes)
        req.add_header('Authorization', f'Bearer {OPENAI_KEY}')
        if content_type:
            req.add_header('Content-Type', content_type)
    elif body is not None:
        data = json.dumps(body).encode('utf-8')
        req = urllib.request.Request(url, method=method, data=data)
        for k, v in HEADERS_JSON.items():
            req.add_header(k, v)
    else:
        req = urllib.request.Request(url, method=method)
        req.add_header('Authorization', f'Bearer {OPENAI_KEY}')
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='replace')
        print(f'HTTP {e.code} on {method} {path}: {err[:500]}')
        raise


def upload_file(path: Path) -> str:
    """Multipart upload to /files."""
    boundary = '----formdata-boundary-7m2nq8d'
    # Manually build multipart body since stdlib has no convenient client
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Disposition: form-data; name="purpose"')
    body.append(b'')
    body.append(b'assistants')
    body.append(f'--{boundary}'.encode())
    body.append(
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"'.encode()
    )
    body.append(b'Content-Type: application/octet-stream')
    body.append(b'')
    body.append(path.read_bytes())
    body.append(f'--{boundary}--'.encode())
    body.append(b'')
    raw = b'\r\n'.join(body)

    res = http(
        'POST',
        '/files',
        raw_bytes=raw,
        content_type=f'multipart/form-data; boundary={boundary}',
    )
    return res['id']


def create_vector_store(name: str, file_ids: list[str]) -> str:
    res = http('POST', '/vector_stores', body={'name': name, 'file_ids': file_ids})
    return res['id']


def poll_vector_store(vs_id: str, expected: int, timeout_s: int = 600) -> dict:
    start = time.time()
    while True:
        res = http('GET', f'/vector_stores/{vs_id}')
        fc = res.get('file_counts', {})
        done = fc.get('completed', 0)
        failed = fc.get('failed', 0)
        in_progress = fc.get('in_progress', 0)
        print(f'  status: {done}/{expected} done, {failed} failed, {in_progress} in progress')
        if done + failed >= expected:
            return res
        if time.time() - start > timeout_s:
            print('  TIMEOUT — proceeding with partial')
            return res
        time.sleep(8)


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}


def save_config(cfg: dict):
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False))


def main():
    args = sys.argv[1:]
    if not args:
        print('Usage: python corpus_upload.py <subject> [--force]')
        sys.exit(1)
    subject = args[0]
    force = '--force' in args

    cfg = load_config()
    if subject in cfg and not force:
        print(f'Already configured: {subject} → {cfg[subject]["vector_store_id"]}')
        print('Pass --force to recreate.')
        sys.exit(0)

    src_root = Path(f'reference_raw/{subject}')
    if not src_root.exists():
        print(f'No reference_raw/{subject}/ — abort.')
        sys.exit(1)

    files = sorted(
        p for p in src_root.rglob('*') if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS
    )
    print(f'Found {len(files)} supported files in reference_raw/{subject}/')
    if not files:
        sys.exit(1)

    # Upload all
    file_ids = []
    for i, p in enumerate(files, 1):
        rel = p.relative_to(src_root)
        try:
            fid = upload_file(p)
            file_ids.append(fid)
            print(f'  [{i}/{len(files)}] {fid}  {rel}')
        except Exception as e:
            print(f'  [{i}/{len(files)}] FAIL {rel}: {e}')

    # Create vector store
    vs_name = f'{subject}-knowledge'
    print(f'\nCreating vector store: {vs_name} with {len(file_ids)} files')
    vs_id = create_vector_store(vs_name, file_ids)
    print(f'  vector_store_id = {vs_id}')

    # Poll until indexed
    print('\nWaiting for indexing...')
    final = poll_vector_store(vs_id, expected=len(file_ids))

    cfg[subject] = {
        'vector_store_id': vs_id,
        'name': vs_name,
        'file_count': len(file_ids),
        'created_at': time.time(),
        'final_status': final.get('file_counts'),
    }
    save_config(cfg)
    print(f'\nSaved to corpus_config.json: {subject} → {vs_id}')


if __name__ == '__main__':
    main()
