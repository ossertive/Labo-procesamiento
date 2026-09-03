# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:31:53 2026

@author: Anoma
"""

# %% Ejercicio 15 resolución
nombre_apellido=input("Ingrese su nombre y apellido:")

# validación y reingreso de materias aprobadas

while True: # creo un ciclo que tenga como condicion simpre True
    try: # voy a intentar
        materias_aprobadas=int(input("Ingrese la cantidad de materias aprobadas:"))
        if materias_aprobadas >= 0:
            break
        else:
            print("La cantidad de materias no puede ser negativa")
    except ValueError: # si ingreso caracter no númerico
        print("Error: Debe ingresar un número entero.")
        
        
promedio_historico = 8.41

#caso especial: El estudiante no aprobo materias.

if materias_aprobadas == 0:
    print(f"El estudiante {nombre_apellido} no aprobó materias.")
else:
    suma_nota = 0.0
    
    # ciclo para pedir materias y notas
    for i in range(materias_aprobadas):
        input(f"\nIngrese el nombre de la materia {i+1}:")
            # validacion y reingreso de cada nota.
        while True:
            try:
                nota=float(input(f"\nIngrese la nota obtenida de la materia {i+1}:"))
                if 0<= nota <= 10:
                    suma_nota += nota # suma += valor
                    break
                else:
                    print("La nota ingresada debe estar entre 0 y 10.")
            except ValueError:  # excepcion si se ingresa una letra
                print("Error:Ingrese un valor númerico")
                
    # calculo promedio y msjes finales
                   
    promedio = suma_nota / materias_aprobadas
    if promedio > promedio_historico:
        print(f"El estudiante {nombre_apellido} aprobo {materias_aprobadas} materias y su promedio es mayor al promedio historico")
    elif promedio < promedio_historico:
        print(f"El estudiante {nombre_apellido} aprobo {materias_aprobadas} materias y su promedio es menor al promedio historico")
    else:
        print(f"El estudiante {nombre_apellido} aprobo {materias_aprobadas} materias y su promedio es igual al promedio historico")

    
