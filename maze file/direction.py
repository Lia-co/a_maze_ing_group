"""
This file defines:
- directions: N, E, S, W
- bit masks for a cell's open/close walls situation
- neighbor cell's opposite wall
- movement in 4 directions

A cell's default situation includes 4 walls in 4 directions: north, east,
south, west. if 1 represent the wall, and 0 represents opened wall, a
cell's situatoin can be wrote as 0000(totally opened cell) or 1111(totally
closed cell). Starts from right, an north-open cell will be 0001, then we
have this table:
d   bit hex
N: 0001 1
E: 0010 2
S: 0100 4
W: 1000 8

Therefore, it is ideal to use hexdecimal number to represent a cell's walls
opening or not.
"""

from typing import Final

"""
Define four directions with final[], making variable impossible to redefine
"""
DIRECTIONS: Final[tuple[str, ...]] = ("N", "E", "S", "W")

"""
Bit masks wall's direction
"""
DIR_BIT_VAL: Final[dict[str, int]] = {
    "N": 1,
    "E": 2,
    "S": 4,
    "W": 8
}


"""
Define the opposite directions of neighbor cell
"""
DIR_OPPOSITE: Final[dict[str, str]] = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E"
}


"""
Define 4 directions of movement
"""
DIR_MOVE: Final[dict[str, tuple[int, int]]] = {
    "N": (0, -1),
    "E": (+1, 0),
    "S": (0, +1),
    "W": (-1, 0)
}
