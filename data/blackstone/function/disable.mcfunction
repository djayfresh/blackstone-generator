# Desc: Config option for disabling converter
#
# Author: DJayFresh

scoreboard players set #b2b_e b2b_e 0

execute if score #b2b_e b2b_e matches 0 run tellraw @a {"text":"Blackstone Generator: disabled basalt to blackstone","color":"red"}
