# Blackstone Generator

A vanilla Minecraft data pack (Minecraft 26.3, pack_format 121) that turns a basalt generator into a
blackstone farm: basalt that forms between soul soil and blue ice is converted to blackstone, up to
five blocks away from a player or a generator marker, in any of the four horizontal directions.

Published on [Planet Minecraft](https://www.planetminecraft.com/data-pack/blackstone-generator/).
Releases on [GitHub](https://github.com/djayfresh/blackstone-generator/releases).

## Using it

1. Drop the zip (or the pack folder) into `world/datapacks/`, then `/reload`.
2. Run `/function blackstone:config` for the in-chat control panel: enable, disable, markers, refresh, and a help book.
3. Stand in front of the line of basalt from your generator. While enabled, basalt with soul soil below
   and blue ice above becomes blackstone every tick.
4. To keep it running while you are away, stand where you would normally stand and click **Mark here**
   (`/function blackstone:mark`). The marker scans the same blocks a player would, as long as the chunk is
   loaded. **Unmark** (`/function blackstone:unmark`) removes markers within 8 blocks.

The pack also replaces `minecraft:gameplay/piglin_bartering` with a copy of the vanilla 26.3 table plus a
basalt trade. Vanilla has no way to append to a loot table, so this conflicts with other packs that change
bartering.

## Layout

- `data/main/`: a tiny scheduler. `main:tick` fires the `#main:loop` tag every tick; `#main:init`
  runs on load. Meant to be shared between packs.
- `data/blackstone/function/`: `init`, `loop`, `convert` -> `scan` -> `try_convert`, `mark`, `unmark`,
  `enable`, `disable`, `config`, `options/help`.
- `data/blackstone/predicate/`: `blue_ice_above`, `soul_soil_below`, used by `try_convert`.
- `data/minecraft/`: `load`/`tick` tags and the bartering loot table.
- `images/`: the screenshots used on the Planet Minecraft page.
- `tools/build.py`: builds `out/blackstone-generator-<version>-mc<mc>.zip` and `pack.png` (version from the `version` file).
- `tools/rcon.py`: RCON client for the local test server (`run/`, gitignored; see `PLAN.md` for the test layout).

## Development

```
python tools/build.py                      # zip into out/
python tools/rcon.py "reload" "function blackstone:config"   # against the run/ server (RCON_PASSWORD=blackstone-dev)
```

## History

Split out of the `minecraft-packs` repo (2020-09-08 to 2020-09-09 commits) on 2026-09-22 with
`git subtree split`, history preserved. `v1.0-mc1.16` is the original 1.16 pack; `v2.0-mc26.3` is the
26.3 port with markers. See `CHANGELOG.md`.
