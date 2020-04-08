#zadanie 11
import cmath
import liczby_zepspolone.czesci_liczby_zespolonej
import liczby_zepspolone.dodawnie_odejmowanie
x=7
y=4
z=complex(x,y)
z2=complex(y,x)
print(liczby_zepspolone.czesci_liczby_zespolonej.czlz(z))
print(liczby_zepspolone.dodawnie_odejmowanie.sumazespolone(z,z2))
print(liczby_zepspolone.dodawnie_odejmowanie.roznicazespolone(z2,z))