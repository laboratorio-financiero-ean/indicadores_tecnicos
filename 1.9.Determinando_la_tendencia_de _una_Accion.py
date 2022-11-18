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
# Resultado: Analizando la tendencia de una accion (stock) 
 

import datetime as date
import numpy    as np
import pandas   as pd
import statsmodels.api   as sm
import matplotlib.pyplot as plt
from   pandas_datareader import data as pdr
from   datetime   import date, datetime, timedelta
from   matplotlib import style

def calculo_de_tendencia(simbolo):
    #      Tenencia 2Años, 1Año, 1Semestre, 1Mes 
    temporalidades = (730, 365, 180, 30)
    for temporalidad in temporalidades:
        fecha = date.today() - timedelta(temporalidad)
        # Obtenemos dataset de datos o DataFrame
        df = pdr.get_data_yahoo(simbolo, fecha)
        
        # Preparamos o Limpiamos el DataFrame
        df = df[df['Volume']>0]
        df = df.drop(['Adj Close'], axis=1)
        
        #Aplicamos escala logaritmica al DataFrame para analizar en detalle la tendencia
        df = np.log(df)

        #Agregamos columna para el ajuste de regresion lineal para facilitar visualización de la linea de tendencia
        df['Regresion'] = sm.OLS(df['Close'],sm.add_constant(range(len(df.index)), prepend=True)).fit().fittedvalues
        
        #Preparamos el grafico
        plt.figure(figsize=(20,8))
        plt.scatter(df.index, df['Close'], color='blue')
        plt.plot(df['Regresion'], color='red', linewidth=2)
        plt.title('Análisis de tendencia de la acción:'+simbolo+' desde:'+str(fecha))
        plt.xlabel('Temporalidad:'+str(temporalidad)+' dias.')
        plt.ylabel('Precio del activo')        
        plt.show()


simbolo ='META'
#simbolo ='NFLX'    
#simbolo ='MCD'    
 
# Se calcula la tendencia en cuatro temporalidades
# 2 Años, 1 Año, 1 Semestre y 1 mes
# Por ello se generan 4 graficos, 1 por cada temporalidad 
calculo_de_tendencia(simbolo)
 



    
