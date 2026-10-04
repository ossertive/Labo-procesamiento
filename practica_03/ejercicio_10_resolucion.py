#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:41:58 2026

@author: gaston
"""

# Ejercicio 10 - practica 3

import numpy as np
import pandas as pd

data = np.load("/home/gaston/Escritorio/Labo_python/Guias_practicas/Practica_3/Datos práctica 3-20261004/data_calidad_aire.npz" , allow_pickle = True)

data_aire = pd.DataFrame({col : data [col] for col in data.files} )

# item a) 

no2_centenario_promedio = data_aire.groupby("hora")["no2_centenario"].mean() # con groupby agrupo por hora y calculo la media de la variable "no2_centenario"

no2_centenario_desvio = data_aire.groupby("hora")["no2_centenario"].std() # idem para desvio estandar.

dic_centenario = {"promedio": no2_centenario_promedio , "desvio" : no2_centenario_desvio} # creo un diccionario  con el nombre de claves " promedio" y " desvio" y los valores que ya calcule anteriormente

data_aire_centenario = pd.DataFrame(dic_centenario) # genero un nuevo dataframe con el diccionario creado.

# item b) 
# primero para calcuar los promedios y desvios de las variables elimine las columnas fechas y horas con df.drop

promedios_totales = data_aire.drop(columns = ["fecha" , "hora"]).mean()

desvio_totales = data_aire.drop(columns = ["fecha" , "hora"]).std()

# item c)

no2_cordoba_promedio = data_aire.groupby("hora")["no2_cordoba"].mean()
co_cordoba_promedio = data_aire.groupby("hora")["co_cordoba"].mean()
pm10_cordoba_promedio = data_aire.groupby("hora")["pm10_cordoba"].mean()

data_aire_cordoba = pd.DataFrame({"co_cordoba" : co_cordoba_promedio ,
                                  "no2_cordoba" : no2_cordoba_promedio , 
                                  "pm10_cordoba" : pm10_cordoba_promedio})
