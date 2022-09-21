import marshmallow as ma
from marshmallow import pre_load, ValidationError
import numpy as np


class TSPObjectiveEvaluationRequest:
    def __init__(
        self, adj_matrix, counts, objFun, objFun_hyperparameters={}, visualization=False
    ):
        self.adj_matrix = adj_matrix
        self.counts = counts
        self.objFun = objFun
        self.visualization = visualization
        self.objFun_hyperparameters = objFun_hyperparameters


class TSPObjectiveEvaluationRequestSchema(ma.Schema):
    adj_matrix = ma.fields.List(ma.fields.List(ma.fields.Float()), required=True)
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    objFun = ma.fields.Str(required=True)
    visualization = ma.fields.Boolean(required=False)
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)


class MaxCutObjectiveEvaluationRequest:
    def __init__(
        self, adj_matrix, counts, objFun, objFun_hyperparameters={}, visualization=False
    ):
        self.adj_matrix = adj_matrix
        self.counts = counts
        self.objFun = objFun
        self.visualization = visualization
        self.objFun_hyperparameters = objFun_hyperparameters


class MaxCutObjectiveEvaluationRequestSchema(ma.Schema):
    adj_matrix = ma.fields.List(ma.fields.List(ma.fields.Float()))
    counts = ma.fields.Dict(keys=ma.fields.Str(), values=ma.fields.Float())
    objFun = ma.fields.Str()
    visualization = ma.fields.Boolean()
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)
