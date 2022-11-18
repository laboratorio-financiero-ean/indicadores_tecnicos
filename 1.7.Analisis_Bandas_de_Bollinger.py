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
# Resultado: Analisis tecnico con Bandas de Bollinger de la Acción de: Google 
 

import datetime as date
import numpy  as np
import pandas as pd
from   pandas_datareader import data as pdr

simbolo='GOOGL'
desde   = '2022-01-01'   # Enero 1/2022
hasta   = '2022-10-31'   # Octubre 31/2022


datos = pdr.get_data_yahoo(simbolo, start = desde, end = hasta)
# Lo que recibimos en data es un Panel de Pandas, una matriz de dos dimensiones
datos.head()

#print(datos)
#%matplotlib inline 
#datos.Close.plot()


def generaBandas(df, n):
    mediaMovil  = pd.Series(pd.Series.rolling(df['Close'], n).mean())
    mediaDesviacionEstandar = pd.Series(pd.Series.rolling(df['Close'], n).std())
    b1 = mediaMovil + (mediaDesviacionEstandar*2)
#    bandaSuperior = pd.Series(b1, name = 'BollingerB_'+ str(n))
    bandaSuperior = pd.Series(b1, name = 'Banda Superior_'+ str(n))
    df = df.join(bandaSuperior)
    
    bandaMediaMovil = pd.Series(mediaMovil, name = 'Banda Media_'+ str(n))
    df = df.join(bandaMediaMovil)
    
    b2 = mediaMovil - (mediaDesviacionEstandar*2)
    bandaInferior = pd.Series(b2, name = 'Banda Inferior_'+ str(n))
    df = df.join(bandaInferior)
    
    return df             # Retorna el dataFrame


df = generaBandas(datos, 20)

df2 = df[['Close', 'Banda Superior_20', 'Banda Inferior_20', 'Banda Media_20']]
titulo  = 'Acción de '+ simbolo +':: Análisis con Bandas de Bollinger '
xTitulo = 'Movimiento desde '+desde+ ' hasta:'+hasta
yTitulo = 'Valor de la acción'

seriesTitle=['Title1', 'Title2', 'Title3', 'Title4']

df2.plot(title = titulo ,xlabel = xTitulo, ylabel = yTitulo, figsize = (16,10))


