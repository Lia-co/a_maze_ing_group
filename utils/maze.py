"""
This file defines a maze class and validate coordinates.
"""

# from typing import List
"""
The initialized maze is a grid of cells with entry and exit, each cell has an int to represent walls' condition.
The cell's default condition is a closed cell(int: 15)
The maze class includes 4 values:
- width
- height
- entry
- exit

The validation will check again:
- if width and height are valid
- if entry is equal to exit
- if entry and exit are within the maze
"""
class maze:
	def __init__(self, width: int, height: int, entry: tuple[int, int], exit: tuple[int, int]) -> None:
		self.width = width
		self.height = height
		self.entry = entry
		self.exit = exit

		# validate width and height
		if width <= 0:
			raise ValueError("WIDTH is invalid, expect inpur are postive digits")
		if height <= 0:
			raise ValueError("HEIGHT is invalid, expect inpur are postive digits")
		# check if entry is equal to exit
		if entry == exit:
			raise ValueError("ENTRY and EXIT are the same, invalid input.")
		# check if entry and exit are within the maze
		x1, y1 = entry
		x2, y2 = exit
		if x1 < 0 or x1 > width or y1 < 0 or y1 > height:
			raise ValueError("ENTRY is outside of maze, invalid input")
		if x2 < 0 or x2 > width or y2 < 0 or y2 > height:
			raise ValueError("EXIT is outside of maze, invalid input")

		# generate a grid of cells with nested list structure, each cell is initialized as 15  
		self.grid: list[list[int]] = []
		for _ in range(self.height):
			#??? why [15]
			row: list[int] = [15] * self.width
			self.grid.append(row)
