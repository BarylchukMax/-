import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return 6*pow(x,4)+4*pow(x,3)+pow(x,2)+x-10
a = 0
b = -1
e = 0.0001
def nuton(a,b,e):
    df2 = derivative(f, b, n=2)
    if (f(b) * df2 > 0):
        xi = b
    else:
        xi = a
    df = derivative(f, xi, n=1)
    xi_1 = xi - f(xi) / df
    while (abs(xi_1 - xi) > e):
        xi = xi_1
    xi_1 = xi - f(xi) / df
    return print('Корінь в точці x = ', xi_1)
nuton (0,1,000.1)