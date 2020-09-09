# Desc: called from minecraft#tick every tick
# Author: DJayFresh

scoreboard players add #djf_tick djf_tick 1

execute if score #djf_tick djf_tick matches 1 run function #main:loop
#execute if score #djf_tick djf_tick matches 21 run function #main:loop
#execute if score #djf_tick djf_tick matches 41 run function #main:loop
#execute if score #djf_tick djf_tick matches 61 run function #main:loop
#execute if score #djf_tick djf_tick matches 81 run function #main:loop

# Run every tick
# default #100
execute if score #djf_tick djf_tick matches 1.. run scoreboard players set #djf_tick djf_tick 0