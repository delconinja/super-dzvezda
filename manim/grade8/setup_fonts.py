#!/usr/bin/env python3
"""
setup_fonts.py — Download and install Google Fonts Noto Sans (Macedonian support).

Usage:
    python setup_fonts.py

This will:
1. Download Noto Sans from Google Fonts
2. Install to system fonts directory
3. Configure Manim to use it
"""
import os
import sys
import urllib.request
import zipfile
import shutil
from pathlib import Path

FONT_URL = "https://fonts.google.com/download?family=Noto+Sans"
FONTS_DIR = Path(os.path.expandvars(r"%WINDIR%\Fonts"))
DOWNLOAD_DIR = Path.home() / "Downloads" / "noto-sans"
MANIM_FONTS_DIR = Path.home() / ".manim" / "fonts"

def download_noto_sans():
    """Download Noto Sans font family."""
    print("📥 Downloading Noto Sans from Google Fonts...")
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    zip_path = DOWNLOAD_DIR / "noto-sans.zip"

    try:
        urllib.request.urlretrieve(FONT_URL, zip_path)
        print(f"✅ Downloaded to {zip_path}")
        return zip_path
    except Exception as e:
        print(f"❌ Download failed: {e}")
        print("\nFallback: Download manually from https://fonts.google.com/noto/specimen/Noto+Sans")
        return None

def extract_fonts(zip_path):
    """Extract fonts from zip."""
    print(f"📂 Extracting fonts...")
    extract_dir = DOWNLOAD_DIR / "extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_dir)
        print(f"✅ Extracted to {extract_dir}")
        return extract_dir
    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        return None

def install_fonts_windows(extract_dir):
    """Copy fonts to Windows Fonts directory."""
    print(f"📋 Installing fonts to Windows...")

    if not FONTS_DIR.exists():
        print(f"❌ Fonts directory not found: {FONTS_DIR}")
        return False

    font_files = list(extract_dir.glob("*.ttf")) + list(extract_dir.glob("*.otf"))

    if not font_files:
        print("❌ No font files found in extracted directory")
        return False

    success_count = 0
    for font_file in font_files:
        try:
            dest = FONTS_DIR / font_file.name
            shutil.copy(font_file, dest)
            print(f"  ✅ Installed: {font_file.name}")
            success_count += 1
        except PermissionError:
            print(f"  ⚠️  Permission denied: {font_file.name} (try running as admin)")
        except Exception as e:
            print(f"  ❌ Failed: {font_file.name} - {e}")

    return success_count > 0

def configure_manim(extract_dir):
    """Configure Manim to use Noto Sans."""
    print("\n⚙️  Configuring Manim...")

    manim_config_dir = Path.home() / ".manim"
    manim_config_dir.mkdir(parents=True, exist_ok=True)

    fonts_dir = manim_config_dir / "fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)

    # Copy fonts to Manim fonts directory
    font_files = list(extract_dir.glob("*.ttf")) + list(extract_dir.glob("*.otf"))
    for font_file in font_files:
        try:
            shutil.copy(font_file, fonts_dir / font_file.name)
            print(f"  ✅ Copied to Manim: {font_file.name}")
        except Exception as e:
            print(f"  ⚠️  Could not copy {font_file.name}: {e}")

    # Create Manim configuration
    manim_cfg = Path.home() / ".manim" / "manim.cfg"

    config_content = """[CLI]
renderer = cairo

[quality]
quality = low_quality_15

[fonts]
font = Noto Sans
text_font = Noto Sans
math_font = DejaVu Math TeX Gyre

[resolution]
frame_rate = 15
pixel_height = 480
pixel_width = 854
"""

    if not manim_cfg.exists():
        manim_cfg.write_text(config_content)
        print(f"✅ Created Manim config: {manim_cfg}")
    else:
        print(f"ℹ️  Manim config already exists: {manim_cfg}")
        print("   (You may want to add font settings manually)")

def main():
    print("=" * 60)
    print("MANIM FONT SETUP — Noto Sans (Macedonian Support)")
    print("=" * 60)

    # Download
    zip_path = download_noto_sans()
    if not zip_path:
        print("\n⚠️  Skipping font installation (download failed)")
        print("You can manually install from: https://fonts.google.com/noto/specimen/Noto+Sans")
        return False

    # Extract
    extract_dir = extract_fonts(zip_path)
    if not extract_dir:
        print("❌ Failed to extract fonts")
        return False

    # Install to Windows
    if install_fonts_windows(extract_dir):
        print("✅ Fonts installed to Windows")
    else:
        print("⚠️  Font installation incomplete")

    # Configure Manim
    configure_manim(extract_dir)

    # Verify
    print("\n✅ Setup complete!")
    print("\nTo test Manim with Noto Sans:")
    print("  python -c \"from manim import *; Text('Привет, Македонија!', font='Noto Sans')\"")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
