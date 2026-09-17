# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:44:48 2026

@author: Anoma
"""

# Ejercicio 6 resolucion
# a) Generar un arreglo numerico de dos dimensiones que tenga 20 columnas y 30 filas. La componente correspondiente a la fila i, columna j del array debe tener el resultado del producto de i*j.

import numpy as np

matriz_a = np.zeros((30,20)) # crea una matriz de ceros en este caso de 2D i=30 j=20.
# anido dos ciclos for que recorran i hasta 30 y j hasta 20.
for i in range (0,30):
    for j in range (0,20):
        matriz_a[i,j] = i*j # indexa la operacion a cada valor i,j
# %% b) Generar la misma matriz del punto anterior pero como producto punto a punto de dos matrices.
filas = np.arange(0,30).reshape(30,1)
columnas = np.arange(0,20).reshape(1,20)
matriz_b = filas * columnas # es un arreglo de 30 filas y 20 columnas donde los valores ij son el resultadod e multiplicar componente a componenete
# %%  c) Guardar la quinta columna del arreglo mencionado en el punto anterior en un vector B.
vector_B = matriz_b[:,4].reshape(1,30)
# %% d) 
matriz_d = np.zeros((20,30,10)) # genera una matriz vacia ceros para llenarla en este caso 3D i=20 j = 30 k = 10
#anido ciclos que recorran los ejes mencionados..
for i in range(20):
    for j in range(30):
        for k in range(10):
            matriz_d[i,j,k]= i*j*k
array=matriz_d[:,:,4]

