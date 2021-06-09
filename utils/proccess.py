import multiprocessing
import sys

from utils.functions import *


class myProcess(multiprocessing.Process):
    def __init__(self, PID, func, graph, k, name, test_name, quit, foundit):
        multiprocessing.Process.__init__(self)
        self.threadID = PID
        self.func = func
        self.graph = graph.copy()
        self.k = k
        self.sol = -1
        self.name = name
        self.test_name = test_name
        self.foundit = foundit
        self.quit = quit
        self.daemon = True

    def run(self):
        start_time = datetime.datetime.now()
        time.sleep(0.001)
        print("Starting " + str(self.threadID) + " for k= " + str(self.k))
        before = self.graph.copy()
        # find feedback vertex set #
        if not self.quit.is_set():
            s, after = self.func(self.graph, self.k)
            if s is not None:
                print("Found feedback vertex set from size:" + str(len(s)))
                # show graphs #
                # show_two_graphs(before, after)
            else:
                print("there is no solution " + "for threadID= " + str(self.threadID) + " k= " + str(self.k))
            # print runtime #
            end_time = datetime.datetime.now()
            print_runtime_id(1, start_time, end_time, self.test_name, len(before.nodes), len(before.edges),
                             self.name, s, self.k)
            self.sol = s
            self.foundit.set()

    def get_sol(self):
        return self.sol
