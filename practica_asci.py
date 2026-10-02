#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:20:51 2026

@author: Estudiante
"""
import os
os.chdir("/home/Estudiante/Escritorio/gaston_labo/Datos ascii-20261002/")
archivo = "boya.txt"
import pandas as pd

df = pd.read_csv(archivo)
df
df = pd.read_csv(archivo, sep="\t")
df

df.shape

archivo2 = "boya_2.txt"
df2 = pd.read_csv(archivo2)
df2

df2 = pd.read_csv(archivo2, sep=",")
df2

import numpy as np

array = np.loadtxt(archivo2, skiprows=1, delimiter=",")
array.shape

import pandas as pd
datos = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
datos.to_csv('datos.txt', sep='\t', index=False)

import numpy as np
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('mi_archivo.txt', matriz,fmt = "%d")
