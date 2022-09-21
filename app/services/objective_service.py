from app.model.objective_request import (
    TSPObjectiveEvaluationRequest,
    MaxCutObjectiveEvaluationRequest,
)
from app.model.objective_response import ObjectiveResponse
from app.services.objectiveFunctions import F_CVaR, F_EE, F_Gibbs
from app.services.visualization import TspVisualization, MaxCutVisualization
from app.constants import *


def generate_tsp_objective_response(input: TSPObjectiveEvaluationRequest):
    objective_function = getObjectiveFunction(
        input.objFun, TSP, **input.objFun_hyperparameters
    )
    objective_value = objective_function.evaluate(input.counts, input.adj_matrix)

    if input.visualization:
        graphic = TspVisualization().visualize(
            counts=objective_function.counts_cost, problem_instance=input.adj_matrix
        )
    else:
        graphic = None

    print("value", objective_value)
    return ObjectiveResponse(objective_value, graphic, input)


def generate_max_cut_objective_response(input: MaxCutObjectiveEvaluationRequest):
    objective_function = getObjectiveFunction(
        input.objFun, MAX_CUT, **input.objFun_hyperparameters
    )
    objective_value = objective_function.evaluate(input.counts, input.adj_matrix)

    graphic = (
        MaxCutVisualization().visualize(
            counts=objective_function.counts_cost, problem_instance=input.adj_matrix
        )
        if input.visualization
        else None
    )
    print("value", objective_value)
    return ObjectiveResponse(objective_value, graphic, input)


def getObjectiveFunction(objFun, costFun, **kwargs):
    if objFun.lower() == EXPECTATION:
        return F_EE(costFun)
    elif objFun.lower() == GIBBS:
        return F_Gibbs(costFun, eta=kwargs["eta"] or 10)
    elif objFun.lower() == CVAR:
        return F_CVaR(costFun, alpha=kwargs["alpha"] or 0.2)
