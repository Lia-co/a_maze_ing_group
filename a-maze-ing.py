#!/usr/bin/env python3

from utils.config_parse import parse_config
from utils.render import MazeVisualizer
from mazegen.prim import generate_prim_maze
from utils.cell import Cell


if __name__ == "__main__":
    config = parse_config()
    maze = generate_prim_maze(config)

    #print maze for testing
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

    solution = {(0,0), (1,0), (1,1)} 

    renderer = MazeVisualizer(maze, config, solution)
    try:
        renderer.start()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")