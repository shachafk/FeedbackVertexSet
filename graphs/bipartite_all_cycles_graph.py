import networkx as nx


def get_graph_nodes(number_of_nodes):
    graph = nx.Graph()
    number_of_nodes = number_of_nodes + 1
    half = int(number_of_nodes / 2) + 1
    graph.add_nodes_from(range(1, half), bipartite=0)
    graph.add_nodes_from(range(half, number_of_nodes), bipartite=1)

    nodes_to_add_0 = [x for x in range(1, half)]
    nodes_to_add_1 = [x for x in range(half, number_of_nodes)]

    for i in nodes_to_add_0:
        for j in nodes_to_add_1:
            graph.add_edge(i, j)
    return graph
