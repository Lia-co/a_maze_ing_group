#!/usr/bin/env python3

import random
from typing import Any, List, Tuple
from utils.cell import Cell


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


def dfs_maze_generate(config: Any) -> List[List[Cell]]:
    """Depth-first search algorithm - iterative implementatoin (with stack)
    With a stack to track visited cells, and it will reach every cell. When all
    cells are visited, it trackback to the entry point.

    This algorithm follows below steps:
    1. Choose the initial cell, mark it as visited and push it to the stack
    2. While the stack is not empty
        2.1 Pop a cell from the stack and make it a current cell
        2.2 If the current cell has any neighbours which have not been visited
            2.2.1 Push the current cell to the stack
            2.2.2 Choose one of the unvisited neighbours
            2.2.3 Remove the wall between the current cell and the chosen cell
            2.2.4 Mark the chosen cell as visited and push it to the stack"""
    if config.seed is not None and config.seed >= 0:
        random.seed(config.seed)

    width, height = config.width, config.height

    # 1. Initialize grid using existing Cell class and stack to track path
    grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
    dfs_stack: list[tuple[int, int]] = []

    # 2. Pick the start cell and mark it as visited
    init_cell: Tuple[int, int] = config.entry
    x, y = init_cell
    start_cell = grid[y][x]
    start_cell.visited = True
    dfs_stack.append(start_cell)

    # 3. look for unvisited neigbor cells in 4 directions
    def add_frontier(cell: Cell) -> List[Cell]:
        """Adds unvisited neighbors of a cell to the frontier list."""
        frontier: list[Cell] = []
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            # if neigbor cell is within the maze
            if 0 <= nx < width and 0 <= ny < height:
                neighbor = grid[ny][nx]
                # !need to add not in 42 pattern
                if not neighbor.visited:
                    frontier.append(neighbor)
        return frontier

    # 4. main dfs' generation loop
    while dfs_stack:
        # Pop a cell from the stack and make it a current cell
        current_cell = dfs_stack[-1]
        candidates = add_frontier(current_cell)

        # If the current cell has any neighbours which have not been visited
        # keep randomly picking until unvisited cells in maze is none
        if candidates:
            neighbor_cell = random.choice(candidates)
            # Remove the wall
            remove_walls(current_cell, neighbor_cell)
            # Mark the chosen cell as visited and push it to the stack
            neighbor_cell.visited = True
            dfs_stack.append(neighbor_cell)

        else:
            dfs_stack.pop()

    # check if visited cells are in forbidden pattern or outside of the maze
    # if (len(visited_cell) < (width * height - len(pattern))):
    #     raise ValueError("Not all cells are visited.")
    # elif (len(visited_cell) > (width * height - len(pattern))):
    #     raise ValueError("Invalid. The amount of visited cells more than the"
    #                      "amount of maze.")

    return grid
