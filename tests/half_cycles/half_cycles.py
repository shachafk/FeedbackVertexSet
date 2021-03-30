from algorithms.bruteforce import get_feedback_vertex_set
from graphs.half_cycles_graph import get_graph_nodes
from utils.functions import *

print("Testing a custom graph with half cycles", end="\n")

number_of_nodes = 20
k = 16

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = get_graph_nodes(number_of_nodes)
before = get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, k)
if s is not None:
    print("Found feedback vertex set from size:" + str(len(s)))
    print("found solution")
    show_two_graphs(before, after)

else:
    print("there is no solution")

# print runtime #
print_runtime(start_time, "half cycles", len(before.nodes), "bruteforce", s,k)

# show graphs #
