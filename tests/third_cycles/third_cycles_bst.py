from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs.third_cycles_graph import get_graph_nodes
from utils.functions import *


def run_test(n, k):
    print("Testing a custom graph with third cycles", end="\n")

    number_of_nodes = n
    # k = 8

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    before = get_graph_nodes(number_of_nodes)

    # find feedback vertex set #
    start_time = datetime.datetime.now()
    s, after = get_feedback_vertex_set(g, k)
    after = prune_graph(before, s)
    print("Found feedback vertex set from size:" + str(len(s)))
    if s is not None and len(s) <= k:
        print("found solution")
    elif s is not None and len(s) > k:
        print("there is no solution")

    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "third cycles", len(before.nodes),len(before.edges), "bounded search tree", s, k)


# show graphs #
# show_two_graphs(before, after)


if __name__ == '__main__':
    for n in range(20, 49):
        if n % 2 == 0:
            run_test(n, 25)

