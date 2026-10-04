#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:20:30 2026

@author: gaston
"""

# Ejercicio 11 

# a)

dic_estacion = {"Estacion": ["Aeroparque"],
                "Latitud": [-34.55] ,
                "Longitud": [-58.41] , 
                "Temp_media_mensual" : [26.3 , 26.0 , 24.5 , 23.1 , 22.0 , 15.0 , 10.1 , 15.3 , 15.7 , 19.0 , 21.3 , 22.8 ] }

# b)

lista_estacion = ["Aeroparque " ,
                  -34.55 ,
                  -58.41 ,
               [26.3 , 26.0 , 24.5 , 23.1 , 22.0 , 15.0 , 10.1 , 15.3 , 15.7 , 19.0 , 21.3 , 22.8] ]


print(f"En la estación {dic_estacion["Estacion"][0]} ubicada en {dic_estacion["Latitud"][0]} y {dic_estacion["Longitud"][0]}, la temperatura media de marzo es {dic_estacion["Temp_media_mensual"][2]}")

print(f"En la estación {lista_estacion[0]} ubicada en {lista_estacion[1]} y {lista_estacion[2]}, la temperatura media de marzo es {lista_estacion[3][2]}")