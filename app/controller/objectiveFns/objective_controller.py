from flask_smorest import Blueprint
from flask import request
from app.services import objective_service
from app.model.objective_response import ObjectiveResponseSchema
from app.model.objective_request import (
    TSPObjectiveEvaluationRequest,
    TSPObjectiveEvaluationRequestSchema,
    MaxCutObjectiveEvaluationRequest,
    MaxCutObjectiveEvaluationRequestSchema,
    KnapsackObjectiveEvaluationRequest,
    KnapsackObjectiveEvaluationRequestSchema,
    ShorDiscreteLogObjectiveEvaluationRequestSchema,
    ShorDiscreteLogObjectiveEvaluationRequest,
)

blp = Blueprint(
    "objective",
    __name__,
    url_prefix="/objective",
    description="compute objective value from counts",
)


@blp.route("/tsp", methods=["POST"])
@blp.arguments(
    TSPObjectiveEvaluationRequestSchema,
    example=dict(
        adj_matrix=[[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]],
        counts={"1" * 16: 100, "0" * 16: 100},
        objFun="Expectation",
        visualization=True,
    ),
)
@blp.response(200, ObjectiveResponseSchema)
def tsp(json: TSPObjectiveEvaluationRequest):
    print(json)
    if json:
        return objective_service.generate_tsp_objective_response(
            TSPObjectiveEvaluationRequest(**json)
        )


@blp.route("/max-cut", methods=["POST"])
@blp.arguments(
    MaxCutObjectiveEvaluationRequestSchema,
    example={
        "adj_matrix": [
            [0, 3, 3, 6, 9, 1],
            [3, 0, 4, 4, -8, 4],
            [3, 4, 0, 3, -7, 1],
            [6, 4, 3, 0, -7, 6],
            [9, -8, -7, -7, 0, -5],
            [1, 4, 1, 6, -5, 0],
        ],
        "counts": {
            "100001": 10,
            "011110": 20,
            "100000": 30,
            "010110": 40,
            "110000": 50,
        },
        "objFun": "Expectation",
        "visualization": "True",
    },
)
@blp.response(200, ObjectiveResponseSchema)
def max_cut(json: MaxCutObjectiveEvaluationRequest):
    print(json)
    if json:
        return objective_service.generate_max_cut_objective_response(
            MaxCutObjectiveEvaluationRequest(**json)
        )


@blp.route("/knapsack", methods=["POST"])
@blp.arguments(
    KnapsackObjectiveEvaluationRequestSchema,
    example={
        "items": [
            {"value": 5, "weight": 2},
            {"value": 2, "weight": 1},
            {"value": 3, "weight": 2},
        ],
        "max_weights": 20,
        "counts": {
            "100001": 10,
            "011110": 20,
            "100000": 30,
            "010110": 40,
            "110000": 50,
        },
        "objFun": "Expectation",
        "visualization": "True",
    },
)
@blp.response(200, ObjectiveResponseSchema)
def max_cut(json: KnapsackObjectiveEvaluationRequest):
    print(json)
    if json:
        return objective_service.generate_knapsack_objective_response(
            KnapsackObjectiveEvaluationRequest(**json)
        )


@blp.route("/shor/discreteLog", methods=["POST"])
@blp.arguments(
    ShorDiscreteLogObjectiveEvaluationRequestSchema,
    example={
        "b": 2,
        "g": 5,
        "p": 7,
        "n": 3,
        "counts": {
            "101 101": 4,
            "000 100": 17,
            "011 111": 15,
            "101 001": 13,
            "000 000": 12,
            "110 010": 1,
            "101 110": 3,
            "000 101": 1,
            "010 011": 2,
            "011 011": 5,
            "011 110": 3,
            "011 010": 2,
            "110 001": 2,
            "010 111": 3,
            "010 110": 1,
            "011 100": 3,
            "001 011": 2,
            "110 101": 2,
            "100 111": 2,
            "011 101": 1,
            "110 000": 1,
            "011 101": 1,
            "110 000": 1,
            "011 001": 1,
            "011 000": 1,
            "101 010": 1,
        },
        "objFun": "Expectation",
        "visualization": "False",
    },
)
@blp.response(200, ObjectiveResponseSchema)
def shor_discrete_log(json: ShorDiscreteLogObjectiveEvaluationRequest):
    print(json)
    if json:
        return objective_service.generate_shor_discrete_log_objective_response(
            ShorDiscreteLogObjectiveEvaluationRequest(**json)
        )
