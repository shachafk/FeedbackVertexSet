import ctypes
import sys
import threading
import time

from utils.functions import *


class myThread(threading.Thread):
    def __init__(self, threadID, func, graph, k, name, test_name, daemon):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.func = func
        self.graph = graph.copy()
        self.k = k
        self._stop_event = threading.Event()
        self.sol = -1
        self.name = name
        self.setDaemon(daemon)
        self.test_name = test_name

    def run(self):
        print("Starting " + str(self.threadID))
        before = self.graph.copy()
        # find feedback vertex set #
        start_time = datetime.datetime.now()
        s, after = self.func(self.graph, self.k)
        if s is not None:
            print("Found feedback vertex set from size:" + str(len(s)))
            # show graphs #
            # show_two_graphs(before, after)
        else:
            print("there is no solution")
        # print runtime #
        end_time = datetime.datetime.now()
        print_runtime(start_time, end_time, self.test_name, len(before.nodes), len(before.edges), self.name, s, self.k)
        self.sol = s

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def get(self):
        return self.sol

    def raise_exception(self):
        self.stop()

    def exit(self):
        self.raise_exception()
        print("exiting")
        sys.exit(0)
