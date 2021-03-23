
import networkx as nx


def reduction1(self, g: nx.MultiGraph, k):
    """
    If there is a loop at a vertex v, delete v from the graph and decrease k by 1.
    """
    changed = False
    vs = nx.nodes_with_selfloops(g)
    for v in vs:
        g.remove_node(v)
        k -= 1
        changed = True
    return k, vs, changed


def reduction3(self, g: nx.MultiGraph, k: int):
    """
    If there is a vertex v of degree at most 1, delete v.
    """
    changed = False
    for v in g.nodes():
        if g.degree(v) <= 1:
            g.remove_node(v)
            changed = True
    return k, None, changed


def reduction4(self, g: nx.MultiGraph, k: int):
    """
     If there is a vertex v of degree 2, delete v and connect its two neighbors by a new edge.
    """
    for v in g.nodes():
        if g.degree(v) == 2:
            # Delete v and make its neighbors adjacent.
            ne = g.neighbors(v)

            if len(ne) == 2: #v has 2 neighbors
                [n1, n2] = ne
            else: #v has one neighbor with 2 edges
                [n1] = ne
                n2 = n1

            g.remove_node(v)
            g.add_edge(n1, n2)

            return k, None, True

    return k, None, False


