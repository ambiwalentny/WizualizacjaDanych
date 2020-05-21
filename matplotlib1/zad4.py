import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


m=np.arange(0,30,0.1)

y=np.sin(m)+2
x=np.sin(m-3.15)

sin=plt.plot(y,label='sin(x)+2')
sinplus2=plt.plot(x,'tab:orange',label='sin(x)')
plt.legend(bbox_to_anchor=(0, 1),
       bbox_transform=plt.gcf().transFigure)
          

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legendloc = ["center right"]

plt.legend()
plt.show()

plt.legend()
plt.show()