# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:30:45 2026

@author: Anoma
"""

# %% Resolucion ejercicio 8
# a) Calcular el cuadrado de los primeros 10 enteros positivos.
for i in range(1,11):
    cuadrado=i**2
    print(cuadrado)

# b) Idem a) pero para los primeros 1000 enteros pares.
for i in range(1,1001):
    pares=2*i
    cuadrado= pares**2
    print(cuadrado)
# Manera limpia
for i in range(2,2001,2):
    cuadrado=i**2
    print(cuadrado)