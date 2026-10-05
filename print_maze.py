#!/usr/bin/env python3

from utils.config_parse import parse_config
from utils.render import MazeVisualizer
from mazegen.prim import generate_prim_maze
from mazegen.dfs import dfs_maze_generate
from utils.bfs_resolve import bfs_maze_solver
from utils.cell import Cell
from utils.config_parse import Config

def print_maze(
    grid: list[list[Cell]],
    config: Config,
    path: list[tuple[int, int]] | None = None,
) -> None:
    width, height = len(grid), len(grid[0])
    path_set = set(path) if path else set()

    def cell_symbol(x: int, y: int) -> str:
        if (x, y) == config.entry:
            return " A "
        if (x, y) == config.exit:
            return " B "
        if (x, y) in path_set:
            return " . "
        return "   "

    print(f"Laberinth generated: {len(grid[0])}x{len(grid)} ({len(grid) * len(grid[0])} total cells).")
    print(f"\n--- DISPLAY MAZE FOR TESTING ({config.width}x{config.height}) ---", end="\n\n")
    # Top border (north walls of row 0)
    top = "+"
    for x in range(width):
        top += "---+" if grid[0][x].north else "   +"
    print(top)

    for y in range(height):
        # Cell row: west wall, cell content, ... , east wall of last cell
        row = "|" if grid[y][0].west else " "
        for x in range(width):
            row += cell_symbol(y, x)
            row += "|" if grid[y][x].east else " "
        print(row)

        # South wall row (becomes north wall of row y+1 visually)
        bottom = "+"
        for x in range(width):
            bottom += "---+" if grid[y][x].south else "   +"
        print(bottom)


if __name__ == "__main__":
    config = parse_config()
    maze = generate_prim_maze(config)
    # maze = dfs_maze_generate(config)
    solution = bfs_maze_solver(config, maze)

    print_maze(maze, config, solution)
    print(solution)

    