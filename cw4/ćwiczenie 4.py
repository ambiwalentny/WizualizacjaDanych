#zadanie 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
       print(self.ilosc, self.jednostka_miary)
        
    def ile_kosztuje(self):
        cena = self.ilosc * self.cena_jed
        return "{} {}".format(self.nazwa_produktu,cena)