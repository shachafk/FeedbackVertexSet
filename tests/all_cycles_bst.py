from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs import all_cycles_graph
from utils.functions import *

print("Testing a custom graph with all cycles", end="\n")

number_of_nodes = 18
k = 15

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = all_cycles_graph.get_graph_nodes(number_of_nodes)
before = all_cycles_graph.get_graph_nodes(number_of_nodes)
show_graph(before, "before")

# find feedback vertex set #
start_time = time.time()
s, after = get_feedback_vertex_set(g, k)
if s is not None:
    print("Found feedback vertex set from size:" + str(len(s)))
else:
    print("There is no solution")

# print runtime #
print_runtime(start_time, "all cycles", len(before.nodes), "bounded search tree", s)

# show graphs #
if after is not None:
    show_graph(after, "after")
