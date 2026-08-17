# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:04:37 2026

@author: Anoma
"""

Ejercicio 1
a) Escribí un “programa” que pregunte por tu nombre y apellido
(separados por un espacio y en minúscula) y devuelva un ¡Hola
<NOMBRE>!
b) Modificá el “programa” anterior para que devuelva un ¡Hola
<nombre> <Inicial apellido>! El nombre debe estar en minúscula y
la inicial del apellido en mayúscula.
c) Ahora escribí un "programa" que reciba dos números y devuelva
el promedio de la siguiente manera: El promedio de <n1> y <n2>
es <promedio>.

#%% Resolución
import os
os.getcwd()
#%%a) Este programa pregunta el nombre y apellido y cuando se ejecuta devuelve un ¡Hola Gastón!

nombre_apellido=input("ingresa tu nombre y apellido (en minuscula):")
nombre_apellido_mayus= nombre_apellido.upper()
print("¡Hola " + nombre_apellido_mayus + "!" )

#%% b) Es el mismo programa del item anterior pero ahora devuelve ¡Hola gastón O (nombre en minuscula e inicial del apellido en mayuscula))
partes = nombre_apellido.split()
nombre = partes[0].lower()
apellido= partes[1]
inicial_apellido= apellido[0].upper()
print(f"¡Hola {nombre} {inicial_apellido}!")

#%%c) este ultimo programa ingresa dos numeros y devuelve el promedio.
n1_texto=input("ingresa el primer número (n1):")
n2_texto=input("ingresa el segundo número (n2):")
n1=float(n1_texto) # convierte el texto "10" en un número de verdad 10.0
n2=float(n2_texto) # convierte el texto "8" en un número de verdad 8.0
promedio=(n1+n2)/2
print(f"El promedio de {n1} y {n2} es {promedio}:")
