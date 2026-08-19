#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:24:39 2026

@author: Estudiante
"""
import os
os.getcwd()
os.chdir("/home/Estudiante/Escritorio/Gaston_labo")
#%% Ejercicio 1 clase 3
##Pida al usuario ingresar su nombre completo separado por un espacio y sucorreo electrónico y muestre por pantalla:
#La cantidad de caracteres que tiene el nombre
#El usuario de mail (sin la extensión)
#Genere una dirección de usuario concatenando: las 3 primeras letras del
#nombre, las 3 últimas letras del apellido y el año actual. Arme un mensaje que muestre:
#%% resolucion
nombre_completo=input("Ingrese su nombre completo (separado por un espacio):") # la variable pide el nombre completo (separado por espacio).
email=input("ingrese su email:")# la variable pide el correro electronico.
nombre_completo_separado=nombre_completo.split(" ")
print(nombre_completo_separado)
nombre=nombre_completo_separado[0]
apellido=nombre_completo_separado[1]
longitud=len(nombre)
print(f"Su nombre tiene:{longitud} caracteres")
primer_nombre=email.split("@")
print(primer_nombre)
usuario_email=primer_nombre[0]
print(f"el nombre usuario es: {usuario_email}")

#%% resolucion segunda parte
año=input("Ingrese el año actual:")
nombre_tres_primeras=nombre_completo[0:3]
apellido_tres_primeras=nombre_completo[-3:]
usuario=nombre_tres_primeras + apellido_tres_primeras+ año 
print(f"Hola {nombre_completo} tu usuario generado es {usuario}")
