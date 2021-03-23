from algorithms.bruteforce import get_feedback_vertex_set
from graphs import all_cycles_graph
from utils.functions import *

print("Testing a custom graph with all cycles", end="\n")

number_of_nodes = 5

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = all_cycles_graph.get_graph_nodes(number_of_nodes)
before = all_cycles_graph.get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g)
print("Found feedback vertex set from size:" + str(len(s)))

# print runtime #
print_runtime(start_time, "all cycles", len(before.nodes), "bruteforce", s)

# show graphs #
show_two_graphs(before, after)
