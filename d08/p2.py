#!/bin/python3

import sys
import itertools

def prod(l):
    result = 1
    for n in l:
        result *= n
    return result

def sq_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

def findset(djnt_sets, a):
    for i, s in enumerate(djnt_sets):
        if a in s:
            return i
    return -1

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    boxes = []
    with open(filename, 'r') as f:
        for l in f:
            coords = l.strip().split(',')
            boxes.append((int(coords[0]), int(coords[1]), int(coords[2])))

    djnt_sets = [{i} for i in range(len(boxes))]

    dist_pairs = [(sq_dist(boxes[a], boxes[b]), a, b) for (a, b) in itertools.combinations(range(len(boxes)), 2)] 
    dist_pairs.sort(key=lambda p: p[0])

    last_pair = None
    for p in dist_pairs:
        s1 = findset(djnt_sets, p[1])
        s2 = findset(djnt_sets, p[2])
        if s1 == s2:
            continue
        last_pair = (p[1], p[2])
        djnt_sets[s1].update(djnt_sets[s2])
        djnt_sets.pop(s2)
    
    result = boxes[last_pair[0]][0] * boxes[last_pair[1]][0]
    print(result)

main()

