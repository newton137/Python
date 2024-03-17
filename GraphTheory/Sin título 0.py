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

def factorial_recursivo(n):
    if n == 2:
        return 2
    else:
        return n * factorial_recursivo(n-1)
print(factorial_recursivo(10))

def grafica_casiirregular(n):
    if n == 2:
        return k2
    else:
        return G1 = nx.full_join(nx.complement(grafica_casiirregular(n-1)),k1,rename = ("G","H"))
G = grafica_casiirregular(10)
nx.draw(G)
plt.show()    