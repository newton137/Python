# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:44:03 2023

@author: fenix
"""

import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import random
from networkx.algorithms import bipartite

n = 10
m = 15
G = nx.complete_bipartite_graph(n,m)
pos =nx.bipartite_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos)
plt.show()
      