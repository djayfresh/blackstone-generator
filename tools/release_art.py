"""Planet Minecraft images built with PIL from vanilla 26.3 textures.

    python tools/release_art.py           -> images/cover.png, images/setup.png, images/markers.png
    python tools/release_art.py cover     -> one of them

Textures and the ascii bitmap font come from the 26.3 client jar in the launcher
folder (MC_JAR below). All three images are 1280x720.
"""
from __future__ import annotations

import io
import math
import os
import sys
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
MC_JAR = Path(os.environ.get("MC_JAR", Path.home() / "AppData/Roaming/.minecraft/versions/26.3/26.3.jar"))
W, H = 1280, 720

_jar: zipfile.ZipFile | None = None


def mc_tex(path: str) -> Image.Image:
    global _jar
    if _jar is None:
        _jar = zipfile.ZipFile(MC_JAR)
    return Image.open(io.BytesIO(_jar.read(f"assets/minecraft/textures/{path}"))).convert("RGBA")


def block_tex(name: str) -> Image.Image:
    return mc_tex(f"block/{name}.png").crop((0, 0, 16, 16))  # first frame of animated strips


def up(img: Image.Image, k: int) -> Image.Image:
    return img.resize((img.width * k, img.height * k), Image.NEAREST)


def shade(img: Image.Image, f: float) -> Image.Image:
    r, g, b, a = img.split()
    lut = [min(255, int(v * f)) for v in range(256)]
    return Image.merge("RGBA", (r.point(lut), g.point(lut), b.point(lut), a))


# ---------------------------------------------------------------- bitmap font
class AsciiFont:
    def __init__(self) -> None:
        self.sheet = mc_tex("font/ascii.png")

    def glyph(self, ch: str) -> Image.Image:
        c = ord(ch)
        g = self.sheet.crop(((c % 16) * 8, (c // 16) * 8, (c % 16) * 8 + 8, (c // 16) * 8 + 8))
        if ch == " ":
            return g.crop((0, 0, 3, 8))
        bbox = g.getbbox()
        return g.crop((0, 0, bbox[2], 8)) if bbox else g.crop((0, 0, 4, 8))

    def render(self, text: str, color=(255, 255, 255), scale: int = 4, shadow=(40, 40, 40)) -> Image.Image:
        glyphs = [self.glyph(ch) for ch in text]
        w = sum(g.width + 1 for g in glyphs)
        line = Image.new("RGBA", (w + 1, 9), (0, 0, 0, 0))
        x = 0
        for g in glyphs:
            if shadow is not None:
                line.paste(Image.new("RGBA", g.size, shadow + (255,)), (x + 1, 1), g.split()[3])
            x += g.width + 1
        x = 0
        for g in glyphs:
            line.paste(Image.new("RGBA", g.size, color + (255,)), (x, 0), g.split()[3])
            x += g.width + 1
        return up(line, scale)


FONT: AsciiFont | None = None


def text(s: str, color=(255, 255, 255), scale=4, shadow=(40, 40, 40)) -> Image.Image:
    global FONT
    if FONT is None:
        FONT = AsciiFont()
    return FONT.render(s, color, scale, shadow)


# ------------------------------------------------------- isometric cube render
COS30, SIN30 = math.cos(math.radians(30)), math.sin(math.radians(30))


def project(x: float, y: float, z: float, s: float, ox: float, oy: float):
    return ox + (x - z) * COS30 * s, oy + (x + z) * SIN30 * s - y * s


def paste_quad(canvas: Image.Image, face: Image.Image, p0, p1, p2):
    """Map face so its (0,0) lands on p0, (w,0) on p1, (0,h) on p2 (a parallelogram)."""
    w, h = face.size
    ax, ay = (p1[0] - p0[0]) / w, (p1[1] - p0[1]) / w
    bx, by = (p2[0] - p0[0]) / h, (p2[1] - p0[1]) / h
    det = ax * by - bx * ay
    ia, ib, ic, id_ = by / det, -bx / det, -ay / det, ax / det
    xs = [p0[0], p1[0], p2[0], p1[0] + p2[0] - p0[0]]
    ys = [p0[1], p1[1], p2[1], p1[1] + p2[1] - p0[1]]
    x0, y0 = int(math.floor(min(xs))), int(math.floor(min(ys)))
    x1, y1 = int(math.ceil(max(xs))), int(math.ceil(max(ys)))
    c = ia * (x0 - p0[0]) + ib * (y0 - p0[1])
    f = ic * (x0 - p0[0]) + id_ * (y0 - p0[1])
    warped = face.transform((x1 - x0, y1 - y0), Image.AFFINE, (ia, ib, c, ic, id_, f), Image.NEAREST)
    canvas.alpha_composite(warped, (x0, y0))


class Iso:
    """Isometric scene: blocks at integer (x, y, z), block size s px per unit."""

    def __init__(self, s: int, ox: float, oy: float, size=(W, H)):
        self.s, self.ox, self.oy = s, ox, oy
        self.canvas = Image.new("RGBA", size, (0, 0, 0, 0))
        self.blocks: list[tuple[int, int, int, str, str, float]] = []

    def add(self, x: int, y: int, z: int, top: str, side: str | None = None, height: float = 1.0):
        self.blocks.append((x, y, z, top, side or top, height))

    def P(self, x, y, z):
        return project(x, y, z, self.s, self.ox, self.oy)

    def draw(self) -> Image.Image:
        s = self.s
        for x, y, z, top, side, h in sorted(self.blocks, key=lambda b: (b[0] + b[2], b[1])):
            t = up(block_tex(top), s // 16 or 1).resize((s, s), Image.NEAREST)
            sd = up(block_tex(side), s // 16 or 1).resize((s, s), Image.NEAREST)
            y1 = y + h
            sd = sd.crop((0, 0, s, max(1, int(s * h))))
            P = self.P
            paste_quad(self.canvas, t, P(x, y1, z), P(x + 1, y1, z), P(x, y1, z + 1))
            paste_quad(self.canvas, shade(sd, 0.8), P(x, y1, z + 1), P(x + 1, y1, z + 1), P(x, y, z + 1))
            paste_quad(self.canvas, shade(sd, 0.6), P(x + 1, y1, z + 1), P(x + 1, y1, z), P(x + 1, y, z + 1))
        return self.canvas


# ------------------------------------------------------------ 2D side-view kit
def cube_face(name: str, px: int) -> Image.Image:
    return block_tex(name).resize((px, px), Image.NEAREST)


def steve_front(px_per_unit: int) -> Image.Image:
    """Front-facing player figure, 16x32 texture pixels, scaled."""
    skin = mc_tex("entity/player/wide/steve.png")
    fig = Image.new("RGBA", (16, 32), (0, 0, 0, 0))
    fig.alpha_composite(skin.crop((8, 8, 16, 16)), (4, 0))        # head
    fig.alpha_composite(skin.crop((40, 8, 48, 16)), (4, 0))       # hat layer
    fig.alpha_composite(skin.crop((20, 20, 28, 32)), (4, 8))      # body
    fig.alpha_composite(skin.crop((44, 20, 48, 32)), (0, 8))      # right arm
    fig.alpha_composite(skin.crop((36, 52, 40, 64)), (12, 8))     # left arm
    fig.alpha_composite(skin.crop((4, 20, 8, 32)), (4, 20))       # right leg
    fig.alpha_composite(skin.crop((20, 52, 24, 64)), (8, 20))     # left leg
    return up(fig, px_per_unit)


def marker_icon(px: int, color=(80, 255, 230)) -> Image.Image:
    """A glowing diamond standing in for the (invisible) marker entity."""
    img = Image.new("RGBA", (px * 3, px * 3), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = px * 1.5, px * 1.5
    r = px * 0.45
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=color + (255,))
    glow = img.filter(ImageFilter.GaussianBlur(px * 0.35))
    glow = Image.merge("RGBA", glow.split()[:3] + (glow.split()[3].point(lambda v: int(v * 0.9)),))
    out = Image.alpha_composite(glow, img)
    d = ImageDraw.Draw(out)
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], outline=(255, 255, 255, 255), width=max(1, px // 12))
    return out


def background(kind: str = "blackstone") -> Image.Image:
    tile = up(block_tex(kind), 4)  # 64 px tiles
    bg = Image.new("RGBA", (W, H))
    for y in range(0, H, tile.height):
        for x in range(0, W, tile.width):
            bg.paste(tile, (x, y))
    bg = Image.alpha_composite(bg, Image.new("RGBA", (W, H), (0, 0, 0, 120)))
    small = Image.new("L", (64, 36), 0)
    px = small.load()
    for y in range(36):
        for x in range(64):
            dx, dy = (x + 0.5) / 64 - 0.5, (y + 0.5) / 36 - 0.5
            px[x, y] = int(min(1.0, (dx * dx + dy * dy) * 2.2) * 150)
    vign = small.resize((W, H), Image.BICUBIC)
    return Image.alpha_composite(bg, Image.merge("RGBA", (Image.new("L", (W, H), 0),) * 3 + (vign,)))


def save(img: Image.Image, out: Path) -> Path:
    """Save via a temp file; image viewers on Windows sometimes hold the target open."""
    import time
    tmp = out.with_suffix(".tmp.png")
    img.convert("RGB").save(tmp)
    for _ in range(10):
        try:
            os.replace(tmp, out)
            return out
        except OSError:
            time.sleep(0.5)
    raise


def drop(cover: Image.Image, img: Image.Image, x: int, y: int, sh: int = 10):
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 110))
    cover.paste(shadow, (x + sh, y + sh), img.split()[3])
    cover.alpha_composite(img, (x, y))


def arrow(d: ImageDraw.ImageDraw, p0, p1, color=(255, 255, 255, 255), width=6, head=18):
    d.line([p0, p1], fill=color, width=width)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for da in (math.radians(150), math.radians(-150)):
        q = (p1[0] + head * math.cos(ang + da), p1[1] + head * math.sin(ang + da))
        d.line([p1, q], fill=color, width=width)


def label(img: Image.Image, s: str, x: int, y: int, color=(255, 255, 255), scale=3, box=True):
    t = text(s, color=color, scale=scale)
    if box:
        pad = 8
        bx = Image.new("RGBA", (t.width + pad * 2, t.height + pad * 2), (0, 0, 0, 150))
        img.alpha_composite(bx, (x - pad, y - pad))
    img.alpha_composite(t, (x, y))
    return t


# ----------------------------------------------------------------------- images
def generator_scene(s: int, ox: float, oy: float, converted: int = 5, with_lava=True) -> Image.Image:
    """Row of five generator cells along +x: soul soil, product, blue ice; lava at the far end."""
    sc = Iso(s, ox, oy)
    for x in range(0, 8):
        for z in range(0, 2):
            sc.add(x, -1, z, "netherrack")
    for x in range(1, 6):
        sc.add(x, 0, 0, "soul_soil")
        sc.add(x, 1, 0, "blackstone" if x <= converted else "basalt_top", "blackstone" if x <= converted else "basalt_side")
        sc.add(x, 2, 0, "blue_ice")
    if with_lava:
        sc.add(6, 0, 0, "netherrack")
        sc.add(6, 1, 0, "lava_still", "lava_still", height=0.85)
        sc.add(6, 0, 1, "netherrack")
        sc.add(6, 1, 1, "netherrack")
        sc.add(7, 1, 0, "netherrack")
        sc.add(7, 0, 0, "netherrack")
    return sc.draw().crop(sc.draw().getbbox())


def make_cover() -> Path:
    cover = background("blackstone")
    scene = generator_scene(s=64, ox=640, oy=120, converted=3)
    drop(cover, scene, W - scene.width - 50, 150, 14)

    title = text("Blackstone Generator", color=(255, 255, 255), scale=8, shadow=(60, 60, 70))
    sub = text("Turn a basalt generator", color=(200, 230, 255), scale=4)
    sub2 = text("into a blackstone farm", color=(200, 230, 255), scale=4)
    ver = text("Minecraft 26.3 data pack", color=(170, 255, 170), scale=3)
    cover.alpha_composite(title, (50, 40))
    y = 40 + title.height + 30
    cover.alpha_composite(sub, (56, y))
    cover.alpha_composite(sub2, (56, y + sub.height + 4))
    cover.alpha_composite(ver, (56, y + sub.height * 2 + 24))

    # basalt -> blackstone strip, bottom left
    y = 520
    cover.alpha_composite(up(block_tex("basalt_side"), 6), (60, y))
    arr = Image.new("RGBA", (120, 96), (0, 0, 0, 0))
    arrow(ImageDraw.Draw(arr), (10, 48), (110, 48), width=8, head=24)
    cover.alpha_composite(arr, (166, y))
    cover.alpha_composite(up(block_tex("blackstone"), 6), (296, y))
    cover.alpha_composite(text("every tick, five blocks each way,", color=(220, 220, 220), scale=3), (60, y + 110))
    cover.alpha_composite(text("with or without you standing there", color=(220, 220, 220), scale=3), (60, y + 144))

    OUT.mkdir(exist_ok=True)
    out = OUT / "cover.png"
    return save(cover, out)


def side_view(px: int, converted: int, standin: str) -> Image.Image:
    """Cross-section: x = block columns (0 = player/marker, 1..5 generator, 6 lava), y up.

    Returns an image with the ground line at the bottom.
    """
    cols = 8
    rows = 4  # y = 0 (feet level) .. 3
    img = Image.new("RGBA", (cols * px, (rows + 1) * px), (0, 0, 0, 0))

    def put(x: int, y: int, name: str):
        img.alpha_composite(cube_face(name, px), (x * px, (rows - 1 - y) * px))

    for x in range(cols):
        put(x, -1, "netherrack")
    for x in range(1, 6):
        put(x, 0, "soul_soil")
        put(x, 1, "blackstone" if x <= converted else "basalt_side")
        put(x, 2, "blue_ice")
    put(6, 0, "netherrack")
    lava = cube_face("lava_still", px).crop((0, 0, px, int(px * 0.85)))
    img.alpha_composite(lava, (6 * px, (rows - 2) * px + int(px * 0.15)))
    put(7, 0, "netherrack")
    put(7, 1, "netherrack")
    # thin lava tongue flowing into the gap that is not yet basalt
    if converted < 5:
        tongue = cube_face("lava_still", px).crop((0, 0, px, int(px * 0.4)))
        for x in range(converted + 1, 6):
            pass  # gap already holds basalt in the diagram; keep it simple
    if standin == "player":
        fig = steve_front(px // 16)
        img.alpha_composite(fig, (0, (rows - 1) * px - fig.height + px))
    elif standin == "marker":
        m = marker_icon(px // 2)
        img.alpha_composite(m, (px // 2 - m.width // 2, (rows - 1) * px + px // 2 - m.height // 2))
    return img


def make_setup() -> Path:
    img = background("netherrack")
    px = 80
    view = side_view(px, converted=3, standin="player")
    vx, vy = 120, 210
    drop(img, view, vx, vy, 12)
    d = ImageDraw.Draw(img)

    title = text("Setup", color=(255, 255, 255), scale=8, shadow=(60, 30, 30))
    img.alpha_composite(title, (60, 40))
    img.alpha_composite(text("side view of a basalt generator", color=(220, 220, 220), scale=4), (66, 40 + title.height + 6))
    label(img, "/function blackstone:config -> [Enable]", 66, 175, color=(255, 255, 160), scale=3)

    # rows: y=2 blue ice, y=1 product, y=0 soul soil (rows index: top row = y 3)
    row_y = lambda y: vy + (3 - y) * px + px // 2 - 14
    right = vx + 8 * px + 40
    for y, s, c in ((2, "Blue ice above", (150, 210, 255)), (1, "Basalt -> blackstone", (255, 220, 160)), (0, "Soul soil below", (200, 170, 140))):
        arrow(d, (right + 4, row_y(y) + 14), (vx + 6 * px + 4, row_y(y) + 14), width=4, head=14)
        label(img, s, right + 20, row_y(y), color=c, scale=3)

    # lava callout, above the lava column
    lx = vx + 6 * px + px // 2
    label(img, "Lava flows in", lx - 100, vy + 10, color=(255, 200, 120), scale=3)
    arrow(d, (lx, vy + 50), (lx, vy + 2 * px + 4), color=(255, 200, 120, 255), width=4, head=14)
    # player callout, above the player's head
    label(img, "Stand here, facing the row", 20, vy + px - 20, color=(170, 255, 170), scale=2)
    arrow(d, (vx + px // 2, vy + px + 16), (vx + px // 2, vy + 2 * px - 14), color=(170, 255, 170, 255), width=4, head=12)
    # distance bracket under the five cells
    by = vy + 5 * px + 30
    d.line([(vx + px, by), (vx + 6 * px, by)], fill=(255, 255, 255, 255), width=4)
    d.line([(vx + px, by - 12), (vx + px, by + 12)], fill=(255, 255, 255, 255), width=4)
    d.line([(vx + 6 * px, by - 12), (vx + 6 * px, by + 12)], fill=(255, 255, 255, 255), width=4)
    label(img, "up to 5 blocks, in any of the 4 directions", vx + px, by + 24, scale=3)

    out = OUT / "setup.png"
    return save(img, out)


def make_markers() -> Path:
    img = background("soul_soil")
    px = 80
    view = side_view(px, converted=5, standin="marker")
    vx, vy = 120, 210
    drop(img, view, vx, vy, 12)
    d = ImageDraw.Draw(img)

    title = text("Generator markers", color=(255, 255, 255), scale=8, shadow=(40, 60, 60))
    img.alpha_composite(title, (60, 40))
    img.alpha_composite(text("new in 2.0: it works while you are away", color=(220, 220, 220), scale=4), (66, 40 + title.height + 6))

    label(img, "Stand where you normally would,", 20, vy + px - 20, color=(120, 255, 235), scale=2)
    label(img, "then click [Mark here]", 20, vy + px + 14, color=(120, 255, 235), scale=2)
    arrow(d, (vx + px // 2, vy + px + 50), (vx + px // 2, vy + 3 * px + 10), color=(120, 255, 235, 255), width=4, head=12)

    # mock config panel on the right
    panel_x, panel_y = vx + 8 * px + 40, vy - 10
    lines = [
        ("Blackstone Generator by DJayFresh", (0, 170, 170)),
        ("Click here for help", (85, 255, 255)),
        ("", (255, 255, 255)),
        ("Status: [Enabled]", (255, 170, 0)),
        ("[Disable]", (255, 85, 85)),
        ("", (255, 255, 255)),
        ("Markers: 1 loaded", (255, 170, 0)),
        ("[Mark here] [Unmark]", (85, 255, 85)),
        ("", (255, 255, 255)),
        ("[Refresh]", (85, 255, 85)),
    ]
    ph = 16 + len(lines) * 24
    panel = Image.new("RGBA", (W - panel_x - 40, ph), (0, 0, 0, 150))
    img.alpha_composite(panel, (panel_x, panel_y))
    y = panel_y + 10
    for s, c in lines:
        if s:
            img.alpha_composite(text(s, color=c, scale=2), (panel_x + 12, y))
        y += 24
    label(img, "/function blackstone:config", panel_x, panel_y + ph + 16, color=(255, 255, 160), scale=2)

    label(img, "The marker scans the same 5 blocks a player would.", 60, H - 90, scale=3)
    label(img, "Keep the chunk loaded and walk away.", 60, H - 50, scale=3)

    out = OUT / "markers.png"
    return save(img, out)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("cover", "all"):
        print(make_cover())
    if what in ("setup", "all"):
        print(make_setup())
    if what in ("markers", "all"):
        print(make_markers())
