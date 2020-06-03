from math import sin, pi, cos, sqrt
import matplotlib.pyplot as plt
import random
import numpy

def x(t, A, phi ):
    return sum(A[i]*sin(partial_frequency[i] * t + phi[i]) for i in range(n))
N = 256
n = 6
frequency = 2100

Ax   = [random.random() for _ in range(n)]
phix = [random.uniform(0, 2*pi) for _ in range(n)]
partial_frequency = [frequency/n * (i+1) for i in range(n)]

x_result = [x(i,Ax,phix) for i in range(N)]

Mx = sum(x_result)/N
Dx = sum((x_result[i] - Mx)**2 for i in range(N))/(N-1)

re =[]
im =[]
for p in range(N-1):
    l=0
    h=0
    for k in range(N-1):
        l += x_result[k] * cos(2*pi/N *p *k)
        h += x_result[k] * sin(2*pi/N *p *k)
    re.append(l)
    im.append(h)
f = []
for p in range(N-1):
    f.append(sqrt(re[p]**2 + im[p]**2))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(list(range(N)), x_result)
ax1.set_xlim([0, N])
ax1.set_title('Mx = {}, Dx = {}'.format(Mx, Dx))
ax1.set_ylabel('x(t)')
ax2.bar(list(range(N-1)), f)

plt.show()