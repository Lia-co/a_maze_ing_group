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

### 1.4.1 Maze generating algorithm

### 1.4.2 Maze solution path algorithm

## 1.5 UI design


# 2. Instruction
## 2.1 How to install
## 2.2 How to run the program

# 3. Resources
[Python Documentation: Dataclass in Python](https://docs.python.org/3/library/dataclasses.html)

[GeeksfoGeeks: Differences and Applications of List, Tuple, Set and Dictionary in Python](https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)

[Wikipedia: Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

[W3school: Python Random seed() Method](https://www.w3schools.com/PYTHON/ref_random_seed.asp)