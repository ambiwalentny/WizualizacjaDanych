import numpy as np
#zadanie 2
a=np.array([[1,6,7],[6,3,9],[3,0,5]])
b=np.array([[1,5,8,2],[4,0,4,6],[3,2,4,8],[1,21,9,0]])
print(a)
print(b)
print(a.min(axis=0))
print(a.min(axis=1))

print(b.min(axis=0))
print(b.min(axis=1))
