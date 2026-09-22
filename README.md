*This project has been created as part of the 42 curriculum by betferna and sliang.*

# 1. Description
## 1.1 Overview
*insert a gif to present the demo*</br>
A_Maze_Ing project is aimed at make a reusable maze generation program with UI design. The user can pass data into a config file to manage how the maze look like. The config file decides the size of the maze(WIDTH, HEIGHT), entry and exit location(ENTRY, EXIT), the name of output file including maze map in hexdecimal code, and if the maze is perfect(only one path) or not(multiple paths).

Here is an example of a config file:
```
# config file
# mandatory part
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True

# conditional part
SEED=42
ALGORITHM=BFS
```

This project is perfect for beginers to understand module logic, algorithms, data parsing process and have fun for UI design.

## 1.2 Tasks distribution

### 1.2.1 The structure of files
### 1.2.2 Decision reasons for distribution

## 1.3 Data parsing, validation and return object

## 1.4 Algorithms choices
For algorithms of generating maze, we choose Depth-first search algorithm, one of the most common choices, and Prim's algorithm.

For maze solution, we choose Breadth First Search algorithm. It starts at a starting point, and visit other cells level by level, which means visiting all adjcent cells. 

### 1.4.1 Maze generating algorithm
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

### 1.4.2 Maze solution path algorithm
BFS will find the shortest path from entry to exit. It tracks visited cells and adjecent cells for visiting later.

## 1.5 UI design
We decide to use MiniLibX(MLX) as interface window. with MLX, we can have more space for UI design and make it more fun. 

# 2. Instruction
## 2.1 How to install
## 2.2 How to run the program

# 3. Resources
[Python Documentation: Dataclass in Python](https://docs.python.org/3/library/dataclasses.html)

[GeeksfoGeeks: Differences and Applications of List, Tuple, Set and Dictionary in Python](https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)

[W3Schools: Python Random seed() Method](https://www.w3schools.com/PYTHON/ref_random_seed.asp)

[W3Schools: Python List pop() Method](https://www.w3schools.com/python/ref_list_pop.asp)

[W3Schools: Python list() Function](https://www.w3schools.com/python/ref_func_list.asp)

[GeeksforGeeks: Deque in Python](https://www.geeksforgeeks.org/python/deque-in-python/)

[Wikipedia: Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

[Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/)
