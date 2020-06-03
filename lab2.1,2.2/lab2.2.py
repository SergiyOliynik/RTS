from mpi4py import MPI
from math import sin, cos, pi, sqrt
from random import random
import matplotlib.pyplot as plt
from time import time


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


n = 6
wmax = 2100
N = 256


def generate_signal(n, wmax, t, A, phi):
    point = 0
    for i in range(n):
        w = wmax / n * (i + 1)
        point += A[i] * sin(w * t + phi[i])

    return point


def generate_random_values(n):
    A = [random() for _ in range(n)]
    phi = [2 * pi * random() for _ in range(n)]

    return A, phi


def count(N, func):
    values = {}
    for i in range(N):
        values[i] = func(2 * pi / N * i)

    return values

def show_graph(g):
    fig, ax = plt.subplots()
    ax.plot(g)
    ax.grid()
    plt.show()
    plt.close(fig)


if rank == 0:
    values = count(N, cos)
    Re = DFT(N, x)
    comm.send(Re, dest=1, tag=11)
elif rank == 1:
    values = count(N, sin)
    Im = DFT(N, x, values)
    Re = comm.recv(source=0, tag=11)
    result = [sqrt(Re[i] + Im[i]) for i in range(len(Re))]
    show_graph(result)