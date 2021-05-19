from algorithms.bounded_search_tree import get_feedback_vertex_set
from graphs import one_cycle_graph
from utils.functions import *

print("Testing a custom graph with 1 cycle", end="\n")

number_of_nodes = 10
k = 4
print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = one_cycle_graph.get_graph_nodes(number_of_nodes)
before = one_cycle_graph.get_graph_nodes(number_of_nodes)

# show_graph(before, "before")

# find feedback vertex set #
start_time = datetime.datetime.now()
s, after = get_feedback_vertex_set(g, k)
after = prune_graph(before, s)
print("Found feedback vertex set from size:" + str(len(s)))

# print runtime #
end_time = datetime.datetime.now()
print_runtime(start_time, end_time, "one cycle", len(before.nodes),len(before.edges), "bounded search tree", s, k)

# show graphs #
# show_graph(after, "after")
