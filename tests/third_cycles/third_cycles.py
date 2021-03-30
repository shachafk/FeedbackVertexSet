from algorithms.bruteforce import get_feedback_vertex_set
from graphs.third_cycles_graph import get_graph_nodes
from utils.functions import *

print("Testing a custom graph with third cycles", end="\n")

number_of_nodes = 25
k = 12

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = get_graph_nodes(number_of_nodes)
before = get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, k)
if s is not None:
    print("Found feedback vertex set from size:" + str(len(s)))
    # show graphs #
    show_two_graphs(before, after)
else:
    print("there is no solution")
# print runtime #
print_runtime(start_time, "third cycles", len(before.nodes), "bruteforce", s,k)


