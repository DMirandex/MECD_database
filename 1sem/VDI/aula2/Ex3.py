# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:54:48 2025

@author: admin
"""

def ocorrencias_em_lista(L, x):
    soma = 0
    for elemento in L:
        if elemento == x:
            soma += 1
    return soma

def ocorrencias_em_lista_2(L, x):
    return len([e for e in L if e==x]) # com comprehension list


LISTA = [3,22,33,4,6,77,8,4,32,5,66,4,6,7,10]
procr = 4

print("Ocorrencias de", procr, "na LISTA --> ", ocorrencias_em_lista(LISTA, procr))
print("Ocorrencias de", procr, "na LISTA --> ", ocorrencias_em_lista_2(LISTA, procr))