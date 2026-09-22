# Desc: Convert basalt into blackstone if part of a basalt generator (soul_soil & blue_ice)
#   Replace up to 5 blocks away from every player and from every generator marker
#   (see blackstone:mark). Markers keep working while the player is elsewhere,
#   as long as the chunk is loaded.
#
# Called by: blackstone:loop (only while enabled)
# Author: DJayFresh

execute as @a at @s run function blackstone:scan
execute as @e[type=minecraft:marker,tag=b2b_gen] at @s run function blackstone:scan
