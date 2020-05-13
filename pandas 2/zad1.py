import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

x = pd.read_excel('imiona.xlsx')
df = pd.DataFrame(x,columns=['Rok','Imie','Liczba','Plec'])
print(df)

grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot()
wykres.set_ylabel("Liczba urodzen")
wykres.set_xlabel('Rok')
wykres.legend()
plt.title('Liczba narodzin')
plt.show()