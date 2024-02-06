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


class KnapsackObjectiveEvaluationRequest(ObjectiveEvaluationRequest):
    def __init__(
        self,
        items,
        max_weights,
        counts,
        objFun,
        objFun_hyperparameters={},
        visualization=False,
    ):
        super().__init__(counts, objFun, objFun_hyperparameters, visualization)
        self.items = items
        self.max_weights = max_weights


class KnapsackObjectiveEvaluationRequestSchema(ma.Schema):
    items = ma.fields.List(
        ma.fields.Dict(keys=ma.fields.Str(), values=ma.fields.Float(), required=True),
        required=True,
    )
    max_weights = ma.fields.Float(required=True)
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    objFun = ma.fields.Str(required=True)
    visualization = ma.fields.Boolean(required=False)
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)


class ShorDiscreteLogObjectiveEvaluationRequest(ObjectiveEvaluationRequest):
    def __init__(
        self,
        b,
        g,
        p,
        counts,
        objFun,
        r=-1,
        n=-1,
        objFun_hyperparameters={},
        visualization=False,
    ):
        super().__init__(counts, objFun, objFun_hyperparameters, visualization)
        self.b = b
        self.g = g
        self.p = p
        self.n = n
        self.r = r


class ShorDiscreteLogObjectiveEvaluationRequestSchema(ma.Schema):
    b = ma.fields.Integer(required=True)
    g = ma.fields.Integer(required=True)
    p = ma.fields.Integer(required=True)
    n = ma.fields.Integer(required=False)
    r = ma.fields.Integer(required=False)
    counts = ma.fields.Dict(
        keys=ma.fields.Str(), values=ma.fields.Float(), required=True
    )
    objFun = ma.fields.Str(required=True)
    visualization = ma.fields.Boolean(required=False)
    objFun_hyperparameters = ma.fields.Dict(keys=ma.fields.Str(), required=False)
