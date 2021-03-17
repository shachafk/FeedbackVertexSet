import networkx as nx


def get_graph():
    number_of_nodes = 10
    graph = nx.Graph()
    number_of_nodes = number_of_nodes+1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in graph.nodes:
        for j in graph.nodes:
            for k in graph.nodes:
                if i != j and i != k and j != k:
                    nx.add_cycle(graph, [i, j, k])
    return graph


def get_graph_nodes(number_of_nodes):
    graph = nx.Graph()
    number_of_nodes = number_of_nodes+1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in graph.nodes:
        for j in graph.nodes:
            for k in graph.nodes:
                if i != j and i != k and j != k:
                    nx.add_cycle(graph, [i, j, k])
    return graph
