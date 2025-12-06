#!/bin/python3

import sys
import math

def calc(operands, start, stop, operator):
    assert(stop >= start)
    
    rng = stop-start
    vals = [0 for _ in range(rng)]
    for l in operands:
        for i in range(rng):
            if l[start+i].isnumeric():
                vals[i] = vals[i]*10 + int(l[start+i])
    
    if operator == '+':
        return sum(vals)
    if operator == '*':
        return math.prod(vals)

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]

    with open(filename, 'r') as f:
        lines = [l for l in f.readlines() if l.strip()]

    operands = lines[:-1]
    operators = lines[-1]
   
    result = 0
    start = 0
    op = operators[start] # first operator
    assert(op.strip() in ['*', '+'])
    
    # find next operator
    for idx in range(start+1, len(operators)):
        if operators[idx].isspace():
            continue
        result += calc(operands, start, idx-1, op)
        
        start = idx
        op = operators[start]
    
    # reached the end, no next operator
    result += calc(operands, start, len(operators), op)

    print(result)

main()

