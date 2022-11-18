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
# Resultado: Analisis MACD - Moving Average Convergence Divergence con la accion de Google
 

import datetime as date
import numpy    as np
import pandas   as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from matplotlib        import gridspec


simbolo='GOOGL'

#desde   = date.datetime(2021,1,1)     # Enero 1/2021
#hasta   = date.datetime(2022,10,31)   # Octubre 31/2022

desde   = '2021-01-01'   # Enero 1/2022
hasta   = '2022-10-31'   # Octubre 31/2022

# Obtenemos datos historicos desde yahoofinance, guardamos el dataFrame.. llamo df
df=pdr.get_data_yahoo(simbolo, start = desde, end = hasta)

# Lo que recibimos en data es un Panel de Pandas, una matriz de dos dimensiones
df.head()
df.Close.plot()
print(df)

#Definimos la funcion que calcula el indicador MACD
def genera_MACD(df, n_fast, n_slow):
    nomvar = str(n_fast)+ '_' + str(n_slow)
    EMAfast = pd.Series(pd.Series.ewm(df['Close'], span = n_fast, min_periods = n_slow -1).mean())
    EMAslow = pd.Series(pd.Series.ewm(df['Close'], span = n_slow, min_periods = n_slow -1).mean()) 

    MACD     = pd.Series(EMAfast - EMAslow, name = "MACD_" + str(n_fast) + '_' + str(n_slow))
    MACDsign = pd.Series(pd.Series.ewm(MACD, span = 9,  min_periods = 8).mean(), name = 'MACDsign_' + nomvar)
    MACDdiff = pd.Series(MACD - MACDsign, name = 'MACDdiff_' + nomvar)
    
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff) 

    return df

df = genera_MACD(df,12,26)
df.tail()
x = range(len(df.index))
print(x)


grafico = plt.figure(figsize = (16,8))
gs  = gridspec.GridSpec(2,1, figure = grafico, height_ratios=[3,1])


ax1 = plt.subplot(gs[0])
plt.plot(x, df.Close)
plt.grid(True)
plt.title('Análisis de la acción:'+simbolo)
plt.ylabel('Precio')  

ax2 = plt.subplot(gs[1], sharex=ax1)
plt.title('Indicador MACD - Moving Average Convergence Divergence')
plt.plot(x, df.MACD_12_26,     color = 'b')  # MACD 12 y 26 - Azul
plt.plot(x, df.MACDsign_12_26, color = 'y')  # La señal MACD - Amarilla
plt.bar (x, df.MACDdiff_12_26, color = 'k')  # Dato de diferencia - Negra
plt.xlabel('Dias tomados en cuenta desde:'+str(desde)+ ' hasta:'+str(hasta))
plt.ylabel('Nivel')  
plt.legend()
plt.grid(True)
plt.show()


        
