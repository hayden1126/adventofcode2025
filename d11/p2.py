#!/bin/python3

import sys
import functools

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
    @functools.lru_cache(maxsize=None)
    def dfs(curr):
        if curr == end:
            return 1
        if curr == "out" or curr not in devices:
            return 0
    
        total = 0
        for c in devices[curr]:
            total += dfs(c)
        return total
    return dfs(start)


print(main())

