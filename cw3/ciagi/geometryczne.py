import math
def nty_wyraz(a1,q,n): #jeśli znamy pierwszy wyraz
    an=a1*(q**(n-1))
    print(an)

def nty_wyraz2(ak,k,q,n):  #jeśli znamy k-ty wyraz
    an=ak*q**(n-k)
    print(an)

def suma(a1,q,n):
    if (q==1):
        wynik=a1*n
        print(wynik)
    else:
        sn=a1*((1-q**n)/(1-q))
        print(sn)