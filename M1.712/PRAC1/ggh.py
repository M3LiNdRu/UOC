import numpy as np
import random
import sys

def ggh():
    pass

def rand_unimod(n):
    random_matrix = [ [np.random.randint(-10,10,) for _ in range(n) ] for _ in range(n) ]
    upperTri = np.triu(random_matrix,0)
    lowerTri = [[np.random.randint(-10,10) if x<y else 0 for x in range(n)] for y in range(n)]  

    #we want to create an upper and lower triangular matrix with +/- 1 in the diag  
    for r in range(len(upperTri)):
        for c in range(len(upperTri)):
            if(r==c):
                if bool(random.getrandbits(1)):
                    upperTri[r][c]=1
                    lowerTri[r][c]=1
                else:
                    upperTri[r][c]=-1
                    lowerTri[r][c]=-1
				
    uniModular = np.matmul(upperTri,lowerTri)
    return uniModular

def main():
    print("GGH's algorithm (CVP)")
    print(f"Loading input values...")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    u = rand_unimod(len(base))
    print(f"det(u) = {np.round(np.linalg.det(u))}")
    w = np.matmul(base,u)
    print(f"B: {base}\nW: {w}\n")

if __name__ == "__main__":
    main()