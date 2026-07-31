# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 01:23:42 2025

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("boston_results_2019.csv", on_bad_lines="skip")

df["gender"] = df["gender"].astype(str).str.strip()
df_m = df[df["gender"] == "M"].copy()

df_m["age"] = pd.to_numeric(df_m["age"], errors="coerce")
df_m = df_m.dropna(subset=["age", "seconds"])

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df_m = remove_outliers_iqr(df_m, "seconds")

plt.figure(figsize=(8, 5))
plt.scatter(df_m["age"], df_m["seconds"], alpha=0.4)
plt.title("Tempo de Conclusão vs Idade (Homens) - Boston Marathon 2019")
plt.xlabel("Idade (anos)")
plt.ylabel("Tempo oficial (segundos)")
plt.grid(True)
plt.tight_layout()

plt.show()