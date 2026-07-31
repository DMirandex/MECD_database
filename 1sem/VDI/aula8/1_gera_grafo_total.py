# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 22:20:21 2025

@author: admin
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

print("Nº de nós:", G.number_of_nodes())
print("Nº de arestas:", G.number_of_edges())

print("Grau médio:", sum(dict(G.degree()).values())/G.number_of_nodes())
print("Densidade:", nx.density(G))

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=10, edge_color="gray")
plt.title("Rede Social - Facebook (SNAP)")
plt.show()

