import sys
import numpy as np
import math
import matplotlib.pyplot as plt

def draw(base):
    origin = np.zeros(np.shape(base), dtype=int)
    plt.quiver(*origin, *base.T, angles='xy', scale_units='xy', scale=1)
    plt.xlim(np.amin(base.T[0]), np.amax(base.T[0]))
    plt.ylim(np.amin(base.T[1]), np.amax(base.T[1]))
    plt.grid()
    plt.show()

def babai_old():
    x1=213
    y1=-437
    x2=312
    y2=105
    x=43127
    y=11349
    costheta = ((x1*x2)+(y1*y2))/(math.sqrt(x1*x1+y1*y1)*math.sqrt(x2*x2+y2*y2))
    print ("Cos theta: ",costheta)
    print ("Grid point: ",x1,y1)
    print ("Grid point: ",x2,y2)
    _solve1 = np.array([[x1,x2], [y1,y2]])
    _solve2 = np.array([x,y])
    x = np.linalg.solve(_solve1, _solve2)
    a=round(x[0],0)
    b=round(x[1],0)
    print ("Solution (not rounded): ",x[0],x[1])
    print ("Solution: ",a,b)
    print ("Nearest: ",x1*a+x2*b,y1*a+y2*b)

def babai(base, vector):
    # costheta = ((x1*x2)+(y1*y2))/(math.sqrt(x1*x1+y1*y1)*math.sqrt(x2*x2+y2*y2))
    # print ("Cos theta: ",costheta)
    # print ("Grid point: ",x1,y1)
    # print ("Grid point: ",x2,y2)
    x = np.linalg.solve(base.T, vector)
    rounded = np.round(x, 0)
    print ("Solution (not rounded): ", x)
    print ("Solution: ", rounded)
    print ("Nearest point close to ", vector , " -> ", np.dot(base.T, rounded))

def check_if_ortogonal(base):
    print(np.allclose(base.T, np.linalg.inv(base), atol=-0.04))

def main_old():
    print("Algorisme de babai (CVP)")
    babai_old();

def main():
    print("Algorisme de babai (CVP)")
    print(f"Carregant valors d'entrada: base={sys.argv[1]}, w={sys.argv[2]}")
    base = np.loadtxt(sys.argv[1], dtype='i', delimiter=' ')
    w = np.loadtxt(sys.argv[2], dtype='i', delimiter=' ')
    print(f"B: {base}\nw: {w}\n")
    babai(base, w)
    draw(base)
    #check_if_ortogonal(base)

if __name__ == "__main__":
    main()