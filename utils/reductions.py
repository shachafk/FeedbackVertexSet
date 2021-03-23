from typing import List
import networkx as nx
from utils.functions import *
from networkx.drawing.nx_agraph import to_agraph
import graphviz
from networkx.drawing.nx_pydot import write_dot


# def reduction1(self, g: nx.MultiGraph, k: int) -> (int, List[int], bool):
def reduction2(self, g: nx.MultiGraph, k: int):
    changed = False
    for u in g.nodes():
        for v in g.neighbors(u):
            while g.number_of_edges(u, v) > 2:
                g.remove_edge(u, v)
                changed = True

    return k, None, changed

# def reduction3(self, g: nx.MultiGraph, k: int) -> (int, List[int], bool):
# def reduction4(self, g: nx.MultiGraph, k: int) -> (int, List[int], bool):
# def reduction5(self, g: nx.MultiGraph, k: int) -> (int, List[int], bool):
