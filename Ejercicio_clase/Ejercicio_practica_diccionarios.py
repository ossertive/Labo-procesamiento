#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:39:22 2026

@author: Estudiante
"""

datos_ctd = {
"temperatura": 12.5, #En Celsius
"salinidad": 35.2, # en PSU
"profundidad": 250} # en metros
# Item a) modificar el valor de salinidad a 35.4 PSU.
datos_ctd.update({'salinidad':35.4})
# Item b) añadir la variable densidad con un valor de 1028.3 kg/m3.
#densidad = 1028.3
datos_ctd['densidad']= 1028.3
# Item c) Eliminar la variable de profundidad.
datos_ctd.pop('profundidad')
#Item d) transformar las temperaturas a grados Fahrenheit según F =C * 9/5 + 32
temperatura_celcius = datos_ctd.get('temperatura')
temperatura_faranheit = temperatura_celcius * (9/5) + 32 
datos_ctd.update({'temperatura':temperatura_faranheit})
print(temperatura_faranheit)

# Ejercicio 2
mes_enero = {"lluvia", "viento", "ola de calor", "granizo",
"tormenta"}
mes_julio = {"nieve", "ola de frío", "viento", "tormenta",
"lluvia"}
# a) En ambos meses
fenomeno_comun = mes_enero & mes_julio

# b) Los que se encuentran solo en un mes y no en el otro (para ambos meses)
print(mes_enero - mes_julio) 
print(mes_julio - mes_enero)
print(mes_enero ^ mes_julio)
# Item c) todos los fenómenos considerando ambos meses.
print(mes_enero | mes_julio)
