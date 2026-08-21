#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:09:32 2026

@author: Estudiante
"""

nota=int(input("Ingrese la nota que obtuvo:"))
if  nota >4:
    print("Su parcial esta aprobado")
elif nota<0 or nota>10:
    print(f"ingrese un valor entre 0 y 10")
    
else:
    print(f"Su parcial esta desaprobado")    

    
