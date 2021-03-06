import itertools

from networkx import MultiGraph

from utils.functions import prune_graph, no_cycles, delete_nodes_deg_zero_one


def get_feedback_vertex_set(graph: MultiGraph, k: int):
    # nodes with degree zero or one cannot be part of a cycle so we remove them
    # deleted_nodes = delete_nodes_deg_zero_one(graph)

    if no_cycles(graph):
        return set(), graph

    nodes = graph.nodes()
    if len(nodes) <= k:
        return nodes, graph
    i = 1
    for subset in itertools.combinations(nodes, k):
        # print("Iteration number #" + str(i))
        # create new graph without current subset
        new_graph = prune_graph(graph.copy(), subset)
        i += 1
        if no_cycles(new_graph):
            return subset, new_graph

    return None, None
