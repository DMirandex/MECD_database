# -*- coding: utf-8 -*-

N = int(input("Quantos numeros vai introduzir?"))

soma = 0
for i in range(N):
    num = int(input("Numero {} -->".format(i)))
    soma += num
    
print ("Soma = ", soma)