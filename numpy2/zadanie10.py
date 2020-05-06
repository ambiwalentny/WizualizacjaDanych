import numpy as np
# zadanie 10
macierz = np.arange(81).reshape(9,9)
print(macierz)
a=macierz.reshape(1,81)
b=macierz.reshape(3,27)
c=macierz.reshape(27,3)
d=macierz.reshape(81,1)
print(a)
print(b)
print(c)
print(d)
#powyżej rozpisałem wszystkie możliwości, mamy 81 liczb w macierzy
#rozmiar macierzy musi być liczbą całkowitą, zatem wymmiarami mogą być tylko dzielniki liczby 81={1,3,27,81}