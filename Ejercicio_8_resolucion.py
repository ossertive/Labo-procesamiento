# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:12:34 2026

@author: Anoma
"""

# %% Resolución ejercicio 8
# a) creo las variables año mes y dia por separado luego creo una nueva variable (feacha) y uso cocatenacion separods por puntos...
año=input("ingrese el año actual en formato YYYY:")
mes=input("ingrese el mes actual en formato MM:")
dia=input("ingrese el dia actual en formato DD:")
fecha_punto=f"{año}.{mes}.{dia}" #la funcion f me da el formato y la separo por puntos.
print(f"la fecha ingresada es:{fecha_punto}")
# %% b) creo una variable que me pida ingresar año mes y dia separado por - luego uso la funcion replace para replasarlos por espacios
anio_mes_dia=input("ingrese el año-mes-dia:")
fecha_separada=anio_mes_dia.split("-")
dia=fecha_separada[2]
mes=fecha_separada[1]
anio=fecha_separada[0]
print(f"La fecha ingreasa es: {dia} del {mes} de {anio}")
# %% c) creo un varible donde me pidan el nombre y luego uso la funcion slicing para extrear la primer o ultima letra lue
nombre=input("ingrese un nombre:")
nombre_primera=nombre[:1]
nombre_ultima=nombre[-1:]
print(f"La primera letra es {nombre_primera} y la ultima letra es {nombre_ultima} ")
