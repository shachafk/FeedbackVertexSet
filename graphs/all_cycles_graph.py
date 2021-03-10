import networkx as nx
from utils.functions import show_graph


def get_graph():
    graph = nx.Graph()
    graph.add_nodes_from(range(1, 10))
    nx.add_cycle(graph, [1, 2, 3])
    nx.add_cycle(graph, [3, 4, 5])
    nx.add_cycle(graph, [5, 6, 7])
    nx.add_cycle(graph, [7, 8, 9])
    nx.add_cycle(graph, [9, 10, 1])
    return graph
