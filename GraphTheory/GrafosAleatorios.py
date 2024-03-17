# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:07:24 2023

@author: fenix
"""

import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import random

n = 10
G = nx.complete_graph(n)
G1 = nx.complete_graph(n)
p = 0.2
for i in G.edges():
    print(i)
    k = random.random()
    if k > p:
        G1.remove_edges_from([i])
nx.draw(G1, with_labels = True)
plt.show()
      