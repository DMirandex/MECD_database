# -*- coding: utf-8 -*-

import random


#FALTAM AS 5 OPORTUNIDADES PARA FALHAR, PARA VOCÊS SE DIVERTIREM!

if __name__ == "__main__":

    def verifica_atribui_letra(palavra_certa, lista_letras_palavra_desconhecida, letra):
        encontrou = False
        if letra in palavra_certa:
            encontrou = True
            for i in range(len(palavra_certa)):
                if letra==palavra_certa[i]:
                    lista_letras_palavra_desconhecida[i]=letra
        return encontrou, lista_letras_palavra_desconhecida
    
    l = ["cadeira", "mesa", "computador", "rato", "teclado", "dados", "gato", "cao", "python", "outras"]
    
    p = random.choice(l)
    
    a = ['_' for x in range(len(p))]
    
    encontrou, a = verifica_atribui_letra(p, a, random.choice(p))
    
    while (''.join(a)!=p):
        print(a)
        guess = input("Letra >>> ")
        encontrou, a = verifica_atribui_letra(p, a, guess)
                    
    print("Parabéns >>> ", ''.join(a))
    