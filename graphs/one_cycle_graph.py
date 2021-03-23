import networkx as nx


def get_graph():
    graph = nx.MultiGraph()
    number_of_nodes = 10
    number_of_nodes = number_of_nodes+1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in range(1, number_of_nodes-1):
        graph.add_edge(i, i + 1)
    nx.add_cycle(graph, [1, 2, 3])
    return graph


def get_graph_nodes(number_of_nodes):
    graph = nx.Graph()
    number_of_nodes = number_of_nodes+1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in range(1, number_of_nodes-1):
        graph.add_edge(i, i + 1)
    if number_of_nodes > 3:
        nx.add_cycle(graph, [1, 2, 3])
    return graph
