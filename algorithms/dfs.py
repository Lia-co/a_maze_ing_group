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
