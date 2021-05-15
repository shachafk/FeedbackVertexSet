from algorithms.bruteforce import get_feedback_vertex_set
from graphs import all_cycles_graph
from utils.functions import *

print("Testing a custom graph with all cycles", end="\n")

number_of_nodes = 18
k = 16

print("Number of nodes: " + str(number_of_nodes))

# get graph#
g = all_cycles_graph.get_graph_nodes(number_of_nodes)
before = all_cycles_graph.get_graph_nodes(number_of_nodes)

# find feedback vertex set #
start_time = datetime.datetime.now()
s, after = get_feedback_vertex_set(g, k)
print("Found feedback vertex set from size:" + str(len(s)))
if s is not None and len(s) <= k:
    print("found solution")
elif s is not None and len(s) > k:
    print("there is no solution")

# print runtime #
print_runtime(start_time, "all cycles", len(before.nodes), "bruteforce", s,k)

# show graphs #
show_two_graphs(before, after)
