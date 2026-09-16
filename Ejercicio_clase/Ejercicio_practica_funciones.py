#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:04:57 2026

@author: Estudiante
"""

# Ejercicio clase de funciones
# 1)

def calcular_promedio_pm25(lista): # defino la funcion en la lista de enteros o flotantes
    promedio = sum(lista) / len(lista)
    return promedio
lecturas_diarias = [12.5, 14.2, 16.8, 18.0, 21.5, 25.1]
promedio = calcular_promedio_pm25(lecturas_diarias)
# b)
def evaluar_calidad_aire(promedio): 
    if promedio <= 15:
        calidad_aire = "Buena"
    elif  promedio <= 20 :
        calidad_aire = "Aceptable"
    else:
        calidad_aire = "Mala"
        
    if calidad_aire == "Mala" or promedio > 20 :
        alerta = True 
    else:
        alerta = False  
    return calidad_aire , alerta
calidad_aire = evaluar_calidad_aire(promedio)
#  c)
def imprimir_reporte(lista_nueva):
   promedio = calcular_promedio_pm25(lista_nueva)
   calidad , alerta = evaluar_calidad_aire(promedio)
   mensaje = f"El promedio es {promedio} , el nivel de de calidad de aire es {calidad} , ¿es necesario emitir alerta? {alerta}."
   return print(mensaje)
lecturas_diarias = [12.5, 14.2, 16.8, 18.0, 21.5, 25.1]
promedio = calcular_promedio_pm25(lecturas_diarias)
imprimir_reporte(lecturas_diarias)
