#!/usr/bin/env python3

"""
Breadth-first Search (BFS) Solution
"""

from typing import List
from utils.cell import Cell
from utils.config_parse import Config
from collections import deque
from typing import Optional


def check_wall(current: Cell, neighbor: Cell) -> None:
    """check between two adjacent cells."""
    dx = neighbor.x - current.x
    dy = neighbor.y - current.y

    if dx == 1 and current.east is False and neighbor.west is False:       # Neighbor is East
        return False
    elif dx == -1 and current.west is False and neighbor.east is False:    # Neighbor is West
        return False
    elif dy == 1 and current.south is False and neighbor.north is False:     # Neighbor is South
        return False
    elif dy == -1 and current.north is False and neighbor.south is False:    # Neighbor is North
        return False
    else:
        return True


def bfs_maze_solver(config: Config, grid: List[List[Cell]]) -> list[tuple[int, int]]:
    x, y = config.entry

    visited_cell: set[tuple[int, int]] = {}
    visited_cell.add(config.entry)

    cell_to_visit: deque[tuple[int, int]] = deque()
    cell_to_visit.append(config.entry)

    # Map each cell's parent cell in BFS tree (child -> parent)
    path_tree: dict[tuple[int, int], Optional[tuple[int, int]]] = {}
    path_tree[config.entry] = None

    while len(cell_to_visit) != 0:
        current_cell = cell_to_visit.popleft()
        x, y = current_cell
        current_cell_bitmask = grid[y][x]

        # if it reaches the exit, break the loop
        if current_cell == config.exit:
            break

        # move to all adjcent cells
        def add_frontier(cell: Cell) -> List[Cell]:
            """Adds unvisited neighbors of a cell to the frontier list."""
            frontier: list[Cell] = []
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = cell.x + dx, cell.y + dy
                # if neigbor cell is within the maze
                if 0 <= nx < config.width and 0 <= ny < config.height:
                    neighbor = grid[ny][nx]
                    if not neighbor.visited:
                        frontier.append(neighbor)
            return frontier

        # check if neighbor cell inside of maze
        if 0 <= nx < config.width and 0 <= ny < config.height:
            # if there is no wall between cell and the wall direction
            if check_wall(current_cell_bitmask, dir.DIR_BIT(direction)) is False:
                neighbor: list[int, int] = nx, ny
                # if neighbor is not visited yet, mark it to visit queue and record path
                if neighbor not in visited_cell:
                    visited_cell.add(neighbor)
                    cell_to_visit.append(neighbor)
                    path_tree[neighbor] = current_cell

    # check if exit in path
    if config.exit not in path_tree:
        raise ValueError("EXIT is not visited.")
    # if exit in path, then reconstruct path from exit to entry
    else:
        last_spot: Optional[tuple[int, int]] = config.exit
        backtrace: list[tuple[int, int]] = []
        while last_spot is not None:
            backtrace.append(last_spot)
            # ???how to update last spot every time?
            last_spot = path_tree[last_spot]
    # ???why list()
    solution = list(reversed(backtrace))
    return solution
