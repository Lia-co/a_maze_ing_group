"""
This file includes wall operations like: 
- open/close a wall of a cell
- check if the wall exisists in a direction
- carve walls for adjecent cells 
"""

from . import direction as dir
from .maze import maze


def open_wall(cell: int, direction: int) -> int:
	"""The method opens the wall of a cell by making the bit mask as 0.
    e.g. if the west wall opened, the bit mask is: 1000, W=8
    1111(a closed cell) -> 0111(west wall)
    int: 15 -> int: 7"""
	new_cell: int = 0
	new_cell = cell - dir.DIR_BIT[direction]
	return new_cell

# def open_wall(cell: int, direction: str) -> int:
# 	new_cell = cell & ~direction
# 	return new_cell


def close_wall(cell: int, direction: int) -> int:
	"""The method closes the wall of a cell by making the bit mask as 1.
    e.g. if closing the west wall, according to direction's bit mask(1000), W=8
    0111(west wall is open) -> 1111(a closed cell)
    int: 7 -> int: 15"""
	new_cell: int = 0 #???do I need to initialize the variable? 
	new_cell = cell + dir.DIR_BIT[direction]
	return new_cell

# def open_wall(cell: int, direction: str) -> int:
# 	new_cell = cell | direction
# 	return new_cell


def check_wall(cell: int, direction: int) -> bool: #???need test later
	"""The method checks the wall of a cell by comparing if the bit mask as 1.
    e.g. if the west wall is closed, according to direction's bit mask(1000), W=8
    1000(west wall is open) v.s 1111(a closed cell)
    if the comparing direction both are 1, return True(1), else return False(0)"""
	if direction & cell == 1:
		return True
	return False


# ???why it is necessary to pass Maze as attribute?
def carve_walls(coord1: tuple[int, int], coord2: tuple[int, int]) -> None:
	"""The method removes the wall between two adjecent cells. The two cells' int are updated."""
	# check if cells are within the maze
	# check if cells are adjecent

	x1, y1 = coord1
	x2, y2 = coord2

	# initialize cell1 and cell2
	cell1 = maze.grid[y1][x1]
	cell2 = maze.grid[y2][x2]

	# check which direction's walls be removed
	direction = None
	if y2 == y1 - 1 and x2 == x1:
		direction = "N"
	elif y2 == y1 and x2 == x1 + 1:
		direction = "E"
	elif y2 == y1 + 1 and x2 == x1:
		direction = "S"
	elif y2 == y1 and x2 == x1 - 1:
		direction = "W"
	if direction is None:
		raise ValueError("Cells are within maze and adjecent, but direction is invalid.")

	# get the bit value of the wall
	# update cell1's value after removing cell1's wall
	# get the opposite wall's direction
	# get the bit value of the opposite wall
	# update cell2's value after removing cell2's wall
	wall_bit_val = dir.wall_bit(direction)
	cell1 = open_wall(cell1, wall_bit_val)
	ad_wall_direction = dir.adjecent_wall(wall_bit_val)
	ad_wall_bit_val = dir.wall_bit(ad_wall_direction)
	cell2 = open_wall(cell2, ad_wall_bit_val)

	# update new cell's bit value in maze without walls
	maze.grid[y1][x1] = cell1
	maze.grid[y2][x2] = cell2
