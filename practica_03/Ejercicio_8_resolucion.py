# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:40:17 2026

@author: Anoma
"""

# Ejercicio 8 resolucion
import numpy as np

data = np.load("C:/Users/Anoma/Desktop/labo_temp/guias/datos_practica03/datos_temp_bsas.npz")
print(list(data))
temperatura =  data['temp_array']
tiempo = data['time']
isobaricas = data['isobaricInhPa']
latitud = data['latitude']
longitud = data['longitude']
# item a)
temp_nivel = temperatura[0,1,:,3] # me quedo solo con la temperatura por nivel
temp_reticula = temperatura[:,:,2,3] #  tomo todos los valores de longitud y latitud
 # promedio para cada punto de la reticula usando funciones.
promedio_nivel = temp_nivel.mean() 
print(sum(temp_nivel) / len(temp_nivel)) # verificacion

promedio_reticula = temp_reticula.mean()

# usando ciclos.
suma_nivel = 0 # defino mi contador en cero
for k in range(4): #creo un ciclo para la dimension de niveles
    suma_nivel += temperatura[0,1,k,3]
promedio_nivel = suma_nivel / len(temperatura[0,1,:,3])
   
suma_reticula = 0 
for i in range(8):
    for j in range(14):
        suma_reticula += temperatura[i,j,2,3] # uso indexacion
promedio_reticula = suma_reticula / temperatura[:,:,2,3].size

# %% item b) Obtener la temperatura media anual en el perıodo analizado para cada nivel y cada punto deretıcula.

# tengo temperatura mensual del periodo 2000 - 2005 luego el total de meses:(( 2005 -2000)+1) *12 = 72 meses

temp_media_anual = temperatura.mean(axis=3) # al seleccionar axis 3 le estoy diciendo que promedie por dimiension del tiempo que correspondo al indice de tiempo 72 meses (indice 3). osea latitud (8) dimension 0 , longitud (14) dimension 1 , niveles (4) dimension (2) , tiempo (72) dimension 3 al usar mean(axis = 3) le digo que relize el promedio de la grilla de 8x14 y los niveles 4 del total de 72 meses seleecionados. y me devuelve un array de dimesion 3 y shape (forma: 8x14x4)

# %% item c) Utilizando la indexacion booleana seleccione el nivel de 850hPa e imprima por pantalla el promedio de temperatura sobre el dominio para cada anio.

nivel_850 = (isobaricas == 850)

temp_nivel_850 = temperatura[:,:, nivel_850,:]

temp_media_mensual = temp_nivel_850.mean(axis = (0,1,2)) # calcula la media aplastando las dimensiones axis = 0 (logitud) , axis =1 (latitud) ,  axis= 2 (nivel_850hpa)

temp_media_anual=temp_media_mensual.reshape(6,12).mean(axis=1) 
# convierto el array de 72 meses a (6,12) donde tengo en las filas 6 años y en las columnas 12 meses luego calculo la media por columna (dominio de cada año)

# %% item d) Utilizando la indexacion booleana seleccione el punto de retıcula mas cercano a la localidad de olavarrıa y obtenga la temperatura promedio para cada anio en el nivel de 1000hPa.

# olavarria coordenadas aproximadas lat -36.89384 long (360 -60.32319) = 299.68
# uso indexacion booleana para seleccinar la posicion de olavarria lon lat isobaricas (xyz posicon espacial)
olavarria_lat = (latitud == -36.75 ) 
olavarria_lon = (longitud == 299.25) 
nivel_1000 = (isobaricas == 1000) 

# uso indexacion selectiva para quedarme con los valores temporales para la (posicion)

temp_olavarria_1000 = temperatura[olavarria_lon,olavarria_lat,nivel_1000,:]
# rescalo los valores de temperatura de los 72 meses en la posicion seleccionada y calculo la media por columnas (12 meses el dominio de por año)
temp_promedio_anio = temp_olavarria_1000.reshape(6,12).mean(axis=1)


