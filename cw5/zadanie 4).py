#zadanie 4
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)

inst1=Point()
inst2=Point(3,3)
inst3=Point()
inst4=Point(5,6)
inst1.update(1)
inst2.update(2)
inst3.update(7)
inst4.update(4)
print(inst1.counter)
print(inst2.counter)
print(inst3.counter)
print(inst4.counter)