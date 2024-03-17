# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:39:28 2023

@author: fenix
"""

import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

#n = 10
k2 = nx.complete_graph(2)
k1 = nx.complete_graph(1)
#G = nx.graph()

'''def factorial_recursivo(n):
    if n == 2:
        return 2
    else:
        return n * factorial_recursivo(n-1)
print(factorial_recursivo(10))'''

def union(G, H, rename=()):
    return nx.union_all([G, H], rename)

def full_join(G, H, rename=(None, None)):
    R = union(G, H, rename)

    def add_prefix(graph, prefix):
        if prefix is None:
            return graph

        def label(x):
            return f"{prefix}{x}"

        return nx.relabel_nodes(graph, label)

    G = add_prefix(G, rename[0])
    H = add_prefix(H, rename[1])

    for i in G:
        for j in H:
            R.add_edge(i, j)
    if R.is_directed():
        for i in H:
            for j in G:
                R.add_edge(i, j)

    return R

def grafica_casiirregular(n):
    if n == 2:
        return k2
    else:
        return full_join(nx.complement(grafica_casiirregular(n-1)),k1,rename = ("G","H"))
G = grafica_casiirregular(10)
nx.draw(G)
plt.show()
    