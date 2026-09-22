# Desc: Place a generator marker at the caller's block. The marker scans the same
#   5 blocks in each direction that a player would, so the generator keeps
#   producing blackstone while nobody stands in front of it.
#
# Author: DJayFresh

execute align xyz positioned ~0.5 ~ ~0.5 unless entity @e[type=minecraft:marker,tag=b2b_gen,distance=..0.1] run summon minecraft:marker ~ ~ ~ {Tags:["b2b_gen"]}
tellraw @s {"text":"Generator marker placed at your feet","color":"green"}
execute store result score #b2b_markers b2b_e if entity @e[type=minecraft:marker,tag=b2b_gen]
tellraw @s [{"text":"Markers loaded: ","color":"gray"},{"score":{"name":"#b2b_markers","objective":"b2b_e"},"color":"yellow"}]
