# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:15:40 2026

@author: Anoma
"""
# %% Ejercicio 9 resolucion
# a)
a=float(input("ingrese un numero positivo:"))
x=a #Este es el valor inicial de x_n
for i in range (1000):
   x= x - (x**2 - a) / (2 * x)
print(f"La raiz cuadrada aproximada del número {a} es: {x}")
# %% 
#b)
a=float(input("ingrese un numero positivo:"))
x=a #Este es el valor inicial de x_n
diferencia = 1.0 # valor aleatorio para obligar a while a arrancar
while diferencia >=10**-4: # condición si es true continua el ciclo 
    x_sig= x - (x**2 - a) / (2 * x) # calculo de x_{n+1}
    diferencia = abs(x-x_sig) # el valor absoluta de la diferencia entre x_n y x_{n+1}
    x=x_sig # actualizo x para la vuelta siguiente.
print(f"La raiz cuadrada aproximada del número {a} es: {x}")
# %%
# c)
a=float(input("ingrese un numero positivo:"))
x=a #Este es el valor inicial de x_n
diferencia = 1.0 # valor aleatorio para obligar a while a arrancar
iteraciones=0
while diferencia >=10**-4: # condición si es true continua el ciclo 
    x_sig= x - (x**2 - a) / (2 * x) # calculo de x_{n+1}
    diferencia = abs(x-x_sig) # el valor absoluta de la diferencia entre x_n y x_{n+1}
    x=x_sig # actualizo x para la vuelta siguiente.
    iteraciones +=1
    if iteraciones == 10000:
        print("El metodo no converge")
        break
if iteraciones < 10000:           
    print(f"La raiz cuadrada aproximada del número {a} es: {x}")

 


