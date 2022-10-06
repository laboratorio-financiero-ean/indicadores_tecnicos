# Repositorio de algoritmos basado en indicadores técnicos  
#
# Universidad EAN, (2022)
# Laboratorio financiero
# Autor: Jose Rafael Morales Parra
# twitter.com/aDataScienceMan       
# linkedin.com/in/adatascienceman/ 
#
# Disclaimer legal.
# Abordamos los temas de análisis de mercados financieros desde el ámbito académico 
# En ningún caso podrá tomarse este contenido académico como consejos de inversión o asesoría financiera.
#
# Resultado: Analisis de la accion de Google, Identificación de soportes y resistencias
 

import numpy  as np
import pandas as pd
from pandas_datareader import data as pdr
import datetime as date
import matplotlib.pyplot as plt

simbolos=['SAN.MC', 'BBVA.MC']
desde   = '2022-01-01'   # Enero 1/2022
hasta   = '2022-09-30'   # Septiembre  30/2022

datos=pdr.get_data_yahoo(simbolos, start=desde, end=hasta)

print(datos)

datos.head()
%matplotlib inline
datos.Close.plot()

# Calculo de la media movil simple


def MA(df,n):
    MA = pd.Series(pd.Series.rolling(df['Close'], n).mean(), name = 'MA_' + str(n))   
    df = df.join(MA)
    return df

mm_10  = MA(datos,10) 
mm10.head() 
