
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

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import mplfinance as mpf

desde   = dt.datetime(2022, 1, 1)   # Enero 1/2022
hasta   = dt.datetime(2022, 9, 30)  # Septiembre 30/2022
accion  = 'AAPL'
dataset = web.DataReader(accion, 'yahoo', desde , hasta )

print(dataset)

mpf.plot(dataset, type='candle', style='charles',
    title='Acción de APPLE - Comportamiento durante 2022', ylabel='Price ($)')

