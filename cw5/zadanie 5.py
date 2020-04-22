# zadanie 5
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

q=isinstance(jozek, Osoba)
print(q)
w=isinstance(jozek, Pracownik)
print(w)
e=isinstance(jozek, Menadzer)
print(e)


r=isinstance(adrian, Osoba)
print(r)
t=isinstance(adrian, Pracownik)
print(t)
y=isinstance(adrian, Menadzer)
print(y)

u=issubclass(Menadzer,Pracownik)
print(u)
i=issubclass(Menadzer,Osoba)
print(i)
o=issubclass(Pracownik,Menadzer)
print(o)
p=issubclass(Pracownik,Osoba)
print(p)