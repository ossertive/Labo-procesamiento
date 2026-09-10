# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:25:33 2026

@author: Anoma
"""

# Ejercicio 1 resolución
# %% a)

a = [ 4 , -10 , 7 , -2 , 8 , 8 , -6 , 1 , -15, 3 , -9]
i=3
j=5
a[:] # slicing
a[i] # -2 indexacion
a[i:j:2] # [-2] slicing
a[i:j:3] # [-2] slicing
a[i:len(a)] # [-2 , 8 , 8 ,-6,1 ,-15, 3 ,-9] slicing
a[-j:] # [-6 , 1 , 1 , -15 , 3 ,-9] slicing
a[-j] # -6 indexacion
a[a == -4] # 4 indexacion
# %% b) 
t = ( 4 , -10, 7 , -2, 8 , 8 , -6, -15, 3 , -9)
# i) 
a[2] = 4 # En la lista puedo modificar los valores asignando un valor a un indice
t[2] = 4  # las tuplas es inmutable (no se puede modificar)