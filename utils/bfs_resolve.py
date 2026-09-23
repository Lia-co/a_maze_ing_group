#!/usr/bin/env python3

"""
Breadth-first Search (BFS) Solution
"""

from utils import direction as dir
from utils import wall
from utils.maze import maze
from collections import deque
# with typing.Optional attribute could be a specific data type or None
from typing import Optional


def bfs_maze_solver(maze: maze, pattern: set) -> list[tuple[int, int]]:
    # get the entry coordinates from maze
    x, y = maze.entry

    # track visited cells as a set, mark entry as visited
    visited_cell: set[tuple[int, int]] = {}
    # add() for set, unorder collection; append() for list, ordered collection
    visited_cell.add(maze.entry)

    # track frontier cells waiting for visiting later
    # ??? why here use deque?
    cell_to_visit: deque[tuple[int, int]] = deque()
    # ???why entry is to visit?
    cell_to_visit.append(maze.entry)

    # Map each cell's parent cell in BFS tree (child -> parent)
    path_tree: dict[tuple[int, int], Optional[tuple[int, int]]] = {}
    path_tree[maze.entry] = None

    while len(cell_to_visit) != 0:
        current_cell = cell_to_visit.popleft()
        x, y = current_cell
        current_cell_bitmask = maze.grid[y][x]

        # if it reaches the exit, break the loop
        if current_cell == maze.exit:
            break

        # move to all adjcent cells
        for direction in dir.DIRECTIONS:
            dx, dy = dir.DIR_MOVE(direction)
            nx = x + dx
            ny = y + dy

        # check if neighbor cell inside of maze
        # can >= 0 || <=maze.width
        if 0 < nx < maze.width and 0 < ny < maze.height:
            # if there is no wall between cell and the wall direction
            if wall.check_wall(current_cell_bitmask, dir.DIR_BIT(direction)) is False:
                neighbor: list[int, int] = nx, ny
                # if neighbor is not visited yet, mark it to visit queue and record path
                if neighbor not in visited_cell and neighbor not in pattern:
                    visited_cell.add(neighbor)
                    cell_to_visit.append(neighbor)
                    path_tree[neighbor] = current_cell

    # check if exit in path
    if maze.exit not in path_tree:
        raise ValueError("EXIT is not visited.")
    # if exit in path, then reconstruct path from exit to entry
    else:
        last_spot: Optional[tuple[int, int]] = maze.exit
        backtrace: list[tuple[int, int]] = []
        while last_spot is not None:
            backtrace.append(last_spot)
            # ???how to update last spot every time?
            last_spot = path_tree[last_spot]
    # ???why list()
    solution = list(reversed(backtrace))
    return solution
