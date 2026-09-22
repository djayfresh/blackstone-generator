# Blackstone Generator - store description

Source of truth for the text on the Planet Minecraft page (https://www.planetminecraft.com/data-pack/blackstone-generator/). Update this file with each release, then copy it over. The original 2020 text is kept in `pack.description.md`. Planet Minecraft uses BBCode, so the section below is written in it.

## Page settings

- Minecraft version: 26.3 (was 1.16 - 1.17)
- Tags: Adventure, Afk, Basalt, Blackstone, Farming, Functions, Game Mechanic, Generator, Loot Tables, Predicates, Markers
- Images (1280x720, built by `python tools/release_art.py` from vanilla 26.3 textures): `images/cover.png` (cover), `images/setup.png` (generator layout, where to stand, enable command), `images/markers.png` (markers and the config panel). The 2020 screenshots `images/Blackstone_Generator*.png` can stay as extra gallery images.

## Description (BBCode)

Turn your basalt generator into a blackstone farm.

Since 1.16, lava that flows between blue ice (above) and soul soil (below) sets into basalt. I always thought that should have been blackstone. This data pack makes it so: while it is enabled, basalt that forms between soul soil and blue ice is converted into blackstone. Piglins also barter basalt instead of blackstone, so both stay renewable.

[b]Updated for Minecraft 26.3.[/b] The pack now works without you standing in front of it: place a marker and walk away.

[hr]

[b]How to use[/b]

[list=1]
[*]Drop the zip into your world's [code]datapacks[/code] folder and run [code]/reload[/code].[/*]
[*]Open the control panel: [code]/function blackstone:config[/code] and click [b]Enable[/b].[/*]
[*]Stand in front of the basalt generator (up to five blocks away, in any of the four directions). Basalt becomes blackstone every tick.[/*]
[*]Want it to run while you are elsewhere? Stand where you would normally stand and click [b]Mark here[/b]. The marker does the standing for you as long as the chunk is loaded. [b]Unmark[/b] removes markers within 8 blocks.[/*]
[*]Mine and repeat.[/*]
[/list]

Shortcuts: [code]/function blackstone:enable[/code], [code]/function blackstone:disable[/code], [code]/function blackstone:mark[/code], [code]/function blackstone:unmark[/code]. The help book is under [b]Click here for help[/b] in the config.

Only basalt with blue ice directly above and soul soil directly below is converted, so a generator with the blue ice on the side keeps making plain basalt.

[hr]

[b]Changelog[/b]

[b]2.0[/b] (26.3) - Ported to the 26.3 data pack format. Generator markers so the farm runs without you. Conversion uses predicates. Piglin bartering re-copied from 26.3 vanilla with the basalt trade added. Chat messages instead of /say.

[b]1.0[/b] (1.16) - Original release.

[hr]

Source and issues: [url=https://github.com/djayfresh/blackstone-generator]github.com/djayfresh/blackstone-generator[/url]

Inspired by the work of [url=/data-pack/basalt-without-silk-touch-drops-blackstone/]Leyxcx[/url].

## Downloads

- GitHub releases: https://github.com/djayfresh/blackstone-generator/releases
- Current: 2.0 - https://github.com/djayfresh/blackstone-generator/releases/tag/v2.0-mc26.3
