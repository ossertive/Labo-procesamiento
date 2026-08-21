#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:30:02 2026

@author: Estudiante
"""
import math
valor=int(input("ingrese un número:"))
if valor >=0:
    raiz=math.sqrt(valor)
    print("la raiz de",valor, "es:" ,raiz)
else:
    print(f"El numero ingresado no es valido ingrese un numero mayor o igual a cero:")