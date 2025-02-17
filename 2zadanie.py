import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10**(-5))
R = 8.314
t2 = -130 + 273.15
V = np.linspace(b + (10**(-5)), 10**(-3), 1000)



P2 = (R*t2)/(V - b) - (a / V**2)

x2 = V
y2 = P2


plt.plot(x2, y2)

plt.title("Зависимость давления от объема")
plt.xlabel("V")
plt.ylabel("P")
plt.show()

local_min = 0
local_max = 0

for i in P2:
    if i < i+1:
        local_min = i
        break


V2 = np.linspace(local_min, 10**(-3), 1000)
P = (R*t2)/(V2 - b) - (a / V2**2)

for i in P:
    if i > i+1:
        local_max = i
        break

print(local_min, local_max)