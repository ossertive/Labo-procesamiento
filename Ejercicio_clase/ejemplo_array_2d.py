# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:52:19 2026

@author: Anoma
"""
# %% Ejercicio matrices
import numpy as np
# item 1
matriz_pp_verano = np.array([
    [28,130.0,118.9] # Fila 0: pp dicimbre
    ,[40,153.2,135.4] # Fila 1: pp enero
    ,[43,152.9,127.2] # fila 2: pp febrero
])
# item 2
desvio = np.std(matriz_pp_verano[1,:])
print(desvio)

# %% item 3
media_estacion = matriz_pp_verano.mean(axis=0)

# item 4
media_estacion_verano = media_estacion.reshape(1,3)
matriz_pp_verano_media= np.concatenate([matriz_pp_verano,media_estacion_verano],axis=0)
print(matriz_pp_verano_media)
