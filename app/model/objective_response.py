from datetime import datetime
import marshmallow as ma
from .objective_request import TSPObjectiveEvaluationRequestSchema
import json


class ObjectiveResponse:
    def __init__(self, objective_value, costs, visualization):
        super().__init__()
        self.objective_value = objective_value
        self.costs = costs
        self.visualization = visualization
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def to_json(self):
        json_objective_response = {
            "objective_value": self.objective_value,
            "costs": json.loads(json.dumps(self.costs)),
            "visualization": self.visualization,
            "timestamp": self.timestamp,
        }
        return json_objective_response


class ObjectiveResponseSchema(ma.Schema):
    objective_value = ma.fields.Float()
    costs = ma.fields.List(ma.fields.Dict(keys=ma.fields.Str(), values=ma.fields.Raw()))
    visualization = ma.fields.String()
    timestamp = ma.fields.String()
