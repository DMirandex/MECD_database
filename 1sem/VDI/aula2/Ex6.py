# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 23:12:53 2025

@author: admin
"""

def podio_nao_ordenado(atletas):
    if len(atletas)<3:
        raise Exception("Numero de atletas inferior a 3...")
    podio = {}
    copyat = atletas.copy()
    while len(podio)<3:
        atl = None
        tmp = -1
        for k,v in copyat.items():
            if tmp == -1 or v<tmp:
                atl = k
                tmp = v
        del copyat[atl]
        podio[atl]=tmp
    
    return podio
    
    



atletas = {
        "Joao": 100,
        "Susana": 120,
        "Joana": 80,
        "Ricardo": 200,
        "Catarina": 90,
    }

#Para ler atletas do utilizador, descomentar codigo abaixo
#atletas = {}
#i=0
#num = int(input("Numero de atletas a introduzir -->"))
#while i<num: 
#    nome = input ("Nome atelta {} ---> ".format(i))
#    if nome in atletas:
#        print ("Este atleta já foi registado!")
#        continue
#    tempo = int(input("Tempo em segundos -->"))
#    atletas[nome] = tempo
#    i+=1
    
print(podio_nao_ordenado(atletas))