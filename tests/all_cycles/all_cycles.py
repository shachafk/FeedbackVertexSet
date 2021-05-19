from algorithms.bruteforce import get_feedback_vertex_set
from graphs import all_cycles_graph
from utils.functions import *


def run_test(n, k):
    start_time = datetime.datetime.now()
    time.sleep(0.1)
    print("Testing a custom graph with all cycles", end="\n")

    number_of_nodes = n
    # k = 16

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = all_cycles_graph.get_graph_nodes(number_of_nodes)
    before = all_cycles_graph.get_graph_nodes(number_of_nodes)

    # find feedback vertex set #
    s, after = get_feedback_vertex_set(g, k)
    if s is not None and len(s) <= k:
        print("Found feedback vertex set from size:" + str(len(s)))
        print("found solution")
    elif s is not None and len(s) > k:
        print("there is no solution")

    # print runtime #
    end_time = datetime.datetime.now()
    print_runtime(start_time, end_time, "all cycles", len(before.nodes), len(before.edges), "bruteforce", s, k)


# show graphs #
# show_two_graphs(before, after)
if __name__ == '__main__':
    for n in range(1, 12):
        run_test(n, 8)
        # if n % 2 == 0:
