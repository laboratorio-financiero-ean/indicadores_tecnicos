
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
# Resultado: Informacion de precio de acciones desde Yahoo finance 

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import mplfinance  as mpf
import matplotlib.pyplot as plt


desde  = dt.datetime(2022, 1, 1)   # Enero 1/2022
hasta  = dt.datetime(2022, 9, 30)  # Septiembre 30/2022

accion = 'AAPL'
datos  = web.DataReader(accion, 'yahoo', desde , hasta )
print(datos)

mpf.plot(datos, type='candle', style='charles',
   title='Gráfico de Velas - Acción de APPLE de Enero 1 a Septiembre 30 de 2022', ylabel='Precio en (USD$)')


