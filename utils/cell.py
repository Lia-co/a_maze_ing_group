#!/usr/bin/env python3

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.visited = False
        self.north = True
        self.east = True
        self.south = True
        self.west = True