#!/bin/python3

import sys

class Machine:
    def __init__(self, line):
        p1, p2 = line.index('('), line.index('{')
        self.goal = sum(1<<(p1-4-i) if v == "#" else 0 for i, v in enumerate(line[1:p1-2]))
        self.state = 0
        
        self.buttons = []
        for button in line[p1:p2-1].split(' '):
            self.buttons.append(sum(1<<int(n) for n in button.strip("()").split(',')))
            
        self.jreqs = [int(n) for n in line[p2:].strip(" {}\n").split(',')]

    def toggle(self, i):
        if type(i) == int:
            self.state ^= i
        elif type(i) == list:
            for n in i:
                self.state ^= i

    def __str__(self):
        return f"{bin(self.state)} : {bin(self.goal)} {[bin(b) for b in self.buttons]} {self.jreqs}"

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    machines = []
    with open(filename, 'r') as f:
        for l in f:
            machines.append(Machine(l))
    

main()

