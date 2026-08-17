# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:57:55 2026

@author: Anoma
"""

##### Ejemplos clase 

### pido ingreso de un nombre por consola
nombre= input("Ingrese su nombre: ")

## imprimo por pantalla la variable nombre
print(nombre)

## quiero retener las dos primeras letras del nombre ingresado
nombre[0:2]

## si quiero la ultima letra 
nombre[-1:]

## para contar cuantos caracteres tiene la variable nombre uso len
len(nombre)

### ahora ingreso nombre y apellidos separados por espacio  
nombre_ap = input("Ingrese su nombre y apellido separado por un espacio: ")


## Quiero dividir el nombre del apellido para eso uso split
separados = nombre_ap.split(" ")
print(separados)

## si quiero el nombre me quedo con la parte 0
nombre2= separados[0]
print(nombre2)

## si quiero el apellido me quedo con la parte 1
apellido2= separados[1]
print(apellido2)

### ahora concanteno todo en una frase

print("tu nombre es", nombre2, "y tu apellido", apellido2)

### ejemplos de replace y join

### creo una frase

frase= "Hola nombre"

## cambio la palabra nombre por uno que quiero
frase2 = frase.replace("nombre", "Juan") 

print(frase2)

## ejemplo de join 

lista = ["Mi nombre es", "Juana"]
resultado = " ".join(lista)
print(resultado)

### ejemplos de upper y lower
palabra = "MESA"

palabra_min = palabra.lower()
print(palabra_min)

