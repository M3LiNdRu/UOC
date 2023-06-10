import numpy as np
import sys

def ggh():
    pass



def main():
    print("GGH's algorithm (CVP)")
    print(f"Loading input values...")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    w = np.loadtxt(sys.argv[2], dtype='i', delimiter=' ')
    print(f"B: {base}\nw: {w}\n")
    ggh()

if __name__ == "__main__":
    main()