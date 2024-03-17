# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:46:48 2023

@author: fenix
"""

import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import random

n = 10
k = 2
p = 0.9
while True:
        G = nx.newman_watts_strogatz_graph(n, k, p, seed=None)
        if nx.is_connected(G):
            break
s = list(G.degree())
lv = []
for i in range(n):
    lv.append(s[i][1]*400)
pos =nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=lv)
nx.draw(G)
plt.show()
#fig = mpl.pyplot.gcf()
#fig.set_size_inches(12, 8)
#plt.savefig('01paisaje3-RedesNuevas-jul20.png',bbox_inches='tight',pad_inches=2,dpi=300)
#plt.close()
#ordenado = []
arbol = nx.minimum_spanning_tree(G)
print(arbol.nodes())
nx.draw(arbol, with_labels = True)
plt.show()
'''s = list(G1.degree())
s = sorted(s)
for j in range(n):
    for i in range(len(list(G1.degree()))):
        print(i)
        if s[i][1] == 1:
            ordenado.append(s[i][0]) 
            G1 = G1.remove_node(s[i][0])
            s = list(G1.degree())
            break'''
def quitar_hojas(arbol):
    hojas = [nodo for nodo in arbol.nodes() if arbol.degree(nodo) == 1]
    for hoja in hojas:
        arbol.remove_node(hoja)
    return hojas
hojas_eliminadas = []
while arbol.number_of_nodes() > 1:
    hojas = quitar_hojas(arbol)
    hojas_eliminadas.extend(hojas)
    print("Eliminando hojas:", hojas)
    print("Árbol actual:", arbol.nodes())
print("Sucesión de nodos:", hojas_eliminadas[::-1])   
