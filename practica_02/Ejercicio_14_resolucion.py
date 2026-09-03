# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:33:26 2026

@author: Anoma
"""
# %% Ejercicio 14 

#ingreso de valor por pantalla
valores=int(input("Ingrese N valores:")) # la cantidad de datos

# Creo un ciclo donde se piden el valor de cada dato
suma_dato = 0.0 # defino los acumuladores antes de iterar
suma_cuadrados = 0.0 #

for i in range(valores):
    dato=float(input(f"Ingrese el valor del dato {i+1}:"))
    # actualizar los acumuladores para cada valor ingresado
    suma_dato += dato 
    suma_cuadrados += dato**2
    
# calculo de la media

media = round((suma_dato / valores),2) # redondeo a dos decimales.

# calculo del desvio estandar 
varianza = ((suma_cuadrados / valores) - media**2)
desvio = round((varianza)**(1/2) , 2)

print(f"El valor de la media es {media} y su devio estandar es {desvio}")
