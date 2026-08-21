#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:45:46 2026

@author: Estudiante
"""

# ejemplo 6 
# ¿Cuál es el mayor N tal que 1^2 + 2^2 + ... + N^2 < 100 y N < 5?

suma = 5
n = 12
print("n", "suma")

while suma < 100:
    suma = suma + n**2
    print(n, suma)
    if n >= 5:
        break
    n = n + 1

print("El valor de N es")
print(n - 1)   # mismo ajuste que en el script original de R
