"""
This file includes wall operations like: 
- open/close a wall of a cell
- check if the wall exisists in a direction
- carve walls for adjecent cells 
"""

from .direction import DIR_BIT

"""
The method open the wall of a cell by making the bit mask as 0.
e.g. if openning the west wall, according to direction's bit mask(1000), W=8
1111(a closed cell) -> 0111(west wall)
int: 15 -> int: 7
"""
def open_wall(cell: int, direction: str) -> int:
	new_cell: int = 0
	new_cell = cell - DIR_BIT[direction]
	return new_cell

# def open_wall(cell: int, direction: str) -> int:
# 	new_cell = cell & ~direction
# 	return new_cell

"""
The method open the wall of a cell by making the bit mask as 1.
e.g. if closing the west wall, according to direction's bit mask(1000), W=8
0111(west wall is open) -> 1111(a closed cell)
int: 7 -> int: 15
"""
def close_wall(cell: int, direction: str) -> int:
	new_cell: int = 0 #???do I need to initialize the variable? 
	new_cell = cell + DIR_BIT[direction]
	return new_cell

# def open_wall(cell: int, direction: str) -> int:
# 	new_cell = cell | direction
# 	return new_cell


def check_wall(cell: int, direction: str) -> bool:




def carve_walls()