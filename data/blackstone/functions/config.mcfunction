#Config

tellraw @s {"text":"\n\n\nBlackstone Generator by DJayFresh","color":"dark_aqua","italic":"true"}
tellraw @s {"text":"Click here for help\n","color":"aqua","underlined":"true","clickEvent":{"action":"run_command","value":"/function blackstone:options/help"},"hoverEvent":{"action":"show_text","value":"Get a user's manual"}}

execute if score #b2b_e b2b_e matches 0 run tellraw @s [{"text":""},{"text":"Status","color":"gold"}, {"text":": ["}, {"text":"Disabled", "color": "red"}, {"text":"]"}]
execute if score #b2b_e b2b_e matches 0 run tellraw @s [{"text":"["}, {"text":"Enable", "color": "green", "clickEvent":{"action":"run_command", "value":"/function blackstone:enable"},"hoverEvent":{"action":"show_text","value":"Enable blackstone generation"}}, {"text":"]"}]

execute if score #b2b_e b2b_e matches 1 run tellraw @s [{"text":""},{"text":"Status","color":"gold"}, {"text":": ["}, {"text":"Enabled", "color": "green"}, {"text":"]"}]
execute if score #b2b_e b2b_e matches 1 run tellraw @s [{"text":"["}, {"text":"Disable", "color": "red", "clickEvent":{"action":"run_command", "value":"/function blackstone:disable"},"hoverEvent":{"action":"show_text","value":"Disable blackstone generation"}}, {"text":"]"}]

tellraw @s [{"text":"\n"},{"text":"[Refresh] ","color":"green","clickEvent":{"action":"run_command","value":"/function blackstone:config"},"hoverEvent":{"action":"show_text","value":"Update screen to show changed values"}}]
