# zadanie 9
def gnrtr(data):
    for i in range(0,len(data)):
        if i%2==0:
            yield data[i]

lista=[1,2,3,4,5,6]
gen = gnrtr(lista)
print(next(gen))
print(next(gen))
print(next(gen))