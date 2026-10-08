#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:06:15 2026

@author: Estudiante
"""

import os

os.chdir("/home/gaston/Escritorio/Labo_python/clases_practicas/Datos ascii-20261008")

archivo = "datos_estaciones.txt"
import numpy as np
import pandas as pd
# con la funcion read_csv de pandas leeo el archivo ascii con formato de tabla y creo el data frame ademas separo las columnas con mas de un espacio con sep , e ignoro los valores erroneos (-999.0 ...) y les asigno el valor de nan.
df = pd.read_csv(archivo , sep = "\s+" ,na_values=[-999, -999.0, "-999"])

datos_faltantes_columna = df.isna().sum() # cuenta la cantidad de datos faltantes (nan) por columna
datos_faltantes_1 = df.isna().sum().sum()
datos_faltantes_2 = datos_faltantes_columna.sum()

maximo_temp = np.nanmax(df["TEMP"]) # usando nanmax() cuanto el maximo ignorando los nan de la columna temp del data frame.
maximo_humedad = np.nanmax(df["HUM"])
maximo_presion = np.nanmax(df["PNM"])

maximo_temp_estacion_hora = df[df["TEMP"] == maximo_temp][["NOMBRE","HORA"]]
maximo_humedad_estacion_hora = df[df["HUM"] == maximo_humedad][["NOMBRE","HORA"]]
maximo_presion_estacion_hora = df[df["PNM"] == maximo_presion][["NOMBRE","HORA"]]

media_temp= round(df.groupby("NOMBRE")["TEMP"].mean(), 2)
desvio_temp = round(df.groupby("NOMBRE")["TEMP"].std() , 2)

data = pd.DataFrame({"Promedio": media_temp ,"Desvio": desvio_temp})

data.to_csv('data.txt', sep ="\t" , index = True)

#%%


def reporte_estaciones(ruta , Estacion):
    
    df = pd.read_csv(ruta , sep = "\s+" , na_values=[-999 ,"999" , -999.0] )
    
    filtro = df[df["NOMBRE"] == Estacion]
    
    promedio = round(filtro["TEMP"].mean(),1)
    desvio = round(filtro["TEMP"].std(),1)
    
    print(f"En la estacion {Estacion} el promedio de la temperatura es de {promedio} y tiene un desvio estandar de {desvio}")
   
reporte_estaciones("datos_estaciones.txt" , "AEROPARQUE")
