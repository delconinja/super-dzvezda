#!/usr/bin/env python3
"""
download_assets.py — fetch curated SVG/PNG assets from Wikimedia Commons.

Uses Wikimedia's Special:FilePath endpoint which auto-resolves file renames
and redirects. Files are public-domain or CC-BY-SA — attribution lives in
ASSETS.md.

Usage:
    python download_assets.py             # everything
    python download_assets.py --biology   # biology only
    python download_assets.py --maps      # maps only
    python download_assets.py --force     # re-download existing
    python download_assets.py --verify    # download + report sizes, no skip
"""
import argparse
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

FILEPATH_BASE = "https://commons.wikimedia.org/wiki/Special:FilePath/"

# (local_filename, wikimedia_filename, short_description)
BIOLOGY = [
    ("human-skeleton.svg",     "Human skeleton front en.svg",                 "Full human skeleton, front view"),
    ("heart.svg",              "Diagram of the human heart (cropped).svg",    "Human heart anatomy, labeled"),
    ("lungs.svg",              "Lungs diagram detailed.svg",                  "Human lungs and bronchi"),
    ("brain.svg",              "Brain human normal inferior view with labels en.svg", "Human brain, inferior view, labeled"),
    ("digestive-system.svg",   "Digestive system diagram en.svg",             "Digestive tract, labeled"),
    ("eye-anatomy.svg",        "Schematic diagram of the human eye en.svg",   "Human eye cross-section"),
    ("animal-cell.svg",        "Animal cell structure en.svg",                "Animal cell organelles"),
    ("plant-cell.svg",         "Plant cell structure svg labels.svg",         "Plant cell organelles"),
    ("dna-helix.svg",          "DNA simple2.svg",                             "DNA double helix"),
    ("muscle.svg",             "202107 Structure of skeletal muscle.svg",     "Skeletal muscle structure"),
]

MAPS = [
    ("europe-blank.svg",       "Blank map of Europe.svg",                     "Blank political map of Europe"),
    ("world-blank.svg",        "BlankMap-World.svg",                          "Blank world political map"),
    ("macedonia-in-europe.svg","Macedonia in Europe.svg",                     "Macedonia highlighted on Europe"),
    ("macedonia-overview.svg", "Macedonia overview.svg",                      "Macedonia country outline"),
]


def download(url, target, force=False, verify=False):
    if target.exists() and not (force or verify):
        return ("skip", target.stat().st_size)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "super-dzvedza-grade8/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 200:
            return ("FAIL", f"response too small ({len(data)} bytes)")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return ("ok", len(data))
    except urllib.error.HTTPError as exc:
        return ("FAIL", f"HTTP {exc.code}")
    except Exception as exc:
        return ("FAIL", str(exc))


def run(items, subfolder, force, verify):
    print(f"\n[{subfolder}]")
    ok = skip = fail = 0
    for local_name, wiki_name, desc in items:
        target = ASSETS / subfolder / local_name
        url = FILEPATH_BASE + wiki_name.replace(" ", "_")
        status, info = download(url, target, force=force, verify=verify)
        if status == "ok":
            kb = info / 1024
            print(f"  ok    {local_name:30s}  {kb:6.1f} KB   {desc}")
            ok += 1
        elif status == "skip":
            kb = info / 1024
            print(f"  skip  {local_name:30s}  {kb:6.1f} KB   (exists)")
            skip += 1
        else:
            print(f"  FAIL  {local_name:30s}  {info}")
            fail += 1
        time.sleep(0.3)  # be polite to Wikimedia
    print(f"  -> {ok} downloaded, {skip} skipped, {fail} failed")
    return fail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--biology", action="store_true")
    parser.add_argument("--maps", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--verify", action="store_true",
                        help="Re-download all and report sizes")
    args = parser.parse_args()

    if not (args.biology or args.maps):
        args.biology = args.maps = True

    fails = 0
    if args.biology:
        fails += run(BIOLOGY, "biology", args.force, args.verify)
    if args.maps:
        fails += run(MAPS, "maps", args.force, args.verify)

    print(f"\nDone.   Assets folder: {ASSETS}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
