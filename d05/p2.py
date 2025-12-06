#!/bin/python3

import sys

def update(ranges, l):
    if l.strip() == "":
        return
    tmp = l.split('-')
    a, b = int(tmp[0]), int(tmp[1])

    inserted = -1

    for i, r in enumerate(ranges):
        if r == [-1, -1]:
            continue

        if inserted < 0:
            if a > r[1]: # next range
                continue
            elif b < r[0]: # insert before current range
                ranges.insert(i, [a, b])
                inserted = i
                break
            r[0] = min(r[0], a)
            r[1] = max(r[1], b)
            inserted = i
        else: # inserted already, check for overlaps with next ranges
            if i == 0:
                break

            if ranges[inserted][1] < r[0]:
                break

            else:
                ranges[inserted][1] = max(ranges[inserted][1], r[1])
                # DELETE new range
                r[0], r[1] = -1, -1 # -1 effectively means deleted without shifting actual index of the range in list

    if inserted < 0: # if (a, b) bigger than all ranges
        ranges.append([a, b])

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    fresh_ranges = []

    with open(filename, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if l == "":
                break
            update(fresh_ranges, l)

    fresh_count = 0

    for r in fresh_ranges:
        if r == [-1, -1]:
            continue
        fresh_count += r[1] - r[0] + 1

    print(fresh_count)

main()

