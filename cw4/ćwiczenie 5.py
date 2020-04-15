#zadanie 5
class CiagiArytmetyczne:
    def __init__(self, a1, an, n, roznica,):
        self.a1 = a1
        self.an = an
        self.n = n
        self.roznica = roznica
    
    def wyświetl_dane(self):
        print("Wartosc pierwszego wyrazu: ", self.a1, "wartosc wyrazu n-tego: ", self.an, "numer n-tego wyrazu: ", self.n, "wartość roznicy: ", self.roznica)
    
    def pobierz_elementy(self):
        self.a1=int(input('podaj pierwszy wyraz: '))
        self.an=int(input('podaj n-ty wyraz: '))
        self.n=int(input('podaj n: '))
        self.roznica=int(input('podaj roznice: '))

    def pobierz_parametry(self):
        self.a1=int(input('podaj pierwszy wyraz: '))
        self.roznica=int(input('podaj roznice: '))
        self.n=int(input("ile elementów wygenreować"))
        
    
    def policz_sume (self):
        return (self.a1+self.an)*0.5*self.n
    
    def policz_elementy(self):
        if(self.a1 != 0 and self.roznica != 0):
            for i in range(0,self.n):
                print(self.a1+(i-1)*self.roznica)
