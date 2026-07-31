# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 22:20:21 2025

@author: admin
"""

import networkx as nx
import matplotlib.pyplot as plt

def tamanhos_por_grau(G, base=100, fator=50):
    graus = dict(G.degree())  # {nó: grau}
    sizes = [base + fator * graus[n] for n in G.nodes()]
    return sizes

G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

nos_filtrados = [n for n in G.nodes() if n <= 100]

G100 = G.subgraph(nos_filtrados).copy()

sizes = tamanhos_por_grau(G100, base=50, fator=30)

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G100, seed=42)
nx.draw(
    G100,
    pos,
    with_labels=False,
    node_size=sizes,
)
plt.title("Rede Social - Facebook (SNAP)")
plt.show()


