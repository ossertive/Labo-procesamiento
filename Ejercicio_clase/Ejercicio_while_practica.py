#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:36:09 2026

@author: Estudiante
"""

# %%
valor_ingresado_1=int(input("ingrese un valor númerico:"))
limite=valor_ingresado_1**2
iteraciones=0
while valor_ingresado_1<limite:
    valor_ingresado_1=valor_ingresado_1+1
    print(f"el valor ingreasado es: {valor_ingresado_1}")
print(f"La cantidad de iteraciones : {iteraciones}")
     