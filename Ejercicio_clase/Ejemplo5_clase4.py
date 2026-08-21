#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:43:46 2026

@author: Estudiante
"""

# ejemplo 5 - teórica parte 2
# ¿Cuál es el mayor N tal que 1^2 + 2^2 + ... + N^2 < 10?

suma = 0
n = 0

print("n", "suma")  # cartel para la salida de valores

while suma < 10:
    suma = suma + n**2
    print(n, suma)   # muestra los valores en pantalla
    n = n + 1

print("El valor de N es")
print(n - 2)  # ajusta por el 0 inicial y la última suma que excede 10
