import numpy as np
import sys

def decrypt(c, privateKey, pubKey):
    x = np.dot(np.linalg.inv(privateKey), c)
    rounded = np.round(x, 0).astype(int)
    v = np.dot(privateKey, rounded)
    Winv = np.linalg.inv(pubKey)
    dec = np.dot(v, Winv)
    m = dec.astype(int)
    return m

def encrypt(m, pubKey):
    # r = np.array([[-1,1,1,-1]])
    r = np.random.randint(-1,1, size=(1,len(pubKey))) 
    cyphertext = np.dot(pubKey,m) + r
    return cyphertext[0]

def rand_unimod(n):
    l = np.tril(np.random.randint(-10, 10, size=(n,n))).astype(int)
    u = np.triu(np.random.randint(-10, 10, size=(n,n))).astype(int)
    for i in range(0, n):
        l[i, i] = u[i, i] = 1
    return np.dot(l,u)

def key_gen(base):
    u = rand_unimod(len(base))
    #print(f"U: {u}")
    print(f"det(u) = {np.round(np.linalg.det(u))}")
    return np.matmul(base,u)
    

def main():
    print("GGH's algorithm (CVP)")
    print(f"Loading input values...")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    m = np.loadtxt(sys.argv[2], dtype='i', delimiter=' ')
    #w = key_gen(base)
    w = np.loadtxt(sys.argv[3], dtype='i', delimiter=' ')
    print(f"B: {base}\nW: {w}\n")
    print(f"m: {m}")
    c = encrypt(m, w)
    print(f"Encrypt ({m}) -> ({c})")
    d = decrypt(c, base, w.T)
    print(f"Decrypt ({c}) -> ({d})")

if __name__ == "__main__":
    main()