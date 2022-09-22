import marshmallow as ma


class ObjectiveEvaluationRequest:
    def __init__(self, counts, objFun, objFun_hyperparameters={}, visualization=False):
        self.counts = counts
        self.objFun = objFun
        self.visualization = visualization
        self.objFun_hyperparameters = objFun_hyperparameters


class TSPObjectiveEvaluationRequest(ObjectiveEvaluationRequest):
    def __init__(
        self, adj_matrix, counts, objFun, objFun_hyperparameters={}, visualization=False
    ):
        super().__init__(counts, objFun, objFun_hyperparameters, visualization)
        self.adj_matrix = adj_matrix


class TSPObjectiveEvaluationRequestSchema(ma.Schema):
    adj_matrix = ma.fields.List(ma.fields.List(ma.fields.Float()), required=True)
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    objFun = ma.fields.Str(required=True)
    visualization = ma.fields.Boolean(required=False)
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)


class MaxCutObjectiveEvaluationRequest(ObjectiveEvaluationRequest):
    def __init__(
        self, adj_matrix, counts, objFun, objFun_hyperparameters={}, visualization=False
    ):
        super().__init__(counts, objFun, objFun_hyperparameters, visualization)
        self.adj_matrix = adj_matrix


class MaxCutObjectiveEvaluationRequestSchema(ma.Schema):
    adj_matrix = ma.fields.List(ma.fields.List(ma.fields.Float()), required=True)
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    objFun = ma.fields.Str(required=True)
    visualization = ma.fields.Boolean(required=False)
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)
