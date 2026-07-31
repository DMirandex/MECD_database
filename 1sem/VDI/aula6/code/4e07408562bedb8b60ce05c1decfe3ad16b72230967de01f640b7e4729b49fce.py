# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 01:23:42 2025

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt

#x = df_m["age"].to_numpy(dtype=float)
#y = df_m["seconds"].to_numpy(dtype=float)

#x_mean = x.mean()
#y_mean = y.mean()

# m = cov(x,y) / var(x)
#m = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean)**2).sum()
#b = y_mean - m * x_mean

#y_hat = m * x + b

#ss_res = ((y - y_hat)**2).sum()
#ss_tot = ((y - y_mean)**2).sum()
#r2 = 1 - ss_res / ss_tot

#rmse = np.sqrt(((y - y_hat)**2).mean())

#print(f"m (inclinação) = {m:.4f}")
#print(f"b (interceção) = {b:.4f}")
#print(f"R^2            = {r2:.4f}")
#print(f"RMSE (min)     = {rmse:.2f}")


#plt.figure(figsize=(8, 5))
#plt.scatter(x, y, alpha=0.35, label="Atletas (M)")
# Linha nos limites do X para ficar contínua
#x_line = np.linspace(x.min(), x.max(), 200)
#y_line = m * x_line + b
#plt.plot(x_line, y_line, linewidth=2, color="red", label=f"Linha ajuste: y = {m:.2f}x + {b:.2f}")
#plt.title("Boston 2019 (M) — Tempo oficial vs Idade (com ajuste linear)")
#plt.xlabel("Idade (anos)")
#plt.ylabel("Tempo oficial (minutos)")
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.show()