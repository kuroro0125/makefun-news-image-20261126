#!/usr/bin/env python3
"""Entry for news-image-20261126: copy the rendered front page to /output.

The image (entry.png, 1024x1024) is a newspaper front page summing up the
world news of Thursday 26 November 2026. It was drawn by draw.py in this
repository; this program only places the finished file where the grader
reads it. Standard library only, no network, deterministic: both runs
write the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _output_dir() -> Path:
    """Where the image goes: MAKEFUN_OUTPUT_DIR, else /output, else ./out.

    The grader provides /output; the ./out fallback only exists so the
    entry can be checked locally without root.
    """
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    candidates = [Path(wanted)] if wanted else [Path("/output"), HERE / "out"]
    for cand in candidates:
        try:
            cand.mkdir(parents=True, exist_ok=True)
            return cand
        except OSError:
            continue
    raise SystemExit("no writable output directory found")


def main() -> None:
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit(f"missing image next to main.py: {src}")
    out_dir = _output_dir()
    dest = out_dir / "entry.png"
    shutil.copyfile(src, dest)
    # Guard the competition's own limits: whole PNG, at most 1 MiB.
    data = dest.read_bytes()
    if len(data) > 1_048_576 or not data.startswith(b"\x89PNG"):
        raise SystemExit("output is not a PNG within the 1 MiB cap")


if __name__ == "__main__":
    main()
