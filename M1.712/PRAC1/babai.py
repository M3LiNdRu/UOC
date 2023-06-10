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

def distance_euclidean(vecA, vecB):
    dist = np.round(np.linalg.norm(vecA-vecB),2)
    print (f"Euclidean distance between {vecA} and {vecB} is: {dist}")

def ortogonal_flaw(B):
    volume = np.sqrt(np.round(np.linalg.det(np.matmul(B.T,B))))
    modules = np.linalg.norm(B[0]) 
    for v in B[1:]:
        modules *= np.linalg.norm(v)  
        
    print (f"Ortogonal flaw of B: {np.round(modules/volume, 3)}")
    print (f"Hadamard ratio of B: {np.round(np.power((volume/modules), 0.5), 3)}")


def babai(base, vector):
    x = np.linalg.solve(base.T, vector)
    rounded = np.round(x, 0)
    v = np.dot(base.T, rounded)
    print (f"Closest vector: {v}")
    return v


def main():
    print("Babai's algorithm (CVP)")
    print(f"Loading input values: base={sys.argv[1]}, w={sys.argv[2]}")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    w = np.loadtxt(sys.argv[2], dtype='i', delimiter=' ')
    print(f"B: {base}\nw: {w}\n")
    v = babai(base, w)
    distance_euclidean(w, v)
    ortogonal_flaw(base)
    #draw(base)

if __name__ == "__main__":
    main()