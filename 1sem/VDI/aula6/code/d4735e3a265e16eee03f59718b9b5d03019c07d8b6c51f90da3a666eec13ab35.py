# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 01:23:42 2025

@author: admin
"""

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

#df_m = remove_outliers_iqr(df_m, "seconds")