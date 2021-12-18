import algorithms.LSTM
import random
import numpy as np
import torch as tr
import os
import pickle


class DfsTreeSearchAlgorithmWithDistribution:
    def __init__(self):
        self.norm_hist_candidates = []
        self.list_historical_candidates = []
        self.tree_nodes_collections = []

        candidates = []

        for i in range(25):
            n = np.random.choice(11, 20, p=[0.05, 0.1, 0.05, 0.2, 0.1, 0.1, 0.05, 0.1, 0.1, 0.1, 0.05])
            candidates.append(n)

        np_samples = np.array(candidates).reshape(25 * 20, 1)
        self.dist_sample = np_samples.squeeze().tolist()
        self.root = None
        self.prev_node_count = 0
        pass

    def name(self):
        return "Depth First Tree Algorithm WithDistribution"

    def __str__(self, self_print=False, print_nodes=False):
        cnt = 0
        if self.root is not None and isinstance(self.root, SimpleTreeNode):
            cnt = self.root.count_search_node_numbers()
        str_result = "Search nodes count: {cnt}\r\n".format(cnt=cnt + self.prev_node_count)
        print(str_result)

    ## return true or false , selected index
    def decide(self, current_index, current_value):
        dt2 = round(self.norm(current_value,0,10))

        if(len(self.list_historical_candidates)>0):
            dt2 = round(self.norm(current_value - min(self.list_historical_candidates),
                                  0,10))

        self.norm_hist_candidates.append(dt2)
        self.list_historical_candidates.append(current_value)

        root = None
        current = None

        for item in self.list_historical_candidates:
            node = SimpleTreeNode(item, current)
            if root is None:
                root = node
                # keep the root
            current = node

        list_exp_values = []

        # the current is the search tree
        # search 100 steps with the expected greatest value
        current_index = 0
        sub_current = current
        current_node_count = 0
        current_exp_sum = 0.0
        while True:
            for i in range(5):
                item2 = self.dist_sample[current_index]
                node = SimpleTreeNode(item2, sub_current)
                z = node.expected_value()
                current_exp_sum += z
                sub_current = node
                current_node_count += 1
                self.prev_node_count += 1
                current_index += 1

            if current_index >= len(self.dist_sample):
                break
        pass


        # sub_current is the expected max in 100 tries
        if dt2 >= (current_exp_sum / current_node_count):
            return True, current_value

        # fake implementation to ensure LSTM algorithm integration
        return False, current_value

    def norm(self, dt, left, right):
        dt2 = dt / 100.0
        range = right - left
        return left + (range * dt2)


class SimpleTreeNode:
    def __init__(self, number: int, parent=None):
        self.number = number
        self.parent = parent
        self.children = []

    def append_children(self, node):
        if node is not None and isinstance(node, SimpleTreeNode):
            self.children.append(node)

    def get_children(self):
        return self.children

    def get_parent(self):
        if self.parent is not None and isinstance(self.parent, SimpleTreeNode):
            return self.parent

        return None

    def get_search_path(self):
        path_list = [self.number]
        while self.parent is not None:
            path_list.insert(0, (self).number)
            self.parent = self.parent.get_parent()

        return path_list

    def count_search_node_numbers(self):
        cnt = 1

        cs = self.get_children()

        if cs is not None:
            for c in cs:
                cnt += self.count_search_node_numbers()

        return cnt

    def expected_value(self):
        list = self.get_search_path()  # at least one as self
        exp_value = (sum(list) + 0.0) / (0.0 + len(list))
        return exp_value
