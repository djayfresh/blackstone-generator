# Desc: Convert basalt into blackstone if part of a basalt generator (soul_soil & blue_ice)
#   Replace up to 5 blocks away
#
# Author: DJayFresh

#Facing South
execute as @a at @s if block ~ ~1 ~1 minecraft:basalt if block ~ ~ ~1 minecraft:soul_soil if block ~ ~2 ~1 minecraft:blue_ice run setblock ~ ~1 ~1 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~2 minecraft:basalt if block ~ ~ ~2 minecraft:soul_soil if block ~ ~2 ~2 minecraft:blue_ice run setblock ~ ~1 ~2 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~3 minecraft:basalt if block ~ ~ ~3 minecraft:soul_soil if block ~ ~2 ~3 minecraft:blue_ice run setblock ~ ~1 ~3 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~4 minecraft:basalt if block ~ ~ ~4 minecraft:soul_soil if block ~ ~2 ~4 minecraft:blue_ice run setblock ~ ~1 ~4 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~5 minecraft:basalt if block ~ ~ ~5 minecraft:soul_soil if block ~ ~2 ~5 minecraft:blue_ice run setblock ~ ~1 ~5 minecraft:blackstone replace

#Facing North
execute as @a at @s if block ~ ~1 ~-1 minecraft:basalt if block ~ ~ ~-1 minecraft:soul_soil if block ~ ~2 ~-1 minecraft:blue_ice run setblock ~ ~1 ~-1 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~-2 minecraft:basalt if block ~ ~ ~-2 minecraft:soul_soil if block ~ ~2 ~-2 minecraft:blue_ice run setblock ~ ~1 ~-2 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~-3 minecraft:basalt if block ~ ~ ~-3 minecraft:soul_soil if block ~ ~2 ~-3 minecraft:blue_ice run setblock ~ ~1 ~-3 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~-4 minecraft:basalt if block ~ ~ ~-4 minecraft:soul_soil if block ~ ~2 ~-4 minecraft:blue_ice run setblock ~ ~1 ~-4 minecraft:blackstone replace
execute as @a at @s if block ~ ~1 ~-5 minecraft:basalt if block ~ ~ ~-5 minecraft:soul_soil if block ~ ~2 ~-5 minecraft:blue_ice run setblock ~ ~1 ~-5 minecraft:blackstone replace

#Facing West
execute as @a at @s if block ~1 ~1 ~ minecraft:basalt if block ~1 ~ ~ minecraft:soul_soil if block ~1 ~2 ~ minecraft:blue_ice run setblock ~1 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~2 ~1 ~ minecraft:basalt if block ~2 ~ ~ minecraft:soul_soil if block ~2 ~2 ~ minecraft:blue_ice run setblock ~2 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~3 ~1 ~ minecraft:basalt if block ~3 ~ ~ minecraft:soul_soil if block ~3 ~2 ~ minecraft:blue_ice run setblock ~3 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~4 ~1 ~ minecraft:basalt if block ~4 ~ ~ minecraft:soul_soil if block ~4 ~2 ~ minecraft:blue_ice run setblock ~4 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~5 ~1 ~ minecraft:basalt if block ~5 ~ ~ minecraft:soul_soil if block ~5 ~2 ~ minecraft:blue_ice run setblock ~5 ~1 ~ minecraft:blackstone replace

#Facing East
execute as @a at @s if block ~-1 ~1 ~ minecraft:basalt if block ~-1 ~ ~ minecraft:soul_soil if block ~-1 ~2 ~ minecraft:blue_ice run setblock ~-1 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~-2 ~1 ~ minecraft:basalt if block ~-2 ~ ~ minecraft:soul_soil if block ~-2 ~2 ~ minecraft:blue_ice run setblock ~-2 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~-3 ~1 ~ minecraft:basalt if block ~-3 ~ ~ minecraft:soul_soil if block ~-3 ~2 ~ minecraft:blue_ice run setblock ~-3 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~-4 ~1 ~ minecraft:basalt if block ~-4 ~ ~ minecraft:soul_soil if block ~-4 ~2 ~ minecraft:blue_ice run setblock ~-4 ~1 ~ minecraft:blackstone replace
execute as @a at @s if block ~-5 ~1 ~ minecraft:basalt if block ~-5 ~ ~ minecraft:soul_soil if block ~-5 ~2 ~ minecraft:blue_ice run setblock ~-5 ~1 ~ minecraft:blackstone replace