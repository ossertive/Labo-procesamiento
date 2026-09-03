# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:50:52 2026

@author: Anoma
"""
#En los años bisiestos la cantidad de dias  son 366 y febrero tiene 29 dias.
#Meses con 31 dias (01 , 03 , 05 , 07 , 08 ,10 , 12) 
# Meses con 30 dias (04 , 06, 09 , 11 )
# Meses con 28 dias (02)
# %% Ejercicio 7 resolución
# a)
dia=int(input("Ingrese un dia en formato (DD):"))
mes=int(input("Ingrese el mes en formato (MM):"))
año=int(input("Ingrese el año en formato (YYYY):"))
# %%
# determino los dias del mes
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_del_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_del_mes = 30
elif mes == 2:
    dias_del_mes = 28
# Calculas la fecha del dia siguiente
if dia < dias_del_mes:
    dia_sig = dia + 1
    mes_sig = mes
    año_sig = año
else:
    # Ultimo dia del mes: reinicia el dia a 1
    dia_sig = 1
    if mes == 12:
    # Ultimo dia del año: pasa a enero y suma un año.
          mes_sig = 1
          año_sig = año + 1 
    else:
        # pasa al siguiente mes dentro del mismo año
         mes_sig = mes + 1 
         año_sig = año
# Asignar nombre a los meses siguientes.
if mes_sig == 1:
    nombre_mes = "Enero"
elif mes_sig == 2:
    nombre_mes = "Febrero"
elif mes_sig == 3:
    nombre_mes = "Marzo"
elif mes_sig == 4:
    nombre_mes = "Abril"
elif mes_sig == 5:
    nombre_mes = "Mayo"
elif mes_sig == 6:
    nombre_mes = "Junio"
elif mes_sig  == 7:
    nombre_mes = "julio"
elif mes_sig == 8:
    nombre_mes = "Agosto"
elif mes_sig == 9:
    nombre_mes = " Septiembre"
elif mes_sig == 10:
    nombre_mes = "Octubre"
elif mes_sig == 11:
    nombre_mes = "Noviembre"
else:
    nombre_mes = " diciembre"    
# Mostrar por pantalla el msj.
print(f"El resultado es día {dia_sig} de {nombre_mes} de {año_sig}")
# %% b) 
es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
    dias_mes = 30
elif mes == 2:
    #anido if else para el mes febrero para años bisiestos y no
    if es_bisiesto:
        dias_mes = 29
    else:
        dias_mes = 28

             

    
    
    


    
