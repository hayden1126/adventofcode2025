#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        ranges = f.readline().strip().split(',')

    count = 0
    for r in ranges:
        tmp = r.split('-')
        a, b = int(tmp[0]), int(tmp[1])

        for n in range(a, b+1):
            n_str = str(n)
            if len(n_str)%2 == 1:
                continue

            i = len(n_str)//2
            if n_str[:i] == n_str[i:]:
                count += n

    print(count)

main()

