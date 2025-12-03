#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = [l for l in f.readlines() if l.strip()]

    pos = 50
    count = 0
    for l in lines:
        sign = 1 if l[0] == 'R' else -1
        mag = int(l[1:])
        
        for _ in range(mag):
            pos += sign
            pos %= 100
            if pos == 0:
                count += 1
    print(count)

main()

