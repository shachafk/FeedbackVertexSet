from networkx import MultiGraph
from random import choice
import math


from utils.functions import no_cycles, prune_graph
from utils.reductions import run_reductions

"""
    run reduction rules FVS.1-FVS.5
    if k<0 - No instance case
    otherwise, we pick an edge e of G' uniformly at random and choose one endpoint of e independently and uniformly at random.
    we recurse on (G'-v, k'-1).
    If the recursive step returns a feedback vertex set X', then we return X := X' U {v} U X0
"""


def get_solution(graph, k):
    x0 = set()
    print("before reductions: nodes-" + str(len(graph.nodes)) + ", k-", str(k))
    k, x0 = run_reductions(graph, k)
    print("after reductions: nodes-" + str(len(graph.nodes)) + ", k-", str(k))

    if k < 0:
        print("there is not solution")
        return None

    if len(graph) == 0:  # if we got empty graph - x0 is the solution
        return x0

    # Pick a random edge, then a random end node of that edge
    rand_edge = choice(list(graph.edges()))
    v = choice(rand_edge)

    # we recurse on (G'-v, k'-1).
    graph.remove_node(v)
    xn = get_solution(graph, k - 1)

    if xn is None:
        # If the recursive step returns a failure, then we return a failure as well.
        return None
    else:
        # If the recursive step returns a feedback vertex set X', then we return X := X' U {v} U X0
        return xn.union({v}).union(x0)


def get_feedback_vertex_set(graph: MultiGraph, k: int):
    if no_cycles(graph):
        return set(), graph

    else:
        n = 4 ** k  # max number of iterations
        print("n: " + str(n))
        for i in range(1, n+1):
            print("iterations number #" + str(i))
            sol = get_solution(graph.copy(), k)
            if sol is None:
                print("couldn't find solution")
            else:
                print("found solution from size: " + str(len(sol)))
                return sol, graph

    return None, None
