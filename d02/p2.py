#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(filename, 'r') as f:
        ranges = f.readline().strip().split(',')

    count = 0
    for r in ranges:
        tmp = r.split('-')
        a, b = int(tmp[0]), int(tmp[1])

        # For each number in range
        for n in range(a, b+1):
            n_str = str(n)

            for splits in range(2, len(n_str)+1):
                if len(n_str)%splits == 1:
                    continue
                
                l = len(n_str)//splits # length of each junction

                isPattern = True
                for i in range(0, len(n_str)-l, l):
                    if n_str[i:i+l] != n_str[i+l:i+l+l]:
                        isPattern = False
                        break
                if isPattern:
                    count += n
                    break

    print(count)

main()

