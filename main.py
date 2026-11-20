#!/usr/bin/env python3
"""News-image entry: copy the front-page image to the output directory.

The image (entry.png, beside this file) sums up the world's news of
Thursday 19 November 2026. The grader runs this program twice with no
network; both runs must write the same bytes, so this just copies the file.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
src = HERE / "entry.png"
if not src.is_file():
    raise SystemExit("entry.png missing beside main.py")
shutil.copyfile(src, OUT / "entry.png")
print(f"wrote {OUT / 'entry.png'} ({src.stat().st_size} bytes)")
