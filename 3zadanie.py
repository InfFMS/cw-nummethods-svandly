import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10**(-5))
R = 8.314
t2 = -130 + 273.15
V = np.linspace(b + (10**(-5)), 10**(-3), 1000)
P2 = (R*t2)/(V - b) - (a / V**2)


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

root1 = solve_ddd(def1, b + (10**(-5)), 10**(-4))
root2 = solve_ddd(def2, b + (10**(-4)), 6**(-4))



plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

ggg = 0
hhh = 0.01
saratov = 0

dlinaotrezok = np.linspace(root1, root2, 1000)
dlinaotrezoky = (R*t2)/(dlinaotrezok - b) - (a / dlinaotrezok**2)

jjj = root1
while jjj < root2:
    dlina1 = (((jjj + 0.0000000000000001) - jjj)**2 + ((((R*t2)/((dlinaotrezok+0.0000000000000001) - b) - (a / (dlinaotrezok+0.0000000000000001)**2)) - ((R*t2)/(dlinaotrezok - b) - (a / dlinaotrezok**2))))**2) ** 0.5
    saratov = saratov + dlina1
    jjj += 0.00000001


print(saratov)

