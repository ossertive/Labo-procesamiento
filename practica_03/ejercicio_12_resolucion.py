#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:51 2026

@author: gaston
"""

# Ejercicio 12



def ingreso(lista_nombres,letra):
    
    lista_filtrada = []
    
    for nombre in lista_nombres:
        
        if nombre[0] == letra:
            lista_filtrada.append(nombre)
            
    return lista_filtrada

nombres = ["Marobel" , "Beto" , "Gaston" , "Melina" , "ana" , "Carolina"]
nombres_2 = ["micaela" , "abigail" , "magali" , "artyon" , "ariel" ]
ingreso(nombres,letra = "a")

ingreso(nombres_2,letra = "m")
