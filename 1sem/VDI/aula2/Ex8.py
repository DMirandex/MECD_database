# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 23:35:12 2025

@author: admin
"""

import random

def sorteia (N=5, E=2):
    NUMEROS = [x for x in range(1,51)]
    ESTRELAS = [x for x in range(1,10)]
    SAMPLE_NUMEROS = random.sample(NUMEROS,N)
    SAMPLE_ESTRELAS = random.sample(ESTRELAS,E)
    SAMPLE_NUMEROS.sort()
    SAMPLE_ESTRELAS.sort()
    return SAMPLE_NUMEROS, SAMPLE_ESTRELAS
    

print(sorteia())