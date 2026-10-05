#!/usr/bin/env python3

from contextlib import AsyncContextDecorator
from typing import Final, List, Tuple
from utils.config_parse import Config

# from utils.cell import Cell

"""
Define four directions with final[], making variable impossible to redefine
"""
DIRECTIONS: Final[tuple[str, ...]] = ("N", "E", "S", "W")

"""
Bit masks wall's direction
"""
DIR_BIT: Final[dict[str, int]] = {
    "north": 1, #0001
    "east": 2,  #0010
    "south": 4, #0100
    "west": 8  #1000
}

DIR_MOVE: Final[dict[tuple, str]] = {
    (0, -1): "N",
    (1, 0): "E",
    (0, 1): "S",
    (-1, 0): "W"
}

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.visited = False
        self.is_special = False  # <-- to delimit the 42 cells
        self.north = True
        self.east = True
        self.south = True
        self.west = True


def cell_to_hex(cell: Cell) -> str:
    val: int = 0
    for wall, wall_bitmask in DIR_BIT.items():
        if getattr(cell, wall):
            val = val | wall_bitmask
    return format(val, "X")


def maze_to_hex(maze: List[List[Cell]], config: Config) -> List[str]:
    width, height = len(maze[0]), len(maze)
    lines: List[str] = []
    for y in range(height):
        for x in range(width):
            line = "".join(cell_to_hex(maze[y][x]))
            lines.append(line)
    return lines


def path_to_dir(path: List[Tuple[int, int]]) -> str:
    dir_path: List[str] = []
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        dx, dy = x2 - x1, y2 - y1
    dir_path.append(DIR_MOVE[(dx, dy)])
    path_str = "".join(dir_path)
    return path_str






# if __name__ == "__main__":
#     c = Cell(0, 0)
#     print(cell_to_hex(c))


