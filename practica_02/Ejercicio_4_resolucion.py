# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:00:25 2026

@author: Anoma
"""
# %% Ejercicio 4 resolución
# %%

temp = float(input("Ingrese la temperatura en grados Celsius: "))

if temp < 35:
    print("Temperatura por debajo de lo normal")
elif temp <= 37:  # De 35 a 37 inclusive
    print("Temperatura normal")
elif temp <= 38:  # De más de 37 a 38 inclusive
    print("Fiebre baja")
else:  # Mayor a 38
    print("Fiebre alta")