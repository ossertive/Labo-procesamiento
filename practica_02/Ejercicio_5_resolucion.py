# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:23:11 2026

@author: Anoma
"""
# %% Ejercicio 5 resolucion
A=16
B=3
isinstance(A, int)
isinstance(B, int)
if not (isinstance(A,int) and isinstance(B,int)): # si no son enteros imprime el msj
    print("Error: los números A y B deben ser enteros")
elif B==0:
    print("Error: no se puede dividir por cero.") # de otra forma si B==0 imprime el segundo msj
else: # Anidado
    if A % B == 0: # Evalúa si el resto es nulo, confirmando si A es divisible por B
        print(f"{A} es multiplo de {B}")
    else:
        print(f"{A} no es múltiplo de {B}.")
        



