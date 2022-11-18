#Задача Коші
#1) Метод Ейлера
import numpy as np
import matplotlib.pyplot as plt
import math
def f(x, y):
    return x+math.cos(y/math.sqrt(10))
a=0.6
b=1.6
h=0.1
x=np.arange(a,b+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=0.8
for i in range(n):
    y[i+1]=y[i]+h*f(x[i], y[i])
print("x:", x, "\ny:", np.round(y,4))
plt.plot(x,y,"s",x,y,"red")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
#2) Метод Ейлера-Коші
import numpy as np
import matplotlib.pyplot as plt
import math
def f(x, y):
    return x+math.sin(y/2.8)
a=1.4
b=2.4
h=0.1
x=np.arange(a,b+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=2.2
for i in range(n):
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i], y[i])))*h/2
print("x:", x, "\ny:", np.round(y,4))
plt.plot(x,y,"s",x,y,"red")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
