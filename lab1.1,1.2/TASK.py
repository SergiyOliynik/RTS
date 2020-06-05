import matplotlib.pyplot as plt
import math
from random import *
import time


n = 6
N = 256
omega = 2100

y = []
freqY = []
AY = []
alphaY = []

x = []
freq = []
A = []
alpha = []
Rxx = []
Rxy = []


def generateFreq(omega, n):
    freq = []

    step = omega/n

    for i in range(n):
        freq.append(omega - step*i)

    return freq

def generateXt(N, n, A, freq, alpha):
    x = [0]*N

    for j in range(N):
        for i in range(n):
            x[j] += A[i]*math.sin(freq[i]*j + alpha[i])
    return x

def mathExpecation(x, N):
    mx = 0.0
    for i in range(N):
        mx += x[i]

    return mx / N

def dispersion(x, N, mx):
    dx = 0.0
    for i in range(N):
        dx += math.pow(x[i]-mx, 2)

    return dx/(N-1)

def arrGenerator(n, min, max):
    arr = [0]*n

    for i in range(n):
        arr[i] = randint(min, max)

    return arr

def findRxx(N, x, mx):
    start = time.time()
    time.sleep(1)
    Rxx = [0]*(int(N/2-1))
    end = time.time() - start - 1
    for i in range(int(N/2-1)):
        for j in range(int(N/2-1)):
            Rxx[i] += ((x[j] - mx) * (x[i+j] - mx))/(N-1)

    return Rxx, end
Rxx_time=findRxx(N, x, mx)

def findRxy(N, y, mx, my):
    Rxy = [0]*(int(N/2-1))

    for i in range(int(N/2-1)):
        for j in range(int(N/2-1)):
            Rxy[i] += ((y[j]-mx)*((y[j+i])-my))/(N-1)

    return Rxy


A = arrGenerator(n, 0, 5)
alpha  = arrGenerator(n, 0, 5)
freq = generateFreq(omega, n)
x = generateXt(N, n, A, freq, alpha)

AY = arrGenerator(n, 0, 5)
alphaY = arrGenerator(n, 0, 5)
freqY = generateFreq(omega, n)
y = generateXt(N, n, AY, freqY, alphaY)

# mx and dx
mx = mathExpecation(x, N)
my = mathExpecation(y, N)

dx = dispersion(x, N, mx)
dy = dispersion(y, N, my)

print("mx: " + str(mx))
print("dx: " + str(dx))
# Rxx, Rxy
Rxx = findRxx(N, x, mx)
print("rxx: " + str(len(Rxx)))
Rxy = findRxy(N, y, mx, my)
print(Rxy)


# Draw xt, Rxx, Rxy
def draw_line():
    for i in range(N):
        y[i] = i

    plt.plot(y, x)
    plt.title("Xt")
    plt.ylabel("x", fontsize=10)
    plt.xlabel("t", fontsize=10)

    plt.tick_params(axis="both", labelsize=9)

    plt.show()


def draw_line_Rxx():
    y = [0]*(int(N/2-1))
    for i in range(int(N / 2 - 1)):
        y[i] = i

    plt.plot(y, Rxx)
    plt.title("Rxx")
    plt.ylabel("Rxx", fontsize=10)
    plt.xlabel("t", fontsize=10)

    plt.tick_params(axis="both", labelsize=9)

    plt.show()


def draw_line_Rxy():
    y = [0]*(int(N/2-1))
    for i in range(int(N/2 - 1)):
        y[i] = i

    plt.plot(y, Rxy)
    plt.title("Rxy")
    plt.ylabel("Rxy", fontsize=10)
    plt.xlabel("t", fontsize=10)

    plt.tick_params(axis="both", labelsize=9)

    plt.show()


draw_line()
draw_line_Rxx()
draw_line_Rxy()
print(Rxx_time)