# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:46:15 2026

@author: Anoma
"""
import os
os.getcwd()
os.chdir("E:\Documents\Cs. de la atmosfera\Laboratorio de procesamiento de la informacion meteorologica\ejemplos practica")
#%% Resolución ejercicio 2
## a)  Escriba un programa que pregunte el numero de tarjeta de credito y devuelva los ultimos 6 digitos.
tarjeta_credito=input("ingrese los 16 números de su tarjeta:")
ultimos_seis=tarjeta_credito[-6:] # cree una nueva variable para los ultimos  ultimos seis carecteres.
print(f"Los ultimos 6 digitos son:{ultimos_seis} ")

### b) Escriba un programa que pregunte el vecimiento de la tarjeta (MM/AAAA) y devuelva cuantos anios le restan para la renovación.

vencimiento=input("ingrese el vencimiento de su tarjeta (MM/AAAA):") # esto ejecuta un string
anios_vencimiento=int(vencimiento[-4:])# lo covierto a entero y uso slincing para tomar los ultimos 4 caracteres (años).
anios_restantes= anios_vencimiento-2026
print(f"Le restan {anios_restantes} años para la renovación")
