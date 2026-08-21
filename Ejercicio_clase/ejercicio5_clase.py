#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:32:30 2026

@author: Estudiante
"""
import numpy as np
temp_max=float(input("ingrese la temperatura maxima registrada en °C :"))
temp_min=float(input("ingrese la temperatura minima registrada en °C:"))
if temp_max<temp_min:
    print(f"Tmax menor a Tmin, verificar los datos")
elif temp_max==temp_min:
    print(f"Tmax igual a Tmin, verificar datos")
else:
    amplitud=round(temp_max-temp_min,)
    print(f"La amplitud diaria fue de {amplitud} °C”. ")