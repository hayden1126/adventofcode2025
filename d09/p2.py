#!/bin/python3

import sys
import itertools
import math

def dist(a, b):
    return abs(a-b)+1

def area(a, b):
    return dist(a[0], b[0]) * dist(a[1], b[1])

def minmax(a, b):
    return min(a, b), max(a, b)

# implemented str.find but for lists
def list_find(l, x, start):
    return next((i for i, val in enumerate(l) if i >= start and val == x), -1)

# returns the first coordinate it finds that is within the polygon
def raycast(grid):
    x, y = 0, 0
    while x < len(grid[0]) and y < len(grid):
        if grid[x][y] == 1:
            return (x+1, y+1)
        x += 1
        y += 1
    return (None, None)

# floodfills the polygon given a list of at least one coordinate within the polygon
def floodfill(grid, queue):
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            continue
        if grid[y][x] != 0:
            continue
        grid[y][x] = 1
        queue.append((x+1, y))
        queue.append((x-1, y))
        queue.append((x, y+1))
        queue.append((x, y-1))

def prefix_sum(grid):
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if x-1 >= 0:
                grid[y][x] += grid[y][x-1]
                if y-1 >= 0:
                    grid[y][x] += grid[y-1][x] - grid[y-1][x-1]
            elif y-1 >= 0:
                grid[y][x] += grid[y-1][x]

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    rtiles = []
    with open(filename, 'r') as f:
        for l in f:
            coords = l.strip().split(',')
            x, y = int(coords[0]), int(coords[1])
            rtiles.append((x, y))

    uniq_x = sorted(list(set(c[0] for c in rtiles)))
    uniq_y = sorted(list(set(c[1] for c in rtiles)))
    x_map = {val: i*2 +1 for i, val in enumerate(uniq_x)}
    y_map = {val: i*2 +1 for i, val in enumerate(uniq_y)}

    x_size, y_size = len(uniq_x)*2 +1, len(uniq_y)*2 +1
    grid = [[0 for _ in range(x_size)] for _ in range(y_size)]
    
    for (x, y) in rtiles:
        grid[y_map[y]][x_map[x]] = 1

    for i in range(len(rtiles)):
        a, b = rtiles[i-1], rtiles[i]
        x1, x2 = minmax(a[0], b[0])
        y1, y2 = minmax(a[1], b[1])
        for x in range(x_map[x1], x_map[x2]+1):
            for y in range(y_map[y1], y_map[y2]+1):
                grid[y][x] = 1
    
    floodfill(grid, [raycast(grid)])

    psgrid = grid.copy()
    prefix_sum(psgrid)

    mx = 0
    pairs = itertools.combinations(range(len(rtiles)), 2)
    while (p := next(pairs, None)) is not None: 
        a, b = rtiles[p[0]], rtiles[p[1]]
        x1, x2 = minmax(x_map[a[0]], x_map[b[0]])
        y1, y2 = minmax(y_map[a[1]], y_map[b[1]])
        s = psgrid[y2][x2] + psgrid[y1-1][x1-1] - psgrid[y1-1][x2] - psgrid[y2][x1-1]
        if dist(x1, x2) * dist(y1, y2) != s:
            continue
        mx = max(mx, area(a, b))
    print(mx)

main()
