from time import time
from random import random
from math import sqrt, factorial

def gregory_leibniz():
    start = time()
    sign = 1
    pi = 0
    divider = 1
    while time() < start + 1:
        pi += sign * 4/divider
        divider += 2
        sign *= -1
    print(pi)

def monte_carlo():
    start = time()
    inside = 0
    outside = 0
    while time() < start + 1:
        if random()**2 + random()**2 < 1:
            inside += 1
        else:
            outside += 1
    print((inside / (outside + inside))*4)


def madhava():
    start = time()
    pi = 1
    divider = 3
    power = 1
    sign = -1
    while time() < start + 1:
        pi += sign/(divider * 3 ** power)
        power += 1
        divider += 2
        sign *= -1
    print(sqrt(12) * pi)

def riemann_2():
    start = time()
    pi = 0
    divider = 1
    while time() < start + 1:
        pi += 1 / (divider ** 2)
        divider += 1
    print(sqrt(pi*6))

def cudnov():
    start = time()
    sum = 0
    k = 0
    while time() < start + 1:
        sum += (factorial(6 * k) * (13591409 + 545140134 * k)) / ((factorial(3 * k)) * (factorial(k)**3) * ((- 640320) ** (3 * k)))
        k += 1
    print((426880 * sqrt(10005))/sum)

def BBP():
    start = time()
    pi = 0
    k = 0
    while time() < start + 1:
        pi += 1 / (16 ** k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
        k += 1
    print(pi)

def Brent_Salamin():
    start = time()
    a = 1
    b = 1/(sqrt(2))
    t = 0.25
    p = 1
    while time() < start + 0.0001:
        a1 = (a + b) / 2
        b1 = sqrt(a * b)
        t1 = t - p * (a - a1)**2
        p1 = 2 * p
        a = a1
        b = b1
        t = t1
        p = p1
    print(((a + b)**2) / (4 * t))

def Archimedes():
    start = time()
    a = 2 * sqrt(3)
    b = 3
    while time() < start + 1:
        a1 = (2 * a * b) / (a + b)
        b1 = sqrt(a1 * b)
        a = a1
        b = b1
    print(a, b)

#gregory_leibniz()
#monte_carlo()
#madhava()
#riemann_2()
#cudnov()
#BBP()
#Brent_Salamin()
Archimedes()