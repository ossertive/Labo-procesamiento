# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:49:13 2026

@author: Gastón Orozco
Laboratorio de procesamiento de la información meteorológica.
"""
import os
os.getcwd()
# ===============================================================================================================
# En este programa se intenta calcular el peso de un paquete a partir de un pedido
# de los productos más vendidos de una juguetería; rompecabezas (750.7 g) y cartas (80.5 g);
# Además el programa pide la cantidad del pedido, el destino y un número de seguimiento de seis caracteres.
# Luego el programa calculará el peso y mostrará en pantalla un mensaje donde contiene el destino en mayúscula
# el peso del paquete, los primeros dos caracteres del código de seguimiento que corresponden al país de origen
# y los últimos tres dígitos que corresponden al número de lote.
# ===============================================================================================================
rompecabezas = 750.7 
cartas = 80.5  
pedido = input("Ingrese la cantidad de su pedido en el formato Rompecabezas-cartas:") # ingresa por consola el pedido.
cantidad_pedido = pedido.split("-") # separa el guion de el pedido ingresado y crea una lista.
cantidad_rompecabezas = int(cantidad_pedido[0]) # selecciona de la lista el valor asignado a rompecabezas.
cantidad_cartas = int(cantidad_pedido[1]) # selecciona de la lista el valor asignado a cartas.
destino = input("Ingrese el destino:") # ingresa por consola el destino.
destino_mayus = destino.upper().strip() # Convierte a mayúsculas y elimina espacios extras al inicio y final.
seguimiento = input("ingrese el codigo de seguimiento de 6 caracteres en formato XXxNNN:") # ingresa por consola el seguimiento.
seguimiento_xx = seguimiento[0:2] # Mediante la funcion slicing separo los primeros dos caracteres.
lote = seguimiento[-3:] # Mediante slicing separo los ultimos tres caracteres.
peso_paquete = round((rompecabezas*cantidad_rompecabezas) + (cartas*cantidad_cartas)) # Calcula el peso del paquete y redondea al numero entero mas cercano.
print(f"El envío con destino a {destino_mayus} tiene un peso total de {peso_paquete} g. El país de origen es {seguimiento_xx} y el número de lote es {lote}")

           
