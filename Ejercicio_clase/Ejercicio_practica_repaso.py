# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np
np.random.seed(123)
muestra = np.random.normal(loc=25, scale=5, size=19716)

# item 1)
lat = np.arange(-38,-22.5,0.5)
long = np.arange(-64,-50.75,0.25)
muestra_array = muestra.reshape(12,len(lat),len(long)) 

# item 2 

mes_marzo = muestra_array[2,:,:] #(enero = 0 , febrero = 1 , marzo = 2 )

# 2 a)

maximo = mes_marzo.max()
minimo = mes_marzo.min()

fila_max , column_max = np.where(mes_marzo == maximo)

lat_max = lat[fila_max[0]]
long_max = long[column_max[0]]
 

fila_min , column_min = np.where(mes_marzo == minimo)

lat_min = lat[fila_min[0]]
long_min = long[column_min[0]]

# 2 b) 

diccionario = {"latitud":[lat_min,lat_max],"longitud":[long_min,long_max] , "temperaturas": [minimo , maximo]}

data_frame = pd.DataFrame(diccionario)
 gas


