from algorithms.bruteforce import get_feedback_vertex_set
from graphs import bipartite_all_cycles_graph
from utils.functions import *

print("Testing a custom bipartite graph with no cycle", end="\n")

number_of_nodes = 10
k = 6
print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = bipartite_all_cycles_graph.get_graph_nodes(number_of_nodes)
before = bipartite_all_cycles_graph.get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, k)
print("Found feedback vertex set from size:" + str(len(s)))

# print runtime #
print_runtime(start_time, "bipartite_all_cycles", len(before.nodes), "bruteforce", s)

# show graphs #
show_two_graphs(before, after)
