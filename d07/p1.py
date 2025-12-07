#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = [list(l) for l in f.readlines() if l.strip()]

    start = lines[0].index('S')
    lines[1][start] = '|'

    count = 0
    for r in range(2, len(lines)):
        row = lines[r]
        for i, c in enumerate(row):
            if lines[r-1][i] == '|':
                if c == '^':
                    count += 1
                    row[i-1], row[i+1] = '|', '|'
                elif c == '.':
                    row[i] = '|'

    print(count)


main()

