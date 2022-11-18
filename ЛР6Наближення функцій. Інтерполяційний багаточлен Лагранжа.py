#Наближення функцій. Інтерполяційний багаточлен Лагранжа
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([-2, -1, 1, 2], dtype=float)
y = np.array([-26, -5, 1, 10], dtype=float)
def lagranz(x,y,t):
    r = 0
    for j in range(len(y)):
        p1 = 1; p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1; p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        r = r + y[j] * p1/p2
    return r
xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
plt.plot(x, y ,'o', xnew, ynew)
plt.grid(True)
plt.show()
f = lagrange(x, y)
fig = plt.figure(figsize = (10, 8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('check')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
