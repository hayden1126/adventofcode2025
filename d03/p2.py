#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    joltage = 0

    for bank in lines:
        digits = [0 for _ in range(13)] # stores the index of n for that digit
        digits[0] = -1

        for d in range(1, 13): # For each digit
            mx = 0
            for i in range(digits[d-1]+1, len(bank)-12+d):
                if int(bank[i]) > mx:
                    mx = int(bank[i]) # first occurance of max within the range
                    digits[d] = i
    
        result = ""
        for d in digits[1:]:
            result += bank[d]

        joltage += int(result)

    print(joltage)
            
main()

