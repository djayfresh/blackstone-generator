# Desc: Config option for enabling converter
#
# Author: DJayFresh

scoreboard players set #b2b_e b2b_e 1

execute if score #b2b_e b2b_e matches 1 run tellraw @a {"text":"Blackstone Generator: enabled basalt to blackstone","color":"green"}
