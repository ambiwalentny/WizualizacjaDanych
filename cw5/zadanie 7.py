# zadanie 7

class parzyste:
    def __init__(self, data):
        self.data = data
        self.max = len(data)
        self.index=-1;

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.max:
            raise StopIteration
        self.index = self.index + 1
        if self.index%2==0:
             return self.data[self.index]

lista=[1,2,3,4,5,6]
klasa= parzyste(lista)
it=iter(klasa)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) 
print(next(it))