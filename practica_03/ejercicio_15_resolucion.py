#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:10:28 2026

@author: gaston
"""
# Ejercicio 15 

temp_celsius = [5.0, 15.0, 28.5, 11.0, 22.0] # cree una lista de prueba de temperaturas en °C

# a) En una nueva lista, transformar las temperaturas en grados Fahrenheit.

# ciclo tradicional

temp_faranheit = [] # lista vacia donde al completar el ciclo se agregaran las temps a kelvin.

for t in temp_celsius:
    temp_faranheit.append((t*9/5) + 32 )
print(temp_faranheit)

# lista por compresion.

temp_faranheit= [(t * 9/5) + 32  for t in temp_celsius]

# item b) 

def categorizar(temp):
    if temp < 12:
        return "FRIO"
    elif  temp < 25:
        return "Normal"
    else:
        return "caliente"
    
temp = [ (t ,(t*9/5)+32 ,categorizar(t)) for t in temp_celsius]
