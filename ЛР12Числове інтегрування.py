#Числове інтегрування
#1) методом прямокутників за умови п=10;
from scipy import integrate
import math
def f1(x):
    return 1/math.sqrt(2*x*x + 1.3)
def l(f1, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum = sum + f1(a + i * h)
    return sum * h
v, err = integrate.quad(f1, 1, 2)
eps = 0.0001
if abs(l(f1, 1, 2, 10) - l(f1, 1, 2, 10))/3. <=eps:
    print("Left rectangle:", round(l(f1, 1, 2, 10), 4))
def r(f1,a,b,n):
    h = (b - a) / n
    sum = 0
    for i in range(1, n + 1):
        sum = sum + f1(a + i * h)
    return sum * h
print("Right rectangle:", round(r(f1, 1, 2, 10), 4))
def m(f1, a, b, n):
    h = 0.1
    sum = 0
    for i in range(0, n):
        sum = sum + f1(a+i*h+0.05)
    return sum * h
print("Middle rectangle:", round(m(f1, 1, 2, 10), 4))
print("Check:", round(v, 4))
#2) методом Сімпсона за умови п=8;
from scipy import integrate
import math
def f(x):
    return math.tan(x*x)/(x**2+1)
def simpson(a, b, n):
    h = (b - a) / n
    int = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            int += 2 * f(k)
        else:
            int += 4 * f(k)
    int *= h / 3
    return int
eps = 0.0001
if abs(simpson(0.2, 1, 8) - simpson(0.2, 1, 8))/ 15. <= eps:
    print("Simpsone method:", round(simpson(0.2, 1, 8), 4))
v, err = integrate.quad(f, 0.2, 1)
print("Check:", round(v, 4))
#3) методом трапецій за умови п=20;
import math
from scipy import integrate
def f1(x):
    return 1/math.sqrt(2*x*x + 1.6)
def trap(f1, a, b, n):
    h = (b-a)/n
    sum = 0.5*(f1(a)+f1(b))
    for i in range(1, n):
        sum += f1(a+i*h)
    return sum*h
v, err = integrate.quad(f1, 0.15, 0.5)
eps = 0.0001
if abs(trap(f1, 0.15, 0.5, 20) - trap (f1, 0.15, 0.5, 20))/3. <= eps:
    print("Trapeze method:", round(trap(f1, 0.15, 0.5, 20), 4))
print("Check:", round(v, 4))

