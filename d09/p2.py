#!/bin/python3

import sys
import itertools
import math

def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

def update_rng(rng, v):
    if v < rng[0]:
        rng[0] = v
    if v > rng[1]:
        rng[1] = v

def xray(grid):
    for l in grid:
        inside = l[0]
        for i in range(1, len(l)):
            if l[i] != l[i-1]:
                if inside:
                    l[i] = True
                else:
                    inside = True

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    rtiles = []
    x_rng = [math.inf, 0]
    y_rng = [math.inf, 0]
    with open(filename, 'r') as f:
        for l in f:
            coords = l.strip().split(',')
            x, y = int(coords[0]), int(coords[1])
            rtiles.append((x, y))
            update_rng(x_rng, x)
            update_rng(y_rng, y)

    x_diff = x_rng[1] - x_rng[0] + 1
    y_diff = y_rng[1] - y_rng[0] + 1
    grid = [[False for _ in range(y_diff)] for _ in range(x_diff)]

    for i in range(len(rtiles)):
        a, b = rtiles[i-1], rtiles[i]
        x1, x2 = min(a[0], b[0])-x_rng[0], max(a[0], b[0])+1-x_rng[0]
        y1, y2 = min(a[1], b[1])-y_rng[0], max(a[1], b[1])+1-y_rng[0]
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = True

    xray(grid)
    for l in grid:
        print(l)
    exit() 

    mx = 0
    pairs = itertools.combinations(range(len(rtiles)), 2)
    while (p := next(pairs, None)) is not None: 
        a, b = rtiles[p[0]], rtiles[p[1]]
        mx = max(mx, area(a, b))

    print(mx)


main()

