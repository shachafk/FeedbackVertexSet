from algorithms.bruteforce import get_feedback_vertex_set
from graphs.third_cycles_graph import get_graph_nodes
from utils.functions import *


def run_test(n, k):

    # number_of_nodes = 20
    # k = 8
    start_time = datetime.datetime.now()
    time.sleep(0.1)
    print("Testing a custom graph with third cycles", end="\n")

    number_of_nodes = n

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    before = get_graph_nodes(number_of_nodes)

    # find feedback vertex set #
    s, after = get_feedback_vertex_set(g, k)
    if s is not None:
        print("Found feedback vertex set from size:" + str(len(s)))
        # show graphs #
        # show_two_graphs(before, after)
    else:
        print("there is no solution")
    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "third cycles", len(before.nodes), len(before.edges), "bruteforce", s, k)


if __name__ == '__main__':
    for n in range(1, 20):
        run_test(n, 6)
        # if n % 2 == 0:
