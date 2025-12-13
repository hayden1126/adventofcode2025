#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    devices = {}
    counters = {"you": 1}
    with open(filename, 'r') as f:
        for l in f:
            s = l.index(':')
            devices[l[:s]] = l[s+1:].strip().split(' ')
    
    queue = ["you"]
    while len(queue) > 0:
        d1 = queue.pop(0)
        for d2 in devices[d1]:
            if d2 not in counters:
                counters[d2] = 0
            counters[d2] += counters[d1]
            if d2 != "out" and d2 not in queue:
                queue.append(d2)
    
    print(counters["out"])

main()

