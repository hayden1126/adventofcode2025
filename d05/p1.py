#!/bin/python3

import sys

def update(ranges, l):
    if l.strip() == "":
        return
    tmp = l.split('-')
    a, b = int(tmp[0]), int(tmp[1])
    ranges.append((a, b))

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    fresh_ranges = []
    ingredients = []

    with open(filename, 'r') as f:
        isRange = True
        for l in f.readlines():
            l = l.strip()

            if not isRange:
                if l == "":
                    continue
                ingredients.append(int(l))
                continue
            if l == "":
                isRange = False
                continue
            update(fresh_ranges, l)

    fresh_count = 0
    for ingr in ingredients:
        for r in fresh_ranges:
            if ingr >= r[0] and ingr <= r[1]:
                fresh_count += 1
                break

    print(fresh_count)

main()

