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
# Resultado: Generacion de Medias moviles basado en el Análisis de la accion de Google
 

import datetime as date
import numpy  as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

#simbolos=['SAN.MC', 'BBVA.MC']
simbolos='GOOGL'
desde   = '2018-01-01'   # Enero 1/2022
hasta   = '2022-09-30'   # Septiembre  30/2022

datos=pdr.get_data_yahoo(simbolos, start = desde, end = hasta)
# Lo que recibimos en data es un Panel de Pandas, una matriz de dos dimensiones
datos.head()
print(datos)

# Dimensiones del dataFrame recibido 
print(datos.shape)

#%matplotlib inline# Impresion grafico 1
#datos.Close.plot()

    
def MediaMovil(df,periodos):
    MediaMovil = pd.Series(pd.Series.rolling(df['Close'], periodos).mean(), name='MA_' + str(periodos)) 
    df = df.join(MediaMovil)
    return df

#ma_9   = MediaMovil(datos,9)      # Acción del precio
ma_50  = MediaMovil(datos, 50)      # Reversiones
ma_200 = MediaMovil(ma_50, 200)     # Tendencia principal

ma_200.head()

df = ma_200[['Close','MA_50','MA_200']]

titulo = 'Acción de '+ simbolos +':: Gráfico de Medias moviles desde:'+ desde + ' hasta:'+ hasta 
df.plot(title = titulo , figsize = (16,8))    

