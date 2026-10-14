#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:38:35 2026

@author: Estudiante
"""

import pandas as pd
import numpy as np
PATH = "/home/Estudiante/Descargas/datos_pp_bariloche.xlsx"
df = pd.read_excel(PATH)
df = pd.read_excel(PATH, na_values=[-9999.0,"-9999",-9999])
df = pd.read_excel(PATH, na_values=[-9999.0],usecols = ['Anio', 'Enero', 'Febrero',
'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
'Octubre', 'Noviembre', 'Diciembre'])
df2 = df.iloc[:, df.columns != 'Anio'] = df.loc[:, df.columns != 'Anio'] / 10

#%% Ejercicio

import pandas as pd
import numpy as np

# 1. Abrir datos.xls y la hoja "serie"
PATH = "/home/Estudiante/Descargas/datos.xls"
df = pd.read_excel(PATH, sheet_name="serie")


filtro_anios = (df['anio'] >= 1995) & (df['anio'] <= 2005)
datos_periodo = df[filtro_anios]

promedio_tmax = datos_periodo['T max (C)'].mean().round(2)
promedio_tmin = datos_periodo['T min (C)'].mean().round(2)

datos_enero = df[df['mes'] == 1]

min_pp_enero = datos_enero['pp (mm)'].min()
idx_min = datos_enero['pp (mm)'].idxmin()
anio_min_pp = df.loc[idx_min, 'anio']

def calcular_tmin_mes(data, mes_num):
    sub = data[data['mes'] == mes_num]
    return sub['T min (C)'].min()
meses = range(1, 13)
minimas = [calcular_tmin_mes(df, m) for m in meses]

df_resumen = pd.DataFrame({
    "mes": list(meses),
    "t_min_absoluta": minimas
})

df_resumen.to_csv("resumen_tmin.csv", index=False)
df_resumen.to_excel("resumen_tmin.xlsx", index=False)
