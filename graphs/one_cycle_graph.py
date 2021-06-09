import networkx as nx


def get_graph():
    graph = nx.MultiGraph()
    number_of_nodes = 10
    number_of_nodes = number_of_nodes + 1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in range(1, number_of_nodes - 1):
        graph.add_edge(i, i + 1)
    nx.add_cycle(graph, [1, 2, 3])
    return graph


def get_graph_nodes(number_of_nodes):
    graph = nx.MultiGraph()
    number_of_nodes = number_of_nodes + 1
    graph.add_nodes_from(range(1, number_of_nodes))
    if number_of_nodes > 3:
        nx.add_cycle(graph, [1, 2, 3])
        for i in range(3, number_of_nodes - 1):
            graph.add_edge(i, i + 1)
        for i in range(1, number_of_nodes - 2):
            graph.add_edge(i, i + 2)
    return graph
