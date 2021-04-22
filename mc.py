import math as m
# import random
import numpy as np
import matplotlib.pyplot as plt

count = 0
n = 1000000
xs = []
ys = []

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

for i in range(n):
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)
    xs.append(x)
    ys.append(y)
    if x*x + y*y <1:
        count += 1

eX = np.linspace(0,5,100)
eY = [m.pow(m.e, -x*x/2) for x in eX]

for i in range(n):
    x = np.random.uniform(0,5)
    y = np.random.uniform(0,1)
    xs.append(x)
    ys.append(y)
    if y<m.pow(m.e, -x*x/2):
        count += 1

print(count/n*10)
print(np.sqrt(2*m.pi))

# plt.plot(x1, x2)
# plt.axis('scaled')
# plt.scatter(xs, ys, c='green')
# plt.plot(eX, eY)
# plt.show()
