#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = [l for l in f.readlines() if l.strip()]
    
    length = len(lines)
    width = len(lines[0])
    count = 0

    for i in range(length):
        for j in range(width): # For each coordinate
            if lines[i][j] != '@': # skips non-toilet paper
                continue
            
            surr_rolls = 0
            # For each coordinate in the vicinity
            for x in range(max(0, i-1), min(length, i+2)):
                for y in range(max(0, j-1), min(width, j+2)):
                    
                    if x == i and y == j: # skip if it is itself
                        continue

                    if lines[x][y] == '@':
                        surr_rolls += 1
            if surr_rolls < 4:
                count += 1

    print(count)


main()

