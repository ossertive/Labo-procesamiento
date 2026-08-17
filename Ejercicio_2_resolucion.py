# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:00:09 2026

@author: Anoma
"""
#%% Resolucion ejercicio 2
a=int(1) # la variable "a" tiene el valor del numero entero 1.
b=int(2)# la variable "b" tiene el valor del numero entero 2.
c=a/b # dividimos las dos variables eso me da un flotante
type(c) # la funcion type me dice que tipo de variable es en este caso un float.
#%% 
import numpy as np
a=np.float64(1)
b=np.float64(3)
a/b
type(a/b)

a=np.float32(1)
b=np.float32(3)
a/b
type(a/b)
# Conclusión Ejercicio 2:
# La diferencia entre float32 y float64 radica en la cantidad de memoria (bits) que usan para representar el número.
# - float32 (precisión simple / 4 bytes): destina menos bits a la mantisa, guardando ~7 cifras significativas (da 0.33333334).
# - float64 (doble precisión / 8 bytes): tiene más estados posibles y guarda ~16 cifras significativas, logrando mayor exactitud.
# En Python estándar, todos los flotantes nativos son de 64 bits (doble precisión).
#%%  Sirve para preguntarle a Python "¿esta variable es de este tipo?", y devuelve un booleano (true or false)
a=int(2)
b=3.14159
isinstance(a,int)
isinstance(b,int)
isinstance(a,str)
isinstance(b,str)
isinstance(a,float)
isinstance(b,float)
#%%
a=int(3)
b=int(3.14159) # La funcion int le dice que tome al flotante como la parte entera al multiplicar solo da un entero
a*b
