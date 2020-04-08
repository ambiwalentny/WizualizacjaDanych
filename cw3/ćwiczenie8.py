#zadanie 8
def suma_ciag(a1=1, r=1, ile_elementów=10):
    suma=((2*a1+(ile_elementów-1)*r)/2)*ile_elementów
    print(suma)

print(suma_ciag())
print(suma_ciag(12,32,24))