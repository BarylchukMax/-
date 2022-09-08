import numpy as np
import math
def f(x):
    return 6*pow(x,4)+4*pow(x,3)+pow(x,2)+x-10
a = 0
b = 1
e = 0.0001
def rec_dyhotomy(a, b, e):
    if abs(f(b) - f(a)) < e:
        print("Пошук кореня")
    m = (a + b) / 2
    if f(m) == 0 or abs(f(m)) < e:
        print("Корінь в точці", m)
    elif f(a) * f(m) < 0:
        rec_dyhotomy(a, m, e)
    else:
        rec_dyhotomy(m, b, e)
rec_dyhotomy(0, 1, 0.0001)