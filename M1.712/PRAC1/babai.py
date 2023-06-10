import numpy as np
import sys

def distance_euclidean(vecA, vecB):
    dist = np.round(np.linalg.norm(vecA-vecB),2)
    print (f"Euclidean distance between {vecA} and {vecB} is: {dist}")

def ortogonal_flaw(B):
    volume = np.sqrt(np.round(np.linalg.det(np.matmul(B.T,B))))
    modules = 1
    for v in B:
        modules *= np.linalg.norm(v)  
    print (f"Ortogonal flaw of B: {np.round(modules/volume, 3)}")
    print (f"Hadamard ratio of B: {np.round(np.power((volume/modules), 0.5), 3)}")

def babai(base, vector):
    #Pas1. Escrivim w com a suma de producte de vectors i obtenim els coeficients
    x = np.linalg.solve(base.T, vector)
    #Pas2. Arrodonim els coeficients obtinguts a l'enter mes proper
    rounded = np.round(x, 0)
    #Pas3. Obtenim el vector resultant aplicant els coeficients x per cada coordenada.
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

if __name__ == "__main__":
    main()