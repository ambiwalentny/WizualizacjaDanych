import sys
#zadanie1
lista=[]
for x in range(101):
    if (x%4==0):
        lista += [x]
plik=open("dane.txt","a+")
plik.writelines(str(lista))
plik.close()