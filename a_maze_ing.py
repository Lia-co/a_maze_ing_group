#!/usr/bin/env python3

import sys
import utils.output as output
from utils.config_parse import parse_config
from utils.render import MazeVisualizer
from mazegen.prim import generate_prim_maze
from mazegen.dfs import dfs_maze_generate
from utils.bfs_solver import bfs_maze_solver
import utils.output as output


def main():
    config_file = sys.argv[1]
    config = parse_config(config_file)
    if config.algorithm.upper() == "DFS":
        maze = dfs_maze_generate(config)
    elif config.algorithm.upper() == "PRIM":
        maze = generate_prim_maze(config)
    solution = bfs_maze_solver(config, maze)

    # write output file
    output.write_output(maze, solution, config)

    # print maze for testing
    print(f"Laberinth generated: {len(maze[0])}x{len(maze)} ({len(maze) * len(maze[0])} total cells).")
    # --- print maze on terminal for testing ---
    print(f"\n--- DISPLAY MAZE FOR TESTING ({config.width}x{config.height}) ---")
    for y, row in enumerate(maze):
        line = ""
        for cell in row:
            top = "---" if cell.north else "   "
            left = "|" if cell.west else " "
            line += left + top
        print(line)
    print("-" * 40)

    renderer = MazeVisualizer(maze, config, solution)
    renderer.start()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")