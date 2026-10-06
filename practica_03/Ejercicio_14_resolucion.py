#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:44:35 2026

@author: gaston
"""

# Ejercicio 14 resolucion 

import pandas as pd

import numpy as np

data = np.load("/home/gaston/Escritorio/Labo_python/Guias_practicas/Practica_3/Datos práctica 3-20261004/datos_estaciones.npz" , allow_pickle = True)

print(list(data))

data_info = np.load("/home/gaston/Escritorio/Labo_python/Guias_practicas/Practica_3/Datos práctica 3-20261004/estaciones_info.npz" , allow_pickle = True)

df_info = pd.DataFrame({col: data_info[col] for col in data_info.files})

# item a) 

dic_estaciones = {} # creo mi diccionario maestro

for nombre in data.files:
    
    fila_info = df_info[df_info["Estaciones"] == nombre] 
    
    array_clima = data[nombre]
    array_clima = np.where(array_clima == 999.9 , np.nan , array_clima)
    
    array_clima[: , 0:2] = (array_clima[: , 0:2] - 32 ) * 5/9
    
    dic_estaciones[nombre] = { 
        "Latitud": fila_info["Latitud"].values[0] ,
        "Longitud" : fila_info["Longitud"].values[0],
        "Altura":fila_info["Altura"].values[0] ,
        "Codigo": fila_info["Codigo"].values[0],
        "Datos_Clima" : array_clima
        }
    
#%% 

# item a) reahciendo.. Armar un diccionario que contenga los datos correspondientes a cada estación como ası́ también información asociada a cada estación en particular: nombre, latitud, longitud, altura y código de identificación.

dic_estaciones = {} # creo un diccionario vacio
for nombre in data.files:
    fila_info = df_info[df_info["Estaciones"] == nombre]
    
    array_clima = data[nombre]
    array_clima = np.where(array_clima == 9999.9 , np.nan , array_clima)
    array_clima[: , 0:2] = ( array_clima[: , 0:2] - 32) * 5/9 # selecciona las columnas temperatura (columna 0) y temp de rocio (columna 1) y las covierte a grados centrigrados
    
    dic_estaciones[nombre] = {
        "Latitud": fila_info["Latitud"].values[0],
        "Longitud": fila_info["Longitud"].values[0],
        "Altura": fila_info["Altura"].values[0] ,
        "Codigo": fila_info["Codigo"].values[0],
        "Datos_Clima" : array_clima
        }

#%% item b) i)

def resumen_estaciones(diccionario):
    for estacion, ficha in diccionario.items():  # .items() separa la clave (nombres) de los valores.
        temperatura = ficha["Datos_Clima"][:,0]
        
        cantidad_datos = len(temperatura)
        
        datos_calor = np.sum(temperatura > 30)
        
        temp_media = np.nanmean(temperatura)
        temp_desvio = np.nanstd(temperatura)
        temp_max = np.nanmax(temperatura)
        temp_min = np.nanmin(temperatura)
   
        print(f"-----Estación: {estacion}------")
        print(f"Cantidad de datos: {cantidad_datos}")
        print(f" Dias con temperatura por encima de los 30°C: {datos_calor}")
        print(f"Temperatura media : {temp_media:.1f}°C")
        print(f"Desvio estandar : {temp_desvio:.1f}°C")
        print("-------------------- \n")
resumen_estaciones(dic_estaciones)
