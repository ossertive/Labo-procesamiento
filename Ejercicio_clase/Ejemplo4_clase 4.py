#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:40:50 2026

@author: Estudiante
"""

# ejemplo 4 
# Calcular la suma de los n primeros términos de la sucesión: 1, 2x, 3x^2, 4x^3, ...

# variables de entrada:
# n: número de términos a sumar
# x: número al cual se le aplica la sucesión

# variables de salida:
# texto en pantalla (valor de la suma)

# Leer entradas
n = int(input("¿Cuántos términos quieres sumar? "))
x = float(input("Dame el valor del número x: "))

# Calcular suma = Σ_{i=1..n} i * x^(i-1)
suma = 0.0
for i in range(1, n + 1):
    suma += i * (x ** (i - 1))

print("El valor pedido es")
print(suma)
print(f"El valor pedido es {suma}")
