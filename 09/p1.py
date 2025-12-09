#!/bin/python3

import sys
import itertools

def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    rtiles = []
    with open(filename, 'r') as f:
        for l in f:
            coords = l.strip().split(',')
            rtiles.append((int(coords[0]), int(coords[1])))
    
    mx = 0
    pairs = itertools.combinations(range(len(rtiles)), 2)
    while (p := next(pairs, None)) is not None: 
        a, b = rtiles[p[0]], rtiles[p[1]]
        mx = max(mx, area(a, b))

    print(mx)


main()

