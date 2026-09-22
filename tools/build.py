"""Build the release zip (and pack.png) for the Blackstone Generator data pack.

    python tools/build.py            -> out/blackstone-generator-<version>-mc<mc>.zip
    python tools/build.py --icon     -> also regenerate pack.png from images/Blackstone_Generator.png

The version and Minecraft version come from the "version" file at the repo root
(one line: "2.0 26.3"). The zip contains pack.mcmeta, pack.png and data/ at the
root, so it can be dropped straight into world/datapacks/.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
ICON_SRC = ROOT / "images" / "Blackstone_Generator.png"
ICON = ROOT / "pack.png"


def read_version() -> tuple[str, str]:
    version, mc = (ROOT / "version").read_text().split()
    return version, mc


def make_icon() -> None:
    """128x128 pack icon: a square from the lower middle of the main screenshot
    (the top carries the caption text)."""
    from PIL import Image

    im = Image.open(ICON_SRC).convert("RGB")
    side = min(im.size) * 2 // 3
    left = (im.width - side) // 2
    top = im.height - side
    im = im.crop((left, top, left + side, top + side)).resize((128, 128), Image.LANCZOS)
    im.save(ICON, optimize=True)
    print(f"wrote {ICON.relative_to(ROOT)}")


def build_zip() -> Path:
    version, mc = read_version()
    OUT.mkdir(exist_ok=True)
    target = OUT / f"blackstone-generator-{version}-mc{mc}.zip"
    files = [ROOT / "pack.mcmeta"]
    if ICON.exists():
        files.append(ICON)
    files += sorted(p for p in (ROOT / "data").rglob("*") if p.is_file())
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f.relative_to(ROOT).as_posix())
    print(f"wrote {target.relative_to(ROOT)} ({len(files)} files)")
    return target


def main(argv: list[str]) -> None:
    if "--icon" in argv or not ICON.exists():
        make_icon()
    build_zip()


if __name__ == "__main__":
    main(sys.argv[1:])
