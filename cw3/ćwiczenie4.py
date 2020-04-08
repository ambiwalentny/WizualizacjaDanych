#zadanie 4
#y=ax+b
def monotonicznosc(a, b):
    if (a > 0):
        print("funkcja jest rosnaca")
    elif(a == 0):
        print("funkcja jest stala")
    else:
        print("funkcja jest malejaca")

print(monotonicznosc(-2,1))
print(monotonicznosc(0,3))
print(monotonicznosc(5,7))