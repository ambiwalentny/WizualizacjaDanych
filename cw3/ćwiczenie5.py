#zadanie 5
#y=a1x+b1 y=a2x+b2
def czy_rownolegle_czy_prostopadle(a1, b1, a2, b2):
    if(a1==a2):
        print("proste sa rownologle")
    elif(a1*a2==-1):
        print("proste są prostopadle")
    else:
        print("proste nie są ani prostopadle ani rownolegle")

print(czy_rownolegle_czy_prostopadle(1,2,-1,3))
print(czy_rownolegle_czy_prostopadle(1,8,1,3))
print(czy_rownolegle_czy_prostopadle(12,4,-6,21))