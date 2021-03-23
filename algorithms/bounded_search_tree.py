
from networkx import MultiGraph
from utils.reductions import run_reductions
from utils.functions import no_cycles


def get_feedback_vertex_set(graph: MultiGraph, k: int):
    if no_cycles(graph):
        return set(), graph

    sol = set()
    # run reductions 1-4
    k, x0 = run_reductions(graph, k)
    # add current solution to our solution, these are self-loop nodes
    if x0 is not None:
        sol = sol.union(x0)
    # reduction 5
    if k < 0:
        return None, None

    # we now have new instance (G', k') such that G' has min degree at least 3 and k' <= k
    # if graph is empty, we already found a solution
    if len(graph) == 0:
        return sol, graph

    # descending order of V(G) nodes according to vertex degrees
    nodes_sorted_by_degree = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    # get first 3*k vertices with largest degrees
    nodes_sorted_by_degree[0:3*k]

    # from the lemma, every solution x to FVS instance (G', k') contains at least one vertex from V3k'

    for v in nodes_sorted_by_degree:
        temp_graph = graph.copy()
        temp_graph.remove_node(v[0])
        x, g = get_feedback_vertex_set(temp_graph, k-1)
        if x is not None:
            return x, g



mg = MultiGraph()
mg.add_node(1)
mg.add_node(2)
mg.add_node(3)
mg.add_edge(1,2)
mg.add_edge(1,3)
mg.add_edge(1,1)
sorted_degrees = sorted(mg.degree, key=lambda x: x[1], reverse=True)
print(sorted_degrees)
print(sorted_degrees[0])
print(sorted_degrees[0][0])
k = 2
print(sorted_degrees[0:2])


