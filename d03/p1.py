#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    joltage = 0

    for bank in lines:
        if len(bank) <= 2:
            joltage += int(bank)

        d1 = 0
        d2 = 0
        for i in range(len(bank)-2, -1, -1):
            n = int(bank[i])
            if n >= d1:
                d2 = d1
                d1 = int(bank[i])
        d2 = max(d2, int(bank[-1]))

        joltage += d1*10 + d2
    
    print(joltage)

            
main()

