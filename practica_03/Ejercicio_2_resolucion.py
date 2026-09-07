# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:12:19 2026

@author: Anoma
"""

# Resolucion ejercicio 2
# a)
temp = [17,26,30,16,7,8,-2] # temp en °C
#i) Generar una lista de igual longitud con valores posibles de temperatura.

temp_kelvin = [ t + 273.15 for t in temp ] # genero una lista por compresion

# ii) Concatenar las dos listas
concatenada = temp + temp_kelvin
print("concatenada",concatenada)

# iii) sumar los valores de ambas listas
# i. Utilizando un ciclo que recorra ambas listas.
suma_elem =[] # creo una lista
for i in range(len(temp)): # realiza el ciclo en la longitud de temp que es igual a la longitud de temp_kelvin
    suma_elem.append(temp[i] + temp_kelvin[i]) # agrego a la nueva lista los elemantos que recorre el ciclo sumados
print("suma elemento a elemento",suma_elem)    

# ii. Utilizando el operador ”+”, ¿Cual es el resultado obtenido?
operador_mas = temp + temp_kelvin 
print("Con el operador +",operador_mas) # con (+) concatena y no suma como operacion matematica.
# iv) Calcular la media y la desviacion estandar de la lista concatenada sin usar funciones predefinidas.

