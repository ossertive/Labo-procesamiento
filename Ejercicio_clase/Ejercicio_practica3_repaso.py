# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np
np.random.seed(123)
# un array de 1d de tamañao 19716
muestra = np.random.normal(loc=25, scale=5, size=19716)

# item 1)
# creo para latitud y longitud un array de 1d donde  toma inicio fin y paso.
lat = np.arange(-38,-22.5,0.5) 
long = np.arange(-64,-50.75,0.25)
# con reshape redimensiono al array original a un array de 3d con (12,31,53).
muestra_array = muestra.reshape(12,len(lat),len(long)) 

# item 2 

mes_marzo = muestra_array[2,:,:] #(enero = 0 , febrero = 1 , marzo = 2 )

# 2 a) 
# identifico los valores maximos y minimos del mes marzo.
maximo = mes_marzo.max()
minimo = mes_marzo.min()

# Identifico la fila y columna donde la temperatura del mes de marzo es maxima

(fila_max , column_max) = np.where(mes_marzo == maximo)

# selecciono el punto (lat - lon) donde la temperatura del mez marzo es maxima.

lat_max = lat[fila_max[0]]
long_max = long[column_max[0]]
 
# idem para el minimo

fila_min , column_min = np.where(mes_marzo == minimo)

lat_min = lat[fila_min[0]]
long_min = long[column_min[0]]

# 2 b) creo un diccionario con las claves latitud donde sus valores son las lat_min,max , longitud donde sus valores son long_min, long_max y la clave temperatura donde sus valores son los min y maximo respectivamente.

diccionario = {"latitud":[lat_min,lat_max],"longitud":[long_min,long_max] , "temperaturas": [np.round(minimo,1) , np.round(maximo,1)]}

# a partir del diccionario creo el dataframe

data_frame = pd.DataFrame(diccionario)

# Item 3 Calcular el campo medio para la primavera (SON) septiembre - octubre - noviembre.
# uso slicing para sep-oct-nov [8-9-10] y como piden campo medio le calculo la media por filas para los tres meses.
campo_primavera = muestra_array[8:11,:,:].mean(axis=0)

desvio_estandar = np.std(campo_primavera)
mediana = np.median(campo_primavera)

diccionario_campo = {"desvio":[desvio_estandar], "mediana":[mediana]}

# Item 4
meses = [1,7,12]

def temp_medias(lista_meses ,datos_array):
   resultados = [] # creo una lista vacia para guardar las temperaturas calculadas.
   
   for mes in lista_meses:
       # opcional: verificacion de los meses del año
       if  mes< 1 or mes >12 :
           print(f"Error : el mes {mes} ingresado no es un valido para el año calendario")
           continue # si la condicion es falsa continua
       indices = mes-1 # pasar los meses del calendario a indices.
       
       temp_media = np.round(datos_array[indices,:,:].mean(),2)
       resultados.append(temp_media) # agrego a la lista vacia las temperaturas medias calculadas
   return resultados
# prueba:
prueba = temp_medias(meses,muestra_array)
print("Las temperaturas medias para los meses enero,julio y diciembre:",prueba)
