#!/bin/python3

import sys
import itertools
from functools import reduce
from operator import xor

class Machine:
    def __init__(self, line):
        p1, p2 = line.index('('), line.index('{')
        self.goal = sum(1<<i if v == "#" else 0 for i, v in enumerate(line[1:p1-2]))
        self.state = 0
        
        self.buttons = []
        for button in line[p1:p2-1].split(' '):
            self.buttons.append(sum(1<<int(n) for n in button.strip("()").split(',')))

    def test_toggle(self, i):
        if type(i) == int:
            return self.state ^ i
        else:
            return self.state ^ reduce(xor, i)

    def toggle(self, i):
        self.state = test_toggle(i)

    def __str__(self):
        return f"{bin(self.state)} : {bin(self.goal)} {[bin(b) for b in self.buttons]} {self.jreqs}"

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    machines = []
    with open(filename, 'r') as f:
        for l in f:
            machines.append(Machine(l))

    count = 0

    for m in machines:
        found = False
        for r in range(1, len(m.buttons)+1):
            groups = itertools.combinations(m.buttons, r)
            while (g := next(groups, None)) is not None: 
                if m.test_toggle(g) == m.goal:
                    count += r
                    found = True
                    break
            if found:
                break

    print(count)


main()

