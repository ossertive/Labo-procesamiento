# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:46:40 2026

@author: Anoma
"""

for i in range(1,6):
    print("caso",i,"\n")

letras=["c" , "l" , "i" , "m" , "a" ]
for i in range(5):
    print(letras[i])
for j in letras:
    print(j)
for i in range(len(letras)):
    print(letras[i])
# %%
i=5
while i>0:
    print("caso",i,"\n")
    i=i-1
# %%
i=0
while i < 5:
    print(letras[i])
    i=i+1
# %% break
a=4
for i in range(11):
    suma=a+i
    print(suma)
    if suma>=9:
        break
# %% continue
for i in range(6): # i va del 0 al 5
    print(i)
    if 3<=i and i<=5:
        continue
    print(i)


