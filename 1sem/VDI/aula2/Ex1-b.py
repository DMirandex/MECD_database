# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:22:02 2025

@author: admin
"""

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0

num = int(input("Numero -->"))

while num != 0:
    if num<0:
        print("Tem que ser positivo ou 0.")
    else:
        if num%2==0:
            qtd_pares += 1
            soma_pares += num
        else:
            qtd_impares += 1
        soma_geral += num
    num = int(input("Numero -->"))

if qtd_pares+qtd_impares==0:
    print("Não foram introduzidos números!")
else:
    print("Quantidade pares --> ", qtd_pares)
    print("Quantidade impares --> ", qtd_impares)
    print("media valores pares --> ", soma_pares/qtd_impares) if qtd_pares>0 else print("media valores pares --> 0") 
    print("media valores geral --> ", soma_geral/(qtd_impares+qtd_pares)) 