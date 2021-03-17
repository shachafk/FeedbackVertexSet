import itertools
import matplotlib.pyplot as plt
import networkx as nx
import os.path
from pathlib import Path
from networkx.algorithms import bipartite

from networkx import Graph, find_cycle, NetworkXNoCycle
import time


def print_runtime(start_time, test,nodes ,algorithm, feedback):
    my_file = Path('runTime.txt')

    if not my_file.exists():
        with open('runTime.txt', 'a') as file:
            file.write("TEST;ALGORITHM;NUMBER_OF_NODES;VERTEX_FEEDBACK_SIZE;RUNTIME" + '\n')

    with open('runTime.txt', 'a') as file:
        file.write(test + ";" + algorithm + ";" + str(nodes) + ";"+str(len(feedback))+";" + str((time.time() - start_time)) + '\n')

    print("file runTime.txt was updated")


def show_graph(graph):
    nx.draw(graph)
    plt.show()


def show_two_graphs(before, after):
    if bipartite.is_bipartite(before):
        plt.figure("before")
        side_b_before = [n for n, d in before.nodes(data=True) if d["bipartite"] == 1]
        nx.draw_networkx(
            before,
            pos=nx.drawing.layout.bipartite_layout(before, side_b_before))

        plt.figure("after")
        side_b_after = [n for n, d in after.nodes(data=True) if d["bipartite"] == 1]
        nx.draw_networkx(
            after,
            pos=nx.drawing.layout.bipartite_layout(after, side_b_after))
    else:
        plt.figure("before")
        nx.draw_networkx(before)
        plt.figure("after")
        nx.draw_networkx(after)

    plt.show()


def no_cycles(g: Graph):
    try:
        find_cycle(g)
    except NetworkXNoCycle:
        return True
    return False


def prune_graph(g: Graph, s: set):
    new_nodes = [x for x in g.nodes() if x not in s]
    new_graph = g.subgraph(new_nodes)
    return new_graph


def delete_nodes_deg_zero_one(g: Graph):
    node_deleted = False
    nodes = list(g.nodes())
    for v in nodes:
        if g.degree(v) <= 1:
            g.remove_node(v)
            node_deleted = True
    return node_deleted
