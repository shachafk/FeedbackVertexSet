from algorithms.bounded_search_tree import get_feedback_vertex_set as bst_func
from algorithms.bruteforce import get_feedback_vertex_set as bf_func
from algorithms.randomized import get_feedback_vertex_set as randomized_func
from graphs.third_cycles_graph import get_graph_nodes
from utils.thread import myThread


def run_test(n, k):
    print("Testing a custom graph with third cycles - 3 algorithms", end="\n")

    number_of_nodes = n
    # k = 8

    print("Number of nodes: " + str(number_of_nodes))

    # get graph#
    g = get_graph_nodes(number_of_nodes)
    # Create new threads
    thread1 = myThread(1, bf_func, g, k, "bruteforce", "third cycle", daemon=True)
    thread2 = myThread(2, randomized_func, g, k, "randomized", "third cycle", daemon=True)
    thread3 = myThread(3, bst_func, g, k, "bst", "third cycle", daemon=True)

    print("threads created")

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()

    j = 0
    while thread1.get() == -1 and thread2.get() == -1 and thread3.get() == -1:
        j += 1

    print("one thread is done")

    print("exiting")

    return


if __name__ == '__main__':
    run_test(20, 8)
