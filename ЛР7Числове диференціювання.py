#Числове диференціювання
mx = [2.4,2.6,2.8,3.0,3.2,3.4]
my = [3.526,3.782,3.945,4.043,4.104,4.155]
h = mx[1] - mx[0]
m1 = []
m2 = []
m3 = []
m4 = []
for i in range(len(my)):
    m1.append(my[i] - my[i-1])
m1.pop (0)
for j in range(len(m1)):
    m2.append(m1[j] - m1[j-1])
m2.pop (0)
for k in range(len(m2)):
    m3.append(m2[k] - m2[k-1])
m3.pop (0)
for l in range(len(m3)):
    m4.append(m3[l] - m3[l-1])
m4.pop (0)
y1 = 1/ h * (m1[1] - m2[1]/ 2 + m3[1] /3 - m4[1]/4)
y2 = 1/ (h**2) * (m2[1] - m3[1] + 11/12*m4[1])
print ('Y` = ', round(y1, 3))
print ('Y`` = ', round(y2, 3))

