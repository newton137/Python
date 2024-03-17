# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:22:16 2023

@author: fenix
"""

import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import random as rd

df = pd.read_csv('gameOfThrones_network.csv')
G = nx.from_pandas_edgelist(df,"Source","Target",["Weight"])
G = G.to_directed() 
print(df.to_string())
nx.draw(G)
plt.show()
print(G.order())
print(G.size())
print(G["Walder"]["Lothar"]["Weight"])
print(G.degree("Walder"))
print(nx.diameter(G))
for _ in range(10):
    nodo1 = rd.choice(list(G.nodes()))
    nodo2 = rd.choice(list(G.nodes()))
    shortest_path = nx.shortest_path(G, source=nodo1, target=nodo2)
    print(f"{nodo1} , {nodo2}: {shortest_path}")
sucesion_de_grado = [degree for (node, degree) in G.degree()]
plt.hist(sucesion_de_grado, bins=range(max(sucesion_de_grado) + 2), alpha=0.5)
plt.title("Distribución de Grado")
plt.xlabel("Grado")
plt.ylabel("Número de Nodos")
plt.show()
n = 10
grados_ordenados = sorted(G.degree, key=lambda x: x[1], reverse=True)[:n]
nodos = [nodo for nodo, _ in grados_ordenados]
Gs = G.subgraph(nodos)
nx.draw(Gs)
plt.show()
grados_entrada = dict(G.in_degree())
grados_salida = dict(G.out_degree())
print(grados_entrada)
print(grados_salida)
SCC = list(nx.strongly_connected_components(G))
print(SCC)