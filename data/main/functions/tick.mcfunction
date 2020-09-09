# gets called ever ticket
# shouldn't be used for anything but modifying scoreboard

scoreboard players add #djf_tick djf_tick 1

# every tick
function #main:tick

# Every 1 second
execute if score #djf_tick djf_tick matches 1 run function #main:second
execute if score #djf_tick djf_tick matches 21 run function #main:second
execute if score #djf_tick djf_tick matches 41 run function #main:second
execute if score #djf_tick djf_tick matches 61 run function #main:second
execute if score #djf_tick djf_tick matches 81 run function #main:second

execute if score #djf_tick djf_tick matches 100.. run scoreboard players set #djf_tick djf_tick 0