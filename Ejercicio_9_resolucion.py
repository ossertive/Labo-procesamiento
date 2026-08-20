# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:41:20 2026

@author: Anoma
"""
import os
os.getcwd()
# %% Resolucion ejercicio 9
nombre=input("Ingrese su nombre:")
edad=input("ingrese su edad:")
edad_int=int(edad)
edad_futura=(edad_int + (2050-2025)+1) # nota:considero que en 2025 no complio años (n1-n0)+1.
print(f"{nombre} va a tener {edad_futura} años en 2050")
