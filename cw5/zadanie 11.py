# zadanie 11
def gen_fib():
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
g = gen_fib()
liczbyfibonacciego = [next(g) for _ in range(100)] 
print(liczbyfibonacciego)