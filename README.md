# Blackstone Generator

A vanilla Minecraft data pack (written for 1.16, pack_format 6) that turns a basalt generator into a
blackstone farm: basalt that forms between soul soil and blue ice is converted to blackstone, up to
five blocks away from the player, in any of the four horizontal directions.

Published on [Planet Minecraft](https://www.planetminecraft.com/data-pack/blackstone-generator/).

## Using it

1. Drop the pack folder (or a zip of it) into `world/datapacks/`, then `/reload`.
2. Run `/function blackstone:config` for the in-chat control panel: enable, disable, refresh, and a help book.
3. Stand in front of the line of basalt from your generator. While enabled, basalt with soul soil below
   and blue ice above becomes blackstone every tick.

The pack also replaces `minecraft:gameplay/piglin_bartering` with a copy of the vanilla 1.16 table
plus a basalt trade.

## Layout

- `data/main/`: a tiny scheduler. `main:tick` counts ticks and fires the `#main:loop` tag; `#main:init`
  creates the scoreboards. Meant to be shared between packs.
- `data/blackstone/functions/`: `init`, `loop`, `convert`, `enable`, `disable`, `config`, `options/help`.
- `data/minecraft/`: `load`/`tick` tags, the bartering loot table, and two predicates
  (`blue_ice_above`, `soul_soil_below`) that the current `convert` function does not use yet.
- `images/`: the screenshots used on the Planet Minecraft page.

## History

Split out of the `minecraft-packs` repo (2020-09-08 to 2020-09-09 commits) on 2026-09-22 with
`git subtree split`, history preserved.
