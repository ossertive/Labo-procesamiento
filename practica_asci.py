#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:06:15 2026

@author: Estudiante
"""

import os
os.chdir("/home/Estudiante/Escritorio/gaston_labo/Datos ascii-20261002/")
archivo = "datos_estaciones.txt"
import numpy as np
import pandas as pd

df = pd.read_csv(archivo , sep = "\s+" ,na_values=[-999, -999.0, "-999"])

datos_faltantes_columna = df.isna().sum()

datos_faltantes = df.isna().sum().sum()

maximo_temp = np.nanmax(df["TEMP"])
maximo_humedad = np.nanmax(df["HUM"])
maximo_presion = np.nanmax(df["PNM"])

maximo_temp_fila = df.loc[...]

media_temp= df.groupby("NOMBRE")["TEMP"].mean()

desvio_temp = df.groupby("NOMBRE")["TEMP"].std()
