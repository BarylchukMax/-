#Інтерполяційний багаточлен Ньютона
import numpy as np
from math import factorial
import matplotlib.pyplot as plt
x = [0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65]
y = [0.8607, 0.8187, 0.7788, 0.7408, 0.7046, 0.6703, 0.6376, 0.6065, 0.57690, 0.5488, 0.5220]
h = x[1] - x[0]
x1 = 0.151
x2 = 0.505
q = (x1 - x[0])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j = j-1
        return n(mas, j)
s1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s2 = q*(q-1)*(q-2)*n(y, 3)[0]/factorial(3)
s3 = q*(q-1)*(q-2)*(q-3)*n(y, 4)[0]/factorial(4)
s4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y, 5)[0]/factorial(5)
n1 = s1 + s2 + s3 + s4
print ('First interpolation formula: F(', x1, ') = ', round(n1,5))
q1 = (x2-x[-1])/h
t1 = y[5] + q1*n(y, 1)[4]+q1*(q1+1)*n(y, 2)[3]/factorial(2)
t2 = q1*(q1+1)*(q1+2)*n(y, 3)[2]/factorial(3)
t3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y, 4)[1]/factorial(4)
t4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y, 4)[1]/factorial(5)
n2 =  t1+t2+t3+t4
print ('Second interpolation formula: F(', x2, ') = ', round(n2,5))
x_1=np.linspace(np.min(x), np.max(x))
y_1=np.linspace(np.min(y), np.max(y))
plt.plot(x, y, "o", x_1, y_1)
plt.title('Interpolation function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


