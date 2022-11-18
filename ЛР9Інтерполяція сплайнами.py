#Інтерполяція сплайнами.
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
x = [0.5, 0.7, 1, 1.4, 1.9]
y = [1.83, 2.14, 1.46, 1.15, 3.28]
sp = UnivariateSpline(x, y)
xs = np.linspace(0, 2, 100)
plt.plot(x,y,'bd', xs, sp(xs), 'r')
plt.title("Spline Interpolation")
plt.ylabel("X")
plt.xlabel("Y")
plt.grid()
plt.show()