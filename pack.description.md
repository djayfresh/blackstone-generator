Added in one change to the base game that I think is valid, but not well executed. 

1.16: added Basalt generation, blue ice above a gap with soul_soil underneath. When lava spreads between the two blocks its converted into basalt. 

I think basalt was the wrong thing to generate, it should have been blackstone. Blackstone at first was not renewable (some snapshot). But later was added to the Piglin bartering system at an okay rate. 

However, I still felt the generation was broken. So, I created my own data pack to handle this. Piglin bartering has been updated to drop basalt instead of blackstone. When a player stands in front of the generated basalt, it will be converted into black stone. 

Basalt is only converted to blackstone after the pack is added, and then enabled (see below). While basalt can be generated from blue ice on the side, for now it requires: 
1. Blue ice is above the basalt
2. Soul Soil is below the basalt
3. Up to five blocks from the player

With that in mind, a normal basalt generation (that drops basalt only) can be achieved by moving the blue ice to the side, instead of on top.


[hr]

How to Use:


[list=1]
[*]Enable the pack (below)[/*]
[*]Stand in front of the basalt generator (pictured)[/*]
[*]Basalt will be converted into blackstone[/*]
[*]Mine & Repeat[/*]
[/list]



Enabling:

The pack has a function to handle configuration:
[code]/function blackstone:config[/code]

Alternatively you can just run:
[code]/function blackstone:enable[/code]
This is my first pack so feedback is appreciated, and welcome! 



[hr]


Planned improvements:
[list]
[*]Blue Ice config (top, side) for converting[/*]
[*]Tick rate (performance)[/*]
[*]Better help book ;)
[/*]
[/list]Inspired by the work of [url=/data-pack/basalt-without-silk-touch-drops-blackstone/]Leyxcx[/url]