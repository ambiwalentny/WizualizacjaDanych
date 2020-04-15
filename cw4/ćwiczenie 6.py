#zadanie 6
class slowa:
    def __init__(self,wyraz1,wyraz2):
        self.w1=wyraz1
        self.w2=wyraz2
    def sprawdz_czy_palindrom(self):
        i = len(self.w1)/2
        while i:
            i -= 1
            if self.w1[i] != self.w1[-i-1]: return False
        return True

    def sprawdz_czy_metagramy(self):
        if len(self.w1) != len(self.w2): return False
        cnt = 0
        while (*self.w1 and *self.w2):
            if (*self.w1 != *self.w2):
                cnt++
            self.w1++
            self.w2++
        if (cnt==1):
            return True
        else:
            return False
    
    def sprawdz_czy_anagramy(self):
        def swap(a, b):
            temp := a
            a := b
            b := temp
        if len(self.w1) != len(self.w2): return False
        for i in range (0,len(self.w1)-1):
            for j in range (0,len(self.w2)-1):
                if(self.w1[j]>self.w1[j+1]):
                    swap(self.w1(j),self.w1[j+1])
                if(self.w2[j]>self.w2[j+1]):
                    swap(self.w2(j),self.w2[j+1])
        return  self.w1=self.w2              

    def wyświetl_wyrazy(self):
        print(self.w1)
        print(self.w2)