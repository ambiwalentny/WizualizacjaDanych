import numpy as np
#zadanie 11
wektor = np.arange(12)
macierz3x4 = wektor.reshape(3,4)
macierz4x3 = wektor.reshape(4,3)
macierz2x6 = wektor.reshape(2,6)

a=macierz3x4.ravel()
b=macierz4x3.ravel()
c=macierz2x6.ravel()
print(a)
print(b)
print(c)
#Tak, po spłaszaczeniu każda jest identyczna