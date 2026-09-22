# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:24:23 2026

@author: Gastón Orozco
Laboratorio de procesamiento de la información meteorológica
"""
import numpy as np
import pandas as pd
datos = np.load("C:/Users/Anoma/Desktop/labo_temp/tps/datos_ej_entregap3.npy")
datos_dim = np.load("C:/Users/Anoma/Desktop/labo_temp/tps/lat_lon.pkl",allow_pickle = True)

#El archivo contiene datos de temperatura media mensual en el periodo 1981-2010 para una región de Argentina (20°-55°S y 80°-50°O) ciudad de buenos aires coordenadas decimales (-34,5 , -58,5)

# %% item a) tengo una array de 3 dimensiones (360,141,121) tiempo - posicion(lat,lon)
# Para determinar los intervalos de la primera dimension realice el siguiente calculo: 
#   (2010-1981)+1 = 30 años entonces 30*12 = 360 meses
#   Periodo (1990 - 2005]
#   posicion (34.5°S -58.5°O) = (-34.5,-58.5)
#   (1990 - 1981) = 9*12 = 108 meses
#   (2005 - 1981) + 1 = 25*12 = 300 meses 
# verificacion: (300-108)=192 entonces 192 / 12 = 16 años ó (2005-1990) + 1 = 16 años 

temperatura = datos[108:300,58,86]
media_mensuales = temperatura.reshape(16,12).mean(axis=0) # con reshape redimensiono a un array de 2Dim y shape (16,12), ademas como la media es mensual le digo que calcule por filas.

# %% item b)
# Creo un diccionario para los meses los ingreso de forma manual  para que tomen el valor de los indices 12 meses y las temperaturas medias mensuales las convierto a °C y las redondeo con np.round( ,1) con un decimal.
diccionario = {"meses":["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],
               "temperaturas": np.round(media_mensuales - 273.15,1)} 
# %% item c) 
# A partir de un diccionario creo el dataframe (una tabla con columnas ("Meses,"Temperaturas"))
data_frame = pd.DataFrame(diccionario)

# %% item d) 
# Creo una columna nueva llamada Categoria, con la funcion logica np.where eligo los valores mayores a 15 °C de la columna "Temperaturas" del dataframe y le digo que me devuelva "superior a 15°C" si la condicion es True o "inferior o igual a 15°C" si es False.

data_frame["categoria"] = np.where(data_frame["temperaturas"] > 15 , # condicion logica
                                   
                    "superior a 15°C" , # que poner si es True
                    
                    "inferior/igual a 15°C") # que poner si es False

# %% item e) 
# La funcion tiene que recibir dos cosas para ser "generica": el dataframe y la etiqueta de la categoria que quiero buscar.
# La funcion tiene que ir a la columna "categoria" del dataframe y contar cuantas veces aparece la "etiqueta".
# El retorno debe ser un diccionario donde la clave sea el nombre de la categoria (etiqueta) y el valor la cantidad que se conto.

def contador_meses(df,etiqueta):
    cantidad = (df["categoria"] == etiqueta).sum()
    diccionario = {etiqueta : cantidad}
    return diccionario
# Aplico el dataframe del incicio d) y la "etiqueta": superior a 15°C

resultado = contador_meses(data_frame,"superior a 15°C")
print(resultado)
