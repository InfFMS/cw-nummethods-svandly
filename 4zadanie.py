import matplotlib.pyplot as plt
import numpy as np

CONST = np.linspace(3664186.998, 3664186.998, 1000)
a = 0.1382
b = 3.19 * (10**(-5))
R = 8.314
t2 = -130 + 273.15
V = np.linspace(b + (10**(-5)), 10**(-3), 1000)

P2 = (R*t2)/(V - b) - (a / V**2)

x2 = V
y2 = P2


plt.plot(x2, y2)
plt.plot(x2, CONST)
plt.title("Зависимость давления от объема")
plt.xlabel("V")
plt.ylabel("P")
plt.show()

for i in ()