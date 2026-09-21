#!/usr/bin/env python3
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
#???maybe I can use enum to difine class

"""
Define four directions with final[], making variable impossible to redefine
"""
DIRECTIONS: Final[tuple[str, ...]] = ("N", "E", "S", "W")

"""
Bit masks wall's direction
"""
DIR_BIT: Final[dict[str, int]] = {
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

"""
Pass direction of wall and return its bit mask
"""
def wall_bit(direction: str) -> int:
	if not direction or direction not in DIR_BIT:
		raise ValueError(f"The {direction} is not valid, expect input: N/E/S/W")
	return DIR_BIT[direction]


"""
Pass curent wall direction and return the wall direction of adjecent cell
"""
def adjecent_wall(direction: str) -> str:
	if not direction or direction not in DIR_OPPOSITE:
		raise ValueError(f"The {direction} is not valid, expect input: N/E/S/W")
	return DIR_OPPOSITE[direction]

"""
Pass curent wall direction and return the tuple of adjecent cell
"""
def move_cell(direction: str) -> tuple:
	if not direction or direction not in DIR_MOVE:
		raise ValueError(f"The {direction} is not valid, expect input: N/E/S/W")
	return DIR_MOVE(direction)