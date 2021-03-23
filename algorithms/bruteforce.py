import itertools

from networkx import MultiGraph

from utils.functions import delete_nodes_deg_zero_one, prune_graph, no_cycles


def get_feedback_vertex_set(graph: MultiGraph):
    if no_cycles(graph):
        return set(), graph

    # nodes with degree zero or one cannot be part of a cycle so we remove them
    delete_nodes_deg_zero_one(graph)

    nodes = graph.nodes()
    for L in range(1, len(nodes) + 1):
        for subset in itertools.combinations(nodes, L):
            # create new graph without current subset
            new_graph = prune_graph(graph, subset)

            if no_cycles(new_graph):
                return subset, new_graph

    return set(), None
