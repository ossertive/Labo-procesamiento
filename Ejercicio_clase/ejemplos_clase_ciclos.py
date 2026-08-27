# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:48:09 2026

@author: Anoma
"""
# %% Ejemplo 1 for
for i in range(0,5):
    print(i)
# %% Ejemplo 2 for
x=5
for i in range(5):
    y=x*i
    print(y)    
# %% Ejemplo 3 for
alumnos=["Rocio" , "Matias" , "Ignacio" , "Micaela" , "Mercedes"]
for i in alumnos:
    print(i)
# %% Ejemplo 4 for
for i in range(len(alumnos)):
    print(f"Hola {alumnos[i]}")
# %%Ejercicio con for
y=100
for i in range(1,11):
    y=2/5*y
    print(f"La pelota alcanza la altura de {y} metros en {i} rebote ")
# %% Ejemplo 1 while
contador = 1
pasos = 0
while contador <= 10:
    pasos = pasos + 1
    print(contador)
    contador = contador + 2
print(f"El número de pasos fue: {pasos}")
# %% Ejemplo 2 while
n = 1
cuadrado = 0
while n<= 4000:
    cuadrado = n**2
    print(cuadrado)
# %% Ejercicio con while 
valor_ingresado=int(input("ingrese un valor:"))
limite=valor_ingresado**2
iteraciones=0
while valor_ingresado < limite:
    valor_ingresado=valor_ingresado + 1
    iteraciones=iteraciones+1
    print(valor_ingresado)      
print(f"la cantidad de interaciones es :{iteraciones}")
# %% Ejemplo de break con for
for i in range (0,5):
    if i==2:
        break
    print(i)
# %%  Ejemplo Break con while.
numero=19
while numero>4:
    if numero==14:
        break
    print(numero)
    numero -=1
# %% continue
for i in range(0,5):
    if i==2:
        continue
    print(i)
# %% Ejercicio para resolver en clase primera parte
# %% Resolución con for
n=int(input("Ingrese la cantidad total de registros de pp:"))
acumulado=0.0
for i in range(n):
    pp=float(input("ingrese el valor de de precipitacion:"))
    acumulado=acumulado + pp
print(f"La precipitación acumalada fue {acumulado}mm")
# %% Resolución con while
n=int(input("Ingrese la cantidad total de registros de pp:"))
acumulado=0.0
i=0 # contador de vueltas
while i < n:
    pp=float(input("ingrese el valor de precipitación:"))
    acumulado=acumulado+pp
    i=i+1 # incrementa una vuelta.
print(f"la precipitación acumulada fue {acumulado}mm")
# %% Ejercicio para resolver en clase segunda parte
# resolucion con while
dia=10
temperatura=295 # kelvin
umbral=303.15 # 30 °C en kelvin
while temperatura < umbral:
    print(f"El dia {dia} y con una temperatura de {temperatura},todavia no se superó el umbral de los 30°C ")
    temperatura=temperatura + 0.5 # el incremento de temp por dia.
    dia=dia+1
    


            

            
    








        






