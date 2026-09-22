# Desc: Remove generator markers within 8 blocks of the caller.
#
# Author: DJayFresh

execute unless entity @e[type=minecraft:marker,tag=b2b_gen,distance=..8] run tellraw @s {"text":"No generator marker within 8 blocks","color":"red"}
execute if entity @e[type=minecraft:marker,tag=b2b_gen,distance=..8] run tellraw @s {"text":"Removed generator marker(s) within 8 blocks","color":"green"}
kill @e[type=minecraft:marker,tag=b2b_gen,distance=..8]
