import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10**(-5))
R = 8.314
t1 = -140 + 273.15
t2 = -130 + 273.15
t3 = -120 + 273.15
t4 = -110 + 273.15
t5 = -100 + 273.15
V = np.linspace(b + (10**(-5)), 10**(-3), 1000)


P1 = (R*t1)/(V - b) - (a / V**2)
P2 = (R*t2)/(V - b) - (a / V**2)
P3 = (R*t3)/(V - b) - (a / V**2)
P4 = (R*t4)/(V - b) - (a / V**2)
P5 = (R*t5)/(V - b) - (a / V**2)

x1 = V
y1 = P1


x2 = V
y2 = P2


x3 = V
y3 = P3


x4 = V
y4 = P4


x5 = V
y5 = P5

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4, color = "red")
plt.plot(x5, y5)
plt.title("Зависимость давления от объема при разном t")
plt.xlabel("V")
plt.ylabel("P")
plt.show()