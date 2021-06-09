from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs import all_cycles_graph
from utils.functions import *


def run_test(n, k):
    start_time = datetime.datetime.now()
    time.sleep(0.001)
    print("Testing a custom graph with all cycles", end="\n")

    number_of_nodes = n
    # k = 15

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = all_cycles_graph.get_graph_nodes(number_of_nodes)
    before = all_cycles_graph.get_graph_nodes(number_of_nodes)
    # show_graph(before, "before")

    # find feedback vertex set #
    s, after = get_feedback_vertex_set(g, k)
    # after = prune_graph(before, s)

    if s is not None:
        print("Found feedback vertex set from size:" + str(len(s)))
    else:
        print("There is no solution")

    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "all cycles", len(before.nodes), len(before.edges), "bounded search tree", s, k)

    # show graphs #
    # if after is not None:
    #     show_graph(after, "after")


if __name__ == '__main__':
    for n in range(1, 14):
        run_test(n, 8)
