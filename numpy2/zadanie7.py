import numpy as np
# zadanie 7
macierzsin=np.array([[0*np.pi/180,30*np.pi/180,45*np.pi/180],[60*np.pi/180,90*np.pi/180,100*np.pi/180]])
a = np.sin(macierzsin)

macierzcos = np.array([[60*np.pi/180,45*np.pi/180,30*np.pi/180],[90*np.pi/180,0*np.pi/180,100*np.pi/180]])
b=np.cos(macierzcos)

c=a+b
print(c)