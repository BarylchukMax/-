#1. Знайти матрицю 𝐴𝐵−𝐵𝐴:
import numpy as np

mat_a = np.array([[1, 2], [4, -1]])
mat_b = np.array([[2, -3], [-4, 1]])
c= mat_a.dot(mat_b)-mat_b.dot(mat_a)
print(c)
#2. Піднести матриці до степеня:
import numpy as np

mat_a = np.array([[-1, 2], [0, 1]])
c = np.linalg.matrix_power(mat_a, 2)
print(c)
#3. Знайти добуток матриць:
import numpy as np

mat_a = np.array([[3, 5], [6, -1]])
mat_b = np.array([[2, 1], [-3, 2]])
c= mat_a.dot(mat_b)
print(c)
#4. Обчислити визначники:
import numpy as np

mat_a = np.array([[2, 3, 4], [1, 0, 6],[7, 8, 9]])
c = np.linalg.det(mat_a)
print(c)
#5. Обчислити визначники.
import numpy as np

mat_a = np.array([[2, 3, 4, 1], [1, 2, 3, 4],[3, 4, 1, 2], [4, 1, 2, 3]])
c = np.linalg.det(mat_a)
print(c)
#6. Знайти обернену матрицю до матриць:
import numpy as np

mat_a = np.array([[1, 2, -3], [0, 1, 2],[0, 0, 1]])
c = np.linalg.inv(mat_a)
print(c)
#7. Визначити ранг матриці:
import numpy as np

mat_a = np.array([[1, 2, 3, 4], [3, -1, 2, 5],[1, 2, 3, 4], [1, 3, 4, 5]])
c = np.linalg.matrix_rank(mat_a)
print(c)
#8. Розв’язати систему лінійних рівнянь методом Крамера:
import numpy as np
mat_a = np.array([[3, -5, 3], [1, 2, 1], [2, 7, -1]])
mat_b = np.array([[1], [4], [8]])
def kramer(a, b):
    det = np.linalg.det(mat_a)
    print('Детермінант матриці = ', det)
    if (det != 0):
        xm = np.matrix(a)
        xm[:, 0] = b
        print('xm=', xm)
        ym = np.matrix(a)
        ym[:, 1] = b
        print('ym=', ym)

        zm = np.matrix(a)
        zm[:, 2] = b
        print('zm=', zm)

        x = np.linalg.det(xm) / det
        y = np.linalg.det(ym) / det
        z = np.linalg.det(zm) / det
        print('X = ', round(x, 5))
        print('Y=', round(y, 5))
        print('Z=', round(z, 5))
    else:
        print('Розв*язків нема')
kramer(mat_a, mat_b)
x = np.linalg.solve(mat_a, mat_b)
print('check X= ', x)
#9. Розв’язати систему лінійних рівнянь матричним методом:
import numpy as np
mat_a = np.array([[3, -5, 3], [1, 2, 1], [2, 7, -1]])
mat_b = np.array([[1], [4], [8]])
inv = np.linalg.inv(mat_a)
print(inv)
x = inv.dot(mat_b)
print('X=',x)
x = np.linalg.solve(mat_a, mat_b)
print('check', 'X=',x)
#Створіть прямокутну матрицю A з N рядками та стовпцями M з випадкових елементів.
# Знайдіть найнижче значення серед середніх значень для кожного рядка матриці.
import numpy as np
c=0
b=0
s=0
print('N: ')
x = int(input())
print('M: ')
y = int(input())
while c<y:
    a = np.array(np.random.randint(0, 9, x))
    print(a)
    for i in np.nditer(a):
        s=s+i
        b+=1
    print("Average: ", round(s/b, 2))
    s=0
    d=0
    c+=1