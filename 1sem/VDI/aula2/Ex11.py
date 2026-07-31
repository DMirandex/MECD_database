import csv
import numpy as np
import random
import os
import matplotlib.pyplot as plt

temperaturas = [random.uniform(20, 45) for i in range(30)]
prob_precipi = [random.uniform(0, 100) for i in range(30)]

print('--->', len(temperaturas), temperaturas)
print('--->', len(prob_precipi), prob_precipi)


#escrever para o csv
with open('clima.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(["TP", "PP"]);
    for i in range(30):
        writer.writerow([temperaturas[i],prob_precipi[i]])

#ler do csv
temperaturas = []
prob_precipi = []
with open('clima.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if 'TP' in row or 'PP' in row:
            continue
        temperaturas.append(float(row[0]))
        prob_precipi.append(float(row[1]))

print('--->', len(temperaturas), temperaturas)
print('--->', len(prob_precipi), prob_precipi)


dias = np.array([x for x in range(30)])

plt.xlabel("Dias")
plt.ylabel("Clima")

plt.plot(dias, temperaturas, '-', label='Temperaturas (ºC)')
plt.plot(dias, prob_precipi, '-', label='Prob. Precipitação (%)')
plt.legend()
plt.show()

