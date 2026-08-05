#!/bin/usr/env python3

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.visited = False
        self.north = True
        self.east = True
        self.south = True
        self.west = True

maze = [
        [Cell(0,0), Cell(0,1)],
        [Cell(1,1), Cell(1,2)]
    ]

if __name__ == "__main__":
    for row in maze:
        for cell in row:
            print(cell.x, cell.y)
        
