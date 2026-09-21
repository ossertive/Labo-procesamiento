# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:16:54 2026

@author: Anoma
"""
# Ejercicio 9 resolucion

import numpy as np
import pandas as pd

data = np.load("C:/Users/Anoma/Desktop/labo_temp/guias/datos_practica03/data_calidad_agua.npz",allow_pickle=True)

data_frame=pd.DataFrame({col:data[col] for col in data.files})
 # a) Elimine la columna del tiempo del DF
 
data_frame_2 = data_frame.drop(columns = "tiempo")

# b) 
dir_prom_agua_rad = np.deg2rad(data_frame_2["dir_prom_agua"]) # la funcin deg2rad tranf de grados a rad y con df["columna] le digo que transforme la columna seleccionada.


# c) Calcule la correlacion entre el pH y el O2 disuelto en el agua. Posteriormente calcule la matriz de correlacion entre la temperatura, salinidad, pH y O2 disuelto en el agua.
data_frame_depurado = data_frame.dropna()
correlacion = np.corrcoef(data_frame_depurado["pH"],data_frame_depurado["O2_dis"])

correlacion = data_frame["pH"].corr(data_frame["O2_dis"]) # al usar esta funcion ya ignora los nan.
print("El valor de correlacion entre el ph y el O2 es:",correlacion)

temp_salin_pH_O2dis = data_frame[["temperatura","salinidad","pH","O2_dis"]] # va doble corchete porque selecciono dentro del data_frame varios subelementos.

matriz_correlacion= temp_salin_pH_O2dis.corr()

print("La matriz correlacion entre temperatura salidad pH y O2 disuelto es:")
print(matriz_correlacion)