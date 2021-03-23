from algorithms.randomized import get_feedback_vertex_set
from graphs import one_cycle_graph
from utils.functions import *

print("Testing a custom graph with 1 cycle", end="\n")

number_of_nodes = 10

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = one_cycle_graph.get_graph_nodes(number_of_nodes)
before = one_cycle_graph.get_graph_nodes(number_of_nodes)

show_graph(before, "before")

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, 4)
print("Found feedback vertex set from size:" + str(len(s)))

# print runtime #
print_runtime(start_time, "one cycle", len(before.nodes), "randomized", s)

# show graphs #
show_graph(after, "after")