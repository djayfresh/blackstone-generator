say one second

#execute at @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:wheat_seeds"}]}] if block ~ ~ ~ minecraft:farmland if block ~ ~1 ~ minecraft:wheat[age=7] run playsound minecraft:block.grass.break block @s ~ ~ ~ 1

#Facing South
execute as @a at @s if block ~ ~1 ~1 minecraft:basalt if block ~ ~ ~1 minecraft:soul_soil if block ~ ~2 ~1 minecraft:blue_ice run setblock ~ ~1 ~1 minecraft:blackstone replace


#Facing North
execute as @a at @s if block ~ ~1 ~-1 minecraft:basalt if block ~ ~ ~-1 minecraft:soul_soil if block ~ ~2 ~-1 minecraft:blue_ice run setblock ~ ~1 ~-1 minecraft:blackstone replace

#Facing West
execute as @a at @s if block ~1 ~1 ~ minecraft:basalt if block ~1 ~ ~ minecraft:soul_soil if block ~1 ~2 ~ minecraft:blue_ice run setblock ~1 ~1 ~ minecraft:blackstone replace


#Facing East
execute as @a at @s if block ~-1 ~1 ~ minecraft:basalt if block ~-1 ~ ~ minecraft:soul_soil if block ~-1 ~2 ~ minecraft:blue_ice run setblock ~-1 ~1 ~ minecraft:blackstone replace

