# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:33:37 2023

@author: fenix
"""
import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

G = nx.Graph([(0, 1), (0, 2)])
H = nx.Graph([(3, 4)])
print(G.nodes())
print(H.nodes())
R = nx.full_join(G, H, rename=("G", "H"))
R.nodes
R.edges