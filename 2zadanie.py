import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10**(-5))
R = 8.314
t2 = -130 + 273.15
V = np.linspace(b + (10**(-5)), 10**(-3), 1000)
V566 = np.linspace(b + (10**(-5)), 10**(-4), 1000)
P345 = (R*t2)/(V566 - b) - (a / V566**2)
V566345 = np.linspace(b + (11**(-4)), 6**(-4), 1000)
P345435 = (R*t2)/(V566345 - b) - (a / V566345**2)

def def1(x):
    return (R * t2) / (x - b) - (a / x ** 2) - 3020567.824359551

def def2(x):
    return (R * t2) / (x - b) - (a / x ** 2) - 3960852.140363344

def solve_ddd(f, a, b, eps = 0.0000000001):
    while (b-a)/2 >= eps:
        c = (a + b)/2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c

root = [solve_ddd(def1, b + (10**(-5)), 10**(-4)), solve_ddd(def2, b + (10**(-4)), 6**(-4))]

print(root)


P2 = (R*t2)/(V - b) - (a / V**2)
x3 = V566
x2 = V
y2 = P2
y3 = P345
x4 = V566345
y4 = P345435


plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.title("Зависимость давления от объема")
plt.xlabel("V")
plt.ylabel("P")
plt.show()

local_min = 0
local_max = 0

# for i in P2:
#     if i < i+1:
#         local_min = i
#         break



V2 = np.linspace(local_min, 10**(-3), 1000)
# P = (R*t2)/(V2 - b) - (a / V2**2)

V5656 = np.linspace(b + (10**(-5)), 10**(-4), 1000)

P34 = (R*t2)/(V5656 - b) - (a / V5656**2)

min = np.min(P34)
argnin = np.argmin(P34)

max = np.max(P345435)
argmain = np.argmax(P345435)

# for i in P:
#     if i > i+1:
#         local_max = i
#         break

print(min, argnin, max, argmain)


# linia = np.linspace(3020567.824359551, 3020567.824359551, 1000)
