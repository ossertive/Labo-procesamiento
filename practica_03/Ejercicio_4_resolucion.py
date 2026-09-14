# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:12:52 2026

@author: Anoma
"""

# Resolución ejercicio 4
# a)
serie  = [ 25 , 20 ,18 ,22 , 27 , 31 , 32 , 28 ] # series de temperaturas medidas en ° C
hora = [0,3,6,9,12,15,18,21] # Intervalos medidos cada 3 horas.

temperatura_max = max(serie) 

posicion = serie.index(temperatura_max) # de la serie de temp buscame el indice donde se encuntra el max de temperatura.

hora_max = hora[posicion] # indexacion digo de la lista hora dame la que se ecuentra en el posicion 6 que corresponde al max de temperatura y la hora max..
print(f"la temperatura maxima de la serie es {temperatura_max}°C y la hora en la cual se registro es {hora_max}Hs.")
# %% b)
import numpy as np

serie_array = np.array(serie) # al no usar corchete creo array de 1d (vector)
hora_array = np.array(hora)
print(serie_array.shape, serie_array.shape)
temp_max = serie_array.max()
posicion_i = np.flatnonzero(serie_array == temp_max) # se guarda como un array de tamaño 1
hora_max = hora_array[posicion_i]
print(f"La temperatura maxima de la serie es {temp_max}°C y la hora en la cual se registro es {hora_max} Hs.")

posicion_ii = np.nonzero(serie_array == temp_max) # al usar nonzero se guarda como una tuppla
hora_max = hora_array[posicion_ii]

posicion_iii = np.argmax(serie_array)
hora_max = hora_array[posicion_iii]

hora_max = hora_array[serie_array == temp_max]
# %% c) 
import numpy as np
serie_2 = [25 , 20 , 18 , 22 , 27 , 32 , 32 , 28]
hora = [0,3,6,9,12,15,18,21]
serie_array2 = np.array(serie_2)
hora_array = np.array(hora)
temp_max = np.max(serie_array2)
posicion_i = np.flatnonzero(serie_array2 == temp_max)
hora_max = hora_array[posicion_i]
posicion_ii = np.nonzero(serie_array2 == temp_max)
hora_max_ii = hora_array[posicion_ii] 
posicion_iii = np.argmax(serie_array2) # me toma solo un indice 
hora_max_iii = hora_array[posicion_iii] # guarda solo 1 de los maximos.
hora_max_iv = hora_array[serie_array2 == temp_max]
