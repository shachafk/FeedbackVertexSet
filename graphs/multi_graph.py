
import networkx as nx
from utils.functions import show_graph

mg = nx.MultiGraph()
mg.add_node(1)
mg.add_node(2)
mg.add_edge(2, 1)
mg.add_edge(1, 2)
mg.add_edge(1,2)
mg.add_edge(1,1)

show_graph(mg,"bla")