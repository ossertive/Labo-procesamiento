# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:48:50 2026

@author: Anoma
"""
# Ejercicio 5 resolucion
import numpy as np

data = np.load('C:/Users/Anoma/Desktop/labo_temp/guias/datos_practica03/datos_T_SABE_2010.npz')
print(list(data))
temp = data['T_SABE']
posiciones = np.where(temp > 40) # tupla
temperatura_mayor40 = temp[posiciones]
indice_error = posiciones[0] # como posiciones es una tupla saco los datos mediante indexacion (con indice 0)
temperatura_anterior = temp[indice_error - 1]
temperatura_posterior = temp[indice_error + 1]
print(np.size(temperatura_mayor40))

# %% b) 
serie_maximo_error = np.max(temp) # tiene en cuenta todos los datos inclusive los errores
serie_sin_error = temp[(temp <=40) & (temp != -999.0)] # la forma directa es usando indexacion
serie_maximo_sin_error = np.max(serie_sin_error)

serie_minimo_error = temp.min()
serie_sin_error = temp[(temp <= 40)& (temp != -999.0)] # aca ya filtro los erroneos y faltantes
serie_minimo_sin_error = serie_sin_error.min()
# suma de datos faltantes NaN
cantidad_datos_faltantes = np.sum(temp == -999.0)
print(f"La cantidad de datos faltantes es {cantidad_datos_faltantes}")
# %% c)
serie_ordenada = np.sort(serie_sin_error)
mediana = np.median(serie_ordenada)
# %% d) La idea es sacar los errores temp > 40 o(|) temp == -999.0 y renombrarlo como NaN
temp_calendario = temp.copy() #copio la serie original

temp_calendario[(temp_calendario > 40) | (temp_calendario == -999)] = np.nan
temp_364 = temp_calendario[:364] # esto es para que me de las semanas enteras no tomo el ultimo dia.
temp_semanas = temp_364.reshape(52,7) # con reshape le digo a numpy que me trasforme un vector de 364 dias a un array de 52 semanas por 7 dias.
medias_semanales = np.nanmean(temp_semanas,axis = 1 )
print(medias_semanales)
# %% e)
n = 10
frecuencias,bordes = np.histogram(serie_sin_error,bins=n)
print(f"La cantidad de dias en cada intervalo: {frecuencias}")
print(f"Limites de los {n} intervalos de temperatura : {bordes}")

# item e) a manopla (plagio)
# %% e) a mano
n = 10
# 1. Calculamos los límites de los intervalos matemáticamente
minimo = serie_sin_error.min()
maximo = serie_sin_error.max()

# np.linspace crea 'n+1' bordes separados exactamente por la misma distancia
bordes_manuales = np.linspace(minimo, maximo, n + 1)

frecuencias_manuales = [] # Lista vacía para ir guardando los resultados

# 2. Ciclo for para contar los días que caen en cada intervalo
for i in range(n):
    limite_inf = bordes_manuales[i]
    limite_sup = bordes_manuales[i + 1]
    
    # Armamos la máscara lógica (mayor o igual al límite inferior Y menor al superior)
    if i == n - 1: # Al último intervalo le ponemos <= para que incluya el máximo absoluto
        mascara = (serie_sin_error >= limite_inf) & (serie_sin_error <= limite_sup)
    else:
        mascara = (serie_sin_error >= limite_inf) & (serie_sin_error < limite_sup)
    
    # Contamos cuántos True hay en la máscara y lo guardamos
    cantidad_dias = np.sum(mascara)
    frecuencias_manuales.append(cantidad_dias)

print("Frecuencias a mano:", frecuencias_manuales)