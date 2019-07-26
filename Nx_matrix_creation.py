import numpy as np
import networkx as nx

m_list=[]
m_labels=[]

for i in range(1000):
    G=nx.gnp_random_graph(10000, 0.5)
    m_list.append(nx.to_numpy_array(G))
    m_labels.append(nx.degree_centrality(G))

np.savez('mat_deg_cen_nx', m_list, m_labels)
