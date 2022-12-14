from flask_smorest import Blueprint
from flask import request
from app.services import objective_service
from app.model.objective_response import ObjectiveResponseSchema
from app.model.objective_request import (
    TSPObjectiveEvaluationRequest,
    TSPObjectiveEvaluationRequestSchema,
    MaxCutObjectiveEvaluationRequest,
    MaxCutObjectiveEvaluationRequestSchema,
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
