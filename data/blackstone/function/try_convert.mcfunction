# Desc: Convert the block at the execution position from basalt to blackstone
#   if it sits between soul soil (below) and blue ice (above), i.e. it was
#   made by a basalt generator.
#
# Called by: blackstone:scan (positioned at each candidate block)
# Author: DJayFresh

execute if block ~ ~ ~ minecraft:basalt if predicate blackstone:soul_soil_below if predicate blackstone:blue_ice_above run setblock ~ ~ ~ minecraft:blackstone replace
