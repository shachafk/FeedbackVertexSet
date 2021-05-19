from algorithms.bruteforce import get_feedback_vertex_set
from graphs.half_cycles_graph import get_graph_nodes
from utils.functions import *


def run_test(n, k):
    start_time = datetime.datetime.now()
    time.sleep(0.1)
    print("Testing a custom graph with half cycles", end="\n")

    number_of_nodes = n
    # k = 16

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    before = get_graph_nodes(number_of_nodes)

    # find feedback vertex set #

    s, after = get_feedback_vertex_set(g, k)
    if s is not None:
        print("Found feedback vertex set from size:" + str(len(s)))
        print("found solution")
        # show_two_graphs(before, after)

    else:
        print("there is no solution")

    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "half cycles", len(before.nodes), len(before.edges), "bruteforce", s, k)

    # show graphs #


if __name__ == '__main__':
    for n in range(6, 20):
        run_test(n, 10)
        # if n % 2 == 0:
