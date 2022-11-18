#Метод найменших квадратів
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.log(x+1)-np.sin(x)
x = np.array ([i*0.1 for i in range(1, 11)])
y = np.array([f(x)])
print ('x=',x)
print ('y=',y)
m_x = np.mean(x)
m_y = np.mean(y)
m_x2 = np.mean(pow(x, 2))
m_xy = np.mean (x*y)
print('Mean x=', round(m_x, 4), '\n', 'Mean y=', round(m_y, 4), '\n', 'Mean xy=', round(m_xy, 4), '\n', 'Mean x2=', round(m_x2, 4))
a1 = (m_xy - m_x*m_y)/(m_x2-pow(m_x, 2))
a0 = m_y - (a1 * m_x)
print('Coefficients', 'a0=', round(a0, 3), 'a1=', round(a1, 3))
plt.plot(x, a0*x + a1, 'b', label='Fitted line')
plt.scatter(x, y, label='Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
