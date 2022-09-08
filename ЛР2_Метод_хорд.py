from scipy.misc import derivative
import numpy as np
import math

def f(x):
  return 6*pow(x,4)+4*pow(x,3)+pow(x,2)+x-10
a = 0
b = 1
e = 0.0001
def hord (a, b, e):
    if (f(a)*derivative(f,a,n = 2)>0):
      x0 = a
      xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * f(xi) / f((xi) - f(x0))
    while (abs(f(xi_1) - f(xi)) > e):
      xi = xi_1
      xi_1 = xi-(xi - x0) * f(xi) / (f(xi) - f(x0))
    print(f'Корень в точці x = ', xi_1)
hord(0, 1, 0.0001)
