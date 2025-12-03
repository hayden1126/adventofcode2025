#!/bin/python3

import sys

def main():
    filename = "in.txt" if len(sys.argv) == 1 else sys.argv[0]
    with open(filename, 'r') as f:
        lines = [l for l in f.readlines() if l.strip()]

main()

