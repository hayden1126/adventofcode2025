import sys

def main():
    filename = len(sys.argv) == 1 ? "in.txt" : sys.argv[0]
    with open(filename, 'r') as f:
        lines = f.readlines()


