# zadanie 6
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


imie="Maciej"
klasa= Wspak (imie)
it=iter(klasa)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
###################
lista=[1,2,3,4,5]
klasa= Wspak (lista)
it=iter(klasa)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
######################
krotka = ("zeszyt", "laptop", "dlugopis", "myszka")
klasa= Wspak (krotka)
it=iter(klasa)
print(next(it))
print(next(it))
print(next(it))
print(next(it))