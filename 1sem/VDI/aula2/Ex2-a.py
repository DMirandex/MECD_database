# -*- coding: utf-8 -*-

import sys #para poder ir buscar o minimo número

def maior_10():
    maior = -sys.maxsize 
    for i in range (0,10):
        num = int(input("Numero -->"))
        if num>maior:
            maior=num
            
    return maior

m10 = maior_10()

print("Maior de 10 = ", m10)
