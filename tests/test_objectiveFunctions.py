import unittest
import os, sys
import json
import re

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from app import create_app


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_expectation_value(self):
        response = self.client.post(
            "/objective/max-cut",
            data=json.dumps(
                {
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
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_CVaR_value(self):
        response = self.client.post(
            "/objective/max-cut",
            data=json.dumps(
                {
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
                    "objFun": "CVaR",
                    "visualization": "True",
                    "objFun_hyperparameters": {"alpha": 0.5},
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_Gibbs_value(self):
        response = self.client.post(
            "/objective/max-cut",
            data=json.dumps(
                {
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
                    "objFun": "Gibbs",
                    "visualization": "True",
                    "objFun_hyperparameters": {"eta": 0.2},
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
