# Blackstone Generator modernization plan

## Findings (2026-09-22)
- Repo: vanilla data pack written for 1.16 (pack_format 6), split out of `minecraft-packs` with history. Published on Planet Minecraft in September 2020 (592 downloads, listed for 1.16 - 1.17).
- Conversion was player-relative: 20 hard-coded `execute as @a at @s if block ...` lines, five blocks in each direction. Two predicates existed but were unused.
- Piglin bartering was a full copy of the 1.16 vanilla table plus a basalt trade.
- What changed by 26.3 (verified against the 26.3 server jar in the NeoForm cache and on a dedicated server):
  - Data folders are singular: `function/`, `tags/function/`, `loot_table/`, `predicate/`.
  - `version.json` says data pack version 121.0; `pack.mcmeta` takes `pack_format` plus `min_format`/`max_format`.
  - Predicates use `"type"` (not `"condition"`) and block predicates use `"blocks"`.
  - Loot table entries use `"modifier": {"type": ...}` instead of `"functions": [...]`; the vanilla bartering table now includes blackstone and dried ghast and carries `random_sequence`. There is still no way to append to a vanilla loot table from a data pack.
  - Text components use `click_event.command` and `hover_event.value`; booleans must be real booleans.
  - Written books are `written_book[written_book_content={title,author,pages:[...]}]`; pages can be plain strings.
  - `gamerule` has no basalt/blackstone rule, so the pack is still the way to get this behaviour. `marker` entities replace the old invisible armour stand trick for player-independent positions.

## Phase 1: Housekeeping  — DONE 2026-09-22
- GitHub repo `djayfresh/blackstone-generator` (public), `master` pushed, tag `v1.0-mc1.16` on the original state.

## Phase 2: Port to 26.3  — DONE 2026-09-22
- Folder renames, `pack_format` 121, predicates fixed and moved to the `blackstone` namespace, bartering table re-copied from 26.3 with basalt appended, tellraw and book rewritten, tick scheduler simplified.
- Verified on a vanilla 26.3 dedicated server (`run/`, gitignored) over RCON (`tools/rcon.py`, password `blackstone-dev`): `/reload` clean, every function parses.

## Phase 3: Predicates and markers  — DONE 2026-09-22
- `blackstone:convert` runs `blackstone:scan` as every player and every `marker` tagged `b2b_gen`; `scan` positions at each of the 20 candidate blocks and calls `blackstone:try_convert`, which checks basalt plus the two predicates.
- `blackstone:mark` / `blackstone:unmark` manage markers; the config panel shows the loaded marker count and has Mark here / Unmark buttons.
- Player-relative conversion stays on by default; markers are additive.

## Phase 4: Verification  — DONE 2026-09-22
RCON on a superflat world, chunk `100 100` force loaded, `pause-when-empty-seconds=0`:
- Soul soil at y=-60, air gap at y=-59, blue ice at y=-58 for x=101..105; lava source at x=106 walled in. Lava flowed into the gap, became basalt, and the marker at `100 -60 100` converted it to blackstone.
- With the pack enabled and no player or marker present, basalt stayed basalt (proves the marker is what drives it).
- Basalt with the blue ice removed above it stayed basalt; putting the ice back converted it.
- `blackstone:disable`, refill with basalt: still basalt after two seconds.
- 100 `loot spawn` rolls of the bartering table dropped both basalt and blackstone.

## Phase 5: Release  — DONE 2026-09-22
- `tools/build.py` writes `out/blackstone-generator-2.0-mc26.3.zip` and `pack.png`; `version` file holds "2.0 26.3".
- Tag `v2.0-mc26.3`, GitHub release with the zip, `CHANGELOG.md`, `mod.description.md` for the Planet Minecraft page update.

## Open ideas
- Blue ice on the side (the 2020 "planned improvements" item): a second pair of predicates and a config toggle.
- Tick rate option: `blackstone:loop` could run every N ticks via a score, as the original scheduler half-implemented.
- Bartering conflict: if a future version lets packs extend loot tables, drop the full-table override.
