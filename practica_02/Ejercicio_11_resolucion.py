# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:48:51 2026

@author: Anoma
"""

# %% Ejercicio 11 resolución
for i in range(5):
    print(f"\n----- punto {i+1}-----")
    x=float(input("ingrese un valor para x:"))
    y=float(input("Ingrese un valor para y:"))
# verico si los pares caen en el area sombreada.
    if (0 <= x<= 1) and (0 <= y <= x):
        print(f"El punto ({x}, {y}) pertenece al área sombreada")
    else:
        print(f"El punto ({x},{y}) no pertenece al área sombreada")
    

