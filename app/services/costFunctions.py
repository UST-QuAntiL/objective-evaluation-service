from qiskit_optimization.applications import Knapsack
from abc import ABC, abstractmethod
import numpy as np


class CostFunction(ABC):
    @abstractmethod
    def evaluate(self, bitstring, problem_instance, **kwargs):
        pass

    def computeCosts(self, counts, problem_instance):
        allCosts = np.array(
            [self.evaluate(x, problem_instance) for x in list(counts.keys())]
        )
        z = zip(list(counts.keys()), list(counts.values()), list(allCosts))
        z = list(z)
        return z


class MaxCutFunction(CostFunction):
    def __init__(self):
        self.cached_graph = None
        self.cached_cut_size = {}
        pass

    # Computes each bitstrings cost and caches it
    # Costs are NEGATED such that they can be minimized
    def evaluate(self, bitstring, problem_instance, **kwargs):
        problem_instance = np.array(problem_instance)
        n_vertices = problem_instance.shape[0]
        cut_string = "".join(str(bitstring))
        if (
            cut_string in self.cached_cut_size.keys()
            and hash(str(problem_instance)) == self.cached_graph
        ):
            return self.cached_cut_size.get(cut_string)
        elif not hash(str(problem_instance)) == self.cached_graph:
            self.cached_graph = hash(str(problem_instance))
            self.cached_cut_size = {}
        C = 0
        for i in range(n_vertices):
            for j in range(i):
                C += problem_instance[i, j] * (not bitstring[i] == bitstring[j])
        self.cached_cut_size[cut_string] = -C
        return -C


class TspFunction(CostFunction):
    def __init__(self):
        pass

    def evaluate(self, bitstring, problem_instance, **kwargs):
        """
        Args:
        counts: dict
                key as bitstring, val as count

        AdjMatrix: Adjacency matrix as numpy array
        """
        n = len(problem_instance)
        path = self.path_from_string(bitstring, n)
        path_length = self.compute_path_length(path + [path[0]], problem_instance)
        return path_length

    def path_from_string(self, string, amount_nodes):
        path = [-1] * amount_nodes
        for i in range(amount_nodes):
            node_string = string[i * amount_nodes : i * amount_nodes + amount_nodes]
            node_position = node_string.find("1")
            path[node_position] = i
        return path

    def compute_path_length(self, path, problem_instance):
        length = 0
        for i, j in zip(path[:-1], path[1:]):
            length += problem_instance[i][j]
        return length


class KnapsackFunction(CostFunction):
    def __init__(self):
        pass

    def evaluate(self, bitstring, problem_instance, **kwargs):
        print("Evaluating knapsack results...")
        items = problem_instance.get("items")
        values = [d["value"] for d in items]
        print("Values: ", values)
        weights = [d["weight"] for d in items]
        print("Weights: ", weights)
        max_weights = problem_instance.get("max_weights")
        print("Max weight: ", max_weights)

        problem = Knapsack(values=values, weights=weights, max_weight=max_weights)
        most_likely_result = problem.sample_most_likely(bitstring)
        print("Most likly result: ", most_likely_result)
        result_list = problem.interpret(most_likely_result)
        print("List of items to use: ", result_list)

        # TODO: calculate costs

        return -100000
