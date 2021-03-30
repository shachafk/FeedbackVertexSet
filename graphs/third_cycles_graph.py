import networkx as nx


def get_graph_nodes(number_of_nodes):
    graph = nx.MultiGraph()
    number_of_nodes = number_of_nodes + 1
    graph.add_nodes_from(range(1, number_of_nodes))
    for i in graph.nodes:
        for j in graph.nodes:
            for k in graph.nodes:
                if i != j and i != k and j != k:
                    if i % 3 == 0 and j % 3 == 0 and k % 3 == 0:
                        if not graph.has_edge(i, j):
                            graph.add_edge(i, j)
                        if not graph.has_edge(j, k):
                            graph.add_edge(j, k)
                        if not graph.has_edge(i, k):
                            graph.add_edge(i, k)
    for i in graph.nodes:
        for j in graph.nodes:
            if i < j and i % 2 != 0 and j % 2 != 0:
                graph.add_edge(i, j)
    return graph
