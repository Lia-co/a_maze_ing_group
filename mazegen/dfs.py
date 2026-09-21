#!/usr/bin/env python3

"""
Depth-first search algorithm - iterative implementatoin (with stack)
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
        2.2.4 Mark the chosen cell as visited and push it to the stack
"""

from utils.maze import maze
import random
from utils import direction as dir
from utils import wall as wall

def dfs_maze_generate(maze: maze, seed: int) -> None:
    random.seed(seed)
    # track visited cells
    visited_cell: list[tuple[int, int]] = []
    # DFS stack: track path of cells
    dfs_stack: list[tuple[int, int]] = []

    # choose the initial cell
    init_cell: tuple[int, int] = maze.entry
    x, y = init_cell
    # mark the initial cell as visited
    visited_cell.append(init_cell)
    # mark the initial cell into stack
    dfs_stack.append(init_cell)

    # While the stack is not empty
    while len(dfs_stack) != 0:
        # Pop a cell from the stack and make it a current cell
        current_cell = dfs_stack[-1]
        x, y = current_cell
        # look for unvisited neigbor cells in 4 directions
        unvisited_neighbor: list[tuple[int, int]] = []
        for direction in dir.DIR_MOVE:
            dx,dy = dir.DIR_MOVE[direction]
            nx = x + dx
            ny = y + dy
            # if neigbor cell is within the maze
            if 0 < nx < maze.width and 0 < ny < maze.height:
                neighbor: list[int, int] = (nx, ny)
                if neighbor not in visited_cell and neighbor not in pattern:
                    unvisited_neighbor.append(neighbor)

        # If the current cell has any neighbours which have not been visited
        # keep randomly picking until unvisited cells in maze is none
        if len(unvisited_neighbor) != 0:
            random_cell = random.randint(0, len(unvisited_neighbor) - 1)
            # Choose one of the unvisited neighbours
            neighbor_cell = unvisited_neighbor(random_cell)

            # Remove the wall between the current cell and the chosen cell
            wall.carve_walls(current_cell, neighbor_cell)
            # Mark the chosen cell as visited and push it to the stack
            visited_cell.append(neighbor_cell)
            dfs_stack.append(neighbor_cell)

        #???why this step?
        else:
            dfs_stack.pop()

    # check if visited cells are in forbidden pattern or outside of the maze






