# Desc: In-chat control panel
#
# Author: DJayFresh

execute store result score #b2b_markers b2b_e if entity @e[type=minecraft:marker,tag=b2b_gen]

tellraw @s {"text":"\n\n\nBlackstone Generator by DJayFresh","color":"dark_aqua","italic":true}
tellraw @s {"text":"Click here for help\n","color":"aqua","underlined":true,"click_event":{"action":"run_command","command":"/function blackstone:options/help"},"hover_event":{"action":"show_text","value":"Get a user's manual"}}

execute unless score #b2b_e b2b_e matches 1 run tellraw @s [{"text":""},{"text":"Status","color":"gold"},{"text":": ["},{"text":"Disabled","color":"red"},{"text":"]"}]
execute unless score #b2b_e b2b_e matches 1 run tellraw @s [{"text":"["},{"text":"Enable","color":"green","click_event":{"action":"run_command","command":"/function blackstone:enable"},"hover_event":{"action":"show_text","value":"Enable blackstone generation"}},{"text":"]"}]

execute if score #b2b_e b2b_e matches 1 run tellraw @s [{"text":""},{"text":"Status","color":"gold"},{"text":": ["},{"text":"Enabled","color":"green"},{"text":"]"}]
execute if score #b2b_e b2b_e matches 1 run tellraw @s [{"text":"["},{"text":"Disable","color":"red","click_event":{"action":"run_command","command":"/function blackstone:disable"},"hover_event":{"action":"show_text","value":"Disable blackstone generation"}},{"text":"]"}]

tellraw @s [{"text":"\n"},{"text":"Markers","color":"gold"},{"text":": "},{"score":{"name":"#b2b_markers","objective":"b2b_e"},"color":"yellow"},{"text":" loaded"}]
tellraw @s [{"text":"["},{"text":"Mark here","color":"green","click_event":{"action":"run_command","command":"/function blackstone:mark"},"hover_event":{"action":"show_text","value":"Place a marker at your feet so the generator works without you"}},{"text":"] ["},{"text":"Unmark","color":"red","click_event":{"action":"run_command","command":"/function blackstone:unmark"},"hover_event":{"action":"show_text","value":"Remove markers within 8 blocks"}},{"text":"]"}]

tellraw @s [{"text":"\n"},{"text":"[Refresh] ","color":"green","click_event":{"action":"run_command","command":"/function blackstone:config"},"hover_event":{"action":"show_text","value":"Update screen to show changed values"}}]
