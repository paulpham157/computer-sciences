# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

TILE_SIZE = 12
WALL_LENGTH = 500

# Put a black tile
length = WALL_LENGTH - TILE_SIZE
num_pairs = length // (TILE_SIZE * 2)
gap = length % (TILE_SIZE * 2)

print(f"The gap at each side is: {gap/2}cm AND I need to use {1+num_pairs*2} tiles.")
