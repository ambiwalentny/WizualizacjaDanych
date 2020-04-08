#zadanie 10
# funckcja ma przyjmować 
# klucz to nazwa
# wartosc to ilosc
# zwracac sume ilosci

def ilosc(**rzeczy):
    suma=0
    for cos in rzeczy:
        suma+=rzeczy[cos]
    print(suma)

ilosc(chleb=2, maslo=4, szynka=6, mleko=3)
ilosc(myszk=4, klawitura=8, zegar=3, biurko=5, drukarka=6)