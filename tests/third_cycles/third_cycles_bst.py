from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs.third_cycles_graph import get_graph_nodes
from utils.functions import *


def run_test(n, k):
    start_time = datetime.datetime.now()
    time.sleep(0.001)

    print("Testing a custom graph with third cycles", end="\n")

    number_of_nodes = n
    # k = 8

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    before = get_graph_nodes(number_of_nodes)

    # find feedback vertex set #
    s, after = get_feedback_vertex_set(g, k)
    # after = prune_graph(before, s)
    if s is not None and len(s) <= k:
        print("Found feedback vertex set from size:" + str(len(s)))
        print("found solution")
    elif s is not None and len(s) > k:
        print("there is no solution")

    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "third cycles", len(before.nodes), len(before.edges), "bounded search tree", s,
                  k)


# show graphs #
# show_two_graphs(before, after)


if __name__ == '__main__':
    for k in range(1, 9):
        run_test(20, k)