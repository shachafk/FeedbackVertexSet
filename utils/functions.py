import itertools
import matplotlib.pyplot as plt
import networkx as nx

from networkx import Graph, find_cycle, NetworkXNoCycle
import time


def print_runtime(start_time, test, algorithm):
    with open('runTime.txt', 'a') as file:
        file.write("TEST [" + test + "] " + "ALGORITHM [" + algorithm + "] RUNTIME [" + str(
            (time.time() - start_time)) + "]" + '\n')
    print("file output\\runTime.txt was updated")


def show_graph(graph):
    nx.draw(graph)
    plt.show()


def show_two_graphs(before, after):
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
