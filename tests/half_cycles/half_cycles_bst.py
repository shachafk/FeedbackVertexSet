from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs.half_cycles_graph import get_graph_nodes
from utils.functions import *

print("Testing a custom graph with half cycles", end="\n")

number_of_nodes = 7
k = 4

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = get_graph_nodes(number_of_nodes)
before = get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, k)
after = prune_graph(before, s)

print("Found feedback vertex set from size:" + str(len(s)))
if s is not None and len(s) <= k:
    print("found solution")
elif s is not None and len(s) > k:
    print("there is no solution")

# print runtime #
print_runtime(start_time, "half cycles", len(before.nodes), "bounded search tree", s,k)

# show graphs #
show_two_graphs(before, after)
