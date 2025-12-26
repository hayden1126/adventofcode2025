#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    devices = {}
    with open(filename, 'r') as f:
        for l in f:
            s = l.index(':')
            devices[l[:s]] = l[s+1:].strip().split(' ')
    r1, r2 = count_paths(devices, "fft", "dac"), count_paths(devices, "dac", "fft")
    assert(r1 == 0 or r2 == 0)

    if r1 == 0:
        return count_paths(devices, "svr", "dac") * r2 * count_paths(devices, "fft", "out")
    elif r2 == 0:
        return count_paths(devices, "svr", "fft") * r1 * count_paths(devices, "dac", "out")

def count_paths(devices, start, end):
    counters = {start: 1}
    queue = [start]
    while len(queue) > 0:
        d1 = queue.pop(0)
        for d2 in devices[d1]:
            if d2 not in counters:
                counters[d2] = 0
            counters[d2] += counters[d1]
            if d2 != end and d2 != "out" and d2 not in queue:
                queue.append(d2)
    
    if end in counters:
        return counters[end]
    else:
        return 0

print(main())

