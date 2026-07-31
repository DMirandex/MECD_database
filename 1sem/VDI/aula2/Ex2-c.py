# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:44:08 2025

@author: admin
"""

def percentagem_numeros_superiores_a_media(lista_numeros):
    media = 0
    for i in lista_numeros:
        media+=i
    media/=len(lista_numeros)
    n_sup = 0
    for i in lista_numeros:
        if i>media:
            n_sup+=1
    return n_sup/len(lista_numeros)*100

l = []
num = int(input("Numero -->"))
while num != 0:
    l.append(num)
    num = int(input("Numero -->"))
    
print("Percentagem de numeros superiores à média: {0:.2f}%".format(percentagem_numeros_superiores_a_media(l)))
    