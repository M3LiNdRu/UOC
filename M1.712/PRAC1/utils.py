import numpy as np
import sys

def vector_difference(c, m):
    result = np.subtract(c, m)
    print ('the difference =', result)
    return result

def distance_euclidean(vecA, vecB):
    dist = np.round(np.linalg.norm(vecA-vecB),2)
    print (f"Euclidean distance between {vecA} and {vecB} is: {dist}")

def ortogonal_flaw(B):
    volume = np.abs(np.linalg.det(B))
    #volume = np.sqrt(np.round(np.linalg.det(np.matmul(B.T,B))))
    print(f"volume: {volume}")
    modules = 1
    for v in B:
        modules *= np.linalg.norm(v)  
    print(modules)
    print (f"Ortogonal flaw of B: {np.round(modules/volume, 3)}")
    print (f"Hadamard ratio of B: {np.round(np.power((volume/modules), 0.5), 3)}")

def decrypt(c, privateKey, pubKey):
    x = np.dot(np.linalg.inv(privateKey), c)
    rounded = np.round(x, 0).astype(int)
    v = np.dot(privateKey, rounded)
    print(v)
    Winv = np.linalg.inv(pubKey)
    m = np.dot(v, Winv).astype(int)
    return m

def encrypt(m, pubKey):
    r = np.array([[70, 94, -111]])
    cyphertext = np.dot(pubKey,m) + r
    return cyphertext[0]

def main():
    print(f"Loading input values: base={sys.argv[1]}, w={sys.argv[2]}")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    w = np.loadtxt(sys.argv[2], dtype='i', delimiter=' ')
    print(f"B: {base}\n")
    ortogonal_flaw(base)
    c = np.array([8930810, -44681748, 75192665])
    v = np.array([8930740, -44681654, 75192776])
    r = vector_difference(c, v)
    Winv = np.linalg.inv(w)
    print(f"c = {np.add(v, r)}")
    m = np.dot(v, Winv).astype(int)
    print(f"message: {m}")
    m = decrypt(c, base, w)
    print(f"message: {m}")
    c = encrypt(m, w.T)
    print(f"c: {c}")
    m = decrypt(c, base, w)
    print(f"message: {m}")

if __name__ == "__main__":
    main()