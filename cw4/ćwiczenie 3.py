#zadanie3
with open("tekst.txt", "a+") as plik:
    plik.writelines("Ala ma kota")
    plik.writelines("Adam ma psa")
    plik.writelines("Kasia ma kanarka")
    plik.writelines("Zbigniew ma rybki")

with open("tekst.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")