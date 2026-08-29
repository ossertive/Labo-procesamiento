#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:03:42 2026

@author: Estudiante
"""
# %%
sueldo=float(input("ingrese su sueldo:"))
if 0<=sueldo<6000:
    print("no paga impuesto")
elif 6000<=sueldo<20000:
    impuesto=(sueldo-6000)*0.17
    print(f"El impuesto a pagar: {impuesto}")
elif 20000<=sueldo<50000:
    impuesto=(2380 + 0.30*(sueldo - 20000))
    print(f"El impuesto a pagar: {impuesto}")
elif  50000<=sueldo<60000:
    impuesto=(11380 + 0.42*(sueldo - 50000))
    print(f"El impuesto a pagar: {impuesto}")
else:
    impuesto=(15580 + 0.47*(sueldo - 60000))
    print(f"el impuesto a pagar: {impuesto}")
# %%
sueldo=float(input("Ingrese su sueldo anual (en US$s):")) # ingresa el sueldo por consola

if  sueldo <=6000: # si el sueldo es menor o igual a 6000
    impuesto = 0.0 # el impuesto es un float 0.0
elif sueldo< 20000: # si el suldo cae en ese intervalo
    impuesto = (sueldo-6000)*0.17 # el impuesto esta dado por la expresion
elif sueldo < 50000:
    impuesto = (2380 + 0.30 * (sueldo - 20000))
elif sueldo < 60000:
    impuesto = (11380 + 0.42 * (sueldo - 50000))
else: # de otra forma el impuesto esa dado por la expresion
    impuesto = (15580 + 0.47 * (sueldo - 60000)) # y se calcula de esta manera
if impuesto == 0: # si el impuesto es igual a cero 
    print("No paga impuestos") # muestra por pantalla "no paga impuestos"
else: # en todos los demas casos imprime el msj con el impuesto calculado
    print(f"El impuesto a abonar es:{impuesto} U$s")
    

    