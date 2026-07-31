# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 00:20:21 2025

@author: admin
"""

import networkx as nx
import matplotlib.pyplot as plt


def travessia_arvore(G, inicio=0, destino=None, modo="pre"):
    
    visitados = []

    # Função recursiva interna
    def dfs(n):
        
        filhos = list(G.successors(n))

        if destino is not None and n == destino:
            visitados.append(n)
            return True

        # PRE-ORDEN
        if modo == "pre":
            visitados.append(n)

        # ESQ
        if len(filhos) >= 1:
            if dfs(filhos[0]): 
                return True

        # IN-ORDEN
        if modo == "in":
            visitados.append(n)

        # DIR
        if len(filhos) >= 2:
            if dfs(filhos[1]):
                return True

        # POST-ORDEN
        if modo == "post":
            visitados.append(n)

        return False

    dfs(inicio)
    
    return visitados, len(visitados)



def gerar_arvore(niveis=4, filhos=2):
    G = nx.DiGraph()
    root = 0
    G.add_node(root)

    nodos_atuais = [root]
    proximo_id = 1

    for nivel in range(1, niveis):
        novos_nodos = []
        for pai in nodos_atuais:
            for _ in range(filhos):
                filho = proximo_id
                proximo_id += 1
                G.add_edge(pai, filho)
                novos_nodos.append(filho)
        nodos_atuais = novos_nodos

    return G, root

G, root = gerar_arvore(niveis=4, filhos=2)

print(travessia_arvore(G, destino=8, modo="pre"))
print(travessia_arvore(G, destino=8, modo="in"))
print(travessia_arvore(G, destino=8, modo="post"))

pos = nx.nx_agraph.graphviz_layout(G, prog="dot") if hasattr(nx.nx_agraph, "graphviz_layout") \
      else nx.spring_layout(G, seed=42)

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    arrows=False,
    node_size=600,
    node_color="lightblue",
    edge_color="gray"
)
plt.title("Árvore gerada automaticamente com 4 níveis")
plt.show()
