import networkx as nx


def get_graph():
    graph = nx.Graph()
    graph.add_nodes_from(range(1, 5))
    for i in range(1, 5):
        graph.add_edge(i, i+1)
    nx.add_cycle(graph, [2, 3, 4])
    nx.add_cycle(graph, [1, 2, 3])
    return graph
