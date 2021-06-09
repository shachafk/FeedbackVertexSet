import multiprocessing as mp

from algorithms.bounded_search_tree import get_feedback_vertex_set as bst_func
from algorithms.bruteforce import get_feedback_vertex_set as bf_func
from algorithms.randomized import get_feedback_vertex_set as randomized_func
from graphs.half_cycles_graph import get_graph_nodes
from utils.proccess import myProcess


def run_test(n, k):
    print("Testing a custom graph with half cycles - 3 algorithms", end="\n")

    number_of_nodes = n

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    # Create new threads

    quit = mp.Event()
    foundit = mp.Event()

    process1 = myProcess(1, bf_func, g, k, "bruteforce", "half cycle", quit, foundit)
    process2 = myProcess(2, randomized_func, g, k, "randomized", "half cycle", quit, foundit)
    process3 = myProcess(3, bst_func, g, k, "bst", "half cycle", quit, foundit)

    jobs = [process1, process2, process3]

    print("process created")
    for j in jobs:
        j.start()

    foundit.wait()
    quit.set()

    for j in jobs:
        j.terminate()

    print("exiting")


if __name__ == '__main__':
    for k in range(8, 9):
        # if n % 2 == 0:
        run_test(15, k)
