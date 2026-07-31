# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 23:00:13 2025

@author: admin
"""


def soma_linhas_matriz(M):
    soma = []
    for l in range(len(M)):
        soma.append(sum(M[l]))
    return (*soma,) #retorna em tuplo

def soma_linhas_matriz_2(M):
    soma = [sum(l) for l in M] #com comprehension list
    return (*soma,) #retorna em tuplo


#Também pode ser lido do utilizador!!!
MATRIZ = [
        [3,5], 
        [2,7], 
        [5,9] 
    ]

print("Soma das linhas por ordem = ", soma_linhas_matriz(MATRIZ))
print("Soma das linhas por ordem = ", soma_linhas_matriz_2(MATRIZ))