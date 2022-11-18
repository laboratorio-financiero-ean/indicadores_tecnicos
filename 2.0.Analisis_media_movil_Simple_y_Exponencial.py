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
# Resultado: Generacion y Comparativa de Media movil SIMPLE y Media movil EXPONENCIAL
 

import datetime as date
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

 
simbolo ='GOOGL'
desde   = '2020-01-01'   # Enero 1/2022
hasta   = '2022-10-31'   # Octubre 31/2022

data=pdr.get_data_yahoo(simbolo, start = desde, end = hasta)
# Lo que recibimos en data es un Panel de Pandas, una matriz de dos dimensiones

# Dimensiones del dataFrame recibido 
print(data.shape)

#%matplotlib inline# Impresion grafico 1
#datos.Close.plot()


def MediaMovil(df,periodos):
    #Proporciona cálculos de ventana móvil.        rolling
    MediaMovil = pd.Series(pd.Series.rolling(df['Close'], periodos).mean(), name='MA_' + str(periodos)) 
    df = df.join(MediaMovil)
    return df

def ExponentialMediaMovil(df,periodos):
    #Proporciona funciones ponderadas exponencialmente.        ewm
    ExpoMediaMovil = pd.Series(pd.Series.ewm(df['Close'], span = periodos,  min_periods = periodos-1, adjust = False).mean(), name = 'EMA_' + str(periodos))
    df = df.join(ExpoMediaMovil)
    return df

    




df = ExponentialMediaMovil(data,50)  
df2= MediaMovil(df, 50)       
df2= df2[['Close','MA_50','EMA_50']] 

titulo = 'Acción de '+ simbolo +':: Análisis con Media movil Simple y Exponencial, desde :'+ desde + ' hasta:'+ hasta 
plt.xlabel('Dias tomados en cuenta desde:'+str(desde)+ ' hasta:'+str(hasta))

df2.plot(title = titulo , figsize = (16,8))    
