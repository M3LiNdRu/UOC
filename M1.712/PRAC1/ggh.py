import numpy as np
import sys

def decrypt(c, privateKey, pubKey):
    # Calculem l'invers de B · c
    x = np.dot(np.linalg.inv(privateKey), c)
    # Arrodonim el resultat
    rounded = np.round(x, 0).astype(int)
    # Calculem B pel resultat de l'operació anterior
    v = np.dot(privateKey, rounded)
    # Calculem l'invers de la clau pública (W)
    Winv = np.linalg.inv(pubKey)
    # m = Winv · v 
    m = np.dot(v, Winv).astype(int)
    return m

def encrypt(m, pubKey):
    #r = np.array([[-1,1,1,-1]])
    r = np.random.randint(-1,1, size=(1,len(pubKey))) 
    cyphertext = np.dot(pubKey,m) + r
    return cyphertext[0]

def rand_unimod(n):
    # Generem matriu aleatoria amb els elements de sobre la diagonal amb 0
    l = np.tril(np.random.randint(-10, 10, size=(n,n))).astype(int)
    # Generem matriu aleatoria amb els elements de sota la diagonal amb 0
    u = np.triu(np.random.randint(-10, 10, size=(n,n))).astype(int)
    # Omplim la diagonal de les dues matrius amb 1
    for i in range(0, n):
        l[i, i] = u[i, i] = 1
    # Multipliquem les matrius per obtenir la matriu unimodular
    return np.matmul(l,u)

def key_gen(base):
    # Pas 1: Generem matriu unimodular
    u = rand_unimod(len(base))
    print(f"U: {u}")
    print(f"det(u) = {np.round(np.linalg.det(u))}")
    # Pas 2: Calculem W = B · U
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
    d = decrypt(c, base, w)
    print(f"Decrypt ({c}) -> ({d})")

if __name__ == "__main__":
    main()