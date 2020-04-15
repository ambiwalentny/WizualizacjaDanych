#zadanie 7
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.k=krok
    def idz_w_gore(self, ile_krokow):
        self.x=self.x
        self.y+=(ile_krokow*self.k)
    def idz_w_dol(self, ile_krokow):
        self.x=self.x
        self.y-=(ile_krokow*self.k)
    def idz_w_lewo(self, ile_krokow):
        self.x-=(ile_krokow*self.k)
        self.y=self.y
    def idz_w_prawo(self, ile_krokow):
        self.x+=(ile_krokow*self.k)
        self.y=self.y
    def pokaz_gdzie_jestes(self):
        print("Aktualne współrzędne Robaczka to: ", self.x, self.y)
    def __del__(self):
        print("Finalizer")