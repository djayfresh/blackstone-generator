# Changelog

## 2.0 (2026-09-22) - Minecraft 26.3

- Ported to the 26.3 data pack format (pack_format 121): singular folder names, `type`-based predicates, `click_event`/`hover_event` text components, the help book as a `written_book_content` item component.
- Generator markers: click **Mark here** in `/function blackstone:config` (or run `/function blackstone:mark`) where you would normally stand and the generator keeps converting while you are away, as long as the chunk is loaded. **Unmark** removes markers within 8 blocks. Standing in front of the generator still works exactly as before.
- Conversion now uses the `soul_soil_below` and `blue_ice_above` predicates through `blackstone:scan` and `blackstone:try_convert` instead of 20 hard-coded block checks.
- Piglin bartering re-copied from the 26.3 vanilla table (which now includes blackstone and dried ghast) with the basalt trade appended. Vanilla still offers no way to add to a loot table without replacing it, so any other pack that changes bartering will conflict.
- Enable/disable announce in chat with `tellraw` instead of `say`.
- The tick scheduler fires every tick directly; the unused tick counter is gone.
- Verified on a 26.3 dedicated server: `/reload` with no errors, lava flowing between soul soil and blue ice becomes basalt then blackstone from a marker, basalt without blue ice above is left alone, disabling stops conversion, bartering rolls include basalt.

## 1.0 (2020-09-09) - Minecraft 1.16

- Original release, tagged `v1.0-mc1.16`. Published on Planet Minecraft.
