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

    def test_tsp(self):
        response = self.client.post(
            "/objective/tsp",
            data=json.dumps(
                {
                    "adj_matrix": [
                        [0, 15, 16, 7],
                        [8, 0, 5, 1],
                        [10, 6, 0, 3],
                        [12, 3, 1, 0],
                    ],
                    "counts": {
                        "0001010000101000": 3,
                        "0010010010000001": 11,
                        "0001100001000010": 1,
                        "0001100000100100": 43,
                        "0001001010000100": 41,
                        "1000000100100100": 6,
                        "0100001010000001": 41,
                        "0100100000100001": 12,
                        "0010010000011000": 58,
                        "0001001001001000": 493,
                        "1000010000010010": 20,
                        "0001010010000010": 7,
                        "0010000110000100": 76,
                        "0010100000010100": 2,
                        "0010000101001000": 3,
                        "0100000100101000": 5,
                        "1000001001000001": 1,
                        "0100001000011000": 4,
                        "0100100000010010": 41,
                        "0010100001000001": 17,
                        "1000010000100001": 74,
                        "1000001000010100": 6,
                        "1000000101000010": 59,
                    },
                    "objFun": "Expectation",
                    "visualization": "True",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_tsp2(self):
        response = self.client.post(
            "/objective/tsp",
            data=json.dumps(
                {
                    "adj_matrix": [
                        [0, 9, 4, 15],
                        [10, 0, 4, 17],
                        [1, 11, 0, 3],
                        [18, 8, 19, 0],
                    ],
                    "counts": {
                        "0001010000101000": 3,
                        "0010010010000001": 11,
                        "0001100001000010": 1,
                        "0001100000100100": 43,
                        "0001001010000100": 41,
                        "1000000100100100": 6,
                        "0100001010000001": 41,
                        "0100100000100001": 12,
                        "0010010000011000": 58,
                        "0001001001001000": 493,
                        "1000010000010010": 20,
                        "0001010010000010": 7,
                        "0010000110000100": 76,
                        "0010100000010100": 2,
                        "0010000101001000": 3,
                        "0100000100101000": 5,
                        "1000001001000001": 1,
                        "0100001000011000": 4,
                        "0100100000010010": 41,
                        "0010100001000001": 17,
                        "1000010000100001": 74,
                        "1000001000010100": 6,
                        "1000000101000010": 59,
                    },
                    "objFun": "Expectation",
                    "visualization": "True",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_max_cut(self):
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
                        "100000": 11,
                        "100001": 5,
                        "100010": 12,
                        "100011": 14,
                        "100100": 15,
                        "100101": 12,
                        "100110": 18,
                        "100111": 17,
                        "101000": 17,
                        "101001": 24,
                        "101010": 9,
                        "101011": 10,
                        "101100": 22,
                        "101101": 17,
                        "101110": 15,
                        "101111": 14,
                        "110000": 14,
                        "110001": 11,
                        "110010": 15,
                        "110011": 11,
                        "110100": 12,
                        "110101": 10,
                        "110110": 11,
                        "110111": 15,
                        "111000": 13,
                        "111001": 9,
                        "111010": 14,
                        "111011": 12,
                        "111100": 9,
                        "111101": 13,
                        "111110": 9,
                        "111111": 17,
                        "000000": 15,
                        "000001": 10,
                        "000010": 9,
                        "000011": 14,
                        "000100": 8,
                        "000101": 10,
                        "000110": 14,
                        "000111": 17,
                        "001000": 10,
                        "001001": 4,
                        "001010": 8,
                        "001011": 14,
                        "001100": 15,
                        "001101": 11,
                        "001110": 19,
                        "001111": 4,
                        "010000": 11,
                        "010001": 12,
                        "010010": 10,
                        "010011": 12,
                        "010100": 16,
                        "010101": 12,
                        "010110": 13,
                        "010111": 10,
                        "011000": 7,
                        "011001": 8,
                        "011010": 15,
                        "011011": 13,
                        "011100": 13,
                        "011101": 10,
                        "011110": 14,
                        "011111": 15,
                    },
                    "objFun": "Expectation",
                    "visualization": "True",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_knapsack(self):
        response = self.client.post(
            "/objective/knapsack",
            data=json.dumps(
                {
                    "items": [
                        {"value": 5, "weight": 2},
                        {"value": 2, "weight": 1},
                        {"value": 3, "weight": 2},
                    ],
                    "max_weights": 20,
                    "counts": {
                        "100000": 30,
                        "100001": 10,
                        "110000": 50,
                        "011110": 20,
                        "010110": 40,
                    },
                    "objFun": "Expectation",
                    "visualization": "True",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
