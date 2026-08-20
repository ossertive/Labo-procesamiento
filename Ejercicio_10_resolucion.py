# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:15:24 2026

@author: Anoma
"""

# %% Resolución ejercicio 10
nombre_apellido=input("ingrese su nombre y apellido separo por comas:")
libreta=input("ingrese su numero de libreta universitaria en formato N/AA:")
materias_aprobadas=int(input("ingrese la cantidad de materias aprobadas:"))
nombre_separado=nombre_apellido.split(",")
libreta_separado=libreta.split("/")
nombre=nombre_separado[0]
apellido=nombre_separado[1]
puesto=libreta_separado[0]
año=libreta_separado[1]
materias_restantes=20-materias_aprobadas
print(f"El alumno {nombre} {apellido} se inscribio como alumno de exactas en el puesto {puesto} en el año 20{año} y debe aprobar {materias_restantes} materias para obtener el título de grado.")
