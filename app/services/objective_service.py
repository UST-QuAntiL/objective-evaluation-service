from app.helperfunctions import take_second, convert_cost_object_to_dict, find_period
from app.model.objective_request import (
    TSPObjectiveEvaluationRequest,
    MaxCutObjectiveEvaluationRequest,
    KnapsackObjectiveEvaluationRequest,
    ShorDiscreteLogObjectiveEvaluationRequest,
)
from app.model.objective_response import ObjectiveResponse
from app.services.objectiveFunctions import F_CVaR, F_EE, F_Gibbs
from app.services.visualization import TspVisualization, MaxCutVisualization
from app.constants import *
from qiskit_optimization.applications import Knapsack
import math
import numpy as np


def generate_tsp_objective_response(input: TSPObjectiveEvaluationRequest):
    objective_function = getObjectiveFunction(
        input.objFun, TSP, **input.objFun_hyperparameters
    )
    objective_value = objective_function.evaluate(input.counts, input.adj_matrix)
    cost_dict = convert_cost_object_to_dict(objective_function.counts_cost)

    if input.visualization:
        graphic = TspVisualization().visualize(
            counts=objective_function.counts_cost, problem_instance=input.adj_matrix
        )
    else:
        graphic = None

    print("value", objective_value)

    return ObjectiveResponse(objective_value, cost_dict, graphic)


def generate_max_cut_objective_response(input: MaxCutObjectiveEvaluationRequest):
    objective_function = getObjectiveFunction(
        input.objFun, MAX_CUT, **input.objFun_hyperparameters
    )
    objective_value = objective_function.evaluate(input.counts, input.adj_matrix)
    cost_dict = convert_cost_object_to_dict(objective_function.counts_cost)

    graphic = (
        MaxCutVisualization().visualize(
            counts=objective_function.counts_cost, problem_instance=input.adj_matrix
        )
        if input.visualization
        else None
    )

    print("value", objective_value)
    return ObjectiveResponse(objective_value, cost_dict, graphic)


def generate_knapsack_objective_response(input: KnapsackObjectiveEvaluationRequest):
    print("Evaluating knapsack results...")
    values = [d["value"] for d in input.items]
    print("Values: ", values)
    weights = [d["weight"] for d in input.items]
    print("Weights: ", weights)
    print("Max weight: ", input.max_weights)

    problem = Knapsack(values=values, weights=weights, max_weight=input.max_weights)
    most_likely_result = problem.sample_most_likely(input.counts)
    print("Most likely result: ", most_likely_result)
    result_list = problem.interpret(most_likely_result)
    print("List of items to use: ", result_list)

    objective_value = sum(values)
    overall_weight = 0
    for i in range(len(result_list)):
        print("Selected package with ID: ", i)

        if i > (len(values) - 1):
            print("Package with index not available...")
            objective_value += 50
        else:
            print("Value: ", values[i])
            objective_value -= values[i]
            overall_weight += weights[i]

    print("Overall weight: ", overall_weight)
    if overall_weight > input.max_weights:
        print("Penalty as weight is higher than allowed max weight!")
        objective_value += input.max_weights - overall_weight

    print("Objective value: ", objective_value)
    result = "".join(str(x) for x in most_likely_result)
    print("Result bit string: ", result)
    costs = {result: objective_value}
    print("Costs: ", costs)
    return ObjectiveResponse(objective_value, [costs], None)


def generate_shor_discrete_log_objective_response(
    input: ShorDiscreteLogObjectiveEvaluationRequest,
):
    if input.n == -1:
        n = math.ceil(math.log(input.p, 2))
    else:
        n = input.n
    res = list()
    print("executed circuit")
    for result in input.counts.keys():
        # split result measurements
        result_s = result.split(" ")
        m_stage1 = int(result_s[1], 2)
        m_stage2 = int(result_s[0], 2)

        res.append((m_stage1, m_stage2, input.counts[result]))

    num_fail = 0
    num_success = 0

    correct_m = -1

    for (y1, y2, freq) in res:

        # period has to be calculated
        r = find_period(res, n, input.p, input.g)

        # k is inferred from the measurement result from first stage
        k = int(round((y1 * r) / (2**n), 0))
        print("k = ", k)

        # m (the discrete log) is calculated by using the congruence:
        # ((km mod r)/r)*2^n = m_stage2
        # v = m_stage2*r/2^n
        v = (y2 * r) / (2**n)
        # print("v=", v)  # = km mod r

        # k inverse exists?
        if np.gcd(k, r) == 1:
            kinv = pow(k, -1, r)
            # print("kInv=", kinv)
            m = int(round(v * kinv % r, 0))
            # print("found m=", m)

            # check if this m actually fits
            if (input.g**m % input.p) == input.b:
                correct_m = m

    graphic = None

    print("calculated m ", correct_m)
    return ObjectiveResponse(correct_m, {}, graphic)


def getObjectiveFunction(objFun, costFun, **kwargs):
    if EXPECTATION in objFun.lower():
        return F_EE(costFun)
    elif objFun.lower() == GIBBS:
        return F_Gibbs(costFun, eta=kwargs["eta"] or 10)
    elif objFun.lower() == CVAR:
        return F_CVaR(costFun, alpha=kwargs["alpha"] or 0.2)
