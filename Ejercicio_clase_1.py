# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:51:06 2026

@author: Anoma
"""

# Ejercicio clase 1

## 1) Defini tu espacio de trabajo en una carpeta con tu nombre que este en el escritorio.

## 2) Definir las siguientes variables 
# a = 3
# b= 12.35
# c= b/a 
# d= "hola" 

## 3) Calcular que tipo de variable es cada una de las definidas en el punto 2. 

## 4) Utilizar las funciones de redondeo para obtener la parte entera de la variable c 

# %%

### Resolución
a=3
b=12.35
c=b/a
d="Hola"
type(a)
type(b)
type(c)
type(d)
import numpy as np
np.round(c)
np.ceil(c)
np.floor(c)
np.trunc(c)
