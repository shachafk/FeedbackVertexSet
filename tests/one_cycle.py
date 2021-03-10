import networkx as nx
import time
from utils.functions import *
from graphs import small_graph
from algorithms.bruteforce import get_feedback_vertex_set

print("Testing a custom graph with 1 cycle", end="\n")
start_time = time.time()
g = small_graph.get_graph()
before = small_graph.get_graph()
s, after = get_feedback_vertex_set(g)
show_two_graphs(before, after)
print(len(s))
print_runtime(start_time, "one cycle", "bruteforce")
