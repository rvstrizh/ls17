import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/tours", methods=['GET'])
def get_tours():
    data = [
        {"id": 1, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 2, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 3, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 4, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
    ]
    return json.dumps(data), 200


@app.route("/tour", methods=['GET'])
def get_tour_by_id():
    sid = request.args.get("id")
    data = [
        {"id": 1, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 2, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 3, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
        {"id": 4, "f1": "value", "f2": 1, "f3": 4.5, "f4": True, "f5": [1, 3, 4, 5]},
    ]
    for d in data:
        if d["id"] == sid:
            return json.dumps(d)
    return "", 404


@app.route("/tours/add", methods=['POST'])
def create_tour():
    # add logic
    return "", 301


@app.route("/tour", methods=['POST'])
def update_tour():
    id = request.args.get("id")
    f1 = request.args.get("f1")
    if id is None or f1 is None:
        return "", 400
    # update logic
    return "", 200


@app.route("/tour/delete", methods=['GET'])
def delete_tour():
    id = request.args.get("id")
    # delete logic
    return "", 201
