import networkx as nx
from utils.functions import show_graph
from utils.reductions import run_reductions

mg = nx.MultiGraph()
mg.add_node(1)
mg.add_node(2)
mg.add_node(3)
mg.add_edge(1, 2)
mg.add_edge(1, 3)
mg.add_edge(2, 3)
mg.add_edge(1, 2)
# mg.add_edge(1, 1)

k = 3
show_graph(mg, "before")
print("number of nodes before " + str(len(mg.nodes)))
print("k before " + str(k))
k, x = run_reductions(mg, k)
print("number of nodes after " + str(len(mg.nodes)))
print("k after " + str(k))
show_graph(mg, "after")
