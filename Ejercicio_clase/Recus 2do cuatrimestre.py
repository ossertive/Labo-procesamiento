#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:12:41 2026

@author: Estudiante
"""
# %% Ejercicio 5 recus 2do cuatrimestre 

# a) 


def precipitacion_acum(pp_registrada,pp_umbral=1): # funcion generica con 2 argumentos 
    
    acumulado = 0 # defino un contador 
    
    for valor in pp_registrada: # ciclo que recorra la lista
    
        if valor > pp_umbral:
            
            acumulado += valor
            
    return acumulado
        
# verificacion: 


# %% b) 

a = {
"Estacion1": [5,8,9,0.5,0.1,1],
"Estacion2": [3,0.4,20,6],
"Estacion3": [0.5,0.2,1,0.6],
"Estacion4": [8,4,0.01]}

claves= a.keys()

for i in claves:
    lista = a[i]
    acumulado_total = precipitacion_acum(lista)
    
    if acumulado_total > 0 :
        print(f"En la estacion {i} el acumulado de precipitación fue de {acumulado_total} mm.")
    else :
        print(f"En la estación {i} el acumulado no fue calculado")