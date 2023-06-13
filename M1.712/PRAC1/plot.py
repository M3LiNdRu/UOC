import numpy as np
import matplotlib.pyplot as plt
import sys

def draw(base):
    origin = np.zeros(np.shape(base), dtype=int)
    plt.quiver(*origin, *base.T, angles='xy', scale_units='xy', scale=1)
    plt.xlim(-10, 350)
    plt.ylim(-450, 150)
    plt.grid()
    plt.show()
    
def main():
    print("Babai's algorithm (CVP)")
    print(f"Loading input values: base={sys.argv[1]}")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    print(f"B: {base}")
    draw(base)

if __name__ == "__main__":
    main()