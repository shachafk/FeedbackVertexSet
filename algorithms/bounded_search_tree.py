from networkx import MultiGraph
from utils.reductions import run_reductions
from utils.functions import no_cycles


def get_feedback_vertex_set(graph: MultiGraph, k: int):
    if no_cycles(graph):
        return set(), graph

    sol = set()
    # run reductions 1-4
    # print("before reductions: nodes-" + str(len(graph.nodes)) + ", k-", str(k))
    k, x0 = run_reductions(graph, k)
    # print("after reductions: nodes-" + str(len(graph.nodes)) + ", k-", str(k))
    # add current solution to our solution, these are self-loop nodes
    if x0 is not None:
        sol = sol.union(x0)
    # reduction 5
    if k < 0:
        # print("invalid k")
        return None, None

    # we now have new instance (G', k') such that G' has min degree at least 3 and k' <= k
    # if graph is empty, we already found a solution
    if len(graph) == 0:
        return sol, graph

    # descending order of V(G) nodes according to vertex degrees
    nodes_sorted_by_degree = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    # get first 3*k vertices with largest degrees
    nodes_sorted_by_degree[0:3 * k]

    # from the lemma, every solution x to FVS instance (G', k') contains at least one vertex from V3k'
    for v in nodes_sorted_by_degree:
        temp_graph = graph.copy()
        node = v[0]
        temp_graph.remove_node(node)
        x, g = get_feedback_vertex_set(temp_graph, k - 1)
        if x is not None:
            return x.union({node}).union(sol), g
    return None, None
