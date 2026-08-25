# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:10:37 2026

@author: Anoma
"""
import os
os.getcwd()
# %% Resolución ejercicio 3
x=int(input("ingrese un valor entero:")) # pide un entero por consola
if x>0: # # Si el número es positivo (x > 0 es True)
    print(5+(1+3*x**2)**-2)
elif x<0 : # Si el número es negativo (x < 0 es True)
    print(1-(1+5*x**2)**-2)
else:     # Si no es positivo ni negativo (x == 0)
    print(0)


