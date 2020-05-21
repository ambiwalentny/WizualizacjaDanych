import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = np.arange(1.,20,1.)
plt.plot(a,1/a,'g**',a,1/a,'g:',label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x[1,20]')

plt.legend()
plt.show()