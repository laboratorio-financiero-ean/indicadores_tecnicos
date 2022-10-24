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
 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data

desde   = '2022-01-01'   # Enero 1/2022
hasta   = '2022-09-30'   # Septiembre 30/2022

dataset = data.DataReader('GOOG', 'yahoo', desde, hasta)
print(dataset)

dataset_signal = pd.DataFrame(index=dataset.index)
dataset_signal['price'] = dataset['Adj Close']
dataset_signal['daily_difference'] = dataset_signal['price'].diff()
dataset_signal['signal'] = 0.0
dataset_signal['signal'][:] = np.where(dataset_signal['daily_difference'][:] > 0, 1.0, 0.0)
dataset_signal['positions'] = dataset_signal['signal'].diff()

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Precio en USD$')
#dibujamos la linea segun el precio
dataset_signal['price'].plot(ax=ax1, color='grey', lw=2.)

#dibujamos señal de soporte 
ax1.plot(dataset_signal.loc[dataset_signal.positions == -1.0].index,
         dataset_signal.price[dataset_signal.positions == -1.0],
         '^', markersize=5, color='g')

#dibujamos señal de resistencia 
ax1.plot(dataset_signal.loc[dataset_signal.positions == 1.0].index,
         dataset_signal.price[dataset_signal.positions == 1.0],
         'v', markersize=5, color='r')

plt.title('Comportamiento de soportes y resistencias de Google durante 2022' )
plt.show()