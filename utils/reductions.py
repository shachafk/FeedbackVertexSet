import networkx as nx
from utils.functions import show_graph


def reduction1(g: nx.MultiGraph, k):
    """
    If there is a loop at a vertex v, delete v from the graph and decrease k by 1.
    """
    changed = False
    vs = list(nx.nodes_with_selfloops(g))
    for v in vs:
        g.remove_node(v)
        k -= 1
        changed = True
    return k, vs, changed


def reduction2(g: nx.MultiGraph, k: int):
    """
     If there is an edge of multiplicity larger than 2, reduce its multiplicity to 2.
    """
    changed = False
    for u in g.nodes():
        for v in g.neighbors(u):
            while g.number_of_edges(u, v) > 2:
                g.remove_edge(u, v)
                changed = True
    return k, None, changed


def reduction3(g: nx.MultiGraph, k: int):
    """
    If there is a vertex v of degree at most 1, delete v.
    """
    changed = False
    nodes = list(g.nodes())
    for v in nodes:
        if g.degree(v) <= 1:
            g.remove_node(v)
            changed = True
    return k, None, changed


def reduction4(g: nx.MultiGraph, k: int):
    """
     If there is a vertex v of degree 2, delete v and connect its two neighbors by a new edge.
    """
    for v in g.nodes():
        if g.degree(v) == 2:
            # Delete v and make its neighbors adjacent.
            ne = list(g.neighbors(v))

            if len(ne) == 2:  # v has 2 neighbors
                [n1, n2] = ne
            else:  # v has one neighbor with 2 edges
                [n1] = ne
                n2 = n1

            g.remove_node(v)
            g.add_edge(n1, n2)

            return k, None, True

    return k, None, False


def run_reductions(g: nx.MultiGraph, k: int):
    # reduction 1 can decrease k - the other reductions won't change k
    # reduction 1 can return X0 - the other reductions will return None
    # Need to check reduction 5 in the calling function
    x = set()
    while True:
        _continue = False
        for f in [reduction1, reduction2, reduction3, reduction4]:
            (k, x0, changed) = f(g, k)

            if changed:
                _continue = True
                show_graph(g, "")
                if x0 is not None:
                    x = x.union(x0)

        if not _continue:
            return k, x
