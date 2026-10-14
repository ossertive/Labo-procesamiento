# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import os
import datetime
import numpy as np
import netCDF4 as nc

os.chdir("/home/Estudiante/Descargas")

# Abrimos el archivo netCDF en modo lectura
file_path = "ERA5_sfc202212_3H00-24_SA.nc"
dataset = nc.Dataset(file_path, 'r')

# Miramos la información del archivo
print(dataset)

print(dataset.dimensions)

print(dataset.variables)

print(dataset.variables.keys)

#Accedemos a los datos
temp = dataset.variables["t2m"]

print(temp)

print(temp.units)

print(temp.dimensions)

print(temp.long_name)

#%%

media = np.max(temp,axis= (1,2))

media_calc=media.tolist()

variable_u = dataset.variables["u10"]
variable_v = dataset.variables["v10"]
np.savez("archivo.npz" ,u10 =  variable_u, v10 = variable_v )

viento = np.load("archivo.npz")




    
