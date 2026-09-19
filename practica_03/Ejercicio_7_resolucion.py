# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:08:33 2026

@author: Anoma
"""
import numpy as np
# Ejercicio 7 resolucion.

matriz_a = np.zeros((5,6)) # creo una matriz de ceros para luego llenarlas las pociciones con el ciclo for.
matriz_b = np.zeros((5,6))
matriz_producto = np.zeros((5,6))
for i in range (5): # crea un ciclo para para las filas.
    for j in range (6): #crea un ciclo para las columnas.
        matriz_a[i,j] = i*j # indexo la posicion y le digo que sea multiplo de filas por columnas

for i in range (5):
    for j in range (6):
        matriz_b[i,j] = i*j
# ahora que ya tengo las matricez tengo que realizar un ciclo que relize el producto componente a componente.
for i in range (5):
    for j in range(6):
        matriz_producto[i,j] = (matriz_a[i,j]) * (matriz_b[i,j])
# verificacion : usando al funcion (*)

matriz = matriz_a * matriz_b

# %% inciso b)
import numpy as np
matriz_a = np.random.randint(0,10,(7,6)) # matriz de 7x6
matriz_b = np.random.randint(0,10,(6,5)) # matriz de 6x5
matriz = np.zeros((matriz_a.shape[0],matriz_b.shape[1])) # genera una matriz vacia de dimesion filas de matria a y columnas de matriz b.
if matriz_a.shape[1] == matriz_b.shape[0]: # mientras las filas de matriz a sean iguales a las filas de la matriz b.
    print("Las dimensiones son compatibles, realizando el calculo")
    for i in range (matriz_a.shape[0]):
        for j in range(matriz_b.shape[1]):
            matriz[i,j] = np.sum(matriz_a[i,:] * matriz_b[:,j]) # producto de matriz fila por columna y suma valores.
else:
    print("La dimensiones de las matrices son distintas no es posible realizar el producto matricial ")
# %% verificacion
print(f"verificacion: {matriz},{matriz_a @ matriz_b}")

# %% inciso d)

matriz = np.copy(matriz)
matriz = np.where(matriz < 0 ,0 ,matriz)
# usando indexacion
matriz[matriz < 0]= 0 
