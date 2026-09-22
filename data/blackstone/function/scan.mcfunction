# Desc: Check the five blocks in each horizontal direction, one block above
#   the executor's feet, and convert generator basalt to blackstone.
#
# Called by: blackstone:convert (as each player and each generator marker)
# Author: DJayFresh

# South (+z)
execute positioned ~ ~1 ~1 run function blackstone:try_convert
execute positioned ~ ~1 ~2 run function blackstone:try_convert
execute positioned ~ ~1 ~3 run function blackstone:try_convert
execute positioned ~ ~1 ~4 run function blackstone:try_convert
execute positioned ~ ~1 ~5 run function blackstone:try_convert

# North (-z)
execute positioned ~ ~1 ~-1 run function blackstone:try_convert
execute positioned ~ ~1 ~-2 run function blackstone:try_convert
execute positioned ~ ~1 ~-3 run function blackstone:try_convert
execute positioned ~ ~1 ~-4 run function blackstone:try_convert
execute positioned ~ ~1 ~-5 run function blackstone:try_convert

# East (+x)
execute positioned ~1 ~1 ~ run function blackstone:try_convert
execute positioned ~2 ~1 ~ run function blackstone:try_convert
execute positioned ~3 ~1 ~ run function blackstone:try_convert
execute positioned ~4 ~1 ~ run function blackstone:try_convert
execute positioned ~5 ~1 ~ run function blackstone:try_convert

# West (-x)
execute positioned ~-1 ~1 ~ run function blackstone:try_convert
execute positioned ~-2 ~1 ~ run function blackstone:try_convert
execute positioned ~-3 ~1 ~ run function blackstone:try_convert
execute positioned ~-4 ~1 ~ run function blackstone:try_convert
execute positioned ~-5 ~1 ~ run function blackstone:try_convert
