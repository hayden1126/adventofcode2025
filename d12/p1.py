#!/bin/python3

import sys
import numpy as np

class Shapes:
    def __init__(self):
        self.shapes = {}
    
    def __toindex__(self, i):
        if type(i) == int:
            return 1<<int(i)
        elif isinstance(i, Shape):
            pass

    def set(self, i, shape):
        if isinstance(shape, Shape):
            self.shapes[self.__toindex__(i)] = shape
        else:
            self.shapes[self.__toindex__(i)] = Shape(shape)

    def get(self, i):
        if (idx := self.__toindex__(i)) not in self.shapes:
            return None
        return self.shapes[idx]

class Shape:
    def __init__(self, s):
        if isinstance(s, str):
            self.s = s
            self.m = np.array([[1 if c == '#' else 0 for c in line] for line in s.split('\n')], dtype=int)
        elif isinstance(s, np.ndarray):
            self.m = s
            self.s = '\n'.join(''.join('#' if c else '.' for c in row) for row in matrix)
        self.o = [np.rot90(self.m, -k) for k in range(4)]
        self.weight = np.sum(self.m)

    def __str__(self):
        return self.s
    def __repr__(self):
        return self.m


def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    shapes = Shapes()
    with open(filename, 'r') as f:
        buf = f.read().split("\n\n")
    for i in range(6):
        s = buf[i][buf[i].find("\n")+1:]
        shapes.set(i, s)

    count = 0
    regions = buf[6].strip().split('\n')
    for r in regions:
        buf = [int(i) for i in r.replace('x', ' ').replace(':', '').split(' ')]    
        wd, ln = buf[0], buf[1]
        
        # if they definitely don't fit
        tweight = sum(n * shapes.get(i).weight for i, n in enumerate(buf[2:]))
        if tweight > wd * ln:
            continue

        # if they definitely fit without needing to overlap
        if sum(buf[2:]) <= (wd//SHAPE_WIDTH) * (ln//SHAPE_LENGTH):
            count += 1
            continue
    
    print(count)

SHAPES_COUNT = 5
SHAPE_WIDTH, SHAPE_LENGTH = 3, 3
main()

