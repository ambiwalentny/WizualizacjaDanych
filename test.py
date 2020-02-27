# liczba= 0
# liczba="0"
# liczba= 0.0
# kazda zmienna jest obiektem
# object klasa bazowa

# print(liczba + liczba)
# print ("Ala")

# alt+shift+strzalka gora (lub dol) kopiowanie zaznczonej linjki powyzej (lub ponizej)
# ctrl+/ zakomentowanie zaznaczonej lini
# konwencja co do zmienny ' = ' lepsze niz '='
# konwencja nazw podlogi przy dlugich nazwach 'dluga_nazwa_zmiennej

# def funkcja():
#     print(liczba + liczba)
#     print ("Ala")
#     print(liczba)

# print("Ala ma" + "5 lat")
# print(0 - 1)
# print(2 / 1)
# print(2 * 1)
# print(2 // 1) # dzielnie bez reszty
# print(2 ** 1) # potegowanie
# print(0 % 1)  # dzielenie modulo
# print(5)
# print("Ala ma 5 lat")
# print("Ala ma" + 5 + "lat") # błąd nieprzekonweruje typu
# print("Ala ma" + str(5) + "lat") # konwersja (rzutowanie) (zmiana typu)
# int("100")
# formtatowanie wyjścia
# print("Ala ma { } lat".format(5))

# print("Ala ma {1} lat a Marta {0}".format(5, 10))
# jeżeli puste to po kolei jeśli zapisane to według indeksów (w pythonie indekoswanie od 0)

# f-string (od Python 3.6)
# wiek = 7
# print(f"Ala ma {wiek} lat")

# imie = "Małgorzata"
# print(imie[4])
# # imie[4] = "a" błąd
imie="Adam"
# print(imie.lower())
# imie = imie.lower()
# print(imie)
# "Wojtek".lower().lstrip().rsplit() # mechanizm łańcuchowania wykonywanie funckji w jednej lini zmiast weilu linijek kodu 


# ~~~~~~~~~~~~~~~~~~listy~~~~~~~~~~~~~~~~~~~~~~~~~~
lista  = []
# print(type(lista)) # zwraca informację o typie zmiennej~
# print(type("Ala"))
# print(type(5))

# <class 'list'>
# <class 'str'>
# <class 'int'>

lista.append(5)
lista.insert(0, 6)

lista2 = [1, 2, 3, 4, 5]
lista2[3]
lista3 = lista2+lista2
print(lista3)
lista4 = [1, "ala", imie, 3.4, [1, 3]] 
print(lista4[4])

macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(macierz[1][1]) # odowłanie do konkretnego miejsca miecierz przy cyzm [wiersz][kolumna]

#~~~~~~~~~~~~~~~słownik~~~~~~~~~~~~~~~~~
slownik = {}
print(type(slownik))
# <class 'dict'>
slownik["imie"] = "Marek"
print(slownik)
slownik2 = {
    'imie': 'Marek',
    'wiek': 25,
    'wzrost': 175}

print(slownik2)
print(slownik2.keys()) # zwraca klucze
print(slownik2.values()) # zwraca wartosci
print(slownik2.items()) # zwraca krotki (klucz i jego wartosc)

# ~~~~~~~~~~~~~~~~~~~~importy~~~~~~~~~~~~~~~~~~~~~~~~~
#nie zalecane
from math import * # skąd zaimportować z pakietu (gwiazdka jeśli wszystko)
from math import pow
#zalecane
import math as m #jeśli chcemy się odwołać do czegoś a mth to musismy użyc aliasa m.funkcja
print(m.pow(2, 2))