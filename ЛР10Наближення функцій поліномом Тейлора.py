#Наближення функцій поліномом Тейлора
import sympy as sp
def taylor(x):
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    print('d` = ', d1, 'd`` = ', d2, 'd``` = ', d3)
    y = 0
    y += f + d1 * x + d2 * (x - 0) ** 2 / 2 + d3 * (x - 0) ** 3 / 6
    print('y = ', y)
    return y
x = sp.symbols('x')
f = sp.ln(x) - sp.sin(x)
tay_x = taylor(x)
sp.plot(tay_x, f, (x, -2, 4))
