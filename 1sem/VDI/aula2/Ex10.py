# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 23:40:52 2025

@author: admin
"""

import random
import math

X = [random.uniform(0, 1000) for x in range(100)]

#print (X)

print("Maior -->", max(X))
print("Menor -->", min(X))
media = sum(X)/len(X)
print("Media -->", media)
dp = math.sqrt(sum([math.pow(x-media,2) for x in X])/len(X))
print("D. Padrão -->", dp)
