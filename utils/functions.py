import itertools
import datetime

import matplotlib.pyplot as plt
import networkx as nx
import os.path
from pathlib import Path
from networkx.algorithms import bipartite

from networkx import Graph, find_cycle, NetworkXNoCycle
import time


def print_runtime(start_time, end_time, test, nodes, edges, algorithm, feedback, k):
    my_file = Path('../runTime.txt')
    if feedback is None:
        sol = "None"
    elif len(feedback) > k:
        print("found larger feedback set from size ", str(len(feedback)))
        sol = "None"
    else:
        sol = str(len(feedback))
    timediff = (end_time - start_time).total_seconds()
    if not my_file.exists():
        with open('../runTime.txt', 'a') as file:
            file.write("TEST;ALGORITHM;NUMBER_OF_NODES;NUMBER_OF_EDGES;VERTEX_FEEDBACK_SIZE;RUNTIME;K" + '\n')

    with open('../runTime.txt', 'a') as file:
        file.write(test + ";" + algorithm + ";" + str(nodes) + ";" + str(edges) + ";" + sol + ";" + str(
            timediff) + ";" + str(k) + '\n')

    print("file runTime.txt was updated")


def print_runtime_id(threadID, start_time, end_time, test, nodes, edges, algorithm, feedback, k):
    filename = "../runTime_" + str(threadID) + ".txt"
    my_file = Path(filename)
    if feedback is None:
        sol = "None"
    elif len(feedback) > k:
        sol = "None"
    else:
        sol = str(len(feedback))
    timediff = (end_time - start_time).total_seconds()
    if not my_file.exists():
        with open(filename, 'a') as file:
            file.write("TEST;ALGORITHM;NUMBER_OF_NODES;NUMBER_OF_EDGES;VERTEX_FEEDBACK_SIZE;RUNTIME;K" + '\n')

    with open(filename, 'a') as file:
        file.write(test + ";" + algorithm + ";" + str(nodes) + ";" + str(edges) + ";" + sol + ";" + str(
            timediff) + ";" + str(k) + '\n')

    print("file " + filename + " was updated")


def show_graph(g, figure):
    pos = nx.circular_layout(g)

    self_loop = set(nx.nodes_with_selfloops(g))
    mg_minus_self_loop = set(g.nodes) - self_loop

    nx.draw_networkx(g, pos)

    nx.draw_networkx_nodes(g, pos, mg_minus_self_loop, node_color="r", node_size=250, alpha=1)
    nx.draw_networkx_nodes(g, pos, self_loop, node_color="b", node_size=250, alpha=1)
    ax = plt.gca()
    for e in g.edges:
        if (len(e) > 2):
            style = 0.3 * e[2]
        else:
            style = 0
        ax.annotate("",
                    xy=pos[e[0]], xycoords='data',
                    xytext=pos[e[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-", color="0.5",
                                    shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=rrr".replace('rrr', str(style)
                                                                           ),
                                    ),
                    )

    plt.axis('off')
    plt.figure(figure)
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

        plt.show()

    else:
        show_graph(before, "before")
        show_graph(after, "after")


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
    nodes = list(g.nodes())
    deleted_nodes = set()
    for v in nodes:
        if g.degree(v) <= 1:
            g.remove_node(v)
            deleted_nodes.add(v)
    return deleted_nodes
