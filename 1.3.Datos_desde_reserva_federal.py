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
# Resultado: Informacion del producto interno bruto desde la Reserva Federal USA 
# https://fred.stlouisfed.org/series/GDP

import pandas as pd
import pandas_datareader.data as web
import datetime as dt

desde   = dt.datetime(2020, 1, 1)   # Enero 1/2022
hasta   = dt.datetime(2022, 9, 30)  # Septiembre 30/2022

pd.set_option('display.max_rows', 36)
indicador  = 'GDP'
dataset = web.DataReader(indicador, 'fred', desde , hasta )
print(dataset)

