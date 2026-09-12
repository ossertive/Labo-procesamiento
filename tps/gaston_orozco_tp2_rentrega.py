# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:32:05 2026

@author: Gastón Orozco 
Laboratorio de procesamiento de la información meteorológica
Ejercicio para entregar de la practica 2
"""
import os 
os.getcwd()
# =============================================================================
# En este programa se intenta que el usuario ingrese los registros diarios de temperatura maxima (Tmax)  en el mes de noviembre (30 dias) y que se ingresen de a uno para ello se crea un ciclo donde se cuentan los dias y cada uno pide el ingreso de un valor de temperatura, como ya me dan el valor del primer dia de noviembre el ciclo tiene 29 dias entonces inicia en 2 y termina en 31 , ademas se incluye las condiciones pedidas; se usa while para verificar que la diferencia de temp del dia actual y anterior en valor absoluto no supere el umbral, si supera el umbral imprime una alerta y pide reingresar un dato valido. Ademas su usa condicinales if/else para el resto de las condiciones pedidas.
# =============================================================================
temp_anterior = 29.0 # temperatura en °C registrada el 1 primero de noviembre.
umbral = 15 # umbral de temperatura en °C
contador_calor = 0 # creo un contador para los dias calor.

for dia in range(2,31): # realizo un ciclo para los 29 dias restantes.

    temp_actual = float(input(f"Ingrese la temperatura máxima registrada del dia {dia} :"))
    
    while abs(temp_actual - temp_anterior) > umbral: # mientras el valor absoluto de la diferencia entre la Tmax del dia actual y anterior  supere un umbral de 15 °C se emite la alerta y pide el reingreso (while ejecuta mientras la condicion sea True y corta cuendo es False.)
    
        print("Alerta se supero el valor umbral reingrese un valor de temperatura")
        
        temp_actual = float(input(f"Reingrese el valor de temperatura del dia {dia}:")) 
        
    if temp_actual > 32: # si la temperatura actual ingresada supera los 32 ° C
        contador_calor += 1 # cantidad de dias en los que se supero los 32 °C
    temp_anterior = temp_actual # actulizo la temperatura del dia anterior con la ultima ingresada.
      
     
if contador_calor == 0: # si no sepero los 32 °C el contador permanece en cero
    print("Durante los 30 días ingresados no se registraron eventos de calor extremo")

else: # de otra forma
    print(f"Durante los 30 días ingresados se registraron {contador_calor} días con temperatura máxima mayor a 32°C")