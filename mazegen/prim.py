#!/usr/bin/env python3

import random
from typing import Any, List, Tuple
from utils.config_parse import Config #?why Config is not accessible?
from utils.cell import Cell

"""
Prim's algorithm
This algorithm follows below steps:
1. Pick a random cell, mark it as visited
2. Add the cell's all adjacent walls to a frontier list.
3. While the frontier list is not empty:
    3.1 Randomly pick a wall from frontier list.
    3.2 Check if the two cells divided by that wall.
        3.2.1 If only one of them has been visited:
        3.2.2 Carve the wall to connect both cells.
4. Mark the unvisited cell as "visited" and repeat from step 2.
5. If both cells are already visited, simply remove the wall from the list
without doing anything (to prevent creating loops/cycles).

While the frontier list is completely empty and the maze is generated.
"""


def remove_walls(current: Cell, neighbor: Cell) -> None:
    """Carves a passage between two adjacent cells."""
    dx = neighbor.x - current.x
    dy = neighbor.y - current.y

    if dx == 1:       # Neighbor is East
        current.east = False
        neighbor.west = False
    elif dx == -1:    # Neighbor is West
        current.west = False
        neighbor.east = False
    elif dy == 1:     # Neighbor is South
        current.south = False
        neighbor.north = False
    elif dy == -1:    # Neighbor is North
        current.north = False
        neighbor.south = False


def generate_prim_maze(config: Any) -> List[List[Cell]]:
    if config.seed is not None and config.seed >= 0:
        random.seed(config.seed)

    width, height = config.width, config.height

    # 1. Initialize grid using your existing Cell class
    grid = [[Cell(x, y) for x in range(width)] for y in range(height)]

    # 2. Pick a random starting cell
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    start_cell = grid[start_y][start_x]
    start_cell.visited = True

    # 3. Frontier list storing wall connections: (visited_cell, neighbor_cell)
    frontier: List[Tuple[Cell, Cell]] = []

    def add_frontier(cell: Cell) -> None:
        """Adds unvisited neighbors of a cell to the frontier list."""
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # North, South, East, West
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbor = grid[ny][nx]
                if not neighbor.visited:
                    frontier.append((cell, neighbor))

    add_frontier(start_cell)

    # 4. Main Prim's generation loop
    while frontier:
        cell, neighbor = frontier.pop(random.randint(0, len(frontier) - 1))

        if not neighbor.visited:
            neighbor.visited = True
            remove_walls(cell, neighbor)
            add_frontier(neighbor)

    return grid
