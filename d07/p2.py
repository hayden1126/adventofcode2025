#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            l = line.strip()
            if l:
                lines.append([-1 if c != '.' else 0 for c in l])

    lines[0][lines[0].index(-1)] = 1 # replace start with 1

    for r in range(1, len(lines)):
        row = lines[r]
        for i, c in enumerate(row):
            prev = lines[r-1][i]
            if prev > 0:
                if c == -1:
                    row[i-1] += prev
                    row[i+1] += prev
                else:
                    row[i] += prev
    
    assert(-1 not in lines[-1])   
    print(sum(lines[-1]))

main()

