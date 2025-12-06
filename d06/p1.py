#!/bin/python3

import sys

def calc(operands, column, operator):
    result = -1

    match operator:
        case '+':
            result = 0
            for r in operands:
                result += int(r[column])
        case '*':
            result = 1
            for r in operands:
                result *= int(r[column])

    return result

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    
    lines = []
    operators = []

    with open(filename, 'r') as f:
        for l in f:
            vals = l.split()
            if not vals:
                continue

            if vals[0].isnumeric():
                lines.append(vals)
            else:
                operators.append(vals)
    assert(len(operators) == 1)
    
    sum = 0
    for c in range(len(lines[0])):
        sum += calc(lines, c, operators[0][c])

    print(sum)

main()

