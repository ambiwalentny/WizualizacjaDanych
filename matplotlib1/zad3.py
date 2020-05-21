import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a=np.arange(0,30,0.1)
x=np.sin(a)
y=np.cos(a)

plt.plot(x,'g',label='sin(x)')
plt.plot(y,'r',label='cos(x)')

plt.xlabel('x')
plt.ylabel('cos(x) i sin(x)')
plt.legend()
plt.show()