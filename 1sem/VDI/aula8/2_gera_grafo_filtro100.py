# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 22:20:21 2025

@author: admin
"""

import networkx as nx

def segundo_grau(G, no):
    
    if no not in G:
        raise ValueError(f"O nó {no} não existe no grafo.")

    viz1 = set(G.neighbors(no))
    
    viz2 = set()
    for v in viz1:
        viz2.update(G.neighbors(v))
    
    viz2.difference_update(viz1)
    viz2.discard(no)
    
    return list(viz2)



G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

nos_filtrados = [n for n in G.nodes() if n <= 100]

G100 = G.subgraph(nos_filtrados).copy()
nos_primeiro_grau_no1 = segundo_grau(G100, 2)
print(nos_primeiro_grau_no1)
