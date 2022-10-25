# Repositorio de algoritmos basado en indicadores técnicos  
#
# Universidad EAN, (2022)
# Laboratorio financiero
# Autor: Jose Rafael Morales Parra
# twitter.com/aDataScienceMan           # linkedin.com/in/adatascienceman/ 
#
# Disclaimer legal.
# Abordamos los temas de análisis de mercados financieros desde el ámbito académico 
# En ningún caso podrá tomarse este contenido académico como consejos de inversión o asesoría financiera.
#
# Resultado: Analisis de Indice de fuerza relativa (RSI) de la Acción de: Google 


import datetime as date
import numpy  as np
import pandas as pd
from   pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from   matplotlib import gridspec


simbolo='GOOGL'
desde   = '2022-01-01'   # Enero 1/2022
hasta   = '2022-09-30'   # Septiembre  30/2022

datos = pdr.get_data_yahoo(simbolo, start = desde, end = hasta)
# Lo que recibimos en data es un Panel de Pandas, una matriz de dos dimensiones
datos.head()

#%matplotlib inline 
datos.Close.plot()

    
def calcular_RSI(df, n):
    i = 0
    UpI = [0]
    DoI = [0]
    df = df.reset_index()
    while i + 1 <= df.index[-1]:
        UpMove = df._get_value(i+1, 'High')  - df._get_value(i, 'High')  
        DoMove = df._get_value( i  , 'Low' ) - df._get_value(i+1, 'Low') 

        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else: UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
             DoD = DoMove
        else: DoD = 0
        DoI.append(DoD)
        i = i + 1

    UpI   = pd.Series(UpI)
    DoI   = pd.Series(DoI)     
    PosDI = pd.Series(pd.Series.ewm(UpI, span = n, min_periods = n-1).mean())
    NegDI = pd.Series(pd.Series.ewm(DoI, span = n, min_periods = n-1).mean())  
    RSI   = pd.Series(PosDI / ( PosDI + NegDI), name = 'RSI_'+str(n))
    df    = df.join(RSI)
    df.set_index('Date', inplace=True)
    
    return df
   

df = calcular_RSI(datos,14) # Periodos
print(df)
df.tail()

x = range( len( df.index))

fig = plt.figure(figsize= (16,10))
gs  = gridspec.GridSpec(2, 1, figure = fig, height_ratios=[3, 1]) 

ax1 = plt.subplot(gs[0])
plt.plot(x,df.Close)
plt.grid(True)
plt.title('Indice de fuerza relativa (RSI) de la Acción de: '+ simbolo)

ax2=plt.subplot(gs[1], sharex=ax1)
plt.plot(x, df.RSI_14, color = 'r')
plt.axhline(y= 0.7, color= 'k', linestyle= '--')
plt.axhline(y= 0.3, color= 'k', linestyle= '--')
plt.legend()
plt.grid(True)
plt.show()




